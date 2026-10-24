#!/usr/bin/env python3
"""从站点 tag 页面分页抓取题目（绕过 API 单关键词 100 条上限）。

站点 tag 页表格结构：<tr data-row-key="id"><td><a href="/question/id">标题</a></td>
<td>难度</td><td>标签</td></tr>
用法:
    python3 fetch_tags_page.py                # 抓默认标签列表
    python3 fetch_tags_page.py HTML 安全开发   # 指定标签
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from matching import match_keyword  # noqa: E402
from filters import is_frontend_question  # noqa: E402

POOL_FILE = os.path.join(HERE, "data", "pool.json")
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}
PAGE_SIZE = 20
MAX_PAGES = 10

DEFAULT_TAGS = [
    "HTML", "HTML5", "网站安全", "安全开发", "密码学", "XSS", "CSRF",
    "Echarts", "Canvas", "可视化", "数据可视化", "性能优化", "前端性能优化",
    "CSS", "CSS3", "布局", "伪类", "CSS动画", "TypeScript", "GraphQL",
    "WebAssembly", "H5 移动端开发", "H5 适配", "H5 基础", "H5 触摸事件",
    "H5 性能优化", "H5 兼容性", "H5 混合开发", "移动端适配", "响应式",
    "设计模式", "架构", "架构设计", "组件设计", "前端系统设计", "前端场景",
    "前端手写代码", "前端兼容性", "前端包管理", "前端脚手架", "前端模块化",
    "前端部署", "React Native", "Electron", "Flutter", "Next.js",
    "网络协议", "计算机网络", "HTTP", "HTTPS", "DNS", "缓存", "WebSocket",
    "SSE", "Node.js", "Express", "Koa", "Webpack", "Vite", "Babel",
    "React", "Vue", "JavaScript", "Promise", "算法", "数据结构", "异步",
]

ROW_RE = re.compile(
    r'<tr[^>]*data-row-key="([0-9a-zA-Z]+)"[^>]*>(.*?)</tr>', re.S
)
LINK_RE = re.compile(r'href="/question/([0-9a-zA-Z]+)"[^>]*>(.*?)</a>', re.S)
TAG_RE = re.compile(r'<span[^>]*class="ant-tag[^"]*"[^>]*>([^<]+)</span>')


def fetch_html(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", "ignore")


def parse_rows(html):
    """解析表格行 -> [(id, title, [tags])]"""
    out = []
    for m in ROW_RE.finditer(html):
        qid, body = m.group(1), m.group(2)
        link = LINK_RE.search(body)
        if not link:
            continue
        title = re.sub(r"<[^>]+>", "", link.group(2))
        title = re.sub(r"\s+", " ", title).strip()
        if not title:
            continue
        tags = [t.strip() for t in TAG_RE.findall(body)]
        out.append((qid, title, tags))
    return out


def main():
    tags = sys.argv[1:] or DEFAULT_TAGS
    pool_list = json.load(open(POOL_FILE, encoding="utf-8"))
    pool = {q["id"]: q for q in pool_list}
    total_added = 0
    for tag in tags:
        added_tag = 0
        for page in range(1, MAX_PAGES + 1):
            url = (
                f"https://www.mianshiya.com/tag/{urllib.parse.quote(tag)}"
                f"?current={page}&pageSize={PAGE_SIZE}"
            )
            try:
                html = fetch_html(url)
            except Exception as exc:  # noqa: BLE001
                print(f"  [{tag}] 第 {page} 页失败: {exc}")
                break
            rows = parse_rows(html)
            if not rows:
                break
            for qid, title, row_tags in rows:
                if qid in pool:
                    continue
                qtags = [t for t in row_tags if t and t not in ("VIP", "普通")]
                if tag not in qtags:
                    qtags.insert(0, tag)
                if not is_frontend_question({"title": title, "tags": qtags}, match_keyword):
                    continue
                pool[qid] = {
                    "id": qid,
                    "title": title,
                    "tags": qtags,
                    "difficulty": None,
                    "viewNum": 0,
                    "favourNum": 0,
                    "needVip": None,
                    "url": f"https://www.mianshiya.com/question/{qid}",
                }
                added_tag += 1
            if len(rows) < PAGE_SIZE:
                break
            time.sleep(0.15)
        if added_tag:
            print(f"  [{tag}] 新增 {added_tag} 题")
            total_added += added_tag
        time.sleep(0.2)
    questions = sorted(pool.values(), key=lambda q: q["id"])
    with open(POOL_FILE, "w", encoding="utf-8") as fp:
        json.dump(questions, fp, ensure_ascii=False, indent=1)
    print("总计新增", total_added, "-> 题池", len(questions))


if __name__ == "__main__":
    main()

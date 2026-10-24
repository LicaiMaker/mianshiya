#!/usr/bin/env python3
"""按标题关键词深挖补池（翻到第 5 页），只保留通过前端判定的题目。"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from fetch_pool import search, merge_records  # noqa: E402
from matching import match_keyword  # noqa: E402
from filters import is_frontend_question  # noqa: E402

POOL_FILE = os.path.join(HERE, "data", "pool.json")
PAGE_SIZE = 20
MAX_PAGES = 5

KEYWORDS = [
    # HTML / DOM
    "语义化", "DOCTYPE", "标签", "meta", "iframe", "表单", "属性", "SVG", "Canvas",
    "DOM", "BOM", "节点", "querySelector", "事件流", "冒泡", "捕获", "事件委托",
    "自定义元素", "Shadow DOM", "无障碍", "aria", "alt", "srcset", "loading",
    "defer", "async", "SEO", "Web Components", "slot", "template",
    # 安全
    "XSS", "CSRF", "CSP", "点击劫持", "同源策略", "httpOnly", "SameSite", "密码",
    "加盐", "哈希", "JWT", "OAuth", "鉴权", "认证", "脱敏", "水印", "防盗链",
    "注入", "转义", "校验", "沙箱", "混合内容", "中间人", "白名单", "签名", "权限",
    "风控", "密钥", "cookie", "token", "正则", "HTTPS", "TLS", "证书", "指纹",
    # 可视化
    "ECharts", "图表", "可视化", "WebGL", "着色器", "粒子", "画布", "像素", "折线图",
    "柱状图", "饼图", "雷达图", "大屏", "坐标系", "地图", "词云", "Three", "位图",
    "矢量", "路径", "裁剪", "绘制", "动画引擎",
    # 性能
    "性能", "优化", "首屏", "白屏", "懒加载", "代码分割", "Tree Shaking", "内存泄漏",
    "长列表", "虚拟列表", "骨架屏", "渲染阻塞", "关键渲染路径", "长任务", "帧率",
    "卡顿", "防抖", "节流", "缓存策略", "请求合并", "预渲染", "体积", "压缩",
    "监控上报", "重新渲染", "图片优化", "webp", "字体", "预加载",
    # 网络 / 浏览器
    "HTTP", "跨域", "CORS", "缓存", "Cookie", "Session", "TCP", "浏览器", "渲染",
    "Service Worker", "storage", "强缓存", "协商缓存", "请求头", "keep-alive", "DNS",
    "CDN", "代理", "反向代理", "WebSocket", "SSE", "QUIC", "重定向", "状态码",
    "三次握手", "拥塞控制", "流式", "URL", "抓包", "预连接", "预取", "报文",
]


def main():
    pool_list = json.load(open(POOL_FILE, encoding="utf-8"))
    pool = {q["id"]: q for q in pool_list}
    added_total = 0
    for kw in KEYWORDS:
        records = []
        for page in range(1, MAX_PAGES + 1):
            body = {"tagList": ["前端"], "title": kw, "current": page, "pageSize": PAGE_SIZE}
            try:
                res = search(body)
            except Exception as exc:  # noqa: BLE001
                print(f"  [kw:{kw}] 第 {page} 页失败: {exc}")
                break
            rows = res.get("records") or []
            records.extend(rows)
            if len(rows) < PAGE_SIZE:
                break
            time.sleep(0.08)
        # 只合并通过前端判定的题
        frontend = [r for r in records if is_frontend_question(
            {"title": (r.get("title") or "").strip(), "tags": r.get("tagList") or []},
            match_keyword)]
        added = merge_records(frontend, pool)
        added_total += added
        if added:
            print(f"  [kw:{kw}] 新增 {added} 题（候选 {len(records)}，前端命中 {len(frontend)}）")
        time.sleep(0.1)
    questions = sorted(pool.values(), key=lambda q: q["id"])
    with open(POOL_FILE, "w", encoding="utf-8") as fp:
        json.dump(questions, fp, ensure_ascii=False, indent=1)
    print("总计新增", added_total, "-> 题池", len(questions))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""补充抓取：针对题量不足的方向（HTML/DOM、安全、可视化、性能）用标题关键词扩池。"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from fetch_pool import search, merge_records  # noqa: E402

POOL_FILE = os.path.join(HERE, "data", "pool.json")

GROUPS = [
    ("html", ["前端"], [
        "HTML", "语义化", "DOCTYPE", "标签", "meta", "iframe", "表单", "属性",
        "SVG", "Canvas", "DOM", "BOM", "节点", "querySelector", "getElementById",
        "事件流", "冒泡", "捕获", "事件委托", "事件监听", "自定义元素", "Shadow",
        "无障碍", "aria", "alt", "srcset", "loading", "defer", "async",
    ]),
    ("sec", ["前端"], [
        "XSS", "CSRF", "CSP", "点击劫持", "同源策略", "httpOnly", "SameSite",
        "密码", "加盐", "哈希", "JWT", "OAuth", "鉴权", "认证", "敏感信息",
        "脱敏", "水印", "防盗链", "注入", "转义", "校验", "沙箱", "iframe 沙箱",
        "混合内容", "中间人", "白名单", "签名", "权限", "风控", "审计", "密钥",
        "cookie", "token", "正则", "拦截", "代理", "HTTPS", "TLS", "证书",
    ]),
    ("viz", ["前端"], [
        "Canvas", "SVG", "ECharts", "Echarts", "图表", "可视化", "WebGL", "Three",
        "着色器", "粒子", "画布", "像素", "折线图", "柱状图", "饼图", "雷达图",
        "大屏", "坐标系", "数据大屏", "地图", "词云", "流图",
    ]),
    ("perf", ["前端"], [
        "性能", "优化", "首屏", "白屏", "懒加载", "代码分割", "Tree Shaking",
        "内存泄漏", "长列表", "虚拟列表", "骨架屏", "渲染阻塞", "关键渲染路径",
        "长任务", "帧率", "卡顿", "防抖", "节流", "缓存策略", "请求合并",
        "预渲染", "SSR", "体积", "压缩", "监控上报", "重新渲染", "图片优化",
        "webp", "字体", "长任务", "线程", "预加载", "网络优化",
    ]),
    ("net", ["前端"], [
        "HTTP", "跨域", "CORS", "缓存", "Cookie", "Session", "TCP", "浏览器",
        "渲染", "Service Worker", "storage", "强缓存", "协商缓存", "请求头",
        "keep-alive", "DNS", "CDN", "代理", "反向代理", "WebSocket", "SSE",
        "QUIC", "重定向", "状态码", "三次握手", "拥塞控制", "流式", "首屏",
        "URL", "GET", "POST", "抓包", "network", "预连接", "预取", "头",
    ]),
]


def main():
    pool_list = json.load(open(POOL_FILE, encoding="utf-8"))
    pool = {q["id"]: q for q in pool_list}
    stats = {}
    for name, tags, kws in GROUPS:
        records = []
        for kw in kws:
            body = {"tagList": tags, "title": kw, "current": 1, "pageSize": 20}
            try:
                res = search(body)
            except Exception as exc:  # noqa: BLE001
                print(f"[{name}] 关键词 {kw} 失败: {exc}")
                continue
            records.extend(res.get("records", []) or [])
        new = merge_records(records, pool)
        stats[name] = new
        print(f"[{name}] 新增 {new} 题")
    questions = sorted(pool.values(), key=lambda q: q["id"])
    with open(POOL_FILE, "w", encoding="utf-8") as fp:
        json.dump(questions, fp, ensure_ascii=False, indent=1)
    print("总计新增", sum(stats.values()), "-> 题池", len(questions))


if __name__ == "__main__":
    main()

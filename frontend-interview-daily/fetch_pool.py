#!/usr/bin/env python3
"""抓取 面试鸭(mianshiya.com) 题库，建立前端面试题池。

用法:
    python3 fetch_pool.py            # 增量抓取（已存在的题目会跳过）
    python3 fetch_pool.py --force    # 清空重建
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

API = "https://api.mianshiya.com/api/question/search"
UA = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
PAGE_SIZE = 20
HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(HERE, "data")
POOL_FILE = os.path.join(DATA_DIR, "pool.json")

# 需要抓取的前端相关标签（来自面试鸭标签体系实测）
TAGS = [
    # 主力池
    "前端",
    # 语言
    "JavaScript", "TypeScript", "HTML", "HTML5", "CSS", "CSS3", "ES6",
    "作用域", "原型", "闭包", "对象", "数据类型", "异步编程", "Promise",
    # 框架
    "React", "React进阶", "React原理", "React基础", "React状态管理", "React工具",
    "Vue", "Vue进阶", "Vue基础", "Vue库", "Vue Router",
    "Redux", "状态管理", "Next.js",
    # Node / 服务端
    "Node.js", "Node框架", "Express", "Koa",
    # 工程化
    "前端工程化", "工程化", "Webpack", "Babel", "单元测试", "npm",
    # 前端细分场景
    "前端场景", "前端手写代码", "前端性能优化", "网络协议", "数据类型", "npm",
    # 浏览器 / 网络 / 安全
    "计算机网络", "HTTP", "HTTPS", "DNS", "代理", "CDN", "WebSocket",
    "网络安全", "网站安全",
    # 性能
    "性能优化", "前端性能优化",
    # 图形 / 可视化
    "Echarts", "可视化", "Canvas", "WebAssembly", "GraphQL",
    # 跨端 / 移动端
    "Flutter", "Electron", "鸿蒙", "移动端适配",
    # 架构 / 设计
    "设计模式", "数据结构", "算法", "布局",
]


def search(body, retries=4):
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(API, data=json.dumps(body).encode(), headers=UA)
            with urllib.request.urlopen(req, timeout=30) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            if payload.get("code") != 0:
                raise RuntimeError(payload.get("message"))
            return payload.get("data") or {}
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(1.2 * (attempt + 1))
    raise RuntimeError(f"search {body} failed: {last}")


def search_tag(tag, current, page_size=PAGE_SIZE):
    return search({"tagList": [tag], "current": current, "pageSize": page_size})


def merge_records(records, pool):
    added = 0
    for rec in records or []:
        qid = rec.get("id")
        if not qid or qid in pool:
            continue
        pool[qid] = {
            "id": qid,
            "title": (rec.get("title") or "").strip(),
            "tags": rec.get("tagList") or [],
            "difficulty": rec.get("difficulty"),
            "viewNum": rec.get("viewNum") or 0,
            "favourNum": rec.get("favourNum") or 0,
            "needVip": rec.get("needVip"),
            "url": f"https://www.mianshiya.com/question/{qid}",
        }
        added += 1
    return added


def fetch_tag(tag, pool, stats):
    page = 1
    total = None
    while True:
        data = search_tag(tag, page)
        records = data.get("records") or []
        if total is None:
            try:
                total = int(data.get("total") or 0)
            except (TypeError, ValueError):
                total = 0
        added = merge_records(records, pool)
        stats[tag] = stats.get(tag, 0) + added
        if len(records) < PAGE_SIZE or (total and page * PAGE_SIZE >= total):
            break
        page += 1
        time.sleep(0.12)
    return total or 0


def fetch_by_keyword(keyword, pool, stats, max_pages=5):
    """按标题关键词 + 「前端」标签补充题库，让小方向也有足够题量。"""
    page = 1
    while page <= max_pages:
        data = search({"tagList": ["前端"], "title": keyword, "current": page, "pageSize": PAGE_SIZE})
        records = data.get("records") or []
        added = merge_records(records, pool)
        stats[f"kw:{keyword}"] = stats.get(f"kw:{keyword}", 0) + added
        if len(records) < PAGE_SIZE:
            break
        page += 1
        time.sleep(0.12)
    return stats.get(f"kw:{keyword}", 0)


def fetch_by_text(keyword, pool, stats, max_pages=5):
    """按全文检索补充题库：命中面比标题检索更广，适合题量小的小方向。

    未登录时单次检索最多翻到第 5 页，因此对命中量大的关键词，
    额外按 difficulty(1~5) / needVip(0,1) 切片再翻页，突破单关键词 100 条上限。
    """
    key = f"text:{keyword}"
    records = []

    def run(body):
        try:
            data = search(body)
        except RuntimeError as exc:
            if "登录" in str(exc):
                return None
            raise
        rows = data.get("records") or []
        records.extend(rows)
        return rows, int(data.get("total") or 0)

    def sweep(body):
        page = 1
        while page <= max_pages:
            res = run(dict(body, current=page, pageSize=PAGE_SIZE))
            if res is None:
                return 0
            rows, total = res
            if len(rows) < PAGE_SIZE:
                break
            page += 1
            time.sleep(0.06)
        return total

    total = sweep({"tagList": ["前端"], "searchText": keyword})

    # 命中总量超过可翻页上限时，用难度 / VIP 切片继续深挖
    if total > max_pages * PAGE_SIZE:
        for diff in (1, 3, 5):
            sweep({"tagList": ["前端"], "searchText": keyword, "difficulty": diff})
        for vip in (0, 1):
            sweep({"tagList": ["前端"], "searchText": keyword, "needVip": vip})

    added = merge_records(records, pool)
    stats[key] = stats.get(key, 0) + added
    return stats[key]


# 全文检索关键词：针对题量较小的方向做扩量
EXPAND_KEYWORDS = [
    # HTML / 语义化
    "语义化", "HTML", "标签", "meta", "DOM", "iframe", "表单", "Web API", "无障碍",
    "HTML5", "自定义元素", "影子", "slot", "webcomponent", "富文本", "编辑器", "拖拽",
    "slot", "canvas", "svg", "doctype", "base", "history", "referrer", "预加载",
    # CSS / 布局
    "布局", "flex", "grid", "定位", "重排", "重绘", "层叠", "继承", "BFC", "居中", "响应式", "媒体查询",
    "flex", "grid", "sticky", "float", "clip-path", "transform", "transition", "animation",
    "变量", "自定义属性", "预处理器", "less", "sass", "tailwind", "原子化", "vw", "rem",
    # JS
    "原型链", "闭包", "this", "事件循环", "垃圾回收", "深拷贝", "模块化", "防抖", "节流",
    "宏任务", "微任务", "代理", "反射", "继承", "浅拷贝", "数组", "字符串", "正则", "类型转换",
    "symbol", "bigint", "promise", "async", "await", "generator", "iterator", "label", "包装函数",
    # TS
    "类型", "泛型", "类型体操", "类型推断", "装饰器", "枚举",
    "interface", "type", "never", "unknown", "any", "utility", "keyof", "infer", "readonly",
    "satisfies", "模板字符串", "声明文件", "d.ts", "类型收窄", "联合类型",
    # React
    "React", "Hook", "Fiber", "虚拟DOM", "Diff", "组件通信", "memo", "useMemo", "Suspense",
    "useEffect", "useState", "context", "reducer", "key", "受控", "非受控", "高阶组件",
    "渲染函数", "并发", "transition", "react18", "流式", "水合", "hydration", "服务端组件",
    # Vue
    "Vue", "响应式", "nextTick", "computed", "watch", "插槽", "keep-alive", "响应式原理",
    "setup", "组合式", "生命周期", "指令", "mixin", "pinia", "vuex", "ref", "reactive",
    "自定义指令", "渲染函数", "动态组件", "异步组件", "v-model", "provide", "inject",
    # Node / 数据层
    "Node", "Express", "Koa", "中间件", "SSR", "BFF", "Stream", "GraphQL", "路由",
    "事件循环", "定时器", "http", "https", "fs", "path", "buffer", "process", "全局对象",
    "会话", "restful", "缓存", "代理服务器", "反向代理", "api", "接口设计",
    # 工程化
    "构建", "打包", "vite", "webpack", "babel", "eslint", "monorepo", "脚手架", "CI", "发布",
    "loader", "plugin", "热更新", "hmr", "treeshaking", "代码分割", "source map", "sourcemap",
    "依赖管理", "pnpm", "yarn", "workspace", "版本", "lock", "npm", "发布流程", "灰度",
    # 网络 / 浏览器
    "HTTP", "跨域", "CORS", "缓存", "Cookie", "TCP", "DNS", "渲染", "Service Worker", "存储", "WebSocket",
    "udp", "quic", "http2", "http3", "keep-alive", "代理", "cdn", "预连接", "预取",
    "localstorage", "sessionstorage", "indexeddb", "缓存策略", "强缓存", "协商缓存", "请求头",
    # 性能
    "性能", "首屏", "懒加载", "代码分割", "内存泄漏", "长列表", "白屏",
    "渲染阻塞", "字体", "图片优化", "webp", "预加载", "关键渲染路径", "长任务", "帧率",
    "卡顿", "节流", "防抖", "虚拟列表", "骨架屏", "ssr", "缓存",
    # 安全
    "XSS", "CSRF", "安全", "加密", "鉴权", "点击劫持", "内容安全策略", "跨站", "劫持", "注入", "CSP", "SameSite",
    "同源策略", "httpOnly", "密码", "认证", "token", "中间人", "混合内容", "暴力破解",
    "渗透", "漏洞", "白名单", "黑名单", "输入校验", "转义", "沙箱", "iframe 沙箱", "签名", "jwt",
    # 可视化 / 图形
    "Canvas", "SVG", "Echarts", "图表", "WebGL", "可视化", "绘制", "Three", "动画", "折线图", "柱状图", "地图",
    "着色器", "像素", "路径", "坐标系", "裁剪", "粒子", "3d", "三维", "贴图", "渲染引擎",
    "图形", "几何", "贝塞尔", "矩阵", "变换", "离屏", "位图", "矢量", "交互式图表", "大屏",
    # 跨端
    "移动端", "小程序", "响应式", "适配", "Electron", "Flutter", "触摸事件", "Hybrid",
    "webview", "原生", "桥接", "capacitor", "cordova", "react native", "uni-app", "taro",
    "安全区", "刘海屏", "rem 适配", "手势", "滚动穿透",
    # 架构
    "设计模式", "架构", "微前端", "组件设计", "发布订阅", "观察者", "单例", "工厂模式", "依赖注入",
    "策略模式", "适配器", "装饰器", "代理模式", "命令模式", "迭代器", "状态模式", "职责",
    "分层", "解耦", "高内聚", "低耦合", "模块化设计", "组件库",
    # 算法
    "算法", "排序", "二分", "递归", "链表", "二叉树", "动态规划", "哈希", "图遍历", "栈", "队列",
    "数组去重", "快排", "归并", "堆排序", "拓扑排序", "最短路径", "贪心", "回溯",
    "字符串匹配", "滑动窗口", "双指针", "前缀树", "字典树", "位运算", "复杂度",
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="清空后重建题池")
    args = parser.parse_args()

    os.makedirs(DATA_DIR, exist_ok=True)
    pool = {}
    if os.path.exists(POOL_FILE) and not args.force:
        with open(POOL_FILE, encoding="utf-8") as fp:
            pool = {q["id"]: q for q in json.load(fp)}
    print(f"已有题目 {len(pool)} 条，开始增量抓取…")

    stats = {}
    for tag in TAGS:
        try:
            total = fetch_tag(tag, pool, stats)
            print(f"  [{tag}] 命中 {total} 条，本次新增 {stats.get(tag, 0)} 条")
        except Exception as exc:  # noqa: BLE001
            print(f"  [{tag}] 抓取失败: {exc}", file=sys.stderr)
        time.sleep(0.15)

    # 按方向关键词补充题量（标题命中 + 「前端」标签过滤）
    config_path = os.path.join(HERE, "directions.json")
    if os.path.exists(config_path):
        with open(config_path, encoding="utf-8") as fp:
            config = json.load(fp)
        keywords = []
        for direction in config.get("directions", []):
            for kw in direction.get("keywords", []):
                if kw not in keywords:
                    keywords.append(kw)
        print(f"按关键词补充题量（{len(keywords)} 个）…")
        for kw in keywords:
            try:
                added = fetch_by_keyword(kw, pool, stats)
                print(f"  [kw:{kw}] 新增 {added} 条")
            except Exception as exc:  # noqa: BLE001
                print(f"  [kw:{kw}] 抓取失败: {exc}", file=sys.stderr)
            time.sleep(0.12)

    # 全文检索扩量：补足题量较小的方向
    print(f"按全文检索扩量（{len(EXPAND_KEYWORDS)} 个）…")
    for kw in EXPAND_KEYWORDS:
        try:
            added = fetch_by_text(kw, pool, stats)
            print(f"  [text:{kw}] 新增 {added} 条")
        except Exception as exc:  # noqa: BLE001
            print(f"  [text:{kw}] 抓取失败: {exc}", file=sys.stderr)
        time.sleep(0.12)

    questions = sorted(pool.values(), key=lambda q: q["id"])
    with open(POOL_FILE, "w", encoding="utf-8") as fp:
        json.dump(questions, fp, ensure_ascii=False, indent=1)
    print(f"题池已保存：{POOL_FILE}（共 {len(questions)} 题）")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""按标题关键词检索补池（不带「前端」标签过滤）。

背景：
    api.mianshiya.com/api/question/search 传 tagList 时只能翻到第 5 页，
    且 tagList=["前端"] 会漏掉那些只挂了细分标签（如 HTML5、浏览器、渲染机制）
    的前端题。改成只传 title 关键词做全站标题检索，可以把这些题捞回来。

接口限制：pageSize <= 20，current <= 5（未登录），即每个关键词最多 100 条。

用法:
    python3 fetch_title.py            # 增量补池并写回
    python3 fetch_title.py --dry      # 只统计不写回
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from matching import match_keyword  # noqa: E402
from filters import is_frontend_question  # noqa: E402

API = "https://api.mianshiya.com/api/question/search"
UA = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
PAGE_SIZE = 20
MAX_PAGES = 5
POOL_FILE = os.path.join(HERE, "data", "pool.json")

# 前端各方向的高频标题关键词
KEYWORDS = [
    # HTML / DOM
    "HTML", "HTML5", "语义化", "DOCTYPE", "iframe", "meta", "DOM", "BOM",
    "事件流", "事件冒泡", "事件捕获", "事件委托", "Shadow DOM", "Web Components",
    "自定义元素", "标签的作用", "浏览器对象模型", "文档对象模型",
    # CSS
    "CSS", "Flex", "Grid", "定位", "盒模型", "BFC", "层叠", "继承", "居中",
    "重排", "重绘", "媒体查询", "伪类", "伪元素", "动画", "过渡", "变量",
    "响应式", "rem", "vw", "Tailwind", "Less", "Sass", "z-index", "float",
    "sticky", "transform", "line-height", "display",
    # JavaScript
    "JavaScript", "原型链", "闭包", "作用域", "变量提升", "this", "继承",
    "深拷贝", "浅拷贝", "防抖", "节流", "事件循环", "宏任务", "微任务",
    "Promise", "async", "await", "Proxy", "Reflect", "Symbol", "BigInt",
    "Generator", "迭代器", "模块化", "类型转换", "正则表达式", "垃圾回收",
    "数组", "字符串", "手写", "柯里化", "链式调用", "跨页面通信",
    # TypeScript
    "TypeScript", "类型体操", "泛型", "类型别名", "类型守卫", "类型推断",
    "接口", "枚举", "any", "unknown", "never", "tsconfig", "装饰器",
    # React
    "React", "Hook", "useEffect", "useMemo", "useCallback", "useReducer",
    "虚拟 DOM", "Diff", "Fiber", "setState", "组件通信", "Context",
    "Redux", "MobX", "Zustand", "Next.js", "SSR", "SSG", "ISR", "App Router",
    # Vue
    "Vue", "Vue3", "Composition API", "响应式原理", "computed", "watch",
    "watchEffect", "nextTick", "keep-alive", "插槽", "指令", "mixin",
    "Vuex", "Pinia", "Vue Router", "路由守卫", "Nuxt",
    # 工程化
    "Webpack", "Vite", "Babel", "ESLint", "Prettier", "Husky", "Monorepo",
    "pnpm", "npm", "yarn", "Tree Shaking", "代码分割", "按需加载", "懒加载",
    "打包", "构建", "CI/CD", "脚手架", "单元测试", "Git", "发布",
    # 浏览器与网络
    "HTTP", "HTTPS", "DNS", "CDN", "缓存", "跨域", "CORS", "代理", "Cookie",
    "Session", "Token", "JWT", "WebSocket", "SSE", "TCP", "浏览器", "渲染",
    "渲染机制", "重排重绘", "请求头", "状态码", "keep-alive", "网络请求",
    "fetch", "Axios", "拦截器", "首屏", "白屏",
    # 性能
    "性能优化", "内存泄漏", "懒加载", "预加载", "图片优化", "长列表", "虚拟列表",
    "Core Web Vitals", "缓存策略", "压缩", "雪崩", "抖动",
    # 安全
    "XSS", "CSRF", "CSP", "点击劫持", "同源策略", "httpOnly", "SameSite",
    "密码存储", "加盐", "哈希", "bcrypt", "JWT", "OAuth", "认证", "鉴权",
    "登录安全", "水印", "防盗链", "敏感信息",
    # 可视化与图形
    "ECharts", "Canvas", "SVG", "WebGL", "Three.js", "可视化", "图表",
    "数据可视化", "大屏", "着色器", "光栅化", "动画原理",
    # 跨端与移动端
    "移动端", "H5", "小程序", "uni-app", "Taro", "React Native", "Flutter",
    "Electron", "鸿蒙", "响应式", "适配", "触摸事件", "兼容性", "Safari",
    # 架构与设计模式
    "设计模式", "单例", "工厂", "观察者", "策略模式", "发布订阅", "代理模式",
    "微前端", "组件设计", "架构设计", "状态管理", "MVVM", "设计体系",
    # 算法
    "二分", "动态规划", "贪心", "双指针", "回溯", "哈希表", "二叉树",
    "链表", "图", "堆", "栈", "队列", "排序", "递归", "位运算",
    # 其他前端场景
    "拖拽", "富文本", "Markdown", "上传", "下载", "剪贴板", "无障碍",
    "国际化", "SEO", "埋点", "错误监控", "前端监控", "虚拟滚动",
    # 补强薄弱方向：HTML / DOM
    "语义化标签", "自定义元素", "Web Components", "表单", "input", "video 标签",
    "canvas 标签", "浏览器兼容", "怪异模式", "DOCTYPE", "srcset", "picture",
    # 补强薄弱方向：安全
    "跨站脚本", "脚本注入", "转义", "内容安全策略", "iframe 沙箱", "混合内容",
    "Cookie 属性", "会话劫持", "暴力破解", "钓鱼", "中间人攻击", "HTTPS",
    "TLS", "密钥", "数字签名", "加密算法", "密码", "权限控制", "越权",
    "安全头", "Referer", "CORS 预检", "SSRF", "文件上传安全",
    # 补强薄弱方向：性能
    "内存泄漏", "重排", "重绘", "关键渲染路径", "长任务", "帧率", "白屏时间",
    "首屏时间", "包体积", "体积优化", "SSR 性能", "缓存失效", "预连接",
    "prefetch", "preload", "骨架屏", "防抖节流", "虚拟列表", "合成层",
    # 补强薄弱方向：可视化
    "折线图", "柱状图", "饼图", "坐标系", "tooltip", "数据大屏", "桑基图",
    "雷达图", "热力图", "词云", "Canvas 绘制", "路径绘制", "图片处理", "离屏渲染",
    # 补强薄弱方向：工程化 / 架构
    "微前端", "qiankun", "模块联邦", "Monorepo", "工作区", "pnpm", "变化检测",
    "灰度发布", "source map", "按需加载", "动态导入", "预处理器", "PostCSS",
    "设计系统", "组件库设计", "状态管理方案", "MVVM", "依赖注入",
    # 补强薄弱方向：跨端
    "JSBridge", "WebView", "混合开发", "小程序性能", "原生", "鸿蒙", "HarmonyOS",
    "跨端方案", "安全区", "刘海屏", "rem 适配", "vw 适配",
]


def search(body, retries=3):
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
            time.sleep(1.0 * (attempt + 1))
    raise RuntimeError(f"search failed: {last}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()

    pool_list = json.load(open(POOL_FILE, encoding="utf-8"))
    pool = {q["id"]: q for q in pool_list}
    print(f"初始题池 {len(pool)}")

    total_added = 0
    for idx, kw in enumerate(KEYWORDS, 1):
        records = []
        for page in range(1, MAX_PAGES + 1):
            try:
                data = search({"title": kw, "current": page, "pageSize": PAGE_SIZE})
            except RuntimeError:
                break
            rows = data.get("records") or []
            records.extend(rows)
            if len(rows) < PAGE_SIZE:
                break
            time.sleep(0.1)
        added = 0
        for rec in records:
            qid = rec.get("id")
            if not qid or qid in pool:
                continue
            title = (rec.get("title") or "").strip()
            tags = rec.get("tagList") or []
            if not is_frontend_question({"title": title, "tags": tags}, match_keyword):
                continue
            pool[qid] = {
                "id": qid,
                "title": title,
                "tags": tags,
                "difficulty": rec.get("difficulty"),
                "viewNum": rec.get("viewNum") or 0,
                "favourNum": rec.get("favourNum") or 0,
                "needVip": rec.get("needVip"),
                "url": f"https://www.mianshiya.com/question/{qid}",
            }
            added += 1
        total_added += added
        if added:
            print(f"  [{idx}/{len(KEYWORDS)}] {kw}: +{added}")
        time.sleep(0.12)

    questions = sorted(pool.values(), key=lambda q: q["id"])
    print(f"总计新增 {total_added} -> 题池 {len(questions)}")
    if not args.dry:
        with open(POOL_FILE, "w", encoding="utf-8") as fp:
            json.dump(questions, fp, ensure_ascii=False, indent=1)
        print("已写回", POOL_FILE)


if __name__ == "__main__":
    main()

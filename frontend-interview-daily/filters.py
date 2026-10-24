#!/usr/bin/env python3
"""前端题目判定规则（clean_pool 与 daily 共用同一套过滤逻辑）。

判定思路：
  1) 硬丢弃：整题都属于非前端领域的标签（后端 / 运维 / 渗透 / 大数据 / 面经…）
  2) 标题硬丢弃：明确属于非前端技术主题的词（VPN / NAT / 零信任 / RSA…）
  3) 主题域白名单：网络 / 安全 / 密码学 / 游戏开发 这些「前端会问一部分」的领域，
     只有题干落在前端相关子话题上才保留（HTTP、缓存、XSS、密码存储…）
  4) 项目题：题干必须出现前端技术信号，否则视为项目背景 / 后端实现题
"""

# ---------------------------------------------------------------------------
# 1. 整题非前端：标签硬丢弃
# ---------------------------------------------------------------------------
HARD_DROP_TAGS = {
    # 后端 / 分布式 / 运维
    "后端", "运维", "DevOps", "Kubernetes", "分布式系统", "API网关", "网关",
    "容器", "Linux", "Oracle", "MySQL", "SQL", "Zookeeper",
    "消息队列", "Kafka", "RabbitMQ", "Elasticsearch", "数据库", "Swoole", "JMeter",
    "系统设计", "场景题", "网络故障排查", "网络配置", "防火墙", "网络安全",
    # AI / 机器学习 / 大模型
    "机器学习", "人工智能", "深度学习", "大模型", "LLM", "RAG", "AI",
    "Agent", "agent", "智能合约", "Web3 开发", "DApp 开发", "LangChain",
    # 安全运维 / 渗透测试
    "渗透测试", "渗透测试基础", "渗透测试流程", "信息收集", "OWASP", "横向移动",
    "内网", "免杀", "提权", "Burp", "Burp Suite", "Metasploit", "社工", "社会工程学",
    "钓鱼邮件", "白帽子", "Kali Linux", "Nmap", "安全伦理", "漏洞评级", "威胁建模",
    "最小权限原则", "安全基础", "安全开发基础", "漏洞", "SQL 注入", "SSRF", "XXE",
    "文件上传安全", "人机识别", "验证码", "SDL", "DevSecOps", "代码审计", "SAST",
    "DAST", "API 安全", "API 访问控制", "RESTful API", "DDoS 防御", "微服务安全",
    "零信任架构", "会话劫持", "API 访问",
    # 测试 / 数据 / 操作系统
    "软件测试", "Web测试", "接口测试", "测试工具", "测试基础理论", "Selenium",
    "自动化测试", "自动化", "移动端测试", "Appium", "数据分析", "大数据", "Flink",
    "Spark", "Hive", "Yarn", "Atlas", "Metacat", "Storm", "操作系统", "鸿蒙", "ArkUI",
    # 面经 / 招聘流程
    "面经", "校招", "实习", "社招", "得物",
    # 其他语言 / 平台（非 Web 前端）
    "Go", "Go基础", "Go并发", "Go底层原理", "Go面向对象", "Go标准库", "Go垃圾回收",
    "C#", "C#框架", ".NET", ".NET Core", "ASP.NET Core", "C 语言", "Rust",
    "PHP", "PHP框架", "Scala", "WPF", "Dubbo", "Dubbo配置", "Yaf", "Java",
    "Java 基础", "Shell", "脚本编写", "Solidity", "Dart", "Android",
    "Android进阶", "Android基础", "Android UI", "Android原理", "Android组件",
    "Android性能优化", "Android网络通信", "Android库", "华为OD", "408考研",
    "通用", "智力题", "计算智力题", "策略智力题", "凑数智力题", "游戏智力题",
}

# ---------------------------------------------------------------------------
# 2. 标题硬丢弃：明确属于非前端技术主题的词
#    ASCII 词走词边界匹配（见 matching.match_keyword），避免 "java" 误伤 JavaScript
# ---------------------------------------------------------------------------
HARD_DROP_TITLE = [
    # 后端语言 / 框架 / 中间件
    "java", "spring", "springboot", "mybatis", "redis", "kafka", "netty", "jvm",
    "hadoop", "hive", "flink", "spark", "elasticsearch", "mongodb", "oracle",
    "mysql", "postgres", "微服务", "shardingsphere", "dockerfile", "nginx",
    "shell 脚本", "centos", "linux 命令", "python", "django", "flask", "php",
    "golang", "c++", "c#", "swift", "kotlin", "objective-c",
    "laravel", "swoole", "jmeter", "appium", "deveco studio",
    "sql 注入", "反序列化漏洞", "命令注入", "xxe", "提权", "内网渗透", "免杀",
    "横向移动", "信息收集", "burp", "metasploit", "挖矿", "勒索", "ddos",
    "arp 欺骗", "ospf", "bgp", "vlan", "白帽子", "灰帽子", "黑帽子",
    "机学习", "深度学习", "神经网络", "rag", "bi 报表",
    "分布式", "容器化", "集群", "高可用", "熔断", "限流", "分布式锁", "消息队列",
    "最终一致", "幂等",
    # 网络工程 / 运维
    "VPN", "SDN", "MPLS", "NAT", "LDAP", "SIP 协议", "TFTP", "PPP 协议",
    "IGMP", "Radius", "TACACS", "NTP 协议", "DHCP", "FTP 协议", "SMTP",
    "IMAP", "Telnet", "SNMP", "云计算", "边缘计算", "5G", "SD-WAN",
    "网络功能虚拟化", "网络虚拟化", "网络中立性", "带宽管理", "智能网络管理",
    "子网掩码", "网络掩码", "广播域", "碰撞域", "ARP 协议", "ICMP", "MTU",
    "RIP 协议", "路由协议", "IP 地址", "网络层", "区块链",
    # 安全工程 / 后端安全
    "零信任", "SDL（", "DevSecOps", "代码审计", "SAST", "DAST", "API 安全",
    "RESTful API 的安全", "SSRF", "会话劫持",
    # 后端密码学
    "RSA", "AES", "椭圆曲线", "ECC", "填充模式", "PKCS1", "OAEP", "密钥管理",
    "对称加密", "非对称加密", "公钥加密", "数字证书", "消息认证码",
    "哈希碰撞", "初始向量", "密钥分发", "对称加密算法", "加密模式",
    # 游戏服务端
    "游戏服务器", "游戏服务端", "长连接服务器", "心跳包", "KCP", "AOI",
    "百万玩家", "弱网环境", "Nagle", "IO 多路复用", "负载均衡策略",
    # 开发工具 / IDE（非前端面试题）
    "Live Templates", "JetBrains",
]

# 命中上面的词、但确实属于前端场景的例外
TITLE_KEEP_EXCEPTIONS = [
    "部署前端项目",
    "反向代理做转发",
    "前端如何",
    "前端性能",
    "ECharts",
]

# ---------------------------------------------------------------------------
# 3. 主题域白名单：标签 -> (前端相关子话题词表)
#    题目命中该域标签时，必须命中词表之一才保留
# ---------------------------------------------------------------------------
NET_KEEP_WORDS = [
    "HTTP", "HTTP2", "HTTP3", "HTTP 1.0", "HTTP 2", "HTTP 3", "HTTPS", "TLS", "SSL",
    "TCP", "UDP", "三次握手", "四次挥手", "粘包", "拆包", "拥塞控制", "滑动窗口",
    "可靠传输", "超时重传", "快速重传", "SACK", "ISN", "初始序列号", "TIME_WAIT",
    "SYN", "CDN", "DNS", "Cookie", "Session", "Token", "JWT", "跨域", "CORS",
    "代理", "反向代理", "缓存", "状态码", "请求头", "keep-alive", "QUIC",
    "WebSocket", "SSE", "Socket", "OSI", "四层模型", "七层模型", "TCP/IP",
    "端口", "鉴权", "认证", "登录", "网络攻击", "攻击", "网址", "网络请求",
    "AJAX", "fetch", "预取", "预连接", "流式", "断点续传", "报文", "首部",
    "网络性能", "抓包", "浏览器", "渲染",
]

SEC_KEEP_WORDS = [
    "XSS", "CSRF", "CSP", "内容安全策略", "点击劫持", "同源", "httpOnly", "SameSite",
    "密码存储", "加盐", "哈希", "hash", "MD5", "bcrypt", "scrypt", "Argon2",
    "JWT", "OAuth", "认证", "鉴权", "登录", "前端", "水印", "防盗链", "正则",
    "调试", "控制台", "混淆", "敏感", "脱敏", "握手", "验证码", "越权", "注入",
]

GAME_KEEP_WORDS = [
    "DDA", "Bresenham", "光栅化", "渲染", "Canvas", "WebGL", "图形", "像素",
    "着色器", "延迟加载", "数学",
]

DOMAIN_RULES = {
    "计算机网络": NET_KEEP_WORDS,
    "网络协议": NET_KEEP_WORDS,
    "网络": NET_KEEP_WORDS,
    "网络通信": NET_KEEP_WORDS,
    "网络请求": NET_KEEP_WORDS,
    "网络优化": NET_KEEP_WORDS,
    "安全开发": SEC_KEEP_WORDS,
    "密码学": SEC_KEEP_WORDS,
    "游戏开发": GAME_KEEP_WORDS,
}

# ---------------------------------------------------------------------------
# 4. 前端技术信号词：项目题（题干带「项目」）必须命中其一
# ---------------------------------------------------------------------------
FRONTEND_TECH_WORDS = [
    "前端", "JavaScript", "TypeScript", "Vue", "React", "Angular", "Svelte",
    "HTML", "CSS", "DOM", "组件", "路由", "状态管理", "性能", "打包", "构建",
    "部署", "脚手架", "工程化", "渲染", "页面", "布局", "样式", "交互", "组件库",
    "响应式", "移动端", "小程序", "跨端", "Electron", "Flutter", "React Native",
    "Canvas", "SVG", "WebGL", "ECharts", "图表", "可视化", "Markdown", "拖拽",
    "上传", "下载", "表单", "登录", "权限", "缓存", "跨域", "接口", "请求",
    "拦截器", "Axios", "埋点", "SEO", "Hook", "Hooks", "生命周期", "事件",
    "动画", "防抖", "节流", "懒加载", "代码分割", "SSR", "水合", "Tree Shaking",
    "单元测试", "ESLint", "Prettier", "Husky", "Git", "npm", "pnpm", "yarn",
    "Monorepo", "WebSocket", "SSE", "流式", "打字机", "沙箱", "iframe", "选择器",
    "XSS", "CSRF", "同源", "Cookie", "Token", "JWT", "OAuth", "源码", "规范",
    "微前端", "设计模式", "架构", "导航", "菜单", "搜索", "OpenAPI", "Umi",
    "Ant Design", "Arco Design", "Element UI", "Monaco", "ByteMD", "bytemd",
    "markmap", "Next.js", "Nuxt", "webpack", "vite", "babel", "虚拟 DOM", "虚拟DOM",
    "Fiber", "Diff", "setState", "computed", "watch", "setup", "插槽", "指令",
    "mixin", "nextTick", "keep-alive", "路由守卫", "树 shaking", "按需加载",
    "Node.js", "node_modules", "package.json", "package-lock", "依赖", "全局",
    "预览", "滚动", "实时", "封装", "token",
]

# 项目题允许「靠标签判定前端」的强标签
STRONG_FRONTEND_TAGS = {
    "前端", "前端工程化", "前端性能优化", "前端场景", "前端手写代码", "前端系统设计",
    "前端部署", "前端包管理", "前端脚手架", "前端模块化", "前端兼容性", "前端库",
    "vue", "react", "typescript", "javascript", "html", "css", "next.js", "nuxt",
    "vue router", "vuex", "redux", "pinia", "状态管理", "组件", "组件设计",
    "架构设计", "设计模式", "工程化", "webpack", "vite", "babel", "eslint",
    "husky", "npm", "前端兼容性",
}


def _hits(title, words, match_keyword):
    return any(match_keyword(title, w) for w in words)


def is_frontend_question(question, match_keyword):
    """返回 True 表示该题属于前端面试题范畴。"""
    tags = {t.lower() for t in question.get("tags", [])}
    title = question["title"]

    # 1) 硬丢弃标签
    if tags & {t.lower() for t in HARD_DROP_TAGS}:
        return False

    # 2) 例外白名单（前端部署 / 反向代理 / 项目里的前端子问题）
    if any(k in title for k in TITLE_KEEP_EXCEPTIONS):
        return True

    # 3) 标题硬丢弃
    if _hits(title, HARD_DROP_TITLE, match_keyword):
        return False

    # 4) 主题域白名单
    for tag, words in DOMAIN_RULES.items():
        if tag.lower() in tags and not _hits(title, words, match_keyword):
            return False

    # 5) 项目题：必须有前端技术信号
    if "项目" in title:
        if _hits(title, FRONTEND_TECH_WORDS, match_keyword):
            return True
        return bool(tags & STRONG_FRONTEND_TAGS)

    return True

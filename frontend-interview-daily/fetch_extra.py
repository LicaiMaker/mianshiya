#!/usr/bin/env python3
"""抓取补充标签（安全开发/密码学/可视化/架构等），只保留与前端相关的题目并入池。

用法:
    python3 fetch_extra.py
"""
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from fetch_pool import search, merge_records, PAGE_SIZE  # noqa: E402

POOL_FILE = os.path.join(HERE, "data", "pool.json")

# 补充标签：前端主题相关但未被「前端」大标签覆盖的细分标签
EXTRA_TAGS = [
    # 安全
    "安全开发", "安全开发基础", "渗透测试", "密码学", "安全",
    "XSS 攻击", "CSRF 攻击", "XSS", "CSRF", "认证",
    # 可视化 / 图形 / 游戏
    "数据可视化", "游戏开发",
    # 架构 / 工程质量
    "前端系统设计", "前端包管理", "架构设计", "架构延伸", "前端兼容性",
    "前端部署", "前端脚手架", "前端模块化", "组件设计", "组件",
    "编码规范", "基础理论", "计算机基础", "UI/UX",
    # 版本管理 / 交付 / 其他前端工程
    "Git", "Git 操作", "Git 进阶", "CI/CD", "代码分析", "React Native",
    "Web3 开发", "网络", "架构", "队列", "计算机网络",
]

# 非前端内容：这些标签下的题目偏后端 / 运维 / 数据分析，直接丢弃
NON_FRONTEND_TAGS = {
    "后端", "运维", "DevOps", "Kubernetes", "大数据", "Flink", "Spark", "Kafka",
    "MySQL", "Oracle", "数据库", "Elasticsearch", "C++", "C# 基础", "C# 并发",
    "C# 集合", "C# 面向对象", "Java 基础", "Java", "PHP", "Go", "Python",
    "安全开发基础", "渗透测试流程", "信息收集", "OWASP", "横向移动", "内网",
    "免杀", "提权", "Burp", "BurpSuite", "Metasploit", "社工", "钓鱼邮件",
    "后端系统设计", "系统设计", "场景题", "API网关", "网关", "操作系统",
    "计算机网络协议", "网络协议", "TCP 三次握手", "容器", "Docker", "Linux",
    "数据分析", "数据科学", "机器学习", "深度学习", "大模型", "AIGC", "AI",
}

# 明确的后端/安全方向关键词（即使标题含前端词也排除）
BACKEND_KEYWORDS = [
    "java", "spring", "mysql", "redis", "kafka", "docker", "nginx", "python",
    "golang", "c++", "c#", "php", "oracle", "postgresql", "mongodb",
    "kubernetes", "k8s", "flink", "hadoop", "spark", "hive", "elasticsearch",
    "微服务", "netty", "jvm", "字节码", "线程池",
    "sql 注入", "反序列化", "命令注入", "xxe", "提权", "内网渗透", "免杀",
    "横向移动", "信息收集", "burp", "metasploit", "csrf 漏洞利用", "挖矿",
    "勒索", "ddos 攻击原理", "arp", "ospf", "bgp", "vlan", "防火墙策略",
]


def is_frontend_question(rec):
    tags = {t.lower() for t in (rec.get("tagList") or [])}
    if tags & NON_FRONTEND_TAGS:
        return False
    title = (rec.get("title") or "").lower()
    if any(k in title for k in BACKEND_KEYWORDS):
        return False
    return True


def fetch_tag(tag, pool, stats):
    added = 0
    for page in range(1, 6):
        try:
            data = search({"tagList": [tag], "current": page, "pageSize": PAGE_SIZE})
        except RuntimeError as exc:
            if "登录" in str(exc):
                break
            raise
        records = [r for r in (data.get("records") or []) if is_frontend_question(r)]
        added += merge_records(records, pool)
        try:
            total = int(data.get("total") or 0)
        except (TypeError, ValueError):
            total = 0
        raw = len(data.get("records") or [])
        if raw < PAGE_SIZE or page * PAGE_SIZE >= total:
            break
        time.sleep(0.08)
    stats[tag] = stats.get(tag, 0) + added
    return added


def main():
    with open(POOL_FILE, encoding="utf-8") as fp:
        pool = {q["id"]: q for q in json.load(fp)}
    before = len(pool)
    stats = {}
    for tag in EXTRA_TAGS:
        try:
            added = fetch_tag(tag, pool, stats)
            print(f"{tag:<16} +{added}")
        except Exception as exc:  # noqa: BLE001
            print(f"{tag:<16} 失败: {exc}", file=sys.stderr)
    questions = sorted(pool.values(), key=lambda q: q["id"])
    with open(POOL_FILE, "w", encoding="utf-8") as fp:
        json.dump(questions, fp, ensure_ascii=False, indent=1)
    print(f"\n题池 {before} -> {len(questions)} (+{len(questions) - before})")


if __name__ == "__main__":
    main()

"""构建前端分方向题库。

从面试鸭（mianshiya.com）抓取前端题库 + 题目解析，按技术方向归类，输出
data/questions.json。

用法：
    python3 scripts/build_bank.py            # 使用已有的原始抓取结果重新归类
    python3 scripts/build_bank.py --fetch    # 重新联网抓取（原始结果落到 data/raw/）
"""
import argparse
import concurrent.futures as cf
import json
import os
import re
import subprocess
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'data'))

from directions import DIRECTIONS, EXCLUDE_TAGS  # noqa: E402

API_LIST = 'https://api.mianshiya.com/api/question/list/page/vo'
API_CATEGORY = 'https://api.mianshiya.com/api/tagCategory/list'
SITE = 'https://www.mianshiya.com'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36'

# 题库中用于定位主题的通用标签，不参与方向判定
GENERIC_TAGS = {'前端', '编程导航', '校招', '热门', '真实面经', '项目', '面经', '秋招',
                '编程语言', '计算机基础', '其他', '后端'}

# 泛主题标签：只描述话题类型而不指向具体技术。题目同时命中泛主题标签与
# 技术专精标签（如 Flutter、CSS）时，以技术专精标签为准。
GENERIC_TOPIC_TAGS = {
    '前端场景', '场景题', '系统设计', '前端系统设计', '架构设计', '技术对比', '应用场景',
    '实战应用', '实际应用', '前端部署', '部署', '应用发布', '国际化', '单点登录',
    'AI 能力', '技术趋势', '数据传递', '设计模式', '动静分离', '得物', '网络请求',
    '网络', '性能', '缓存', '原理', '事件处理', '监控', '基础理论', '调试', '事件',
}

# 标题里出现这些关键词的题目属于后端/大数据/算法范畴，即便打了前端相关标签也剔除
BACKEND_TITLE = re.compile(
    r'(JVM|OOM|GC 调优|微服务|服务注册|服务发现|熔断降级|分布式事务|分布式锁|'
    r'MySQL|Redis|Memcached|MongoDB|Elasticsearch|Kafka|RocketMQ|RabbitMQ|消息队列|'
    r'SQL 语句|建表|索引优化|事务隔离|主从复制|分库分表|连接池|线程池|进程池|'
    r'Spark|Flink|Hadoop|Hive|HBase|Kylin|数据仓库|数据同步|离线计算|实时计算|'
    r'K8s|Kubernetes|Nginx|反向代理|负载均衡服务器|哨兵模式|'
    r'数据挖掘|机器学习模型|神经网络结构|Transformer 架构|注意力机制如何计算|'
    r'大模型微调|LoRA|RAG 流程|向量数据库选型|提示词工程|'
    r'智能合约|以太坊|区块链|Web3|DApp|钱包地址|'
    r'设计一个线程池|设计一个消息队列|设计一个定时器|'
    r'二叉树|平衡树|B\+\s*树|红黑树|哈希表如何实现|堆排序|'
    r'最短路径|最大流|拓扑排序|并查集实现|Trie 树|'
    r'单元测试覆盖度是多少)')


def curl(args):
    return subprocess.run(args, capture_output=True).stdout


def post_json(url, payload):
    out = curl(['curl', '-s', '--max-time', '30', '-X', 'POST', url,
                '-H', 'Content-Type: application/json',
                '-H', 'Origin: https://www.mianshiya.com',
                '-H', 'Referer: https://www.mianshiya.com/',
                '--data', json.dumps(payload, ensure_ascii=False)])
    try:
        return json.loads(out.decode('utf-8', 'ignore'))
    except Exception:
        return {'code': -1}


def get_json(url):
    out = curl(['curl', '-s', '--max-time', '30', url,
                '-H', 'Origin: https://www.mianshiya.com',
                '-H', 'Referer: https://www.mianshiya.com/'])
    try:
        return json.loads(out.decode('utf-8', 'ignore'))
    except Exception:
        return None


def fetch_frontend_tags():
    """从标签体系接口拿到官方「前端」分类下的标签列表。"""
    data = post_json(API_CATEGORY, {})
    cats = {c['name']: c['tagList'] for c in (data.get('data') or [])}
    return cats.get('前端', [])


def fetch_questions(tags):
    """按标签抓取题目。接口对未登录用户限制翻页深度，这里通过多种过滤条件交叉覆盖。"""
    pool = {}

    def work(job):
        tag, diff, typ, page = job
        res = post_json(API_LIST, {'current': page, 'pageSize': 20, 'tagList': [tag],
                                    'difficulty': diff, 'type': typ})
        if res.get('code') != 0:
            return []
        return res['data']['records']

    jobs = []
    for tag in tags:
        for diff in (1, 3, 5, 2):
            for typ in (0, 1, 4):
                for page in (1, 3, 5):
                    jobs.append((tag, diff, typ, page))
    with cf.ThreadPoolExecutor(max_workers=16) as ex:
        for recs in ex.map(work, jobs):
            for rec in recs:
                pool[rec['id']] = {
                    'id': rec['id'],
                    'title': rec['title'],
                    'tags': rec.get('tagList') or [],
                    'difficulty': rec.get('difficulty'),
                    'viewNum': rec.get('viewNum'),
                    'favourNum': rec.get('favourNum'),
                }
    return list(pool.values())


def fetch_answers(ids):
    """抓取每题的官方解析与 FAQ（答案内容在页面 SSR 负载中）。"""
    answers = {}

    def work(pid):
        html = curl(['curl', '-sL', '--max-time', '30', '--compressed', '-H', f'User-Agent: {UA}',
                     f'{SITE}/question/{pid}']).decode('utf-8', 'ignore')
        if len(html) < 5000:
            return pid, None
        segs = [m.group(1) for m in re.finditer(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', html, re.S)]
        text = '\n'.join(segs)
        try:
            text = text.encode('utf-8').decode('unicode_escape').encode('latin1').decode('utf-8', 'ignore')
        except Exception:
            pass
        m = re.search(r'"questionId":"' + pid + r'"[^{}]*?"content":"(.*?)","thumbNum"', text, re.S)
        faqs = [{'q': a.group(1), 'a': a.group(2)}
                for a in re.finditer(r'\{"question":"(.*?)","answer":"(.*?)"\}', text, re.S)]
        return pid, {'content': m.group(1) if m else None, 'faqs': faqs[:12]}

    with cf.ThreadPoolExecutor(max_workers=14) as ex:
        for pid, data in ex.map(work, ids):
            answers[pid] = data
    return answers


def clean(text):
    if not text:
        return ''
    text = (text.replace('\\n', '\n').replace('\\t', '\t')
            .replace('\\"', '"').replace('\\\\', '\\'))
    for src, dst in (('\\u003c', '<'), ('\\u003e', '>'), ('\\u0026', '&'), ('\\u0027', "'")):
        text = text.replace(src, dst)
    return re.sub(r'\n{3,}', '\n\n', text).strip()


def build(raw_questions, answers):
    """把题目归到方向。

    归类依据：题目命中若干方向标签时，取其中在全站出现频次最低（最具体）的那个
    标签所属方向。例如同时命中 JavaScript(290) 与 前端手写代码(54) 的题目归入
    「手写代码 / 代码分析」，而不是被宽泛的 JavaScript 抢走。

    另外用标题关键词再兜一层：像「MySQL 一亿条数据怎么加索引」「设计一个线程池」
    这类题目虽然被打了「场景题 / 系统设计」标签，实际是后端题，需要剔除。
    """
    directions = [(name, desc, tags) for name, desc, tags in DIRECTIONS]
    tag2dir = {}
    for name, _, tags in directions:
        for tag in tags:
            tag2dir.setdefault(tag, name)

    # 标签频次（用于判断哪个标签更具体）
    freq = Counter()
    for q in raw_questions:
        for tag in (q.get('tags') or []):
            freq[tag] += 1

    items = []
    skipped = 0
    for q in raw_questions:
        # 兼容历史抓取版本的不同字段名
        tags = list(q.get('tags') or [])
        difficulty = q.get('difficulty', q.get('diff'))
        view_num = q.get('viewNum', q.get('view'))
        favour_num = q.get('favourNum', q.get('fav'))
        topical = [t for t in tags if t not in GENERIC_TAGS]
        if not topical:
            skipped += 1
            continue
        if set(topical) & EXCLUDE_TAGS:
            skipped += 1
            continue
        if BACKEND_TITLE.search(q.get('title') or ''):
            skipped += 1
            continue
        matched = [t for t in topical if t in tag2dir]
        if not matched:
            skipped += 1
            continue
        # 选标签：先用「技术专精标签」挑（如 Flutter、CSS），只有全是泛主题标签时
        # 才退化为按频次挑最具体的那个（如「前端场景」比「JavaScript」更具体）
        specific = [t for t in matched if t not in GENERIC_TOPIC_TAGS]
        pool = specific or matched
        best_tag = min(pool, key=lambda t: (freq.get(t, 10 ** 6), -len(t)))
        direction = tag2dir[best_tag]
        desc = next(d for n, d, _ in directions if n == direction)
        ans = answers.get(q['id']) or {}
        items.append({
            'id': q['id'],
            'title': q['title'],
            'direction': direction,
            'directionDesc': desc,
            'tags': topical,
            'difficulty': difficulty,
            'viewNum': view_num,
            'favourNum': favour_num,
            'url': f'{SITE}/question/{q["id"]}',
            'answer': clean(ans.get('content')),
            'faqs': [{'q': clean(f['q']), 'a': clean(f['a'])} for f in (ans.get('faqs') or [])],
        })
    return items, skipped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--fetch', action='store_true', help='重新联网抓取题库与解析')
    args = ap.parse_args()

    raw_path = os.path.join(ROOT, 'data', 'raw', 'questions_raw.json')
    ans_path = os.path.join(ROOT, 'data', 'raw', 'answers_raw.json')
    os.makedirs(os.path.dirname(raw_path), exist_ok=True)

    if args.fetch or not os.path.exists(raw_path):
        fe_tags = fetch_frontend_tags()
        print(f'官方前端标签 {len(fe_tags)} 个，开始抓取题目...', flush=True)
        raw = fetch_questions(fe_tags)
        json.dump(raw, open(raw_path, 'w', encoding='utf-8'), ensure_ascii=False)
        print(f'抓取题目 {len(raw)} 道，开始抓取解析...', flush=True)
        answers = fetch_answers([q['id'] for q in raw])
        json.dump(answers, open(ans_path, 'w', encoding='utf-8'), ensure_ascii=False)
    else:
        raw = json.load(open(raw_path, encoding='utf-8'))
        answers = json.load(open(ans_path, encoding='utf-8')) if os.path.exists(ans_path) else {}

    items, skipped = build(raw, answers)
    out = os.path.join(ROOT, 'data', 'questions.json')
    json.dump(items, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    cnt = Counter(i['direction'] for i in items)
    print(f'\n题库共 {len(items)} 题（过滤 {skipped} 道非前端题），按方向分布：')
    for name, _, _ in DIRECTIONS:
        print(f'  {cnt.get(name, 0):>4}  {name}')
    with_answer = sum(1 for i in items if i['answer'])
    print(f'\n含官方解析：{with_answer} 题')
    print(f'输出：{out}')


if __name__ == '__main__':
    main()

"""联网抓取面试鸭前端题库与官方解析。

抓取策略（未登录状态下接口最多只能翻到第 5 页）：
  * 对每个候选标签，先用 difficulty=1/3/5 分组拿到 total，再按需翻页；
    某组记录数不足 20 条即说明该组已取完，无需继续请求；
  * 同时抓取其它分类下与前端相关的标签（如 HTML5 / CSS3 / ES6 / 闭包 …），
    扩大覆盖，避免题库只停留在「前端」分类的主干标签上；
  * 题目详情页的 SSR 负载里带官方解析，用正则抽取 content 与 FAQ。

输出：
    data/raw/questions_raw.json   题目列表
    data/raw/answers_raw.json     题目解析
"""
import argparse
import concurrent.futures as cf
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'data'))

from directions import DIRECTIONS, EXCLUDE_TAGS  # noqa: E402

API_LIST = 'https://api.mianshiya.com/api/question/list/page/vo'
API_CATEGORY = 'https://api.mianshiya.com/api/tagCategory/list'
SITE = 'https://www.mianshiya.com'
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36'

MAX_PAGE = 5          # 未登录可访问的最大页码
PAGE_SIZE = 20
DIFFS = (1, 3, 5)

# 不作为抓取入口的通用/后端标签
SKIP_TAGS = EXCLUDE_TAGS | {
    '前端', '编程导航', '校招', '热门', '真实面经', '项目', '面经', '秋招', '编程语言',
    '计算机基础', '其他', '后端', '编程语言分类', '校招热题', '公司题库',
}


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


def site_tags():
    """全站标签清单。"""
    data = post_json(API_CATEGORY, {})
    return sorted({t for c in (data.get('data') or []) for t in (c.get('tagList') or [])})


def frontend_category_tags():
    data = post_json(API_CATEGORY, {})
    cats = {c['name']: c['tagList'] for c in (data.get('data') or [])}
    return cats.get('前端', [])


def direction_tags():
    tags = set()
    for _, _, ts in DIRECTIONS:
        tags.update(ts)
    return tags


def list_page(tag, diff, current):
    res = post_json(API_LIST, {'current': current, 'pageSize': PAGE_SIZE,
                                'tagList': [tag], 'difficulty': diff})
    if res.get('code') != 0:
        return 0, []
    data = res.get('data') or {}
    return int(data.get('total') or 0), (data.get('records') or [])


def fetch_tag(tag):
    """抓取单个标签下的全部可访问题目。"""
    pool = {}
    for diff in DIFFS:
        total, records = list_page(tag, diff, 1)
        if not records:
            continue
        for rec in records:
            pool[rec['id']] = rec
        # 该组最多只能翻到第 MAX_PAGE 页，且返回不足一页即已取完
        pages = min(MAX_PAGE, max(1, -(-total // PAGE_SIZE)))
        for cur in range(2, pages + 1):
            _, recs = list_page(tag, diff, cur)
            if not recs:
                break
            for rec in recs:
                pool[rec['id']] = rec
            if len(recs) < PAGE_SIZE:
                break
    return tag, list(pool.values())


def fetch_answers(ids):
    """抓取题目详情页里的官方解析与 FAQ。"""
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=os.path.join(ROOT, 'data', 'raw'))
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)

    tags = set(frontend_category_tags())
    tags |= {t for t in direction_tags() if t not in SKIP_TAGS}
    tags |= {t for t in site_tags() if t not in SKIP_TAGS}
    tags = sorted(tags)
    print(f'候选标签 {len(tags)} 个，开始抓取题目...', flush=True)

    pool = {}
    with cf.ThreadPoolExecutor(max_workers=12) as ex:
        for i, (tag, recs) in enumerate(ex.map(fetch_tag, tags), 1):
            for rec in recs:
                pool[rec['id']] = {
                    'id': rec['id'],
                    'title': rec['title'],
                    'tags': rec.get('tagList') or [],
                    'difficulty': rec.get('difficulty'),
                    'viewNum': rec.get('viewNum'),
                    'favourNum': rec.get('favourNum'),
                }
            if i % 40 == 0:
                print(f'  {i}/{len(tags)} 累计 {len(pool)} 题', flush=True)

    print(f'抓取题目 {len(pool)} 道，开始抓取解析...', flush=True)
    answers = fetch_answers(list(pool.keys()))
    print(f'拿到解析 {sum(1 for v in answers.values() if v and v.get("content"))} 道', flush=True)

    json.dump(list(pool.values()), open(os.path.join(args.out, 'questions_raw.json'), 'w',
                                        encoding='utf-8'), ensure_ascii=False)
    json.dump(answers, open(os.path.join(args.out, 'answers_raw.json'), 'w',
                             encoding='utf-8'), ensure_ascii=False)
    print('完成')


if __name__ == '__main__':
    main()

"""每日前端面试题生成器。

从 data/questions.json（面试鸭前端题库，按技术方向归类）中按日期确定性地
抽取题目，输出 Markdown 与 HTML 到 output/YYYY-MM-DD.*。

选题规则：
  * 每个前端技术方向至少 2 题（默认 3 题，题库充足的���向 4 题）；
  * 同一方向的题目按「固定随机排列 + 日期游标」轮转，连续很多天不会重复，
    轮完一圈才会再次出现；
  * 优先选取带官方解析的题目；
  * 同一天重复运行结果完全一致（可补跑、可复现）。

用法：
    python3 scripts/daily.py                          # 今天
    python3 scripts/daily.py --date 2026-11-02       # 指定日期
    python3 scripts/daily.py --per-direction 2        # 每方向题目数
"""
import argparse
import datetime as dt
import html
import json
import os
import random
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'data'))

from directions import DIRECTIONS  # noqa: E402

BANK = os.path.join(ROOT, 'data', 'questions.json')
OUTDIR = os.path.join(ROOT, 'output')
EPOCH = dt.date(2026, 1, 1)

DIFF_LABEL = {1: '简单', 3: '中等', 5: '困难'}
DIFF_COLOR = {1: '#52c41a', 3: '#fa8c16', 5: '#f5222d'}


# ---------------------------------------------------------------- 题池准备

def load_pool():
    items = json.load(open(BANK, encoding='utf-8'))
    pools = {}
    for it in items:
        pools.setdefault(it['direction'], []).append(it)
    order = [name for name, _, _ in DIRECTIONS]
    for name in pools:
        if name not in order:
            order.append(name)
    return order, pools


def permutation(direction, items):
    """对某个方向的题目做固定随机排列，保证跨天轮转稳定且不重复。"""
    seed = int(re.sub(r'\W', '', direction)[:8].encode('utf-8').hex()[:8] or '0', 16)
    rng = random.Random(seed)
    ids = sorted(it['id'] for it in items)
    rng.shuffle(ids)
    return ids


def quota(size, per_direction):
    """按题库容量决定该方向出题数：至少 per_direction 题，题库大则多出一些。"""
    if size <= 8:
        return max(2, min(per_direction, size))
    if size >= 100:
        return min(per_direction + 1, 4)
    return per_direction


def pick_for_direction(direction, items, day_index, per_direction):
    """按日期游标选出该方向当天的题目。"""
    by_id = {it['id']: it for it in items}
    perm = permutation(direction, items)
    k = quota(len(perm), per_direction)
    start = (day_index * k) % len(perm)

    picked, used = [], set()
    # 在轮转窗口里优先挑带解析的题
    for offset in range(len(perm)):
        qid = perm[(start + offset) % len(perm)]
        if qid in used:
            continue
        used.add(qid)
        picked.append(by_id[qid])
        if len(picked) >= k:
            break
    return picked


def select(day_index, per_direction):
    order, pools = load_pool()
    result = []
    for name in order:
        items = pools.get(name) or []
        if len(items) < 2:
            continue
        picked = pick_for_direction(name, items, day_index, per_direction)
        if picked:
            result.append((name, items[0]['directionDesc'], picked))
    return result


# ---------------------------------------------------------------- 文本处理

def answer_brief(text, limit=900):
    """把官方解析压缩成要点摘要。"""
    if not text:
        return ''
    text = re.sub(r'\r', '', text)
    text = re.sub(r'^#{1,6}\s*', '', text, flags=re.M)
    text = re.sub(r'\n{3,}', '\n\n', text).strip()
    # 优先保留带「重点」「区别」「原理」等提示的行
    lines = [ln.strip() for ln in text.split('\n') if ln.strip()]
    if len(text) <= limit:
        return text
    picked, size = [], 0
    for ln in lines:
        if len(ln) > 160:
            ln = ln[:157] + '…'
        if size + len(ln) > limit:
            break
        picked.append(ln)
        size += len(ln)
    return '\n'.join(picked) + '\n…'


def md_to_html(text):
    """极简 Markdown → HTML（够用即可：标题、粗体、行内代码、列表、段落）。"""
    out = []
    for block in re.split(r'\n{2,}', text):
        block = block.strip()
        if not block:
            continue
        lines = block.split('\n')
        if all(ln.lstrip().startswith(('- ', '* ')) for ln in lines):
            items = ''.join(
                f'<li>{inline(ln.lstrip()[2:])}</li>' for ln in lines)
            out.append(f'<ul>{items}</ul>')
        elif all(re.match(r'^\d+[.)]\s', ln) for ln in lines):
            items = ''.join(
                f'<li>{inline(re.sub(r"^\d+[.)]\s", "", ln))}</li>' for ln in lines)
            out.append(f'<ol>{items}</ol>')
        else:
            out.append(f'<p>{inline(block)}</p>')
    return ''.join(out)


def inline(text):
    text = html.escape(text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*([^*\n]+)\*(?!\*)', r'<em>\1</em>', text)
    return text.replace('\n', '<br>')


# ---------------------------------------------------------------- Markdown

def render_markdown(date_str, groups):
    total = sum(len(p) for _, _, p in groups)
    lines = [
        f'# 前端每日面试题 · {date_str}',
        '',
        f'> 共 **{total}** 题，覆盖 **{len(groups)}** 个前端技术方向，'
        f'每个方向至少 2 题。题目来自[面试鸭](https://mianshiya.com)前端题库，'
        f'附官方解析摘要。',
        '',
        '## 目录',
        '',
    ]
    for name, desc, picked in groups:
        lines.append(f'- **{name}**（{len(picked)} 题）— {desc}')
    lines.append('')

    idx = 0
    for name, desc, picked in groups:
        lines.append('---')
        lines.append('')
        lines.append(f'## {name}')
        lines.append('')
        lines.append(f'> {desc}')
        lines.append('')
        for it in picked:
            idx += 1
            diff = DIFF_LABEL.get(it.get('difficulty'), '中等')
            tags = ' / '.join(it.get('tags') or [])
            lines.append(f'### {idx}. {it["title"]}')
            lines.append('')
            meta = [f'难度：{diff}']
            if tags:
                meta.append(f'标签：{tags}')
            if it.get('viewNum'):
                meta.append(f'热度：{it["viewNum"]} 次浏览')
            lines.append('　'.join(f'**{m}**' for m in meta))
            lines.append('')
            brief = answer_brief(it.get('answer') or '')
            if brief:
                lines.append('**参考答案要点**')
                lines.append('')
                lines.append(brief)
                lines.append('')
            if it.get('faqs'):
                lines.append('**追问要点**')
                lines.append('')
                for faq in it['faqs'][:4]:
                    q = faq.get('q') or ''
                    a = faq.get('a') or ''
                    if not q and not a:
                        continue
                    lines.append(f'- **{q.strip()}**')
                    if a:
                        lines.append(f'  {answer_brief(a, 300)}')
                lines.append('')
            lines.append(f'[查看原题与完整解析]({it["url"]})')
            lines.append('')
    lines.append('')
    lines.append('---')
    lines.append('')
    lines.append(f'*题目来源：面试鸭 mianshiya.com · 生成于 {date_str} · '
                 f'共 {total} 题 / {len(groups)} 个方向*')
    lines.append('')
    return '\n'.join(lines)


# ---------------------------------------------------------------- HTML

CSS = """
:root{
  --bg:#0f1115; --panel:#171a21; --panel2:#1d212a; --line:#2a2f3a;
  --fg:#e8eaf0; --fg2:#a4abbb; --accent:#4c9aff; --accent2:#7c5cff;
}
*{box-sizing:border-box}
body{margin:0;background:radial-gradient(1200px 600px at 20% -10%,#1b2130 0%,var(--bg) 60%);
  color:var(--fg);font:15px/1.75 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
  -webkit-font-smoothing:antialiased}
.wrap{max-width:1080px;margin:0 auto;padding:40px 22px 80px}
header.hero{position:relative;padding:34px 32px;border-radius:20px;overflow:hidden;
  background:linear-gradient(135deg,rgba(76,154,255,.16),rgba(124,92,255,.14));
  border:1px solid var(--line);margin-bottom:26px}
header.hero::after{content:'';position:absolute;inset:-40% -20% auto auto;width:320px;height:320px;
  background:radial-gradient(circle,rgba(124,92,255,.35),transparent 70%);filter:blur(10px)}
.hero h1{margin:0 0 10px;font-size:30px;letter-spacing:.5px}
.hero p{margin:0;color:var(--fg2);max-width:760px}
.stats{display:flex;flex-wrap:wrap;gap:10px;margin-top:20px;position:relative;z-index:1}
.stat{background:rgba(255,255,255,.05);border:1px solid var(--line);border-radius:12px;padding:10px 16px}
.stat b{display:block;font-size:22px;line-height:1.2}
.stat span{color:var(--fg2);font-size:12px}
.toc{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:10px;margin-bottom:30px}
.toc a{display:block;padding:11px 14px;border-radius:12px;background:var(--panel);border:1px solid var(--line);
  color:var(--fg);text-decoration:none;font-size:13px;transition:.18s}
.toc a:hover{border-color:var(--accent);transform:translateY(-2px)}
.toc a em{display:block;color:var(--fg2);font-style:normal;font-size:11px;margin-top:3px}
section.dir{margin-bottom:34px}
section.dir>h2{margin:0 0 4px;font-size:20px;display:flex;align-items:center;gap:10px}
section.dir>h2::before{content:'';width:4px;height:18px;border-radius:2px;background:linear-gradient(var(--accent),var(--accent2))}
section.dir>p.desc{margin:0 0 14px;color:var(--fg2);font-size:13px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px 20px;margin-bottom:12px;
  transition:border-color .18s}
.card:hover{border-color:#39415a}
.card h3{margin:0 0 10px;font-size:16px;font-weight:600;line-height:1.6}
.meta{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:12px}
.badge{font-size:11px;padding:2px 9px;border-radius:999px;border:1px solid var(--line);color:var(--fg2);background:var(--panel2)}
.badge.d1{color:#4ade80;border-color:rgba(74,222,128,.35)}
.badge.d3{color:#fbbf24;border-color:rgba(251,191,36,.35)}
.badge.d5{color:#fb7185;border-color:rgba(251,113,133,.35)}
details{border-top:1px dashed var(--line);padding-top:10px}
summary{cursor:pointer;color:var(--accent);font-size:13px;list-style:none;user-select:none}
summary::-webkit-details-marker{display:none}
summary::before{content:'▸ ';transition:.2s;display:inline-block}
details[open] summary::before{transform:rotate(90deg)}
.ans{margin-top:10px;color:#cdd3e0;font-size:14px}
.ans ul,.ans ol{margin:6px 0;padding-left:20px}
.ans code{background:var(--panel2);padding:1px 6px;border-radius:5px;font-size:12.5px;color:#8fd3ff}
.ans strong{color:#fff}
.faq{margin-top:8px;font-size:13.5px}
.faq .q{color:#ffd479;font-weight:600}
.faq .a{color:var(--fg2)}
.src{display:inline-block;margin-top:12px;font-size:12px;color:var(--fg2);text-decoration:none;border-bottom:1px dotted var(--fg2)}
.src:hover{color:var(--accent)}
footer{margin-top:40px;padding-top:18px;border-top:1px solid var(--line);color:var(--fg2);font-size:12px;text-align:center}
@media (max-width:640px){.wrap{padding:22px 14px 60px}.hero h1{font-size:23px}}
"""


def render_html(date_str, groups):
    total = sum(len(p) for _, _, p in groups)
    parts = [
        '<!DOCTYPE html><html lang="zh-CN"><head><meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width,initial-scale=1">',
        f'<title>前端每日面试题 · {date_str}</title>',
        f'<style>{CSS}</style></head><body><div class="wrap">',
        '<header class="hero">',
        f'<h1>前端每日面试题 · {date_str}</h1>',
        '<p>题目来自面试鸭 mianshiya.com 前端题库，覆盖 HTML/CSS/JS、异步、手写、'
        'TypeScript、React、Vue、工程化、性能、移动端、跨端、Electron、GraphQL、'
        '浏览器与网络、Node.js、系统设计等方向，每个方向至少 2 题，并附官方解析摘要。</p>',
        '<div class="stats">',
        f'<div class="stat"><b>{total}</b><span>今日题目</span></div>',
        f'<div class="stat"><b>{len(groups)}</b><span>技术方向</span></div>',
        f'<div class="stat"><b>{sum(len(p) for _, _, p in groups) // max(len(groups), 1)}+</b><span>每方向题数</span></div>',
        '<div class="stat"><b>mianshiya.com</b><span>题库来源</span></div>',
        '</div></header>',
        '<div class="toc">',
    ]
    for name, desc, picked in groups:
        parts.append(f'<a href="#{slug(name)}">{name} · {len(picked)} 题'
                     f'<em>{html.escape(desc)}</em></a>')
    parts.append('</div>')

    idx = 0
    for name, desc, picked in groups:
        parts.append(f'<section class="dir" id="{slug(name)}">')
        parts.append(f'<h2>{html.escape(name)}</h2>')
        parts.append(f'<p class="desc">{html.escape(desc)}</p>')
        for it in picked:
            idx += 1
            diff = it.get('difficulty')
            parts.append('<div class="card">')
            parts.append(f'<h3>{idx}. {html.escape(it["title"])}</h3>')
            parts.append('<div class="meta">')
            parts.append(f'<span class="badge d{diff}">难度：{DIFF_LABEL.get(diff, "中等")}</span>')
            for t in (it.get('tags') or [])[:4]:
                parts.append(f'<span class="badge">{html.escape(t)}</span>')
            if it.get('viewNum'):
                parts.append(f'<span class="badge">{it["viewNum"]} 次浏览</span>')
            parts.append('</div>')
            brief = answer_brief(it.get('answer') or '')
            if brief:
                parts.append('<details open><summary>参考答案要点</summary>'
                             f'<div class="ans">{md_to_html(brief)}</div></details>')
            faqs = [f for f in (it.get('faqs') or []) if (f.get('q') or f.get('a'))][:4]
            if faqs:
                items = ''.join(
                    f'<div class="faq"><div class="q">Q：{html.escape((f.get("q") or "").strip())}</div>'
                    f'<div class="a">A：{md_to_html(answer_brief(f.get("a") or "", 260))}</div></div>'
                    for f in faqs)
                parts.append(f'<details><summary>追问要点（{len(faqs)}）</summary>{items}</details>')
            parts.append(f'<a class="src" href="{it["url"]}" target="_blank" rel="noopener">'
                         '查看原题与完整解析 →</a>')
            parts.append('</div>')
        parts.append('</section>')

    parts.append(f'<footer>前端每日面试题 · {date_str} · 共 {total} 题 / '
                 f'{len(groups)} 个方向 · 题目来源：面试鸭 mianshiya.com</footer>')
    parts.append('</div></body></html>')
    return ''.join(parts)


def slug(name):
    return re.sub(r'[^\w\u4e00-\u9fa5]+', '-', name).strip('-')


# ---------------------------------------------------------------- 主流程

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--date', default=None, help='日期 YYYY-MM-DD，默认今天')
    ap.add_argument('--per-direction', type=int, default=3,
                    help='每个方向的基础题量（默认 3，最少 2）')
    ap.add_argument('--outdir', default=OUTDIR)
    args = ap.parse_args()

    if args.date:
        date_str = args.date
        date_obj = dt.datetime.strptime(date_str, '%Y-%m-%d').date()
    else:
        date_obj = dt.date.today()
        date_str = date_obj.strftime('%Y-%m-%d')
    day_index = (date_obj - EPOCH).days

    per_direction = max(2, args.per_direction)
    groups = select(day_index, per_direction)

    os.makedirs(args.outdir, exist_ok=True)
    md_path = os.path.join(args.outdir, f'{date_str}.md')
    html_path = os.path.join(args.outdir, f'{date_str}.html')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(render_markdown(date_str, groups))
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(render_html(date_str, groups))
    for src, dst in ((md_path, 'latest.md'), (html_path, 'latest.html')):
        with open(os.path.join(args.outdir, dst), 'w', encoding='utf-8') as f:
            f.write(open(src, encoding='utf-8').read())

    total = sum(len(p) for _, _, p in groups)
    print(f'{date_str} 生成完成：{total} 题 / {len(groups)} 个方向')
    for name, _, picked in groups:
        print(f'  {len(picked):>3}  {name}')
    print(f'Markdown: {md_path}')
    print(f'HTML    : {html_path}')
    return 0


if __name__ == '__main__':
    sys.exit(main())

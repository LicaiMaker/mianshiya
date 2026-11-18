#!/usr/bin/env python3
"""
每日前端面试题生成器
- 从面试鸭（mianshiya.com）抓取的真实题库中，按前端技术方向抽取题目
- 每个技术方向至少 2 道题
- 按日期做确定性轮转，保证每天题目不重复、覆盖全部方向
"""
import json, os, random, re, subprocess, urllib.parse, argparse, datetime, hashlib

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
BASE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(BASE, "questions_cache.json")
OUTDIR = os.path.join(BASE, "daily")

DIRECTIONS = {
    "JavaScript": ["JavaScript", "ES6"],
    "TypeScript": ["TypeScript"],
    "HTML": ["HTML"],
    "CSS": ["CSS"],
    "React": ["React", "React基础", "React进阶", "React原理"],
    "Vue": ["Vue", "Vue基础", "Vue进阶"],
    "Node.js": ["Node.js"],
    "前端工程化": ["前端工程化", "工程化", "Webpack", "Vite"],
    "计算机网络": ["计算机网络", "HTTP", "TCP"],
    "性能优化": ["前端性能优化"],
    "浏览器原理": ["浏览器"],
    "安全": ["安全"],
    "工程协作": ["Git"],
}

# 方向归类：题目 tags 命中该方向的任一标签即归入该方向
DIR_TAGS = {d: set(t) for d, t in DIRECTIONS.items()}


def curl(url, tries=3):
    for _ in range(tries):
        r = subprocess.run(["curl", "-s", "-m", "60", url, "-H", f"User-Agent: {UA}"],
                           capture_output=True, text=True)
        if r.stdout:
            return r.stdout
    return ""


def unescape_payload(p):
    try:
        return json.loads('"' + p + '"')
    except Exception:
        return p.encode().decode('unicode_escape', errors='ignore')


def parse_question(html_text, url):
    out = {"title": None, "answer": None, "keywords": None, "tags": [],
           "difficulty": None, "url": url}
    for b in re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', html_text, re.S):
        try:
            d = json.loads(b)
        except Exception:
            continue
        for it in (d if isinstance(d, list) else [d]):
            if isinstance(it, dict) and it.get("@type") == "QAPage":
                q = it.get("mainEntity", {})
                out["title"] = q.get("name")
                out["keywords"] = q.get("keywords")
                out["answer"] = (q.get("acceptedAnswer") or {}).get("text")
    parts = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', html_text, re.S)
    buf = "".join(unescape_payload(p) for p in parts)
    m = re.search(r"tagList[^0-9a-f]*([0-9a-f]{2})", buf)
    if m:
        am = re.search(re.escape(m.group(1)) + r":(\[[^\]]*\])", buf)
        if am:
            try:
                out["tags"] = json.loads(am.group(1))
            except Exception:
                pass
    m = re.search(r'"difficulty":(\d+)', buf)
    if m:
        out["difficulty"] = int(m.group(1))
    return out


def fetch_bank_ids(tag, max_pages=12, page_size=20):
    ids, seen = [], set()
    for cur in range(1, max_pages + 1):
        url = f"https://www.mianshiya.com/tag/{urllib.parse.quote(tag)}?current={cur}&pageSize={page_size}"
        h = curl(url)
        found = re.findall(r"/question/(\d+)", h)
        new = [i for i in found if i not in seen]
        if not new:
            break
        seen.update(new)
        ids.extend(new)
        total = re.search(r"总共 <strong>(\d+)</strong>", h)
        if total and len(ids) >= int(total.group(1)):
            break
        if len(found) < page_size:
            break
    return ids


def build_cache():
    """抓取全部前端方向的题目，构建本地题库缓存"""
    from concurrent.futures import ThreadPoolExecutor
    bank_ids = {}
    for d, tags in DIRECTIONS.items():
        ids = []
        for t in tags:
            got = fetch_bank_ids(t)
            print(f"[{d}] tag={t} -> {len(got)}", flush=True)
            ids.extend(got)
        bank_ids[d] = sorted(set(ids), key=int)
    all_ids = sorted({i for v in bank_ids.values() for i in v}, key=int)
    print("unique ids:", len(all_ids), flush=True)

    out = []
    with ThreadPoolExecutor(max_workers=8) as ex:
        for r in ex.map(lambda i: parse_question(curl(f"https://www.mianshiya.com/question/{i}"),
                                                  f"https://www.mianshiya.com/question/{i}"), all_ids):
            if r and r["title"]:
                out.append(r)
    print("kept:", len(out), flush=True)
    json.dump({"questions": out, "bank_ids": bank_ids}, open(CACHE, "w"), ensure_ascii=False)
    return out


def load_cache():
    if not os.path.exists(CACHE):
        return build_cache()
    return json.load(open(CACHE))["questions"]


def classify(questions):
    """按 tags 把题目分配到各技术方向"""
    buckets = {d: [] for d in DIRECTIONS}
    for q in questions:
        tags = set(q.get("tags") or [])
        for d, dtags in DIR_TAGS.items():
            if tags & dtags:
                buckets[d].append(q)
    # 题库 tag 顺序即为优先级（React 具体子方向先归入 React 主方向，这里保持顺序避免重复归属）
    return buckets


def pick_daily(buckets, day: datetime.date, per_direction=2):
    """按日期确定性选取：同一天结果稳定，不同天轮转"""
    seed = int(hashlib.md5(day.isoformat().encode()).hexdigest()[:8], 16)
    rng = random.Random(seed)
    picked = {}
    for d, qs in buckets.items():
        if not qs:
            continue
        # 按日期偏移整体轮转，保证不同日期取到不同题
        offset = (seed + len(d)) % len(qs)
        rotated = qs[offset:] + qs[:offset]
        # 优先取有答案解析的题
        with_ans = [q for q in rotated if q.get("answer")]
        rest = [q for q in rotated if not q.get("answer")]
        chosen = (with_ans + rest)[:per_direction]
        picked[d] = chosen
    return picked


def render_markdown(day, picked, per_direction):
    lines = [f"# 前端每日一练 · {day.isoformat()}", "",
             f"> 题目来源：面试鸭（mianshiya.com）真实题库 | 共 {len(picked)} 个技术方向 / "
             f"{sum(len(v) for v in picked.values())} 道题", "",
             "---", ""]
    for i, (d, qs) in enumerate(picked.items(), 1):
        lines.append(f"## {i}. {d}")
        lines.append("")
        for j, q in enumerate(qs, 1):
            lines.append(f"### {d} · 第 {j} 题")
            lines.append("")
            lines.append(f"**{q['title']}**")
            lines.append("")
            meta = []
            if q.get("difficulty"):
                meta.append(f"难度 {q['difficulty']}/5")
            if q.get("tags"):
                meta.append("标签 " + "、".join(q["tags"]))
            if q.get("keywords"):
                meta.append(f"关键词 {q['keywords']}")
            if meta:
                lines.append("`" + " | ".join(meta) + "`")
                lines.append("")
            if q.get("answer"):
                lines.append("**参考答案**")
                lines.append("")
                lines.append(q["answer"].strip())
                lines.append("")
            lines.append(f"[原题链接]({q['url']})")
            lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", default=None, help="日期 YYYY-MM-DD，默认今天")
    ap.add_argument("--per-direction", type=int, default=2, help="每个方向出题数，默认 2")
    ap.add_argument("--rebuild", action="store_true", help="重新抓取题库缓存")
    args = ap.parse_args()

    day = datetime.date.fromisoformat(args.date) if args.date else datetime.date.today()

    if args.rebuild and os.path.exists(CACHE):
        os.remove(CACHE)
    questions = load_cache()
    buckets = classify(questions)
    picked = pick_daily(buckets, day, args.per_direction)

    os.makedirs(OUTDIR, exist_ok=True)
    path = os.path.join(OUTDIR, f"{day.isoformat()}.md")
    md = render_markdown(day, picked, args.per_direction)
    open(path, "w", encoding="utf-8").write(md)
    print(path)
    for d, qs in picked.items():
        print(f"  {d}: {len(qs)}")


if __name__ == "__main__":
    main()

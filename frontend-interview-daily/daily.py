#!/usr/bin/env python3
"""每日前端面试题生成器（数据源：面试鸭 mianshiya.com）。

用法:
    python3 daily.py                 # 生成今天的题目
    python3 daily.py -d 2026-10-25   # 生成指定日期的题目
    python3 daily.py -n 3            # 每个方向出 3 题（默认 2）
    python3 daily.py --dry           # 只看统计，不写文件
"""
import argparse
import datetime as dt
import json
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(HERE, "data")
OUT_DIR = os.path.join(HERE, "out")
POOL_FILE = os.path.join(DATA_DIR, "pool.json")
STATE_FILE = os.path.join(DATA_DIR, "state.json")
CONFIG_FILE = os.path.join(HERE, "directions.json")


def load_json(path, default):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as fp:
        return json.load(fp)


def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=1)


def is_frontend(question):
    """统一走 filters.py 判定，保证只出前端面试题。"""
    from matching import match_keyword
    from filters import is_frontend_question

    return is_frontend_question(question, match_keyword)


def matches_keywords(title, keywords):
    from matching import matches_keywords as _match
    return _match(title, keywords)


TAG_WEIGHT = 3
KEYWORD_WEIGHT = 1
FORCE_WEIGHT = 100


def score_question(question, direction):
    """方向归属打分：标签命中权重远高于关键词，避免通用词串味。

    directions.json 中可用 "excludeTags" 排除本方向不吃的标签（例如 Electron
    题里的「性能优化」标签不该归到前端性能优化方向）。
    可用 "tagWeight" 覆盖该方向的标签权重（例如「编程导航」这类泛标签
    权重调低，避免把 Vue/React 具体题抢走）。
    """
    tags = {t.lower() for t in question.get("tags", [])}
    exclude = {t.lower() for t in direction.get("excludeTags", [])}
    if tags & exclude:
        return 0
    dir_tags = {t.lower() for t in direction.get("tags", [])}
    tag_hits = len(tags & dir_tags)
    title = question["title"]
    kw_hits = sum(1 for kw in direction.get("keywords", []) if matches_keywords(title, [kw]))
    score = direction.get("tagWeight", TAG_WEIGHT) * tag_hits + KEYWORD_WEIGHT * kw_hits
    # forceKeywords：命中即强制归属本方向（用于标签落在别处但主题明确属于本方向的题）
    if matches_keywords(title, direction.get("forceKeywords", [])):
        score += FORCE_WEIGHT
    return score


def build_pools(usable, directions):
    """给每道题分配归属方向；每题只归属得分最高的方向（主池）。

    返回 (owners, shared)：
      owners  -> {方向名: [题]}  归属该方向的题
      shared  -> {方向名: [题]}  与该方向有关但归属别处的题（仅作补充池）
    """
    owners = {d["name"]: [] for d in directions}
    shared = {d["name"]: [] for d in directions}
    for q in usable:
        best_name, best_score = None, 0
        for d in directions:
            s = score_question(q, d)
            if s > best_score:
                best_name, best_score = d["name"], s
        if best_name:
            owners[best_name].append(q)
            for d in directions:
                if d["name"] != best_name and score_question(q, d) > 0:
                    shared[d["name"]].append(q)
    return owners, shared


def pick(candidates, used, needed, rng, direction_name):
    """在未被用过的题目里按日期随机种子抽取 needed 道；不够则开启新一轮循环。"""
    fresh = [q for q in candidates if q["id"] not in used]
    if len(fresh) < needed:
        fresh = list(candidates)
    rng.shuffle(fresh)
    chosen = fresh[:needed]
    return chosen, len(fresh)


def build(day, per_direction, dry):
    config = load_json(CONFIG_FILE, {"frontendTags": [], "directions": []})
    pool = load_json(POOL_FILE, [])
    state = load_json(STATE_FILE, {"used": {}, "history": [], "lastUsed": {}})
    frontend_tags = {t.lower() for t in config["frontendTags"]}

    usable = []
    for q in pool:
        tags = {t.lower() for t in q.get("tags", [])}
        if not (tags & frontend_tags):
            continue
        if not is_frontend(q):
            continue
        usable.append(q)
    by_id = {q["id"]: q for q in usable}

    directions = config["directions"]
    owners, shared = build_pools(usable, directions)
    last_used = state.get("lastUsed", {})
    picked = []
    taken = set()

    # 题库紧张的方向优先挑，避免小方向被大方向「抢光」
    order = sorted(directions, key=lambda d: len(owners[d["name"]]))

    for direction in order:
        name = direction["name"]
        # 候选池 = 主池 + 补充池（补充池是主题相关但归属其他方向的题，
        # 主池题量出尽后才启用，保证小方向不会过早重复）
        primary = owners[name]
        primary_ids = {q["id"] for q in primary}
        extra = [q for q in shared[name] if q["id"] not in primary_ids]
        if not primary and not extra:
            continue
        rng = random.Random(f"{day.isoformat()}::{name}")

        # 排序规则：未出过的题（主池优先）→ 出过但最久未出的题
        # 保证「尽量不重复」，主池题目优先归属本方向
        fresh = [q for q in primary if q["id"] not in last_used]
        fresh_extra = [q for q in extra if q["id"] not in last_used]
        stale = sorted(
            (q for q in primary + extra if q["id"] in last_used),
            key=lambda q: (last_used[q["id"]], q["id"]),
        )
        rng.shuffle(fresh)
        rng.shuffle(fresh_extra)
        rng.shuffle(stale)
        ordered = fresh + fresh_extra + stale
        chosen = []
        for q in ordered:
            if q["id"] in taken:
                continue
            chosen.append(q)
            taken.add(q["id"])
            if len(chosen) >= per_direction:
                break
        for q in chosen:
            last_used[q["id"]] = day.isoformat()
        used_map = state.setdefault("used", {})
        used_map[name] = sorted(set(used_map.get(name, [])) | {q["id"] for q in chosen})
        picked.append({
            "direction": name,
            "icon": direction.get("icon", "•"),
            "poolSize": len(primary) + len(extra),
            "questions": chosen,
        })

    picked.sort(key=lambda p: [d["name"] for d in directions].index(p["direction"]))
    state["lastUsed"] = last_used
    total = sum(len(p["questions"]) for p in picked)
    summary = {
        "date": day.isoformat(),
        "weekday": "星期" + "一二三四五六日"[day.weekday()],
        "directions": len(picked),
        "total": total,
        "items": [
            {
                "direction": p["direction"],
                "icon": p["icon"],
                "poolSize": p["poolSize"],
                "questions": [
                    {
                        "id": q["id"],
                        "title": q["title"],
                        "tags": q.get("tags", []),
                        "difficulty": q.get("difficulty"),
                        "viewNum": q.get("viewNum", 0),
                        "needVip": q.get("needVip"),
                        "url": q["url"],
                    }
                    for q in p["questions"]
                ],
            }
            for p in picked
        ],
    }

    if dry:
        print(json.dumps(summary, ensure_ascii=False, indent=1))
        return summary, state, by_id

    os.makedirs(OUT_DIR, exist_ok=True)
    md_path = os.path.join(OUT_DIR, f"{day.isoformat()}.md")
    with open(md_path, "w", encoding="utf-8") as fp:
        fp.write(render_markdown(summary))

    html = render_html(summary)
    report_dir = os.path.join(HERE, "report")
    os.makedirs(report_dir, exist_ok=True)
    html_path = os.path.join(report_dir, f"{day.isoformat()}.html")
    with open(html_path, "w", encoding="utf-8") as fp:
        fp.write(html)

    state.setdefault("history", []).append({
        "date": day.isoformat(), "total": total, "directions": len(picked),
    })
    state["history"] = state["history"][-120:]
    save_json(STATE_FILE, state)

    # 归档日历：必须在当天文件写完之后再刷新，否则会漏掉当天
    import build_calendar
    build_calendar.main()

    print(f"已生成 {total} 题 / {len(picked)} 个方向")
    print(f"  Markdown: {md_path}")
    print(f"  HTML    : {html_path}")
    print(f"  入口页  : {os.path.join(report_dir, 'index.html')}")
    return summary, state, by_id


def render_markdown(summary):
    lines = [
        f"# 每日前端面试题 · {summary['date']}（{summary['weekday']}）",
        "",
        f"> 共 {summary['total']} 题，覆盖 {summary['directions']} 个前端技术方向，每个方向至少 2 题。",
        "> 题目来源：面试鸭 mianshiya.com",
        "",
    ]
    for item in summary["items"]:
        lines.append(f"## {item['icon']} {item['direction']}")
        lines.append("")
        for i, q in enumerate(item["questions"], 1):
            tags = "、".join(q["tags"][:4])
            lines.append(f"{i}. **{q['title']}**")
            lines.append(f"   - 标签：{tags} | 难度：{q['difficulty']} | 热度：{q['viewNum']}")
            lines.append(f"   - 链接：{q['url']}")
        lines.append("")
    return "\n".join(lines)


def render_html(summary):
    from html import escape

    LEVEL_LABEL = {1: "简单", 2: "中等", 3: "较难", 4: "困难", 5: "专家"}
    LEVEL_CLASS = {1: "lv1", 2: "lv2", 3: "lv3", 4: "lv4", 5: "lv5"}
    LEVEL_NAME = {1: "简单", 2: "中等", 3: "较难", 4: "困难", 5: "专家"}

    difficulty_counter = {}
    for item in summary["items"]:
        for q in item["questions"]:
            lvl = q.get("difficulty") or 3
            difficulty_counter[lvl] = difficulty_counter.get(lvl, 0) + 1

    chart_data = {
        "directions": [
            {"name": item["direction"], "count": item.get("poolSize", 0)}
            for item in summary["items"]
        ],
        "difficulty": [
            {"name": LEVEL_NAME[lvl], "value": difficulty_counter[lvl]}
            for lvl in sorted(difficulty_counter)
        ],
    }

    blocks = []
    for item in summary["items"]:
        cards = []
        for i, q in enumerate(item["questions"], 1):
            lvl = q.get("difficulty") or 3
            tags = "".join(
                f'<span class="tag">{escape(t)}</span>' for t in q.get("tags", [])[:4]
            )
            vip = '<span class="vip">VIP</span>' if q.get("needVip") else ""
            cards.append(
                f'<article class="q">'
                f'<div class="qtop"><span class="qn">Q{len(cards) + 1}</span>'
                f'<span class="pill {LEVEL_CLASS.get(lvl, "lv2")}">{LEVEL_LABEL.get(lvl, "中等")}</span>{vip}</div>'
                f'<h3 class="qt"><a href="{q["url"]}" target="_blank" rel="noopener">{escape(q["title"])}</a></h3>'
                f'<div class="qmeta">{tags}'
                f'<span class="views">{q.get("viewNum", 0)} 浏览</span></div>'
                f'</article>'
            )
        blocks.append(
            f'<section class="dir">'
            f'<h3 class="dhead"><span class="ico">{item["icon"]}</span>{escape(item["direction"])}'
            f'<span class="dmeta">今日 {len(item["questions"])} 题 · 题库覆盖 {item.get("poolSize", 0)} 题</span>'
            f'</h3>'
            f'<div class="qgrid">{"".join(cards)}</div>'
            f'</section>'
        )

    json_data = json.dumps(chart_data, ensure_ascii=False).replace("</", "<\\/")

    return f"""<!-- Generated by Trae Work -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>每日前端面试题 · {summary['date']}</title>
<link rel="stylesheet" href="./assets/styles.css">
</head>
<body>
<div class="wrap">
  <header class="hero">
    <p class="kicker">Daily Frontend Interview · 面试鸭题库</p>
    <h1>每日前端面试题<span class="day">{summary['date']} · {summary['weekday']}</span></h1>
    <p class="lede">覆盖 <strong>{summary['directions']}</strong> 个前端技术方向，每个方向至少 <strong>2</strong> 道题；题目按日期种子轮换，<strong>优先不重复</strong>，已出过的题会留档换新。</p>
    <div class="statgrid">
      <div class="stat"><b>{summary['total']}</b><span>今日题目</span></div>
      <div class="stat"><b>{summary['directions']}</b><span>技术方向</span></div>
      <div class="stat"><b>{min(len(i["questions"]) for i in summary["items"])}</b><span>单方向最少题量</span></div>
      <div class="stat"><b>{sum(i.get("poolSize", 0) for i in summary["items"])}</b><span>题库可用题量</span></div>
    </div>
  </header>

  <section class="sec">
    <h2>今日概览</h2>
    <p class="sub">各方向题库覆盖量与今日难度构成，用于判断刷题密度是否均衡。</p>
    <div class="chart-grid">
      <figure class="chart-figure">
        <figcaption><b>各技术方向题库覆盖量</b>（题）</figcaption>
        <div id="chart-pool" style="width:100%;min-height:420px"></div>
      </figure>
      <figure class="chart-figure">
        <figcaption><b>今日题目难度分布</b>（题）</figcaption>
        <div id="chart-difficulty" style="width:100%;min-height:420px"></div>
      </figure>
    </div>
  </section>

  <section class="sec">
    <h2>今日题目清单</h2>
    <p class="sub">点击标题跳转面试鸭原题页面查看完整题解（部分题目为 VIP 内容）。</p>
    {"".join(blocks)}
  </section>

  <footer>
    <div class="sources">
      <h2>Sources</h2>
      <ol>
        <li id="cite-1">
          <span class="src-title">面试鸭 mianshiya.com，前端面试题库。题目标题、标签、难度与浏览量数据来源。</span>
          <a class="src-url" href="https://www.mianshiya.com" target="_blank" rel="noopener">https://www.mianshiya.com</a>
        </li>
        <li id="cite-2">
          <span class="src-title">面试鸭题库公开检索接口 api.mianshiya.com/api/question/search。本页题目由该接口按前端标签抓取。</span>
          <a class="src-url" href="https://api.mianshiya.com" target="_blank" rel="noopener">https://api.mianshiya.com</a>
        </li>
      </ol>
    </div>
    <p class="note">本页由 <code>daily.py</code> 每日自动生成 · 题库抓取时间：{summary['date']}</p>
  </footer>
</div>

<script type="application/json" id="report-data">{json_data}</script>
<script src="./_shared/js/echarts.min.js"></script>
<script src="./assets/charts.js"></script>
</body>
</html>
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--date", default=None, help="日期 YYYY-MM-DD，默认今天")
    parser.add_argument("-n", "--num", type=int, default=2, help="每个方向出题数量")
    parser.add_argument("--dry", action="store_true", help="只打印，不写文件")
    args = parser.parse_args()

    day = dt.date.fromisoformat(args.date) if args.date else dt.date.today()
    build(day, args.num, args.dry)


if __name__ == "__main__":
    main()

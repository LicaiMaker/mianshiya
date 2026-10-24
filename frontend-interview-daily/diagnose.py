#!/usr/bin/env python3
"""诊断：统计各方向主池/补充池/未归属题目量。"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from matching import match_keyword  # noqa: E402
from filters import is_frontend_question  # noqa: E402


def main():
    pool = json.load(open(os.path.join(HERE, "data", "pool.json"), encoding="utf-8"))
    config = json.load(open(os.path.join(HERE, "directions.json"), encoding="utf-8"))
    frontend_tags = {t.lower() for t in config["frontendTags"]}
    kept = [
        q for q in pool
        if {t.lower() for t in q.get("tags", [])} & frontend_tags
        and is_frontend_question(q, match_keyword)
    ]
    directions = config["directions"]
    owners = {d["name"]: [] for d in directions}
    shared = {d["name"]: [] for d in directions}
    for q in kept:
        best, best_score = None, 0
        for d in directions:
            s = score(q, d)
            if s > best_score:
                best, best_score = d["name"], s
        if best:
            owners[best].append(q)
            for d in directions:
                if d["name"] != best and score(q, d) > 0:
                    shared[d["name"]].append(q)

    print(f"可用题 {len(kept)}")
    print(f"{'方向':22s} 主池  补充  合计")
    for d in directions:
        n = d["name"]
        print(f"{n:22s} {len(owners[n]):4d}  {len(shared[n]):4d}  {len(owners[n]) + len(shared[n]):4d}")

    assigned = {q["id"] for n in owners for q in owners[n]}
    un = [q for q in kept if q["id"] not in assigned]
    print(f"\n未归属 {len(un)} 题")
    for q in un[:40]:
        print("  ", q["title"], q["tags"])


def score(q, d):
    tags = {t.lower() for t in q.get("tags", [])}
    exclude = {t.lower() for t in d.get("excludeTags", [])}
    if tags & exclude:
        return 0
    dir_tags = {t.lower() for t in d.get("tags", [])}
    tag_hits = len(tags & dir_tags)
    kw_hits = sum(1 for kw in d.get("keywords", []) if match_keyword(q["title"], kw))
    s = d.get("tagWeight", 3) * tag_hits + kw_hits
    if any(match_keyword(q["title"], kw) for kw in d.get("forceKeywords", [])):
        s += 100
    return s


if __name__ == "__main__":
    main()

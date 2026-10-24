#!/usr/bin/env python3
"""统计各方向候选题量（tag 交集 ∪ 标题关键词命中），用于调优 directions.json。"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from daily import load_json, is_backend, is_dropped, matches_keywords  # noqa: E402

CONFIG_FILE = os.path.join(HERE, "directions.json")
POOL_FILE = os.path.join(HERE, "data", "pool.json")


def main():
    config = load_json(CONFIG_FILE, {})
    pool = load_json(POOL_FILE, [])
    frontend_tags = {t.lower() for t in config["frontendTags"]}
    usable = [
        q for q in pool
        if ({t.lower() for t in q.get("tags", [])} & frontend_tags)
        and not is_backend(q) and not is_dropped(q)
    ]
    print(f"可用前端题：{len(usable)}")

    for d in config["directions"]:
        tags = {t.lower() for t in d.get("tags", [])}
        kws = d.get("keywords", [])
        by_tag = [q for q in usable if {t.lower() for t in q.get("tags", [])} & tags]
        by_kw = [q for q in usable if matches_keywords(q["title"], kws)]
        union = {q["id"] for q in by_tag} | {q["id"] for q in by_kw}
        print(f"{d['name']:<16} tag={len(by_tag):>4}  kw={len(by_kw):>4}  union={len(union):>4}  (kw独有 {len(union) - len(by_tag)})")


if __name__ == "__main__":
    main()

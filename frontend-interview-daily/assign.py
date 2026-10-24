#!/usr/bin/env python3
"""方向归属评分模型：把每道题分配到最匹配的方向。

score(题, 方向) = 3 × 命中标签数 + 1 × 标题命中关键词数
标签命中权重远高于关键词，避免 React/Vue 的通用词（组件、路由）互相串味。
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from daily import load_json, is_backend, is_dropped  # noqa: E402

CONFIG_FILE = os.path.join(HERE, "directions.json")
POOL_FILE = os.path.join(HERE, "data", "pool.json")

TAG_WEIGHT = 3
KEYWORD_WEIGHT = 1


def load_usable():
    config = load_json(CONFIG_FILE, {})
    pool = load_json(POOL_FILE, [])
    frontend_tags = {t.lower() for t in config["frontendTags"]}
    usable = [
        q for q in pool
        if ({t.lower() for t in q.get("tags", [])} & frontend_tags)
        and not is_backend(q) and not is_dropped(q)
    ]
    return usable, config


def score(question, direction):
    tags = {t.lower() for t in question.get("tags", [])}
    dir_tags = {t.lower() for t in direction.get("tags", [])}
    tag_hits = len(tags & dir_tags)
    title = question["title"].lower()
    kw_hits = sum(1 for kw in direction.get("keywords", []) if kw.lower() in title)
    return TAG_WEIGHT * tag_hits + KEYWORD_WEIGHT * kw_hits


def assign(usable, config):
    """每题归属到得分最高的方向；同分时按方向顺序。"""
    buckets = {d["name"]: [] for d in config["directions"]}
    for q in usable:
        best_name, best_score = None, 0
        for d in config["directions"]:
            s = score(q, d)
            if s > best_score:
                best_name, best_score = d["name"], s
        if best_name:
            buckets[best_name].append(q)
    return buckets


def main():
    usable, config = load_usable()
    buckets = assign(usable, config)
    total = sum(len(v) for v in buckets.values())
    print(f"可用前端题 {len(usable)}，已分配 {total}\n")
    for d in config["directions"]:
        n = len(buckets[d["name"]])
        print(f"{d['name']:<20} {n:>4}")


if __name__ == "__main__":
    main()

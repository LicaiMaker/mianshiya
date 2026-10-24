#!/usr/bin/env python3
"""并发扩充题池：用全文检索(searchText)抓取更多前端题目。

用法:
    python3 expand_pool.py            # 扩充 data/pool.json
"""
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import fetch_pool as fp

HERE = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(HERE, "data")
POOL_FILE = os.path.join(DATA_DIR, "pool.json")


def worker(keyword, pool, lock, stats):
    before = len(pool)
    try:
        fp.fetch_by_text(keyword, pool, stats)
    except Exception as exc:  # noqa: BLE001
        return keyword, 0, str(exc)
    with lock:
        added = len(pool) - before
    return keyword, added, ""


def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    pool = {}
    if os.path.exists(POOL_FILE):
        with open(POOL_FILE, encoding="utf-8") as fp_:
            pool = {q["id"]: q for q in json.load(fp_)}
    print(f"已有题目 {len(pool)} 条，开始并发扩量…", flush=True)

    keywords = []
    for kw in fp.EXPAND_KEYWORDS:
        if kw not in keywords:
            keywords.append(kw)

    import threading
    lock = threading.Lock()
    stats = {}
    with ThreadPoolExecutor(max_workers=6) as pool_exec:
        results = list(pool_exec.map(lambda kw: worker(kw, pool, lock, stats), keywords))

    total_new = 0
    for keyword, added, err in results:
        if err:
            print(f"  [text:{keyword}] 失败: {err}", file=sys.stderr)
        elif added:
            total_new += added
            print(f"  [text:{keyword}] +{added}", flush=True)
    print(f"本轮新增 {total_new} 题")

    questions = sorted(pool.values(), key=lambda q: q["id"])
    with open(POOL_FILE, "w", encoding="utf-8") as fp_:
        json.dump(questions, fp_, ensure_ascii=False, indent=1)
    print(f"题池已保存：{POOL_FILE}（共 {len(questions)} 题）")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""调优 directions.json：测量各方向候选量与 N 天重复率。

用法:
    python3 tune.py [天数]
"""
import datetime as dt
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from daily import (  # noqa: E402
    load_json, is_backend, is_dropped, build_pools,
)

CONFIG_FILE = os.path.join(HERE, "directions.json")
POOL_FILE = os.path.join(HERE, "data", "pool.json")


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


def simulate(usable, config, days, per_direction=2):
    owners, shared = build_pools(usable, config["directions"])
    last_used = {}
    appeared = {}
    base = dt.date(2026, 1, 1)
    order = sorted(config["directions"], key=lambda d: len(owners[d["name"]]))

    for i in range(days):
        day = base + dt.timedelta(days=i)
        taken = set()
        for d in order:
            name = d["name"]
            primary = owners[name]
            primary_ids = {q["id"] for q in primary}
            extra = [q for q in shared[name] if q["id"] not in primary_ids]
            rng = random.Random(f"{day.isoformat()}::{name}")
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
            picked = []
            for q in ordered:
                if q["id"] in taken:
                    continue
                picked.append(q)
                taken.add(q["id"])
                if len(picked) >= per_direction:
                    break
            for q in picked:
                last_used[q["id"]] = day.isoformat()
                appeared.setdefault(q["id"], []).append(day.isoformat())

    repeated = {q: d for q, d in appeared.items() if len(d) > 1}
    total_slots = days * per_direction * len(order)
    uniq = len(appeared)
    return appeared, repeated, total_slots, uniq, owners, shared


def main():
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    per_direction = 2
    usable, config = load_usable()
    print(f"可用前端题：{len(usable)}\n")
    appeared, repeated, total_slots, uniq, owners, shared = simulate(usable, config, days)
    print(f"{days} 天模拟：出题 {total_slots} 次，去重后 {uniq} 道，重复题 {len(repeated)} 道 "
          f"（重复率 {len(repeated) / max(uniq, 1):.1%}）\n")
    for d in config["directions"]:
        name = d["name"]
        primary = owners[name]
        primary_ids = {q["id"] for q in primary}
        pool = primary + [q for q in shared[name] if q["id"] not in primary_ids]
        ids = {q["id"] for q in pool}
        rep = sum(1 for q in ids if len(appeared.get(q, [])) > 1)
        mark = "  <-- 题量不足" if len(pool) < days * 2 else ""
        print(f"{name:<20} 主池 {len(primary):>4} 可用 {len(pool):>4} 重复 {rep:>3}{mark}")


if __name__ == "__main__":
    main()

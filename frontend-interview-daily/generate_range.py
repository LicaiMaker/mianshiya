#!/usr/bin/env python3
"""连续生成 N 天的前端面试题（一次跑完，题库不变时可直接产出未来几天的报告）。

按日期顺序逐日生成，state.json 里的 lastUsed 会在天与天之间累积，
因此后续日期会自动避开前面已出过的题（LRU 轮换）。

用法:
    python3 generate_range.py --days 30 --start 2026-10-24
    python3 generate_range.py --days 30 --start 2026-10-24 --reset   # 重置轮换状态
"""
import argparse
import datetime as dt
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import daily  # noqa: E402

STATE_FILE = os.path.join(HERE, "data", "state.json")


def reset_state():
    with open(STATE_FILE, encoding="utf-8") as fp:
        state = json.load(fp)
    state["lastUsed"] = {}
    state["history"] = []
    with open(STATE_FILE, "w", encoding="utf-8") as fp:
        json.dump(state, fp, ensure_ascii=False, indent=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=30)
    ap.add_argument("--start", default=dt.date.today().isoformat())
    ap.add_argument("--num", type=int, default=2, help="每个方向出题数量")
    ap.add_argument("--reset", action="store_true", help="生成前清空轮换状态")
    args = ap.parse_args()

    if args.reset:
        reset_state()

    start = dt.date.fromisoformat(args.start)
    seen = {}
    for i in range(args.days):
        day = start + dt.timedelta(days=i)
        summary, _, _ = daily.build(day, args.num, dry=False)
        ids = [q["id"] for item in summary["items"] for q in item["questions"]]
        for qid in ids:
            seen[qid] = seen.get(qid, 0) + 1
        uniq = len(set(ids))
        print(f"{day}  {len(ids)} 题 / {summary['directions']} 方向  本日去重 {uniq}")

    total_all = sum(seen.values())
    uniq_all = len(seen)
    print(f"\n{args.days} 天共 {total_all} 题，去重 {uniq_all}，重复率 {(total_all - uniq_all) / total_all:.2%}")
    for c, q in sorted(((c, q) for q, c in seen.items() if c > 1), reverse=True)[:10]:
        print(f"  出现 {c} 次: {q}")


if __name__ == "__main__":
    main()

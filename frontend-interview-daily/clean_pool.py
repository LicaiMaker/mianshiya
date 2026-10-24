#!/usr/bin/env python3
"""清洗题池：剔除后端 / 安全运维 / AI 机器学习 / 面经项目题等非前端题目。

判定规则统一收敛到 filters.py，本脚本只负责「应用规则 + 写回」。

用法:
    python3 clean_pool.py            # 清洗并写回 data/pool.json
    python3 clean_pool.py --dry      # 只打印将被删除的题目
    python3 clean_pool.py --dry -v   # 打印将被删除的题目标题
"""
import argparse
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
POOL_FILE = os.path.join(HERE, "data", "pool.json")


def is_backend(question):
    """复用 filters.py 的统一判定：非前端题返回 True。"""
    from matching import match_keyword
    from filters import is_frontend_question

    return not is_frontend_question(question, match_keyword)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    ap.add_argument("-v", "--verbose", action="store_true", help="打印被剔除的题目标题")
    args = ap.parse_args()

    with open(POOL_FILE, encoding="utf-8") as fp:
        pool = json.load(fp)

    kept, removed = [], []
    for q in pool:
        (removed if is_backend(q) else kept).append(q)

    print(f"题池 {len(pool)} -> 保留 {len(kept)}，剔除 {len(removed)}")
    by_tag = {}
    for q in removed:
        for t in q.get("tags", []):
            by_tag[t] = by_tag.get(t, 0) + 1
    for t, n in sorted(by_tag.items(), key=lambda x: -x[1])[:20]:
        print(f"  涉及标签 {t}: {n}")

    if args.verbose:
        print("\n--- 被剔除的题目 ---")
        for q in removed:
            print(f"  [{'/'.join(q.get('tags', []))}] {q['title']}")

    if not args.dry:
        with open(POOL_FILE, "w", encoding="utf-8") as fp:
            json.dump(kept, fp, ensure_ascii=False, indent=1)
        print("已写回", POOL_FILE)


if __name__ == "__main__":
    main()

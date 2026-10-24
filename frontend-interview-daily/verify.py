#!/usr/bin/env python3
"""校验所有已生成报告：每个方向题数、是否全部为前端题、重复率。"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from matching import match_keyword  # noqa: E402
from filters import is_frontend_question  # noqa: E402

OUT_DIR = os.path.join(HERE, "out")


def main():
    files = sorted(f for f in os.listdir(OUT_DIR) if f.endswith(".md"))
    total = 0
    uniq = set()
    bad = []
    min_dir = 99
    bad_dir = []
    for name in files:
        text = open(os.path.join(OUT_DIR, name), encoding="utf-8").read()
        blocks = re.findall(r"^## (.+)$\n(.*?)(?=^## |\Z)", text, re.M | re.S)
        for title, body in blocks:
            titles = re.findall(r"^\d+\. \*\*(.+?)\*\*$", body, re.M)
            min_dir = min(min_dir, len(titles))
            if len(titles) < 2:
                bad_dir.append((name, title, len(titles)))
            for t in titles:
                total += 1
        ids = re.findall(r"mianshiya\.com/question/(\d+)", text)
        uniq.update(ids)

    # 非前端题复核：把生成的题与题池比对
    pool = {q["id"]: q for q in json.load(open(os.path.join(HERE, "data", "pool.json"), encoding="utf-8"))}
    for name in files:
        text = open(os.path.join(OUT_DIR, name), encoding="utf-8").read()
        for m in re.finditer(r"^\d+\. \*\*(.+?)\*\*$\n\s+- 标签：(.+?) \|", text, re.M):
            title, tags = m.group(1), [t.strip() for t in m.group(2).split("、")]
            if not is_frontend_question({"title": title, "tags": tags}, match_keyword):
                bad.append((name, title, tags))

    print(f"报告期数 {len(files)}  总题数 {total}  去重 {len(uniq)}  重复率 {(total - len(uniq)) / total:.2%}")
    print(f"单方向最少题数 {min_dir}" + (f"  不足的方向: {bad_dir}" if bad_dir else "  (全部 >= 2)"))
    print(f"非前端题 {len(bad)}" + ("  <-- 需修正" if bad else "  (全部为前端题)"))
    for b in bad[:20]:
        print("   ", b)


if __name__ == "__main__":
    main()

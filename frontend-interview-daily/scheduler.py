#!/usr/bin/env python3
"""每日出题调度守护进程（由 supervisord 拉起）。

每天固定时间（默认 08:00，Asia/Shanghai）调用 daily.py 生成当天报告，
并把输出追加到 logs/daily.log。

用法:
    python3 scheduler.py                # 前台运行
    python3 scheduler.py --at 08:30     # 改触发时间
    python3 scheduler.py --run-now      # 立刻跑一次再进入等待
"""
import argparse
import datetime as dt
import os
import subprocess
import sys
import time

os.environ.setdefault("TZ", "Asia/Shanghai")
try:
    time.tzset()
except AttributeError:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(HERE, "logs")
LOG_FILE = os.path.join(LOG_DIR, "daily.log")


def log(message):
    stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{stamp}] {message}"
    print(line, flush=True)
    try:
        os.makedirs(LOG_DIR, exist_ok=True)
        with open(LOG_FILE, "a", encoding="utf-8") as fp:
            fp.write(line + "\n")
    except OSError:
        pass


def run_daily(day=None):
    """调用 daily.py 生成当天（或指定日期）报告。"""
    day = day or dt.date.today()
    cmd = [sys.executable, os.path.join(HERE, "daily.py"), "-d", day.isoformat()]
    log(f"开始生成 {day} 的题目 -> {' '.join(cmd)}")
    try:
        proc = subprocess.run(
            cmd, cwd=HERE, capture_output=True, text=True, timeout=600
        )
    except subprocess.TimeoutExpired:
        log("生成超时（600s），跳过")
        return False
    if proc.returncode != 0:
        log(f"生成失败 rc={proc.returncode}\n{proc.stderr.strip()[:2000]}")
        return False
    for line in (proc.stdout or "").strip().splitlines():
        log("  " + line)
    return True


def seconds_until(hour, minute):
    now = dt.datetime.now()
    target = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if target <= now:
        target += dt.timedelta(days=1)
    return (target - now).total_seconds(), target


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--at", default="08:00", help="每日触发时间 HH:MM")
    ap.add_argument("--run-now", action="store_true", help="启动时先立刻跑一次")
    args = ap.parse_args()

    hour, minute = (int(x) for x in args.at.split(":"))
    log(f"调度器启动：每天 {args.at}（{time.tzname[0]}）生成前端面试题")

    if args.run_now:
        run_daily()

    while True:
        wait, target = seconds_until(hour, minute)
        log(f"下次运行 {target:%Y-%m-%d %H:%M}，等待 {wait / 3600:.2f} 小时")
        while wait > 0:
            time.sleep(min(wait, 300))
            wait, _ = seconds_until(hour, minute)
        run_daily()


if __name__ == "__main__":
    main()

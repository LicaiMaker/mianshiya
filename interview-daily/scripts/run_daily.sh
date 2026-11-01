#!/usr/bin/env bash
# 前端每日面试题调度器：每天定点生成一次，生成后进入休眠等待次日。
#
# 沙箱内没有 cron，因此用常驻循环 + 定点等待的方式实现「每日自动执行」。
# 通过 supervisord 拉起，进程退出后会被自动重启。
set -u

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="$ROOT/output/logs"
RUN_HOUR="${INTERVIEW_DAILY_HOUR:-9}"
RUN_MINUTE="${INTERVIEW_DAILY_MINUTE:-0}"
TZ_NAME="${INTERVIEW_DAILY_TZ:-Asia/Shanghai}"

mkdir -p "$LOG_DIR"

log() {
  printf '[%s] %s\n' "$(date '+%F %T')" "$*" >> "$LOG_DIR/runner.log"
}

# 若当天文件尚未生成（例如首次部署），立即补一次
today="$(date +%F)"
if [ ! -f "$ROOT/output/$today.html" ]; then
  log "补生成 $today 的题目"
  python3 "$ROOT/scripts/daily.py" --date "$today" >> "$LOG_DIR/runner.log" 2>&1 \
    || log "生成失败：$today"
fi

while true; do
  now_epoch=$(date +%s)
  target_epoch=$(date -d "today ${RUN_HOUR}:${RUN_MINUTE}" +%s 2>/dev/null || echo "")
  if [ -z "$target_epoch" ]; then
    sleep 3600
    continue
  fi
  if [ "$target_epoch" -le "$now_epoch" ]; then
    target_epoch=$(date -d "tomorrow ${RUN_HOUR}:${RUN_MINUTE}" +%s)
  fi
  wait_s=$((target_epoch - now_epoch))
  log "下次执行在 $((wait_s / 3600)) 小时 $(((wait_s % 3600) / 60)) 分后"
  sleep "$wait_s"
  run_day="$(date +%F)"
  log "开始生成 $run_day 的题目"
  python3 "$ROOT/scripts/daily.py" --date "$run_day" >> "$LOG_DIR/runner.log" 2>&1 \
    || log "生成失败：$run_day"
done

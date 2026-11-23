#!/bin/bash
# Chạy mỗi sáng trên máy anh (launchd/cron gọi). Cần: Claude Code CLI (lệnh `claude`), python3, ffmpeg, node.
set -euo pipefail
cd "$(dirname "$0")"
LOG="work/daily-$(date +%F).log"; mkdir -p work
exec > >(tee -a "$LOG") 2>&1
echo "== $(date) =="
git -C .. pull --ff-only || true
SKIP=""
for try in 1 2 3; do
  python3 rotd.py pick $SKIP
  out=$(claude -p "$(cat prompt_script.md)" --allowedTools "Read,Write" 2>&1 | tail -1)
  echo "claude: $out"
  if [[ "$out" == *SKIP* ]]; then SKIP="$SKIP $(python3 -c 'import json;print(json.load(open("work/pick.json"))["full_name"])')"; continue; fi
  break
done
python3 rotd.py render
python3 rotd.py post

#!/bin/bash
# Cài Repo of the Day trên macOS (chạy một lần): bash setup_mac.sh
set -euo pipefail
cd "$(dirname "$0")"
command -v brew >/dev/null || { echo "Cần Homebrew: https://brew.sh"; exit 1; }
brew install ffmpeg node python@3.12 || true
python3 -m pip install --user -q piper-tts pillow
(cd motion && npm install --silent && npx playwright install chromium)
command -v claude >/dev/null || echo "⚠️  Chưa có Claude Code CLI: npm install -g @anthropic-ai/claude-code, rồi chạy 'claude' một lần để đăng nhập."
[ -f .env ] || printf 'FB_PAGE_ID=\nFB_ACCESS_TOKEN=\n' > .env && chmod 600 .env
PLIST=~/Library/LaunchAgents/com.repooftheday.daily.plist
cat > "$PLIST" <<PL
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>com.repooftheday.daily</string>
  <key>ProgramArguments</key><array><string>/bin/bash</string><string>$(pwd)/run_daily.sh</string></array>
  <key>StartCalendarInterval</key><dict><key>Hour</key><integer>6</integer><key>Minute</key><integer>46</integer></dict>
  <key>EnvironmentVariables</key><dict><key>PATH</key><string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:$HOME/.local/bin</string></dict>
  <key>StandardOutPath</key><string>$(pwd)/work/launchd.log</string>
  <key>StandardErrorPath</key><string>$(pwd)/work/launchd.log</string>
</dict></plist>
PL
launchctl unload "$PLIST" 2>/dev/null || true
launchctl load "$PLIST"
echo "✅ Đã cài. Mở file .env, điền FB_PAGE_ID và FB_ACCESS_TOKEN. Lịch chạy: 6:46 sáng mỗi ngày (máy phải mở, không ngủ)."
echo "Chạy thử ngay: bash run_daily.sh"

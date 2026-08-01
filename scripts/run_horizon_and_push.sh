#!/bin/bash
# Horizon 每日扫描 + 自动 push 到 GitHub 触发网站部署
# 用法：crontab 每天 15:07 运行
#   7 15 * * * /Users/wanglingwei/Horizon/scripts/run_horizon_and_push.sh >> /Users/wanglingwei/Horizon/logs/horizon.log 2>&1

set -e

export PATH="/Users/wanglingwei/Library/Application Support/remio/Users/SharedData/runtime/uv/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"

HORIZON_DIR="$HOME/Horizon"
LOG_DIR="$HORIZON_DIR/logs"
mkdir -p "$LOG_DIR"

echo "=== $(date '+%Y-%m-%d %H:%M:%S') Horizon scan start ==="

cd "$HORIZON_DIR"

# 1. 运行 Horizon 扫描
uv run horizon --hours 24

# 2. 强制添加 _posts（被 .gitignore 排除）+ git push
git add -f docs/_posts/
git add docs/index.html docs/_layouts/ docs/_config.yml docs/assets/ 2>/dev/null || true
git commit -m "🌅 Horizon daily summary $(date '+%Y-%m-%d')" || echo "nothing to commit"
git push origin main

echo "=== $(date '+%Y-%m-%d %H:%M:%S') done — GitHub Actions will auto-deploy ==="

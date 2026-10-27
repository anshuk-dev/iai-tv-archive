#!/bin/bash
# IAI.tv Automated Sync Script (Articles, Videos & Reader)
# ========================================================
# Checks internet connectivity, pulls latest changes, scrapes
# any new IAI.tv articles and videos, rebuilds the reader, and
# pushes updates to GitHub automatically.

set -e

DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$DIR"

LOG_FILE="$DIR/logs/auto_sync.log"
mkdir -p "$DIR/logs"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# 1. Check Internet Connectivity (Timeout 5 seconds)
if ! curl -s --head --request GET "https://iai.tv" --connect-timeout 5 --max-time 10 > /dev/null 2>&1; then
    log "Network offline or IAI.tv unreachable. Will retry on next schedule."
    exit 0
fi

log "Network connected. Starting automatic IAI.tv content sync..."

# 2. Pull remote commits first to stay up to date
git pull --rebase origin main >> "$LOG_FILE" 2>&1 || true

# 3. Check and scrape new articles
log "Checking for new IAI.tv articles..."
python3 scraper.py --workers 8 >> "$LOG_FILE" 2>&1

# 4. Check and sync new videos
log "Checking for new IAI.tv debate videos..."
python3 scripts/build_videos_index.py >> "$LOG_FILE" 2>&1

# 5. Rebuild reader static assets
log "Rebuilding reader static catalog..."
python3 scripts/build_reader.py >> "$LOG_FILE" 2>&1

# 6. Check for content changes and push
git add articles/ new_articles/ CATALOG.md articles_index.json baseline_ids.json VIDEOS_CATALOG.md iai_videos.json README.md LAST_SESSION.md
if ! git diff --cached --quiet; then
    log "✨ New content staged! Committing and pushing to GitHub..."
    git commit -m "Auto-update: sync latest IAI.tv content (local auto-sync)" >> "$LOG_FILE" 2>&1
    git push origin main >> "$LOG_FILE" 2>&1
    log "🚀 Successfully pushed updates to GitHub!"
else
    log "All content is already up to date in repository. No push needed."
fi

log "Sync run finished cleanly."

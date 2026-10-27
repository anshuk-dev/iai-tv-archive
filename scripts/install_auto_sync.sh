#!/bin/bash
# Install macOS LaunchAgent for background IAI.tv auto-sync
set -e

DIR="$(cd "$(dirname "$0")/.." && pwd)"
PLIST_SRC="$DIR/scripts/com.anshuk.iaitv.sync.plist"
PLIST_DEST="$HOME/Library/LaunchAgents/com.anshuk.iaitv.sync.plist"

mkdir -p "$HOME/Library/LaunchAgents"

# Unload existing if loaded
launchctl unload "$PLIST_DEST" 2>/dev/null || true

# Copy plist to LaunchAgents
cp "$PLIST_SRC" "$PLIST_DEST"

# Load LaunchAgent
launchctl load -w "$PLIST_DEST"

echo "✅ IAI.tv Auto-Sync LaunchAgent successfully installed and activated!"
echo "• Sync runs automatically every 1 hour and whenever internet is available."
echo "• Logs are stored at: $DIR/logs/auto_sync.log"
echo "• To uninstall, run: ./scripts/uninstall_auto_sync.sh"

#!/bin/bash
# Uninstall macOS LaunchAgent for IAI.tv auto-sync
set -e

PLIST_DEST="$HOME/Library/LaunchAgents/com.anshuk.iaitv.sync.plist"

if [ -f "$PLIST_DEST" ]; then
    launchctl unload "$PLIST_DEST" 2>/dev/null || true
    rm -f "$PLIST_DEST"
    echo "✅ IAI.tv Auto-Sync LaunchAgent uninstalled successfully."
else
    echo "LaunchAgent was not installed."
fi

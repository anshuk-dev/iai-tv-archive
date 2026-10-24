#!/bin/bash
# ==========================================
# 1-Click Private IAI.tv Reader Launcher
# ==========================================
cd "$(dirname "$0")"

PORT=8080
echo "================================================="
echo "  Starting Private IAI.tv Archive & Reader"
echo "  Accessible at: http://localhost:$PORT"
echo "================================================="

# Start background web server
python3 -m http.server $PORT &
SERVER_PID=$!

# Wait for server to bind
sleep 1

# Open in default browser
open "http://localhost:$PORT"

echo "Server is running (PID: $SERVER_PID)."
echo "Press [Ctrl + C] in this window to stop the server."

wait $SERVER_PID

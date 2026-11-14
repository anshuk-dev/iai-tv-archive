#!/bin/bash
set -e
cd "$(dirname "$0")"

# Automatically pull latest articles and updates from GitHub if online
git pull --rebase origin main 2>/dev/null || true

python3 scripts/build_reader.py
READER_PORT=8080
if lsof -Pi :8080 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    READER_PORT=8081
fi
python3 -m http.server "$READER_PORT" --bind 127.0.0.1 --directory dist &
READER_SERVER_PID=$!
trap 'kill "$READER_SERVER_PID" 2>/dev/null || true' EXIT INT TERM
open "http://127.0.0.1:$READER_PORT"
echo "Private reader: http://127.0.0.1:$READER_PORT"
echo "Press Ctrl+C to stop."
wait "$READER_SERVER_PID"

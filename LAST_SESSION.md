# IAI Archive, Video Streaming & Automation Status

## Overview
- **Repository:** `git@github.com:anshuk-dev/iai-tv-archive.git` (Private)
- **Articles Total:** **2,201 articles** archived in `articles/` (and new ones in `new_articles/`), unpaywalled via BPC.
  - Latest article: *Our cosmological theories are maps, not the territory* by Andrew Jaffe (ID: 3734, 23rd November 2026).
  - 21 new articles synced since baseline.
- **Debates & Videos Total:** **2,066 videos** cataloged with direct unpaywalled `.mp4` URLs and full metadata:
  - Latest debate: *The edge of the world* (23rd November 2026, 40m 38s, ID: 1).
  - Metadata enriched: 1,999 videos with guest speakers (96.8%), 963 with hosts/chairs (46.6%), and 1,656 with complete speaker biographies/descriptions (80.2%).
- **Interactive Video Watch Tracker & Spreadsheets:**
  - `dist/videos.html` / `videos.html`: Standalone interactive web dashboard with:
    - Real-time checkboxes and status toggles (`Unwatched`, `Watching / Continue`, `Watched`).
    - Persistent watch history saved to browser `localStorage`.
    - Live progress counters and completion bar.
    - Full-text search and filters across titles, dates, speakers, hosts, and bios.
    - Inline HTML5 video player with direct stream and Google Drive integration.
    - 1-click "Export to Excel (CSV)" and JSON backup/restore buttons.
  - `iai_videos_tracker.csv`: Complete Excel / Google Sheets spreadsheet with UTF-8 BOM, clickable links, status column, and speaker bios.
  - `VIDEOS_CATALOG.md`: GitHub markdown table with `| [ ] |` checklist checkboxes, dates, duration, speakers, hosts, and direct stream links.
- **Full Cloud Automation (Zero Intervention):**
  - Workflow: `.github/workflows/update-articles.yml` runs every 2 hours (`0 */2 * * *`).
  - Scrapes new articles, syncs video catalogs, enriches new video metadata via `data/video_metadata_cache.json`, rebuilds web reader and tracker data, commits and pushes to GitHub repository.
  - Automatically uploads a complete built `dist/` web reader artifact on every run.
- **Local Reader & Tracker:**
  - Double-click `start_reader.command` on macOS to automatically pull latest GitHub updates, rebuild dist, and view:
    - Reading Room: `http://127.0.0.1:8080`
    - Video Watch Tracker: `http://127.0.0.1:8080/videos.html`
- **Google Drive Cloud Downloader:**
  - `IAI_Cloud_Downloader.ipynb` transfers videos directly from IAI.tv to Google Drive (`MyDrive/IAI_Videos`) with zero local Mac disk space.

# IAI Archive, Video Streaming & Automation Status

## Overview
- **Repository:** `git@github.com:anshuk-dev/iai-tv-archive.git` (Private)
- **Articles Total:** **2,201 articles** archived in `articles/` (and new ones in `new_articles/`), unpaywalled via BPC.
  - Latest article: *Our cosmological theories are maps, not the territory* by Andrew Jaffe (ID: 3734, 23rd November 2026).
  - 21 new articles synced since baseline (6 new articles since Nov 14).
- **Debates & Videos Total:** **2,066 videos** cataloged with direct unpaywalled `.mp4` URLs.
  - Latest debate: *The edge of the world* (23rd November 2026, 40m 38s, ID: 1).
  - Catalogs: `VIDEOS_CATALOG.md` and `iai_videos.json`.
- **Full Cloud Automation (Zero Intervention):**
  - Workflow: `.github/workflows/update-articles.yml` runs every 2 hours (`0 */2 * * *`).
  - Scrapes new articles, syncs video catalogs, rebuilds web reader data, commits and pushes to GitHub repository.
  - Automatically uploads a complete built `dist/` web reader artifact on every run.
- **Local Reader:**
  - Double-click `start_reader.command` on macOS to automatically pull latest GitHub updates, rebuild dist, and view at `http://127.0.0.1:8080`.
- **Google Drive Cloud Downloader:**
  - `IAI_Cloud_Downloader.ipynb` transfers videos directly from IAI.tv to Google Drive (`MyDrive/IAI_Videos`) with zero local Mac disk space.

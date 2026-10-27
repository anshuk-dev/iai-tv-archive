# IAI Archive, Video Streaming & Google Drive Integration

## Overview
- **Repository:** `git@github.com:anshuk-dev/iai-tv-archive.git` (Private)
- **Articles:** 2,182 articles archived in `articles/` (and new ones in `new_articles/`), unpaywalled via BPC, synchronized incrementally every 6 hours via GitHub Actions (`.github/workflows/update-articles.yml`).
  - Added on 26 Oct 2026: *The mind is not separate from the body* (ID: 3712) by Tarek Dika
  - Added on 27 Oct 2026: *Great Britain could still be a great power* (ID: 3713) by Brendan Simms & Hugh Simms
- **Debates & Videos (2,051 total):**
  - Added on 26 Oct 2026: *The philosophy and dangers of fame* (34m 16s)
  - All direct `.mp4` video stream URLs cataloged in `iai_videos.json` and `VIDEOS_CATALOG.md`.
  - **No paywall / trial prompt**: The direct `.mp4` URLs bypass IAI's frontend 3.5-minute paywall script completely.
  - **Google Colab Cloud-to-Cloud Downloader:** `IAI_Cloud_Downloader.ipynb` streams files directly from IAI's CDN into user's 5 TB Google Drive (`MyDrive/IAI_Videos`) with zero local Mac disk consumption and zero home data usage.
  - **Reader Video Player:** Includes a "Debates & Videos" tab with search, sorting, direct full-length playback, "Play on Drive" link, and direct MP4 download.

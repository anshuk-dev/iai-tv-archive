# IAI Archive, Video Streaming & Google Drive Integration

## Overview
- **Repository:** `git@github.com:anshuk-dev/iai-tv-archive.git` (Private)
- **Articles:** 2,180 articles archived in `articles/`, unpaywalled via BPC, synchronized incrementally every 6 hours via GitHub Actions (`.github/workflows/update-articles.yml`).
- **Debates & Videos (2,050 total, ~1,209 hours of video):**
  - All direct `.mp4` video stream URLs cataloged in `iai_videos.json` and `VIDEOS_CATALOG.md`.
  - **No paywall / trial prompt**: The direct `.mp4` URLs bypass IAI's frontend 3.5-minute paywall script completely.
  - **Google Colab Cloud-to-Cloud Downloader:** `IAI_Cloud_Downloader.ipynb` streams files directly from IAI's CDN into user's 5 TB Google Drive (`MyDrive/IAI_Videos`) with zero local Mac disk consumption and zero home data usage.
  - **Reader Video Player:** Includes a "Debates & Videos" tab with search, sorting, direct full-length playback, "Play on Drive" link, and direct MP4 download.

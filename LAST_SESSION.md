# IAI Archive & Cloud Downloader Status

## Completed
1. **Video Catalog & Indexing (2,050 Videos):**
   - Extracted all 2,050 high-definition debate and talk records from `https://iai.tv/VideoController/videoSitemap.xml`.
   - 2,019 have direct `.mp4` URLs on IAI's CDN.
   - Total watch time: ~1,209 hours (~50.4 days of non-stop video).
   - Saved machine-readable index: `iai_videos.json`.
   - Saved human-readable catalog: `VIDEOS_CATALOG.md`.

2. **Google Colab Cloud-to-Cloud Transfer (`IAI_Cloud_Downloader.ipynb`):**
   - 100% cloud-to-cloud transfer from IAI CDN directly to user's 5 TB Google Drive (`/content/drive/MyDrive/IAI_Videos`).
   - Zero local disk space consumed on user's Mac.
   - Zero home Wi-Fi data consumed.
   - Downloads on Google Cloud backbone at 50–100 MB/s.
   - Safeguard for Google Drive 750 GB / 24-hour upload quota: downloads in daily batches of ~450 videos, archiving all 2,050 videos in ~4 days.
   - Smart resumption: skips already completed downloads.

3. **Web Reader Enhancement (`index.html`, `reader.js`, `css/reader.css`):**
   - Added **Debates & Videos** navigation tab.
   - Full search & filter by title, speaker, topic, duration, and date.
   - Integrated HTML5 video player modal with dark cinema UI, speed controls, direct play, and download link.

4. **Articles Archive:**
   - 2,180 unpaywalled articles saved in `articles/` as Markdown.
   - Scheduled automatic incremental updater in `.github/workflows/update-articles.yml`.
   - Private GitHub repository: `anshuk-dev/iai-tv-archive`.

# IAI — Private Reading Room & Video Archive

**[Open the private IAI article reader](https://iai-private-reading-room.savoryrain2.chatgpt.site)** · **[Browse all articles](https://iai-private-reading-room.savoryrain2.chatgpt.site/#library)**

Open using the owning ChatGPT account. The reader is private; GitHub sign-in alone does not grant access.

A complete archive and responsive editorial reader for **2,180 unpaywalled articles** and **2,050 high-definition video debates** (~1,209 hours of video) from [IAI.tv (The Institute of Art and Ideas)](https://iai.tv).

---

## 🎬 2,050 Video Debates Archive & Google Drive Cloud Transfer

All 2,050 full-length debate and talk videos are fully cataloged with titles, runtimes, descriptions, and direct `.mp4` CDN streams.

### Option 1: 1-Click Cloud-to-Cloud Transfer into Google Drive (0% Local Disk Space)
If you have a 5 TB Google Drive, you can transfer all ~2.8 TB of videos directly from IAI.tv's CDN servers to your Google Drive **without downloading anything to your computer or consuming home Wi-Fi data**:

1. Open **`IAI_Cloud_Downloader.ipynb`** in [Google Colab](https://colab.research.google.com/).
2. Run **Cell 1**: Connects Colab to your Google Drive (`/content/drive/MyDrive/IAI_Videos`).
3. Run **Cell 2 & 3**: Sets up batch download settings and loads the 2,050 video catalog.
4. Run **Cell 4**: Downloads videos at 50–100 MB/s directly into your Google Drive folder.
   > **Note on Google Drive Limits:** Google Drive has a 750 GB / 24-hour upload quota. The notebook downloads in batches of ~450 videos/day so you can cleanly archive the complete 2,050 video library across ~4 days without exceeding limits.

### Option 2: Stream in the Web Reader
Open the local reader or online viewer and click the **Debates & Videos** tab in the navigation bar to search, filter by duration/date, and stream any of the 2,050 debates in the built-in HTML5 player.

See the complete catalog in [`VIDEOS_CATALOG.md`](file:///Users/anshu_macmini/Downloads/aiaitv/VIDEOS_CATALOG.md) and [`iai_videos.json`](file:///Users/anshu_macmini/Downloads/aiaitv/iai_videos.json).

---

## 📖 Article Reading Room

An authentic IAI mobile/desktop reading room for all 2,180 articles:
- **Articles Library**: Searchable by keyword, author, channel (Philosophy, Science, Politics, Arts & Culture).
- **New Articles**: Incremental sync via GitHub Actions (`.github/workflows/update-articles.yml`) every 6 hours.
- **Reading Controls**: Floating accessibility widget with scale (90%–150%), high contrast, and link underlines.
- **Privacy**: Kept strictly private on GitHub.

### Run locally

Double-click `start_reader.command` on macOS, or run:

```bash
python3 scripts/build_reader.py
python3 -m http.server 8080 --bind 127.0.0.1 --directory dist
```

Then visit [http://127.0.0.1:8080](http://127.0.0.1:8080).

---

## Key Files

- `IAI_Cloud_Downloader.ipynb`: Google Colab cloud-to-cloud downloader for Google Drive.
- `VIDEOS_CATALOG.md`: Full catalog of 2,050 videos with direct streaming links.
- `iai_videos.json`: Machine-readable database of all video metadata.
- `articles/`: 2,180 archived unpaywalled articles in Markdown format.
- `articles_index.json` & `CATALOG.md`: Full articles catalog and metadata.
- `index.html`, `reader.js`, `css/reader.css`: Fast, responsive reader and video player.
- `scripts/build_videos_index.py`: Generator for video catalog and metadata.
- `scripts/build_reader.py`: Generator for static reader dist.
- `start_reader.command`: 1-click macOS launcher.

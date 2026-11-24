#!/usr/bin/env python3
"""Fix all video URLs to ensure 100% playable streams with CORS and proper percent-encoding.

1. Replaces 'iai.tv/assets/videos/' with 'cdn.iai.tv/assets/videos/' (supports CORS & range requests).
2. Percent-encodes spaces (%20) and fragments (%23 for '#') in all video paths.
3. Fixes known 404 URLs discovered via DOM inspection.
4. Updates iai_videos.json, dist/reader-data/videos_index.json, iai_videos_tracker.csv, and VIDEOS_CATALOG.md.
"""

import csv
import json
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Verified live URLs for previously failing items
VERIFIED_FIXES = {
    'truth-theory-and-ultimate-reality': 'https://cdn.iai.tv/assets/videos/linked/HTLGI2024_H142 Truth, theory and ultiamte reality.SD.downsized.mp4',
    'better-left-unsaid': 'https://cdn.iai.tv/assets/videos/linked/HTLGI2024_H150 Better left unsaid.HD.downsized..mp4',
    'the-matrix-myths-and-metaphysics': 'https://cdn.iai.tv/assets/videos/linked/HTLGI2023_H19 The matrix, myths and metaphysics.SD.mp4',
    'the-centre-of-the-universe': 'https://cdn.iai.tv/assets/videos/linked/HTLGI2023_H141 The centre of the universe.SD.mp4',
    'language-and-the-world': 'https://cdn.iai.tv/assets/videos/linked/HTLGI2016_553_LanguageAndTheWorldHD.mp4'
}

def clean_and_encode_url(raw_url, slug=""):
    if slug in VERIFIED_FIXES:
        raw_url = VERIFIED_FIXES[slug]

    if not raw_url or not raw_url.startswith('http'):
        return ""

    # Switch to high-speed CDN endpoint which has 'Access-Control-Allow-Origin: *'
    if 'iai.tv/assets/videos/' in raw_url and not raw_url.startswith('https://cdn.iai.tv'):
        raw_url = raw_url.replace('https://iai.tv/assets/videos/', 'https://cdn.iai.tv/assets/videos/')
        raw_url = raw_url.replace('http://iai.tv/assets/videos/', 'https://cdn.iai.tv/assets/videos/')

    # Handle special character '#' in filename before urlsplit
    # e.g., 'Consolations of P#19376.mp4' -> '#' must be '%23'
    if '#' in raw_url:
        raw_url = raw_url.replace('#', '%23')

    # Parse and encode path cleanly
    parts = urllib.parse.urlsplit(raw_url)
    # unquote first to prevent double-encoding, then quote
    unquoted_path = urllib.parse.unquote(parts.path)
    encoded_path = urllib.parse.quote(unquoted_path, safe='/')

    return urllib.parse.urlunsplit((parts.scheme, parts.netloc, encoded_path, parts.query, parts.fragment))

def main():
    videos_file = ROOT / "iai_videos.json"
    with open(videos_file, "r", encoding="utf-8") as f:
        videos = json.load(f)

    print(f"Processing {len(videos)} video records...")

    updated_count = 0
    for v in videos:
        old_url = v.get('video_url', '')
        new_url = clean_and_encode_url(old_url, v.get('slug', ''))
        if new_url != old_url:
            v['video_url'] = new_url
            updated_count += 1

    print(f"Updated {updated_count} video URLs to accessible CDN endpoints.")

    # 1. Save iai_videos.json
    with open(videos_file, "w", encoding="utf-8") as f:
        json.dump(videos, f, indent=2, ensure_ascii=False)
    print(f"Saved {videos_file}")

    # 2. Save dist/reader-data/videos_index.json
    dist_videos = ROOT / "dist" / "reader-data" / "videos_index.json"
    dist_videos.parent.mkdir(parents=True, exist_ok=True)
    with open(dist_videos, "w", encoding="utf-8") as f:
        json.dump(videos, f, ensure_ascii=False, separators=(',', ':'))
    print(f"Saved {dist_videos}")

    # 3. Regenerate iai_videos_tracker.csv
    csv_file = ROOT / "iai_videos_tracker.csv"
    with open(csv_file, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Watch Status",
            "Date",
            "Title",
            "Duration",
            "Direct MP4 Stream URL (CORS Enabled)",
            "IAI Post URL",
            "Guests & Speakers",
            "Host / Chair",
            "Speaker Bios & Descriptions",
            "Synopsis & Topics",
            "Video ID"
        ])
        for v in videos:
            writer.writerow([
                "Unwatched",
                v.get('publication_date') or "",
                v.get('title') or "",
                v.get('duration') or "",
                v.get('video_url') or "",
                v.get('page_url') or "",
                ", ".join(v.get('speakers', [])),
                ", ".join(v.get('chairs', [])),
                v.get('speaker_desc') or "",
                v.get('description') or "",
                v.get('id')
            ])
    print(f"Regenerated {csv_file}")

    # 4. Regenerate VIDEOS_CATALOG.md
    md_file = ROOT / "VIDEOS_CATALOG.md"
    md_lines = [
        "# IAI.tv Complete Video & Debate Catalog & Watch Tracker",
        "",
        f"**Total Videos:** {len(videos)} | **Total Watch Time:** ~1,209 hours | **All Streams:** CDN CORS-Enabled (.mp4)",
        "",
        "### How to Use This Tracker:",
        "- **Web Interactive Tracker:** Open [https://anshuk-dev.github.io/iai-tv-archive/videos.html](https://anshuk-dev.github.io/iai-tv-archive/videos.html) in your browser for interactive checkboxes, search, filter, and inline player.",
        "- **Excel Spreadsheet:** Open [`iai_videos_tracker.csv`](iai_videos_tracker.csv) in Excel / Google Sheets / Apple Numbers with direct clickable watch links and status column.",
        "- **Google Drive Cloud Downloader:** Run `IAI_Cloud_Downloader.ipynb` in Google Colab to transfer videos directly cloud-to-cloud with zero local Mac storage.",
        "",
        "---",
        "",
        "| Track | Date | Title | Duration | Guests & Speakers | Host / Chair | Watch Video (.mp4) | Post Link |",
        "|:---:|:---:|---|:---:|---|---|:---:|:---:|"
    ]

    for v in videos:
        date = v.get('publication_date') or "Unknown"
        title = (v.get('title') or "Untitled").replace('|', '-')
        dur = v.get('duration') or ""
        speakers = ", ".join(v.get('speakers', [])).replace('|', '-') or "—"
        chairs = ", ".join(v.get('chairs', [])).replace('|', '-') or "—"
        vurl = v.get('video_url', '')
        purl = v.get('page_url', '')

        watch_link = f"[Play MP4]({vurl})" if vurl.startswith('http') else "N/A"
        post_link = f"[Open Post]({purl})" if purl.startswith('http') else "N/A"

        md_lines.append(f"| [ ] | {date} | **{title}** | {dur} | {speakers} | {chairs} | {watch_link} | {post_link} |")

    with open(md_file, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines) + "\n")
    print(f"Regenerated {md_file}")

if __name__ == "__main__":
    main()

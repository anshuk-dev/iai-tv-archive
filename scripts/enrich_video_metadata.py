#!/usr/bin/env python3
"""Enrich IAI.tv video catalog with speakers, host (chairs), bios, and generate interactive trackers.

Outputs:
1. data/video_metadata_cache.json - Persistent cache of scraped metadata
2. iai_videos.json - Updated with speakers, chairs, speaker_desc, subtitle
3. dist/reader-data/videos_index.json - Synchronized for offline reader
4. iai_videos_tracker.csv - Excel / Google Sheets spreadsheet with clickable links & checkbox status
5. VIDEOS_CATALOG.md - Updated markdown catalog with tracking checkboxes
"""

import csv
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from scripts.fix_video_urls import clean_and_encode_url
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)
CACHE_FILE = DATA_DIR / "video_metadata_cache.json"

CTX = ssl._create_unverified_context()
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

def clean_text(text):
    if not text:
        return ""
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def fetch_metadata(v):
    url = v.get('page_url')
    slug = v.get('slug')
    vid_id = v.get('id')

    if not url:
        return {'id': vid_id, 'slug': slug, 'speakers': [], 'chairs': [], 'speaker_desc': '', 'subtitle': '', 'status': 'no_url'}

    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, context=CTX, timeout=12) as resp:
                html = resp.read().decode('utf-8', errors='ignore')

                speakers = []
                chairs = []
                speaker_desc = ''
                subtitle = ''

                m_sp = re.search(r'\"Speakers\":\s*(\[[^\]]*\])', html)
                if m_sp:
                    try: speakers = json.loads(m_sp.group(1))
                    except: pass

                m_ch = re.search(r'\"Chairs\":\s*(\[[^\]]*\])', html)
                if m_ch:
                    try: chairs = json.loads(m_ch.group(1))
                    except: pass

                m_sd = re.search(r'\"SpeakerDescription\":\s*\"(.*?)(?<!\\\\)\"', html)
                if m_sd:
                    try:
                        s = json.loads('\"' + m_sd.group(1) + '\"')
                        speaker_desc = clean_text(s)
                    except:
                        speaker_desc = clean_text(m_sd.group(1))

                m_sub = re.search(r'\"Subtitle\":\s*\"(.*?)(?<!\\\\)\"', html)
                if m_sub:
                    try: subtitle = json.loads('\"' + m_sub.group(1) + '\"')
                    except: subtitle = m_sub.group(1)

                # Fallback: if speakers still empty, check JSON-LD
                if not speakers:
                    ld_matches = re.findall(r'<script[^>]*type=[\"\']application/ld\+json[\"\'][^>]*>(.*?)</script>', html, re.DOTALL)
                    for ld in ld_matches:
                        try:
                            data = json.loads(ld)
                            authors = data.get('author', [])
                            for a in authors:
                                name = f"{a.get('givenName', '')} {a.get('familyName', '')}".strip()
                                u = a.get('url', '')
                                if not name:
                                    continue
                                if '/host/' in u:
                                    if name not in chairs: chairs.append(name)
                                else:
                                    if name not in speakers: speakers.append(name)
                        except:
                            pass

                return {
                    'id': vid_id,
                    'slug': slug,
                    'speakers': speakers,
                    'chairs': chairs,
                    'speaker_desc': speaker_desc,
                    'subtitle': subtitle,
                    'status': 'ok'
                }
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(2 * (attempt + 1))
            elif e.code == 404:
                return {'id': vid_id, 'slug': slug, 'speakers': [], 'chairs': [], 'speaker_desc': '', 'subtitle': '', 'status': '404'}
            else:
                time.sleep(1 + attempt)
        except Exception:
            time.sleep(1 + attempt)

    return {'id': vid_id, 'slug': slug, 'speakers': [], 'chairs': [], 'speaker_desc': '', 'subtitle': '', 'status': 'failed'}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

def main():
    videos_file = ROOT / "iai_videos.json"
    if not videos_file.exists():
        print(f"Error: {videos_file} not found.")
        sys.exit(1)

    with open(videos_file, "r", encoding="utf-8") as f:
        videos = json.load(f)

    print(f"Loaded {len(videos)} videos from {videos_file}")

    # Load cache
    cache = {}
    if CACHE_FILE.exists():
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                cache = json.load(f)
            print(f"Loaded {len(cache)} cached video metadata entries.")
        except Exception as e:
            print(f"Warning loading cache: {e}")

    # Determine tasks
    tasks = [v for v in videos if v.get('slug') not in cache or not cache[v.get('slug')].get('speakers')]
    print(f"Pending scrape: {len(tasks)} videos (Cached complete: {len(videos) - len(tasks)})")

    if tasks:
        t0 = time.time()
        completed = 0
        with ThreadPoolExecutor(max_workers=6) as pool:
            future_to_v = {pool.submit(fetch_metadata, v): v for v in tasks}
            for fut in as_completed(future_to_v):
                res = fut.result()
                slug = res['slug']
                cache[slug] = res
                completed += 1

                if completed % 50 == 0 or completed == len(tasks):
                    save_cache(cache)
                    elapsed = time.time() - t0
                    rate = completed / elapsed if elapsed > 0 else 0
                    print(f"Progress: {completed}/{len(tasks)} ({completed/len(tasks)*100:.1f}%) in {elapsed:.1f}s [{rate:.1f} req/s]")

        save_cache(cache)
        print(f"Scraping completed in {time.time()-t0:.1f}s.")

    # Enrich video records
    enriched_videos = []
    for v in videos:
        slug = v.get('slug')
        meta = cache.get(slug, {})

        speakers = meta.get('speakers', [])
        chairs = meta.get('chairs', [])
        speaker_desc = meta.get('speaker_desc', '')
        subtitle = meta.get('subtitle', '')

        # Fallback if no speakers found: parse from description or title
        if not speakers:
            m_with = re.search(r'with\s+([A-Z][a-zA-Z\s\.\-]+?)(?:\s+on|\s*$)', v.get('title', ''))
            if m_with:
                speakers = [m_with.group(1).strip()]

        v['speakers'] = speakers
        v['chairs'] = chairs
        v['speaker_desc'] = speaker_desc
        v['subtitle'] = subtitle
        v['video_url'] = clean_and_encode_url(v.get('video_url', ''), v.get('slug', ''))
        enriched_videos.append(v)

    # Save enriched iai_videos.json
    with open(videos_file, "w", encoding="utf-8") as f:
        json.dump(enriched_videos, f, indent=2, ensure_ascii=False)
    print(f"Saved enriched {len(enriched_videos)} records to {videos_file}")

    # Save to dist/reader-data/videos_index.json
    dist_videos = ROOT / "dist" / "reader-data" / "videos_index.json"
    dist_videos.parent.mkdir(parents=True, exist_ok=True)
    with open(dist_videos, "w", encoding="utf-8") as f:
        json.dump(enriched_videos, f, ensure_ascii=False, separators=(',', ':'))
    print(f"Saved web reader index to {dist_videos}")

    # Generate iai_videos_tracker.csv
    csv_file = ROOT / "iai_videos_tracker.csv"
    print(f"Generating {csv_file}...")
    with open(csv_file, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Watch Status",
            "Date",
            "Title",
            "Duration",
            "Direct MP4 Stream URL",
            "IAI Post URL",
            "Guests & Speakers",
            "Host / Chair",
            "Speaker Bios & Descriptions",
            "Synopsis & Topics",
            "Video ID"
        ])

        for v in enriched_videos:
            status = "Unwatched"
            date = v.get('publication_date') or ""
            title = v.get('title') or ""
            duration = v.get('duration') or ""
            video_url = v.get('video_url') or ""
            post_url = v.get('page_url') or ""
            speakers_str = ", ".join(v.get('speakers', []))
            chairs_str = ", ".join(v.get('chairs', []))
            speaker_desc = v.get('speaker_desc') or ""
            desc = v.get('description') or ""
            vid_id = v.get('id')

            writer.writerow([
                status,
                date,
                title,
                duration,
                video_url,
                post_url,
                speakers_str,
                chairs_str,
                speaker_desc,
                desc,
                vid_id
            ])
    print(f"Generated {csv_file} with {len(enriched_videos)} rows.")

    # Generate updated VIDEOS_CATALOG.md
    md_file = ROOT / "VIDEOS_CATALOG.md"
    print(f"Generating updated {md_file}...")
    md_lines = [
        "# IAI.tv Complete Video & Debate Catalog & Watch Tracker",
        "",
        f"**Total Videos:** {len(enriched_videos)} | **Total Watch Time:** ~1,209 hours | **Repository:** Private Archive",
        "",
        "### How to Use This Tracker:",
        "- **Web Interactive Tracker:** Open `dist/videos.html` in your browser for interactive checkboxes, search, filter, and inline player.",
        "- **Excel Spreadsheet:** Open `iai_videos_tracker.csv` in Excel / Google Sheets / Apple Numbers with direct clickable watch links and status column.",
        "- **Google Drive Cloud Downloader:** Run `IAI_Cloud_Downloader.ipynb` in Google Colab to transfer videos directly cloud-to-cloud with zero local Mac storage.",
        "",
        "---",
        "",
        "| Track | Date | Title | Duration | Guests & Speakers | Host / Chair | Watch Video (.mp4) | Post Link |",
        "|:---:|:---:|---|:---:|---|---|:---:|:---:|"
    ]

    for v in enriched_videos:
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
    print(f"Generated {md_file}")

if __name__ == "__main__":
    main()

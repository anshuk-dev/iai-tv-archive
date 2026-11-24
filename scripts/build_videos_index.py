#!/usr/bin/env python3
"""Build complete index of all 2,050 IAI.tv videos from sitemap and page metadata."""
import re
import ssl
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = Path(__file__).resolve().parents[1]
CTX = ssl._create_unverified_context()
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}

def fetch_sitemap():
    url = "https://iai.tv/VideoController/videoSitemap.xml"
    print(f"Fetching sitemap from {url}...")
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, context=CTX, timeout=30) as resp:
        return resp.read()

def fetch_page_video_url(page_url):
    try:
        req = urllib.request.Request(page_url, headers=HEADERS)
        with urllib.request.urlopen(req, context=CTX, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            m = re.search(r'\"contentUrl\":\s*\"(https://[^\"]+)\"', html)
            if m:
                return m.group(1).replace(r'\/', '/')
    except Exception as e:
        print(f"Failed to fetch fallback for {page_url}: {e}")
    return ""

def format_duration(seconds):
    if not seconds:
        return ""
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    if h > 0:
        return f"{h}h {m}m {s}s"
    return f"{m}m {s}s"

def sanitize_filename(name):
    # Keep safe chars, remove invalid filesystem chars
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    return name.strip()

def main():
    xml_data = fetch_sitemap()
    root = ET.fromstring(xml_data)
    ns = {
        'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9',
        'video': 'http://www.google.com/schemas/sitemap-video/1.1'
    }
    urls = root.findall('sm:url', ns)
    print(f"Found {len(urls)} video entries in sitemap.")

    records = []
    fallback_tasks = []

    for idx, u in enumerate(urls, 1):
        loc = u.find('sm:loc', ns).text.strip() if u.find('sm:loc', ns) is not None else ""
        slug = loc.split('/')[-1] if loc else f"video-{idx}"
        v = u.find('video:video', ns)

        title = v.find('video:title', ns).text.strip() if (v is not None and v.find('video:title', ns) is not None and v.find('video:title', ns).text) else slug.replace('-', ' ').title()
        desc = v.find('video:description', ns).text.strip() if (v is not None and v.find('video:description', ns) is not None and v.find('video:description', ns).text) else ""
        content_loc = v.find('video:content_loc', ns).text.strip() if (v is not None and v.find('video:content_loc', ns) is not None and v.find('video:content_loc', ns).text) else ""
        thumb = v.find('video:thumbnail_loc', ns).text.strip() if (v is not None and v.find('video:thumbnail_loc', ns) is not None and v.find('video:thumbnail_loc', ns).text) else ""
        dur_str = v.find('video:duration', ns).text.strip() if (v is not None and v.find('video:duration', ns) is not None and v.find('video:duration', ns).text) else ""
        pub = v.find('video:publication_date', ns).text.strip() if (v is not None and v.find('video:publication_date', ns) is not None and v.find('video:publication_date', ns).text) else ""

        duration_sec = int(dur_str) if dur_str.isdigit() else 0

        record = {
            "id": idx,
            "slug": slug,
            "title": title,
            "page_url": loc,
            "video_url": content_loc,
            "thumbnail_url": thumb,
            "duration_seconds": duration_sec,
            "duration": format_duration(duration_sec),
            "publication_date": pub,
            "description": desc,
            "filename": ""
        }

        if not content_loc or not content_loc.endswith('.mp4'):
            fallback_tasks.append(record)
        else:
            raw_fn = urllib.parse.unquote(content_loc.split('/')[-1])
            record["filename"] = sanitize_filename(raw_fn)

        records.append(record)

    if fallback_tasks:
        print(f"Fetching {len(fallback_tasks)} missing/fallback video URLs concurrently...")
        with ThreadPoolExecutor(max_workers=8) as pool:
            future_to_rec = {pool.submit(fetch_page_video_url, rec["page_url"]): rec for rec in fallback_tasks}
            for fut in as_completed(future_to_rec):
                rec = future_to_rec[fut]
                url = fut.result()
                if url:
                    rec["video_url"] = url
                    raw_fn = urllib.parse.unquote(url.split('/')[-1])
                    rec["filename"] = sanitize_filename(raw_fn)
                    print(f"Resolved fallback for {rec['slug']} -> {raw_fn}")
                else:
                    rec["filename"] = sanitize_filename(f"{rec['slug']}.mp4")

    # Fix any empty filename or duplicate filenames
    seen_filenames = {}
    for r in records:
        fn = r["filename"]
        if not fn or not fn.endswith('.mp4'):
            fn = sanitize_filename(f"{r['slug']}.mp4")
        if fn in seen_filenames:
            seen_filenames[fn] += 1
            stem = fn[:-4]
            fn = f"{stem}_{seen_filenames[fn]}.mp4"
        else:
            seen_filenames[fn] = 1
        r["filename"] = fn

    # Ensure clean, CORS-enabled CDN streaming URLs with proper percent-encoding
    try:
        from scripts.fix_video_urls import clean_and_encode_url
        for r in records:
            r["video_url"] = clean_and_encode_url(r.get("video_url", ""), r.get("slug", ""))
    except Exception as e:
        print(f"URL encoding warning: {e}")

    # Save iai_videos.json
    out_json = ROOT / "iai_videos.json"
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(records)} video records to {out_json}")

    # Also save to dist/reader-data/videos_index.json for offline web reader
    reader_videos_json = ROOT / "dist" / "reader-data" / "videos_index.json"
    reader_videos_json.parent.mkdir(parents=True, exist_ok=True)
    with open(reader_videos_json, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, separators=(',', ':'))
    print(f"Saved web reader video index to {reader_videos_json}")

    # Generate VIDEOS_CATALOG.md
    print("Generating VIDEOS_CATALOG.md...")
    md_lines = [
        "# IAI.tv Complete Video & Debate Catalog",
        "",
        f"**Total Videos:** {len(records)} | **Total Watch Time:** ~1,209 hours (~50.4 days) | **Cloud Destination:** Google Drive (`/content/drive/MyDrive/IAI_Videos`)",
        "",
        "This catalog contains all 2,050 high-definition debate and talk videos from the [Institute of Art and Ideas](https://iai.tv).",
        "All videos can be transferred directly to Google Drive cloud-to-cloud with zero local disk usage using the included `IAI_Cloud_Downloader.ipynb` Google Colab notebook, or streamed directly in the web reader.",
        "",
        "---",
        "",
        "| # | Date | Duration | Title | Direct Video Stream (.mp4) |",
        "|---|---|---|---|---|"
    ]

    for r in records:
        date_str = r['publication_date'] or 'Unknown'
        dur_str = r['duration'] or 'Unknown'
        title_esc = r['title'].replace('|', '-')
        vurl = r['video_url']
        link_str = f"[Play MP4]({vurl})" if vurl.startswith('http') else "N/A"
        md_lines.append(f"| {r['id']} | {date_str} | {dur_str} | [{title_esc}]({r['page_url']}) | {link_str} |")

    cat_path = ROOT / "VIDEOS_CATALOG.md"
    with open(cat_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines) + "\n")
    print(f"Generated {cat_path}")

    # Automatically enrich with speakers, host, bios, tracker spreadsheet, and interactive web tracker
    try:
        import sys
        sys.path.insert(0, str(ROOT))
        from scripts.enrich_video_metadata import main as enrich_main
        enrich_main()
    except Exception as e:
        print(f"Video enrichment warning: {e}")

if __name__ == "__main__":
    main()

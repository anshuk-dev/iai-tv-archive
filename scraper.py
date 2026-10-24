#!/usr/bin/env python3
"""
IAI.tv Article Scraper & Markdown Archiver
==========================================
Uses the Bypass Paywalls Clean (BPC) method to extract complete unpaywalled
article content from IAI.tv via meta tag inspection and content fallback,
converting all articles into cleanly structured Markdown files with frontmatter.
"""

import os
import re
import sys
import json
import time
import logging
import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import xml.etree.ElementTree as ET

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from tqdm import tqdm

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger("iai_scraper")

SITEMAP_URL = "https://iai.tv/ArticlePage_Controller/articleSitemap.xml"
DEFAULT_OUTPUT_DIR = Path("./articles")
INDEX_JSON_PATH = Path("./articles_index.json")
INDEX_MD_PATH = Path("./CATALOG.md")
FAILED_URLS_PATH = Path("./failed_urls.txt")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://iai.tv/articles",
}


def create_session(pool_size: int = 25) -> requests.Session:
    session = requests.Session()
    session.headers.update(HEADERS)
    retry_strategy = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        raise_on_status=False
    )
    adapter = HTTPAdapter(
        max_retries=retry_strategy,
        pool_connections=pool_size,
        pool_maxsize=pool_size
    )
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def get_all_article_urls(session: requests.Session) -> list[str]:
    """Fetch sitemap and extract all article URLs containing -auid-."""
    logger.info(f"Fetching sitemap from {SITEMAP_URL}...")
    resp = session.get(SITEMAP_URL, timeout=30)
    resp.raise_for_status()

    root = ET.fromstring(resp.content)
    namespace = {"ns": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    all_locs = [elem.text.strip() for elem in root.findall(".//ns:loc", namespace) if elem.text]

    # Filter out categories and generic URLs, keep -auid- articles
    article_urls = [
        u for u in all_locs
        if "-auid-" in u and "/articles/" in u
    ]
    logger.info(f"Found {len(article_urls)} total article URLs in sitemap.")
    return article_urls


def sanitize_filename(name: str) -> str:
    """Ensure filename is safe across all platforms."""
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    return name.strip()


def parse_article_html(html: str, url: str) -> dict | None:
    """
    Extract article content using the Bypass Paywalls Clean (BPC) method:
    - Primary: <meta name="twitter:description" content="..."> which contains full article HTML
    - Secondary fallback: full body content container
    """
    soup = BeautifulSoup(html, "html.parser")

    # Title
    title = ""
    h1 = soup.find("h1", class_="iai-article--heading")
    if h1 and h1.get_text(strip=True):
        title = h1.get_text(strip=True)
    if not title:
        og_title = soup.find("meta", property="og:title")
        if og_title and og_title.get("content"):
            title = og_title["content"].strip()
            title = re.sub(r"\s*[»|]\s*IAI\s*TV.*$", "", title, flags=re.IGNORECASE)
    if not title and soup.title:
        title = re.sub(r"\s*[»|]\s*IAI\s*TV.*$", "", soup.title.get_text(strip=True), flags=re.IGNORECASE)

    if not title:
        slug = url.rstrip("/").split("/")[-1]
        title = slug.replace("-", " ").title()

    # Subheading
    subheading = ""
    h2_sub = soup.find("h2", class_="iai-article--subheading")
    if h2_sub:
        subheading = h2_sub.get_text(strip=True)

    # Author
    author = ""
    h2_author = soup.find("h2", class_="iai-article--author")
    if h2_author and h2_author.get_text(strip=True):
        author = h2_author.get_text(strip=True)
    elif soup.find("strong", class_="iai-article--author"):
        author = soup.find("strong", class_="iai-article--author").get_text(strip=True)

    # Date
    date = ""
    date_div = soup.find("div", class_="iai-article--date")
    if date_div:
        date = date_div.get_text(strip=True)

    # Word count and read time
    word_count = ""
    wc_el = soup.find("div", class_="iai-article--word-count")
    if wc_el:
        word_count = wc_el.get_text(strip=True)

    read_time = ""
    rt_el = soup.find("div", class_="iai-article--read-time")
    if rt_el:
        read_time = rt_el.get_text(strip=True)

    # dataLayer direct extraction
    channel = ""
    themes = ""
    tags = ""
    author_dl = ""
    date_dl = ""

    for key in ["channel", "themes", "tags", "author", "upload_date"]:
        m = re.search(r"[\x27\"]" + key + r"[\x27\"]\s*:\s*[\x27\"]([^\x27\"]*)[\x27\"]", html)
        if m:
            val = m.group(1).strip()
            if key == "channel": channel = val
            elif key == "themes": themes = val
            elif key == "tags": tags = val
            elif key == "author": author_dl = val
            elif key == "upload_date": date_dl = val

    if not author and author_dl:
        author = author_dl
    if not date and date_dl:
        date = date_dl

    # Header image
    header_image = ""
    og_img = soup.find("meta", property="og:image")
    if og_img and og_img.get("content"):
        header_image = og_img["content"]

    # ==========================================
    # BPC Unpaywall Extraction Method
    # ==========================================
    meta_tw = soup.find("meta", attrs={"name": "twitter:description"})
    tw_content = meta_tw.get("content", "").strip() if meta_tw else ""

    # Alternative body extraction
    body_div = (
        soup.find(class_="article-post-content--full")
        or soup.find(class_="iai-article--content-inner")
        or soup.find(class_="iai-article--content")
    )
    if body_div:
        for pw in body_div.find_all(class_=lambda c: c and ("paywall" in c or "disruption" in c)):
            pw.decompose()
        body_html = str(body_div).strip()
    else:
        body_html = ""

    # Choose the most complete content source (BPC twitter:description vs page body)
    if len(tw_content) >= len(body_html):
        unpaywall_source = "BPC twitter:description meta"
        content_html = tw_content
    elif body_html:
        unpaywall_source = "body HTML container"
        content_html = body_html
    else:
        unpaywall_source = "none"
        content_html = tw_content or ""

    if not content_html or not content_html.strip():
        # Fallback if page is an empty placeholder or editorial stub
        markdown_content = "*[No body content available on IAI.tv for this article (editorial placeholder stub)]*"
    else:
        # Convert HTML to clean Markdown
        markdown_content = md(
            content_html,
            heading_style="ATX",
            strip=["script", "style"]
        ).strip()

    if not markdown_content:
        markdown_content = "*[No body content available on IAI.tv for this article (editorial placeholder stub)]*"

    # Convert relative links and images to absolute URLs
    markdown_content = re.sub(r"\]\((/(?:assets|articles|video)[^\)]*)\)", r"](https://iai.tv\1)", markdown_content)
    markdown_content = re.sub(r"\]\(((?:video|articles)/[^\)]*)\)", r"](https://iai.tv/\1)", markdown_content)

    # Clean redundant blank lines (more than 2 consecutive newlines)
    markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)

    slug = url.rstrip("/").split("/")[-1]
    auid_match = re.search(r"-auid-(\d+)", slug)
    article_id = auid_match.group(1) if auid_match else ""

    return {
        "id": article_id,
        "slug": slug,
        "url": url,
        "title": title,
        "subheading": subheading,
        "author": author,
        "date": date,
        "channel": channel,
        "themes": themes,
        "tags": tags,
        "word_count": word_count,
        "read_time": read_time,
        "header_image": header_image,
        "unpaywall_method": unpaywall_source,
        "content_length": len(markdown_content),
        "markdown_body": markdown_content
    }


def format_markdown_file(meta: dict) -> str:
    """Assemble frontmatter and body into Markdown string."""
    title_escaped = meta["title"].replace('"', '\\"')
    sub_escaped = meta["subheading"].replace('"', '\\"')
    author_escaped = meta["author"].replace('"', '\\"')

    lines = [
        "---",
        f'title: "{title_escaped}"',
        f'subtitle: "{sub_escaped}"',
        f'author: "{author_escaped}"',
        f'date: "{meta["date"]}"',
        f'article_id: "{meta["id"]}"',
        f'channel: "{meta["channel"]}"',
        f'themes: "{meta["themes"]}"',
        f'tags: "{meta["tags"]}"',
        f'word_count: "{meta["word_count"]}"',
        f'read_time: "{meta["read_time"]}"',
        f'header_image: "{meta["header_image"]}"',
        f'unpaywall_method: "{meta["unpaywall_method"]}"',
        f'source_url: "{meta["url"]}"',
        "---",
        "",
        f'# {meta["title"]}',
        ""
    ]

    if meta["subheading"]:
        lines.append(f'*{meta["subheading"]}*')
        lines.append("")

    meta_parts = []
    if meta["author"]:
        meta_parts.append(f'**By {meta["author"]}**')
    if meta["date"]:
        meta_parts.append(f'*{meta["date"]}*')
    if meta["read_time"]:
        meta_parts.append(f'*{meta["read_time"]}*')
    if meta["word_count"]:
        meta_parts.append(f'*{meta["word_count"]}*')

    if meta_parts:
        lines.append(" | ".join(meta_parts))
        lines.append("")

    if meta["header_image"]:
        lines.append(f'![{meta["title"]}]({meta["header_image"]})')
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(meta["markdown_body"])
    lines.append("")

    return "\n".join(lines)


def process_url(url: str, session: requests.Session, output_dir: Path) -> dict:
    slug = url.rstrip("/").split("/")[-1]
    safe_slug = sanitize_filename(slug)
    file_path = output_dir / f"{safe_slug}.md"

    # Skip if file already exists and is non-empty
    if file_path.exists() and file_path.stat().st_size > 100:
        return {"status": "skipped", "url": url, "path": str(file_path), "slug": slug}

    try:
        resp = session.get(url, timeout=25)
        if resp.status_code != 200:
            return {"status": "error", "url": url, "error": f"HTTP {resp.status_code}"}

        article_data = parse_article_html(resp.text, url)
        if not article_data or not article_data["markdown_body"]:
            return {"status": "error", "url": url, "error": "No article content extracted"}

        full_md = format_markdown_file(article_data)
        file_path.write_text(full_md, encoding="utf-8")

        return {
            "status": "success",
            "url": url,
            "path": str(file_path),
            "slug": slug,
            "id": article_data["id"],
            "title": article_data["title"],
            "author": article_data["author"],
            "date": article_data["date"],
            "themes": article_data["themes"],
            "word_count": article_data["word_count"],
            "unpaywall_method": article_data["unpaywall_method"],
            "content_length": article_data["content_length"]
        }
    except Exception as e:
        return {"status": "error", "url": url, "error": str(e)}


def generate_catalog_files(successful_entries: list[dict], output_dir: Path):
    """Write articles_index.json and CATALOG.md"""
    try:
        sorted_entries = sorted(
            successful_entries,
            key=lambda x: int(x["id"]) if x.get("id") and x["id"].isdigit() else 0,
            reverse=True
        )
    except Exception:
        sorted_entries = successful_entries

    INDEX_JSON_PATH.write_text(json.dumps(sorted_entries, indent=2, ensure_ascii=False), encoding="utf-8")

    md_lines = [
        "# IAI.tv Articles Catalog",
        "",
        f"Total downloaded posts: **{len(sorted_entries)}**",
        "",
        "| ID | Title | Author | Date | Themes | File |",
        "|:---|:---|:---|:---|:---|:---|"
    ]

    for item in sorted_entries:
        title = item.get("title", "").replace("|", "-")
        author = item.get("author", "").replace("|", "-")
        date = item.get("date", "").replace("|", "-")
        themes = item.get("themes", "").replace("|", "-")
        item_id = item.get("id", "")
        slug = item.get("slug", "")
        file_link = f"[{slug}.md](./articles/{slug}.md)"
        md_lines.append(f"| {item_id} | {title} | {author} | {date} | {themes} | {file_link} |")

    INDEX_MD_PATH.write_text("\n".join(md_lines), encoding="utf-8")
    logger.info(f"Generated catalog with {len(sorted_entries)} entries at {INDEX_MD_PATH} and {INDEX_JSON_PATH}")


def main():
    parser = argparse.ArgumentParser(description="Scrape and unpaywall all IAI.tv articles to Markdown.")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of articles to download (0 for all).")
    parser.add_argument("--workers", type=int, default=16, help="Number of concurrent download threads.")
    parser.add_argument("--output", type=str, default=str(DEFAULT_OUTPUT_DIR), help="Output directory for markdown files.")
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    session = create_session(pool_size=args.workers + 5)
    urls = get_all_article_urls(session)

    if args.limit > 0:
        urls = urls[:args.limit]
        logger.info(f"Limiting to first {args.limit} articles.")

    logger.info(f"Starting download of {len(urls)} articles with {args.workers} workers...")

    results = []
    failed_urls = []
    success_count = 0
    skipped_count = 0
    error_count = 0

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(process_url, url, session, output_dir): url for url in urls}

        with tqdm(total=len(urls), desc="Scraping IAI.tv Articles", unit="article") as pbar:
            for future in as_completed(futures):
                res = future.result()
                results.append(res)
                if res["status"] == "success":
                    success_count += 1
                elif res["status"] == "skipped":
                    skipped_count += 1
                else:
                    error_count += 1
                    failed_urls.append(f"{res['url']} - {res.get('error', 'Unknown')}\n")

                pbar.update(1)
                pbar.set_postfix({
                    "saved": success_count,
                    "cached": skipped_count,
                    "failed": error_count
                })

    if failed_urls:
        FAILED_URLS_PATH.write_text("".join(failed_urls), encoding="utf-8")
        logger.warning(f"{len(failed_urls)} URLs failed. Logged to {FAILED_URLS_PATH}")

    # Build catalog of all articles in output_dir
    logger.info("Scanning output directory to generate complete catalog index...")
    all_articles = []
    for md_file in output_dir.glob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
            title_m = re.search(r'^title:\s*"(.*)"$', content, re.MULTILINE)
            author_m = re.search(r'^author:\s*"(.*)"$', content, re.MULTILINE)
            date_m = re.search(r'^date:\s*"(.*)"$', content, re.MULTILINE)
            id_m = re.search(r'^article_id:\s*"(.*)"$', content, re.MULTILINE)
            themes_m = re.search(r'^themes:\s*"(.*)"$', content, re.MULTILINE)
            method_m = re.search(r'^unpaywall_method:\s*"(.*)"$', content, re.MULTILINE)

            slug = md_file.stem
            all_articles.append({
                "id": id_m.group(1) if id_m else "",
                "slug": slug,
                "title": title_m.group(1) if title_m else slug,
                "author": author_m.group(1) if author_m else "",
                "date": date_m.group(1) if date_m else "",
                "themes": themes_m.group(1) if themes_m else "",
                "unpaywall_method": method_m.group(1) if method_m else "",
                "file_path": str(md_file.relative_to(output_dir.parent))
            })
        except Exception:
            pass

    generate_catalog_files(all_articles, output_dir)

    print("\n" + "=" * 60)
    print("Scraping Summary:")
    print(f"  Total URLs targeted:  {len(urls)}")
    print(f"  Newly downloaded:     {success_count}")
    print(f"  Previously cached:    {skipped_count}")
    print(f"  Failed:               {error_count}")
    print(f"  Total files in catalog: {len(all_articles)}")
    print(f"  Articles directory:   {output_dir.resolve()}")
    print(f"  Catalog index:        {INDEX_MD_PATH.resolve()}")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()

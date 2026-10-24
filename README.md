# IAI.tv Full Article Archiver & Unpaywaller

🌐 **Live Web Reader:** [https://anshuk-dev.github.io/iai-tv-archive/](https://anshuk-dev.github.io/iai-tv-archive/)

[![GitHub Pages](https://img.shields.io/badge/Live%20Website-GitHub%20Pages-success.svg?style=flat&logo=github)](https://anshuk-dev.github.io/iai-tv-archive/)
[![Continuous Sync](https://github.com/anshuk-dev/iai-tv-archive/actions/workflows/update-articles.yml/badge.svg)](https://github.com/anshuk-dev/iai-tv-archive/actions/workflows/update-articles.yml)
[![Total Articles](https://img.shields.io/badge/articles-2%2C180%20archived-blue.svg)](./CATALOG.md)
[![Format](https://img.shields.io/badge/format-HTML%20%2B%20Markdown-green.svg)](https://anshuk-dev.github.io/iai-tv-archive/)

A complete unpaywalled archive and continuous auto-updating mirror of **[IAI.tv](https://iai.tv)** (The Institute of Art and Ideas) articles and posts, implementing the **Bypass Paywalls Clean (BPC)** unpaywall extraction method.

---

## 🌐 Live Web Reader (Interactive Webpage)

You can read all articles directly in your browser with full HTML formatting, search, and dark mode at:
👉 **[https://anshuk-dev.github.io/iai-tv-archive/](https://anshuk-dev.github.io/iai-tv-archive/)**

- **Instant Search:** Search across 2,180 articles by title, author, keyword, or ID.
- **Theme Filtering:** Filter by Philosophy, Science, Art & Culture, Politics, etc.
- **Reader Mode:** Clean typography, font size controls, dark/light theme, and direct sharing URLs (`#article=<slug>`).

---

## 📚 Complete Article Catalog (Markdown)

Browse the complete indexed catalog of all 2,180 articles:
👉 **[CATALOG.md](./CATALOG.md)** (Contains titles, authors, release dates, themes, and direct links to each markdown file).

A structured machine-readable JSON database is also available at:
👉 **[`articles_index.json`](./articles_index.json)**

---

## ⚡ How It Works: The BPC Unpaywall Technique

[Bypass Paywalls Clean (BPC)](https://gitflic.ru/project/magnolia1234/bpc) targets `iai.tv` using the following rule:

```javascript
else if (matchDomain('iai.tv')) {
  let paywall = document.querySelector('div.article-paywall-main');
  if (paywall && dompurify_loaded) {
    removeDOMElement(paywall);
    let article = document.querySelector('div > div.iai-article--content-inner');
    if (article) {
      let content_new = document.querySelector('head > meta[name="twitter:description"][content]');
      if (content_new) {
        let parser = new DOMParser();
        let doc = parser.parseFromString('<div>' + DOMPurify.sanitize(content_new.content, dompurify_options) + '</div>', 'text/html');
        let article_new = doc.querySelector('div');
        article.parentNode.replaceChild(article_new, article);
      }
    }
  }
}
```

### The Mechanism
1. On `iai.tv`, when a user is not logged in or unsubscribed, the web page truncates the visible body with an subscription wall (`div.article-paywall-main`).
2. However, for search engine crawlers and social share previews (Twitter / X), `iai.tv` serves the **full, complete article text** within `<meta name="twitter:description" content="...">` in the HTML `<head>`.
3. Our scraper uses this exact method:
   - Fetches the article page.
   - Extracts the full unpaywalled content from `<meta name="twitter:description">` (with automated fallback to `.article-post-content--full` or `.iai-article--content-inner`).
   - Cleans and parses HTML using `BeautifulSoup`.
   - Converts formatting, headings, links, blockquotes, and lists into Markdown via `markdownify`.
   - Resolves relative URLs (`/assets/...`, `/articles/...`) into absolute URLs.
   - Generates YAML frontmatter containing article metadata (Title, Subtitle, Author, Date, Channel, Themes, Tags, Word Count, Header Image, and Source URL).

---

## 🔄 Automated Continuous Updates (GitHub Actions)

This repository includes a daily GitHub Actions cron workflow (`.github/workflows/update-articles.yml`):
- Runs **every day at 06:00 UTC**.
- Automatically queries `https://iai.tv/ArticlePage_Controller/articleSitemap.xml`.
- Downloads any newly published articles.
- Updates [`CATALOG.md`](./CATALOG.md) and [`articles_index.json`](./articles_index.json).
- Commits and pushes new articles directly to `main`.

---

## 📁 Repository Structure

```
.
├── articles/                   # All 2,180+ downloaded articles in .md format
│   ├── <slug>-auid-<id>.md
│   └── ...
├── CATALOG.md                  # Complete searchable Markdown catalog of all articles
├── articles_index.json         # JSON database of all articles with metadata
├── scraper.py                  # Multi-threaded BPC scraper script
├── requirements.txt            # Python dependencies
├── .github/workflows/          # GitHub Actions daily automated updater
└── README.md                   # Project documentation
```

---

## 🚀 Running Locally

```bash
# Clone the repository
git clone https://github.com/anshuk-dev/iai-tv-archive.git
cd iai-tv-archive

# Install dependencies
pip install -r requirements.txt

# Run the scraper (cached files are skipped automatically)
python scraper.py --workers 8
```

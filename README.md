# IAI — Private Reading Room

Private URL: **https://iai-private-reading-room.savoryrain2.chatgpt.site**

Open with the owning ChatGPT account. The hosted reader is owner-private; other visitors cannot access its articles or data.

A responsive editorial reader for 2,180 locally archived IAI.tv articles. It follows the supplied IAI mobile layout: Arial typography, compact black header, red category navigation, white reading column, rectangular artwork, spacious metadata and italic introduction. The original Markdown files and article index remain unchanged.

- **Home** opens the searchable library; categories, sorting and pagination help browse.
- Direct links retain `#article=<slug>`.
- **Share** shares a private reader link; **cite** copies a source citation.
- The floating accessibility button controls text size, contrast and link underlines.
- **Subscribe / Sign In** open the original IAI website. ChatGPT sign-in protects this private reader separately.

## Run locally

Install dependencies from `requirements.txt`, then double-click `start_reader.command`, or run:

```bash
python3 scripts/build_reader.py
python3 -m http.server 8080 --bind 127.0.0.1 --directory dist
```

Open http://127.0.0.1:8080. Serve the generated `dist/` directory rather than the repository root.

## Files

- `articles/`: unchanged source Markdown.
- `articles_index.json`: unchanged archive index.
- `index.html`, `reader.js`, `css/reader.css`: reusable data-driven reader components.
- `scripts/build_reader.py`: creates `dist/` with rendered article JSON and catalog.
- `sites/iai-private/`: private Sites checkout and persisted hosting identity.
- `READER_DEPLOYMENT.md`: build, private publishing and validation details.
- `scraper.py`: existing archive maintenance utility; not run during this redesign.

The current Site is a published snapshot. Existing archive maintenance does not automatically republish the ChatGPT Site. Most article artwork still loads from the original IAI CDN; the reference article artwork is local. One original entry (ID 504) is a placeholder without body text.

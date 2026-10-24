# Private IAI reader

Site: https://iai-private-reading-room.savoryrain2.chatgpt.site

Open with the owning ChatGPT account. Hosting access is custom/owner-only (one owner, no groups or external visitors). Subscribe and Sign In in the replica header open the original IAI service; ChatGPT controls access to this private reader separately.

## Build and preview

Install requirements.txt, then run `python3 scripts/build_reader.py`. Serve `dist/` or double-click `start_reader.command`. The build preserves all original Markdown and generates 2,180 article JSONs, a search catalog, HTML/CSS/JS and local reference artwork.

Default page is the supplied atheism article. `#library` opens all articles; `#article=<original-slug>` links directly. Search covers title, author, subtitle, channel, theme and ID. Category filtering, sorting and pagination work locally. Share copies a private link (or opens native sharing); Cite formats the original source. Accessibility controls change text size, contrast and link underlines, persisted per browser.

Only the reference article's caption and biography were verified from the original webpage. Other articles show available source metadata without invented biographies or captions. Most images remain external CDN resources. One original archive item (ID 504) is an editorial placeholder without a body; preserved as such.

## Publish updates

Reuse project ID in `sites/iai-private/.openai/hosting.json`. Build first, copy the resulting dist into the Site checkout, then use official Sites `site-workflow.mjs` with a fresh repository credential via stdin to commit/push/package. Pass its exact commit and archive to owner-private deployment. Never push to the separate GitHub archive as part of this workflow. Source Markdown changes require their own authorized scope.

## Verification

Rendered at 320px, 393px and desktop (1280/1600px). Measured no horizontal overflow; mobile header 34px/nav 40px, 16px gutters at 393px, 22px headline, 18px subtitle, 16px caption, 20px/31px intro, 19px/28.5px body, 70px intro-to-body gap. Desktop reading container 740px including padding. Tested author search, citation dialog, text-size/reset, library routes, and nonsticky header. All 2,180 generated JSON files validated; original article files not edited. No supplied screenshot attachments were available for a pixel-difference comparison.

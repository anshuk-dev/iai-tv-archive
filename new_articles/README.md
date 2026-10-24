# New Articles (Auto-Updated)

This directory automatically stores any new articles published on [IAI.tv](https://iai.tv) after the initial archive snapshot of 2,180 articles.

Whenever the automated GitHub Actions sync workflow runs:
1. It detects any newly published article not present in `baseline_ids.json`.
2. It extracts and unpaywalls the article using the BPC method.
3. It saves the Markdown file right here in `new_articles/<slug>.md` (as well as indexing it in the main archive).
4. It updates the live web reader with a **[NEW]** badge.

# Paper PKM guide — version retention policy

Applies to both `ja/paper-pkm/` and `en/paper-pkm/`.

Before **every future edit** to either language's `index.html` or `guide.md`:

1. Read the four current files from the same Git commit.
2. Copy all four unchanged into `ja/paper-pkm/versions/YYYY-MM-DD-vN/` and `en/paper-pkm/versions/YYYY-MM-DD-vN/` respectively (use a unique suffix if needed).
3. Commit the archive **before** editing the current pages. Never overwrite or delete archived versions.
4. Update both languages together; retain diagrams and links to previous editions.
5. Add links from the current pages to the archived edition and verify both versions render.
6. Keep Git history as an additional recovery mechanism.

Baseline preserved: `versions/2026-11-11-before-update/` in both languages, containing the original HTML and Markdown files.

**Important:** This is an editorial procedure, not an automated GitHub Action. Any future editor must follow it. Git commit history itself also retains previous revisions.

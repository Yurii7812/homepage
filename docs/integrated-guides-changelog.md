# Integrated guides — 2026-11-11

- Archived both language home pages, both paper guides and both YuriiNote guides before editing.
- Preserved the existing paper workflow and its detailed examples. Added a twelve-entry diagram directory, three vector diagrams (structure, navigation and a worked coffee example), and keyboard-accessible enlargement for all diagrams.
- Removed obsolete application-specific instructions from the paper-only workflow.
- Replaced the brief app overview with matching Japanese and English step-by-step guides generated from `yuriinote-guide.json`: 18 sections, numbered actual Electron screenshots, implementation source links and explicit development/release status.
- Corrected the roleplay creation instructions to match the current integrated character controls in chat memos.
- Kept the existing repository and guide links; added direct cross-language paper-guide links without duplicating the YuriiNote links.
- The source changes are prepared on a review branch. Publishing these sources at the existing GitHub Pages URLs requires the site's publication workflow; an open PR alone does not update the live site.

## Verification

Run `python scripts/build-yuriinote-guides.py` then `python scripts/validate-guides.py`.
Actual screenshots use sample data and the Japanese UI, captured in the Linux Electron development app. Physical Android USB transfer, packaged updates and Windows/macOS installer execution were not tested.

## Source implementation

YuriiNote implementation: [PR #9](https://github.com/Yurii7812/YuriiNote/pull/9), based on the inspected changes in PR #8. App checks: **147/147 tests passed**, build passed. The app has not been merged or released.

## Checks completed

- Six current HTML pages: **176 local links/assets** checked.
- Japanese/English anchors, section IDs and step counts match.
- Paper guide: **27 figures per language**. App guide: **18 sections and 22 figures per language**, using 18 actual screenshot assets.
- Enlargement controls: syntax check and DOM interaction check passed on all four guides (open/close).
- Responsive CSS is supplied. Actual browser rendering, visual layout on mobile and native-dialog Escape behavior in a browser were not verified because the cloud browser cannot access the local preview server. DOM tests mock the native dialog open/close API.

## Publication status

These are source changes on a review branch. Neither this PR nor app PR #9 has been merged. The existing public URLs have not been updated by this work:

- https://yurii7812.github.io/homepage/ja/paper-pkm/
- https://yurii7812.github.io/homepage/en/paper-pkm/
- https://yurii7812.github.io/homepage/ja/yuriinote/
- https://yurii7812.github.io/homepage/en/yuriinote/

## 2026-11-11 — Explain the design through problems

- Added a progressive, bilingual illustrated introduction: one A4 sheet, eight problems and their solutions, then the combined Double Index System.
- Added ten precise SVG diagrams per language. Branching appears first, cross-references next, Topic Index next, and Global Index after the reader encounters the need for it. The combined diagram is deliberately withheld until the end of the introduction.
- Kept one consistent bag/shopping/travel example. Travel supplies use ID 27; appliance comparisons use 28 so one ID never changes meaning mid-example.
- Moved the earlier benefits, diagram directory and ready-made overview after the practical guide.
- Kept the detailed paper workflow; aligned the older red-dot text and tables with the newly stated meaning: a Topic Index exists for that ID. The red dot remains distinct from a summary/progress ●.
- Presented gaps and index-creation timing as working conventions that can be refined through examples.
- Archived the HTML/Markdown pages before this revision; updated both Markdown companions and both home-page summaries.
- Verified local links, bilingual anchors, progressive diagram order, SVG parsing and raster rendering. Website/browser visual QA remains unverified as described above. Publication remains pending; this updates the existing review branch.

# S01E03 — what it shows

Prepared for Abilyne with Codex on 2026-11-01. This repository contains the course's
2026-10-04 support KB export and a new, signed reassessment. No live desk workflow or
production product has been changed.

## Deliverables

- Source page: `src/routes/kb/incidents/4471-reassessment/+page.svx`
- Standalone rendered snapshot: `rendered/4471-reassessment.html` (download and open)
- Interactive rendered page: `rendered/kb/incidents/4471-reassessment/index.html`
- Issue drafts: `issue-drafts/parser.md` and `issue-drafts/hint.md`
- Computed report groups and included IDs: `analysis.json`

The supplied classifier yields **379 parser reports and 33 hint reports**, totaling
**412 unique reports** from 427 rows. Five unusual reports remain in the parser group
with explicit uncertainty; no additional root cause is claimed from their wording.

## Reproduce

Use Node 22.18 or newer and Python 3:

```sh
npm ci --ignore-scripts
npm run build
python3 scripts/snapshot.py
python3 -m http.server 43103 --bind 127.0.0.1 --directory rendered
```

Open `http://127.0.0.1:43103/kb/incidents/4471-reassessment/`.
The standalone snapshot contains inline CSS and no JavaScript; its form controls are
disabled. The directory version includes the compiled interactive Svelte components.
The original export's accepted decision and other source pages are preserved.

## Validation

The production SvelteKit build renders every KB route. Checks against the supplied
TypeScript classifier verified the unique total, disjoint cause counts, booking-v3
channel distinction, month-first locale behavior, and unknown-tenant handling.
Tables, timeline, dedupe examples, and desk reference are computed during rendering.

Counts describe the export, not the current queue. Rebuild with fresh desk data and
review the resulting groups before updating issue counts.

## Engineering update

The course page subsequently reported #4471 closed on 5 October: parser fixed
(`fix(dates): parse dd/mm for eu locales`); hint won’t fix because booking-v3 was retired.
GitHub #1 records completed; #2 records not planned. The initial analysis-only closure
was corrected after checking the changed challenge page.

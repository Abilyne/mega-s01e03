# [#4471] Booking-v3 date hint contradicts day-first form parsing

Covers **33 unique reports** merged into #4471 in the 2026-10-04 KB export.

## Problem

Booking-v3 displays `MM/DD/YYYY` but parses its form input in the tenant’s day-first convention. People following the hint get the wrong date. This affects 33 form reports from Alder Physio, Copper Studio, and Pale Harbour. It requires a separate UI/input-contract fix from the shared parser issue.

## Evidence and counting

427 export rows reduce to 412 unique IDs. Join tenants by handle; determine day-first order using `Intl.DateTimeFormat(...).formatToParts`; classify using tenant form and report channel in `src/lib/kb/causes.ts`. Do not count browser-locale intake tags as causes. The disjoint groups are 379 parser and 33 hint reports.

This group’s intake tags: 15 tagged parser, 18 tagged hint.

- R-41230, copper.studio, form: “My client came on 1 June instead of 6 January. We sorted it out.”
- R-41241, alder.physio, form: “We had two people show up on 8 June. They were booked for 6 August.”

## Acceptance criteria

- Derive hint and accepted format from the same tenant date convention for booking-v3.
- Reproduce with a day-first tenant entering a date according to the current month-first hint; confirm the corrected form preserves the intended date.
- Cover all three affected tenants and month-first regression cases. A shared-parser change alone does not satisfy this issue.
- Monitor new reports after the fix. The export is a snapshot; no production fix or live workflow change has been performed.

## Included report IDs

R-41230, R-41241, R-41251, R-41259, R-41262, R-41275, R-41294, R-41305, R-41308, R-41366, R-41372, R-41384, R-41387, R-41396, R-41400, R-41406, R-41415, R-41416, R-41418, R-41428, R-41439, R-41441, R-41449, R-41453, R-41456, R-41460, R-41472, R-41485, R-41493, R-41539, R-41572, R-41582, R-41584

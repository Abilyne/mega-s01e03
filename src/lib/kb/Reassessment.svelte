<script lang="ts">
  import reports from '#lib/data/reports-4471.json';
  import notes from '#lib/data/desk-notes.json';
  import { uniqueById, groupByCause, type Report } from '#lib/kb/causes';
  import { tenantOf } from '#lib/kb/locales';
  const all = reports as Report[];
  const unique = uniqueById(all);
  const merged = unique.filter(r => r.mergedInto === 4471);
  const groups = groupByCause(merged, tenantOf);
  const mismatched = groups.reduce((sum, g) => sum + g.reports.filter(r => r.meta.intakeTag !== g.cause).length, 0);
  const unusual = merged.filter(r => notes.oneDayMove.includes(r.id));
</script>

<h2>Counting and uncertainty</h2>
<p>{all.length} export rows contain {unique.length} unique report IDs; {all.length - unique.length} repeated rows are counted once. All {merged.length} unique reports belong to #4471. Tenant-and-channel classification disagrees with {mismatched} intake tags.</p>
<p>The desk flagged {unusual.length} reports as one-day moves. They remain included in the parser count under the supplied classifier. Their text also includes an early invite and a timezone-dependent date difference. These are unresolved observations, not proof of a third established cause. A parser fix must not silently close them.</p>
<table>
  <thead><tr><th>Report</th><th>Tenant / channel</th><th>Observation</th></tr></thead>
  <tbody>{#each unusual as r}<tr><td>{r.id}</td><td>{r.tenant} / {r.channel}</td><td>{r.body}</td></tr>{/each}</tbody>
</table>
<p>Investigate original input, intended date, stored value, timezone, invite payload, and send time for each exception. Confirm a reproducible mechanism before creating another cause group or changing its count.</p>

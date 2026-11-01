---
name: report-template
description: The artifact that makes findings stick — scorecard structure, severity-tagged findings with evidence, and trend tracking across audits.
tags: [reporting, findings, scorecard, severity, tracking]
related: [review-process, a11y-audit, perceived-performance]
---

# Design Review Guide: Audit Report Template

## 1. Definition

An audit without a standardized report produces screenshots that die in chat threads. This guide defines the report artifact: the scorecard header (surface, date, auditors, scope), the per-axis scores from every audit guide in this repo, the findings table (id, axis, severity, WCAG/criteria reference, evidence screenshot, recommendation, owner, status), the trend section (scores over time), and the distribution — who gets it and what happens next. The template is the reason audits compound instead of evaporating: the same structure run every quarter turns isolated reviews into a trajectory of design debt you can actually manage down.

## 2. Core Principles

- **One template for all audits:** every review uses the same structure — comparability over time is the point.
- **The scorecard header scopes it:** surface, date, auditors, scope, and build/commit — findings are reproducible or they're anecdotes.
- **Per-axis scores from the checklists:** hierarchy, consistency, a11y, motion, typography, spacing, states, content, performance, responsive — each scored with its guide's criteria.
- **Findings are structured rows:** id, axis, severity, criteria reference, evidence, recommendation, owner, status — unstructured findings can't be tracked.
- **Evidence is attached:** screenshot/recording per finding, captured at audit time — evidence-first prevents relitigation.
- **Recommendations are specific:** what to change and to what standard — 'improve spacing' is not a recommendation.
- **The trend section tracks scores:** per-axis scores plotted over audits — copy debt and its reduction become visible.
- **Distribution has a protocol:** findings go to owners with due dates; the summary goes to leadership — reports have next steps, not just archives.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Report structure | `--rev-report-structure` | `header+scores+findings+trend` | One template, all audits |
| Scorecard header | `--rev-scorecard-header` | `surface,date,auditors,scope,commit` | Reproducibility data |
| Axis scores | `--rev-axis-scores` | `10-audit-axes-scored` | From each guide's checklist |
| Findings table | `--rev-findings-table` | `id,axis,severity,criteria,evidence,fix,owner,status` | The tracking unit |
| Evidence required | `--rev-evidence-required` | `screenshot-per-finding` | Captured at audit time |
| Recommendation format | `--rev-recommendation-format` | `specific+standard-cited` | Not 'improve X' |
| Trend section | `--rev-trend-section` | `scores-over-time` | Debt made visible |
| Distribution protocol | `--rev-distribution-protocol` | `owners+leadership` | Next steps attached |
| Severity reuse | `--rev-severity-reuse` | `review-process-scale` | Shared vocabulary |
| Template version | `--rev-template-version` | `versioned-doc` | Evolves with the guides |

Consume them by linking `assets/css/report-template.css` at the review-doc root, then reading `var(--rev-<role>)` — the CSS uses the tokens for severity colors and table styling, while the export tooling reads them via `getComputedStyle(document.documentElement).getPropertyValue(...)` to validate that a generated report contains every required structural unit before it ships.

## 4. Composition

- **Composes with every audit guide in this repo:** their checklists produce this report's axis scores and findings rows — the template is the single downstream consumer of all ten audits.
- **Composes with review-process (guide 01):** severity scale and ticket flow are inherited contracts — the report reuses the blocker/major/minor/polish vocabulary rather than inventing its own.
- **Composes with skill-design-review companions (icon-system-audit, copy-audit):** their scorecards nest into this template's axes — companion audits add rows, never new structures.

## 5. Signature Patterns

- **The findings-table-first report:** the structured findings table is the primary artifact; narrative summary second — the table is what gets tracked. A report whose value lives in prose paragraphs cannot be filtered, assigned, or trended; one whose value lives in rows can feed tickets, dashboards, and next quarter's diff automatically.
- **The trend dashboard:** per-axis scores from successive audits plotted — the one-glance view of design debt trajectory. A single report is a snapshot; the trend line is what tells leadership whether the investment is working and which axis is rotting fastest.

## 6. Real-World Use Cases

- **Every audit this repo runs** — the template is the shared output; each guide's checklist feeds the same scorecard.
- **Leadership reporting on design quality investment** — the trend section converts audit work into a legible trajectory for budget decisions.
- **Cross-team comparisons** where standardized audits make scores meaningful — team A's 82 on a11y is comparable to team B's because both came from the same criteria.

## 7. Combination Notes

### With other design-review skills

- **Good with review-process:** the strongest pairing in the repo — the process defines the severity scale and ticket flow the report inherits; without it, report severities are private dialects and findings have nowhere to go.
- **Good with every audit guide (a11y, motion, typography, spacing, states, content, perceived-performance, responsive, hierarchy, consistency):** each guide contributes one axis score and its findings rows; the template's value is precisely that all ten collapse into one comparable artifact.
- **Why good compositions dominate:** the report has no criteria of its own — it borrows standards from every other guide — so it conflicts with none of them and degrades gracefully when some audits are skipped (missing axes score as "not assessed," never as zero).
- **No caution or avoid entries:** the only anti-composition is running audits without this template at all, which is the anti-pattern list, not a partner list.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, class-morphism, and flat-design:** the report itself should follow these styles — minimal tables, flat severity tags, class-morphic depth reserved for the scorecard summary. A report styled like the system it audits reads as credible.
- **No caution entries:** style affects how the report is rendered, never what it must contain; the structural tokens (header, scores, findings, trend) are style-invariant.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** report UI motion (score count-ups, sparkline draw-ins, severity tag transitions) uses the motion token ladder — 100-300ms feedback, standard easings — so the report demonstrates the discipline it audits.
- **No caution entries:** the report is a static document at heart; motion is optional garnish and must collapse under reduced-motion like any audited surface would.

## 8. Anti-Patterns

- **Screenshot audits** — findings in chat threads, dead by Friday
- **Vibes reports** — 'overall good, tighten things up' with no findings rows
- **Evidence-free findings** — claims that get relitigated on sight
- **Archive-only reports** — produced, filed, never distributed with next steps

### Accessibility Notes

The report template makes a11y findings first-class: the a11y axis is scored like every other axis (not a separate annex), WCAG criteria are cited per finding so remediation is checkable, and blocker-severity a11y findings gate releases — the template is how a11y accountability persists beyond the audit day. The report artifact itself must also be accessible: findings tables use real `<table>` semantics with header cells, severity is signaled by text label and not color alone, evidence links carry descriptive names, and the exported HTML passes the same contrast and keyboard checks the audits enforce. The fallback rule: if a full template is too heavy, adopt the findings table alone (id/axis/severity/criteria/evidence/owner/status) — it's the unit that makes everything else trackable.

## 9. Code Examples

### Example 1 — The full audit report rendered

Tokens: `assets/css/report-template.css`

```html
<article class="report">
  <header>
    <h1>Audit Report — Checkout Flow</h1>
    <p class="meta">2026-11-02 · Auditors: S. Nguyen, R. Okafor · Scope: /checkout/* · Build: a3f9c1e</p>
  </header>
  <section aria-label="Axis scores">
    <h2>Axes (10)</h2>
    <ul class="axes">
      <li>Hierarchy 82</li><li>Consistency 74</li><li>A11y 68</li><li>Motion 90</li>
      <li>Typography 85</li><li>Spacing 79</li><li>States 71</li><li>Content 77</li>
      <li>Performance 64</li><li>Responsive 58</li>
    </ul>
    <svg class="spark" viewBox="0 0 120 28" role="img" aria-label="A11y score trend: 61, 65, 68">
      <polyline points="4,22 40,16 76,12 116,8" fill="none" stroke="#2563eb" stroke-width="2"/>
    </svg>
  </section>
  <table>
    <caption>Findings</caption>
    <thead><tr><th>ID</th><th>Axis</th><th>Severity</th><th>Criteria</th><th>Evidence</th><th>Recommendation</th><th>Owner</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td>F-001</td><td>Responsive</td><td><span class="sev major">major</span></td><td>WCAG 1.4.10</td><td><a href="#ev1">320px screenshot</a></td><td>Reflow cart grid to single column at 320px per responsive guide</td><td>Team Checkout</td><td>Open</td></tr>
      <tr><td>F-002</td><td>States</td><td><span class="sev blocker">blocker</span></td><td>WCAG 2.4.7</td><td><a href="#ev2">Focus recording</a></td><td>Restore visible focus ring on Pay button (2px + offset)</td><td>Team Checkout</td><td>In progress</td></tr>
      <tr><td>F-003</td><td>Performance</td><td><span class="sev minor">minor</span></td><td>Band contract &gt;3s</td><td><a href="#ev3">Throttle capture</a></td><td>Add cancel affordance to 3s+ address validation</td><td>Platform</td><td>Open</td></tr>
    </tbody>
  </table>
</article>
<style>
  .report { font: 14px/1.5 system-ui, sans-serif; max-width: 720px; border: 1px solid #ddd; border-radius: 8px; padding: 20px; }
  .report h1 { font-size: 18px; margin: 0 0 4px; }
  .meta { color: #525252; margin: 0 0 16px; }
  .axes { list-style: none; display: flex; flex-wrap: wrap; gap: 6px; padding: 0; }
  .axes li { border: 1px solid #e5e5e5; border-radius: 999px; padding: 2px 10px; background: #fafafa; }
  table { width: 100%; border-collapse: collapse; margin-top: 12px; }
  th, td { text-align: left; padding: 6px 8px; border-bottom: 1px solid #eee; }
  .sev { font-weight: 600; padding: 1px 8px; border-radius: 4px; }
  .sev.blocker { background: #fee2e2; color: #b91c1c; }
  .sev.major   { background: #fef3c7; color: #92400e; }
  .sev.minor   { background: #e0f2fe; color: #075985; }
</style>
```

### Example 2 — Findings-to-tickets export (JSON/CSV)

```html
<div class="export">
  <button id="json">Download findings.json</button>
  <button id="csv">Download findings.csv</button>
  <pre id="out" role="status"></pre>
</div>
<script>
  // Findings rows mirror the report's findings table 1:1 — the tracking unit
  const findings = [
    { id:'F-001', axis:'responsive', severity:'major', criteria:'WCAG 1.4.10', evidence:'320px.png',
      recommendation:'Reflow cart grid to single column at 320px', owner:'Team Checkout', status:'open' },
    { id:'F-002', axis:'states', severity:'blocker', criteria:'WCAG 2.4.7', evidence:'focus.mp4',
      recommendation:'Restore visible focus ring on Pay button', owner:'Team Checkout', status:'in-progress' },
  ];
  const csv = ['id,axis,severity,criteria,evidence,recommendation,owner,status',
    ...findings.map(f => [f.id,f.axis,f.severity,f.criteria,f.evidence,`"${f.recommendation}"`,f.owner,f.status].join(','))].join('\n');
  const dl = (name, text, type) => {
    const a = document.createElement('a');
    a.href = URL.createObjectURL(new Blob([text], { type }));
    a.download = name; a.click(); URL.revokeObjectURL(a.href);
    return name + ': ' + findings.length + ' rows exported';
  };
  document.getElementById('json').onclick = () =>
    document.getElementById('out').textContent = dl('findings.json', JSON.stringify(findings, null, 2), 'application/json');
  document.getElementById('csv').onclick = () =>
    document.getElementById('out').textContent = dl('findings.csv', csv, 'text/csv');
</script>
<style>
  .export { font: 14px/1.5 system-ui, sans-serif; max-width: 480px; }
  .export button { margin-right: 8px; padding: 8px 14px; border: 1px solid #ddd; border-radius: 8px; background: #fff; cursor: pointer; }
  .export button:hover { background: #f5f5f5; }
  #out { background: #fafafa; border: 1px solid #eee; border-radius: 6px; padding: 10px; }
</style>
```

## 10. Implementation Checklist

- [ ] Every audit run against this repo uses the one template structure from `--rev-report-structure` — no bespoke report formats.
- [ ] Scorecard header carries all `--rev-scorecard-header` fields (surface, date, auditors, scope, commit) so findings are reproducible.
- [ ] All 10 axes from `--rev-axis-scores` scored (or marked "not assessed") from their guides' checklists.
- [ ] Every finding is a full `--rev-findings-table` row — no prose-only findings anywhere in the report.
- [ ] Each finding attaches evidence per `--rev-evidence-required`, captured at audit time.
- [ ] Recommendations cite a specific change plus a standard per `--rev-recommendation-format` — "improve X" rows bounce.
- [ ] Severity labels reuse the `--rev-severity-reuse` review-process scale verbatim.
- [ ] Report distributed per `--rev-distribution-protocol`: owners have tickets with due dates, leadership gets the trend summary, and the template itself is versioned per `--rev-template-version`.

---
name: icon-system-audit
description: The system health check: consistency scoring, a11y sweep, weight audit, and the per-surface review pass.
tags: [audit, accessibility, quality, icons, consistency]
related: [accessible-icons, icon-style-selection, svg-optimization]
---

# Visual Asset Guide: Icon & Illustration System Audit

## 1. Definition

Icon and illustration systems decay silently: style drift, unnamed icons, weight bloat. This guide is the audit layer: the per-surface review pass (every icon named/hidden/contrasted, every illustration paired), system-level scoring (style adherence, grid discipline, library hygiene), weight audits (payload per page), and findings-to-tickets tracking. It composes with skill-design-review as the visual-asset section of the broader design audit. Where guides 01-11 define contracts, this guide measures them: each contract becomes a scorecard criterion, each finding becomes a prioritized ticket, and scores over time turn silent decay into a visible, trendable curve.

## 2. Core Principles

- **Audits are per-surface:** walk the surface checking every icon (named? contrasted? right family?) and illustration (paired? weighted? on-spec?) - findings, not vibes.
- **The a11y sweep is first:** unnamed interactive icons and unhidden decorations are the highest-severity findings.
- **Style adherence is scored:** stroke weight, corner, fill consistency checked against the spec sheet - drift is measured, not felt.
- **Grid discipline verified:** sampled icons overlaid on keylines - violations quantified per audit.
- **Weight is audited per page:** icon+illustration payload measured (gzipped) against budgets - bloat trends tracked.
- **Findings become tickets:** each audit produces prioritized tickets with owners - audits without follow-up are theater.
- **Audit cadence:** per-release gates for new assets + quarterly full sweeps - decay is caught on schedule, not by accident.
- **Results trend:** audit scores over time show the system improving - or identify the drift source.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Audit scope | `--icon-audit-scope` | `per-surface+system` | Surface pass + system score |
| A11y sweep | `--icon-a11y-sweep-first` | `names+hide+contrast` | Highest-severity findings first |
| Style score | `--icon-style-score` | `vs-spec-sheet` | Drift measured against spec |
| Grid check | `--icon-grid-check` | `keyline-overlay-sample` | Violations quantified |
| Weight audit | `--icon-weight-audit` | `gzipped-per-page` | vs budgets (icons under 50KB) |
| Findings | `--icon-findings-to-tickets` | `prioritized+owned` | Follow-up mandatory |
| Cadence | `--icon-audit-cadence` | `release-gate+quarterly` | Scheduled, not accidental |
| Trending | `--icon-trend-tracking` | `scores-over-time` | Decay made visible |
| Review link | `--icon-design-review-link` | `visual-asset-section` | Feeds skill-design-review |
| Criteria source | `--icon-a11y-criteria-source` | `skill-accessibility` | Criteria layer referenced |

Consume them by linking `assets/css/icon-system-audit.css` at the app root - the audit tooling and scorecard components read scope, cadence, and thresholds via `var(--icon-...)`, so the per-surface walker, the weight auditor, and the trend dashboard all enforce the same declared criteria rather than each tool carrying its own private list.

## 4. Composition

- **Composes with every guide in this repo:** the audit scorecard references each guide's contracts as criteria.
- **Composes with skill-design-review:** this guide is the visual-asset section of the product-wide review.
- **Composes with skill-accessibility media-alt-text:** the a11y sweep uses those criteria directly.

## 5. Signature Patterns

- **The visual-asset audit scorecard:** per-surface checklist (names, contrast, family, grid, weight, pairing) with severity per finding - the audit's artifact. Each row cites the guide whose contract it checks, so a failing score points straight at the governing rule, not an opinion.
- **The quarterly system sweep:** full-library review (usage, duplicates, deprecations) + per-page weight trend - the system health report. The sweep reads the library's own usage data (icon-library-management), so pruning and auditing share one source of truth.

## 6. Real-World Use Cases

- **Pre-release reviews of new surfaces.**
- **Post-acquisition/legacy audits before icon unification.**
- **Ongoing system health for large icon/illustration estates.**

## 7. Combination Notes

### With other icons-illustration skills

- **Good with every guide in this repo - that is the design:** the audit scorecard is a consumer of contracts; icon-style-selection supplies the spec sheet, accessible-icons the naming/hiding rules, svg-optimization the weight budgets, and favicon-app-icons the set-completeness checks. The audit is good with all of them because it adds measurement, not rules.
- **Good with icon-library-management specifically:** usage tracking and audit findings share the same data - the prune list and the drift list come from one build scan.
- **Good with animation-integration and illustration-direction:** motion rationing and illustration spec adherence are scorecard rows; loops, fallbacks, and off-spec art are counted, not sensed.
- **No caution or avoid entries:** as the measurement layer, this skill has no incompatible partners - the only failure mode is skipping it, which is what the cadence token prevents.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** these styles' restraint is checkable - stroke counts, flat fills, and limited palettes make style-adherence scoring objective, so audits resolve quickly and disputes are rare.
- **Caution with expressive styles (collage-art, maximalism, claymorphism):** richer styles blur the line between intentional variety and drift; audits against them need the spec sheet amended first (documented acceptable variance), or every legitimate stylistic choice scores as a finding.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** motion contracts (durations, easings, fallback behavior) are auditable against tokens - the scorecard checks that icon animation durations and easings resolve to the shared motion tokens, and that reduced-motion fallbacks exist.
- **Caution with ambient-motion:** ambient animation is the audit's least stable row - loops are rationed per viewport and long scenes need pause controls, so an ambient-heavy direction raises audit overhead; schedule those checks as part of the release gate, not ad hoc.

## 8. Anti-Patterns

- **Audit theater** — sweeps run, findings never ticketed
- **Feel-based reviews** — looks-off judgements without spec-sheet measurement
- **Weight-blind audits** — style checked, payload ignored
- **One-time audits** — no cadence, decay returns within a quarter

### Accessibility Notes

The audit enforces the a11y contracts of every guide here: WCAG 1.1.1/1.4.11/2.5.8/4.1.2 findings categorized by severity - the a11y sweep is the audit's first pass, not an afterthought. Concretely, the walker classifies every icon instance (functional icons carry accessible names, decorative ones carry `aria-hidden` and sit outside the tab order), checks meaningful glyphs against the 3:1 contrast floor at their shipping size, verifies 44px effective targets where icons are interactive, and reports unnamed interactive icons as the highest-severity findings before any style or weight rows are scored. The fallback rule: if a full audit program cannot start, run the a11y sweep alone (names/hide/contrast) - it catches the highest-severity issues with the least effort.

## 9. Code Examples

### Example 1 — Audit scorecard: per-guide rows with pass/fail scoring via JS

Tokens: `assets/css/icon-system-audit.css`

```html
<div class="scorecard">
  <table>
    <thead><tr><th>Criterion</th><th>Source guide</th><th>Status</th></tr></thead>
    <tbody id="rows">
      <tr data-check="names"><td>Functional icons named</td><td>accessible-icons</td><td class="status">?</td></tr>
      <tr data-check="hide"><td>Decorative icons hidden</td><td>accessible-icons</td><td class="status">?</td></tr>
      <tr data-check="family"><td>One icon family per surface</td><td>icon-style-selection</td><td class="status">?</td></tr>
      <tr data-check="weight"><td>Icon payload under budget</td><td>svg-optimization</td><td class="status">?</td></tr>
    </tbody>
  </table>
  <p class="score" aria-live="polite">Score: —</p>
</div>
<style>
  .scorecard { font: 14px/1.5 Inter, system-ui, sans-serif; color: #1e293b; max-width: 480px; }
  table { width: 100%; border-collapse: collapse; }
  th, td { text-align: left; padding: 8px 10px; border-bottom: 1px solid #E2E8F0; }
  th { font-size: 12px; text-transform: uppercase; letter-spacing: .04em; color: #64748B; }
  .status, .score { font-weight: 600; }
  [data-result="pass"] .status { color: #15803D; } [data-result="fail"] .status { color: #B91C1C; }
</style>
<script>
  // --icon-a11y-sweep-first: names+hide+contrast — a11y rows are scored first
  const doc = document;
  const checks = {
    names:  () => [...doc.querySelectorAll('button[data-icon-btn]')].every(b => (b.getAttribute('aria-label') || b.textContent.trim()).length > 0),
    hide:   () => [...doc.querySelectorAll('svg.decorative')].every(s => s.getAttribute('aria-hidden') === 'true'),
    family: () => new Set([...doc.querySelectorAll('svg[data-family]')].map(s => s.dataset.family)).size <= 1,
    weight: () => [...doc.querySelectorAll('svg[data-bytes]')].reduce((a, s) => a + Number(s.dataset.bytes), 0) < 50 * 1024,
  };
  let pass = 0, total = 0;
  for (const row of doc.querySelectorAll('#rows tr')) {
    const ok = checks[row.dataset.check]?.() ?? false;
    row.dataset.result = ok ? 'pass' : 'fail';
    row.querySelector('.status').textContent = ok ? 'Pass' : 'Fail';
    total++; if (ok) pass++;
  }
  doc.querySelector('.score').textContent = `Score: ${pass}/${total} — findings become tickets (--icon-findings-to-tickets)`;
</script>
```

### Example 2 — Per-surface checklist walker: names/contrast/family/weight on a sample toolbar

Tokens: `assets/css/icon-system-audit.css`

```html
<div class="toolbar-wrap">
  <div class="toolbar" id="surface">
    <button type="button" data-icon-btn aria-label="Search files">
      <svg class="decorative" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false" data-family="outline" data-bytes="640"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="#404040" stroke-width="2"/><path d="M15.5 15.5L20 20" stroke="#404040" stroke-width="2"/></svg>
    </button>
    <button type="button" data-icon-btn aria-label="Upload">
      <svg class="decorative" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false" data-family="outline" data-bytes="580"><path d="M12 16V5m0 0l-4 4m4-4l4 4M5 19h14" fill="none" stroke="#404040" stroke-width="2"/></svg>
    </button>
    <button type="button" data-icon-btn>
      <svg class="decorative" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false" data-family="filled" data-bytes="610"><path d="M12 3l2.6 5.6L20 9.3l-4 4.1.9 5.6-4.9-2.7-4.9 2.7.9-5.6-4-4.1 5.4-.7z" fill="#404040"/></svg>
    </button>
  </div>
  <ul class="findings" id="findings" aria-live="polite"></ul>
</div>
<style>
  .toolbar-wrap { font: 14px/1.5 Inter, system-ui, sans-serif; color: #1e293b; }
  .toolbar { display: inline-flex; gap: 4px; padding: 6px; border: 1px solid #E2E8F0; border-radius: 8px; }
  .toolbar button { display: grid; place-items: center; width: 44px; height: 44px; border: none; background: #fff; border-radius: 6px; cursor: pointer; }
  .findings { margin: 12px 0 0; padding-left: 18px; color: #475569; } .findings .sev-high { color: #B91C1C; font-weight: 600; }
</style>
<script>
  // Per-surface walk: --icon-audit-scope: per-surface+system
  const surface = document.getElementById('surface'), out = [];
  const buttons = [...surface.querySelectorAll('button[data-icon-btn]')];
  // 1. Names (a11y sweep first — highest severity)
  for (const b of buttons) if (!(b.getAttribute('aria-label') || '').trim()) out.push(['high', 'Unnamed icon button (WCAG 4.1.2)']);
  // 2. Hidden decoration
  for (const s of surface.querySelectorAll('svg')) if (s.getAttribute('aria-hidden') !== 'true') out.push(['high', 'Decorative SVG not hidden (WCAG 1.1.1)']);
  // 3. Family consistency — --icon-style-score: vs-spec-sheet
  const families = new Set([...surface.querySelectorAll('svg[data-family]')].map(s => s.dataset.family));
  if (families.size > 1) out.push(['med', `Style drift: ${families.size} families in one toolbar (filled star vs outline set)`]);
  // 4. Weight — --icon-weight-audit: gzipped-per-page, icons under 50KB
  const bytes = [...surface.querySelectorAll('svg[data-bytes]')].reduce((a, s) => a + Number(s.dataset.bytes), 0);
  if (bytes > 50 * 1024) out.push(['med', 'Icon payload over 50KB budget']);
  const list = document.getElementById('findings');
  list.innerHTML = out.length ? out.map(([sev, msg]) => `<li class="sev-${sev}">[${sev.toUpperCase()}] ${msg}</li>`).join('') : '<li>All checks pass — 0 findings.</li>';
</script>
```

## 10. Implementation Checklist

- [ ] The audit scope covers `var(--icon-audit-scope)`: a per-surface walk plus a system-level score, both artifacts produced.
- [ ] The a11y sweep runs first per `var(--icon-a11y-sweep-first)` - names, hiding, and contrast scored before any style rows.
- [ ] Style adherence is scored against the spec sheet via `var(--icon-style-score)` - drift quantified, not felt.
- [ ] Sampled icons pass the `var(--icon-grid-check)` keyline overlay with violations counted per audit.
- [ ] Page weight is measured gzipped per `var(--icon-weight-audit)` and compared against budgets.
- [ ] Every finding exits as a prioritized, owned ticket per `var(--icon-findings-to-tickets)` - no unowned findings.
- [ ] Cadence follows `var(--icon-audit-cadence)`: release gates for new assets, quarterly full sweeps on the calendar.
- [ ] Scores are persisted per `var(--icon-trend-tracking)` so improvement and decay sources are visible over time.

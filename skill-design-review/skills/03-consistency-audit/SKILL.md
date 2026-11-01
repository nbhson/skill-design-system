---
name: consistency-audit
description: Token adherence, component reuse, and pattern discipline: is the product speaking one visual language?
tags: [consistency, audit, tokens, reuse, drift]
related: [review-process, visual-hierarchy-audit, typography-audit]
---

# Design Review Guide: Consistency Audit

## 1. Definition

Consistency is the perceived quality multiplier: users read consistency as reliability. The audit checks token adherence (any raw hex/px values escaping the system?), component reuse (hand-rolled one-offs beside system components?), pattern discipline (same task done the same way across surfaces?), and terminology consistency (one concept, one term). The output is a drift map: where the product diverges from its own system, ranked by user impact.

## 2. Core Principles

- **Raw values are findings:** any hex/px/font-family in product CSS outside tokens/component styles is a consistency violation.
- **Component reuse is checked, not assumed:** custom one-offs beside existing system components are flagged — duplication is debt.
- **Same task, same pattern:** delete actions, date pickers, and empty states work identically across surfaces — per-surface reinvention is a finding.
- **Terminology matches the glossary:** one concept, one term (ux-writing copy-audit contract) — drift here is user-visible confusion.
- **Spacing/radii/shadows come from scales:** off-scale values (17px padding, 7px radius) are mechanical findings.
- **Interaction patterns are consistent:** primary buttons, hover states, and focus treatment identical everywhere.
- **Drift is mapped by impact:** inconsistency in high-traffic flows outranks settings-page drift — the drift map is ranked.
- **Consistency has a source of truth:** the audit needs the token/component/pattern docs to exist — auditing against nothing measures nothing.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Raw Value Scan | `--rev-raw-value-scan` | `zero-outside-tokens` | Mechanical; lint-assisted |
| Component Reuse Check | `--rev-component-reuse-check` | `one-offs-flagged` | Duplication is debt |
| Pattern Parity | `--rev-pattern-parity` | `same-task-same-pattern` | Per-surface reinvention banned |
| Terminology Check | `--rev-terminology-check` | `glossary-adherence` | One concept, one term |
| Scale Adherence | `--rev-scale-adherence` | `spacing,radius,shadow` | Off-scale = mechanical finding |
| Interaction Consistency | `--rev-interaction-consistency` | `states-identical-cross-surface` | Buttons/hover/focus uniform |
| Drift Map | `--rev-drift-map` | `impact-ranked` | High-traffic drift first |
| Source Of Truth | `--rev-source-of-truth` | `docs-required` | Audit needs criteria to exist |
| Audit Frequency | `--rev-audit-frequency` | `per-release+quarterly` | Decay caught on schedule |
| Consistency Score | `--rev-consistency-score` | `per-surface` | Feeds report template |

Consume them by linking `assets/css/consistency-audit.css` in the audit tooling, then referencing `var(--rev-<role>)` when rendering drift maps and scorecards. The tokens encode the audit's thresholds: `--rev-raw-value-scan` is the zero-tolerance bar for the lint sweep, and `--rev-audit-frequency` is the schedule the decay check runs on — per-release for the mechanical sweep, quarterly for the full walk.

## 4. Composition

- **Composes with skill-design-tokens + skill-component-recipes:** those repos are the source of truth this audit enforces.
- **Composes with review-process (guide 01):** findings flow through the severity scale and ticket loop.
- **Composes with content-microcopy-audit (guide 09):** terminology and copy consistency are shared checks.

## 5. Signature Patterns

- **The raw-value sweep:** lint/build scan for raw hex/px outside tokens — mechanical findings in minutes, the audit's highest-yield pass. Because it is scriptable, it runs per release per `--rev-audit-frequency`, catching token theater the moment it appears rather than at quarterly review.
- **The cross-surface task walk:** perform one task (delete, search, invite) across 3 surfaces; divergences are pattern-parity findings. The walk is the human complement to the mechanical sweep — it catches reinvention no linter can see, and each divergence enters the drift map ranked by the traffic of the surfaces involved.

## 6. Real-World Use Cases

- **Post-acquisition and legacy products unifying divergent UI:** the drift map becomes the unification roadmap — impact-ranked so the highest-traffic divergence is fixed first.
- **Design systems measuring adoption:** scale-adherence rate and component-reuse checks turn "adoption" from an anecdote into a number the consistency score tracks per surface.
- **Audit: off-scale values, one-off components, terminology drift:** the three named failure classes this pass exists to find, from stray 17px paddings to a custom modal beside the system modal.

## 7. Combination Notes

### With other design-review skills

- **Good with review-process:** the consistency audit produces findings; the process gives them severity, owners, and a decision record — without that loop, drift maps are documentation, not change.
- **Good with visual-hierarchy-audit, typography-audit, and spacing-rhythm-audit:** these audits check whether the system is applied well within a surface; consistency-audit checks whether the system is the same across surfaces — surface-level and system-level reads of the same substrate.
- **Good with interaction-states-audit and a11y-audit:** interaction consistency and a11y-critical pattern consistency are shared checks — inconsistent focus treatment is simultaneously a consistency finding and a blocker.
- **Good with content-microcopy-audit, perceived-performance, responsive-audit, and motion-audit:** terminology, loading patterns, breakpoint behavior, and motion tokens each have cross-surface parity checks that feed the drift map.
- **Good with report-template:** the per-surface consistency score lands in the report, and the drift map is its ranked appendix.
- **No caution or avoid list:** consistency-audit is a consumer of every sibling's criteria — no audit's findings conflict with it, because its only question is "does this match the declared system?"

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** all three are system-driven styles whose visual rules are expressible as tokens and scales — exactly the source-of-truth artifacts this audit enforces, making checks mechanical rather than interpretive.
- **Caution with collage-art:** collage aesthetics deliberately juxtapose divergent fragments, so a naive drift map will flag intentional juxtaposition as findings. If collage-art is the declared style, scope the raw-value sweep to structural properties (spacing, radii, focus treatment) and exempt the deliberate material variance — audited against nothing measures nothing.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** duration and easing tokens are part of the source of truth — the raw-value sweep extends to motion (random cubic-bezier values and off-ladder durations are consistency findings), and interaction-consistency covers state-transition timing being identical across surfaces.
- **No caution list:** motion consistency is a normal subset of pattern parity; entrance conventions that vary per surface are pattern-parity findings like any other.

## 8. Anti-Patterns

- **Token theater:** tokens defined but raw values shipped anyway
- **One-off sprawl:** a custom modal beside the system modal
- **Task roulette:** the same action working differently on three screens
- **Terminology drift:** 'project' here, 'workspace' there

### Accessibility Notes

Consistency is an a11y multiplier: consistent focus treatment, contrast, and interaction patterns reduce relearning for AT and cognitive-load users (WCAG 3.2.4 consistent identification) — the audit treats inconsistency in a11y-critical patterns as major. This is why the cross-surface task walk always includes the focus and contrast dimensions: a delete flow whose confirmation modal is keyboard-operable on one surface and mouse-only on another is not merely inconsistent, it is a major a11y finding, and the drift map ranks it by the traffic of the failing surface. The fallback rule keeps the audit shippable: if full scoring is too heavy, run the raw-value sweep + focus/contrast consistency walk — those two passes cover the highest-impact drift.

## 9. Code Examples

### Example 1 — Raw-value sweep demo (JS scanning sample CSS for off-token hex/px)

Tokens: `assets/css/consistency-audit.css`

```html
<section class="sweep">
  <h1>Raw-Value Sweep — <code>var(--rev-raw-value-scan)</code>: zero-outside-tokens</h1>
  <pre id="sampleCss" hidden>/* sample product CSS */
.card { padding: 17px; border: 1px solid #E5E7EB; border-radius: 7px; }
.card-title { color: #111827; font-size: 15px; }
.btn { background: var(--rev-token-surface, #fff); padding: 12px; }</pre>
  <button id="runSweep">Run sweep</button>
  <ul id="findings" aria-live="polite"></ul>
</section>
<style>
  .sweep { max-width: 560px; font: 14px/1.5 ui-monospace, SFMono-Regular, Menlo, monospace; padding: 24px; border: 1px solid #D4D4D4; border-radius: 8px; }
  .sweep h1 { font: 600 16px/1.4 Inter, system-ui, sans-serif; margin: 0 0 12px; }
  .sweep button { padding: 8px 16px; border: none; border-radius: 6px; background: #2563EB; color: #fff; font-weight: 600; margin: 12px 0; }
  #findings { margin: 0; padding: 0; list-style: none; }
  #findings li { padding: 6px 10px; border-left: 3px solid #EF4444; background: #F5F5F5; margin-bottom: 4px; }
  #findings li.on-token { border-left-color: #22C55E; }
</style>
<script>
  // Mechanical sweep: flag raw hex/px in declarations not expressed via var(--rev-*) tokens.
  document.getElementById('runSweep').addEventListener('click', () => {
    const css = document.getElementById('sampleCss').textContent;
    const out = document.getElementById('findings');
    out.innerHTML = '';
    const decls = css.match(/[\w-]+\s*:\s*[^;{}]+/g) || [];
    decls.forEach((d) => {
      const isTokenized = d.includes('var(--rev-');
      const rawHex = /#[0-9A-Fa-f]{3,8}\b/.test(d);
      const rawPx = /\b\d+px\b/.test(d);
      if (!isTokenized && (rawHex || rawPx)) {
        const li = document.createElement('li');
        li.textContent = 'FINDING: off-token raw value — ' + d.trim() + (rawHex ? ' [hex]' : '') + (rawPx ? ' [px]' : '');
        out.appendChild(li);
      }
    });
    if (!out.children.length) {
      const li = document.createElement('li');
      li.className = 'on-token';
      li.textContent = 'PASS: zero raw values outside tokens.';
      out.appendChild(li);
    }
  });
</script>
```

### Example 2 — Cross-surface task-walk comparison (same task on 3 surfaces, parity checks)

```html
<section class="walk">
  <h1>Task Walk — "Delete project" across 3 surfaces (<code>var(--rev-pattern-parity)</code>)</h1>
  <table class="parity">
    <thead>
      <tr><th scope="col">Check</th><th scope="col">Dashboard</th><th scope="col">Settings</th><th scope="col">Admin</th></tr>
    </thead>
    <tbody>
      <tr><th scope="row">Entry point labeled "Delete"</th><td class="ok">✓</td><td class="ok">✓</td><td class="bad">✗ "Remove"</td></tr>
      <tr><th scope="row">Confirmation dialog is system modal</th><td class="ok">✓</td><td class="ok">✓</td><td class="bad">✗ custom modal</td></tr>
      <tr><th scope="row">Destructive color from danger token</th><td class="ok">✓</td><td class="ok">✓</td><td class="ok">✓</td></tr>
      <tr><th scope="row">Keyboard operable + focus trapped</th><td class="ok">✓</td><td class="bad">✗ no trap</td><td class="ok">✓</td></tr>
      <tr><th scope="row">Terminology matches glossary</th><td class="ok">✓</td><td class="ok">✓</td><td class="bad">✗ drift</td></tr>
    </tbody>
  </table>
  <p class="verdict">Drift map (<code>var(--rev-drift-map)</code>): Admin ranked first (high-traffic, 3 parity fails, includes a11y-critical); Settings second (keyboard trap = major per <code>var(--rev-interaction-consistency)</code>).</p>
</section>
<style>
  .walk { max-width: 640px; font: 14px/1.5 Inter, system-ui, sans-serif; padding: 24px; border: 1px solid #D4D4D4; border-radius: 8px; }
  .walk h1 { font-size: 16px; margin: 0 0 12px; }
  .parity { width: 100%; border-collapse: collapse; }
  .parity th, .parity td { text-align: left; padding: 8px; border-bottom: 1px solid #D4D4D4; }
  .parity thead th { font-weight: 600; color: #171717; }
  .parity tbody th { font-weight: 400; color: #404040; }
  .ok { color: #166534; }
  .bad { color: #991B1B; font-weight: 600; }
  .verdict { color: #404040; margin: 12px 0 0; }
</style>
```

## 10. Implementation Checklist

- [ ] Raw-value sweep run per `--rev-raw-value-scan` (zero outside tokens) — lint/build integrated so it executes at `--rev-audit-frequency`.
- [ ] Component one-offs flagged per `--rev-component-reuse-check`; each reuse finding references the system component it duplicates.
- [ ] Cross-surface task walk executed per `--rev-pattern-parity` for at least one core task (delete/search/invite) across 3 surfaces.
- [ ] Terminology checked against the glossary per `--rev-terminology-check` — one concept, one term, drift logged per string.
- [ ] Spacing/radius/shadow values verified on-scale per `--rev-scale-adherence` — off-scale values logged as mechanical findings.
- [ ] Interaction states compared cross-surface per `--rev-interaction-consistency` — focus treatment divergences ranked major.
- [ ] Drift map built per `--rev-drift-map`, ranked by user impact with high-traffic flows first.
- [ ] `--rev-source-of-truth` confirmed to exist (token/component/pattern docs) before scoring, and the per-surface `--rev-consistency-score` recorded in the report template.

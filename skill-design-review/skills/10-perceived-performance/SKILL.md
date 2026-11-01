---
name: perceived-performance
description: Speed as the user feels it — skeleton discipline, optimistic UI, progress honesty, and the response-time bands every async surface must map to.
tags: [perceived-performance, loading, skeletons, progress, audit]
related: [motion-audit, review-process, report-template]
---

# Design Review Guide: Perceived Performance Audit

## 1. Definition

Users judge speed by feel, not by TTI: a 2s load with skeletons and progress feels faster than a 1.5s blank freeze. The audit checks the perception layer — response-time bands honored (feedback <100ms instant, <1s busy indicator, 1-3s skeleton+progress, >3s cancellable with stages), skeleton discipline (matching layout, never past 3s — the component-recipes contract), optimistic UI for reversible actions, and the perceived-speed motion tricks (continuous motion, delayed empties) verified against honesty rules. The unit of analysis is the async operation: every spinner, skeleton, and progress bar is evidence of either a designed wait or an accidental one, and the audit's job is to tell them apart and score the difference.

## 2. Core Principles

- **Response bands are the contract:** <100ms instant, <1s busy spinner, 1-3s skeleton/progress, >3s staged progress + cancel — every async surface mapped to a band.
- **Skeletons match layout and cap at 3s:** skeleton-to-content shape match and the 3s progress handoff (component-recipes contract).
- **Optimistic UI for reversible actions:** saves, likes, and sends render immediately with an undo path — the perceived-speed jackpot.
- **Progress is honest:** fake progress bars that jump to 90% and stall are worse than none — determinate when possible.
- **Continuous motion reads faster:** progress bars that move smoothly (even slightly fudged) beat stuttering honest ones — motion shapes perception.
- **Nothing just sits blank:** any wait longer than 100ms has some response — blank freezes are the cardinal finding.
- **Delays are designed, not natural:** content appears when renderable, not batched behind the slowest call — waterfall audits reveal batching sins.
- **Perceived speed is measured:** time-to-first-meaningful-content tracked per surface — the metric the audit optimizes.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Response bands | `--rev-response-bands` | `<100ms,1s,3s,staged` | Nielsen bands; every async mapped |
| Skeleton contract | `--rev-skeleton-contract` | `match-layout+cap-3s` | Then progress indication |
| Optimistic UI | `--rev-optimistic-ui` | `reversible-actions` | Instant render + undo |
| Progress honesty | `--rev-progress-honesty` | `determinate-when-possible` | Fake stalls = finding |
| Continuous motion | `--rev-continuous-motion` | `smooth-over-stutter` | Perception-shaped motion |
| No blank freeze | `--rev-no-blank-freeze` | `response-under-100ms` | Any wait has feedback |
| Waterfall check | `--rev-waterfall-check` | `no-artificial-batching` | Content when renderable |
| TTMC metric | `--rev-ttmc-metric` | `time-to-meaningful-content` | The audited metric |
| Cancellable long loads | `--rev-cancellable-long-loads` | `>3s-offers-cancel` | User control contract |
| Perception score | `--rev-perception-score` | `per-surface` | Feeds report template |

Consume them by linking `assets/css/perceived-performance.css` once at the review-harness root, then reading `var(--rev-<role>)` — in CSS for the band/skeleton styling and in JS via `getComputedStyle(document.documentElement).getPropertyValue(...)` to drive band thresholds and pass/fail assertions in the audit tooling. The tokens encode contracts, not pixels; a surface that violates its mapped band fails the check regardless of how fast the backend is.

## 4. Composition

- **Composes with component-recipes empty-loading-error:** that recipe implements the states; this audit verifies them — the split is "who builds" vs "who scores."
- **Composes with motion-audit (guide 05):** skeleton/progress motion and the duration ladder are shared checks — run the two audits in one pass over loading surfaces.
- **Composes with skill-animation loading-states:** that discipline defines the loading patterns; the audit verifies application — deviations become findings, not preferences.

## 5. Signature Patterns

- **The band map:** every async operation on the surface listed with its expected duration and matching band treatment — unmapped waits are findings. The map is a table (operation, expected duration, band, treatment) and it doubles as the audit's evidence sheet: each row either passes or produces a finding row in the report template.
- **The throttle test:** audit with CPU/network throttled (4x CPU, slow 3G) — the perception layer is only tested when it's actually needed. Unthrottled passes prove nothing about the 3G commuter or the low-end Android; throttling makes every band violation reproducible on demand.

## 6. Real-World Use Cases

- **Async-heavy dashboards and checkout flows** where dozens of parallel calls create wait surfaces the team never designed.
- **Products with slow backends** improving feel without infra cost — skeleton discipline, optimistic UI, and staged progress buy back seconds the backend can't.
- **Audit passes hunting the classics:** blank freezes, skeleton-forever states, fake progress stalls.

## 7. Combination Notes

### With other design-review skills

- **Good with motion-audit, a11y-audit, and interaction-states-audit:** loading states are where all three meet — motion shapes perception, AT users need narrated waits, and loading is a state like any other. Run them together on async surfaces.
- **Good with report-template:** the perception score is a per-surface axis; this audit's band map rows convert directly into findings rows.
- **Caution with motion-audit:** both audits judge the same skeletons and spinners, but through different lenses — honesty here vs restraint there. Coordinate so a smooth-but-inedited progress animation isn't scored twice or double-flagged.
- **No avoid list:** perceived performance composes cleanly with every audit; the only incompatibility is a surface with no async at all, where the audit trivially passes.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** all three favor honest, structured surfaces — skeletons that match layout read naturally in flat/minimal products, and class-morphism's layered depth makes the skeleton-to-content handoff visually seamless.
- **No caution entries:** perception discipline is style-agnostic; even brutalist or maximalist products need band-compliant waits, so the audit's contracts hold across the style spectrum.

### With motion skills (companion repo skill-animation)

- **Good affinity with loading-states and easing-timing:** loading-states is the source of the skeleton/progress patterns this audit verifies, and easing-timing's duration ladder governs the transitions between band treatments (skeleton fade to content, busy to skeleton).
- **Caution with ambient-motion:** ambient loops during waits fight with progress perception — a background animation running while a user waits makes the wait feel longer and muddies what "the page is working" looks like. Suppress ambient motion while a load is in flight.

## 8. Anti-Patterns

- **The blank freeze** — no feedback until the full response lands
- **Skeleton-forever** — skeletons hanging past 3s with no progress
- **Stalling progress** — bars that jump to 90% and freeze there
- **Batched-by-laziness** — content waiting for the slowest API call

### Accessibility Notes

Perceived-performance states are announced states: skeletons and progress must narrate politely (WCAG 4.1.3 status messages), progress bars need accessible names describing what is loading, and all loading motion respects reduced-motion — perceived speed must not come at the cost of AT users' orientation. In practice this means `aria-live="polite"` regions that announce "Loading orders…" once (not per skeleton shuffle), `<progress>` elements or `role="progressbar"` with `aria-valuenow` when determinate, and skeleton shimmer disabled under `prefers-reduced-motion` while the skeleton shapes themselves remain. The fallback rule: if progressive enhancement is limited, ensure at minimum that waits >1s produce a narrated status — a spoken "loading" beats a silent freeze.

## 9. Code Examples

### Example 1 — Response-band map with skeleton-to-progress handoff

Tokens: `assets/css/perceived-performance.css`

```html
<div class="bandmap">
  <h3>Async surface: order dashboard</h3>
  <ul id="ops">
    <li data-band="instant">Save filter — instant (&lt;100ms)</li>
    <li data-band="busy">Validate address — busy (&lt;1s)</li>
    <li data-band="skeleton">Load order list — skeleton (1-3s)</li>
    <li data-band="progress">Generate report — progress + cancel (&gt;3s)</li>
  </ul>
  <div class="panel">
    <div id="skel" class="skeleton" hidden></div>
    <div id="prog" class="progress" hidden>
      <div class="bar"></div>
      <button id="cancel">Cancel</button>
    </div>
    <div id="done" hidden>Report ready.</div>
  </div>
  <p id="verdict" role="status"></p>
</div>
<script>
  const r = getComputedStyle(document.documentElement);
  const cap = (r.getPropertyValue('--rev-skeleton-contract') || '').includes('cap-3s');
  // Simulated slow load: skeleton at t=0, progress handoff at 3s (the cap)
  const skel = document.getElementById('skel');
  const prog = document.getElementById('prog');
  skel.hidden = false;                                  // band: 1-3s skeleton
  setTimeout(() => {                                    // 3s cap reached
    skel.hidden = true; prog.hidden = false;            // handoff to progress
    let pct = 8; const iv = setInterval(() => {
      pct = Math.min(100, pct + 6);                     // smooth, honest increments
      prog.querySelector('.bar').style.width = pct + '%';
      if (pct >= 100) { clearInterval(iv); prog.hidden = true;
        document.getElementById('done').hidden = false;
        document.getElementById('verdict').textContent =
          cap ? 'PASS: skeleton capped at 3s, handed off to staged progress with cancel.' : 'CHECK: skeleton cap token missing.';
      }
    }, 200);
    document.getElementById('cancel').onclick = () => { clearInterval(iv);
      document.getElementById('verdict').textContent = 'Load cancelled — >3s contract honored.'; };
  }, 3000);
</script>
<style>
  .bandmap { font: 14px/1.5 system-ui, sans-serif; max-width: 460px; padding: 16px; border: 1px solid var(--rev-response-bands, #ddd); border-radius: 8px; }
  [data-band]::before { content: '● '; }
  .skeleton { height: 56px; border-radius: 6px; background: linear-gradient(90deg, #ececec 25%, #f8f8f8 50%, #ececec 75%); background-size: 200% 100%; animation: shim 1.2s linear infinite; }
  .progress { display: flex; align-items: center; gap: 12px; }
  .progress .bar { height: 8px; width: 8%; background: #2563eb; border-radius: 4px; transition: width 200ms linear; flex: 1; }
  @keyframes shim { to { background-position: -200% 0; } }
  @media (prefers-reduced-motion: reduce) { .skeleton { animation: none; } }
</style>
```

### Example 2 — Skeleton vs blank A/B with timers

```html
<div class="ab">
  <section><h4>A — blank (finding)</h4><div id="a" class="zone"></div><p class="t" id="ta"></p></section>
  <section><h4>B — skeleton (pass)</h4><div id="b" class="zone"><div class="sk"></div></div><p class="t" id="tb"></p></section>
</div>
<script>
  const start = performance.now();
  const ta = document.getElementById('ta'), tb = document.getElementById('tb');
  const tick = () => {
    const ms = Math.round(performance.now() - start);
    ta.textContent = ms + 'ms blank freeze';
    tb.textContent = ms + 'ms skeleton visible';
    if (ms >= 1800) {
      document.getElementById('a').textContent = 'Content (arrived late, user already lost)';
      document.getElementById('b').innerHTML = '<strong>Content</strong> — shape matched the skeleton';
      tb.textContent = ms + 'ms: skeleton → content, shape match PASS';
    } else requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
</script>
<style>
  .ab { display: flex; gap: 16px; font: 14px/1.5 system-ui, sans-serif; }
  .zone { width: 200px; height: 80px; border: 1px solid #ddd; border-radius: 6px; padding: 12px; box-sizing: border-box; }
  .sk { height: 100%; border-radius: 4px; background: linear-gradient(90deg, #ececec 25%, #f8f8f8 50%, #ececec 75%); background-size: 200% 100%; animation: shim 1.2s linear infinite; }
  @keyframes shim { to { background-position: -200% 0; } }
  @media (prefers-reduced-motion: reduce) { .sk { animation: none; } }
</style>
```

## 10. Implementation Checklist

- [ ] Every async operation on the audited surface appears in the band map with a band treatment matching `--rev-response-bands`.
- [ ] No wait longer than `--rev-no-blank-freeze` (100ms) shows a blank region — freezes logged as blocker findings.
- [ ] Skeletons match final content layout and hand off to progress at the `--rev-skeleton-contract` 3s cap.
- [ ] All loads expected over `--rev-cancellable-long-loads` (3s) expose a working cancel affordance.
- [ ] Optimistic UI applied to reversible actions per `--rev-optimistic-ui`, each with an undo path.
- [ ] Progress bars are determinate where possible per `--rev-progress-honesty`; no bar stalls above its real state.
- [ ] Throttle test (4x CPU, slow 3G) run and TTMC recorded per `--rev-ttmc-metric`.
- [ ] Loading states narrate politely and respect reduced motion; perception score recorded for `--rev-perception-score`.

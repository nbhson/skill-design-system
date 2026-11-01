---
name: visual-hierarchy-audit
description: Does the page guide the eye: primary action dominance, scanning patterns, and the squint test.
tags: [hierarchy, audit, layout, scanning, emphasis]
related: [review-process, spacing-rhythm-audit, typography-audit]
---

# Design Review Guide: Visual Hierarchy Audit

## 1. Definition

Visual hierarchy is whether the page tells users what matters first, second, third — through size, weight, color, and position. The audit pass: blur/squint the page (do 3 elements dominate correctly?), trace the scanning path (F/Z patterns, primary action found in under 5 seconds), and check competing emphasis (two primaries, banners fighting banners). This guide owns the hierarchy audit checklist and its scoring.

## 2. Core Principles

- **The squint test is the first check:** blurred, the page shows 2-3 dominant elements — if everything is equally loud, hierarchy has failed.
- **One primary action per view:** the single most-emphasized action is findable in under 5 seconds — competing primaries dissolve hierarchy.
- **The scanning path is traced:** where does the eye land first, second, third? The path must serve the task (F-pattern reading, Z-pattern landing pages).
- **Size/weight/color are used consistently:** headers scale, body stays body — hierarchy through random emphasis is noise.
- **Whitespace is hierarchy's tool:** groups separated by space beat groups separated by boxes — box-everything audits as a failure.
- **Position encodes importance:** top-left (LTR) and center get emphasis — important actions buried bottom-right audit as findings.
- **Density is checked against the task:** data-dense views use hierarchy to layer (summary > detail); marketing views use it to sequence.
- **Hierarchy is tested on real content:** lorem-ipsum audits are invalid — real headlines and real copy shift emphasis.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Squint Test | `--rev-squint-test` | `2-3-dominant-elements` | First check; blurred view |
| Primary Finding | `--rev-primary-finding` | `under-5-seconds` | Primary action findability budget |
| One Primary Rule | `--rev-one-primary-rule` | `per-view` | Competing primaries = finding |
| Scan Path Check | `--rev-scan-path-check` | `f/z-pattern-traced` | Eye path serves the task |
| Emphasis Tools | `--rev-emphasis-tools` | `size,weight,color,position` | Consistent, not random |
| Whitespace Hierarchy | `--rev-whitespace-hierarchy` | `space-over-boxes` | Box-everything = finding |
| Position Emphasis | `--rev-position-emphasis` | `task-relevant` | Important ≠ buried |
| Density Layering | `--rev-density-layering` | `summary-over-detail` | Dense views layer information |
| Real Content Rule | `--rev-real-content-rule` | `lorem-invalid` | Audits run on real copy |
| Hierarchy Score | `--rev-hierarchy-score` | `per-surface` | Scored in the report template |

Consume them by linking `assets/css/visual-hierarchy-audit.css` in the audit tooling, then reading `var(--rev-<role>)` when rendering checklists and scorecards — the thresholds (2-3 dominant elements, under-5-seconds) are the audit's pass/fail constants. The hierarchy score token feeds the report template per surface, so one surface, one score, one place it lands.

## 4. Composition

- **Composes with skill-typography visual-hierarchy:** the type scale is a hierarchy tool — audits check its application.
- **Composes with spacing-rhythm-audit (guide 07):** whitespace and rhythm are hierarchy's substrate.
- **Composes with skill-color-theory:** emphasis color and contrast models feed the hierarchy checks.

## 5. Signature Patterns

- **The blur pass:** screenshot → blur 8px → mark the 3 dominant elements → compare against intended hierarchy — fast, brutal, effective. Blur removes the details the eye rationalizes around, leaving only what size/weight/color actually broadcast; if the intended primary doesn't survive the blur, it isn't primary.
- **The 5-second test:** new users given the surface asked 'what's the main action?' — wrong answers are hierarchy findings. The budget is the `--rev-primary-finding` token: if the answer doesn't arrive in under 5 seconds, the emphasis system failed regardless of how the design intent reads.

## 6. Real-World Use Cases

- **Landing pages and marketing surfaces where hierarchy drives conversion:** the Z-pattern trace and one-primary rule are the checks that decide whether the CTA wins.
- **Dense dashboards where layering prevents overwhelm:** density-layering (summary > detail) keeps data-heavy views scannable instead of flat walls of numbers.
- **Audit: competing primaries, box-everything layouts, buried CTAs:** the named findings this pass exists to catch — two loud buttons, border-heavy grouping, key actions below the fold.

## 7. Combination Notes

### With other design-review skills

- **Good with review-process:** hierarchy findings enter the severity scale and ticket loop like any other — a buried primary on a checkout step is a blocker candidate, and the process decides that, not this audit.
- **Good with spacing-rhythm-audit and typography-audit:** whitespace and the type scale are hierarchy's two main tools — these audits read the same surface in the same session and share the space-over-boxes check.
- **Good with consistency-audit, a11y-audit, interaction-states-audit, content-microcopy-audit, perceived-performance, responsive-audit, and motion-audit:** each contributes adjacent checks — consistency verifies the emphasis tools are uniform, a11y verifies hierarchy survives color removal and zoom, motion-audit verifies entrances don't fight the scan path.
- **Good with report-template:** the per-surface hierarchy score lands in the report alongside the other audit scores.
- **Caution with content-microcopy-audit:** both audits judge emphasis through copy — real headlines and button labels shift what dominates, so run them on the same final copy, not in isolation, or findings will contradict each other.
- **No avoid list:** hierarchy overlaps but never conflicts with sibling audits — it reads the page at the coarsest level, and the others refine.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** all three rely on disciplined emphasis — few elements, restrained decoration — which makes the squint test and one-primary rule straightforward to pass and easy to verify.
- **Caution with maximalism:** maximalist surfaces are intentionally loud and dense; the 2-3-dominant-elements bar may legitimately fail on style grounds. If the style is the choice, audit hierarchy against the style's own intent — deviations from maximalist intent still count, but uniform-loudness is not automatically a finding.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** entrance and hover timing shapes where attention lands during the first 5 seconds — staggered entrances following the duration ladder should reinforce, not contradict, the intended scan path.
- **Good affinity with entrance-exit:** entrance choreography is hierarchy in time; the audit checks that the first element animated is the element that should dominate, and that entrances don't re-trigger on scroll jitter to fake emphasis.

## 8. Anti-Patterns

- **Everything-is-important:** uniform emphasis making nothing important
- **Box-world:** every group boxed until boxes are the hierarchy
- **Buried primary:** the key action below the fold behind secondary content
- **Lorem-ipsum hierarchy:** emphasis designed on fake copy

### Accessibility Notes

Hierarchy must not rely on color alone (WCAG 1.4.1) and must survive zoom/reflow (1.4.4/1.4.10) — the audit checks hierarchy with color removed and at 400% zoom; heading structure (2.4.6) is the AT parallel of visual hierarchy. In practice this means running the blur pass a second time in grayscale: if the primary action disappears when the tint is gone, emphasis was carried by hue, and size/weight/position must take over. The 400% zoom pass catches hierarchies that collapse when reflow pushes the buried action even further down. The fallback rule bridges visual and semantic: if the visual audit is inconclusive, check the heading outline + primary-action aria — semantic hierarchy that works for AT usually reveals the visual fix.

## 9. Code Examples

### Example 1 — Squint-test demo (CSS blur toggle over a sample dashboard)

```html
<section class="dash" id="dash">
  <h1>Billing overview</h1>
  <div class="dash-metric"><span class="metric-label">Outstanding · November 2026</span><span class="metric-value">$12,480</span></div>
  <button class="dash-primary">Pay invoices</button>
  <button class="dash-secondary">Download CSV</button>
  <ul class="dash-list">
    <li>INV-2041 · Acme Corp · $4,200</li>
    <li>INV-2042 · Globex · $8,280</li>
  </ul>
</section>
<label class="squint-toggle"><input type="checkbox" id="blurToggle" /> Squint test (blur 8px)</label>
<style>
  .dash { max-width: 420px; font: 14px/1.5 Inter, system-ui, sans-serif; padding: 24px; border: 1px solid #D4D4D4; border-radius: 8px; transition: filter 200ms ease; }
  .dash.squinting { filter: blur(8px); } /* --rev-squint-test: blurred view */
  .dash h1 { font-size: 20px; margin: 0 0 2px; }
  .dash-metric { display: flex; flex-direction: column; margin-bottom: 16px; } /* dominant 1: largest text */
  .metric-label { font-size: 12px; color: #737373; }
  .metric-value { font-size: 32px; font-weight: 700; color: #171717; }
  .dash-primary { background: #2563EB; color: #fff; border: none; border-radius: 8px; padding: 10px 20px; font-weight: 600; margin-right: 8px; } /* dominant 2 */
  .dash-secondary { background: transparent; color: #2563EB; border: 1px solid #D4D4D4; border-radius: 8px; padding: 10px 16px; }
  .dash-list { margin: 16px 0 0; padding: 0; list-style: none; color: #404040; border-top: 1px solid #D4D4F4; } /* subordinate rows */
  .dash-list li { padding: 8px 0; border-bottom: 1px solid #F5F5F5; }
</style>
<script>
  // Blur pass: mark the 3 dominant elements against var(--rev-squint-test) = 2-3-dominant-elements
  const dash = document.getElementById('dash');
  document.getElementById('blurToggle').addEventListener('change', (e) => {
    dash.classList.toggle('squinting', e.target.checked);
  });
</script>
```

### Example 2 — 5-second test harness (surface shown, prompt, timer, answer check)

```html
<section class="harness">
  <h1>5-Second Test — <code>var(--rev-primary-finding)</code>: under-5-seconds</h1>
  <div id="stage" class="stage hidden">
    <button class="cta">Start free trial</button>
    <a class="quiet" href="#docs">Read the docs</a>
  </div>
  <p id="prompt" class="prompt hidden"><strong>What's the main action?</strong></p>
  <form id="answerForm" class="answer hidden">
    <label>Answer: <input id="answer" type="text" autocomplete="off" /></label>
    <button type="submit">Check</button>
  </form>
  <p id="result" role="status" aria-live="polite"></p>
</section>
<style>
  .harness { max-width: 480px; font: 14px/1.5 Inter, system-ui, sans-serif; padding: 24px; border: 1px solid #D4D4D4; border-radius: 8px; }
  .harness h1 { font-size: 16px; margin: 0 0 12px; }
  .stage { display: flex; gap: 12px; padding: 24px; border: 1px dashed #D4D4D4; border-radius: 8px; margin-bottom: 12px; }
  .cta { background: #2563EB; color: #fff; border: none; border-radius: 8px; padding: 10px 20px; font-weight: 600; } /* intended primary */
  .quiet { color: #737373; align-self: center; }
  .hidden { display: none; }
  .prompt, .answer { margin: 8px 0; }
  .answer input { padding: 6px 10px; border: 1px solid #D4D4D4; border-radius: 6px; }
  #result.pass { color: #166534; } #result.fail { color: #991B1B; }
</style>
<script>
  // Show the surface for exactly 5 seconds (--rev-primary-finding budget), then hide and ask.
  const BUDGET_MS = 5000;
  const stage = document.getElementById('stage');
  const prompt = document.getElementById('prompt');
  const form = document.getElementById('answerForm');
  const result = document.getElementById('result');
  stage.classList.remove('hidden');
  const timer = setTimeout(() => {
    stage.classList.add('hidden');       // surface removed — answer from memory only
    prompt.classList.remove('hidden');
    form.classList.remove('hidden');
    document.getElementById('answer').focus();
  }, BUDGET_MS);
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    clearTimeout(timer);
    const guess = document.getElementById('answer').value.trim().toLowerCase();
    const ok = guess.includes('trial');
    result.textContent = ok
      ? 'Pass: primary action identified within the 5-second budget.'
      : 'Fail: hierarchy finding — primary not identified; run the blur pass.';
    result.className = ok ? 'pass' : 'fail';
  });
</script>
```

## 10. Implementation Checklist

- [ ] Squint pass run first per `--rev-squint-test`: blurred surface shows exactly 2-3 dominant elements matching intent.
- [ ] Primary action identified under the `--rev-primary-finding` budget (under 5 seconds); one primary per view enforced via `--rev-one-primary-rule`.
- [ ] Scan path traced per `--rev-scan-path-check` (F/Z pattern) and confirmed to serve the task.
- [ ] Emphasis drawn only from `--rev-emphasis-tools` (size, weight, color, position), applied consistently across the surface.
- [ ] Whitespace grouping verified per `--rev-whitespace-hierarchy`; important elements not buried per `--rev-position-emphasis`.
- [ ] Density layered per `--rev-density-layering`; audit run on real copy per `--rev-real-content-rule`; the per-surface `--rev-hierarchy-score` recorded in the report template.

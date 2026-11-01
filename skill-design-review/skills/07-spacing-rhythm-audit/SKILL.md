---
name: spacing-rhythm-audit
description: The 4/8px grid check for design reviews — off-scale spacing, grouping errors, and vertical rhythm that holds across the surface.
tags: [spacing, rhythm, proximity, layout, audit]
related: [visual-hierarchy-audit, consistency-audit, responsive-audit]
---

# Design Review Guide: Spacing & Rhythm Audit

## 1. Definition

Spacing is the invisible 60% of perceived quality: off-scale gaps read as "something's off" without naming why. The audit verifies that all spacing derives from the 4/8px scale defined by skill-design-tokens, that grouping logic follows the proximity principle (related items sit closer than unrelated ones), that component-internal spacing is consistent (does the card use the same padding everywhere?), and that vertical rhythm holds down the page — surfaces should breathe in consistent intervals, not lurch between 16, 40, 22, and 90px gaps. Unlike judgment-heavy reviews, most spacing findings are mechanical: a value is either on-scale or it is not, which makes this the fastest audit to script and the easiest to score per surface.

## 2. Core Principles

- **Everything is on-scale:** padding/margin/gap values divisible per the 4/8px system — off-scale values are mechanical findings, not taste calls.
- **Proximity is the grouping test:** related items sit closer than unrelated ones — if users can't tell what belongs to what by spacing alone, grouping has failed.
- **Component-internal spacing is consistent:** the card's padding is the card's padding everywhere — per-instance drift is a finding.
- **Vertical rhythm holds:** consistent section spacing intervals down the page — lurching gaps (16, 40, 22, 90) are findings.
- **Whitespace beats boxes:** if groups need borders to be understood, the spacing is wrong (shared with visual-hierarchy).
- **Density tiers are declared:** compact/default/comfortable tiers documented — mixed densities on one surface are findings.
- **Alignment is absolute:** left edges align across components (LTR) — almost-aligned elements audit as major findings.
- **Responsive spacing scales:** gaps shrink proportionally at breakpoints — fixed spacing that breaks mobile layouts is a finding.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Spacing scale | `--rev-spacing-scale` | `4-8px-system` | All values on-scale |
| Proximity test | `--rev-proximity-test` | `grouping-by-space` | Related > unrelated distance |
| Component consistency | `--rev-component-consistency` | `same-padding-everywhere` | Per-instance drift flagged |
| Vertical rhythm | `--rev-vertical-rhythm` | `consistent-intervals` | No lurching gaps |
| Space over boxes | `--rev-space-over-boxes` | `borders-are-failure` | Shared with hierarchy audit |
| Density tiers | `--rev-density-tiers` | `compact,default,comfortable` | Declared per surface |
| Alignment check | `--rev-alignment-check` | `edges-align` | Almost-aligned = finding |
| Responsive spacing | `--rev-responsive-spacing` | `proportional-shrink` | Breakpoint-verified |
| Raw value scan | `--rev-raw-value-scan` | `lint-assisted` | Mechanical sweep |
| Spacing score | `--rev-spacing-score` | `per-surface` | Feeds report template |

Consume them by linking `assets/css/spacing-rhythm-audit.css` at the review harness root, then reading `var(--rev-...)` from audit tooling and overlays — the tokens keep the audit's thresholds declarative so a scale change in skill-design-tokens propagates here without editing scripts.

## 4. Composition

- **Composes with skill-design-tokens spacing guide:** that guide defines the scale; this audit verifies it. The audit never invents step values — a gap that feels right but is off-scale is still a finding, and a scale extension goes through token governance, not component CSS.
- **Composes with visual-hierarchy-audit (guide 03):** whitespace is hierarchy's tool — the "space over boxes" check is shared, so one pass covers both: groups that survive without borders pass the hierarchy eye-test too.
- **Composes with responsive-audit (guide 11):** spacing behavior at breakpoints is the crossover surface — the proportional-shrink contract is verified here mechanically and there behaviorally.

## 5. Signature Patterns

- **The overlay pass:** render the surface with a spacing-scale grid overlay — off-scale values and misalignments become visually obvious in seconds. The overlay draws column lines at scale intervals so a 17px padding shows as a hairline misalignment against the nearest 16px line, and a 22px section gap visibly straddles 20 and 24.
- **The proximity walk:** for each group, ask "could a user circle what belongs together using spacing alone?" — failures are grouping findings. The walk is done per container, top to bottom, and its failures map directly to either spacing changes (preferred) or, as a last resort, separators.

## 6. Real-World Use Cases

- **Any surface — spacing drift is universal,** making this the default first pass of every design review.
- **Design system adoption measurement,** where the scale adherence rate is the metric teams track quarter over quarter.
- **Audit deliverables:** off-scale gaps, misaligned edges, and box-everything grouping reported per surface with the spacing score.

## 7. Combination Notes

### With other design-review skills

- **Good with review-process and report-template:** spacing findings are mechanical, so they slot into the severity scale cleanly and feed the per-surface spacing score into the final report.
- **Good with visual-hierarchy-audit and consistency-audit:** proximity, whitespace-over-boxes, and per-instance padding drift are the shared checks — run the overlay pass once and both audits read from it.
- **Good with typography-audit, a11y-audit, interaction-states-audit, content-microcopy-audit, perceived-performance, responsive-audit, and motion-audit:** none of them conflict — spacing findings (tight targets, lurching rhythm, fixed mobile gaps) feed each of these as input, and each returns context that re-ranks spacing severity.
- **No caution or avoid list:** spacing is the substrate every other check sits on; there is no skill whose scope it contradicts.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** all three lean on whitespace and grid discipline instead of ornament, so a passing spacing audit is close to a passing style review — the styles amplify the audit's value.
- **Caution with brutalism-ui:** the style deliberately breaks the grid, overlaps edges, and uses jarring gaps as an aesthetic statement. Audit against the style's own declared spacing intent rather than the default 4/8px contract, and record the deviation as intentional, not as drift.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** spacing changes that animate — expanding cards, accordion opens, hover lifts — must use the shared easing and duration tokens; the audit verifies the resting positions while easing-timing verifies the path between them, and off-scale resting gaps invalidate the animation regardless of how smooth it is.

## 8. Anti-Patterns

- **Off-scale sprawl:** 17px paddings and 13px gaps from nowhere
- **Proximity failure:** groups closer to strangers than to their own members
- **Lurching rhythm:** vertical gaps jumping without system
- **Almost-aligned:** elements 3px off the column line

### Accessibility Notes

Spacing serves WCAG 1.4.12 (text spacing tolerance: no clipping when users override spacing) and 2.5.8 (target spacing): the audit verifies surfaces survive user spacing overrides and that interactive targets keep effective separation. In practice this means the overlay pass runs twice — once at authored values and once with user-agent text spacing overrides applied — because a layout that is on-scale at rest can still clip labels when line-height, letter, word, and paragraph spacing are overridden. Target spacing is the proximity principle applied to controls: adjacent interactive targets must keep enough effective separation that a pointer or touch near one does not activate the other. The fallback rule: if the overlay pass is unavailable, run the raw-value lint sweep — off-scale values are mechanical and machine-findable, so a computed-style dump against the 4/8px scale recovers nearly all findings without visual tooling.

## 9. Code Examples

### Example 1 — Spacing overlay: exposing off-scale gaps in a card layout

Tokens: `assets/css/spacing-rhythm-audit.css`

```html
<button id="overlay-toggle" type="button">Toggle spacing overlay</button>
<article class="card">
  <h3>Weekly report</h3>
  <p>Usage grew 12% across all regions.</p>
  <button class="card-cta" type="button">View details</button>
</article>
<style>
  :root {
    /* mirrors assets/css/spacing-rhythm-audit.css */
    --rev-spacing-scale: 4-8px-system;
    --rev-raw-value-scan: lint-assisted;
    --rev-alignment-check: edges-align;
    /* scale steps consumed from skill-design-tokens spacing-sizing */
    --s1: 4px; --s2: 8px; --s3: 12px; --s4: 16px; --s6: 24px;
  }
  .card {
    max-width: 320px;
    padding: var(--s4);
    border: 1px solid #d4d4d4;
    border-radius: 8px;
    font: 14px/1.5 Inter, system-ui, sans-serif;
  }
  .card h3 { margin: 0 0 var(--s2); }
  .card p  { margin: 0 0 var(--s4); } /* an off-scale 13px here shows instantly */
  .card-cta { padding: var(--s2) var(--s3); }
  body.overlay-on .card { outline: 2px solid rgba(37,99,235,.35); position: relative; }
  body.overlay-on .card::before {
    content: "";
    position: absolute; inset: 0; pointer-events: none;
    background:
      repeating-linear-gradient(to right, rgba(37,99,235,.12) 0 1px, transparent 1px var(--s4)),
      repeating-linear-gradient(to bottom, rgba(37,99,235,.12) 0 1px, transparent 1px var(--s4));
  }
</style>
<script>
  // Mechanical sweep per --rev-raw-value-scan: flag any gap off the 4/8px scale
  document.getElementById('overlay-toggle').addEventListener('click', (e) => {
    document.body.classList.toggle('overlay-on');
    for (const el of document.querySelectorAll('.card, .card *')) {
      const cs = getComputedStyle(el);
      for (const side of ['Top','Right','Bottom','Left']) {
        const v = parseFloat(cs['padding' + side]);
        if (v && v % 4 !== 0) console.warn('off-scale padding', side.toLowerCase(), v, el);
      }
    }
  });
</script>
```

### Example 2 — Proximity test: spacing shows membership; boxes hide failure

```html
<div class="panel">
  <h4>Team members</h4>
  <div class="group group-good">
    <span class="member">Ada</span><span class="member">Lin</span><span class="member">Sam</span>
  </div>
  <div class="group group-bad">
    <span class="member boxed">Ada</span><span class="member boxed">Lin</span><span class="member boxed">Sam</span>
  </div>
</div>
<style>
  :root { --rev-proximity-test: grouping-by-space; --rev-space-over-boxes: borders-are-failure; }
  .panel { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 360px; }
  .group  { display: flex; margin: 0 0 16px; } /* 16px between groups = unrelated distance */
  .member { padding: 8px 12px; }
  /* Good: members 4px apart (related) vs 16px between groups — spacing alone circles the team */
  .group-good .member + .member { margin-left: 4px; }
  /* Counter-example: members spread 16px apart — spacing no longer groups, so every
     member needs a box. Per --rev-space-over-boxes, borders-are-failure: the boxes
     are the symptom; the fix is closing the gap, not styling the border. */
  .group-bad  .member + .member { margin-left: 16px; }
  .boxed { border: 1px solid #d4d4d4; border-radius: 6px; }
</style>
```

## 10. Implementation Checklist

- [ ] Every padding, margin, and gap on the surface resolves to `var(--rev-spacing-scale)` steps — the raw-value sweep reports zero off-scale values.
- [ ] The proximity walk passed: membership is readable from `var(--rev-proximity-test)` spacing alone, with borders removed wherever they were doing spacing's job.
- [ ] Shared components show `var(--rev-component-consistency)` padding in every instance — no per-instance overrides.
- [ ] Vertical rhythm follows `var(--rev-vertical-rhythm)` intervals; the gap histogram has no lurching outliers.
- [ ] Density is declared per surface against `var(--rev-density-tiers)` — no mixed compact/comfortable on one screen.
- [ ] Left edges align across components per `var(--rev-alignment-check)`; almost-aligned elements are filed as major findings.
- [ ] Breakpoints shrink spacing proportionally per `var(--rev-responsive-spacing)`, verified with text-spacing overrides for WCAG 1.4.12.
- [ ] The per-surface `var(--rev-spacing-score)` is recorded in the report template with each finding's severity.

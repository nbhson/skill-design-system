---
name: line-height
description: Leading inversely proportional to size — 1.1–1.2 display, 1.5 body, 1.7 long-form — plus the vertical rhythm that aligns text to the 4px grid.
tags: [typography, line-height, rhythm, readability, leading]
related: [type-scale, font-pairing, readability-legibility]
---

# Typography Skill: Line-Height & Rhythm

## 1. Definition

Line-height (leading) controls reading comfort and vertical rhythm: tight for display (1.1–1.2), relaxed for body (1.5), looser for long-form (1.7). It is the quietest typography decision — nobody notices good leading, everybody feels bad leading — and in Vietnamese and other stacked-diacritic scripts, line-height is also the difference between readable and clipped text. Leading never ships alone: it is bundled into text roles with size and weight, and paragraph spacing snaps to the 4px grid, so rhythm is a system property rather than a per-component guess.

## 2. Core Principles

- **Line-height decreases as size increases:** display 1.1–1.2, headings 1.2–1.3, body 1.5, long-form 1.7.
- **Unitless line-heights only:** unitless values inherit as ratios and scale with font size — px line-heights break at every zoom level.
- **Body line-height never below 1.5:** WCAG 1.4.12 users and dyslexic readers need the air; 1.5 is the floor for paragraphs.
- **Diacritics need headroom:** Vietnamese stacked marks (ề, ậ) require line-height ≥ 1.5 and fallbacks that do not clip — verify at every step.
- **Rhythm comes from line-height + spacing tokens:** paragraph spacing uses space tokens; the combination snaps text to the 4px grid.
- **Headings snap into rhythm:** round heading line-height boxes to grid multiples where layout alignment matters.
- **CJK and Latin differ:** CJK runs taller (1.7–2.0); locale-aware line-height tokens prevent cramped mixed-script text.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Line-height display | `--type-line-height-display` | `1.1` | Hero/marketing display sizes |
| Line-height heading | `--type-line-height-heading` | `1.2` | h1–h4; tight but safe for diacritics at 2xl+ |
| Line-height body | `--type-line-height-body` | `1.5` | Default paragraphs; WCAG 1.4.12 floor |
| Line-height relaxed | `--type-line-height-relaxed` | `1.7` | Long-form articles, documentation |
| Line-height ui | `--type-line-height-ui` | `1.35` | Buttons, list items, labels — compact but uncramped |
| Paragraph gap | `--type-paragraph-gap` | `var(--space-4)` | Paragraph spacing from the 4px grid, not margin guesses |
| Rhythm grid | `--type-rhythm-grid` | `4px` | Vertical rhythm snaps to the spacing scale |
| Line-height CJK | `--type-line-height-cjk` | `1.8` | CJK locale variant; taller boxes for dense glyphs |
| Diacritic headroom | `--type-diacritic-headroom` | `1.5-min` | Vietnamese stacked marks never clip below 1.5 |
| Measure default | `--type-measure-default` | `65ch` | Paragraph max-width; see readability-legibility guide |

Consume them by linking `assets/css/line-height.css` at the app root and referencing `var(--type-line-height-*)` inside text roles only — no component invents a leading value inline. Paragraph spacing pulls `var(--type-paragraph-gap)` (which itself references the spacing scale's `var(--space-4)`), keeping rhythm grid-snapped.

## 4. Composition

- **Composes with type-scale:** every scale step ships with its line-height as a bundle — the pair is reviewed together, so a size change is never merged without its leading adjustment.
- **Composes with spacing tokens (skill-design-tokens guide 03):** rhythm = line-height boxes + space tokens; margins are typographic exceptions only, never the default paragraph spacing mechanism.
- **Composes with multilingual-vietnamese:** diacritic headroom is a hard constraint that can override aesthetic tightness at any step — a 1.1 hero in Latin becomes ≥ 1.3 in Vietnamese.

## 5. Signature Patterns

- **Role-bundled leading:** text roles bundle (size, weight, line-height, tracking) so no consumer invents a leading value — the role API is the only path to a rendered line box.
- **Grid-snapped headings:** headings get line-height computed so their box lands on the 4px grid, aligning section starts across columns and cards.

## 6. Real-World Use Cases

- **Long-form reading products (docs, news) tuning 1.5–1.8 for comfort:** the relaxed token is the starting point; A/B the band, never leave it.
- **Vietnamese/cedilla-heavy locales verifying no clipped marks at any size:** the 1.5 floor plus the diacritic stress page (below) are the QA contract.
- **Design systems enforcing unitless leading and grid rhythm:** the tokens make px leading and off-grid margins lint failures.

## 7. Combination Notes

### With other typography skills

- **Pairs naturally with type-scale and font-pairing:** every scale step is really (size, weight, leading) and every family renders leading differently — the three are one review unit.
- **Pairs with readability-legibility and accessible-typography:** measure + leading + size form the reading triangle, and the 1.5 body floor is both a readability rule and a WCAG 1.4.12 requirement.
- **Pairs with multilingual-vietnamese and letter-spacing:** diacritic headroom and tracking both modify line boxes at the glyph level; they must be tuned together for marked scripts.
- **Caution/avoid list is empty:** no sibling conflicts with leading — conflicts only arise when leading is set outside the tokens.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism and flat-design:** both styles rely on generous, even whitespace — the 1.5/1.7 leading band and grid rhythm deliver the air these styles promise.
- **Caution with brutalism-ui and collage-art:** both may want cramped, overlapping, or claustrophobic leading as an expressive device; deviations must be documented style exceptions that never touch running body text, where the 1.5 floor is non-negotiable.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** entrance animations that animate line-height or margins (staggered list reveals) should interpolate between token values, not arbitrary numbers — the rhythm grid defines valid keyframe endpoints.
- **Caution/avoid list is empty:** motion disciplines do not conflict with leading directly, but animated line-height changes on text with diacritics must never dip below the 1.5 floor mid-animation.

## 8. Anti-Patterns

- **Px line-heights** — fixed leading that clips at zoom and breaks user font scaling
- **One leading everywhere** — 1.5 display type (loose, limp) or 1.2 body (cramped, exhausting)
- **Clipped diacritics** — 1.15 line-height on Vietnamese headings shearing ề and ậ marks
- **Margin chaos** — paragraph spacing invented per component instead of grid-snapped space tokens

### Accessibility Notes

Unitless leading is the WCAG 1.4.4/1.4.12 guarantee: text scales with user settings and layouts tolerate user spacing overrides — a px line-height defeats both by refusing to grow with font size. The 1.5 body floor serves dyslexic and low-vision readers, who need predictable line separation to track text without losing their place. The fallback rule: if tight display leading clips diacritics, raise that step's line-height — aesthetics yield to legibility every time, and the fix ships product-wide through the token rather than as a per-component patch.

## 9. Code Examples

### Example 1 — Leading comparison demo

Tokens: `assets/css/line-height.css`

```html
<div class="leading-demo">
  <h2 class="leading-demo-title">Leading by role</h2>
  <div class="leading-row leading-display">
    <span class="leading-label">display — 1.1</span>
    <p>Ship the interface, not the impedance.</p>
  </div>
  <div class="leading-row leading-heading">
    <span class="leading-label">heading — 1.2</span>
    <p>Quarterly platform reliability report</p>
  </div>
  <div class="leading-row leading-ui">
    <span class="leading-label">ui — 1.35</span>
    <p>Deploy to production environment</p>
  </div>
  <div class="leading-row leading-body">
    <span class="leading-label">body — 1.5</span>
    <p>Paragraph text sits at the 1.5 floor: tight enough to read as a block, loose enough that descenders and ascenders never collide.</p>
  </div>
  <div class="leading-row leading-relaxed">
    <span class="leading-label">relaxed — 1.7</span>
    <p>Long-form documentation runs looser still. Over a thousand words, the extra air measurably reduces re-reading and eye strain, and gives inline code and links room to breathe.</p>
  </div>
</div>
<style>
  .leading-demo { font-family: var(--type-font-text, system-ui, sans-serif); max-width: 640px; margin: 32px auto; padding: 24px; }
  .leading-demo-title { font-size: var(--type-size-xl); line-height: var(--type-line-height-heading); font-weight: 600; margin: 0 0 20px; }
  .leading-row { border-top: 1px solid #E5E7EB; padding: 12px 0; }
  .leading-label { display: block; font-size: var(--type-size-2xs); text-transform: uppercase; letter-spacing: 0.08em; color: #9CA3AF; margin-bottom: 4px; }
  .leading-display p { font-family: var(--type-font-display, inherit); font-size: var(--type-size-3xl); font-weight: 700; line-height: var(--type-line-height-display); margin: 0; }
  .leading-heading p { font-size: var(--type-size-lg); font-weight: 600; line-height: var(--type-line-height-heading); margin: 0; }
  .leading-ui p { font-size: var(--type-size-sm); font-weight: 600; line-height: var(--type-line-height-ui); margin: 0; }
  .leading-body p { font-size: var(--type-size-sm); line-height: var(--type-line-height-body); margin: 0; }
  .leading-relaxed p { font-size: var(--type-size-sm); line-height: var(--type-line-height-relaxed); margin: 0; }
</style>
```

### Example 2 — Vietnamese diacritic stress test (ề, ậ, ắ)

Tokens: `assets/css/line-height.css`

```html
<div class="vi-stress">
  <h2 class="vi-stress-title">Diacritic headroom — 1.5 floor</h2>
  <p class="vi-hero">Hệ thống thiết kế</p>
  <p class="vi-hero vi-tight" id="viTight">Hệ thống thiết kế</p>
  <p class="vi-body">Trăm năm trong cõi người ta — ability: ậ, ế: ề, ắ: ắ</p>
  <p class="vi-note" id="viNote"></p>
</div>
<script>
  // Guard: clipped marks are caught in QA, not by users
  const el = document.getElementById('viTight');
  const cs = getComputedStyle(el);
  const lh = parseFloat(cs.lineHeight) / parseFloat(cs.fontSize);
  document.getElementById('viNote').textContent =
    'Display line-height: ' + lh.toFixed(2) +
    (lh >= 1.5 ? ' — passes diacritic headroom' : ' — FAILS: stacked marks (ề, ậ) will clip');
</script>
<style>
  .vi-stress { font-family: var(--type-font-text, system-ui, sans-serif); max-width: 640px; margin: 32px auto; padding: 24px; }
  .vi-stress-title { font-size: var(--type-size-lg); font-weight: 600; line-height: var(--type-line-height-heading); margin: 0 0 20px; }
  .vi-hero {
    font-family: var(--type-font-display, inherit);
    font-size: var(--type-size-2xl);
    font-weight: 700;
    line-height: var(--type-line-height-heading); /* 1.2 — safe for diacritics at 2xl+ */
    margin: 0 0 8px;
  }
  .vi-tight { line-height: 1.1; color: #B91C1C; } /* deliberately tight: the anti-pattern demo */
  .vi-body {
    font-size: var(--type-size-sm);
    line-height: var(--type-line-height-body); /* 1.5 — the floor; stacked marks never clip */
    margin: 16px 0 0;
    max-width: var(--type-measure-default);
  }
  .vi-note { font-size: var(--type-size-xs); color: #6B7280; margin: 12px 0 0; }
</style>
```

## 10. Implementation Checklist

- [ ] All line-height values are unitless ratios pulled from `var(--type-line-height-*)` — zero px leading anywhere.
- [ ] Body paragraphs render at 1.5 or above (WCAG 1.4.12 floor); long-form surfaces use the relaxed 1.7 token.
- [ ] Display and heading steps ship with their bundled leading — no size change is merged without its line-height review.
- [ ] Vietnamese stress strings (ề, ậ, ắ) render unclipped at every scale step and weight, including display sizes.
- [ ] Paragraph spacing uses `var(--type-paragraph-gap)` from the 4px grid — no per-component margin guesses.
- [ ] Heading line-height boxes are rounded to 4px grid multiples where section alignment matters.
- [ ] CJK locales resolve the taller 1.8 variant via locale-aware tokens, not per-page overrides.
- [ ] Paragraphs are capped at `var(--type-measure-default)` (65ch) so leading and measure are tuned together.

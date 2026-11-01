---
name: typography-audit
description: Scale adherence, hierarchy in text, line-length and readability, and the named type crimes — checked mechanically against skill-typography's contracts.
tags: [typography, type-scale, audit, readability, line-height]
related: [review-process, visual-hierarchy-audit, content-microcopy-audit]
---

# Design Review Guide: Typography Audit

## 1. Definition

The typography audit verifies the text layer against skill-typography's contracts: scale adherence (are all sizes from the type ramp?), hierarchy legibility (do headings read as headings?), line length and line height (45–75ch measure, 1.4–1.6 body leading), and the classic type crimes — tracked-out lowercase, ALL CAPS long strings, widowed headings, and justified rivers. The pass is fast because the contracts are mechanical: computed styles are extracted and diffed against the ramp, the heading outline is checked for skips, and the crimes are a named checklist run top to bottom.

## 2. Core Principles

- **Sizes come from the scale:** any font-size outside the type ramp is a mechanical finding (skill-typography type-scale contract).
- **Heading hierarchy is real:** h1–h6 without skips, visual weight matching semantic weight — styled-div headings are findings.
- **Line length within 45–75ch:** paragraphs beyond the comfort band are flagged — including full-width text in wide layouts.
- **Line height matches the role:** 1.4–1.6 for body, tighter for headings — a single unitless line-height value across mixed sizes is a finding.
- **The type crimes list:** tracked-out lowercase (negative tracking), ALL CAPS long strings, justified text with rivers, widowed headings — each is a named, repeatable check.
- **Fluid type verified at breakpoints:** clamp() behavior checked at 320px and 1440px+ — overflow or invisible shrink is a finding.
- **Tabular figures where numbers align:** tables, timers, and metrics use `tabular-nums` (skill-typography numeric-tabular contract).
- **Font loading doesn't flash:** FOUT/FOIT on the audited surface is a performance-typography finding (webfont-loading contract).

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Contract | `--rev-scale-adherence` | `type-ramp-only` | Off-ramp sizes = mechanical finding |
| Contract | `--rev-heading-hierarchy` | `real-headings-no-skips` | Styled-div headings flagged |
| Threshold | `--rev-line-length` | `45-75ch` | Paragraph comfort band |
| Threshold | `--rev-line-height` | `body-1.4-1.6` | Role-matched leading |
| Check | `--rev-type-crimes` | `tracked-lower,caps-strings,widows,rivers` | Named checks |
| Check | `--rev-fluid-check` | `clamp-320-to-1440` | Breakpoint-verified |
| Contract | `--rev-tabular-figures` | `tables+metrics` | Aligned numbers contract |
| Check | `--rev-font-load-check` | `no-fout-foit` | Loading strategy verified |
| Threshold | `--rev-contrast-in-text` | `4.5:1` | Shared with a11y-audit |
| Score | `--rev-typography-score` | `per-surface` | Feeds report template |

Consume them by linking `assets/css/typography-audit.css` once at the review workspace root, then referencing `var(--rev-line-length)`, `var(--rev-type-crimes)`, and the rest from audit scripts and scorecards — thresholds never live inline in one-off lint scripts. If a size seems to need a value off the ramp, that request goes to the type-scale contract through review, not into the component's CSS.

## 4. Composition

- **Composes with skill-typography:** that repo owns the contracts (type-scale, line-height, numeric-tabular, webfont-loading); this audit scores surfaces' adherence to them.
- **Composes with visual-hierarchy-audit (guide 03):** the type scale is hierarchy's main tool — the two audits share the heading and emphasis evidence.
- **Composes with content-microcopy-audit (guide 09):** copy and its typography are reviewed in the same pass — line-length findings often trace back to copy length.

## 5. Signature Patterns

- **The scale sweep:** extract every computed font-size on the surface, diff against the type ramp — off-ramp values are listed mechanically, no judgment required.
- **The type-crimes checklist:** the named list (tracking, caps, widows, rivers, skips) run top to bottom — fast, reproducible, and identical between reviewers.

## 6. Real-World Use Cases

- **Content-heavy surfaces** (docs, marketing, articles) where readability contracts dominate.
- **Post-migration typography checks** — a new font family or new scale, verified across every template.
- **Audit triage:** off-scale sizes, heading skips, and river-y justified text, listed as mechanical findings.

## 7. Combination Notes

### With other design-review skills

- **Pairs with review-process and report-template:** mechanical findings still flow through the severity scale and land as tickets — "it's just typography" is how off-scale sizes survive for years.
- **Pairs with visual-hierarchy-audit and content-microcopy-audit:** the scale sweep and string walk share data — one extraction pass serves both audits.
- **Pairs with consistency-audit and spacing-rhythm-audit:** off-ramp sizes and broken leading are consistency drift; line-height and spacing interact on vertical rhythm, so the audits share the rhythm evidence.
- **Pairs with a11y-audit, interaction-states-audit, perceived-performance, responsive-audit, and motion-audit:** text contrast, resize behavior, font-loading performance, reflow at breakpoints, and animated type are crossover checks — findings cite the typography token and the partner guide.
- **No caution or avoid list:** every sibling audit consumes this pass's output without conflict.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, class-morphism, and retro:** minimalism lives or dies by the type ramp doing the visual work; class-morphism and retro lean on deliberate type treatment that still obeys scale and measure contracts.
- **Caution with brutalism-ui:** brutalist styles deliberately break the grid, including type conventions — the audit still enforces readability (contrast, measure, resize survival), so deviations must be documented exceptions, not defaults.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** any type that animates (counters, ticker text, reveal headings) uses duration and easing tokens, keeping text motion inside the ladder the motion audit enforces.
- **Caution on animated text generally:** moving or fading text must remain readable and announced — if type motion is decorative, the type audit flags it under readability while motion-audit flags it under purpose.

## 8. Anti-Patterns

- **Off-ramp sizes** — 17px and 23px body text from nowhere
- **Heading skips** — h2 to h5 jumps breaking the outline
- **Tracked-out lowercase** — negative letter-spacing squeezing body text
- **River-y justification** — full-justify with no hyphenation control

### Accessibility Notes

The audit covers WCAG 1.4.3 (text contrast, shared with a11y-audit via `--rev-contrast-in-text`), 1.4.4 (resize text), 1.4.12 (text spacing override tolerance), and 2.4.6 (headings and labels): text must survive user text-spacing overrides and 200% resize without clipping — checked by toggling the spacing overrides and re-running the layout checks. Heading hierarchy is the screen reader parallel of visual hierarchy, which is why styled-div headings are findings even when they look right: they break the outline AT users navigate by. The fallback rule when the full pass is too heavy: run the text-spacing override bookmarklet plus a 200% zoom pass — both are 5-minute checks with high yield, and they catch the failure modes (clipping, overlap) that static screenshots never show.

## 9. Code Examples

### Example 1 — Scale sweep: computed font-sizes diffed against the type ramp

Tokens: `assets/css/typography-audit.css`

```html
<article class="doc" id="sweep-root">
  <h1>Release notes</h1>
  <h2>Improved search</h2>
  <p>Search now handles typos and partial matches across all workspaces.</p>
  <p class="weird">This paragraph was styled with an off-ramp size for the demo.</p>
  <table class="sweep" id="sweep">
    <thead><tr><th>Element</th><th>Computed</th><th>Ramp</th><th>Verdict</th></tr></thead>
    <tbody></tbody>
  </table>
</article>
<style>
  :root { /* mirrors assets/css/typography-audit.css */
    --rev-scale-adherence: type-ramp-only; --type-ramp: 12px, 14px, 16px, 20px, 24px, 32px;
  }
  .doc { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 560px; }
  .doc h1 { font-size: 32px; margin: 0 0 8px; }
  .doc h2 { font-size: 20px; margin: 16px 0 8px; }
  .doc p { font-size: 16px; margin: 0 0 8px; }
  .weird { font-size: 17px; } /* deliberate off-ramp value */
  .sweep { border-collapse: collapse; width: 100%; font-size: 12px; margin-top: 12px; }
  .sweep th, .sweep td { border: 1px solid #D4D4D4; padding: 4px 8px; text-align: left; }
</style>
<script>
  // Scale sweep: extract computed sizes, diff against the ramp, list off-ramp findings.
  const ramp = [12, 14, 16, 20, 24, 32]; // mirrors --type-ramp
  const tbody = document.querySelector('#sweep tbody');
  document.querySelectorAll('#sweep-root h1, #sweep-root h2, #sweep-root p').forEach((el) => {
    const px = parseFloat(getComputedStyle(el).fontSize);
    const on = ramp.includes(px);
    const row = tbody.insertRow();
    row.innerHTML = `<td>${el.tagName.toLowerCase()}${el.className ? '.' + el.className : ''}</td><td>${px}px</td><td>${on ? px + 'px' : '—'}</td><td>${on ? 'PASS' : 'FAIL: off-ramp'}</td>`;
  });
</script>
```

### Example 2 — Type-crimes checklist runner

Tokens: `assets/css/typography-audit.css`

```html
<div class="crimes" id="crimes-root">
  <h2>Q3 <span class="skip-demo">Results</span></h2>
  <p class="tracked">Tight body copy with negative tracking applied.</p>
  <p class="caps">THIS ENTIRE PARAGRAPH IS SET IN ALL CAPS WHICH IS HARD TO READ.</p>
  <p class="justified">Justified text without hyphenation control can open uneven rivers of white space between words across full lines.</p>
  <ol class="crime-report" id="crime-report"></ol>
</div>
<style>
  :root { /* mirrors assets/css/typography-audit.css */
    --rev-type-crimes: tracked-lower,caps-strings,widows,rivers;
  }
  .crimes { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 480px; }
  .crimes h2 { font-size: 20px; margin: 0 0 8px; }
  .tracked { letter-spacing: -0.06em; }             /* crime: tracked-out lowercase */
  .caps { text-transform: uppercase; }              /* crime: long caps string */
  .justified { text-align: justify; hyphens: none; } /* crime: rivers risk */
  .crime-report { font-size: 12px; padding-left: 20px; }
  .crime-report li { margin-bottom: 2px; }
  .crime-report .fail { color: #B91C1C; font-weight: 600; }
</style>
<script>
  // Named checks from --rev-type-crimes, run top to bottom.
  const findings = [];
  document.querySelectorAll('#crimes-root p, #crimes-root h2').forEach((el) => {
    const cs = getComputedStyle(el);
    if (parseFloat(cs.letterSpacing) < 0 && cs.textTransform !== 'uppercase')
      findings.push(`FAIL tracked-lowercase: <${el.tagName.toLowerCase()}> letter-spacing ${cs.letterSpacing}`);
    const text = el.textContent;
    if (cs.textTransform === 'uppercase' && text.length > 40)
      findings.push(`FAIL caps-string: <${el.tagName.toLowerCase()}> ${text.length} chars in caps`);
    if (cs.textAlign === 'justify' && cs.hyphens === 'none')
      findings.push(`FAIL rivers: justified <${el.tagName.toLowerCase()}> without hyphenation`);
  });
  // Heading-skip check: heading levels must not jump.
  const levels = [...document.querySelectorAll('#crimes-root h1, #crimes-root h2, #crimes-root h3')]
    .map((h) => +h.tagName[1]);
  levels.forEach((lvl, i) => {
    if (i > 0 && lvl - levels[i - 1] > 1) findings.push(`FAIL heading-skip: h${levels[i - 1]} to h${lvl}`);
  });
  const list = document.getElementById('crime-report');
  list.innerHTML = (findings.length ? findings : ['PASS: no type crimes detected']).map((f) => `<li class="${f.startsWith('FAIL') ? 'fail' : 'pass'}">${f}</li>`).join('');
</script>
```

## 10. Implementation Checklist

- [ ] The scale sweep is run and every computed font-size sits on the type ramp — zero off-ramp sizes per `--rev-scale-adherence`.
- [ ] The heading outline has no level skips, and no styled divs are serving as headings.
- [ ] All paragraph measures fall within `--rev-line-length` (45–75ch), including full-width text in wide layouts.
- [ ] Line heights match roles: 1.4–1.6 body, tighter headings — no single value across mixed sizes.
- [ ] The type-crimes checklist is clean: no tracked-out lowercase, long caps strings, widowed headings, or uncontrolled justification.
- [ ] Fluid clamp() type is verified at 320px and 1440px+ with no overflow or invisible shrink.
- [ ] Tables, timers, and metrics use tabular figures per `--rev-tabular-figures`.
- [ ] Text contrast passes 4.5:1, and text survives 200% resize and spacing overrides without clipping.

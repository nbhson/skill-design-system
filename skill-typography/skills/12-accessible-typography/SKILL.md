---
name: accessible-typography
description: The a11y floors for text: contrast, zoom, spacing overrides, dyslexia-friendly defaults, and semantic structure that AT can navigate.
tags: [typography, accessibility, wcag, contrast, inclusive-design]
related: [type-scale, line-height, readability-legibility, font-pairing, fluid-responsive, numeric-tabular]
---

# Typography Skill: Accessible Typography

## 1. Definition

Accessible typography is the set of floors every text surface must clear: 4.5:1 contrast (7:1 for long-form), rem-based sizes that honor 200% zoom, respect for user text-spacing overrides (WCAG 1.4.12), real heading structure for screen reader navigation, and letterform choices that reduce reading errors for dyslexic users. Text is the majority of most interfaces — typography is therefore the majority of accessibility.

## 2. Core Principles

- **Contrast floors are absolute:** 4.5:1 body, 7:1 long-form targets — no aesthetic override (pairs with a11y repo color-contrast).
- **Sizes in rem, zoom-proof:** all type tokens are rem; 200% zoom must leave every control functional (1.4.4).
- **Respect user spacing overrides:** layouts must survive users setting line-height 1.5x, letter-spacing 0.12em, word-spacing 0.16em (1.4.12).
- **Real headings, real structure:** h1-h6 outline matches the visual hierarchy; screen readers navigate by headings — divs styled as headings are a bug.
- **Links distinguish themselves:** underline + color (or ≥2 signals) — color alone fails 1.4.1 and users with color vision deficiency.
- **Dyslexia-friendly defaults:** generous leading (1.5+), left alignment, longer line spacing between paragraphs, uncluttered backgrounds.
- **No text in images of text:** real text scales, translates, and reflows (1.4.5) — images-of-text only for logos/essential.
- **Reading overrides beat brand aesthetics:** if 1.4.12 overrides break the layout, the layout is too rigid — fix the layout.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Contrast | `--type-a11y-contrast-body` | `4.5:1` | WCAG 1.4.3 floor, always |
| Contrast | `--type-a11y-contrast-longform` | `7:1` | AAA reading surfaces |
| Size unit | `--type-a11y-size-unit` | `rem-only` | Type tokens never px (1.4.4) |
| Zoom | `--type-a11y-zoom-tested` | `200%` | All flows pass at 200% text zoom |
| Spacing | `--type-a11y-spacing-override` | `1.5-1.7-0.12-0.16` | WCAG 1.4.12: layout survives these overrides |
| Headings | `--type-a11y-heading-map` | `h1-h6-semantic` | Outline = visual hierarchy; lint-checked |
| Link signal | `--type-a11y-link-signal` | `underline-plus-color` | Minimum two distinguishing signals |
| Line height | `--type-a11y-line-height-floor` | `1.5` | Paragraph leading floor |
| Alignment | `--type-a11y-alignment` | `left-ragged` | Justified text off by default (1.4.8) |
| Font policy | `--type-a11y-font-family-policy` | `user-overridable` | Respect user stylesheet font swaps |

Consume them by linking `assets/css/accessible-typography.css` once at the app root, then referencing `var(--type-a11y-line-height-floor)`, `var(--type-a11y-contrast-body)`, and `var(--type-a11y-link-signal)` from text roles and component styles — product code never bypasses an a11y floor token. If a design decision conflicts with a floor token, the floor wins and the design adjusts.

## 4. Composition

- **Composes with skill-accessibility:** color-contrast, zoom-reflow, and cognitive-content are the specialized guides behind these floors — this guide states the typography-specific contracts.
- **Composes with skill-design-tokens guide 02:** type tokens carry the rem/contrast guarantees; this guide states the a11y rationale behind those guarantees.
- **Composes with readability-legibility:** readability floors and a11y floors are the same numbers viewed from two sides — 1.5 leading is both a readability optimum and a WCAG floor.

## 5. Signature Patterns

- **Override-stress test:** apply the 1.4.12 spacing overrides in devtools; any broken layout becomes a bug with the screenshot attached — not a "won't fix, users never do that" debate.
- **Heading lint:** CI checks one h1, ordered h-levels, and no styled-div headings per page — the heading map is machine-checkable, not a manual review note.

## 6. Real-World Use Cases

- **Any text-heavy product claiming WCAG AA** — the floors here are the typography-specific criteria the audit will test.
- **Dyslexia-inclusive products** (education, reading, government) — leading, alignment, and background clutter rules are the primary levers.
- **Audit: contrast, zoom, spacing-override, and heading-structure passes** — the four checks this guide's tokens map to.

## 7. Combination Notes

### With other typography skills

- **Good with type-scale, line-height, and readability-legibility:** the scale's sizes are rem-based by this contract; leading floors (1.5) are shared with the readability guide; the two skills enforce the same numbers from the design and a11y sides.
- **Good with font-pairing, letter-spacing, and fluid-responsive:** the pairing's fallback chain respects user font swaps; tracking tokens never override user letter-spacing; fluid type stays rem-based so zoom scaling holds.
- **Good with visual-hierarchy, multilingual-vietnamese, numeric-tabular, variable-fonts, and webfont-loading:** hierarchy ranks with weight/size (never color-only de-ranking); Vietnamese diacritics need the same zoom-proof sizes; tabular figures and variable named instances support a11y predictability.
- **Caution is unnecessary — the avoid list is empty:** accessible typography is a constraint layer on every other skill, not a conflicting skill. Every other typography guide's tokens already respect these floors.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** these styles' clean surfaces, generous whitespace, and restrained palettes naturally clear the contrast, leading, and clutter floors.
- **Caution with collage-art and brutalism-ui:** both may deliberately use low-contrast text, tight leading, or raw texture behind text as a style gesture — if so, apply the floors to body/reading text first and document the display-only exceptions consciously; never let style override a reading surface.

### With motion skills (companion repo skill-animation)

- **Good affinity with reduced-motion and easing-timing:** the reduced-motion skill's pause/swap contract pairs with typography's no-weight-animation rule; easing tokens govern any text-reveal so motion never obscures reading.
- **Caution beyond that:** any animation that obscures text (blurs, heavy overlays) during the animation window effectively drops contrast below floor — keep text fully legible at the animation's resting state.

## 8. Anti-Patterns

- **Outline:none on text** — removing focus indication from links and inputs
- **Gray-on-white hierarchy** — de-ranking text below 4.5:1 instead of using weight/size
- **Div headings** — styled divs where screen readers need h1-h6
- **Rigid layouts** — designs that shatter when users apply legal spacing overrides

### Accessibility Notes

This guide IS the accessibility layer of typography: every floor cited (1.4.3, 1.4.4, 1.4.5, 1.4.8, 1.4.12) is a conformance criterion, and heading structure is the screen reader's primary navigation. The fallback rule: when brand type choices conflict with floors, floors win — the brand adjusts (darker shade, larger size), never the criterion. Every token in section 3 is either a floor (contrast, leading, zoom) or a policy (rem-only, user-overridable) that exists to keep a WCAG criterion satisfied without per-component negotiation.

## 9. Code Examples

### Example 1 — WCAG-passing text page with heading map and zoom-safe sizes

Tokens: `assets/css/accessible-typography.css`

```html
<article class="readable-page">
  <h1>Reading comfort on the web</h1>
  <p class="lede">Body text at 1.125rem, 1.5 leading, left-aligned.</p>
  <h2>Contrast floors</h2>
  <p>Body text on white clears 4.5:1 — <a href="#floors">links underline</a>.</p>
  <h3>Long-form targets</h3>
  <p>Long-form reading surfaces target 7:1 (AAA) for extended sessions.</p>
</article>
<style>
  /* All sizes in rem — zoom-proof (1.4.4). No px type sizes. */
  .readable-page {
    max-width: 65ch;
    margin: 0 auto;
    padding: 48px 24px;
    font: 1.125rem/1.5 Inter, system-ui, sans-serif;
    color: #171717; /* 16.9:1 on white — clears --type-a11y-contrast-longform */
    text-align: left; /* --type-a11y-alignment: left-ragged, never justified */
  }
  .readable-page h1 { font-size: 2.25rem; line-height: 1.2; margin: 0 0 16px; }
  .readable-page h2 { font-size: 1.5rem;  line-height: 1.3; margin: 32px 0 12px; }
  .readable-page h3 { font-size: 1.25rem; line-height: 1.3; margin: 24px 0 8px; }
  .readable-page p  { line-height: var(--type-a11y-line-height-floor); margin: 0 0 16px; }
  .readable-page .lede { font-size: 1.25rem; color: #404040; } /* 10.3:1 */
  /* Link: underline + color — two signals (1.4.1) */
  .readable-page a { color: #1D4ED8; text-decoration: underline; text-underline-offset: 3px; }
  .readable-page a:hover { color: #1E40AF; }
  .readable-page a:focus-visible { outline: 2px solid #1D4ED8; outline-offset: 2px; }
</style>
```

### Example 2 — WCAG 1.4.12 spacing-override stress test

```html
<div class="card-grid">
  <div class="card">
    <h3 class="card-title">Card title</h3>
    <p class="card-body">Body text that must survive user spacing overrides.</p>
    <a class="card-link" href="#detail">Read more</a>
  </div>
</div>
<script>
  // WCAG 1.4.12 stress test: apply the legal user overrides, check nothing
  // clips or overflows, then restore. Any broken element is a layout bug.
  const OVERRIDES = { lineHeight: "1.5", letterSpacing: "0.12em", wordSpacing: "0.16em" };

  function stressTest(scope = document.body) {
    const touched = [...scope.querySelectorAll("*")].map((el) => [el, el.style.cssText]);
    touched.forEach(([el]) => Object.assign(el.style, OVERRIDES));

    // Horizontal overflow after overrides is a 1.4.12 failure
    const broken = touched
      .filter(([el]) => el.scrollWidth > el.clientWidth + 1
        && getComputedStyle(el).overflow !== "auto")
      .map(([el]) => el);
    touched.forEach(([el, css]) => { el.style.cssText = css; });

    if (broken.length) console.error("1.4.12 stress test failed — layout too rigid:", broken);
    else console.log("1.4.12 stress test passed — layout survives user overrides.");
    return broken;
  }

  stressTest();
</script>
<style>
  .card-grid {
    display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 24px; padding: 24px; font-family: Inter, system-ui, sans-serif;
  }
  .card {
    background: #FAFAFA; border: 1px solid #E5E5E5; border-radius: 12px; padding: 20px;
    /* No fixed heights — content grows with overrides instead of clipping */
  }
  .card-title { font-size: 1.125rem; font-weight: 600; line-height: 1.4; margin: 0 0 8px; color: #171717; }
  .card-body {
    font-size: 1rem; margin: 0 0 12px;
    line-height: var(--type-a11y-line-height-floor); /* 1.5 floor */
    color: #404040; /* 10.3:1 — clears the 4.5:1 body floor */
  }
  .card-link { color: #1D4ED8; text-decoration: underline; text-underline-offset: 3px; } /* 2 signals */
  .card-link:focus-visible { outline: 2px solid #1D4ED8; outline-offset: 2px; } /* never outline: none */
</style>
```

## 10. Implementation Checklist

- [ ] All type tokens are rem-based (`--type-a11y-size-unit: rem-only`) — zero px font sizes in product code; 200% zoom leaves every control functional (1.4.4).
- [ ] Every text/background pairing clears `--type-a11y-contrast-body` (4.5:1); long-form reading surfaces clear `--type-a11y-contrast-longform` (7:1).
- [ ] Paragraph leading is at or above `--type-a11y-line-height-floor` (1.5); body text alignment is left-ragged, never justified (1.4.8).
- [ ] Layouts survive the `--type-a11y-spacing-override` stress test (1.5 line-height, 0.12em letter-spacing, 0.16em word-spacing) with no content loss or overlap (1.4.12).
- [ ] Heading map is semantic and lint-checked: exactly one h1, ordered h-levels, zero styled-div headings.
- [ ] All links carry `--type-a11y-link-signal` (underline + color); no `outline: none` on any focusable text element.
- [ ] No images-of-text render outside logo/essential exceptions (1.4.5); real text handles scale, translate, and reflow.
- [ ] Font-family policy is `user-overridable` — user stylesheet font swaps are respected, not blocked.
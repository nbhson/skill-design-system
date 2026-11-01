---
name: color-contrast
description: WCAG 1.4.3/1.4.11 as designed-in properties — ratio thresholds, safe pairings, and contrast that survives dark mode and brands.
tags: [contrast, wcag, color, pairings, focus-ring]
related: [wcag-fundamentals, keyboard-navigation, focus-management]
---

# Accessibility Skill: Color & Contrast

## 1. Definition

Color contrast is the most-measured accessibility property: text must reach 4.5:1 against its background (3:1 for large text), and non-text UI (icons, input borders, control boundaries, focus rings) must reach 3:1 against adjacent colors. This skill covers how to design palettes that pass by construction — validated alias pairings from skill-design-tokens — rather than fixing contrast after build with darker-and-darker text. The unit of decision is the pairing, not the color: a gray that fails as body text may pass perfectly as an icon, and a blue that fails on white may pass on the very surface it is meant to sit on.

## 2. Core Principles

- **Know the numbers:** 4.5:1 body text, 3:1 large text (24px/19px bold), 3:1 UI components and graphical objects (WCAG 1.4.3, 1.4.11).
- **Contrast belongs to pairings, not colors:** only text-on-background has a ratio — design pairs, then lock them as alias contracts.
- **Focus indicators are first-class:** the ring must reach 3:1 against both sides of the boundary it crosses (WCAG 2.4.13).
- **Hover/pressed deltas must be visible:** a state change nobody can perceive (or that only color-blind users cannot) is a failure.
- **Never signal with color alone:** pair color with text, icons, or position (WCAG 1.4.1 Use of Color).
- **Disabled states are exempt but documented:** record their ratios so nobody 'fixes' them into confusion later.
- **Validated in both themes and every brand:** a pairing without dark-mode and per-brand ratios is unfinished.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Threshold | `--a11y-contrast-body-min` | `4.5:1` | WCAG 1.4.3 AA body text |
| Threshold | `--a11y-contrast-large-min` | `3:1` | 24px regular / 18.66px bold text |
| Threshold | `--a11y-contrast-ui-min` | `3:1` | WCAG 1.4.11 icons, borders, control boundaries |
| Threshold | `--a11y-contrast-aaa-body` | `7:1` | AAA for long-form reading surfaces |
| Threshold | `--a11y-contrast-focus-min` | `3:1` | WCAG 2.4.13 focus ring vs adjacent colors |
| Focus ring | `--a11y-focus-ring-color` | `#1D4ED8` | 6.3:1 on white, 4.6:1 on neutral-100 - safe default |
| Focus ring | `--a11y-focus-ring-width` | `2px` | WCAG 2.4.13 wants visible thickness; 2px minimum |
| Focus ring | `--a11y-focus-ring-offset` | `2px` | Separation from the component edge; visible against both surfaces |
| State delta | `--a11y-state-delta-min` | `1.5:1` | Hover/pressed shift perceivable to low vision |
| Signal policy | `--a11y-non-color-signal` | `icon-or-text-paired` | WCAG 1.4.1: never color alone for errors/required/status |

Load `assets/css/color-contrast.css` once at the app root so thresholds and the default focus ring exist as custom properties, then consume them via `var(--a11y-<role>)` in component CSS — hover deltas check their shift against `var(--a11y-state-delta-min)`, and every ring uses the shared `--a11y-focus-ring-*` triplet instead of per-component outline styles that drift out of validation.

## 4. Composition

- **Composes with skill-design-tokens:** thresholds live as token properties (contrast-validation guide); this skill covers the design practice around them — the manifest, the review, the remediation habits.
- **Composes with dark-mode theming:** every pairing re-validates per theme cell; the manifest makes N x M validation automatic instead of a per-release surprise.
- **Composes with data-viz work (skill-color-theory guide 10):** chart series need 3:1 against adjacent surfaces plus non-color differentiation — contrast rules apply to data just as hard as to chrome.

## 5. Signature Patterns

- **Pairing manifest first:** write text/bg, icon/surface, and focus/surface pairs with computed ratios before styling anything — styling then becomes filling in pre-validated slots, not discovering failures in review.
- **Contrast-first palette build:** pick alias pairs that pass, let the palette be whatever values satisfy the manifest — the inverse of picking pretty colors and hoping they pass.

## 6. Real-World Use Cases

- **Designing new palettes or themes that pass WCAG AA by construction:** the manifest is written before the first hex ships.
- **Remediating audit findings at the token level so fixes propagate everywhere:** one alias fix, every component healed.
- **Reviewing charts, dashboards, and data-dense UI where non-text contrast is routinely ignored:** borders, gridlines, and series colors are 1.4.11 subjects too.

## 7. Combination Notes

### With other accessibility skills

- **Good with wcag-fundamentals, keyboard-navigation, focus-management, aria-fundamentals, forms-errors, screen-readers, zoom-reflow, testing-audit, cognitive-content, media-alt-text, aria-patterns-widgets:** contrast intersects nearly every criterion — focus rings pair with focus-management, error colors with forms-errors, chart differentiation with media-alt-text — and 1.4.1 (never color alone) makes color a signal enhancer for all of them, never the sole carrier.
- **No caution or avoid list:** nothing in accessibility argues for lower contrast; the conflicts are with styles, not siblings.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and glassmorphism:** flat palettes and disciplined surfaces make pairings easy to enumerate and validate; glassmorphism works only when tint overlays are treated as the real background color in every ratio computation.
- **Caution with brutalism-ui and collage-art:** raw type over arbitrary imagery and clashing collage swatches fight 4.5:1 by intent; any deviation must ship as a documented alias override with computed ratios, not an unchecked flourish.

### With motion skills (companion repo skill-animation)

- **Good affinity with reduced-motion:** reduced-motion is the animation-side sibling — color-only state changes must survive with animation removed, which is exactly why hover deltas and non-color signals are designed as static properties here.
- **No caution list:** animated color transitions are fine as long as the resting pairing passes; the resting state is what this skill validates.

## 8. Anti-Patterns

- **Eyeball contrast** — judging ratios by looking at the screen - human vision adapts and lies; compute the number
- **Darker-and-darker text** — fixing every failure by forcing text to black until hierarchy disappears
- **Light-theme-only audits** — shipping dark themes and brand cells whose pairings were never computed
- **Color-only signaling** — red error borders without text or icons - invisible to color-blind users

### Accessibility Notes

This guide IS a WCAG enforcement skill: 1.4.3, 1.4.11, 1.4.1, and 2.4.13 are its daily subject matter, and every ratio is computed with the WCAG relative-luminance formula — never estimated. Beyond text, the skill's special watch is the boundaries nobody measures: input borders, icon strokes, chart series against neighbors, and the focus ring, which must hold 3:1 on both surfaces it straddles. The fallback rule when a pairing fails: change the background alias, the text alias, or (last resort) add a validated primitive step through skill-design-tokens governance — never by shipping below threshold and hoping nobody checks.

## 9. Code Examples

### Example 1 — Validated text pairing with a relative-luminance ratio checker

Tokens: `assets/css/color-contrast.css`

```html
<article class="note">
  <h2>Account updated</h2>
  <p>Your billing address now applies to invoices issued from today onward.</p>
</article>
<script>
  // WCAG relative-luminance ratio checker — validates the pairing at runtime
  function lum(hex) {
    const c = hex.match(/\w\w/g).map(v => {
      const s = parseInt(v, 16) / 255;
      return s <= 0.03928 ? s / 12.92 : Math.pow((s + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
  }
  function ratio(fg, bg) {
    const [a, b] = [lum(fg), lum(bg)].sort((x, y) => y - x);
    return (a + 0.05) / (b + 0.05);
  }
  const css = getComputedStyle(document.documentElement);
  const bodyMin = parseFloat(css.getPropertyValue('--a11y-contrast-body-min')); // 4.5
  const r = ratio('#171717', '#FFFFFF'); // heading on card background
  console.assert(r >= bodyMin, `pairing fails ${bodyMin}:1 (actual ${r.toFixed(2)}:1)`);
</script>
<style>
  .note {
    background: #FFFFFF;
    color: #404040; /* body text pairing validated against --a11y-contrast-body-min */
    border: 1px solid #D4D4D4; /* non-text boundary meets --a11y-contrast-ui-min */
    border-left: 4px solid #22C55E;
    border-radius: 8px;
    padding: 16px;
    max-width: 420px;
    font: 14px/1.5 Inter, system-ui, sans-serif;
  }
  .note h2 {
    margin: 0 0 8px;
    font-size: 16px;
    color: #171717; /* heading pairing: computed ratio asserted in JS */
  }
  .note p { margin: 0; }
</style>
```

### Example 2 — Button with focus ring, hover delta, and non-color state signal

Tokens: `assets/css/color-contrast.css`

```html
<button class="save" id="save-btn">
  <svg aria-hidden="true" width="14" height="14" viewBox="0 0 16 16"><path d="M3 8l4 4 6-8" fill="none" stroke="currentColor" stroke-width="2"/></svg>
  Save changes
</button>
<script>
  const btn = document.getElementById('save-btn');
  btn.addEventListener('click', () => {
    // WCAG 1.4.1: state change pairs color with an icon, never color alone
    btn.dataset.state = 'saved';
    btn.setAttribute('aria-disabled', 'true');
  });
</script>
<style>
  .save {
    display: inline-flex; align-items: center; gap: 8px;
    background: #2563EB; color: #FFFFFF; /* validated: 4.6:1 */
    border: none; border-radius: 8px; padding: 10px 20px;
    font: 600 14px/1 Inter, system-ui, sans-serif; cursor: pointer;
  }
  .save:hover { background: #1D4ED8; } /* delta vs --a11y-state-delta-min; icon count = non-color signal */
  .save[aria-disabled="true"] { opacity: 0.6; cursor: default; } /* exempt, ratio documented */
  .save:focus-visible {
    outline: var(--a11y-focus-ring-width) solid var(--a11y-focus-ring-color);
    outline-offset: var(--a11y-focus-ring-offset); /* ring holds 3:1 on both surfaces (2.4.13) */
  }
</style>
```

## 10. Implementation Checklist

- [ ] A pairing manifest exists listing text/bg, icon/surface, and focus/surface pairs with computed ratios before styling.
- [ ] All body text pairings meet the `var(--a11y-contrast-body-min)` threshold of 4.5:1 in every theme and brand cell.
- [ ] Icons, input borders, and control boundaries meet `var(--a11y-contrast-ui-min)` at 3:1 against adjacent colors.
- [ ] The focus ring uses the shared `--a11y-focus-ring-color/width/offset` triplet and holds 3:1 on both sides of its boundary.
- [ ] Hover/pressed states shift by at least `var(--a11y-state-delta-min)` and never rely on color alone (WCAG 1.4.1).
- [ ] Disabled pairings have documented, exempt ratios so they are not silently 'corrected'.
- [ ] Dark-mode and per-brand cells are computed — a pairing without both is treated as unfinished.
- [ ] Failing pairings are fixed at the alias level (or via a validated primitive step), never by shipping below threshold.

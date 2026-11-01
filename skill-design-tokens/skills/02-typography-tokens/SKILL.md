---
name: typography-tokens
description: Font families, a modular type scale, weights, and line-height tokens that make text hierarchy systematic instead of per-screen improvisation.
tags: [typography, tokens, type-scale, fonts, design-systems]
related: [color-tokens, spacing-sizing, semantic-alias-naming]
---

# Design Token Skill: Typography Token System

## 1. Definition

Typography tokens encode every text decision the product is allowed to make: which families load, which sizes exist, which weights pair with them, and how tall each line runs. A modular scale (root 16px, ratio ~1.25) plus a closed weight set means hierarchy comes from stepping along the scale, not from inventing 17px here and 22px there. Because text is the majority of most interfaces, typography tokens are usually the highest-traffic token layer in the whole system.

## 2. Core Token Principles

- **One modular scale, root 16px, ratio 1.2–1.25:** it covers body through display in ~9 steps without off-scale sizes creeping in.
- **Close the weight set:** 400/500/600/700 covers 95% of UI; loading 9 weights is a performance tax paid on every page.
- **Line-height is inversely proportional to size:** tight (1.1–1.2) for display, relaxed (1.5–1.7) for body.
- **Two families maximum:** one text face, one optional display or mono face; every extra family costs loading, consistency, and review time.
- **Letter-spacing tightens as size grows:** display faces need -0.02em to -0.04em, body stays 0, uppercase labels earn +0.04em.
- **Sizes are rem, never px:** user font-size preferences must scale the whole hierarchy (WCAG 1.4.4 resize).
- **Token names describe role, not appearance:** `text-body`, `text-heading`, `text-caption` — so a font swap never breaks the vocabulary.

## 3. Token Set

| Role | Token | Value | Notes |
|---|---|---|---|
| Family | `--dt-font-family-sans` | `Inter, system-ui, -apple-system, sans-serif` | The default text face; system fallbacks keep first paint unstyled-fast |
| Family | `--dt-font-family-mono` | `ui-monospace, SFMono-Regular, Menlo, monospace` | Code, numeric alignment, token names |
| Size | `--dt-font-size-2xs` | `0.75rem` | 12px - legal, timestamps; never for primary reading |
| Size | `--dt-font-size-xs` | `0.875rem` | 14px - secondary text, table cells, captions |
| Size | `--dt-font-size-sm` | `1rem` | 16px - body default; the root step of the scale |
| Size | `--dt-font-size-md` | `1.125rem` | 18px - lead paragraphs, emphasized body |
| Size | `--dt-font-size-lg` | `1.25rem` | 20px - h4/card titles |
| Size | `--dt-font-size-xl` | `1.5rem` | 24px - h3, section headers |
| Size | `--dt-font-size-2xl` | `1.875rem` | 30px - h2, page titles |
| Weight | `--dt-font-weight-semibold` | `600` | Headings and interactive emphasis; pairs with -0.01em tracking at lg+ |
| Line height | `--dt-line-height-body` | `1.5` | Default for text at sm/md; relaxed 1.7 for long-form reading |

Consume them by linking `assets/css/typography-tokens.css` once at the app root, then referencing `var(--dt-font-...)` / `var(--dt-line-height-...)` in every component and role class. If a size not in this table seems necessary, the scale is wrong; step along it or add a step through review, never a 17px one-off.

## 4. Composition & Layering

- **Typography tokens compose with spacing tokens.** Paragraph rhythm uses space tokens, never margin guesses, so text blocks snap to the same grid as components.
- **Font-size steps pair with fixed line-height tokens.** The pair (size, line-height) is reviewed together, never independently — a step's vertical box is part of its definition.
- **Dark mode re-points color aliases only.** Type tokens are theme-invariant, which is what keeps text metrics stable across themes and prevents layout shift on theme switches.

## 5. Signature Patterns

- **Role-based text classes:** `.text-body` / `.text-heading` / `.text-caption` bundle size + weight + line-height + letter-spacing so consumers pick one class, not four values.
- **Fluid display:** heading steps interpolate with `clamp()` between two scale stops so titles scale with the viewport without extra breakpoints.

## 6. Real-World Use Cases

- **Design systems standardizing a type ramp** across web products.
- **Vietnamese and other diacritic-heavy locales:** verifying line-height and fallback stacks render stacked marks without clipping.
- **Performance budgets:** auditing weight loading and font-display strategy against the closed token set.

## 7. Combination Notes

### With other token skills

- **Pairs well with color-tokens and spacing-sizing:** type supplies the hierarchy, color the legibility, and spacing the rhythm — together they form the vertical grid every layout is built on (line-height boxes + space tokens).
- **Pairs with semantic-alias-naming, dark-mode, and contrast-validation:** text color flows through aliases while type tokens stay theme-invariant, and every size/weight pairing is contrast-checked at its documented surface.
- **Caution with radius-elevation:** both define independent systems, so compose only at the component tier (e.g. card title uses text-lg inside radius-lg surfaces) rather than letting one influence the other's scale.
- **Caution with multi-brand-theming:** brands may swap the font family but inherit the same size/line-height steps; a brand that wants its own ramp is asking for a fork that fragments the vocabulary.
- **Caution with platform-mapping:** rem values must map to pt/dp with font scaling enabled (Dynamic Type, fontScale) — a value-only mapping silently breaks user text scaling on mobile.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism, flat-design, and class-morphism:** these styles reward a restrained ramp and closed weight set where hierarchy comes from size and weight, not decoration.
- **Caution with collage-art and maximalism:** both push expressive, mixed, or oversized type that fights a 9-step scale; if so, deviate consciously via a display face and documented role overrides — never by sprinkling off-scale sizes.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** type changes that animate (size/weight transitions, number tickers) should run on duration tokens so text motion matches every other transition in the product.
- **Caution with ambient-motion:** continuously animating text (scrollers, glowing titles) undermines reading and the stable metrics these tokens guarantee; keep text as the still center and let motion live around it.

## 8. Anti-Patterns

- **Off-scale sizes:** 17px or 22px one-offs erode the scale until every screen invents its own hierarchy
- **Open weight loading:** shipping 400-900 in one family file multiplies payload for weights nobody uses
- **Px font sizes:** locking text to pixels breaks user font-size preferences and WCAG 1.4.4 resize
- **Appearance-named tokens:** text-small-bold-uppercase encodes today's look and dies at the first redesign

### Accessibility Notes

Type tokens carry two WCAG duties. First, real text must respect 200% zoom: all size tokens are rem-based so the whole hierarchy multiplies with the user's browser setting (WCAG 1.4.4), and the `--dt-font-family-sans` fallback stack keeps first paint unstyled-fast for assistive-tech-heavy sessions. Second, line-height tokens must keep diacritics unclipped at every step — Vietnamese stacked marks are the canonical test case, and any step that shaves its line-height too tight fails on them first. The fallback is directional and non-negotiable: if a step's tight line-height clips diacritics or wraps badly at 200% zoom, raise that step's line-height token — never shrink the text to fit the box.

## 9. Code Examples

### Example 1 — Article page: role classes over the ramp

Tokens: `assets/css/typography-tokens.css`

```html
<article class="post">
  <h1 class="text-page-title">Design tokens, explained</h1>
  <p class="text-meta">Updated May 2026 · 6 min read</p>
  <p class="text-lead">
    A modular scale turns typography from per-screen improvisation into a
    closed set of decisions the whole product shares.
  </p>
  <p class="text-body">Hierarchy comes from stepping along the scale —
    never from inventing a new size mid-screen.</p>
</article>
<style>
  body { margin: 0; padding: 32px; background: #fff; }
  .post { max-width: 560px; font-family: var(--dt-font-family-sans); }

  .text-page-title {
    font-size: var(--dt-font-size-2xl);        /* 1.875rem */
    font-weight: var(--dt-font-weight-semibold);
    line-height: 1.2;                          /* tight for display */
    letter-spacing: -0.02em;                   /* tracking tightens with size */
    margin: 0 0 8px;
  }
  .text-meta {
    font-size: var(--dt-font-size-xs);         /* 0.875rem */
    color: #737373;
    line-height: 1.5;
    margin: 0 0 16px;
  }
  .text-lead {
    font-size: var(--dt-font-size-md);         /* 1.125rem */
    line-height: var(--dt-line-height-body);
    color: #404040;
    margin: 0 0 12px;
  }
  .text-body {
    font-size: var(--dt-font-size-sm);         /* 1rem - body default */
    line-height: var(--dt-line-height-body);
    color: #171717;
    margin: 0;
  }
</style>
```

### Example 2 — Fluid display heading with clamp()

Tokens: `assets/css/typography-tokens.css`

```html
<section class="hero">
  <h1 class="display">Ship faster, type better</h1>
</section>
<script>
  // Fluid display: interpolate between scale stops (1.5rem → 1.875rem)
  const css = getComputedStyle(document.documentElement);
  const xl = parseFloat(css.getPropertyValue('--dt-font-size-xl'));   // 1.5
  const xxl = parseFloat(css.getPropertyValue('--dt-font-size-2xl')); // 1.875
  document.documentElement.style.setProperty(
    '--dt-font-size-display-fluid',
    `clamp(${xl}rem, ${xl}rem + ${(xxl - xl) * 4}vw, ${xxl}rem)`
  );
</script>
<style>
  .hero { padding: 48px 24px; font-family: var(--dt-font-family-sans); }
  .display {
    font-size: var(--dt-font-size-display-fluid, var(--dt-font-size-2xl));
    font-weight: var(--dt-font-weight-semibold);
    line-height: 1.15;
    letter-spacing: -0.03em;
    margin: 0;
  }
</style>
```

## 10. Implementation Checklist

- [ ] Every font-size token is in rem and steps along one modular scale (root 16px, ratio 1.2–1.25) — zero px sizes, zero off-scale one-offs.
- [ ] Only 400/500/600/700 weights are loaded; the family files contain no unused weights.
- [ ] Maximum two font families ship (text face + optional display/mono), each with system fallbacks in `--dt-font-family-sans`.
- [ ] Each size step has a paired line-height reviewed together; long-form reading uses 1.7, body default uses `--dt-line-height-body`.
- [ ] Token names describe role (`text-body`, `text-heading`), not appearance — no `text-small-bold-uppercase`-style names.
- [ ] Display steps use negative tracking (-0.02em to -0.04em); uppercase labels use +0.04em.
- [ ] Vietnamese/diacritic text is visually verified unclipped at every step, including at 200% browser zoom (WCAG 1.4.4).
- [ ] Fluid display headings interpolate between two scale stops with `clamp()` — no viewport-specific breakpoints for type.

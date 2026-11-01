---
name: webfont-loading
description: Fast, stable font delivery — subsets, font-display, preload discipline, and CLS prevention that keeps text readable while fonts arrive.
tags: [performance, webfonts, subsetting, cls, preload]
related: [font-pairing, variable-fonts, multilingual-vietnamese]
---

# Typography Skill: Webfont Loading & Performance

## 1. Definition

Webfont loading is the performance contract of typography: fonts arrive fast (subsets, WOFF2, compression), text renders immediately (font-display swap), and layout does not jump when the real face lands (CLS < 0.02). Every 100ms of font delay is perceived slowness; every reflow is user-visible jank. This skill covers the loading pipeline — what to load (unicode-range subsets), when to load (preload), and how to fail gracefully (metric-matched fallback). Custom fonts are an enhancement, never a dependency; the system stack is always the fallback.

## 2. Core Principles

- **WOFF2 only, subset per script:** latin/latin-ext/vietnamese unicode-range subsets cut payload 50–80% versus monolithic files.
- **Load the closed weight set only:** 2–3 weights per face (type tokens) — every extra weight is a request nobody needed.
- **font-display: swap with metric-matched fallbacks:** text shows immediately in the fallback, swaps when ready — invisible-text periods (block) are worse than FOUT.
- **Preload only the primary subset:** one `<link rel=preload>` for the above-the-fold body font; preloading everything delays everything.
- **Kill CLS with size-adjust:** ascent-override/size-adjust on the fallback keeps layout stable while the real font loads.
- **Self-host when possible:** third-party font CDNs add DNS/TLS round trips and privacy exposure; self-hosting wins on control.
- **Cache aggressively:** immutable + max-age=31536000 on versioned font files — repeat visits cost zero.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Font format | `--type-font-format` | `woff2-only` | Modern browsers; no woff/ttf fallbacks needed |
| Font-display strategy | `--type-font-display-strategy` | `swap` | Text visible immediately in fallback face |
| Preload policy | `--type-preload-policy` | `primary-subset-only` | Above-the-fold body font, one request |
| Subset strategy | `--type-subset-strategy` | `unicode-range` | latin + latin-ext + vietnamese per face |
| Fallback matching | `--type-fallback-matching` | `size-adjust-tuned` | ascent-override/size-adjust kill CLS |
| Weight budget | `--type-weight-budget` | `max-3-per-face` | Matches the closed type-token weight set |
| Total font budget | `--type-total-font-budget` | `under-100kb` | All faces+subsets per page view |
| Hosting | `--type-hosting` | `self-hosted` | First-party origin; immutable caching |
| Cache policy | `--type-cache-policy` | `immutable-1y` | Versioned filenames, 1-year max-age |
| CLS target | `--type-cls-target` | `under-0.02` | Font-swap layout shift budget |

Consume by linking `assets/css/webfont-loading.css` in the document `<head>` before any stylesheet that references custom fonts, then referencing `var(--type-font-display-strategy)` and `var(--type-font-format)` in @font-face declarations. Actual font files and subsetting are handled in the build step.

## 4. Composition

- Composes with font-pairing and variable-fonts: the closed weight set and unicode-range subset strategy originate in those decisions — loading executes what pairing and variable-fonts specify.
- Composes with multilingual-vietnamese: unicode-range subsets are the mechanism by which Vietnamese coverage ships without payload bloat — the two skills are two sides of the same decision.
- Composes with perceived-performance (skill-design-review): font loading is a top-3 source of CLS and perceived slowness — audit it early and update the budget continuously.

## 5. Signature Patterns

- **Self-hosted subset pipeline:** the build step subsets WOFF2 per script and emits @font-face with unicode-range + one preload hint for the body font — the same output format every time.
- **Fallback metric tuning:** measure the primary face's ascent/size-adjust deltas once per family and bake them into the fallback @font-face block — the tuning is done once, then versioned with the font.

## 6. Real-World Use Cases

- **Any product loading custom fonts** — the defaults here (swap + unicode-range subsets + preload primary subset) are the starting config for every webfont adoption.
- **Performance audits:** measuring font payload, swap CLS, and invisible-text periods against the `--type-total-font-budget` (under-100kb) and `--type-cls-target` (under-0.02) tokens.
- **Privacy-sensitive products:** eliminating third-party font CDN exposure — self-hosting with `--type-hosting: self-hosted` is the first step.

## 7. Combination Notes

### With other typography skills

- **Pairs naturally with font-pairing and variable-fonts:** the loading decision is downstream of the family and weight decisions — pairing defines what to load; loading defines how.
- **Pairs with multilingual-vietnamese:** unicode-range subsets (latin + latin-ext + vietnamese) are the concrete overlap — a webfont-loading setup without vietnamese subsets is a coverage failure.
- **Caution with type-scale:** if the scale uses many weights, the `--type-weight-budget` (max-3-per-face) constraint may conflict — revisit the scale before inflating the font payload.
- **Avoid pairing with font-pairing for faces without WOFF2:** every custom face must ship as WOFF2 only; if the foundry only provides TTF, the face is not adoptable.

### With design styles (companion repo skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** these styles typically use one or two weights — well within the budget tokens, easy to subset.
- **Caution with maximalism:** editorial or luxury designs may demand 6+ weights and decorative faces, inflating the payload past `--type-total-font-budget` — scope the weight budget with the design team before committing.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** loading-state typography transitions (weight or style changes on font arrival) should animate with token-driven durations — instant swaps feel jarring.
- **Caution with data-animation:** count-up or animated number displays must not change face mid-animation — the swap moment will cause the digit widths to change, breaking the animation.

## 8. Anti-Patterns

- **Preload everything** — six preloaded fonts starving the critical path
- **Block-then-render** — font-display: block hiding text 3s behind an invisible period
- **Monolithic files** — 400KB font files loading 6 weights and 3 scripts for one page
- **Third-party default** — shipping Google Fonts CDN by default with no privacy/perf review

### Accessibility Notes

Loading strategy is an accessibility issue: invisible-text periods (font-display: block) hide content from everyone — including screen reader users who encounter the page mid-load. CLS from un-tuned font swaps disorients users with motor or low-vision impairments who rely on stable layout to navigate. The `--type-font-display-strategy: swap` token with `--type-fallback-matching: size-adjust-tuned` is the baseline; the fallback rule: if font loading cannot be optimized in time, system font stacks are a valid, fast, accessible default — custom fonts are an enhancement, never a dependency.

## 9. Code Examples

### Example 1 — Self-hosted WOFF2 subset pipeline with swap and preload

```html
<!-- Preload only the above-the-fold latin body subset — one request -->
<link rel="preload" as="font" type="font/woff2"
  href="/fonts/inter-latin.woff2?v=3.19" crossorigin />

<link rel="stylesheet" href="assets/css/webfont-loading.css" />

<style>
  /* Fallback tuned with size-adjust to kill CLS */
  @font-face {
    font-family: 'Inter';
    src: local('Segoe UI'), local('Helvetica Neue'), local('Arial');
    font-display: var(--type-font-display-strategy, swap);
    size-adjust: 104%;
    ascent-override: 92%;
  }
  /* Primary latin subset */
  @font-face {
    font-family: 'Inter';
    src: url('/fonts/inter-latin.woff2?v=3.19') format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC;
    font-display: var(--type-font-display-strategy, swap);
  }
  /* Latin-extended + Vietnamese subset — loads when unicode-range matches */
  @font-face {
    font-family: 'Inter';
    src: url('/fonts/inter-latin-ext-vietnamese.woff2?v=3.19') format('woff2');
    unicode-range: U+0100-024F, U+1EA0-1EF9;
    font-display: var(--type-font-display-strategy, swap);
  }

  body { font-family: 'Inter', system-ui, sans-serif; }
</style>
```

### Example 2 — Variable font with font-feature-settings and metric fallback

```html
<link rel="preload" as="font" type="font/woff2"
  href="/fonts/be-vietnam-pro-var.woff2?v=1.004" crossorigin />

<style>
  @font-face {
    font-family: 'Be Vietnam Pro';
    src: local('Noto Sans'), local('Arial');
    font-display: var(--type-font-display-strategy, swap);
    size-adjust: 101%;
    ascent-override: 94%;
  }
  @font-face {
    font-family: 'Be Vietnam Pro';
    src: url('/fonts/be-vietnam-pro-var.woff2?v=1.004') format('woff2');
    font-display: var(--type-font-display-strategy, swap);
    font-weight: 100 900;
  }

  :root {
    --type-weight-regular: 400;
    --type-weight-semibold: 600;
  }

  .article-headline {
    font-family: 'Be Vietnam Pro', system-ui, sans-serif;
    font-size: clamp(2rem, 5vw, 4rem);
    font-weight: var(--type-weight-semibold, 600);
    font-feature-settings: 'calt' 1, 'mark' 1, 'liga' 1;
    line-height: 1.2;
  }

  .body-text {
    font-family: 'Be Vietnam Pro', system-ui, sans-serif;
    font-size: 1.125rem;
    font-weight: var(--type-weight-regular, 400);
    font-feature-settings: 'calt' 1, 'mark' 1;
    line-height: 1.6;
    max-width: 66ch;
  }
</style>
```

## 10. Implementation Checklist

- [ ] All @font-face declarations use `--type-font-format` (woff2-only) — no woff or TTF in any production build.
- [ ] `font-display: var(--type-font-display-strategy, swap)` on every @font-face; zero `block` or `optional` declarations.
- [ ] Only one `<link rel=preload>` per page for the above-the-fold body font — no preloading of display, italic, or secondary subsets.
- [ ] Fallback @font-face blocks include `size-adjust` and `ascent-override` tuned to the primary face metrics — CLS checked with the font-swap test.
- [ ] Unicode-range subsets (latin, latin-ext, vietnamese) per face — monolithic font files replaced; total payload verified under `--type-total-font-budget` (under-100kb).
- [ ] Self-hosting confirmed with `--type-hosting: self-hosted`; no Google Fonts CDN default in production builds.
- [ ] Font files use versioned filenames (e.g. `inter-latin.woff2?v=3.19`) and `Cache-Control: max-age=31536000, immutable` headers — `--type-cache-policy: immutable-1y`.
- [ ] CLS measured on font swap (Lab mode in DevTools or WebPageTest filmstrip); confirmed under `--type-cls-target` (under-0.02).
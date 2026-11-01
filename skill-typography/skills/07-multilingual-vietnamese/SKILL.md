---
name: multilingual-vietnamese
description: Diacritic stacking, line-height headroom, fallback stacks, and locale conventions — first-class type for Vietnamese and other marked scripts.
tags: [vietnamese, i18n, diacritics, subsetting, line-height]
related: [font-pairing, line-height, webfont-loading]
---

# Typography Skill: Multilingual & Vietnamese Typography

## 1. Definition

Vietnamese and other diacritic-heavy scripts (Czech, Turkish, Indic) break typography that was designed for English only: stacked tone marks need line-height headroom, fonts need the right OpenType coverage (latin-ext, vietnamese subsets), and fallback stacks determine whether ề renders or becomes tofu. This skill makes marked-script typography a first-class constraint in family selection, scale, and rendering — not an afterthought discovered in QA. In Vietnamese especially, the stakes are semantic: words differ by tone marks alone, so a clipped or missing diacritic is a different word, not a cosmetic flaw.

## 2. Core Principles

- **Vietnamese coverage is an adoption gate:** fonts must include the vietnamese subset (Google Fonts flags it; foundries list it) — no coverage, no adoption.
- **Stacked marks need headroom:** line-height >= 1.5 for body and >= 1.3 even for display — ề, ậ, ắ stack two marks vertically.
- **Subset your webfonts:** ship latin + latin-ext + vietnamese subsets, not the monolithic file — load what the locale needs.
- **Fallback stacks follow the primary:** every fallback in the stack must also carry Vietnamese coverage, or marks render from a different face (the "mixed-face" look).
- **Uppercase transforms marks:** Vietnamese caps carry full diacritics (À, Ạ) — do not strip them, and give caps extra tracking for the taller stack.
- **Locale conventions vary:** Vietnamese uses no letter-spacing traditions; quotes, dashes, and number formatting follow the locale, not the source language.
- **Test real copy, not pangrams:** 'Trăm năm trong cõi người ta' stresses different glyph pairs than 'The quick brown fox'.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Script coverage | `--type-script-coverage` | `latin,latin-ext,vietnamese` | Required subsets per family; adoption gate |
| Line height (vi body) | `--type-line-height-vi-body` | `1.5` | Floor for stacked marks; 1.6 comfortable |
| Line height (vi display) | `--type-line-height-vi-display` | `1.3` | Display leading raised vs Latin 1.1 for mark clearance |
| Fallback chain | `--type-fallback-chain-vi` | `all-fallbacks-covered` | Every fallback face carries Vietnamese |
| Subset strategy | `--type-subset-strategy` | `per-locale-unicode-range` | unicode-range subsets; load only what renders |
| Caps diacritics | `--type-caps-diacritics` | `keep-full` | Uppercase keeps all tone marks |
| Tracking (vi) | `--type-tracking-vi` | `0-0.04em-caps` | Body 0; caps +0.04em for taller stacks |
| Font features (vi) | `--type-font-feature-vi` | `calt-on,mark-on` | Mark positioning features never disabled |
| Test copy | `--type-test-copy-vi` | `real-sentences` | Real Vietnamese copy in QA, not pangrams |
| Mixed-script spacing | `--type-mixed-script-spacing` | `locale-aware` | CJK taller leading; RTL no tracking (see letter-spacing) |

Consume by linking `assets/css/multilingual-vietnamese.css` once per locale scope, then referencing `var(--type-line-height-vi-body)`, `var(--type-tracking-vi)`, and `var(--type-font-feature-vi)` in component styles. Tokens drive headroom and feature flags; actual family selection happens in font-pairing and is gated on `--type-script-coverage`.

## 4. Composition

- Composes with font-pairing: coverage is the first pairing gate — a beautiful face without the vietnamese subset is disqualified at review, before metrics or aesthetics are ever evaluated.
- Composes with line-height: diacritic headroom can override Latin leading aesthetics at every scale step; the `--type-line-height-vi-body` token is the floor, not a suggestion.
- Composes with webfont-loading: subset strategy and unicode-range are the loading-side execution of coverage — the same decision, two implementation surfaces.

## 5. Signature Patterns

- **Mark-stress test page:** a static page of worst-case Vietnamese strings (ộ, ế, ắ at every scale step and weight) screenshotted per release — catches regression before it ships.
- **Fallback simulation:** block the primary font in devtools; verify the fallback renders Vietnamese without metric jumps or tofu — the mixed-face look is caught here.

## 6. Real-World Use Cases

- **Products localizing into Vietnamese** (the default audience for this skill set's authors) — this skill ships with every localization effort by default.
- **Global products handling Czech, Turkish, Polish, Indic scripts** with the same discipline — coverage + headroom applies broadly.
- **Auditing existing products** for mixed-face diacritics, clipped marks, and tofu glyphs in production — the fallback simulation catches all three.

## 7. Combination Notes

### With other typography skills

- **Pairs naturally with font-pairing and line-height:** coverage gates family adoption; line-height tokens supply the headroom. No vi-localized product should ship without both.
- **Pairs with webfont-loading:** unicode-range subsets are the concrete mechanism — the coverage decision and the loading decision express the same requirement.
- **Caution with font-pairing for Latin-optimized faces:** if a chosen face omits vietnamese, the pairing is rejected at the scorecard — do not patch with a separate vi-only fallback font.
- **Avoid pairing with type-scale if the scale was built on Latin leading only:** display sizes that land at 1.1 or 1.2 for aesthetics will clip vi marks; re-tune before shipping.

### With design styles (companion repo skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** both styles use restrained type hierarchies where headroom tokens survive without visual noise.
- **Caution with retro:** retro editorial designs may specify tight leading for period aesthetics; apply the `--type-line-height-vi-display` floor regardless — period feel does not excuse clipped diacritics.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** animate typography state changes (weight, size) with durations that account for mark rendering — fast transitions on diacritic-heavy text can look strobing.
- **Caution with ambient-motion:** animated backgrounds that cycle surface colors must keep their contrast pairings annotated and passing — a cycle that pushes text outside the 4.5:1 floor for any frame is a failure.

## 8. Anti-Patterns

- **Tofu fallbacks** — system stacks (Arial, Helvetica) missing Vietnamese where the custom font fails to load
- **Clipped display marks** — hero headlines at 1.1 leading shearing tone marks
- **English-only QA** — approving fonts from Latin-only test strings
- **Uppercase stripping** — text-transform pipelines that drop Vietnamese diacritics (legacy encodings)

### Accessibility Notes

Clipped or tofu'd diacritics change meaning in Vietnamese — distinguishable words differ by marks alone, so legibility here is comprehension, not aesthetics. WCAG 1.4.4 (resize text) and the headroom requirement must hold together at every scale step. The fallback rule is strict: if the primary face clips marks at a given size, raise line-height product-wide for that step — never switch faces per locale, which creates the mixed-face look and fragments the visual system.

## 9. Code Examples

### Example 1 — Vietnamese stress copy at display and body scale

```html
<h1 class="vi-hero">Hà Nội trong tôi</h1>
<p class="vi-body">Trăm năm trong cõi người ta, chỉ tại nước non.</p>
<p class="vi-small">ề ậ ắ ộ ế — worst-case stacked marks</p>
<style>
  @import url('assets/css/multilingual-vietnamese.css');

  .vi-hero {
    font-family: 'Be Vietnam Pro', 'Noto Serif', serif;
    font-size: 3.5rem;
    font-weight: 700;
    line-height: var(--type-line-height-vi-display, 1.3);
    letter-spacing: -0.02em;
    font-feature-settings: var(--type-font-feature-vi, 'calt' 1, 'mark' 1);
  }
  .vi-body {
    font-family: 'Be Vietnam Pro', 'Noto Serif', serif;
    font-size: 1.125rem;
    font-weight: 400;
    line-height: var(--type-line-height-vi-body, 1.5);
    max-width: 66ch;
  }
  .vi-small {
    font-size: 0.875rem;
    line-height: var(--type-line-height-vi-body, 1.5);
    color: var(--dt-color-neutral-700, #404040);
  }
</style>
```

### Example 2 — Unicode-range subset loading with fallback-chain check

```html
<!-- Preload only the latin core for above-the-fold -->
<link rel="preload" as="font" type="font/woff2"
  href="/fonts/be-vietnam-pro-latin.woff2" crossorigin />
<link rel="preload" as="font" type="font/woff2"
  href="/fonts/be-vietnam-pro-latin-ext-vietnamese.woff2" crossorigin />

<style>
  @font-face {
    font-family: 'Be Vietnam Pro';
    src: url('/fonts/be-vietnam-pro-latin.woff2') format('woff2');
    unicode-range: U+0000-00FF, U+0131, U+0152-0153;
    font-display: swap;
    size-adjust: 102%;
    ascent-override: 95%;
  }
  @font-face {
    font-family: 'Be Vietnam Pro';
    src: url('/fonts/be-vietnam-pro-latin-ext-vietnamese.woff2') format('woff2');
    unicode-range: U+0100-024F, U+1EA0-1EF9;
    font-display: swap;
  }
  /* Every fallback in the stack carries Vietnamese coverage */
  body { font-family: 'Be Vietnam Pro', 'Noto Serif', 'DejaVu Serif', serif; }
</style>
```

## 10. Implementation Checklist

- [ ] All font families adopted for Vietnamese locales include the `vietnamese` subset — coverage verified before the face enters the scorecard.
- [ ] `--type-line-height-vi-body` (1.5) applied to all body text; `--type-line-height-vi-display` (1.3) applied to display/hero sizes.
- [ ] Unicode-range subsets loaded per locale (latin + latin-ext + vietnamese) — monolithic files replaced with per-script WOFF2.
- [ ] Every fallback in every font-family stack verified to carry Vietnamese coverage — no Arial or Helvetica in the vi stack without coverage audit.
- [ ] Real Vietnamese sentence copy used in QA at every scale step — 'Trăm năm…' and stacked-mark strings tested, not pangrams.
- [ ] `text-transform` and uppercase utilities confirmed to preserve Vietnamese diacritics — no stripping in the pipeline.
- [ ] `--type-tracking-vi` (+0.04em caps) applied to all-caps Vietnamese text for mark clearance.
- [ ] Fallback simulation run in devtools (font blocked) — zero tofu, zero mixed-face rendering.

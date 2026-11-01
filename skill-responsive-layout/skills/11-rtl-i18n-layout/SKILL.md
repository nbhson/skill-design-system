---
name: rtl-i18n-layout
description: Layouts that flip, reflow, and re-text for every locale: logical properties, RTL mirroring, text expansion, and internationalization-safe responsive design.
tags: [rtl, i18n, logical-properties, localization, layout]
related: [flexbox-patterns, layout-compositions, responsive-testing]
---

# Responsive Layout Skill: RTL & i18n Layout

## 1. Definition

An internationalized layout survives translation: Arabic/Hebrew flip it horizontally (RTL), German lengthens labels by 35%, Thai changes line-breaking rules, and CJK changes both reading and type expectations. The modern toolkit makes this cheap: CSS logical properties (margin-inline, padding-block, inset-inline) replace physical directions, flex/grid follow direction automatically, and text expansion budgets are planned in component design — so localization becomes configuration, not a layout rewrite.

## 2. Core Principles

- **Logical properties everywhere:** margin-inline-start, not margin-left; padding-block, not padding-top — direction becomes a single dir attribute flip.
- **Flex and grid are direction-aware:** row follows writing direction; row-reverse to 'fix' RTL is a bug, not a fix.
- **Plan for 30-40% text expansion:** German/Finnish labels grow; buttons, nav items, and table headers need flexible widths, never fixed.
- **Mirroring is semantic, not absolute:** media players, progress bars, and timelines flip direction; logos, media controls for playback, and clock faces do not.
- **dir attribute is set at the html level and corrected per-fragment:** user-generated RTL content inside LTR pages gets dir=auto.
- **Icons and arrows flip when directional:** back arrows, chevrons, and indent icons mirror; brand marks and checkmarks do not.
- **Test the full locale matrix:** one RTL locale (Arabic), one long-word locale (German), one CJK (Japanese) — the minimum QA set.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Spacing model | `--layout-i18n-spacing-model` | `logical-properties-only` | margin-inline/padding-block; physical directions lint-blocked |
| Direction source | `--layout-i18n-direction-source` | `html-dir-attr` | dir=rtl\|ltr at root; dir=auto for user content |
| Text expansion | `--layout-i18n-text-expansion` | `40%-budget` | Labels/UI strings sized to survive German-length translations |
| Mirror list | `--layout-i18n-mirror-list` | `documented-per-icon` | Which icons/glyphs flip in RTL; the rest never do |
| Flex behavior | `--layout-i18n-flex-behavior` | `follow-dir-naturally` | No row-reverse hacks; direction flows from dir |
| Test locales | `--layout-i18n-test-locales` | `ar,de,ja` | Minimum QA locale set: RTL + long-word + CJK |
| Line break | `--layout-i18n-line-break` | `line-break-rules-per-script` | Thai/CJK breaking; overflow-wrap: anywhere fallbacks |
| Numerals | `--layout-i18n-numerals` | `locale-formats` | Date/number formatting via Intl, never hand-rolled |
| Nav flip | `--layout-i18n-nav-flip` | `mirror-shell` | Sidebar/logo/actions mirror; content order stays DOM order |
| Font fallback | `--layout-i18n-font-fallback` | `per-script-stacks` | Arabic/CJK/Thai faces in the fallback chain where needed |

Consume them by linking `assets/css/rtl-i18n-layout.css` once at the app root, then referencing `var(--layout-i18n-...)` wherever layout behavior must stay locale-agnostic. Most tokens are contracts rather than raw lengths — they name the policy (logical-properties-only, 40%-budget, ar,de,ja) and are enforced by lint rules and test matrices; the CSS file is the single place those policies are documented alongside the script-aware font fallback stacks.

## 4. Composition

- **Composes with grid-systems and layout-compositions:** the shell's mirroring contract (what flips, what does not) is documented per composition.
- **Composes with flexbox-patterns:** flex follows direction automatically — patterns here must never hardcode physical directions.
- **Composes with multilingual-vietnamese (skill-typography guide 07):** script coverage and fallback stacks are shared contracts.

## 5. Signature Patterns

- **Logical-property migration:** codemod margin-left/right/top/bottom to inline/block equivalents repo-wide; lint blocks new physical properties.
- **RTL smoke page:** one page rendering nav, forms, tables, and icons under dir=rtl, screenshotted per release against the mirror list.

## 6. Real-World Use Cases

- **Products launching Arabic/Hebrew/Urdu markets.**
- **Global products keeping one responsive system across 20+ locales.**
- **Audit: hardcoded margin-left, non-mirroring arrows, buttons that explode with German labels.**

## 7. Combination Notes

### With other responsive-layout skills

- **Good with everything in the catalog:** rtl-i18n-layout has an empty caution and avoid list — logical properties and dir-driven behavior are additive contracts every other layout skill can adopt without changing its own math (grid-systems, flexbox-patterns, css-grid-patterns, layout-compositions, fluid-container-queries, intrinsic-design all list it as good).
- **Good with flexbox-patterns in particular:** flex follows writing direction automatically, so the flex idioms (nav bar, media object, toolbar) become RTL-free the moment they stop hardcoding physical directions.
- **Good with layout-compositions:** the composition catalog is where mirroring contracts live — 'sidebar flips, logo does not' is documented per composition, not rediscovered per page.
- **Good with responsive-testing:** the locale matrix (ar, de, ja) is defined here and executed there; the RTL smoke page is a per-release input to the testing skill's matrix.
- **Good with grid-systems and breakpoints-strategy:** tier changes and column counts survive the dir flip as long as the grid itself is direction-neutral; nothing about the tier set is locale-specific.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism and flat-design:** restrained palettes and flat surfaces keep mirrored interfaces legible — there is no dimensional lighting or texture whose direction betrays a bad flip.
- **Caution with collage-art and brutalism-ui:** overlapping compositions and decorative type treatments rarely survive mirroring cleanly and often rely on hard physical positioning; where these styles are required, define per-locale variants explicitly instead of hoping the dir flip fixes them.

### With motion skills (companion repo skill-animation)

- **Good affinity with page-transitions and easing-timing:** page transitions must read as forward motion in both directions — a transition that slides left in LTR should slide right in RTL; shared easing tokens keep both directions feeling identical.
- **Caution with scroll-animation:** scroll-driven effects with horizontal components (parallax, directional reveals) can contradict RTL reading direction; gate any horizontal motion effect on direction and verify it in the RTL smoke pass.

## 8. Anti-Patterns

- **Physical-direction CSS:** margin-left sprinkled through codebase, making RTL a rewrite instead of an attribute
- **Row-reverse band-aids:** 'fixing' RTL by reversing flex instead of trusting dir
- **Fixed-width labels:** buttons sized for English that shatter with translated strings
- **Everything-mirrors:** flipping logos, clocks, and playback controls that read wrong mirrored

### Accessibility Notes

Correct dir attributes are an accessibility requirement (WCAG 1.3.2 meaningful sequence; H58 dir usage): screen readers switch reading behavior with dir — wrong direction is wrong narration; DOM order must remain logical in both directions. The fallback rule is decisive: if full RTL support cannot ship for a locale, disable that locale's UI (content-only mode) rather than shipping a broken mirrored interface. Note that mirroring must never be achieved by visually reordering the DOM (row-reverse, order) — the source order IS the accessible reading order, which is exactly why the nav-flip token says 'content order stays DOM order'.

## 9. Code Examples

### Example 1 — Logical-properties page under dir=rtl (nav mirrors, arrows flip, logos do not)

Tokens: `assets/css/rtl-i18n-layout.css`

```html
<html lang="ar" dir="rtl">
  <body>
    <header class="bar">
      <img class="logo" src="logo.png" alt="Acme"> <!-- never mirrors -->
      <nav class="nav" aria-label="Primary">
        <a href="#" aria-current="page">الرئيسية</a>
        <a href="#">التقارير</a>
        <a href="#">الإعدادات</a>
      </nav>
      <a class="back" href="#"><svg class="icon" viewBox="0 0 16 16"><path d="M10 2 4 8l6 6"/></svg>رجوع</a>
    </header>
    <main class="page">
      <p class="lead">الاتجاه يتبع سمة dir؛ لا حاجة لأي CSS اتجاهي يدوي.</p>
    </main>
  </body>
</html>
<style>
  .bar {
    display: flex;              /* flex follows dir naturally — no row-reverse */
    align-items: center;
    gap: 1rem;
    padding-block: 0.75rem;
    padding-inline: 1.5rem;     /* logical: flips with dir automatically */
    border-block-end: 1px solid #ddd;
  }
  .nav { display: flex; gap: 1rem; margin-inline-start: auto; }
  .nav a { padding: 0.5rem 0.75rem; text-decoration: none; }
  .nav a[aria-current="page"] { font-weight: 700; }
  .back { display: inline-flex; align-items: center; gap: 0.25rem; text-decoration: none; }
  .icon { width: 16px; height: 16px; }
  /* Directional icon flips; the logo above never does (--layout-i18n-mirror-list) */
  [dir="rtl"] .back .icon { transform: scaleX(-1); }
  [dir="ltr"] .back .icon { transform: none; }
</style>
```

### Example 2 — German text-expansion stress demo (40%-budget contract)

```html
<html lang="en" dir="ltr">
  <body>
    <div class="row">
      <button class="btn" data-en="Save" data-de="Speichern">Save</button>
      <button class="btn" data-en="Delete selected items" data-de="Ausgewählte Elemente löschen">Delete selected items</button>
      <button class="btn" data-en="Settings" data-de="Einstellungen">Settings</button>
    </div>
  </body>
</html>
<style>
  .row { display: flex; flex-wrap: wrap; gap: 0.75rem; padding: 1rem; }
  .btn {
    /* 40%-budget: flexible width, never fixed; growth happens via inline padding */
    min-width: max-content;
    max-width: 100%;
    padding-inline: 1rem;
    padding-block: 0.5rem;
    white-space: nowrap;      /* single-line labels; wrap is the row's job */
    overflow-wrap: anywhere;  /* --layout-i18n-line-break fallback for worst cases */
  }
</style>
<script>
  // Locale-stress probe: swap strings to German and fail if any label overflows
  // its button or the row clips (verifies the --layout-i18n-text-expansion budget).
  const RATIO = 1.4; // 40% expansion budget
  document.querySelectorAll('.btn').forEach(btn => {
    const en = btn.textContent;
    const de = btn.dataset.de;
    btn.style.width = 'auto'; btn.textContent = de;
    const fits = btn.scrollWidth <= btn.clientWidth + 1 && btn.scrollWidth <= en.length * RATIO * 16;
    btn.textContent = en;
    console.assert(fits, `German label overflows budget: "${de}"`);
  });
</script>
```

## 10. Implementation Checklist

- [ ] Zero physical-direction properties (margin-left, padding-top, text-align: left) — `--layout-i18n-spacing-model` is logical-properties-only and lint-enforced.
- [ ] Direction is set by `--layout-i18n-direction-source` (html dir attr), with dir=auto on user-generated fragments.
- [ ] Flex and grid follow direction naturally — no row-reverse, no order hacks anywhere in the codebase.
- [ ] Labels and buttons survive the `--layout-i18n-text-expansion` 40% budget: flexible widths, min-width: max-content, no fixed px.
- [ ] A per-icon mirror list (`--layout-i18n-mirror-list`) exists; arrows/chevrons flip, logos/clocks/playback controls do not.
- [ ] Date/number formatting uses Intl per `--layout-i18n-numerals` — no hand-rolled formatting.
- [ ] Font fallback chains include script faces per `--layout-i18n-font-fallback` for ar, de, ja.
- [ ] The RTL smoke page (nav, forms, tables, icons under dir=rtl) is screenshotted per release across the `--layout-i18n-test-locales` set.

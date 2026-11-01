---
name: platform-mapping
description: One token source translated to CSS custom properties, iOS, Android, and utility frameworks — with values that survive unit and paradigm differences.
tags: [cross-platform, codegen, ios, android, tailwind]
related: [token-pipeline-figma, semantic-alias-naming, dark-mode]
---

# Design Token Skill: Cross-Platform Mapping

## 1. Definition

Platform mapping is the translation layer between the platform-neutral token source and its consumers: CSS custom properties on the web, Swift/iOS asset catalogs and UIFont metrics, Android Compose themes and dimens, plus utility frameworks like Tailwind. Good mapping preserves meaning — one spacing scale, one type ramp — while respecting each platform's units (px/rem/dp/pt), paradigms (font scaling on mobile), and idioms (Material elevation vs CSS shadows). The web renderer, built on prefixed CSS custom properties, is the reference output every other platform renderer is diffed against.

## 2. Core Token Principles

- **One source of truth, many renderers:** tokens are authored once (W3C DTCG format) and codegen'd per platform — hand-synced platform files rot.
- **Unit mapping is explicit:** CSS rem (root 16), iOS pt, Android dp; 1rem = 16 = 16pt = 16dp, and the mapping table is versioned with the tokens.
- **Respect platform font scaling:** iOS Dynamic Type and Android fontScale must multiply type tokens — fixed-pixel type on mobile is an accessibility bug.
- **Map paradigms, not just values:** elevation becomes Material elevation levels on Android and CALayer shadows on iOS; the altitude meaning survives.
- **CSS custom properties are the web renderer:** prefixed (`--dt-`), themeable via data-attributes, and the reference output other renderers are diffed against.
- **Utility frameworks map to tokens, never bypass them:** Tailwind config extends from the same source so text-lg IS font-size-lg.
- **Behavior parity is validated:** dark mode, brand switching, and density modes must work identically on every mapped platform.

## 3. Token Set

| Role | Token | Value | Notes |
|---|---|---|---|
| CSS prefix | `--dt-map-css-prefix` | `--dt-` | Web custom-property prefix; collision-safe |
| iOS prefix | `--dt-map-ios-prefix` | `DT` | Swift enum/asset prefix (DTColor.actionPrimary) |
| Android prefix | `--dt-map-android-prefix` | `dt_` | Resource prefix: dt_action_primary |
| CSS base unit | `--dt-map-base-unit-css` | `1rem = 16px` | Root-relative; multiplies with user font-size preference |
| Native base unit | `--dt-map-base-unit-native` | `1dp = 1pt = 1px@1x` | Density-independent baseline across mobile platforms |
| Font scaling | `--dt-map-font-scaling` | `dynamic-type-on` | iOS Dynamic Type / Android fontScale multiply type tokens |
| Breakpoint sm | `--dt-breakpoint-sm` | `640px` | Phone landscape / small tablet |
| Breakpoint md | `--dt-breakpoint-md` | `768px` | Tablet portrait |
| Breakpoint lg | `--dt-breakpoint-lg` | `1024px` | Tablet landscape / small laptop |
| Breakpoint xl | `--dt-breakpoint-xl` | `1280px` | Desktop; content max-widths derive from here |

Consume them by linking `assets/css/platform-mapping.css` at the app root and referencing `var(--dt-...)` (breakpoints as `@media (min-width: var(--dt-breakpoint-md))` via a preprocessor, since media queries cannot read custom properties natively). These mapping tokens are primarily machine contracts: the codegen reads them to name and scale outputs per platform.

## 4. Composition & Layering

- **Mapping composes with the pipeline:** token-pipeline-figma emits per-platform renderers; this skill defines their contracts (prefixes, units, scaling).
- **It composes with dark mode and brands:** data-theme/data-brand on web, trait collections on iOS, configuration qualifiers on Compose — same alias semantics per platform.
- **It composes with typography:** the type ramp maps with font scaling rules so rem/pt/dp agree at every Dynamic Type size.

## 5. Signature Patterns

- **Codegen with golden tests:** each platform output is generated and diffed in CI; a hand-edit to generated files fails the build.
- **Parity matrix:** rows are features (dark mode, brand, density, font scaling), columns are platforms; a feature ships when all columns pass.

## 6. Real-World Use Cases

- **Design systems spanning web, iOS, and Android** from one token source.
- **Tailwind/utility adoption:** generating the config from tokens so utilities cannot drift.
- **Audit: finding hand-synced platform files** that have already diverged from the source.

## 7. Combination Notes

### With other token skills

- **Pairs well with spacing-sizing and semantic-alias-naming:** uniform units (dp/pt/px) and alias semantics are the easiest things to translate identically across renderers — they form the safe core of any mapping.
- **Pairs well with dark-mode, contrast-validation, and governance-migration:** theme switching must be parity-tested per platform, ratios re-computed per renderer's output, and generated-file hand-edits rejected by the same lint machinery.
- **Pairs well with token-pipeline-figma:** the pipeline is the engine and mapping is the transmission — renderers emitted by the pipeline must honor the prefix/unit/scaling contracts defined here.
- **Caution with color-tokens, typography-tokens, and radius-elevation:** each carries platform-specific physics — sRGB/P3 gamut, Dynamic Type multiplication, Material vs CALayer elevation — so these map by paradigm, not copy-paste; budget design review for the translated behavior, not just the values.
- **Caution with multi-brand-theming and component-tokens:** brand switching and slot overrides use different mechanisms per platform (data-attributes vs trait collections vs qualifiers); verify the alias semantics survive each mechanism before promising parity.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with flat-design and minimalism:** flat, token-friendly aesthetics translate with the least loss across CSS, Material, and Human Interface idioms.
- **Caution with skeuomorphism and neumorphism:** platform idioms already own depth conventions (Material elevation, CALayer shadows); importing a bespoke depth style multiplies the per-platform translation work and drifts easily.

### With motion skills (companion repo skill-animation)

- **Good affinity with page-transitions and gesture-drag:** both map to strong native idioms (UINavigationController push, shared-element transitions, gesture-driven dismissals) — tokens provide the durations/curves while each platform renders natively.
- **Caution with illustration-lottie:** baked motion timelines render near-identically everywhere but bypass the token system; treat them as shared assets, not mapped tokens.

## 8. Anti-Patterns

- **Hand-synced platforms:** three teams maintaining three token files until they quietly disagree
- **Fixed type on mobile:** px-locked font sizes ignoring Dynamic Type and fontScale
- **Value-only mapping:** copying hexes but losing the semantic layer, so dark mode must be rebuilt per platform
- **Utility bypass:** Tailwind arbitrary values (text-[17px]) as a side door around the mapped scale

### Accessibility Notes

Platform mapping owns WCAG 1.4.4 resize on the web — rem-based tokens honoring the user's font-size preference — and its native equivalents, iOS Dynamic Type and Android fontScale. A token set that renders at fixed px on mobile fails accessibility regardless of how good its contrast ratios are, because users lose the ability to scale text at all. The type ramp must therefore be expressed in scaling units per platform (rem, pt with `UIFontMetrics`, sp with fontScale), with layouts that tolerate the resulting reflow. If a platform renderer genuinely cannot support font scaling, that platform's type tokens ship with a documented fixed-size exception and a tracking ticket — never silently.

## 9. Code Examples

### Example 1 — Web reference output: tokens, breakpoints, and a card UI

Tokens: `assets/css/platform-mapping.css`

```html
<section class="card">
  <h2>Quarterly report</h2>
  <p>Rendered from the same tokens the iOS and Android builds consume.</p>
  <button class="btn">Download PDF</button>
</section>
<style>
  :root {
    --dt-map-css-prefix: --dt-;
    --dt-map-base-unit-css: 1rem = 16px;
    /* Translated values (codegen output shown inline for standalone demo) */
    --dt-space-4: 1rem;      /* 16px = 16dp = 16pt */
    --dt-radius-md: 0.5rem;  /* 8px */
    --dt-color-action-primary: #2563EB;
    --dt-color-text-on-action: #FFFFFF;
  }
  .card {
    max-width: 22rem; /* content max-widths derive from breakpoints */
    margin: var(--dt-space-4) auto; padding: var(--dt-space-4);
    border-radius: var(--dt-radius-md);
    border: 1px solid #e4e7ec; font: 0.875rem/1.5 system-ui;
  }
  .btn {
    padding: 0.625rem 1rem; border: 0; border-radius: var(--dt-radius-md);
    background: var(--dt-color-action-primary); color: var(--dt-color-text-on-action);
  }
  /* Breakpoints come from the same token source; md = 768px */
  @media (min-width: 768px) { .card { max-width: 34rem; } }
</style>
```

### Example 2 — One token, four renderers (CSS + Tailwind + Swift + Kotlin sketch)

Tokens: `assets/css/platform-mapping.css`

```html
<button class="btn">Action</button>
<style>
  /* Renderer 1: CSS (reference output) */
  .btn {
    height: 2.5rem;              /* 40px = 40dp = 40pt */
    padding: 0 1rem;
    border-radius: 0.5rem;       /* --dt-radius-md */
    background: var(--dt-color-action-primary, #2563EB);
    color: var(--dt-color-text-on-action, #FFFFFF);
    font-size: 1rem;             /* rem: scales with user preference (WCAG 1.4.4) */
  }
</style>
<script>
  /* Renderer 2: Tailwind config is GENERATED from the same DTCG source —
     never hand-extended, never bypassed with arbitrary values. */
  const tailwindSketch = {
    theme: { extend: {
      spacing:    { '4': 'var(--dt-space-4)' },
      fontSize:   { lg: 'var(--dt-font-size-lg)' },   /* text-lg IS font-size-lg */
      borderRadius: { md: 'var(--dt-radius-md)' },
      colors:     { 'action-primary': 'var(--dt-color-action-primary)' },
      screens:    { sm: '640px', md: '768px', lg: '1024px', xl: '1280px' },
    } } /* text-[17px] in PRs fails the lint: no side doors */
  };
  /* Renderer 3: Swift — prefix DT, pt units, Dynamic Type ON
     enum DTColor { static let actionPrimary = Color(hex: 0x2563EB) }
     enum DTSpacing { static let space4: CGFloat = 16 }          // pt
     // Type: UIFontMetrics(forTextStyle: .body).scaledFont(
     //        for: .systemFont(ofSize: 16))  // multiplies with Dynamic Type */
  /* Renderer 4: Kotlin — prefix dt_, dp/sp units
     object DTColor { val actionPrimary = Color(0xFF2563EB) }
     val dtSpace4 = 16.dp                                        // dp
     // Type: 16.sp  // fontScale multiplies sp automatically */
  console.log('Renderers kept in sync via codegen + golden tests, not humans.');
</script>
```

## 10. Implementation Checklist

- [ ] Tokens are authored once in W3C DTCG format and codegen'd — no platform file is hand-maintained.
- [ ] The mapping table (`--dt-map-base-unit-css`, `--dt-map-base-unit-native`, prefixes) is versioned alongside the tokens.
- [ ] All type tokens render in scaling units: rem on web, Dynamic Type-aware pt on iOS, sp on Android (`--dt-map-font-scaling: dynamic-type-on` verified).
- [ ] Generated files carry a DO-NOT-EDIT header and a CI golden test; hand-edits fail the build.
- [ ] Tailwind config is generated from the token source; `text-lg` resolves to the token, and arbitrary values like `text-[17px]` fail lint.
- [ ] Dark mode, brand switching, and density modes pass the parity matrix on every platform column before a feature ships.
- [ ] Breakpoints (`--dt-breakpoint-sm` through `--dt-breakpoint-xl`) are the only media-query values in the codebase.
- [ ] Elevation maps by paradigm (Material levels, CALayer shadows), not by copying CSS box-shadows verbatim.

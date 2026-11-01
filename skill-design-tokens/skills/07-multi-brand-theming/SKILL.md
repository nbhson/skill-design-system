---
name: multi-brand-theming
description: White-label theming at the alias tier — per-brand primitive overrides, a locked shared vocabulary, and a brand matrix that stays validated instead of exploding.
tags: [theming, white-label, brand-tokens, alias-tier, design-systems]
related: [semantic-alias-naming, color-tokens, contrast-validation]
---

# Design Token Skill: Multi-Brand Theming

## 1. Definition

Multi-brand theming extends the dark-mode mechanism horizontally: instead of two themes over one brand, it manages N brands, each re-pointing the same semantic aliases to its own set of primitives. The discipline lies less in what brands may change than in what they may not — the shared component vocabulary, spacing, and interaction patterns stay fixed while color, radius personality, font family, and illustration voice vary per brand. The failure mode is the matrix explosion: brands × themes × densities × components, each cell demanding its own overrides until the system collapses under its own forks. Done correctly, a brand is just another theme — a scoped set of alias overrides that ships through the same pipeline and validation gates as everything else.

## 2. Core Token Principles

- **Brands override the alias tier only:** they may re-point `color-action-primary` and friends, never restructure the vocabulary itself.
- **The component tier is brand-neutral:** if two brands genuinely need different button anatomy, that is two components — not one component riddled with brand forks.
- **Per-brand primitives ship as full scales, not single hexes:** a brand anchor plus its contrast-safe siblings, validated like any other ramp.
- **Typography varies by family, not by scale:** brands may swap the font family but inherit the same size and line-height steps (license and loading permitting).
- **The brand matrix is explicit:** brands × themes documented in one table; a cell that has not been contrast-validated does not ship.
- **Brand switching is runtime-safe:** swapping a `data-brand` attribute re-points aliases without reload — the proof that tier separation is real, not theoretical.
- **Shared components are the contract:** a brand override that breaks a component in another brand fails CI (governance), not just the brand's own eyes.

## 3. Token Set

| Role | Token | Value | Notes |
|---|---|---|---|
| Brand A anchor | `--dt-brand-a-primary` | `#2563EB` | Brand A anchor; full sibling ramp validated around it |
| Brand A on-primary | `--dt-brand-a-on-primary` | `#FFFFFF` | Text on A-primary: 4.6:1 |
| Brand B anchor | `--dt-brand-b-primary` | `#16A34A` | Brand B anchor; white text fails 3.0:1 - use neutral-900 |
| Brand B on-primary | `--dt-brand-b-on-primary` | `#052E16` | Dark text on B-primary: 10.9:1 - proves on-primary must be per-brand |
| Brand C anchor | `--dt-brand-c-primary` | `#9333EA` | Brand C anchor; white on it passes 4.9:1 |
| Brand radius override | `--dt-brand-radius-override` | `12px` | Optional per-brand radius personality at alias tier |
| Brand font override | `--dt-brand-font-override` | `'Brand Sans', Inter, sans-serif` | Family swap only; size scale inherited |
| Theming strategy | `--dt-theming-strategy` | `alias-tier-override` | The documented mechanism; component forks are forbidden |
| Logo slot | `--dt-brand-logo-max-width` | `160px` | Layout slot contract so brand marks cannot break headers |

Consume them by linking `assets/css/multi-brand-theming.css` once at the app root and reading `var(--dt-brand-*)` (and any other `var(--dt-...)`) from component code. The `data-brand` attribute selects which brand block wins in the cascade; components never know which brand is active.

## 4. Composition & Layering

- **Brand theming stacks with dark mode:** the matrix is brands × themes, so each brand's primitives need both light and dark validated pairings — budget for it before the second brand lands, not after.
- **It composes with component tokens:** component tokens reference semantic aliases, so a brand switch flows through automatically; per-brand component-token forks are the avoid-level failure.
- **It composes with governance:** brand overrides ship through the same review and validation pipeline as core tokens — a brand is a theme, not a fork.

## 5. Signature Patterns

- **`data-brand` + `data-theme` composition:** `[data-brand='b'][data-theme='dark']` — CSS custom properties compose naturally; each axis owns its tier and neither touches component code.
- **Brand starter kit:** each brand onboards with a template (anchor hex + font family + logo slot), and the pipeline generates its validated ramps and pairings.

## 6. Real-World Use Cases

- **White-label SaaS** where customer logos and colors overlay one product.
- **Multi-brand portfolios** sharing one component library across consumer brands.
- **Agency/client handoff:** the design system ships, the client brand themes it safely.

## 7. Combination Notes

### With other token skills

- **Pairs well with color-tokens and semantic-alias-naming:** brands are expressed as per-brand primitive ramps re-pointed at the alias tier — the alias vocabulary is precisely what keeps N brands from becoming N codebases.
- **Pairs well with contrast-validation:** the brand × theme matrix is exactly the pairing table the validation skill automates; without it, matrix cells ship unmeasured.
- **Pairs well with token-pipeline-figma and governance-migration:** brand onboarding is generated from a starter kit and gated like any token change — the pipeline makes "a brand is a theme" mechanically true.
- **Caution with typography-tokens, spacing-sizing, radius-elevation, and dark-mode:** each multiplies the matrix (font loading per brand, density per brand, radius per brand, themes per brand); allow variance only where the brand case is proven, and re-validate the combined cells.
- **Avoid component-tokens for brand variation:** per-brand component token forks are the canonical anti-pattern — if a brand truly needs different component anatomy, that is a new component, not a fork of the token layer.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism and flat-design:** restrained styles scale across brands because a token swap is enough to carry the brand voice; the shared component anatomy stays coherent.
- **Caution with retro and skeuomorphism:** highly opinionated styles encode their personality in structure, not just values — two brands with different retro voices will not share components, and forcing them through aliases produces a compromise nobody chose.

### With motion skills (companion repo skill-animation)

- **Caution with illustration-lottie:** brand-specific motion assets are baked timelines, not tokens; a brand swapping illustration voice swaps Lottie files wholesale, so keep brand motion out of the token contract and treat those assets as per-brand deliverables.

## 8. Anti-Patterns

- **Brand component forks:** button-brand-a vs button-brand-b instead of one button consuming brand aliases
- **Single-hex brands:** a brand with only a primary hex cannot fill hover, disabled, and on-primary roles accessibly
- **Unvalidated matrix cells:** shipping brand x theme combinations no one ever contrast-checked
- **Brand-specific vocabulary:** brand-a-card-bg aliases that fragment the semantic tier per brand

### Accessibility Notes

Brand identity never lowers the bar. Each brand's on-primary, link, and feedback pairings must pass WCAG 1.4.3 in every theme cell of the matrix — and `on-primary` is a per-brand token precisely because a shared white fails on some anchors (white on the green `--dt-brand-b-primary` lands at 3.0:1 while the dark `--dt-brand-b-on-primary` reaches 10.9:1). The fallback is equally non-negotiable: if a brand's anchor cannot reach 4.5:1 with any text, the anchor changes or its text role darkens — brand preference loses to contrast, every time.

## 9. Code Examples

### Example 1 — data-brand + data-theme attribute switching, no reload

Tokens: `assets/css/multi-brand-theming.css`

```html
<main data-brand="a" data-theme="light">
  <div class="card">
    <h1>Team workspace</h1>
    <p>One component tree; the brand axes re-point aliases underneath it.</p>
    <button class="btn" onclick="this.closest('main').dataset.brand =
      this.dataset.brand === 'a' ? 'b' : 'a';
      this.dataset.brand = this.closest('main').dataset.brand">
      Switch brand (<span id="who">A</span>)
    </button>
  </div>
</main>
<style>
  /* Alias defaults (Brand A, light) */
  main { --action: var(--dt-brand-a-primary); --on-action: var(--dt-brand-a-on-primary); }
  /* Brand axis: each brand owns only its alias re-pointing */
  [data-brand="b"] { --action: var(--dt-brand-b-primary); --on-action: var(--dt-brand-b-on-primary); }
  [data-brand="c"] { --action: var(--dt-brand-c-primary); --on-action: #FFFFFF; }
  #who { font-weight: 600; }
  .card {
    max-width: 340px; margin: 24px auto; padding: 24px;
    font: 14px/1.5 var(--dt-brand-font-override);
    border-radius: var(--dt-brand-radius-override);
    background: #fff; border: 1px solid #e4e7ec;
  }
  .btn {
    padding: 10px 16px; border: 0; border-radius: 8px; cursor: pointer;
    background: var(--action); color: var(--on-action);
  }
</style>
```

### Example 2 — Brand starter kit ramp with validated on-primary per anchor

Tokens: `assets/css/multi-brand-theming.css`

```html
<div class="row" data-brand="a"><span class="swatch"></span><code>A · white on #2563EB → 4.6:1</code></div>
<div class="row" data-brand="b"><span class="swatch"></span><code>B · #052E16 on #16A34A → 10.9:1</code></div>
<div class="row" data-brand="c"><span class="swatch"></span><code>C · white on #9333EA → 4.9:1</code></div>
<style>
  .row { display: flex; align-items: center; gap: 12px; margin: 12px auto; max-width: 420px; font: 13px/1.4 monospace; }
  .swatch { width: 48px; height: 32px; border-radius: 8px; background: var(--action); display: grid; place-items: center; }
  .swatch::after { content: "Aa"; font: 600 14px system-ui; color: var(--on-action); }
  [data-brand="a"] { --action: var(--dt-brand-a-primary); --on-action: var(--dt-brand-a-on-primary); }
  [data-brand="b"] { --action: var(--dt-brand-b-primary); --on-action: var(--dt-brand-b-on-primary); }
  [data-brand="c"] { --action: var(--dt-brand-c-primary); --on-action: #FFFFFF; }
</style>
```

## 10. Implementation Checklist

- [ ] Every brand ships as a `data-brand` alias-override block — zero per-brand component forks (`button-brand-a` does not exist).
- [ ] Each brand defines a full ramp around its anchor, not a lone `--dt-brand-*-primary` hex — hover, pressed, and disabled siblings exist.
- [ ] `--dt-brand-*-on-primary` is declared per brand; a shared white on-primary is a failing pairing waiting to happen.
- [ ] The brands × themes matrix is documented in one table, and every cell has a computed contrast ratio before merge.
- [ ] Swapping `data-brand` at runtime re-points all aliases without reload — verified manually and in a test.
- [ ] Typography variance is family-only: the size/line-height scale is inherited from the shared system.
- [ ] Brand overrides pass through the same pipeline review and CI gates as core token changes.
- [ ] Brand marks are constrained by `--dt-brand-logo-max-width` so no logo can break the header layout.

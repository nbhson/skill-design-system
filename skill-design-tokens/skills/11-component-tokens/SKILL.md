---
name: component-tokens
description: Per-component token slots (component-button-bg, component-input-border) derived from semantic aliases — the top tier that gives components flexibility without forking the system.
tags: [tokens, components, theming, api, design-systems]
related: [semantic-alias-naming, multi-brand-theming, governance-migration]
---

# Design Token Skill: Component Tokens

## 1. Definition

Component tokens are the top tier of the token architecture: named slots owned by a specific component (`component-button-radius`, `component-input-border-focus`) whose defaults derive from semantic aliases rather than raw values. They give components an extension surface — products and brands can restyle a button via tokens without touching component code — while keeping every default traceable to the system. The art is restraint: a component token is an API, and every slot you expose is a promise to support, document, and eventually deprecate with a migration path. Few well-chosen slots beat a knob for every CSS property.

## 2. Core Token Principles

- **Derive defaults, never fork:** `component-button-bg: var(--dt-color-action-primary)` — a component token that hardcodes a hex has bypassed the system and silently exempted the component from every theme.
- **Slots, not knobs:** expose the handful of decisions consumers actually make (bg, radius, height, border) — not every internal CSS property, or the component's internals become public contract.
- **Component tokens are the only tier components consume transitively:** code reads `component-*` or `alias-*` tokens; primitives are invisible to product code by construction.
- **State slots are explicit:** `-hover`, `-focus`, `-disabled` variants exist for every colored slot — no runtime color math (`brightness(0.9)`) hiding inside components.
- **Size variants are token families:** `component-button-height-sm/md/lg` ship as a set, and the variants agree on which steps they use.
- **Naming is namespaced:** `component-{component}-{property}` prevents collisions across libraries and makes ownership grep-able — `--bg` or `--radius` alone is a collision waiting to happen.
- **Adding a slot is an API review:** every new component token is documented, versioned, and deprecation-managed like any public interface, because that is exactly what it is.

## 3. Token Set

| Role | Token | Value | Notes |
|---|---|---|---|
| Component | `--dt-component-button-height` | `40px` | Default control height; sm=32px, lg=48px siblings |
| Component | `--dt-component-button-radius` | `var(--dt-radius-md)` | Derived from system radius, overridable per product |
| Component | `--dt-component-button-bg` | `var(--dt-color-action-primary)` | Default primary action surface |
| Component | `--dt-component-button-text` | `var(--dt-color-text-on-action)` | Paired label color; contrast-validated with -bg |
| Component | `--dt-component-input-height` | `44px` | Meets the 44px touch target floor |
| Component | `--dt-component-input-border-focus` | `var(--dt-contrast-focus-ring-color)` | Focus ring slot; 3:1-validated |
| Component | `--dt-component-card-padding` | `var(--dt-space-4)` | Density modes re-map space tokens, cards follow |
| Component | `--dt-component-modal-max-width` | `640px` | Reading-width contract for dialogs |
| Component | `--dt-component-table-row-height` | `48px` | Compact mode derives 40px from the same slot system |
| Component | `--dt-component-toast-width` | `360px` | Toast footprint; stacking logic depends on it |

Consume them by linking `assets/css/component-tokens.css` after the alias tier (so derived defaults resolve), then referencing `var(--dt-component-<component>-<property>)` inside component styles. Products override slots at a scope (`:root`, `.theme-x`, or a specific region), never by rewriting component CSS. If a slot's default seems wrong, fix the alias it derives from — do not fork the slot.

## 4. Composition & Layering

- **Component tokens consume semantic aliases, which consume primitives** — so dark mode, brands, and density flow through automatically. A component needing its own dark override signals a *missing alias*, not a missing override.
- **They compose with the motion system:** interactive component slots (hover elevation, focus ring appearance) animate using motion tokens from skill-animation, so a slot change never carries its own timing.
- **They compose with governance-migration:** the slot list is an API surface with semver; removing or renaming a slot is a deprecation cycle, not a cleanup commit.

## 5. Signature Patterns

- **Slot contract per component:** every component documents its tokens — name, default, pairing notes — in one table that *is* the component's styling API, reviewed like code.
- **Product theming via slots:** a product overrides `component-button-radius` without forking the component, and the override is reviewed like any other API usage rather than smuggled in with `!important`.

## 6. Real-World Use Cases

- **Component libraries** balancing consistency across products with product-level flexibility.
- **White-label deployments** restyling controls per brand without code forks.
- **Auditing component tiers:** finding components with hardcoded values that should be slots — or slot overload that needs pruning back to decisions consumers actually make.

## 7. Combination Notes

### With other token skills

- **Pairs with color-tokens, typography-tokens, spacing-sizing, and radius-elevation:** these primitive layers supply the values slots derive from; because defaults point at aliases instead of literals, a ramp or radius change re-skins every component with zero component edits.
- **Pairs with semantic-alias-naming:** the alias tier is what makes component slots safe — `component-button-bg` deriving from `color-action-primary` inherits every theme, state axis, and contrast validation the alias already carries.
- **Pairs with dark-mode and contrast-validation:** slot pairings (`button-text` on `button-bg`) are checked in every theme cell through their alias sources, so a slot cannot pass light mode and fail dark.
- **Pairs with token-pipeline-figma and governance-migration:** the pipeline generates and diffs the slot tables, and governance versions them — adding a slot without review is the canonical governance violation.
- **Avoid with multi-brand-theming at the slot level:** per-brand component token forks explode the matrix. If brand A and brand B each fork `component-button-*`, the maintenance surface is brands × themes × components with no shared vocabulary — that is two *components*, not one component with brand forks. Brands override the alias tier; the component tier stays brand-neutral.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism, flat-design, and glassmorphism:** these styles reward a small slot surface — bg/radius/height covers their variation needs, so the API stays honest and small.
- **Caution with collage-art and brutalism-ui:** both prize deliberately rough, per-instance treatments that resist slot-based theming; satisfy them with documented alias overrides or a separate component, never by exposing 40 more knobs.

### With motion skills (companion repo skill-animation)

- **Good affinity with micro-interactions, loading-states, and feedback-confirmation:** these skills define exactly the interactive moments component slots govern (hover, focus, pending), and motion tokens supply the timing so slot changes animate consistently.
- **No caution entries:** component slots are passive values; they animate only via the motion system's tokens, which is the correct division of labor.

## 8. Anti-Patterns

- **Hardcoded defaults:** component-button-bg: #2563EB silently exempting the button from themes
- **Knob explosion:** 40 slots per component - every property exposed is a promise to maintain
- **Hidden color math:** brightness(0.9) inside components instead of declared -hover slots
- **Unnamespaced slots:** --bg or --radius colliding across components

### Accessibility Notes

Slot pairings inherit the contrast contract from the alias layer they derive from: `component-button-text` on `component-button-bg` must pass its threshold in every theme and brand cell, validated through `color-text-on-action` on `color-action-primary` rather than re-measured per component. A slot override that breaks the pairing fails CI — the override is rejected in review, and the product chooses a different validated slot value instead. Sizing slots carry obligations too: `component-input-height` sits at the 44px touch-target floor, and products must not shrink it below that via override. Because slots are themable, they must never encode meaning alone — a focus slot that only changes shadow (not border or outline) disappears in forced-colors modes, so visual state always pairs at least two channels.

## 9. Code Examples

### Example 1 — Button with derived slots and a reviewed product override

Tokens: `assets/css/component-tokens.css`

```html
<button class="btn btn--primary">Deploy to production</button>
<button class="btn btn--primary btn--compact">Deploy</button>
<style>
  :root {
    /* Component tier: defaults DERIVE from aliases — never literals */
    --dt-component-button-height: 40px;
    --dt-component-button-radius: var(--dt-radius-md, 8px);
    --dt-component-button-bg: var(--dt-color-action-primary, #2563EB);
    --dt-component-button-text: var(--dt-color-text-on-action, #FFFFFF);
    --dt-component-button-bg-hover: var(--dt-color-action-primary-hover, #1D4ED8);

    /* Product override — reviewed like API usage, scoped, no !important */
    --dt-component-button-radius: 12px;
  }
  .btn {
    height: var(--dt-component-button-height);
    padding-inline: var(--dt-component-button-height); /* square-ish from the same slot */
    background: var(--dt-component-button-bg);
    color: var(--dt-component-button-text); /* pairing contrast-validated upstream */
    border: none;
    border-radius: var(--dt-component-button-radius);
    font: 600 14px/1 system-ui;
    cursor: pointer;
    /* State slots are explicit — no filter: brightness() math */
    transition: background 150ms ease;
  }
  .btn--primary:hover { background: var(--dt-component-button-bg-hover); }
  .btn:focus-visible { outline: 2px solid var(--dt-component-button-bg); outline-offset: 2px; }
  .btn--compact {
    --dt-component-button-height: 32px; /* sm sibling of the same token family */
    font-size: 13px;
  }
</style>
```

### Example 2 — Input whose slots inherit themes and the 44px floor

Tokens: `assets/css/component-tokens.css`

```html
<label class="field">
  <span class="field-label">API key</span>
  <input class="field-input" type="text" value="dt_live_9f2c…" />
</label>
<style>
  :root {
    --dt-component-input-height: 44px; /* WCAG 2.5.8 touch-target floor */
    --dt-component-input-border: var(--dt-color-border-default, #D4D4D4);
    --dt-component-input-border-focus: var(--dt-contrast-focus-ring-color, #1D4ED8);
    --dt-component-input-bg: var(--dt-color-bg-default, #FFFFFF);
  }
  .field { display: grid; gap: 4px; max-width: 320px; font: 14px/1.4 system-ui; }
  .field-label { color: var(--dt-color-text-secondary, #404040); font-weight: 500; }
  .field-input {
    height: var(--dt-component-input-height); /* a product cannot legally shrink this */
    padding: 0 12px;
    background: var(--dt-component-input-bg);
    border: 1px solid var(--dt-component-input-border);
    border-radius: 8px;
    font: inherit;
  }
  .field-input:focus-visible {
    outline: 2px solid var(--dt-component-input-border-focus);
    outline-offset: 2px; /* 3:1-validated slot — two channels, not shadow alone */
  }
  /* Dark theme flows through aliases: slots resolve automatically, no override needed. */
  [data-theme="dark"] {
    --dt-color-border-default: #2E2E30;
    --dt-color-bg-default: #1C1C1E;
    --dt-color-text-secondary: #A3A3A3;
  }
</style>
```

## 10. Implementation Checklist

- [ ] Every component default derives from an alias (`var(--dt-color-*)`, `var(--dt-space-*)`, `var(--dt-radius-*)`) — zero literal hexes or px values inside component styles except in slot defaults.
- [ ] Slots are namespaced as `--dt-component-{component}-{property}`; no bare `--bg`/`--radius` custom properties exist in any component.
- [ ] Every colored slot has explicit `-hover`/`-focus`/`-disabled` siblings — no `filter: brightness()` or runtime color math in components.
- [ ] Each component ships a slot-contract table (name, default, pairing notes) reviewed as its public API.
- [ ] Size variants ship as token families (`-sm/-md/-lg`) and agree on which scale steps they use.
- [ ] Sizing slots respect floors: input heights stay at or above the 44px touch target in every override.
- [ ] No product override creates a failing contrast pairing — CI validates slot pairings in every theme/brand cell.
- [ ] Adding, renaming, or removing a slot goes through governance review with semver and a changelog entry — never a drive-by commit.

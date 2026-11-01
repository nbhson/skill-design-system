---
name: radius-elevation
description: Border-radius steps, shadow elevation levels, and a closed z-index enum — the depth system that says what floats above what, in four shadows and five radii instead of forty ad-hoc box-shadows.
tags: [depth, radius, elevation, z-index, shadows]
related: [semantic-alias-naming, dark-mode, spacing-sizing]
---

# Design Token Skill: Radius & Elevation Tokens

## 1. Definition

Radius and elevation tokens encode **depth**: border-radius communicates surface softness and container identity, shadow tokens encode height above the page (card < dropdown < modal < toast), and z-index tokens assign legal stacking layers. Together they answer the question layouts constantly ask — *what is floating above what, and how rounded is it* — with four shadows and five radii instead of forty ad-hoc box-shadows. Because depth is perceived relationally (a shadow only reads as altitude against the surfaces below it), these tokens only work as a shared scale: every component requesting altitude from the same ramp is what makes a dropdown feel "higher" than a card, rather than merely different.

## 2. Core Token Principles

- **Five radii cover all UI:** none, sm (4px), md (8px), lg (16px), full — control-like surfaces get sm/md, containers lg, pills full.
- **Elevation is a scale of altitude, not beauty:** each level means a specific interactivity class (resting card, hover lift, dropdown, modal, toast).
- **Shadows are soft, directional, and layered:** two stacked shadows (ambient + key) per level read more real than one heavy blur.
- **Radius is consistent across an altitude:** everything at elevation-2 shares the same radius family — mixed radii at one level look assembled.
- **Z-index is a closed enum, not an integer lottery:** named layers (dropdown 1000, modal 1050, toast 1100) prevent the 9999 arms race.
- **Dark mode changes shadow physics:** dark surfaces need stronger, more opaque shadows plus subtle borders — light-theme shadows vanish on dark backgrounds.
- **Elevation never substitutes for contrast:** a shadow does not make text readable (contrast-validation owns that).
- **Depth is requested, never improvised:** a component declares "I am a modal" and inherits elevation-4 + radius-lg; it never authors its own shadow string.

## 3. Token Set

| Role | Token | Value | Notes |
|---|---|---|---|
| Radius | `--dt-radius-none` | `0px` | Tables, full-bleed media, aligned grid edges |
| Radius | `--dt-radius-sm` | `4px` | Inputs, small buttons, chips |
| Radius | `--dt-radius-md` | `8px` | Buttons, dropdowns, cards in dense UI |
| Radius | `--dt-radius-lg` | `16px` | Modals, large cards, marketing surfaces |
| Radius | `--dt-radius-full` | `9999px` | Pills, avatars, FABs |
| Elevation | `--dt-elevation-1` | `0 1px 2px rgba(16,24,40,0.06), 0 1px 3px rgba(16,24,40,0.10)` | Resting cards, sticky headers |
| Elevation | `--dt-elevation-2` | `0 2px 4px rgba(16,24,40,0.06), 0 4px 8px rgba(16,24,40,0.10)` | Hover lift, popovers |
| Elevation | `--dt-elevation-3` | `0 4px 6px rgba(16,24,40,0.05), 0 12px 24px rgba(16,24,40,0.14)` | Dropdowns, command menus |
| Elevation | `--dt-elevation-4` | `0 8px 12px rgba(16,24,40,0.06), 0 24px 48px rgba(16,24,40,0.18)` | Modals, drawers |
| Z-index | `--dt-z-index-dropdown` | `1000` | Menus, selects, popovers |
| Z-index | `--dt-z-index-modal` | `1050` | Modals, drawers, sheets; toast sits above |

Consume them by linking `assets/css/radius-elevation.css` once at the app root, then referencing `var(--dt-elevation-2)`, `var(--dt-radius-md)`, and `var(--dt-z-index-dropdown)` in components. If a shadow or radius not in this table seems necessary, the surface is asking for an altitude or radius step that does not exist yet — raise it through the token scale, not a component-local value.

## 4. Composition & Layering

- Elevation composes with dark-mode tokens: dark themes re-map every shadow to stronger variants and add border aliases — the altitude meaning stays constant even though the physics change.
- Component tokens consume radius/elevation (component-modal-radius = radius-lg), keeping per-component values derived instead of forked.
- Radius tokens pair with spacing: inner padding should relate to outer radius (radius-md surfaces use space-3/space-4 padding) so corners never look cramped.
- Z-index layers sit above the altitude ramp: an element's shadow level describes its visual height, while its z-index token guarantees it actually stacks there — both come from this skill, never from ad-hoc integers.

## 5. Signature Patterns

- **Altitude contract:** document the meaning of each elevation level once; components request altitude, not raw shadows.
- **Hover = altitude delta:** interactive surfaces move up one elevation level on hover (elevation-1 to elevation-2), paired with the motion system's duration tokens.

## 6. Real-World Use Cases

- **Design systems defining a depth language** for cards, overlays, and floating UI.
- **Dark theme rollout:** re-mapping the shadow ramp for dark physics.
- **Taming z-index chaos:** replacing 9999-style stacking with a closed layer enum.

## 7. Combination Notes

### With other token skills

- **Pairs well with color-tokens, spacing-sizing, semantic-alias-naming, and dark-mode:** shadows read against the color surface beneath them, corners sit against the spacing rhythm, and dark mode re-maps this entire ramp — all four skills consume or extend the depth layer.
- **Pairs well with token-pipeline-figma, component-tokens, and governance-migration:** radius/elevation values flow through the same pipeline as every other tier, and component tokens derive their shadow from the altitude request rather than forking raw strings.
- **Caution with typography-tokens:** radius and elevation never modify text — the only interaction point is that elevated surfaces must still pass text contrast, which is not this skill's job to enforce.
- **Caution with multi-brand-theming:** a brand may want a radius personality (sharper corners), but that is a single alias-tier override (brand-radius-override), not a per-brand shadow redesign — altitude semantics must stay shared.
- **Caution with contrast-validation and platform-mapping:** shadows carry no contrast guarantee (pair them with borders per the accessibility notes), and elevation maps to different native paradigms (Material elevation, CALayer) — the altitude meaning must survive translation, not the raw shadow strings.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with claymorphism, neumorphism, and glassmorphism:** these are depth-first styles — they live or die on a disciplined shadow and radius ramp, which is exactly what this token set provides.
- **Caution with brutalism-ui and flat-design:** both may reject shadows entirely; if so, depth collapses to borders and background shifts at the alias tier — deviate consciously and document it rather than deleting the ramp.

### With motion skills (companion repo skill-animation)

- **Good affinity with feedback-confirmation and micro-interactions:** hover altitude deltas and overlay entrances are the classic consumers — a one-level elevation lift paired with a ~150-240ms duration token reads as physical, not decorative.
- **Caution with nothing, but coordinate:** the shadow change itself is instant in CSS; the perceived smoothness comes entirely from the motion tokens animating transform/opacity alongside it, so the two ramps must be paired at the component level.

## 8. Anti-Patterns

- **Shadow soup:** a unique box-shadow per component instead of four altitude levels
- **z-index lottery:** 99, 999, 9999 competing across codebases until one more zero "wins"
- **Mixed radii at one altitude:** 6px and 12px corners on the same level read as two different systems
- **Shadow-as-contrast:** using elevation to separate text from background instead of meeting WCAG 1.4.3

### Accessibility Notes

Depth must never carry meaning alone: an element indicated only by shadow is lost to users with shadows disabled or in flat/high-contrast modes, so every elevation level must be paired with a border or background change to satisfy WCAG 1.4.11 non-text contrast for visible boundaries. The fallback in `assets/css/radius-elevation.css` maps each elevation level to an explicit border under `forced-colors: active` and high-contrast overrides — box-shadow alone never delineates an interactive surface. Z-index discipline is also an accessibility concern: modals must trap focus above `--dt-z-index-modal`, toasts above that, and a closed enum is what makes those guarantees auditable.

## 9. Code Examples

### Example 1 — Card with hover altitude delta

Tokens: `assets/css/radius-elevation.css`

```html
<article class="card">
  <h3>Quarterly report</h3>
  <p>Revenue grew 12% quarter over quarter across all regions.</p>
  <button class="card-action">View details</button>
</article>
<style>
  .card {
    background: #fff;
    border: 1px solid #e4e7ec;              /* depth never rides on shadow alone */
    border-radius: var(--dt-radius-md);
    box-shadow: var(--dt-elevation-1);       /* resting altitude */
    padding: 24px;
    transition: box-shadow 240ms cubic-bezier(0.2, 0, 0, 1),
                transform 240ms cubic-bezier(0.2, 0, 0, 1);
  }
  .card:hover {
    box-shadow: var(--dt-elevation-2);       /* one altitude up on hover */
    transform: translateY(-1px);
  }
  .card h3 { margin: 0 0 8px; font: 600 16px/1.4 system-ui; }
  .card p  { margin: 0 0 16px; font: 14px/1.5 system-ui; color: #404040; }
  .card-action {
    border: 1px solid #d0d5dd; background: #fff; cursor: pointer;
    border-radius: var(--dt-radius-sm);      /* controls get sm, containers md */
    padding: 8px 12px; font: 500 14px system-ui;
  }
  .card-action:focus-visible { outline: 2px solid #1d4ed8; outline-offset: 2px; }
</style>
```

### Example 2 — Dropdown respecting the z-index enum

Tokens: `assets/css/radius-elevation.css`

```html
<div class="menu-wrap">
  <button class="trigger" aria-haspopup="menu" aria-expanded="false">Actions ▾</button>
  <ul class="menu" role="menu">
    <li role="menuitem">Rename</li>
    <li role="menuitem">Duplicate</li>
    <li role="menuitem">Archive</li>
  </ul>
</div>
<script>
  const wrap = document.querySelector('.menu-wrap');
  const btn = wrap.querySelector('.trigger');
  btn.addEventListener('click', () => {
    const open = wrap.classList.toggle('open');
    btn.setAttribute('aria-expanded', open);
  });
</script>
<style>
  .menu-wrap { position: relative; display: inline-block; font: 14px/1.4 system-ui; }
  .trigger {
    padding: 10px 16px; cursor: pointer;
    border: 1px solid #d0d5dd; border-radius: var(--dt-radius-sm); background: #fff;
  }
  .menu {
    position: absolute; top: calc(100% + 6px); left: 0; margin: 0; padding: 6px;
    list-style: none; min-width: 160px; display: none;
    background: #fff; border: 1px solid #e4e7ec;
    border-radius: var(--dt-radius-md);
    box-shadow: var(--dt-elevation-3);            /* dropdown altitude */
    z-index: var(--dt-z-index-dropdown);          /* closed enum, not 9999 */
  }
  .menu-wrap.open .menu { display: block; }
  .menu li { padding: 8px 12px; border-radius: var(--dt-radius-sm); cursor: pointer; }
  .menu li:hover { background: #f2f4f7; }
</style>
```

## 10. Implementation Checklist

- [ ] Every `box-shadow` in components is one of the four `--dt-elevation-*` tokens — zero bespoke shadow strings.
- [ ] Every `border-radius` is one of the five `--dt-radius-*` tokens; controls use sm/md, containers use lg.
- [ ] All stacking uses the `--dt-z-index-*` enum; a grep for `z-index: [0-9]` outside the token file returns nothing.
- [ ] Each elevation level is paired with a border or background change, not shadow alone.
- [ ] Hover lifts move exactly one altitude level (elevation-1 → elevation-2) with a motion-system duration.
- [ ] Surfaces at one altitude share a radius family — no mixed 6px/12px corners on the same level.
- [ ] Dark theme re-maps the elevation ramp to border-led variants and the alias re-pointing is verified.
- [ ] `forced-colors` fallback borders are present and verified with Windows High Contrast Mode.

---
name: semantic-alias-naming
description: The three-tier naming architecture — primitive, semantic alias, component — that lets themes swap values without code ever changing; the API every other token skill programs against.
tags: [naming, aliases, tokens, theming, architecture]
related: [color-tokens, dark-mode, component-tokens]
---

# Design Token Skill: Semantic & Alias Naming

## 1. Definition

Alias naming is the architecture that makes tokens themeable: primitives (`blue-500`) are referenced by semantic aliases (`color-action-primary`), which are referenced by component tokens (`component-button-bg`). Product code consumes only the top tiers, so switching light/dark, brand A to brand B, or default to high-contrast is a **re-pointing of aliases** — not a code change. Naming is therefore the highest-leverage decision in the whole system: it is the API every other token skill programs against, and a bad alias name, like a bad API name, propagates its confusion into every consumer until the only fix is a governed migration.

## 2. Core Token Principles

- **Three tiers, strict direction:** primitive → semantic alias → component; nothing references downward or sideways.
- **Name aliases by role and intent:** color-text-primary, color-bg-surface, color-action-primary — never by value or appearance.
- **One alias vocabulary across the product:** if a modal and a card both need a surface, they both use color-bg-surface; no modal-bg vs card-bg fork at the semantic tier.
- **Aliases encode state axes explicitly:** -hover, -pressed, -disabled are distinct tokens, not CSS-derived ad-hoc colors.
- **Feedback axes are closed:** success/warning/danger/info, each with bg/border/text roles — new meanings require a new axis decision, not a new one-off.
- **Rename with deprecation, never in place:** aliases are an API; governance-migration owns renames.
- **An alias that maps to nothing** (no primitive) **or a primitive consumed directly by code** are both contract violations.

## 3. Token Set

| Role | Token | Value | Notes |
|---|---|---|---|
| Background | `--dt-color-bg-default` | `var(--dt-color-neutral-0)` | Page background |
| Background | `--dt-color-bg-subtle` | `var(--dt-color-neutral-100)` | Wells, table stripes, code blocks |
| Background | `--dt-color-bg-inverse` | `var(--dt-color-neutral-900)` | Tooltips, dark surfaces on light theme |
| Text | `--dt-color-text-primary` | `var(--dt-color-neutral-900)` | Body and heading text |
| Text | `--dt-color-text-secondary` | `var(--dt-color-neutral-700)` | Meta, captions, inactive labels |
| Text | `--dt-color-text-on-action` | `var(--dt-color-neutral-0)` | Text/icons on filled actions |
| Border | `--dt-color-border-default` | `var(--dt-color-neutral-300)` | Inputs, card outlines, dividers |
| Action | `--dt-color-action-primary` | `var(--dt-color-brand-500)` | Primary buttons, links, active nav |
| Action state | `--dt-color-action-primary-hover` | `var(--dt-color-brand-600)` | Hover state axis; pressed maps to -600/700 |
| Feedback | `--dt-color-feedback-danger-text` | `var(--dt-color-danger-600)` | Error text; passes 4.5:1 where the raw 500 does not |
| Feedback | `--dt-color-feedback-success-bg` | `var(--dt-color-success-100)` | Success banner background tint |

Consume them by linking `assets/css/semantic-alias-naming.css` once at the app root, then referencing only `var(--dt-color-*)` aliases in product code — never `var(--dt-color-neutral-900)`-style primitives. Note that each alias value is itself a reference to a primitive: that indirection is the entire mechanism. If an alias's value is ever written as a raw hex, the tier separation has been broken.

## 4. Composition & Layering

- Alias tier is where cross-domain composition happens: dark-mode re-points aliases, multi-brand-theming overrides brand aliases, component-tokens consume aliases — each theme change is one tier deep.
- State axes (-hover, -pressed, -disabled) compose with the motion system: state changes animate with motion tokens, colors come from state aliases.
- The alias vocabulary is the lint target for governance: component code referencing primitives (var(--dt-color-neutral-900)) is a build failure, not a style nit.
- Alias names are theme-invariant while their values are theme-specific: the word "surface" survives every re-skin, which is precisely what lets components be written once.

## 5. Signature Patterns

- **Role-matrix review:** for each semantic role, write down bg/border/text/hover/pressed/disabled once; missing cells become tickets, not improvisations.
- **Alias-first design review:** designs expressed in primitives ("use blue-700 here") are rejected; they must state intent ("action-primary on inverse surface").

## 6. Real-World Use Cases

- **Any product preparing for theming:** dark mode, brands, or density — aliases are the prerequisite.
- **Component libraries:** components consume alias/component tiers only so they render correctly in every theme.
- **Cleaning up a legacy palette:** introducing the alias tier above existing primitives without breaking current code.

## 7. Combination Notes

### With other token skills

- **Pairs well with everything — literally:** this skill has no caution or avoid entries, because the alias tier is the shared vocabulary the other tiers speak; color-tokens feeds it primitives, dark-mode and multi-brand-theming re-point it, and component-tokens sit on top of it.
- **Pairs well with contrast-validation and governance-migration:** contrast pairings live at the alias tier (so one validation covers every consumer), and renames flow through governance precisely because aliases are an API.
- **Good with typography-tokens, spacing-sizing, and radius-elevation:** the same role/intent naming discipline extends beyond color — text-body, space-4, and radius-md are aliases in spirit, describing role rather than appearance.
- **Caution with none, but responsibility with all:** because every skill consumes this vocabulary, a rename here is a system-wide event — the reason renames are governed, never ad-hoc.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism and flat-design:** both styles thrive on small, tightly-named vocabularies where every value has one clear intent — exactly what a closed alias set enforces.
- **Caution with collage-art and maximalism:** these styles celebrate expressive, layered, and improvised surfaces; force their richness into the alias tier as new *roles* (reviewed axes), not as component-local one-offs that bypass the vocabulary.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** state axes are the meeting point — when a hover alias fires, the transition runs on motion duration/easing tokens while the color comes from the `-hover` alias; the two systems compose at the component without either knowing about the other.
- **Caution with none needed, but mirror the discipline:** motion's five-duration scale and this skill's closed feedback axes are the same architectural idea (few named steps, no one-offs) — keep the vocabularies symmetric so consumers can reason about both the same way.

## 8. Anti-Patterns

- **Two-tier collapse:** components consuming primitives directly, which makes theming a code-wide find-and-replace
- **Appearance-named aliases:** color-light-blue-button encodes value and usage and dies at the first rebrand
- **Alias explosion:** modal-bg, dialog-bg, sheet-bg as separate aliases instead of one shared surface role
- **Hidden state math:** deriving hover colors in CSS (filter: brightness) instead of declaring -hover aliases

### Accessibility Notes

The alias tier is where contrast is guaranteed: state aliases (-disabled, -on-action) must declare their ratio pairing (e.g. color-text-on-action on color-action-primary passes 4.5:1) so valid combinations are the only combinations. This is what makes accessibility systematic rather than per-component heroics — when the only way to render text is through a validated text-on-surface alias pair, an inaccessible combination cannot be assembled in the first place. The fallback is architectural, not cosmetic: if an alias pairing fails contrast, fix the alias mapping (choose different primitive steps) — never override the alias value in component code, which would silently fork the pairing for every other consumer.

## 9. Code Examples

### Example 1 — Components consuming only aliases

Tokens: `assets/css/semantic-alias-naming.css`

```html
<article class="alert alert-danger">
  <strong>Payment failed</strong>
  <p>Your card was declined. Update your billing details to retry.</p>
</article>
<style>
  .alert {
    display: flex; flex-direction: column; gap: 4px;
    padding: 16px;
    border-radius: 8px;
    background: var(--dt-color-feedback-success-bg, #DCFCE7); /* fallback shown; danger variant below */
  }
  /* The danger alert re-maps ONLY aliases — anatomy is identical */
  .alert-danger {
    background: #FEF2F2;
    border: 1px solid #FECACA;
  }
  .alert strong {
    font: 600 14px/1.4 system-ui;
    color: var(--dt-color-feedback-danger-text);  /* danger-600, 4.5:1-safe */
  }
  .alert p {
    margin: 0; font: 14px/1.5 system-ui;
    color: var(--dt-color-text-secondary);
  }
</style>
```

### Example 2 — Proof of themeability: swap aliases, keep the component

Tokens: `assets/css/semantic-alias-naming.css`

```html
<main class="page" data-theme="light">
  <section class="card">
    <h2>Alias tier in action</h2>
    <p>Toggle the theme — the component below never changes.</p>
    <button class="btn">Continue</button>
  </section>
</main>
<script>
  const page = document.querySelector('.page');
  document.querySelector('.btn').addEventListener('click', () => {
    const next = page.dataset.theme === 'light' ? 'dark' : 'light';
    page.dataset.theme = next; // aliases re-point; zero component code changes
  });
</script>
<style>
  /* Tier 2 — semantic aliases (values shown inline for standalone demo) */
  .page {
    --dt-color-bg-default: #FFFFFF; --dt-color-bg-surface: #F5F5F5;
    --dt-color-text-primary: #171717; --dt-color-text-secondary: #404040;
    --dt-color-action-primary: #2563EB; --dt-color-text-on-action: #FFFFFF;
  }
  .page[data-theme='dark'] {
    --dt-color-bg-default: #0A0A0A; --dt-color-bg-surface: #1C1C1E;
    --dt-color-text-primary: #FAFAFA; --dt-color-text-secondary: #A3A3A3;
    --dt-color-action-primary: #60A5FA; --dt-color-text-on-action: #0A0A0A;
  }
  /* Tier 3 — component consumes aliases only */
  .page { min-height: 120px; padding: 24px; background: var(--dt-color-bg-default); }
  .card {
    background: var(--dt-color-bg-surface); padding: 16px; border-radius: 8px;
    max-width: 320px;
  }
  .card h2 { margin: 0 0 4px; font: 600 16px/1.4 system-ui; color: var(--dt-color-text-primary); }
  .card p  { margin: 0 0 12px; font: 14px/1.5 system-ui; color: var(--dt-color-text-secondary); }
  .btn {
    border: 0; cursor: pointer; padding: 10px 16px; border-radius: 8px;
    background: var(--dt-color-action-primary); color: var(--dt-color-text-on-action);
    font: 500 14px system-ui;
  }
</style>
```

## 10. Implementation Checklist

- [ ] Product code references only `--dt-color-*` aliases — a lint rule fails the build on direct primitive usage.
- [ ] Every alias value is a `var()` reference to a primitive or another alias; no raw hexes at the alias tier.
- [ ] Names state role and intent (`-text-primary`, `-action-primary`), never value or appearance.
- [ ] Every interactive alias has explicit `-hover` / `-pressed` / `-disabled` tokens — no CSS-derived state math.
- [ ] The feedback axes (success/warning/danger/info) are closed, each with bg/border/text roles.
- [ ] Each alias pairing declares its contrast ratio; failing pairs fix the mapping, not the component.
- [ ] A role-matrix review has documented bg/border/text/hover/pressed/disabled for every semantic role.
- [ ] Renames flow through the deprecation process — no alias is renamed in place.

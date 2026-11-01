---
name: type-scale
description: A root-16px modular scale (ratio ~1.25) that covers body through display in 9 steps — hierarchy by stepping, never by improvising.
tags: [typography, type-scale, hierarchy, tokens, modular]
related: [font-pairing, line-height, letter-spacing]
---

# Typography Skill: Modular Type Scale

## 1. Definition

A modular type scale is a geometric progression of font sizes built from one base (16px) and one ratio (~1.25 major third): 16, 20, 25, 31, 39, 49... A closed scale means every hierarchy decision is 'step up or down' — never invent 17px or 22px. The scale is the contract between design and code: type tokens (skill-design-tokens guide 02) express it, and every text class steps along it. Because each step ships as a bundle (size + weight + line-height + tracking), the scale is not a list of numbers but a set of named text roles that product code consumes.

## 2. Core Principles

- **Root 16px, ratio 1.2–1.25:** 1.25 (major third) suits most products; 1.2 for dense UI, 1.333 for dramatic marketing.
- **9 steps cover everything:** body sits at step 0–1; display at 6–8 — if a design needs step 12, the ratio is wrong, not the count.
- **Size steps imply weight pairing:** each step ships with its weight and line-height as a bundle, never a naked size.
- **Smallest legible step is 12px:** below 12px, detail loss and x-height collapse hurt readability — captions floor here.
- **Scale in rem:** steps multiply with user font-size preferences (WCAG 1.4.4).
- **Display sizes get negative tracking:** as size grows, letter-spacing tightens (−0.01 to −0.03em) — see letter-spacing guide.
- **One scale for the whole product:** marketing pages may extend upward, never sideways into a second parallel scale.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Scale base | `--type-scale-base` | `1rem` | 16px body root; the scale's step 0 |
| Scale ratio | `--type-scale-ratio` | `1.25` | Major third; 1.2 dense, 1.333 dramatic |
| Size 2xs | `--type-size-2xs` | `0.75rem` | 12px captions/legal floor |
| Size xs | `--type-size-xs` | `0.875rem` | 14px secondary text |
| Size sm | `--type-size-sm` | `1rem` | 16px body default |
| Size md | `--type-size-md` | `1.25rem` | 20px lead/emphasis |
| Size lg | `--type-size-lg` | `1.563rem` | 25px h4/card titles |
| Size xl | `--type-size-xl` | `1.953rem` | 31px h3/section headers |
| Size 2xl | `--type-size-2xl` | `2.441rem` | 39px h2/page titles |
| Size 3xl | `--type-size-3xl` | `3.052rem` | 49px h1/hero |
| Size 4xl | `--type-size-4xl` | `3.815rem` | 61px marketing display (extends upward only) |

Consume them by linking `assets/css/type-scale.css` at the app root, then referencing `var(--type-size-*)` — or better, the role classes (`.text-body`, `.text-heading`, `.text-display`) that bundle size with weight, line-height, and tracking. Every rendered font-size in product code must resolve to one of these tokens; a raw `17px` or `22px` anywhere is a token violation caught in review.

## 4. Composition

- **The scale feeds typography tokens (skill-design-tokens guide 02):** sizes are rem values with paired weights and line-heights — the token tier is the typed expression of this ramp.
- **It composes with fluid-responsive:** heading steps interpolate via `clamp()` between two scale stops — the scale defines the stops, so fluidity never introduces off-scale sizes.
- **It composes with spacing tokens:** vertical rhythm snaps text blocks to the 4px grid via line-height + space tokens — the size ramp and the space ramp are tuned as one system.

## 5. Signature Patterns

- **Named text roles:** `.text-body` / `.text-heading` / `.text-display` bundle (size, weight, line-height, tracking) — consumers pick roles, not sizes, which makes hierarchy decisions portable across screens.
- **Step-up hierarchy check:** any screen where hierarchy needs more than 3 consecutive steps is restructured, not re-scaled — the closed ramp forces information architecture to stay honest.

## 6. Real-World Use Cases

- **Design systems defining their type ramp:** the scale IS the ramp — this skill is the single source of truth for every text size decision.
- **Auditing for off-scale sizes:** every 17px/22px found in production CSS is a token violation and a bug ticket.
- **Marketing vs product:** extending the same scale upward (size-4xl) for display rather than forking scales — one ramp serves both surfaces.

## 7. Combination Notes

### With other typography skills

- **Pairs naturally with font-pairing and line-height:** the pairing decides which families the scale applies to; line-height is bundled into every step so size and leading are reviewed together, never tuned independently.
- **Pairs with letter-spacing, visual-hierarchy, and fluid-responsive:** tracking tightens per step, hierarchy consumes the steps as ranks, and fluid type interpolates between stops — all three depend on the ramp being closed.
- **Caution/avoid list is empty:** every sibling skill builds on the scale; incompatibility is only possible by bypassing it (off-scale values).

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism, flat-design, and class-morphism:** these styles lean on a disciplined size ramp where whitespace and weight carry hierarchy — a closed 9-step scale is exactly their tool.
- **Caution with collage-art:** collage aesthetics may want jarring, arbitrary type sizes as a deliberate device; if so, deviate consciously in a documented style exception — never by adding parallel scale tokens to the system.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** entrance animations that scale text (fade-up on headings) should interpolate between two scale stops, not arbitrary pixel values — the scale provides the animation's keyframe endpoints.
- **Caution/avoid list is empty:** no motion discipline conflicts with the scale; count-up and data animations just require tabular figures, which is a sibling concern.

## 8. Anti-Patterns

- **Off-scale sizes** — 17px and 22px one-offs that quietly dissolve the scale
- **Ratio perfectionism** — forcing 1.618 everywhere and getting display sizes too big for real UI
- **Naked sizes** — shipping size tokens without weight/line-height pairing - hierarchy fragments
- **Parallel scales** — product and marketing type systems that share nothing and drift forever

### Accessibility Notes

A rem-based scale is the WCAG 1.4.4 guarantee: the whole hierarchy multiplies with user font-size settings, so zooming or raising the browser's default text size scales every step proportionally — hierarchy survives because relationships, not absolutes, are encoded. The 12px floor keeps small text legible even when the scale is used at its smallest step. The fallback rule: if a display step overflows containers at 200% zoom, allow wrapping (never shrink the step) and check the fluid-responsive clamp bounds — aesthetics yield to user scaling every time.

## 9. Code Examples

### Example 1 — The full ramp rendered

Tokens: `assets/css/type-scale.css`

```html
<div class="ramp-demo">
  <h2 class="ramp-title">The 1.25 Major-Third Ramp</h2>
  <div class="ramp-step ramp-4xl">4xl — 3.815rem (61px)</div>
  <div class="ramp-step ramp-3xl">3xl — 3.052rem (49px)</div>
  <div class="ramp-step ramp-2xl">2xl — 2.441rem (39px)</div>
  <div class="ramp-step ramp-xl">xl — 1.953rem (31px)</div>
  <div class="ramp-step ramp-lg">lg — 1.563rem (25px)</div>
  <div class="ramp-step ramp-md">md — 1.25rem (20px)</div>
  <div class="ramp-step ramp-sm">sm — 1rem (16px) — body default</div>
  <div class="ramp-step ramp-xs">xs — 0.875rem (14px)</div>
  <div class="ramp-step ramp-2xs">2xs — 0.75rem (12px) — floor</div>
</div>
<style>
  .ramp-demo { font-family: var(--type-font-text, system-ui, sans-serif); max-width: 720px; margin: 32px auto; padding: 24px; }
  .ramp-title { font-size: var(--type-size-xl); font-weight: 600; margin: 0 0 24px; color: #111827; }
  .ramp-step { margin: 0 0 12px; padding-bottom: 12px; border-bottom: 1px solid #F3F4F6; color: #111827; }
  .ramp-4xl { font-size: var(--type-size-4xl); font-weight: 700; letter-spacing: -0.03em; line-height: 1.1; }
  .ramp-3xl { font-size: var(--type-size-3xl); font-weight: 700; letter-spacing: -0.025em; line-height: 1.1; }
  .ramp-2xl { font-size: var(--type-size-2xl); font-weight: 600; letter-spacing: -0.02em; line-height: 1.2; }
  .ramp-xl  { font-size: var(--type-size-xl);  font-weight: 600; letter-spacing: -0.02em; line-height: 1.2; }
  .ramp-lg  { font-size: var(--type-size-lg);  font-weight: 600; letter-spacing: -0.01em; line-height: 1.25; }
  .ramp-md  { font-size: var(--type-size-md);  font-weight: 600; line-height: 1.35; }
  .ramp-sm  { font-size: var(--type-size-sm);  font-weight: 400; line-height: 1.5; }
  .ramp-xs  { font-size: var(--type-size-xs);  font-weight: 400; line-height: 1.5; color: #374151; }
  .ramp-2xs { font-size: var(--type-size-2xs); font-weight: 400; line-height: 1.5; color: #6B7280; }
</style>
```

### Example 2 — Text-role classes (the consumer API)

Tokens: `assets/css/type-scale.css`

```html
<article class="role-demo">
  <h1 class="text-display">Quarterly platform report</h1>
  <p class="text-lead">Shipping velocity is up 34% while incident load dropped to a record low.</p>
  <h2 class="text-heading">Highlights</h2>
  <p class="text-body">The design system shipped 12 new components this quarter. Adoption reached 87% of product surfaces, up from 61% last quarter. Check out the <code class="text-mono">--type-size-*</code> ramp in the tokens package.</p>
  <p class="text-meta">Updated Nov 2026 · 4 min read</p>
</article>
<style>
  .role-demo { font-family: var(--type-font-text, system-ui, sans-serif); max-width: 65ch; margin: 0 auto; padding: 40px 24px; color: #111827; }
  .text-display { font-size: var(--type-size-3xl); font-weight: 700; letter-spacing: -0.025em; line-height: 1.1; margin: 0 0 16px; }
  .text-lead    { font-size: var(--type-size-md);  font-weight: 400; line-height: 1.5; color: #374151; margin: 0 0 32px; }
  .text-heading { font-size: var(--type-size-lg);  font-weight: 600; letter-spacing: -0.01em; line-height: 1.25; margin: 32px 0 8px; }
  .text-body    { font-size: var(--type-size-sm);  font-weight: 400; line-height: 1.5; margin: 0 0 16px; }
  .text-meta    { font-size: var(--type-size-xs);  font-weight: 400; line-height: 1.5; color: #6B7280; }
  .text-mono    { font-family: var(--type-font-mono, ui-monospace, monospace); font-size: 0.875em; background: #F3F4F6; padding: 2px 6px; border-radius: 4px; }
</style>
```

## 10. Implementation Checklist

- [ ] Every rendered font-size in product CSS resolves to a `var(--type-size-*)` token — zero raw px values outside the ramp.
- [ ] All size tokens are declared in `rem` so the hierarchy multiplies with user font-size preferences (WCAG 1.4.4).
- [ ] Each scale step ships as a bundled role: size + weight + line-height (+ tracking for display steps) — no naked sizes.
- [ ] The 12px floor holds: `--type-size-2xs` is the smallest rendered text, used only for captions/legal.
- [ ] Marketing display sizes extend upward only (`--type-size-4xl`) — no parallel second scale exists anywhere.
- [ ] Any screen needing more than 3 consecutive scale steps is restructured in review, not re-scaled.
- [ ] Fluid interpolation (if used) clamps strictly between two `--type-size-*` stops — endpoints are scale steps.
- [ ] Off-scale values (17px, 22px, …) are caught by lint or CI diff against the token set before merge.

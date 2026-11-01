---
name: illustration-direction
description: Defining the illustration language — purpose matrix, style lock-up with brand, color discipline, and consistency across artists.
tags: [illustration, art-direction, brand, consistency, style-spec]
related: [empty-error-illustrations, mascot-character, icon-style-selection]
---

# Visual Asset Guide: Illustration Direction

## 1. Definition

Illustrations are brand moments inside product UI: onboarding heroes, empty states, success celebrations. This guide covers the direction work that turns individual drawings into a system: the purpose matrix (where illustration earns its place vs where it is noise), style definition (line weight, palette limits, character rules) locked to the brand, color discipline (illustration consumes brand/semantic ramps, not free palettes), and the consistency system — templates, component libraries, and review — that keeps multiple artists producing one language. Without direction, illustration accumulates as one-off assets; with it, a new artist can ship on-language work on day one.

## 2. Core Principles

- **Illustration has a purpose matrix:** orient (onboarding), explain (concepts), reward (success), humanize (empty states) — decoration without purpose is noise.
- **Style is defined, not felt:** line weight, palette, character proportions, and level of detail documented as the illustration spec.
- **The style locks to the brand:** illustration personality matches the design style (styleAffinity) — playful products get playful lines.
- **Color discipline:** illustrations consume the brand ramp + a defined illustration palette — never free hex choices that drift from tokens.
- **One character system:** mascots and people follow proportion rules (head counts, features) — character drift is style drift.
- **Scene templates enforce consistency:** backgrounds, ground shadows, and framing are reusable components, not redrawn per illustration.
- **Detail scales with display size:** hero illustrations carry detail; 120px spots stay simple — the detail budget is part of the spec.
- **The library is curated:** approved illustrations live in a versioned library with usage notes — ad-hoc art dropped into products is banned.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Purpose matrix | `--icon-purpose-matrix` | `orient,explain,reward,humanize` | Illustration must serve one |
| Illustration spec | `--icon-illustration-spec` | `line+palette+character+lod` | The documented style contract |
| Style-brand lock | `--icon-style-brand-lock` | `matches-design-style` | Illustration mirrors product personality |
| Color discipline | `--icon-color-discipline` | `brand-ramp+palette-limits` | No free hex in artwork |
| Character proportions | `--icon-character-proportions` | `documented-rules` | One character system |
| Scene templates | `--icon-scene-templates` | `reusable-components` | Framing/shadows not redrawn |
| Detail budget | `--icon-detail-budget` | `scales-with-size` | Spots simple; heroes detailed |
| Illustration library | `--icon-illustration-library` | `versioned+curated` | Approved art only |
| Usage notes | `--icon-usage-notes` | `per-illustration` | Where/how each asset is used |
| Export format | `--icon-export-format` | `svg+lottie-as-needed` | Vector first; animation opt-in |

Consume them by linking `assets/css/illustration-direction.css` at the app root and driving all artwork color through `var(--icon-...)` CSS custom properties — illustration fills reference the same custom properties the token tier defines, so a brand re-map re-colors the entire illustration library without touching a single source file. The non-paintable tokens (purpose matrix, curation, usage notes) are enforced in the library's submission checklist and design review, exactly like other governance tokens.

## 4. Composition

- **Composes with empty-error-illustrations (guide 07):** the most common illustration surface — the slot contracts there are drawn under this guide's spec, sharing style, palette, and template kit.
- **Composes with skill-color-theory:** illustration palettes are audited against brand ramps and contrast models, keeping artwork legible on real surfaces rather than only in the artboard.
- **Composes with skill-ui-ux styles:** illustration is where design styles express most strongly — styleAffinity records the direction, and the illustration spec cites it explicitly.

## 5. Signature Patterns

- **The illustration spec + template kit:** one style spec document plus reusable scene components — new artists produce on-language work without supervision, because the decisions are pre-made.
- **The curation pipeline:** artists submit to the library, a design review checks spec adherence, approved assets are versioned with usage notes — nothing ships from a DM or a desktop folder.

## 6. Real-World Use Cases

- **Brand-forward products building an illustration system from zero** — the spec, palette contract, and template kit are the founding documents.
- **Multi-artist teams needing one visual language** — freelancers, agencies, and in-house artists producing under one reviewed spec.
- **Audit:** style drift, off-token colors, purposeless decorative art — the three symptoms of a system running on taste instead of direction.

## 7. Combination Notes

### With other icons-illustration skills

- **Pairs naturally with empty-error-illustrations and mascot-character:** empty/error slots are the highest-traffic illustration surfaces and the mascot is the character system inside this spec — both consume the spec and template kit directly.
- **Pairs with icon-style-selection and icon-grid-sizing (with caution):** icon style and illustration style are adjacent contracts that must feel like one family, but they are governed by different specs — never force illustration detail onto the icon grid or vice versa; the caution is a boundary, not a conflict.
- **Pairs with svg-optimization and animation-integration:** exported artwork is optimized (vector first, `--icon-export-format`) and Lottie usage is opt-in per the same token.
- **Pairs with icon-library-management, icon-usability, accessible-icons, favicon-app-icons, and icon-system-audit:** the curated illustration library follows the library-management model, illustrations obey the accessibility naming/hidden contract, and the audit checks style drift alongside icon drift.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with collage-art, maximalism, and retro:** expressive styles are where illustration carries the most brand weight — layered textures, rich palettes, and era-specific line work all reward a strong documented spec, because the style is complex enough that drift is visible immediately.
- **Caution with minimalism:** in a minimalist product, illustration is a deliberate contrast moment — keep it rare, restrained, and explicitly justified in the purpose matrix, or the art fights the style instead of expressing it.

### With motion skills (companion repo skill-animation)

- **Good affinity with illustration-lottie:** vector illustration is the natural source for Lottie; `--icon-export-format: svg+lottie-as-needed` makes animation an opt-in export decision, not a rebuild.
- **Good affinity with ambient-motion:** hero illustrations can carry gentle ambient loops (floating shapes, breathing characters) — as long as the loop is subordinate to the scene and respects reduced-motion from the a11y contract.

## 8. Anti-Patterns

- **Style drift** — three artists, three visual languages, one product
- **Off-token color** — artwork in hex values that exist nowhere in the system
- **Decoration without purpose** — hero art slowing pages where no message is served
- **Character chaos** — the mascot's proportions changing per artist

### Accessibility Notes

Illustrations are WCAG 1.1.1 surface: informative illustrations get text alternatives (adjacent copy or aria), decorative ones are hidden — and animation on illustrations must respect reduced-motion (a11y repo media-alt-text + skill-animation guide 12). In practice this means every illustration entering the library carries a classification (informative or decorative) in its usage notes, so the alt decision is made at curation time rather than per-implementation, and any Lottie export ships alongside a static fallback for users with reduced motion. The fallback rule: if per-illustration alt copy is missing, ensure every illustration is paired with adjacent explanatory text — the pairing satisfies 1.1.1 even with an empty alt.

## 9. Code Examples

### Example 1 — Purpose-matrix gallery with CSS-variable fills

Tokens: `assets/css/illustration-direction.css`

```html
<section class="matrix" aria-label="Illustration purpose matrix">
  <figure class="spot" data-purpose="orient">
    <svg class="art" viewBox="0 0 120 80" aria-hidden="true" focusable="false">
      <rect x="18" y="14" width="84" height="52" rx="6" class="s1"/>
      <path d="M18 52 44 32l20 14 18-10 20 16v8H18z" class="s2"/>
      <circle cx="86" cy="26" r="7" class="s2"/>
    </svg>
    <figcaption><strong>Orient</strong> — onboarding heroes</figcaption>
  </figure>
  <figure class="spot" data-purpose="explain">
    <svg class="art" viewBox="0 0 120 80" aria-hidden="true" focusable="false">
      <circle cx="38" cy="40" r="16" class="s2"/>
      <path d="M64 24h38v6H64zm0 14h30v6H64zm0 14h22v6H64z" class="s1"/>
    </svg>
    <figcaption><strong>Explain</strong> — concept diagrams</figcaption>
  </figure>
  <figure class="spot" data-purpose="reward">
    <svg class="art" viewBox="0 0 120 80" aria-hidden="true" focusable="false">
      <path d="M60 12 71 36l26 3-19 18 5 26-23-13-23 13 5-26-19-18 26-3z" class="s2"/>
    </svg>
    <figcaption><strong>Reward</strong> — success moments</figcaption>
  </figure>
  <figure class="spot" data-purpose="humanize">
    <svg class="art" viewBox="0 0 120 80" aria-hidden="true" focusable="false">
      <circle cx="60" cy="30" r="14" class="s2"/>
      <path d="M32 70c4-14 15-20 28-20s24 6 28 20z" class="s1"/>
    </svg>
    <figcaption><strong>Humanize</strong> — empty states</figcaption>
  </figure>
</section>
<style>
  .matrix { display: flex; flex-wrap: wrap; gap: var(--icon-target-spacing, 8px); font: 13px/1.4 system-ui, sans-serif; }
  .spot { margin: 0; padding: 12px; width: 150px; border: 1px solid #e5e5e5; border-radius: 8px; }
  .art { display: block; width: 100%; height: auto; }
  .art .s1 { fill: var(--ill-primary, #2563eb); }   /* --icon-color-discipline: brand ramp only */
  .art .s2 { fill: var(--ill-secondary, #93c5fd); }
  figcaption { margin-top: 8px; color: #404040; }
  /* Detail budget: hero art may add texture; these 120px-class spots stay simple */
</style>
```

### Example 2 — Scene templates: reusable background + shadow components

```html
<div class="scenes">
  <figure class="scene">
    <svg class="art" viewBox="0 0 200 120" aria-hidden="true" focusable="false">
      <rect class="tpl-bg" x="0" y="0" width="200" height="120" rx="8"/>
      <ellipse class="tpl-shadow" cx="100" cy="102" rx="52" ry="7"/>
      <rect x="72" y="34" width="56" height="56" rx="10" class="s1"/>
      <path d="M86 62h28M100 48v28" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
    </svg>
    <figcaption>Empty workspace — template bg + shadow, new subject</figcaption>
  </figure>
  <figure class="scene">
    <svg class="art" viewBox="0 0 200 120" aria-hidden="true" focusable="false">
      <rect class="tpl-bg" x="0" y="0" width="200" height="120" rx="8"/>
      <ellipse class="tpl-shadow" cx="100" cy="102" rx="52" ry="7"/>
      <circle cx="100" cy="60" r="30" class="s1"/>
      <path d="M88 62h24" stroke="#fff" stroke-width="6" stroke-linecap="round"/>
    </svg>
    <figcaption>Deleted record — same template, different subject</figcaption>
  </figure>
</div>
<style>
  .scenes { display: flex; gap: 16px; flex-wrap: wrap; font: 13px/1.4 system-ui, sans-serif; }
  .scene { margin: 0; width: 220px; }
  .art { display: block; width: 100%; height: auto; }
  /* Scene template components: background and shadow are shared, never redrawn */
  .art .tpl-bg { fill: var(--ill-bg, #f5f5f5); }
  .art .tpl-shadow { fill: var(--ill-shadow, #e5e5e5); }
  .art .s1 { fill: var(--ill-primary, #2563eb); }
  figcaption { margin-top: 8px; color: #404040; }
</style>
```

## 10. Implementation Checklist

- [ ] Every illustration in the product serves one purpose from `--icon-purpose-matrix` (orient/explain/reward/humanize) — purposeless decoration is removed.
- [ ] The illustration spec (`--icon-illustration-spec`) documents line weight, palette, character rules, and detail budget, and cites the locked design style (`--icon-style-brand-lock`).
- [ ] All artwork color resolves through `var(--icon-...)` / brand-ramp custom properties (`--icon-color-discipline`) — zero free hex in any source file.
- [ ] Characters follow the documented proportion rules (`--icon-character-proportions`); new character work is reviewed against them.
- [ ] Backgrounds, shadows, and framing come from shared scene-template components (`--icon-scene-templates`), not per-illustration redraws.
- [ ] Detail scales with display size (`--icon-detail-budget`): spots stay simple, heroes may carry texture.
- [ ] Approved art lives in the versioned, curated library (`--icon-illustration-library`) with per-illustration usage notes (`--icon-usage-notes`).
- [ ] Exports are SVG-first with Lottie only as needed (`--icon-export-format`), and each asset records informative-vs-decorative for the 1.1.1 decision.

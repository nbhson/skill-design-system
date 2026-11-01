---
name: icon-library-management
description: The pipeline: naming conventions, source-of-truth files, versioning, contribution workflow, and pruning dead icons.
tags: [icons, library, pipeline, versioning, governance]
related: [icon-style-selection, icon-grid-sizing, icon-system-audit]
---

# Visual Asset Guide: Icon Library Management

## 1. Definition

Icons rot without a pipeline: duplicate names, stale exports, and dead glyphs accumulate. This guide covers the library mechanics: naming conventions (category-action, kebab-case), the source of truth (Figma/SVG masters, single source), export automation (SVGO + component generation), versioning (semver for icon families), the contribution workflow (grid check, style check, review), and pruning (usage-based dead icon removal). The library is the enforcement point for everything guides 01 and 02 decide: a beautiful spec sheet nobody gates on becomes folklore within two quarters, while a gated pipeline makes the right icon the easy icon.

## 2. Core Principles

- **Names are category-action:** 'chart-bar', 'user-plus' — predictable names are findable names; numbered exports ('icon_24') are banned.
- **One source of truth:** masters live in one repo/library; product teams consume generated assets — never hand-copied SVGs.
- **Exports are automated:** SVGO-optimized SVGs + framework components generated from masters — manual export steps are where drift is born.
- **Versioning is semver for the family:** added icons = minor; renamed/removed = major; restyled = major (visual contract).
- **Contribution is gated:** new icons pass grid + style + a11y review before merge — the library only grows through the pipeline.
- **Usage is tracked:** icon usage dashboards (or build-time scans) feed pruning decisions — dead icons get one deprecation cycle then removal.
- **Deprecation is visible:** deprecated icons are flagged in docs and lint warnings — silent removal breaks builds; silent decay breaks trust.
- **Search beats memory:** the library is searchable by name, keyword, and category — if contributors cannot find an icon, they will draw a duplicate.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Naming convention | `--icon-naming-convention` | `category-action-kebab` | 'chart-bar', 'user-plus' |
| Source of truth | `--icon-source-of-truth` | `single-library` | No hand-copied SVGs |
| Export pipeline | `--icon-export-pipeline` | `svgo+components-generated` | Automated from masters |
| Versioning | `--icon-versioning` | `semver` | Restyle = major (visual contract) |
| Contribution gate | `--icon-contribution-gate` | `grid+style+a11y-review` | Growth only via pipeline |
| Usage tracking | `--icon-usage-tracking` | `build-scan+dashboard` | Feeds pruning |
| Deprecation policy | `--icon-deprecation-policy` | `one-cycle-then-remove` | Flagged, linted, then gone |
| Search discovery | `--icon-search-discovery` | `name+keyword+category` | Findable beats duplicatable |
| Library docs | `--icon-library-docs` | `browsable-gallery` | Live preview per icon |
| Duplicate check | `--icon-duplicate-check` | `pre-merge` | New icons checked against existing |

Consume these by linking `assets/css/icon-library-management.css` once at the app root, then referencing `var(--icon-...)` from generated components — sizing and color props resolve to token-based values (`--icon-size-ramp` steps, design-token aliases), so a version bump re-themes every consumer without touching artwork. The contract tokens drive CI: the naming linter reads `--icon-naming-convention`, and the deprecation lint reads `--icon-deprecation-policy`.

## 4. Composition

- **Composes with icon-grid-sizing + icon-style-selection:** the contribution gate enforces both contracts — a glyph that fails the keyline overlay or deviates from the spec sheet does not merge, which is the only mechanism that keeps the family pure as contributors rotate.
- **Composes with icon-system-audit (guide 12):** usage tracking and audit findings share the same data — the build scan that prunes dead icons is the same artifact that measures drift, orphan exports, and naming violations.
- **Composes with skill-design-tokens:** generated components consume token-based sizing/color props — a `size` prop accepts only ramp values and a `color` prop only alias tokens, keeping the library theme-safe by construction.

## 5. Signature Patterns

- **The generate-don't-copy pipeline:** masters in, optimized SVGs + components out — CI regenerates on merge so consumers always match masters. Hand-copying an SVG into a product folder is the drift event the whole system exists to prevent; the pipeline makes the generated path the fastest path.
- **The usage-scan prune:** quarterly build scans list unused icons; maintainers deprecate with a removal date — the library stays lean. Deprecation is announced in docs, flagged by lint, and enforced one cycle later, so consumers always have an escape hatch before the breaking release.

## 6. Real-World Use Cases

- **Design systems shipping icon libraries to multiple codebases** — generated React/Vue/Svelte components from one master set, versioned independently of the apps.
- **Multi-brand setups with family variants (filled/outline per brand)** — one pipeline, per-brand variant outputs, shared masters.
- **Audit: hand-copied SVG drift, unversioned restyles, dead-icon bloat** — diffing product folders against library exports and the usage dashboard.

## 7. Combination Notes

### With other icons-illustration skills

- **Pairs naturally with icon-style-selection (guide 01) and icon-grid-sizing (guide 02):** the contribution gate is where their contracts become merge checks — style spec sheet and keyline overlay run automatically, so the family survives contributors who never read the docs.
- **Pairs with icon-usability, accessible-icons, and svg-optimization:** the gate includes recognition testing for novel glyphs, generated components ship with the aria contract pre-wired, and SVGO runs inside the pipeline rather than as an afterthought.
- **Pairs with icon-system-audit, animation-integration, favicon-app-icons, empty-error-illustrations, illustration-direction, and mascot-character:** audits consume the usage data; animated, app-icon, and illustration assets flow through the same single-source, versioned, generated pipeline.
- **No caution list:** library mechanics are orthogonal to how glyphs look or move — every icon-producing skill gets stronger behind a gated pipeline.
- **No avoid list:** the pipeline conflicts with nothing; bypassing it (hand-copied SVGs) is the anti-pattern, not a partner skill.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** simple geometric families generate and optimize cleanly (small SVG payloads, predictable component APIs), and token-based sizing/color props align with the disciplined token culture these styles demand.
- **No caution list:** expressive styles change the artwork content, not the library mechanics — a maximalist family still benefits from category-action names, semver, and CI-generated components; only the visual spec sheet differs.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** generated icon components expose motion through shared duration/easing tokens rather than baked-in CSS, so an icon family version bump never silently changes animation feel — motion lives in the token tier, artwork in the library.

## 8. Anti-Patterns

- **Hand-copied drift** — product folders holding mutated copies of library SVGs
- **Numbered-export names** — 'icon_24_new_final' as the naming system
- **Silent removal** — icons deleted with no deprecation cycle, breaking builds
- **Bloat-by-duplicate** — five search icons because nobody could find the first four

### Accessibility Notes

The library bakes in accessibility: icons ship with accessible-name props (or aria-hidden for decorative use) documented per icon — the a11y contract is part of the generated component, not a downstream responsibility. Because the pipeline generates the component wrapper, the aria attributes, focus-ring contract, and contrast notes from guides 01/02 land in every consumer automatically; a product team that forgets accessibility still ships it. The fallback: if generated components are not in place, ship a documented naming + usage guide with the SVGs and enforce the aria contract in code review — the contract matters more than the tooling.

## 9. Code Examples

### Example 1 — Browsable, searchable icon gallery (category-action names)

```html
<div class="gallery">
  <input class="search" type="search" placeholder="Search icons…" aria-label="Search icons">
  <ul class="grid" id="grid"></ul>
</div>
<script>
  const ICONS = [
    { name: 'chart-bar',  category: 'data',   body: '<rect x="4" y="12" width="4" height="8"/><rect x="10" y="8" width="4" height="12"/><rect x="16" y="4" width="4" height="16"/>' },
    { name: 'user-plus',  category: 'people', body: '<circle cx="10" cy="8" r="4"/><path d="M3 21c1.5-4 4-6 7-6s5.5 2 7 6"/><path d="M19 8v6M16 11h6"/>' },
    { name: 'file-copy',  category: 'files',  body: '<rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h2"/>' },
    { name: 'trash-delete', category: 'actions', body: '<path d="M4 7h16M9 7V5h6v2M6 7l1 14h10l1-14"/><path d="M10 11v6M14 11v6"/>' },
    { name: 'search-zoom', category: 'actions', body: '<circle cx="11" cy="11" r="6"/><path d="m20 20-4.5-4.5"/>' }
  ];
  const grid = document.getElementById('grid');
  const render = (q = '') => {
    grid.innerHTML = '';
    for (const ic of ICONS.filter(i => (i.name + ' ' + i.category).includes(q))) {
      const li = document.createElement('li');
      li.className = 'cell';
      li.innerHTML = `<svg viewBox="0 0 24 24" role="img" aria-label="${ic.name} icon">${ic.body}</svg><code>${ic.name}</code>`;
      grid.append(li);
    }
  };
  document.querySelector('.search').addEventListener('input', e => render(e.target.value));
  render();
</script>
<style>
  :root {
    /* Mirror of assets/css/icon-library-management.css */
    --icon-naming-convention: category-action-kebab;
    --icon-size-ramp: 16, 20, 24, 32, 48;
  }
  .gallery { width: max-content; padding: 16px; border: 1px solid #e5e5e5; border-radius: 10px; font: 13px/1.4 Inter, system-ui, sans-serif; }
  .search { width: 240px; padding: 8px 12px; border: 1px solid #d4d4d4; border-radius: 8px; margin-bottom: 12px; }
  .grid { display: flex; flex-wrap: wrap; gap: 12px; margin: 0; padding: 0; list-style: none; }
  .cell { width: 88px; padding: 10px 4px; display: grid; justify-items: center; gap: 6px; border: 1px solid #f0f0f0; border-radius: 8px; }
  .cell svg { width: 24px; height: 24px; fill: none; stroke: #2563EB; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
  .cell:first-child svg { fill: #2563EB; stroke: none; } /* chart-bar ships as a filled glyph */
  code { font-size: 11px; color: #404040; }
</style>
```

### Example 2 — Deprecation demo: lint-style warning + replacement pointer

```html
<div class="entry is-deprecated" role="note">
  <div class="preview">
    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M9 7V5h6v2M6 7l1 14h10l1-14"/></svg>
  </div>
  <div class="meta">
    <code>trash</code>
    <span class="flag">⚠ deprecated since v3.2 — remove in v4.0</span>
    <span class="lint">icon-lint: use <code>trash-delete</code> (category-action naming)</span>
  </div>
</div>
<style>
  :root {
    /* Mirror of assets/css/icon-library-management.css */
    --icon-deprecation-policy: one-cycle-then-remove;
  }
  .entry { display: flex; gap: 12px; align-items: flex-start; width: max-content; padding: 12px 16px; border: 1px solid #FDE68A; border-left: 4px solid #F59E0B; border-radius: 10px; background: #FFFBEB; font: 13px/1.5 Inter, system-ui, sans-serif; }
  .preview svg { width: 32px; height: 32px; fill: none; stroke: #A16207; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; opacity: 0.6; }
  .meta { display: grid; gap: 2px; }
  .meta code { color: #404040; }
  .flag { color: #92400E; font-weight: 600; }
  .lint { color: #737373; font-size: 12px; }
  .lint code { color: #2563EB; }
</style>
```

## 10. Implementation Checklist

- [ ] All icon names follow `category-action-kebab` (`--icon-naming-convention`); numbered exports are rejected by lint.
- [ ] Masters live in one library (`--icon-source-of-truth`); zero hand-copied SVGs exist in product folders.
- [ ] CI generates SVGO-optimized SVGs + framework components on merge (`--icon-export-pipeline`); no manual export steps.
- [ ] Releases follow semver (`--icon-versioning`): adds = minor, renames/removals/restyles = major.
- [ ] Every contribution passes the grid + style + a11y gate (`--icon-contribution-gate`) with a pre-merge duplicate check.
- [ ] Usage scans run quarterly (`--icon-usage-tracking`); dead icons get one flagged deprecation cycle, then removal.
- [ ] Deprecated icons are visibly flagged in the browsable gallery (`--icon-library-docs`) and by lint, with replacement pointers.
- [ ] Generated components consume token-based sizing/color via `var(--icon-...)` and ship with the aria contract pre-wired.

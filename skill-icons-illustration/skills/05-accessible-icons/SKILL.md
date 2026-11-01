---
name: accessible-icons
description: The aria contract — accessible names for functional icons, aria-hidden for decorative ones, and contrast that survives WCAG 1.4.11.
tags: [icons, accessibility, aria, contrast, wcag]
related: [icon-usability, icon-library-management, svg-optimization]
---

# Visual Asset Guide: Accessible Icons

## 1. Definition

Icons are invisible to screen readers unless named, and invisible to low-vision users unless contrasted. This guide covers the aria contract that makes every icon survivable in an assistive-technology tree: functional icons carry accessible names (aria-label or visible text), decorative icons are explicitly hidden (aria-hidden, focusable=false), icon buttons are real buttons with names, and meaningful icon graphics meet WCAG 1.4.11's 3:1 contrast against adjacent colors. The decision rule is a single question asked per icon instance: does the icon carry information? Name it. Is it decoration? Hide it. Never an unnamed interactive icon — that combination is the highest-severity accessibility failure an icon can produce.

## 2. Core Principles

- **Functional icons are named:** aria-label minimum ("Search"), visible text preferred ("Search" beside the glyph).
- **Decorative icons are hidden:** aria-hidden="true" + focusable="false" — decoration must never enter the AT tree or tab order.
- **Icon buttons are real buttons:** `<button aria-label="...">` — never a clickable div with a background-image glyph.
- **3:1 contrast for meaningful graphics:** icons that carry information meet WCAG 1.4.11 against adjacent colors — including state changes.
- **Names are human phrases, not icon names:** "Delete file", not "trash-can-2" — the aria-label is the same string the tooltip shows.
- **State changes are named:** favorite toggles announce state ("Remove from favorites" vs "Add to favorites") — static names lie about toggles.
- **Icon fonts are legacy:** they inject junk characters into AT — inline SVG or sprite + name is the default.
- **Focus visibility survives icon styling:** custom icon buttons keep the focus-ring contract (2px + offset).

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Functional name | `--icon-functional-name` | `aria-label-required` | Human phrase, not icon name |
| Decorative hide | `--icon-decorative-hide` | `aria-hidden+focusable-false` | Decoration out of AT tree |
| Icon button element | `--icon-icon-button-element` | `real-button` | Never clickable divs |
| Graphic contrast | `--icon-graphic-contrast` | `3:1-meaningful` | WCAG 1.4.11 vs adjacent colors |
| Name-tooltip parity | `--icon-name-tooltip-parity` | `same-string` | aria-label matches visible tooltip |
| Toggle naming | `--icon-toggle-naming` | `state-aware` | Pressed/aria-pressed announced |
| Icon font policy | `--icon-icon-font-policy` | `legacy-banned` | Inline SVG default |
| Focus ring | `--icon-focus-ring` | `2px+offset-2px` | Shared button contract |
| SVG title policy | `--icon-svg-title-policy` | `role-img+title-or-hidden` | Standalone SVGs named or hidden |
| Name language | `--icon-name-language` | `user-terms` | Same voice charter as visible copy |

Consume them by linking `assets/css/accessible-icons.css` at the app root for the paintable contracts (focus ring, contrast-bearing fills via `var(--icon-...)`), and enforcing the structural ones (`--icon-functional-name`, `--icon-icon-button-element`, `--icon-decorative-hide`) in markup, lint rules, and the generated icon components — the aria contract is versioned and reviewed like any other token tier, not left to per-developer memory.

## 4. Composition

- **Composes with icon-usability (guide 04):** recognition (visual) and naming (AT) are the two halves of one contract — the icon+label pattern satisfies both with a single markup structure.
- **Composes with skill-accessibility media-alt-text + keyboard-navigation:** the criteria layer for names, contrast, and focus; this guide is the icon-specific application of those broader rules.
- **Composes with icon-library-management:** the generated components ship with the aria contract pre-wired, so naming is inherited by default rather than re-implemented per usage site.

## 5. Signature Patterns

- **The icon button recipe:** `<button aria-label="Delete file">` + inline SVG aria-hidden + focus ring + 44px target — one pattern, reused everywhere, so reviewers only ever check deviations from it.
- **The decorative/functional audit:** every icon instance classified (functional: named; decorative: hidden) — unclassified icons are audit failures, not judgment calls.

## 6. Real-World Use Cases

- **Every icon instance in every product** — the most common a11y surface, which is why the contract is componentized rather than memorized.
- **Design systems baking naming into icon components** so a required `label` prop makes the unnamed icon button a compile error.
- **Audit:** unnamed icon buttons, icon-font junk in AT, 1.4.11 contrast fails — the recurring trio in shipped-product scans.

## 7. Combination Notes

### With other icons-illustration skills

- **Pairs naturally with icon-usability (guide 04):** recognition and naming are one contract split across two guides — the classification audit here and the recognition test there use the same per-instance inventory.
- **Pairs with icon-style-selection and icon-grid-sizing:** style and grid decisions must preserve stroke weights that keep 3:1 contrast alive at shipping sizes; a style change is an a11y re-check, not just a visual one.
- **Pairs with icon-library-management and svg-optimization:** generated components carry the aria contract pre-wired, and SVGO configs must keep title/aria attributes — optimization that strips names silently destroys the contract.
- **Pairs with icon-system-audit:** unnamed icon buttons and icon-font remnants are first-class audit findings.
- **Pairs with empty-error-illustrations, illustration-direction, mascot-character, and favicon-app-icons:** all non-icon artwork obeys the same rule — informative graphics get text alternatives, decorative ones get aria-hidden.
- **Pairs with animation-integration:** state-change announcements must survive animated toggles — the name updates at state-change time, not animation-end.
- **No caution or avoid list:** the aria contract is additive and compatible with every icon skill; conflicts only appear when a skill bypasses it.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** these styles keep icons as simple, high-contrast single-color marks — the easiest glyphs to hold above the 1.4.11 line against their surfaces, with few competing fills to audit.
- **No caution list:** style changes color and weight, never the naming contract; any style must still deliver `--icon-graphic-contrast` at 3:1.

### With motion skills (companion repo skill-animation)

- **Good affinity with reduced-motion:** this guide's state announcements pair with reduced-motion-safe toggles — state is communicated by name and non-motion cues first, so suppressed animation loses no information.
- **Good affinity with micro-interactions:** press and toggle feedback can animate freely as long as the accessible name flips with `aria-pressed` at the same moment the visual state changes.

## 8. Anti-Patterns

- **The unnamed icon button** — a clickable glyph no screen reader can explain
- **Decoration in the AT tree** — aria-hidden missing, icons read as 'graphic' noise
- **Icon-font remnants** — ligature junk ('') read aloud by AT
- **Low-contrast glyphs** — 1.2:1 icons invisible to low-vision users

### Accessibility Notes

This guide implements WCAG 1.1.1 (non-text content), 1.4.11 (non-text contrast), and 2.1.1/4.1.2 (keyboard + name/role/value): every functional icon named, every decorative icon hidden, every meaningful glyph contrasted — the aria contract is non-negotiable. In practice that means the AT tree reads as intent ("Delete file, button") rather than noise ("graphic"), toggles announce their state through aria-pressed, and contrast is checked against the actual adjacent color in both themes, including state-change colors like an activated favorite. The fallback rule: if per-instance naming cannot be enforced immediately, prioritize interactive icons (buttons/links) — unnamed interactive controls are the highest-severity failures; decorative misses degrade gracefully.

## 9. Code Examples

### Example 1 — The icon button recipe with toggle naming

Tokens: `assets/css/accessible-icons.css`

```html
<button class="icon-btn" id="favBtn" type="button" aria-label="Add to favorites" aria-pressed="false">
  <svg class="icon-btn-glyph" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
    <path class="glyph-fill" d="M12 21s-7.5-4.7-10-9.3C.4 8.6 2.3 5 5.7 5c2 0 3.4 1.1 4.3 2.6h4c.9-1.5 2.3-2.6 4.3-2.6 3.4 0 5.3 3.6 3.7 6.7C19.5 16.3 12 21 12 21z"/>
  </svg>
</button>
<style>
  .icon-btn {
    display: inline-grid;
    place-items: center;
    width: 44px; height: 44px; /* hit area carries the target, not the glyph */
    border: 1px solid #d4d4d4;
    border-radius: 8px;
    background: #fff;
    cursor: pointer;
  }
  .icon-btn-glyph { width: 20px; height: 20px; fill: #404040; }
  .icon-btn[aria-pressed="true"] .glyph-fill { fill: #b91c1c; } /* state change stays >= 3:1 on white */
  .icon-btn:focus-visible { outline: 2px solid #2563eb; outline-offset: 2px; } /* --icon-focus-ring */
</style>
<script>
  // --icon-toggle-naming: state-aware — name and pressed state flip together.
  const btn = document.getElementById('favBtn');
  btn.addEventListener('click', () => {
    const pressed = btn.getAttribute('aria-pressed') === 'true';
    btn.setAttribute('aria-pressed', String(!pressed));
    btn.setAttribute('aria-label', pressed ? 'Add to favorites' : 'Remove from favorites');
  });
</script>
```

### Example 2 — Functional vs decorative classification (AT-tree difference)

```html
<div class="row">
  <button class="icon-btn" type="button" aria-label="Search files">
    <svg class="glyph" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
      <path d="M10.5 3a7.5 7.5 0 1 1 0 15 7.5 7.5 0 0 1 0-15zm5.8 12.7 4.5 4.5-1.6 1.6-4.5-4.5z"/>
    </svg>
  </button>
  <span class="row-text">24 files
    <svg class="glyph glyph-deco" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
      <path d="M12 2 2 22h20L12 2zm0 6 6 12H6z"/>
    </svg>
  </span>
</div>
<style>
  .row { display: flex; align-items: center; gap: 8px; padding: 12px 16px; max-width: 320px; border: 1px solid #e5e5e5; border-radius: 8px; font: 14px/1.5 system-ui, sans-serif; }
  .icon-btn { display: inline-grid; place-items: center; width: 44px; height: 44px; border: none; border-radius: 8px; background: #f5f5f5; cursor: pointer; }
  .icon-btn:focus-visible { outline: 2px solid #2563eb; outline-offset: 2px; }
  .glyph { width: 20px; height: 20px; fill: #171717; }
  .glyph-deco { width: 14px; height: 14px; fill: #d4d4d4; vertical-align: -2px; }
</style>
<script>
  // Functional: named button + hidden glyph -> AT reads "Search files, button".
  // Decorative: aria-hidden + focusable=false -> AT reads only "24 files".
  // The audit rule: every .glyph instance is one or the other — unclassified = audit failure.
  document.querySelectorAll('svg.glyph').forEach((svg) => {
    console.assert(
      svg.getAttribute('aria-hidden') === 'true' && svg.getAttribute('focusable') === 'false',
      'Every glyph is hidden from AT; meaning lives on the named control'
    );
  });
</script>
```

## 10. Implementation Checklist

- [ ] Every functional icon carries an accessible name (`--icon-functional-name`) phrased in user terms, matching its tooltip string (`--icon-name-tooltip-parity`).
- [ ] Every decorative icon ships `aria-hidden="true" focusable="false"` (`--icon-decorative-hide`) — nothing decorative reaches the AT tree or tab order.
- [ ] All icon buttons are real `<button>` elements (`--icon-icon-button-element`) — no clickable divs or background-image glyphs.
- [ ] Meaningful glyphs hold 3:1 contrast against adjacent colors in both themes, including state-change colors (`--icon-graphic-contrast`).
- [ ] Toggles announce state via aria-pressed with a state-aware name (`--icon-toggle-naming`).
- [ ] Icon fonts are fully retired (`--icon-icon-font-policy`); inline SVG or sprites with names are the only delivery.
- [ ] Icon button focus rings follow `--icon-focus-ring` (2px + 2px offset) in every theme.
- [ ] Standalone SVGs are either named (role="img" + title) or hidden (`--icon-svg-title-policy`).

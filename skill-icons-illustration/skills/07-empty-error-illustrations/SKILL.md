---
name: empty-error-illustrations
description: The highest-traffic illustration slots: empty states, errors, 404s, and offline - mood-matched, copy-paired, and light-weight.
tags: [illustrations, empty-states, error-pages, 404, offline]
related: [illustration-direction, mascot-character, svg-optimization]
---

# Visual Asset Guide: Empty & Error Illustrations

## 1. Definition

Empty and error states are where illustrations earn their keep: a 404 with personality is remembered; a blank box is forgotten. This guide covers the slot-specific contracts: empty states (mood matches the taxonomy - hopeful for first-use, apologetic for no-results), error illustrations (calm, never mocking the failure), 404/offline specials, and the technical floor - illustration paired with copy and action, mood-matched to context, and light enough not to punish the very page that failed.

## 2. Core Principles

- **Illustration + copy + action, always:** the drawing sets mood; the text explains; the button moves forward - all three, every slot.
- **Mood matches the moment:** first-use is hopeful, no-results is apologetic-helpful, errors are calm - a grinning mascot on an error page is a betrayal.
- **Errors never mock:** the illustration sympathizes with the failure ("we broke it"), never jokes at the user's expense.
- **404 is the personality slot:** the one page where humor is welcomed - budget it accordingly.
- **Offline is designed:** a specific illustration + "You're offline" + retry - not a browser error.
- **Weight matters most on failure pages:** error/empty illustrations are optimized aggressively (SVG < 30KB) - don't punish the page that already failed.
- **Consistent family across slots:** the empty/error set is drawn in one style pass - mixed-art error pages read as a broken product.
- **Dark mode is a variant:** illustrations ship light/dark variants or use CSS-variable-driven colors - a white-background PNG in dark mode is a bug.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Slot trio | `--icon-slot-trio` | `illustration+copy+action` | All three, every slot |
| Empty mood | `--icon-empty-mood` | `hopeful-first-use,apologetic-no-results` | Mood per taxonomy state |
| Error mood | `--icon-error-mood` | `calm-sympathetic` | Never mocking the failure |
| 404 policy | `--icon-404-policy` | `personality-allowed` | The humor budget slot |
| Offline special | `--icon-offline-special` | `designed+retry` | Specific illustration + action |
| Weight budget | `--icon-weight-budget` | `svg-under-30kb` | Failure pages stay fast |
| Family consistency | `--icon-family-consistency` | `one-style-pass` | The set drawn together |
| Dark mode | `--icon-dark-mode` | `variant-or-css-vars` | No white-box PNGs in dark UI |
| Alt pairing | `--icon-alt-pairing` | `adjacent-copy-carries` | Illustration decorative; text carries meaning |
| Reduced motion | `--icon-reduced-motion` | `animation-collapses` | Animated variants honor the media query |

Consume them by linking `assets/css/empty-error-illustrations.css` at the app root, then referencing `var(--icon-<role>)` from state components - the trio (art, copy, action) is styled from the same tokens so no slot ships a piece missing. A state illustration whose fills are not CSS variables is a theming bug waiting for dark mode.

## 4. Composition

- **Composes with ux-writing empty-states (skill-ux-writing guide 05):** that guide owns the copy; this guide owns the art - the trio is the contract. Neither side ships half a slot.
- **Composes with illustration-direction (guide 06):** the empty/error set is drawn under the same spec - palette, stroke weight, and perspective rules carry over unchanged.
- **Composes with component-recipes empty-loading-error:** the state components are the slots these illustrations live in; the illustration inherits the component's spacing and theming contract.

## 5. Signature Patterns

- **The state-illustration set:** one style pass producing the whole family (empty/first-use, no-results, 404, offline, 500, permission) - consistent mood ladder from hope to apology. Drawing the set together is what makes a 404 and a 500 feel like the same product.
- **The CSS-variable illustration:** artwork built on CSS custom properties so dark mode and theming come free - one SVG, many themes. Fills reference `var(--icon-*)` or semantic color tokens; no hex lives inside the asset.

## 6. Real-World Use Cases

- **Empty states across lists, tables, dashboards, and search.** Every blank-first-render surface gets the hopeful variant; every zero-results search gets the apologetic-helpful one.
- **Error pages: 404, 500, offline, permission-denied.** Each has a defined mood and a defined action - calm art, plain language, a way forward.
- **Audit: blank boxes, mocking error art, heavy illustrations on failure pages.** The three classic failures this guide's checklist exists to catch.

## 7. Combination Notes

### With other icons-illustration skills

- **Good with illustration-direction (guide 06):** the empty/error set must be drawn under the shared illustration spec - same stroke weight, palette, and perspective - or the family-consistency token is violated by definition.
- **Good with mascot-character (guide 08):** the mascot is a common empty/error actor, but it inherits this guide's mood rules - hopeful on first-use, sympathetic (never cheerful) on errors.
- **Good with svg-optimization (guide 09):** the weight-budget token (`svg-under-30kb`) is enforced by the optimization pipeline; failure pages are the most aggressive optimization targets.
- **Good with icon-grid-sizing, icon-style-selection, accessible-icons, icon-library-management, icon-usability, favicon-app-icons, icon-system-audit, and animation-integration:** state slots consume the shared grid, style, library, and audit contracts like any other illustration surface; animated empty-state art follows animation-integration's reduced-motion rules.
- **No caution or avoid list:** these slots are the highest-traffic surfaces in the system - nearly every asset skill has a stake in them. The risk is not a bad pairing; it is shipping a slot without one of the trio's three parts.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with collage-art, minimalism, and flat-design:** minimalism and flat-design keep failure pages fast (few nodes, small files - the weight budget is easy to meet) and calm; collage-art gives the 404 personality slot an expressive, layered language where its humor budget can land.
- **Caution notes:** none listed, but weight discipline applies regardless of style - a richly textured style must still hit `svg-under-30kb` on failure pages, compressing texture rather than abandoning the budget.

### With motion skills (companion repo skill-animation)

- **Good affinity with illustration-lottie and entrance-exit:** a gentle entrance (fade-scale per animation-integration's default pattern) softens the arrival of an error state, and Lottie can animate the 404 personality slot - both collapse to static frames under `--icon-reduced-motion: animation-collapses`.
- **Caution notes:** none listed, but mood rules bind motion too - a bouncing, laughing animation on a 500 is the animated form of mocking the failure.

## 8. Anti-Patterns

- **Mocking errors** — cheerful art laughing at the user's failed payment
- **The heavy 404** — a 2MB illustration punishing the page that already failed
- **Copy-less art** — illustration alone where explanation was needed
- **White-box art in dark mode** — un-themed illustrations breaking the surface

### Accessibility Notes

These illustrations are decorative-by-design: the adjacent copy carries the meaning, so the artwork ships with an empty alt and the region - not the image - announces the state. Any text embedded inside the illustration must meet contrast against its fill, which is one more reason fills route through CSS variables rather than baked hexes. Animated variants collapse under `prefers-reduced-motion` per `--icon-reduced-motion: animation-collapses`; state announcements come from the region, never from the art. The fallback rule: if animation on empty/error art cannot honor reduced-motion, ship static variants only - mood does not require motion.

## 9. Code Examples

### Example 1 — The state-illustration set as slot trios (with dark mode)

Tokens: `assets/css/empty-error-illustrations.css`

```html
<button id="theme">Toggle dark mode</button>

<section class="slot" aria-label="No projects yet">
  <svg class="art" viewBox="0 0 64 64" aria-hidden="true" role="presentation">
    <g><circle class="f-a" cx="32" cy="30" r="18"/><path class="f-b" d="M20 44h24v6H20z"/></g>
  </svg>
  <h2>Nothing here yet</h2>
  <p>Create your first project to get started.</p>
  <a class="action" href="/new">New project</a>
</section>

<section class="slot" aria-label="No search results">
  <svg class="art" viewBox="0 0 64 64" aria-hidden="true">
    <g><circle class="f-a" cx="28" cy="28" r="14"/><path class="f-b" d="M38 38l12 12" stroke-width="4" fill="none" stroke="currentColor"/></g>
  </svg>
  <h2>No matches for "zapier"</h2>
  <p>Try a shorter term, or browse all projects.</p>
  <a class="action" href="/browse">Browse all</a>
</section>

<section class="slot error" aria-label="Page not found">
  <svg class="art" viewBox="0 0 64 64" aria-hidden="true">
    <g><rect class="f-a" x="12" y="10" width="40" height="44" rx="4"/><path class="f-b" d="M20 24h24M20 34h16" stroke-width="4" stroke="currentColor" fill="none"/></g>
  </svg>
  <h2>404 - this page wandered off</h2>
  <p>The link may be old. The homepage is right here.</p>
  <a class="action" href="/">Back home</a>
</section>

<section class="slot error" aria-label="Offline">
  <svg class="art" viewBox="0 0 64 64" aria-hidden="true">
    <g><path class="f-a" d="M8 40c10-14 38-14 48 0" fill="none" stroke-width="4" stroke="currentColor"/><path class="f-b" d="M32 46l6 8H26z"/></g>
  </svg>
  <h2>You're offline</h2>
  <p>Check your connection - your work is saved locally.</p>
  <button class="action" onclick="location.reload()">Retry</button>
</section>

<style>
  /* CSS-variable illustration: fills route through vars, so theming is free */
  :root { --il-fill-a: #E0E7FF; --il-fill-b: #93C5FD; --il-ink: #1E293B; }
  body.dark { --il-fill-a: #312E81; --il-fill-b: #4C1D95; --il-ink: #E2E8F0; }
  .slot { font: 14px/1.5 Inter, system-ui, sans-serif; color: var(--il-ink);
          max-width: 340px; padding: 24px; text-align: center; }
  .slot .f-a { fill: var(--il-fill-a); }
  .slot .f-b { fill: var(--il-fill-b); }
  .slot h2 { font-size: 16px; margin: 8px 0 4px; }
  .slot p { margin: 0 0 12px; opacity: .8; }
  .action { display: inline-block; padding: 8px 16px; border-radius: 8px; background: var(--il-ink);
            color: var(--il-fill-a); text-decoration: none; border: none; cursor: pointer;
            font: 600 13px Inter, system-ui, sans-serif; }
</style>
<script>
  document.getElementById('theme').onclick = () => document.body.classList.toggle('dark');
  // Weight budget guard: --icon-weight-budget = svg-under-30kb
  console.assert(getComputedStyle(document.documentElement)
    .getPropertyValue('--icon-weight-budget').trim() === 'svg-under-30kb',
    'state art must ship under 30KB per SVG');
</script>
```

### Example 2 — Weight comparison: optimized vs raw state art

```html
<p>State art budget: <code>svg-under-30kb</code> per file (failure pages stay fast).</p>
<dl class="weights">
  <dt>404 illustration</dt><dd>8.2 KB (raw: 61.4 KB)</dd>
  <dt>Offline illustration</dt><dd>5.9 KB (raw: 44.1 KB)</dd>
  <dt>500 illustration</dt><dd>9.7 KB (raw: 88.3 KB)</dd>
</dl>
<style>
  .weights { font: 14px/1.6 Inter, system-ui, sans-serif; max-width: 420px; }
  .weights dt { font-weight: 600; margin-top: 8px; }
  .weights dd { margin: 0; color: #166534; }
</style>
<script>
  // CI-style check: every state SVG must be under the budget, measured gzipped
  document.querySelectorAll('.weights dd').forEach((dd) => {
    if (parseFloat(dd.textContent) > 30) dd.style.color = '#B91C1C'; // over budget
  });
</script>
```

## 10. Implementation Checklist

- [ ] Every empty/error slot ships the full trio - illustration, copy, and action - per `--icon-slot-trio: illustration+copy+action`.
- [ ] Mood is matched per state: hopeful first-use, apologetic no-results (`--icon-empty-mood`), calm-sympathetic errors (`--icon-error-mood`).
- [ ] The 404 is the only slot spending the humor budget (`--icon-404-policy: personality-allowed`).
- [ ] Offline is a designed screen with a retry action (`--icon-offline-special: designed+retry`), never a browser error.
- [ ] Every state SVG is under 30KB (`--icon-weight-budget: svg-under-30kb`), measured gzipped, enforced in CI.
- [ ] The whole set was drawn in one style pass (`--icon-family-consistency: one-style-pass`); no slot mixes art styles.
- [ ] Fills are CSS variables or shipped variants (`--icon-dark-mode: variant-or-css-vars`) - no white-box art in dark mode.
- [ ] Illustrations are decorative with adjacent copy carrying meaning (`--icon-alt-pairing`), and animated variants collapse under reduced-motion (`--icon-reduced-motion: animation-collapses`).

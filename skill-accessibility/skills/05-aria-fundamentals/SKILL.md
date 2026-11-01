---
name: aria-fundamentals
description: The first rule of ARIA and the core vocabulary — roles, states, properties, live regions, and when native HTML wins.
tags: [accessibility, aria, semantics, screen-readers, html]
related: [aria-patterns-widgets, screen-readers, forms-errors]
---

# Accessibility Skill: ARIA Fundamentals

## 1. Definition

ARIA (Accessible Rich Internet Applications) is the contract between custom UI and assistive technology: roles say what a thing IS, states say how it currently is, and live regions narrate change. Its first rule governs everything — do not use ARIA if native HTML can do the job, because a native button carries focus, keyboard, and semantics for free while an ARIA-imitated div must reimplement all of them, usually wrongly. This skill is the vocabulary layer every other accessibility skill builds on: accessible names (aria-label, aria-labelledby, visible text), state attributes that must track the DOM (aria-expanded, aria-checked, aria-pressed), idref wiring that must resolve (aria-describedby, aria-labelledby), decorative handling (aria-hidden="true"), and the landmark skeleton (header/nav/main/aside/footer) that gives screen reader users a page map.

## 2. Core Principles

- **First rule of ARIA:** prefer native HTML — button, link, input, select, and table carry semantics, keyboard, and mobile behaviors automatically.
- **Roles do not add behavior:** `role='button'` on a div gives narration but no keyboard — you must implement Tab/Enter/Space yourself (or use a real button).
- **Every interactive control has an accessible name:** aria-label, aria-labelledby, or visible text — unnamed buttons read as 'button' in screen readers.
- **States are live data, not decoration:** aria-expanded, aria-pressed, aria-checked, aria-disabled must actually track component state.
- **Ids referenced must exist:** aria-labelledby/aria-describedby pointing at missing ids produce silence - CI-lint the references.
- **aria-hidden hides from AT only:** it does not remove focus - hidden-but-focusable is a trap; pair with inert or removal from tab order.
- **Live regions are registered before they announce:** an aria-live region must exist in the DOM before content changes for narration to fire.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Native-first policy | `--a11y-native-first-policy` | `html-before-aria` | First rule of ARIA; custom roles need justification in review |
| Accessible name policy | `--a11y-accessible-name-policy` | `required` | Every interactive element; lint-blocks unnamed controls |
| Name source order | `--a11y-name-source-order` | `labelledby > label > aria-label > content` | Prefer visible text as the name source |
| State tracking | `--a11y-state-tracking` | `must-match-dom` | aria-expanded/checked/pressed mirror real state |
| Live region verbosity | `--a11y-live-region-verbosity` | `polite-default` | aria-live=polite; assertive only for errors/timeouts |
| Decorative policy | `--a11y-decorative-policy` | `aria-hidden-true` | Decorative icons/images excluded from the AT tree |
| Idref validation | `--a11y-idref-validation` | `ci-lint` | aria-labelledby/describedby targets must exist |
| Hidden focus rule | `--a11y-hidden-focus-rule` | `aria-hidden-plus-inert` | Hidden content must also be unfocusable |
| Role validation | `--a11y-role-validation` | `axe-ci` | Required parent/child role structure checked in CI |
| Landmark set | `--a11y-landmark-set` | `header-nav-main-aside-footer` | Page skeleton roles; one main per page |

Consume them by linking `assets/css/aria-fundamentals.css` at the app root — it ships the visually-hidden (sr-only) utility used for live regions and labels, plus the landmark skeleton — and treat the policy tokens as review gates: `var(--a11y-...)` values encode lint rules (unnamed controls blocked, idrefs CI-checked) that PRs must satisfy, not optional guidance.

## 4. Composition

- **Composes with aria-patterns-widgets:** fundamentals are the vocabulary; patterns are the validated combinations (tabs, menus, comboboxes).
- **Composes with screen-readers:** ARIA is only half the contract - testing with actual screen readers validates what markup alone cannot.
- **Composes with forms-errors:** label/description/error wiring (aria-describedby) is the highest-traffic ARIA usage in most products.

## 5. Signature Patterns

- **Name-it-once labeling:** visible visible-label + aria-labelledby wiring as the default; aria-label reserved for icon-only controls.
- **Live-region service:** a single polite live region utility announces toasts, filter results, and async status app-wide - no per-component live regions.

## 6. Real-World Use Cases

- **Custom components:** giving divs real semantics when native elements genuinely do not fit.
- **Icon-only buttons, toggles, and dynamic state UI that native HTML cannot express.**
- **Auditing for the classic failures: unnamed controls, stale states, dangling idrefs.**

## 7. Combination Notes

### With other accessibility skills

- **Good with aria-patterns-widgets:** fundamentals define the vocabulary (roles, states, names); the patterns skill assembles them into APG-exact widgets — learning vocabulary before combinations is the intended order.
- **Good with screen-readers:** correct markup is only half the contract; listening tests validate what the AT tree actually narrates, catching the gap between valid ARIA and useful ARIA.
- **Good with forms-errors:** aria-describedby label/hint/error wiring is the highest-traffic ARIA usage in real products, so these two skills are exercised together on nearly every screen.
- **Good with keyboard-navigation and focus-management:** ARIA roles narrate what keyboard and focus make operable — markup without operability, or operability without narration, both fail.
- **No caution or avoid list:** ARIA fundamentals compose with every sibling; the risk is misuse (ARIA soup, stale states), not conflicting partners.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** lean, text-forward styles keep visible labels on controls, which aligns with the name-source-order preference for visible text over aria-label.
- **Caution with collage-art and maximalism:** icon-heavy, layered compositions multiply icon-only controls and decorative layers — each one needs a deliberate name or aria-hidden decision, and the density raises the cost of getting names wrong.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** state changes that animate (expand/collapse, toggles) are exactly the ones whose ARIA state must update in sync — aria-expanded flips when the animation starts, not when it ends.
- **No caution list:** animated UI still needs the same names and states; motion never licenses removing semantics, so there is no conflicting motion partner.

## 8. Anti-Patterns

- **ARIA soup** — role='button' + tabindex + keydown on a div when a <button> did it all for free
- **Aria-label on everything** — slapping labels over visible text, producing names that differ from what users see
- **Stale states** — aria-expanded that never changes because the JS forgot the attribute exists
- **Dead references** — aria-describedby pointing at removed ids - silent in code review, silent in screen readers

### Accessibility Notes

ARIA misused is worse than ARIA absent: wrong roles misorient screen reader users more than no roles at all — that is why the native-first policy is a lint gate, not a suggestion. The fallback rule follows from it: when unsure which ARIA fits, downgrade to native HTML; an unstyled native control is accessible, an over-ARIA'd div usually is not. Operationally that means every interactive control carries an accessible name from the agreed source order, decorative content is marked `aria-hidden="true"` *and* made unfocusable, live regions are registered before they announce with polite as the default verbosity, and axe in CI validates role structure and idrefs so silent breakage cannot ship.

## 9. Code Examples

### Example 1 — Unnamed vs named controls (before/after)

Tokens: `assets/css/aria-fundamentals.css`

```html
<!-- BEFORE: unnamed control — narrates as "button" -->
<button class="icon-btn" aria-label="">🔍</button>

<!-- AFTER: named control — narrates as "Search" -->
<button class="icon-btn" aria-label="Search">
  <svg aria-hidden="true" width="16" height="16" viewBox="0 0 16 16">
    <circle cx="6" cy="6" r="5" fill="none" stroke="currentColor" stroke-width="2"/>
    <line x1="10" y1="10" x2="15" y2="15" stroke="currentColor" stroke-width="2"/>
  </svg>
</button>

<style>
  /* --a11y-decorative-policy: aria-hidden-true keeps the glyph out of the AT tree;
     --a11y-accessible-name-policy: required gives the button its name */
  .icon-btn {
    display: inline-grid; place-items: center;
    width: 40px; height: 40px; border-radius: 8px;
    border: 1px solid #d4d4d4; background: #fff; cursor: pointer;
  }
  .icon-btn:focus-visible { outline: 2px solid #1D4ED8; outline-offset: 2px; }
</style>
```

### Example 2 — Visible label wiring + polite live region

Tokens: `assets/css/aria-fundamentals.css`

```html
<form class="filter">
  <!-- --a11y-name-source-order: labelledby > label > aria-label > content -->
  <label for="q" id="q-label">Filter invoices</label>
  <input id="q" type="text" aria-labelledby="q-label" aria-describedby="q-hint">
  <span id="q-hint" class="hint">Matches invoice number or client</span>

  <p id="results" class="sr-only" role="status" aria-live="polite"></p>
  <ul id="list" class="results"></ul>
</form>

<style>
  .filter { max-width: 360px; font: 14px/1.5 system-ui, sans-serif; display: grid; gap: 6px; }
  .hint { color: #404040; font-size: 12px; }
  .results { margin: 8px 0 0; padding-left: 18px; }
  /* sr-only utility from assets/css/aria-fundamentals.css */
  .sr-only { position: absolute; width: 1px; height: 1px; margin: -1px;
             overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
</style>
<script>
  const invoices = ['INV-001 Acme', 'INV-002 Globex', 'INV-003 Initech'];
  const input = document.getElementById('q');
  const list = document.getElementById('list');
  // --a11y-live-region-verbosity: polite-default; region exists in DOM before announcing
  const status = document.getElementById('results');

  input.addEventListener('input', () => {
    const hits = invoices.filter(i => i.toLowerCase().includes(input.value.toLowerCase()));
    list.innerHTML = hits.map(i => `<li>${i}</li>`).join('');
    status.textContent = `${hits.length} invoice${hits.length === 1 ? '' : 's'} found`;
  });
</script>
```

## 10. Implementation Checklist

- [ ] Every interactive control has an accessible name per `--a11y-accessible-name-policy`, sourced in `--a11y-name-source-order` order.
- [ ] Native HTML is used wherever it fits, per `--a11y-native-first-policy`; custom roles carry review justification.
- [ ] All aria-expanded/checked/pressed attributes track real component state per `--a11y-state-tracking`.
- [ ] aria-labelledby/describedby references resolve at build time per `--a11y-idref-validation` (ci-lint).
- [ ] Decorative content follows `--a11y-decorative-policy` and the `--a11y-hidden-focus-rule` (aria-hidden + inert).
- [ ] One shared polite live region (`--a11y-live-region-verbosity`) announces toasts, filter counts, and async status app-wide.
- [ ] Page skeleton implements `--a11y-landmark-set` with exactly one `main`, validated by `--a11y-role-validation` (axe-ci).

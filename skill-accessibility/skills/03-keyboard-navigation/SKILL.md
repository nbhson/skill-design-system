---
name: keyboard-navigation
description: Everything operable by mouse works by keyboard — tab order, skip links, roving tabindex, and shortcut discipline (WCAG 2.1.1/2.4.3).
tags: [keyboard, tab-order, focus, shortcuts, wcag]
related: [wcag-fundamentals, focus-management, aria-patterns-widgets]
---

# Accessibility Skill: Keyboard Navigation

## 1. Definition

Keyboard navigation is the operability backbone: every interactive element reachable and usable without a mouse (WCAG 2.1.1), in a meaningful order (2.4.3), with no traps the user cannot escape (2.1.2). It serves motor-impaired users, screen reader users, and power users alike — and it is the fastest accessibility audit there is: unplug the mouse and try to use the product. Keyboard operability cannot have an 'alternative path' shortcut, because for any UI a mouse cannot reach, the keyboard path IS the alternative path.

## 2. Core Principles

- **Everything interactive is tabbable or contains a documented path:** if it has a click handler, it needs a keyboard story (button, link, or roving tabindex).
- **DOM order IS tab order:** visually reordered layouts (CSS order, grid re-placement) silently break logical navigation — keep source order semantic.
- **Skip links are mandatory on repeated navigation:** first Tab reaches 'skip to main content' and it must actually appear on focus.
- **No keyboard traps without escape:** focus traps are legal only inside modals, and Escape releases them (WCAG 2.1.2).
- **Custom widgets follow ARIA patterns exactly:** tabs, menus, and comboboxes have documented keymaps — inventing keymaps is an anti-pattern.
- **Shortcuts are enhancements, never the only path:** single-key shortcuts must be remappable or active only on focus (WCAG 2.1.4).
- **Visible focus is keyboard's companion:** every stop shows where you are — a tabbable-but-invisible focus is a focus-management bug.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Navigation | `--a11y-nav-model` | `dom-order` | Tab order follows DOM; visual reordering must preserve semantics |
| Navigation | `--a11y-skip-link-required` | `true` | First tabbable element on pages with repeated nav blocks |
| Navigation | `--a11y-escape-releases-trap` | `true` | WCAG 2.1.2: modal focus traps always exit via Escape |
| Widgets | `--a11y-roving-tabindex` | `pattern-owned` | Composite widgets (tabs/listbox/grid) own arrow-key roving |
| Widgets | `--a11y-arrow-key-semantics` | `in-group-only` | Arrows move inside a widget; Tab moves between widgets |
| Shortcuts | `--a11y-shortcut-policy` | `remappable-or-focus-only` | WCAG 2.1.4 character key shortcuts |
| Targets | `--a11y-interactive-min-target` | `44px` | Keyboard focus + touch share the target-size floor (2.5.8) |
| Modals | `--a11y-modal-focus-policy` | `trap-and-return` | Trap inside modal; return to trigger on close |
| Modals | `--a11y-tabindex-policy` | `0-or-negative-only` | tabindex=1+ is a build failure in review |
| Testing | `--a11y-keyboard-test` | `mouse-unplugged` | The 5-minute audit: complete a core task keyboard-only |

Load `assets/css/keyboard-navigation.css` at the app root to ship the skip-link treatment and shared focus styles as custom properties, then consume them via `var(--a11y-<role>)` from the page template and component library — the skip link, the 44px target floor, and the tabindex policy are shared contracts, not per-page decisions.

## 4. Composition

- **Composes with focus-management:** keyboard defines the stops; focus management defines where focus lands when surfaces change — open, close, route, and return are its jurisdiction.
- **Composes with aria-patterns-widgets:** composite widgets inherit their keymaps from ARIA patterns — this skill enforces them at the page level and in review.
- **Composes with modals/dialogs recipes (skill-component-recipes guide 04):** the trap-and-return policy is a shared contract across both repos' implementations.

## 5. Signature Patterns

- **Mouse-unplugged walkthrough:** complete one core task (signup, checkout, search) keyboard-only before release; record every stop that fails — the fastest full-coverage audit in the toolkit.
- **Skip-link + landmark skeleton:** header/nav/main/footer landmarks with a working skip link ship as a page template, not per-page work — one skeleton, every page inherits it.

## 6. Real-World Use Cases

- **Any product with forms, tables, or custom widgets** — the surfaces where keyboard breaks first and repairs cost most.
- **Enterprise apps used all day by keyboard-first power users:** keyboard support is a productivity feature, not charity.
- **Quick audits:** the mouse-unplugged test finds the worst violations in minutes and prioritizes the backlog.

## 7. Combination Notes

### With other accessibility skills

- **Good with wcag-fundamentals, color-contrast, focus-management, aria-fundamentals, aria-patterns-widgets, forms-errors, screen-readers, zoom-reflow, testing-audit, cognitive-content, media-alt-text:** keyboard operability is the shared substrate — focus-management owns landings, aria-patterns owns keymaps, color-contrast owns the visible focus ring, and screen-readers verify the whole circuit by ear.
- **No caution or avoid list:** keyboard support never conflicts with another accessibility skill; the only enemy is a click handler without a keyboard story.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** clean layouts keep DOM order aligned with visual order, and flat surfaces make visible focus states easy to render — the styles and the tab circuit stay in agreement.
- **Caution with collage-art:** overlapping, scattered compositions invite CSS re-placement that breaks the DOM-order tab model; if a collage layout reorders visually, source order must be re-authored to match, not patched with positive tabindex.

### With motion skills (companion repo skill-animation)

- **Good affinity with micro-interactions and easing-timing:** hover/pressed transitions read as state feedback for keyboard users too — the same eased transitions fire on :focus-visible and :active.
- **Caution with gesture-drag:** drag-heavy interactions (sortable lists, sliders) must ship a keyboard equivalent per WCAG 2.5.7 (dragging movements); a gesture with no arrow-key path is a blocker.

## 8. Anti-Patterns

- **Div-with-onClick** — clickable non-focusable elements - the single most common WCAG 2.1.1 failure
- **tabindex Positive** — 1, 2, 3 overrides that break the moment the DOM shifts
- **Invisible focus** — outline: none without a replacement - keyboard users navigate blind
- **Visual order lies** — CSS-reordered layouts whose tab order no longer matches what eyes see

### Accessibility Notes

This skill exists for WCAG 2.1.1/2.4.3/2.1.2/2.1.4: keyboard operability is non-negotiable and cannot have an 'alternative path' short-cut — the keyboard path IS the alternative path for mouse-inaccessible UI. Every principle here is checkable without assistive technology, which makes it the first audit to run and the cheapest to keep green. The fallback rule is absolute: if a control cannot be made keyboard-operable, replace it with a native control; a broken custom widget is never shipped alongside a documented apology.

## 9. Code Examples

### Example 1 — Skip link + landmark page skeleton

Tokens: `assets/css/keyboard-navigation.css`

```html
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  <header class="site-header"><nav aria-label="Primary">…nav links…</nav></header>
  <main id="main" tabindex="-1">
    <h1>Inbox</h1>
    <p>Every stop from here down is reachable by Tab, in DOM order.</p>
    <button type="button">Compose</button>
  </main>
  <footer class="site-footer">…footer links…</footer>
</body>
<style>
  .skip-link {
    position: absolute; left: -9999px; top: 0;
    background: #171717; color: #FFFFFF; padding: 8px 16px;
    font: 600 14px/1 Inter, system-ui, sans-serif;
    border-radius: 0 0 6px 0;
  }
  /* First Tab must make it actually appear (WCAG 2.4.1) */
  .skip-link:focus { left: 0; }
  .site-header { border-bottom: 1px solid #D4D4D4; padding: 12px 16px; }
  main { max-width: 640px; margin: 16px auto; padding: 0 16px; }
  main:focus { outline: none; } /* programmatic target; focus-visible users never Tab here */
  .site-footer { border-top: 1px solid #D4D4D4; padding: 12px 16px; }
  button { min-height: 44px; min-width: 44px; } /* target-size floor (2.5.8) */
  button:focus-visible { outline: 2px solid #1D4ED8; outline-offset: 2px; }
</style>
```

### Example 2 — Roving-tabindex listbox (APG keymap sketch)

Tokens: `assets/css/keyboard-navigation.css`

```html
<span id="sort-label">Sort by</span>
<ul class="listbox" role="listbox" aria-labelledby="sort-label">
  <li role="option" aria-selected="true" tabindex="0">Date</li>
  <li role="option" aria-selected="false" tabindex="-1">Relevance</li>
  <li role="option" aria-selected="false" tabindex="-1">Author</li>
</ul>
<script>
  const box = document.querySelector('.listbox');
  const options = [...box.querySelectorAll('[role="option"]')];
  const active = () => options.findIndex(o => o.tabIndex === 0);
  // APG listbox: arrows move inside, Tab moves between widgets
  box.addEventListener('keydown', (e) => {
    const i = active();
    let next = i;
    if (e.key === 'ArrowDown') next = Math.min(i + 1, options.length - 1);
    else if (e.key === 'ArrowUp') next = Math.max(i - 1, 0);
    else if (e.key === 'Home') next = 0;
    else if (e.key === 'End') next = options.length - 1;
    else return;
    e.preventDefault(); // arrows never scroll the page inside the widget
    options[i].tabIndex = -1;
    options[next].tabIndex = 0;
    options[next].focus();
    options.forEach(o => o.setAttribute('aria-selected', o === options[next]));
  });
</script>
<style>
  .listbox {
    list-style: none; margin: 8px 0; padding: 4px; width: 200px;
    border: 1px solid #D4D4D4; border-radius: 8px;
    font: 14px/1.4 Inter, system-ui, sans-serif;
  }
  [role="option"] { padding: 8px 12px; border-radius: 6px; cursor: pointer; }
  [role="option"][aria-selected="true"] { background: #EFF6FF; font-weight: 600; }
  [role="option"]:focus-visible { outline: 2px solid #1D4ED8; outline-offset: -2px; }
</style>
```

## 10. Implementation Checklist

- [ ] Tab order follows DOM order per `var(--a11y-nav-model)` — CSS-reordered layouts re-author source order instead of patching with tabindex.
- [ ] Positive tabindex does not exist anywhere (`var(--a11y-tabindex-policy)` is 0-or-negative-only and lint-enforced).
- [ ] Every page with repeated navigation ships a working skip link (`var(--a11y-skip-link-required)`) that appears on first Tab.
- [ ] All interactive elements meet the 44px target floor via `var(--a11y-interactive-min-target)` (WCAG 2.5.8).
- [ ] Composite widgets use roving tabindex per `var(--a11y-roving-tabindex)` with arrows moving in-group only and Tab exiting.
- [ ] Modal focus traps always release via Escape and return to the trigger (`var(--a11y-modal-focus-policy)` = trap-and-return).
- [ ] Single-key shortcuts are remappable or focus-only per `var(--a11y-shortcut-policy)` (WCAG 2.1.4).
- [ ] The mouse-unplugged walkthrough (`var(--a11y-keyboard-test)`) completes one core task keyboard-only before each release.

---
name: aria-patterns-widgets
description: The APG patterns — tabs, menus, combobox, dialog, listbox, grid — implemented exactly as specified: roles, keymaps, and state wiring.
tags: [accessibility, aria, widgets, apg, keyboard]
related: [keyboard-navigation, focus-management, aria-fundamentals]
---

# Accessibility Skill: ARIA Widget Patterns

## 1. Definition

Composite widgets (tabs, menus, comboboxes, dialogs, listboxes, grids) have validated recipes in the W3C ARIA Authoring Practices Guide (APG): exact roles, required attributes, and canonical keymaps. This skill covers implementing those patterns faithfully — because users of assistive tech have learned these keymaps from every other product, a widget that invents its own keys is a widget they cannot use. The discipline is threefold: role structure must match the pattern (tablist/tab/tabpanel with the required aria wiring), the keymap must match the pattern (arrow keys, Home/End, Escape, Enter — nothing added, nothing removed), and state must update live (aria-selected, aria-expanded, aria-activedescendant change the moment the UI changes). Deviation is a design decision with a cost paid by AT users, so it is made by exception, never by convenience.

## 2. Core Principles

- **Follow the APG exactly:** the role structure, required attributes, and keymap come from the pattern - creativity belongs in styling, not keymaps.
- **Arrow keys move within, Tab moves between:** composite widgets use roving tabindex inside; Tab exits after the widget's last stop.
- **Every state change updates ARIA state:** tab selection updates aria-selected, combobox updates aria-expanded + aria-activedescendant.
- **Dialogs follow the dialog pattern:** role=dialog, aria-modal=true, labelled by title, focus trap, Escape closes, focus returns.
- **Menus are for actions, selects are for values:** menu/listbox confusion is the most common pattern misuse.
- **Grid is not a table:** grid owns arrow-key cell navigation and interactive cells; a read-only data table stays native <table>.
- **Announce async results:** combobox results, filter counts, and loading states narrate via live regions or aria-activedescendant changes.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Pattern source | `--a11y-pattern-source` | `w3c-apg` | ARIA Authoring Practices Guide is the canonical reference |
| Tabs keymap | `--a11y-tabs-keymap` | `arrows+home+end` | Roving tabindex; optional delete key per APG |
| Menu keymap | `--a11y-menu-keymap` | `arrows+escape+enter` | Open/read/close contract; typeahead optional |
| Combobox keymap | `--a11y-combobox-keymap` | `arrows+enter+escape` | aria-expanded + listbox popup + activedescendant |
| Dialog keymap | `--a11y-dialog-keymap` | `escape-close` | Focus trap + labelled title + focus return |
| Listbox vs menu | `--a11y-listbox-vs-menu` | `value-vs-action` | Listbox selects values; menu triggers actions |
| Grid policy | `--a11y-grid-policy` | `interactive-cells-only` | Static data stays native table |
| Accordion keymap | `--a11y-accordion-keymap` | `enter+space` | aria-expanded on the trigger button |
| Tree keymap | `--a11y-tree-keymap` | `arrows+left-collapse` | Hierarchical nav per APG tree pattern |
| Pattern tests required | `--a11y-pattern-tests-required` | `keyboard+sr` | Each widget ships with keymap + screen reader tests |

Consume them by linking `assets/css/aria-patterns-widgets.css` at the app root — it carries the shared selected-tab, popup, and focus styling keyed to `var(--a11y-...)` state conventions — and treat each keymap token as the widget's public contract: components consume the keymap tokens rather than inventing per-instance bindings, and any deviation from `--a11y-pattern-source` (w3c-apg) requires a review exception.

## 4. Composition

- **Composes with keyboard-navigation and focus-management:** patterns define the keymap; those skills define the page-level circuit around the widget.
- **Composes with component-recipes (skill-component-recipes):** recipes give visual/UX specs (tabs guide 09, dropdowns guide 10); this skill gives the AT contract.
- **Composes with screen-readers:** every pattern ships with an NVDA/VoiceOver test script, not just automated checks.

## 5. Signature Patterns

- **Pattern library centralization:** tabs/menu/combobox/dialog implemented once, tested once, consumed everywhere - pattern drift across teams is how keymaps fork.
- **APG + recipes pairing:** for each widget, the APG pattern (AT contract) and the component recipe (visual spec) are linked documents.

## 6. Real-World Use Cases

- **Building the widget layer of a design system: tabs, menus, comboboxes, dialogs, grids.**
- **Fixing custom widgets that 'look accessible' but break in NVDA/VoiceOver.**
- **Reviewing third-party component libraries before adoption.**

## 7. Combination Notes

### With other accessibility skills

- **Good with keyboard-navigation and focus-management:** the APG pattern supplies the within-widget keymap; keyboard-navigation enforces Tab-into/out-of behavior and focus-management owns where focus lands on open/close — a tabs widget is correct only when all three agree.
- **Good with aria-fundamentals:** patterns are vocabulary in combination — roles, states, and names from fundamentals are the building blocks the APG patterns assemble; skipping fundamentals produces copy-paste markup nobody can debug.
- **Good with screen-readers, testing-audit, and forms-errors:** each widget's `--a11y-pattern-tests-required` contract demands keymap plus screen reader tests, and comboboxes sit at the intersection with forms — aria-expanded/activedescendant wiring must coexist with labels and error descriptions.
- **No caution or avoid list:** APG fidelity composes with every sibling; the enemy is pattern drift, not partner conflict.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and glassmorphism:** all three restyle widget surfaces freely (underlines, fills, frosted popups) without touching the role/keymap contract — visual identity lives in CSS while the AT contract stays APG-exact.
- **Caution with collage-art:** collage-style deconstruction can fragment widget affordances (tabs without tab shapes, menus without visual containment); if the style obscures what a control is, the pattern's semantics and visuals drift apart and AT users get narration that contradicts the screen.

### With motion skills (companion repo skill-animation)

- **Good affinity with micro-interactions and feedback-confirmation:** selection changes, popup reveals, and confirmations are pattern-level events that deserve token-driven motion — animating the *surface* while aria-selected/aria-expanded flip immediately keeps state truthful for AT.
- **No caution list:** motion is an overlay on state here, not a substitute for it; reduced-motion users still get instant state updates, so no animation partner conflicts with the APG contract.

## 8. Anti-Patterns

- **Invented keymaps** — a tab widget where Escape or J moves - users' muscle memory from every other product breaks
- **Menu/select confusion** — role=menu for a value picker breaks form narration and mobile behavior
- **Stale pattern state** — aria-selected frozen on the first tab because selection logic never touched attributes
- **Grid abuse** — arrow-key grids wrapping static tables nobody needs to navigate cell-by-cell

### Accessibility Notes

This skill exists to make AT users first-class widget consumers: the APG keymaps are the interface contract they have learned product-wide, so partial patterns are worse than none. The fallback rule is strict: if a widget cannot implement its APG pattern fully, ship the native HTML equivalent (select, details, dialog) instead of a partial pattern. In practice that means each widget is implemented once in the pattern library with its full role structure and keymap, state attributes update on every selection change, async results narrate via live regions or aria-activedescendant, and the widget ships only after keyboard plus screen reader tests (`--a11y-pattern-tests-required`) pass on the supported matrix.

## 9. Code Examples

### Example 1 — APG-exact tabs widget (roving tabindex, arrows, Home/End)

Tokens: `assets/css/aria-patterns-widgets.css`

```html
<div class="tabs">
  <div role="tablist" aria-label="Account sections">
    <button role="tab" id="tab-profile" aria-controls="panel-profile" aria-selected="true" tabindex="0">Profile</button>
    <button role="tab" id="tab-billing" aria-controls="panel-billing" aria-selected="false" tabindex="-1">Billing</button>
    <button role="tab" id="tab-security" aria-controls="panel-security" aria-selected="false" tabindex="-1">Security</button>
  </div>
  <div role="tabpanel" id="panel-profile" aria-labelledby="tab-profile" tabindex="0">Profile settings…</div>
  <div role="tabpanel" id="panel-billing" aria-labelledby="tab-billing" tabindex="0" hidden>Billing history…</div>
  <div role="tabpanel" id="panel-security" aria-labelledby="tab-security" tabindex="0" hidden>Security options…</div>
</div>
<style>
  .tabs { font: 14px/1.5 system-ui, sans-serif; max-width: 420px; }
  [role="tablist"] { display: flex; gap: 4px; border-bottom: 2px solid #d4d4d4; }
  [role="tab"] { padding: 10px 14px; border: none; background: none; cursor: pointer; border-radius: 6px 6px 0 0; }
  [role="tab"][aria-selected="true"] { font-weight: 600; box-shadow: inset 0 -2px #2563EB; }
  [role="tab"]:focus-visible { outline: 2px solid #1D4ED8; outline-offset: -2px; }
  [role="tabpanel"] { padding: 14px 4px; }
</style>
<script>
  // --a11y-tabs-keymap: arrows+home+end with roving tabindex (per --a11y-pattern-source: w3c-apg)
  const tabs = [...document.querySelectorAll('[role="tab"]')];
  const panels = [...document.querySelectorAll('[role="tabpanel"]')];
  function selectTab(tab) {
    tabs.forEach((t, i) => {
      const on = t === tab;
      t.setAttribute('aria-selected', on);   // state must match DOM on every change
      t.tabIndex = on ? 0 : -1;              // roving tabindex: one stop in Tab order
      panels[i].hidden = !on;
    });
    tab.focus();
  }
  document.querySelector('[role="tablist"]').addEventListener('keydown', (e) => {
    const i = tabs.indexOf(document.activeElement);
    if (i === -1) return;
    const next = { ArrowRight: (i + 1) % tabs.length, ArrowLeft: (i + tabs.length - 1) % tabs.length,
                   Home: 0, End: tabs.length - 1 }[e.key];
    if (next !== undefined) { e.preventDefault(); selectTab(tabs[next]); }
  });
  tabs.forEach(t => t.addEventListener('click', () => selectTab(t)));
</script>
```

### Example 2 — Menu as actions (vs select for values) with live announcements

Tokens: `assets/css/aria-patterns-widgets.css`

```html
<div class="menu-wrap">
  <button id="actions-btn" aria-haspopup="menu" aria-expanded="false">Record actions</button>
  <ul role="menu" id="actions-menu" hidden>
    <li role="none"><button role="menuitem" tabindex="-1">Duplicate record</button></li>
    <li role="none"><button role="menuitem" tabindex="-1">Archive record</button></li>
  </ul>
</div>
<p id="menu-status" class="sr-only" role="status" aria-live="polite"></p>
<style>
  .menu-wrap { display: inline-block; position: relative; font: 14px/1.5 system-ui, sans-serif; }
  #actions-btn { padding: 10px 16px; border-radius: 8px; border: 1px solid #d4d4d4; cursor: pointer; }
  #actions-btn:focus-visible { outline: 2px solid #1D4ED8; outline-offset: 2px; }
  [role="menu"] { position: absolute; margin: 4px 0 0; padding: 4px; list-style: none; background: #fff; border: 1px solid #d4d4d4;
                  border-radius: 8px; min-width: 180px; box-shadow: 0 4px 12px rgb(0 0 0 / 0.1); }
  [role="menuitem"] { width: 100%; text-align: left; padding: 8px 10px; border: none; background: none; border-radius: 6px; cursor: pointer; }
  [role="menuitem"]:focus { background: #eff6ff; }
  .sr-only { position: absolute; width: 1px; height: 1px; margin: -1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
</style>
<script>
  // --a11y-menu-keymap: arrows+escape+enter; this menu triggers ACTIONS (value pickers use listbox/select)
  const btn = document.getElementById('actions-btn');
  const menu = document.getElementById('actions-menu');
  const items = [...menu.querySelectorAll('[role="menuitem"]')];
  const status = document.getElementById('menu-status');
  function openMenu() { menu.hidden = false; btn.setAttribute('aria-expanded', 'true'); items[0].focus(); }
  function closeMenu(restoreFocus = true) { menu.hidden = true; btn.setAttribute('aria-expanded', 'false'); if (restoreFocus) btn.focus(); }
  btn.addEventListener('click', () => (menu.hidden ? openMenu() : closeMenu()));
  menu.addEventListener('keydown', (e) => {
    const i = items.indexOf(document.activeElement);
    if (e.key === 'Escape') { e.preventDefault(); closeMenu(); }
    if (e.key === 'ArrowDown') { e.preventDefault(); items[(i + 1) % items.length].focus(); }
    if (e.key === 'ArrowUp')   { e.preventDefault(); items[(i - 1 + items.length) % items.length].focus(); }
  });
  items.forEach(item => item.addEventListener('click', () => {
    closeMenu(); status.textContent = `${item.textContent} completed`; // action results narrate politely
  }));
</script>
```

## 10. Implementation Checklist

- [ ] Every composite widget implements its APG pattern per `--a11y-pattern-source`, with the canonical keymap token (e.g. `--a11y-tabs-keymap`) as its contract.
- [ ] Composite widgets use roving tabindex: arrows move within, Tab exits after the widget's last stop.
- [ ] Selection and expansion state updates ARIA state on every change (aria-selected, aria-expanded, aria-activedescendant).
- [ ] Dialogs follow `--a11y-dialog-keymap`: labelled title, focus trap, Escape closes, focus returns to the trigger.
- [ ] Value pickers use listbox/select and action triggers use menu, per `--a11y-listbox-vs-menu`.
- [ ] Static data ships as native `<table>`; grid is reserved for interactive cells per `--a11y-grid-policy`.
- [ ] Async results and action completions narrate via polite live regions or aria-activedescendant.
- [ ] Each widget ships with keyboard + screen reader tests per `--a11y-pattern-tests-required` before merge.

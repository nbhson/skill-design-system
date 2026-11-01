---
name: dropdowns-menus
description: Selects, menus, popovers, and tooltips: the value-vs-action distinction, keyboard contracts, and positioning that stays in viewport.
tags: [dropdowns, menus, combobox, popover, tooltip]
related: [forms-inputs, buttons-badges, command-palette]
---

# Component Recipe: Dropdowns & Menus

## 1. Definition

Dropdown-family components divide into value pickers (select, combobox — choose a value) and action menus (dropdown menu, context menu — trigger a command), plus the popover/tooltip satellites. Confusing them is the classic bug: a menu-as-select breaks form narration and mobile behavior. The recipe covers each pattern's contract, keyboard map, positioning (floating-ui, viewport-aware flip/shift), and the native-select default.

## 2. Core Principles

- **Value vs action is the first decision:** choosing a value = select/combobox; triggering a command = menu — the distinction drives semantics and keymaps.
- **Native select is the default:** unless styling demands more, `<select>` carries mobile pickers, autofill, and AT support for free.
- **Menus are APG-exact:** role=menu/menuitem, arrows navigate, Escape closes, focus returns to trigger — invented keymaps break muscle memory (a11y repo guide 06).
- **Combobox = input + listbox:** aria-expanded, aria-activedescendant or focus-managed options, typeahead, and announced result counts.
- **Positioning never clips:** floating positioning with flip/shift keeps popovers in viewport — overflow: hidden ancestors are tested, not assumed.
- **Tooltips are hover supplements, never the only label:** dismissible, hoverable, persistent (WCAG 1.4.13) — and the control carries its own accessible name.
- **Popovers escape their DOM box:** position: fixed/absolute rendering (top layer) so parent overflow/stacking contexts cannot clip them.
- **Nested menus are capped:** one submenu level; deeper IA becomes a dialog or page — depth 3 menus are unusable on touch.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Value vs action | `--comp-value-vs-action` | select-vs-menu | The first decision; drives everything |
| Select default | `--comp-select-default` | native-select | Custom only with justification |
| Menu role set | `--comp-menu-role-set` | menu/menuitem | APG structure |
| Menu keymap | `--comp-menu-keymap` | arrows+escape+enter | APG menu contract |
| Combobox structure | `--comp-combobox-structure` | input+listbox+activedescendant | APG combobox contract |
| Combobox announce | `--comp-combobox-announce` | result-count-polite | Filtered results narrated |
| Popover positioning | `--comp-popover-positioning` | floating-ui-flip-shift | Never clipped by ancestors |
| Tooltip contract | `--comp-tooltip-contract` | dismissible-hoverable-persistent | WCAG 1.4.13 |
| Menu focus return | `--comp-menu-focus-return` | trigger-on-close | Escape returns focus |
| Menu nesting cap | `--comp-menu-nesting-cap` | 1-submenu | Deeper IA becomes page/dialog |

Consume them by linking `assets/css/dropdowns-menus.css` once and reading `var(--comp-menu-...)`, `var(--comp-combobox-...)`, and `var(--comp-popover-positioning)` from widget CSS and behavior code. The tokens are contracts first: a widget that does not implement `--comp-menu-keymap` or `--comp-menu-focus-return` exactly is not a menu, and a custom picker without a written justification against `--comp-select-default` does not ship.

## 4. Composition

- **Composes with forms-inputs:** combobox/select are form fields — the field wiring recipe wraps them, so labels, descriptions, and error narration come from the form contract, not from this one.
- **Composes with accessibility-wiring and a11y repo guide 06:** APG menu/combobox contracts are the AT layer of this recipe — wiring verifies roles, keymaps, focus return, and announced results.
- **Composes with navigation-patterns:** nav overflow collapses into menus; the menu contract is shared, so a nav kebab behaves identically to a toolbar menu.

## 5. Signature Patterns

- **Popover primitive:** one positioning wrapper (floating-ui) powering menus, tooltips, and popovers — flip/shift/escape logic implemented once, so no widget ever re-solves viewport collision on its own.
- **Native-first audit:** every custom dropdown in the codebase justifies itself against `<select>`/`<details>` — custom pickers need custom features to exist, not just a different look.

## 6. Real-World Use Cases

- **Toolbars and row actions** (kebab menus) — the APG action-menu contract in its most common habitat.
- **Filtered pickers** (country, user, tag comboboxes) — input + listbox with typeahead and announced result counts.
- **Audit** — menu-as-select, clipped popovers, tooltip-only labels: the three recurring findings this recipe's checklist targets.

## 7. Combination Notes

### With other component-recipe skills

- **Good with tables-data-grid, forms-inputs, and navigation-patterns:** row actions and filter menus live inside grids; combobox/select are form fields wrapped by the field wiring recipe; nav overflow collapses into menus — the menu contract is shared, and each side owns a distinct layer.
- **Good with buttons-badges, command-palette, tabs-accordions, modals-dialogs, toasts-notifications, cards-lists, empty-loading-error, accessibility-wiring:** triggers are real buttons, the command palette is the keyboard-first cousin of the action menu, menus trigger dialogs and toasts, sit inside card action rows, and are validated by wiring — hosting or triggering never blurs ownership of the popover contract.
- **No caution or avoid list:** as long as value pickers and action menus stay distinct, the dropdown family composes cleanly with everything else.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and glassmorphism:** menus and popovers are small elevated surfaces where these styles excel — flat hairline borders, clean shadows, or translucent panels all slot into the popover primitive's skin without touching the keyboard contract.
- **Caution with skeuomorphism:** hyper-realistic drop shadows, glossy highlights, and heavy chrome tend to obscure the focus ring and the selected-item state — if the style is used, the focus indicator and `aria-selected`/`aria-activedescendant` highlight must win visually over decoration.

### With motion skills (companion repo skill-animation)

- **Good affinity with entrance-exit and micro-interactions:** menus, popovers, and tooltips are the canonical enter/exit surfaces — short opacity/translate opens, instant Escape closes, hover states at micro-interaction scale, all token-driven and never delaying keyboard use.

## 8. Anti-Patterns

- **Menu-as-select** — role=menu picking form values - narration and mobile pickers break
- **Clipped popovers** — menus amputated by overflow: hidden ancestors
- **Tooltip-only labels** — icon buttons whose name lives only in hover
- **Submenu spirals** — three-deep cascades unusable by keyboard and touch alike

### Accessibility Notes

This recipe implements the APG menu/combobox/listbox patterns plus WCAG 1.4.13 (tooltip contract): keymaps, focus return, announced results, and dismissible tooltips — dropdown family is where invented keymaps do the most damage. Menus are `role="menu"` with `role="menuitem"` children, arrow-key navigation, Escape to close, and focus returning to the trigger on close; comboboxes pair an input with a listbox via `aria-expanded` and `aria-activedescendant`, announce filtered result counts politely, and support typeahead; tooltips are dismissible (Escape), hoverable (the pointer can travel to them), and persistent, and the control they describe always carries its own accessible name so the tooltip is a supplement, never the label. The fallback rule: when a custom picker cannot complete its APG contract, ship the native select — a plain-looking select that works beats a beautiful one that narrates nothing.

## 9. Code Examples

### Example 1 — APG action menu with arrows, Escape, and focus return

Tokens: `assets/css/dropdowns-menus.css`

```html
<div class="menu-wrap">
  <button class="menu-trigger" id="row-menu-btn" aria-haspopup="menu" aria-expanded="false">Row actions</button>
  <ul role="menu" id="row-menu" aria-labelledby="row-menu-btn" hidden>
    <li role="none"><button role="menuitem" type="button">Duplicate</button></li><li role="none"><button role="menuitem" type="button">Rename</button></li><li role="none"><button role="menuitem" type="button">Archive</button></li>
  </ul>
</div>
<script>
  const btn = document.getElementById('row-menu-btn'), menu = document.getElementById('row-menu');
  const items = [...menu.querySelectorAll('[role="menuitem"]')];
  function openMenu() {
    menu.hidden = false; btn.setAttribute('aria-expanded', 'true'); items[0].focus(); // focus enters the menu
  }
  function closeMenu(returnFocus = true) {             // --comp-menu-focus-return: trigger-on-close
    menu.hidden = true; btn.setAttribute('aria-expanded', 'false');
    if (returnFocus) btn.focus();
  }
  btn.addEventListener('click', () => btn.getAttribute('aria-expanded') === 'true' ? closeMenu() : openMenu());
  menu.addEventListener('keydown', e => {
    const i = items.indexOf(document.activeElement);
    const next = { ArrowDown: (i + 1) % items.length, ArrowUp: (i + items.length - 1) % items.length, Home: 0, End: items.length - 1 }[e.key];
    if (next != null) { e.preventDefault(); items[next].focus(); }
    if (e.key === 'Escape') { e.preventDefault(); closeMenu(); }     // APG: Escape closes, focus returns
  });
  items.forEach(item => item.addEventListener('click', () => closeMenu()));
</script>
<style>
  .menu-wrap { position: relative; display: inline-block; }
  .menu-trigger { font: 500 14px/1 Inter, system-ui, sans-serif; padding: 8px 14px; border: 1px solid #D4D4D4; border-radius: 8px; background: #fff; cursor: pointer; color: #171717; }
  .menu-trigger:focus-visible { outline: 2px solid #2563EB; outline-offset: 2px; }  [role="menu"] { position: absolute; top: calc(100% + 4px); left: 0; z-index: 10; min-width: 160px; margin: 0; padding: 4px; list-style: none; background: #fff; border: 1px solid #D4D4D4; border-radius: 8px; box-shadow: 0 4px 12px rgba(0, 0, 0, .08); }
  [role="menuitem"] { display: block; width: 100%; text-align: left; padding: 8px 10px; border: none; border-radius: 6px; font: 14px/1.4 Inter, system-ui, sans-serif; color: #171717; background: none; cursor: pointer; }
  [role="menuitem"]:hover, [role="menuitem"]:focus { background: #F5F5F5; outline: none; }
</style>
```

### Example 2 — Combobox with activedescendant + 1.4.13-compliant tooltip

Tokens: `assets/css/dropdowns-menus.css`

```html
<label class="cb-label" id="assignee-label" for="assignee">Assignee</label>
<div class="cb-wrap">
  <input class="cb-input" id="assignee" role="combobox" aria-expanded="false" aria-controls="assignee-list" aria-autocomplete="list" aria-labelledby="assignee-label" autocomplete="off">
  <ul class="cb-list" id="assignee-list" role="listbox" hidden></ul>
  <span class="tip-anchor">
    <button class="tip-btn" type="button" aria-label="Assignee rules" aria-describedby="assignee-tip">?</button><span class="tooltip" id="assignee-tip" role="tooltip">Members of the current workspace only.</span>
  </span>
</div>
<p class="cb-status" role="status" aria-live="polite"></p>
<script>
  const people = ['Ana Torres', 'Bilal Khan', 'Chen Wei', 'Dana Lee'];
  const input = document.getElementById('assignee'), list = document.getElementById('assignee-list'), status = document.querySelector('.cb-status');
  let options = [], active = -1;
  input.addEventListener('input', () => {
    const q = input.value.toLowerCase();
    options = people.filter(p => p.toLowerCase().includes(q));   // typeahead filter
    list.innerHTML = options.map(o => `<li role="option" aria-selected="false" id="opt-${o.replace(/\W/g, '')}">${o}</li>`).join('');
    list.hidden = options.length === 0; input.setAttribute('aria-expanded', String(!list.hidden));
    input.removeAttribute('aria-activedescendant'); active = -1;
    status.textContent = options.length + ' result' + (options.length === 1 ? '' : 's'); // --comp-combobox-announce
  });
  input.addEventListener('keydown', e => {
    if (e.key !== 'ArrowDown' && e.key !== 'ArrowUp') return; else e.preventDefault();
    active = e.key === 'ArrowDown' ? Math.min(active + 1, options.length - 1) : Math.max(active - 1, 0);
    [...list.children].forEach((li, i) => li.setAttribute('aria-selected', i === active));
    input.setAttribute('aria-activedescendant', [...list.children][active]?.id); // --comp-combobox-structure
  });
  list.addEventListener('click', e => { if (!e.target.matches('[role="option"]')) return; input.value = e.target.textContent; list.hidden = true; input.setAttribute('aria-expanded', 'false'); });
  // Tooltip: dismissible (Escape), hoverable, persistent — WCAG 1.4.13
  document.querySelector('.tip-btn').addEventListener('keydown', e => { if (e.key === 'Escape') document.getElementById('assignee-tip').classList.remove('show'); });
</script>
<style>
  .cb-label { display: block; font: 600 13px/1.4 Inter, system-ui, sans-serif; margin-bottom: 4px; } .cb-wrap { position: relative; display: flex; align-items: center; gap: 8px; max-width: 320px; }
  .cb-input { flex: 1; padding: 8px 10px; font: 14px/1.4 Inter, system-ui, sans-serif; border: 1px solid #D4D4D4; border-radius: 8px; }
  .cb-list { position: absolute; top: calc(100% + 4px); left: 0; right: 0; z-index: 10; margin: 0; padding: 4px; list-style: none; background: #fff; border: 1px solid #D4D4D4; border-radius: 8px; box-shadow: 0 4px 12px rgba(0, 0, 0, .08); }
  .cb-list [role="option"] { padding: 8px 10px; font: 14px/1.4 Inter, system-ui, sans-serif; border-radius: 6px; cursor: pointer; }
  .cb-list [aria-selected="true"] { background: #F5F5F5; }
  .cb-status { font: 13px/1.4 Inter, system-ui, sans-serif; color: #737373; }
  .tip-anchor { position: relative; }
  .tip-btn { width: 24px; height: 24px; border-radius: 50%; border: 1px solid #D4D4D4; background: #fff; font: 600 12px/1 Inter, system-ui, sans-serif; cursor: pointer; }
  .tip-btn:focus-visible { outline: 2px solid #2563EB; outline-offset: 2px; }
  .tooltip { position: absolute; bottom: calc(100% + 6px); left: 50%; transform: translateX(-50%); width: max-content; max-width: 220px; padding: 6px 10px; font: 12px/1.4 Inter, system-ui, sans-serif; color: #fff; background: #171717; border-radius: 6px; visibility: hidden; opacity: 0; transition: opacity 150ms ease; }
  .tip-anchor:hover .tooltip, .tip-btn:focus-visible + .tooltip, .tooltip.show { visibility: visible; opacity: 1; }
</style>
```

## 10. Implementation Checklist

- [ ] Every dropdown-family widget passed the value-vs-action test (`--comp-value-vs-action`): form values use select/combobox, commands use menus — zero menu-as-select anywhere.
- [ ] Custom pickers carry a written justification against `--comp-select-default`; anything `<select>` serves ships native.
- [ ] Menus implement the APG contract (`--comp-menu-role-set`, `--comp-menu-keymap`): arrows navigate, Enter activates, Escape closes, and focus returns to the trigger (`--comp-menu-focus-return`).
- [ ] Comboboxes wire `aria-expanded`, `aria-activedescendant` (`--comp-combobox-structure`) and announce filtered result counts politely (`--comp-combobox-announce`).
- [ ] All popovers position with flip/shift (`--comp-popover-positioning`) and were tested inside `overflow: hidden` ancestors — nothing clips.
- [ ] Tooltips satisfy 1.4.13 (`--comp-tooltip-contract`: dismissible, hoverable, persistent) and every control carries its own accessible name.
- [ ] Menu nesting respects `--comp-menu-nesting-cap` (one submenu); deeper hierarchies were redesigned as pages or dialogs.


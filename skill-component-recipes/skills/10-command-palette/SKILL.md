---
name: command-palette
description: Cmd-K overlays — fuzzy search over actions and objects, keyboard-first UX, recent/frecency ranking, and the analytics loop.
tags: [command-palette, cmd-k, fuzzy-search, keyboard, search]
related: [navigation-patterns, modals-dialogs, dropdowns-menus]
---

# Component Recipe: Command Palette & Search

## 1. Definition

The command palette (Cmd-K) is the power-user surface: one overlay searching across actions ("Create project"), navigation ("Go to settings"), and objects ("Open ACME deal"). The recipe covers the overlay contract (modal focus, trap-and-return), the search index (actions + objects + navigation), fuzzy matching, frecency ranking, and the analytics loop that records which commands run — palettes are data products as much as UI. Because the palette is inherently a keyboard-only interface, its dialog and combobox contracts (focus management, narration, Escape behavior) are core features, not polish.

## 2. Core Principles

- **One palette, three item types:** actions, navigation, and objects — the index is typed and each type renders a distinct group with a distinct verb.
- **Keyboard-first contract:** Cmd-K/Ctrl-K opens, arrows navigate, Enter runs, Escape closes — mouse is the fallback, not the target.
- **Fuzzy matching with typeahead:** matching tolerates typos and abbreviations ("usr set" finds User Settings) — strict prefix matching starves palettes.
- **Frecency + recency ranking:** recently and frequently used items surface first — the palette learns the user instead of returning the same order every time.
- **Empty state teaches:** a first-run palette shows examples ("Try: create, invite, export") — the blank palette is a dead end.
- **Dialog contract underneath:** the palette is a dialog — focus trap-and-return, Escape, and scroll lock all apply (modals-dialogs recipe).
- **Results are announced:** result counts narrate politely as the user types (combobox contract).
- **Analytics close the loop:** query logs with no-result tracking feed the index — "nothing found" entries are roadmap data.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Hotkey | `--comp-palette-hotkey` | `cmd-k/ctrl-k` | Global open; documented app-wide |
| Item types | `--comp-palette-item-types` | `action,nav,object` | Typed index; grouped rendering |
| Keymap | `--comp-palette-keymap` | `arrows+enter+escape` | Keyboard-first contract |
| Matching | `--comp-palette-matching` | `fuzzy+typeahead` | Tolerant matching; no strict-prefix |
| Ranking | `--comp-palette-ranking` | `frecency+recency` | Learns per user |
| Dialog contract | `--comp-palette-dialog-contract` | `trap-and-return` | Dialog recipe underneath |
| Empty state | `--comp-palette-empty-state` | `teaching-examples` | First-run shows try-queries |
| Announce | `--comp-palette-announce` | `result-count-polite` | Combobox narration |
| Analytics | `--comp-palette-analytics` | `query+selection-logged` | No-result tracking feeds roadmap |
| Highlight | `--comp-palette-highlight` | `match-substring-marked` | Matches visually marked |

Consume them by linking `assets/css/command-palette.css` once at the app root; structural styling then references `var(--comp-...)` — most tokens here are policies (keymaps, ranking, announcement) consumed by the palette component's JavaScript rather than CSS, and that is by design: the palette's contract is behavioral. Only the highlight treatment and dialog chrome resolve to CSS values; everything else is enforced in code review against this table.

## 4. Composition

- **Composes with modals-dialogs:** the overlay contract (trap/return/Escape/scrim) is the dialog recipe — the palette does not re-invent focus management, it consumes the Dialog primitive and adds a combobox.
- **Composes with navigation-patterns:** "Go to..." items make the palette a navigation accelerant on top of the nav system — deep IA becomes one keystroke away, and palette nav entries derive from the same route state that drives `aria-current`.
- **Composes with dropdowns-menus:** the result list follows the combobox contract (announced counts, `aria-activedescendant`) — the same list semantics menus use, applied to search results.

## 5. Signature Patterns

- **Typed command registry:** features register actions into the palette index with `(type, verb, keywords, handler)` — palette coverage grows with features automatically, and no team has to remember to "add it to the palette" as a separate task.
- **No-result analytics:** a weekly review of zero-result queries turns missing commands into tickets — the palette's index is maintained like a search engine's, with query + selection logging (`--comp-palette-analytics`) as the data source.

## 6. Real-World Use Cases

- **Power-user products:** IDEs, CRMs, project tools, and admin consoles where the palette is the fastest path to any action.
- **Deep-IA products:** palettes flatten navigation for large apps — five sidebar levels collapse into "Go to billing".
- **Audit:** palettes missing actions, strict matching that finds nothing, and no analytics loop.

## 7. Combination Notes

### With other component-recipe skills

- **Pairs naturally with navigation-patterns, modals-dialogs, and dropdowns-menus:** navigation supplies the "Go to" items, dialogs supply the overlay contract, and menus supply the combobox list semantics — the palette is the composition of all three.
- **Pairs with tables-data-grid, buttons-badges, forms-inputs, tabs-accordions, cards-lists, toasts-notifications, and empty-loading-error:** palette actions open records, run button-system verbs, pre-fill forms, and report failure via toasts — the palette is an accelerator into every other recipe. The caution/avoid lists are empty — deliberately: a palette conflicts with no sibling; the failure mode is under-composition (navigation-only palettes).

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, glassmorphism, and class-morphism:** a palette is a focused chrome-light overlay — minimalist restraint keeps results scannable, glass surfaces fit the transient overlay idiom, and class-morphism's crisp grouping suits typed result groups.
- **Caution with skeuomorphism:** heavy faux-3D chrome slows scanning in a list surface built for speed; if a skeuomorphic theme is mandated, confine it to the input field and keep the result rows flat.

### With motion skills (companion repo skill-animation)

- **Good affinity with entrance-exit and micro-interactions:** the overlay fades/scales in with duration tokens, the active item highlight follows the arrow keys, and highlight marking applies instantly — motion reinforces the keyboard rhythm without delaying it.
- **Caution is empty, with one hard rule:** result filtering must never animate the list itself — retyping re-sorts results, and animated reordering makes the palette feel laggy; apply motion to the overlay, not the results.

## 8. Anti-Patterns

- **Silent palettes** — overlays that grab focus and narrate nothing
- **Strict matching** — 'proj cr' finding nothing while the user stares
- **Static ranking** — every query returning the same order - the palette never learns
- **Actionless palettes** — navigation-only palettes where users expected verbs

### Accessibility Notes

The palette is the keyboard-accessibility showcase: it IS a keyboard-only interface, so the dialog + combobox contracts must be airtight — focus management, narration, and Escape behavior are its core features, not polish (WCAG 2.1.1, 4.1.3, and the APG combobox pattern). Concretely: `role="dialog"` with an accessible name, focus enters the input on open and returns to the trigger on close, `aria-activedescendant` tracks the highlighted option, result counts announce politely in a live region, and Escape always closes. The fallback: if analytics/fuzzy search cannot ship in v1, launch with a static typed list + arrow/enter keyboard contract — a simple, narrated palette beats a broken search.



## 9. Code Examples

### Example 1 — Palette overlay: dialog contract, typed groups, narration

Tokens: `assets/css/command-palette.css`

```html
<button id="paletteTrigger" class="palette-trigger">Commands <kbd>⌘K</kbd></button>
<div id="palette" class="palette" hidden>
  <div class="palette-box" role="dialog" aria-modal="true" aria-label="Command palette">
    <input id="pi" role="combobox" aria-expanded="true" aria-controls="pl" aria-activedescendant=""
           autocomplete="off" placeholder="Search actions, navigation, objects…">
    <p id="ps" class="palette-status" role="status" aria-live="polite"></p>
    <ul id="pl" class="palette-list" role="listbox" aria-label="Commands"></ul>
    <p id="pe" class="palette-empty" hidden>Nothing found. Try: <em>create, invite, export</em></p>
  </div>
</div>
<style>
.palette { position: fixed; inset: 0; z-index: 50; display: grid; place-items: start center; padding-top: 12vh; background: rgba(0,0,0,0.45); }
  .palette[hidden] { display: none; }
  .palette-box { width: min(560px, 92vw); background: var(--comp-palette-surface, #fff); border: 1px solid var(--comp-palette-border, #d4d4d4); border-radius: 12px; box-shadow: 0 16px 40px rgba(0,0,0,0.2); font: 14px/1.4 system-ui, sans-serif; }
  .palette-trigger { font: 600 14px system-ui, sans-serif; padding: 10px 16px; cursor: pointer; }
  .palette-input { width: 100%; box-sizing: border-box; font: inherit; border: none; outline: none; padding: 14px 16px; }
  .palette-status, .palette-group, .palette-empty { color: var(--comp-palette-muted, #737373); margin: 0; }
  .palette-status { padding: 4px 16px; }
  .palette-list { list-style: none; margin: 0; padding: 6px; max-height: 320px; overflow: auto; }
  .palette-group { padding: 8px 10px 2px; font-size: 11px; font-weight: 600; text-transform: uppercase; }
  .palette-item { padding: 10px 12px; border-radius: 8px; cursor: pointer; }
  .palette-item[data-active="true"] { background: var(--comp-palette-active, #f0f4ff); outline: none; }
  .palette-item mark { background: var(--comp-palette-highlight, #fef08a); }
  .palette-empty { padding: 16px; }
  @media (prefers-reduced-motion: reduce) { .palette * { transition: none !important; } }
</style>
```

### Example 2 — Search engine: fuzzy match, keymap, frecency, analytics

```html
<script>
  // Typed registry: features register (type, label, keywords, handler)
  const REGISTRY = [
    { type: 'action', label: 'Create project', keywords: 'new add',  run: () => console.log('create') },
    { type: 'nav',    label: 'Go to settings', keywords: 'usr set',  run: () => console.log('nav') },
    { type: 'object', label: 'Open ACME deal', keywords: 'acme',     run: () => console.log('open') },
  ];
  const F = JSON.parse(localStorage.getItem('palette-frecency') || '{}'); // frecency store
  const $ = id => document.getElementById(id);
  let results = [], active = 0, lastTrigger = null;
  // Fuzzy subsequence + word-boundary bonus — "usr set" finds User Settings
  const fuzzy = (q, t) => { q = q.toLowerCase(); t = t.toLowerCase(); let ti = 0, s = 0, last = -2;
    for (const c of q) { if (c === ' ') { s++; continue; }
      const f = t.indexOf(c, ti); if (f < 0) return -1;
      s += f === last + 1 ? 2 : 1; if (!f || /[\s/]/.test(t[f - 1])) s += 2; last = f; ti = f + 1; }
    return s; };
  const search = q => REGISTRY.map(it => ({ it, s: fuzzy(q, it.label + ' ' + it.keywords) }))
    .filter(r => r.s >= 0).sort((a, b) => b.s + (F[b.it.label] || 0) - (a.s + (F[a.it.label] || 0)));
  function render(q) { // grouped rendering + polite result-count narration
    results = search(q); active = 0; $('pl').innerHTML = ''; let g = null;
    results.forEach((r, i) => {
      if (r.it.type !== g) { g = r.it.type;
        const h = document.createElement('li'); h.className = 'palette-group';
        h.textContent = { action: 'Actions', nav: 'Navigation', object: 'Objects' }[g];
        $('pl').appendChild(h); }
      const li = document.createElement('li'); li.className = 'palette-item'; li.id = 'opt-' + i;
      li.setAttribute('role', 'option'); li.textContent = r.it.label; li.onclick = () => run(i); $('pl').appendChild(li);
    });
    $('pe').hidden = results.length > 0;
    $('ps').textContent = q ? results.length + ' result' + (results.length === 1 ? '' : 's') : '';
    if (q && !results.length) console.log('palette:no-result', q); // zero-result analytics
    setActive(0);
  }
  const setActive = i => { active = i;
    [...$('pl').querySelectorAll('.palette-item')].forEach((el, x) => el.dataset.active = x === i);
    if ($('opt-' + i)) $('pi').setAttribute('aria-activedescendant', 'opt-' + i); };
  function run(i) { // frecency update + selection log, then execute
    const it = results[i].it; F[it.label] = (F[it.label] || 0) + 1;
    localStorage.setItem('palette-frecency', JSON.stringify(F));
    console.log('palette:select', $('pi').value, it.label); close(); it.run(); }
  const open  = () => { lastTrigger = document.activeElement; $('palette').hidden = false; $('pi').focus(); render(''); };
  const close = () => { $('palette').hidden = true; if (lastTrigger) lastTrigger.focus(); }; // trap-and-return  $('pi').addEventListener('input', () => render($('pi').value));
  $('pi').addEventListener('keydown', e => { // keymap: arrows + enter + escape
    if (e.key === 'ArrowDown')    { e.preventDefault(); setActive(Math.min(active + 1, results.length - 1)); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); setActive(Math.max(active - 1, 0)); }
    else if (e.key === 'Enter')   { e.preventDefault(); if (results.length) run(active); }
    else if (e.key === 'Escape')  { e.preventDefault(); close(); } });
  $('palette').addEventListener('click', e => { if (e.target.dataset.close !== undefined) close(); });
  document.addEventListener('keydown', e => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') { e.preventDefault(); $('palette').hidden ? open() : close(); } });
  $('paletteTrigger').addEventListener('click', open);
</script>
```
## 10. Implementation Checklist

- [ ] Cmd-K/Ctrl-K opens the palette globally and is documented app-wide (`--comp-palette-hotkey`).
- [ ] The index is typed (`action,nav,object`) and renders grouped results (`--comp-palette-item-types`).
- [ ] The keymap — arrows, Enter, Escape — is implemented and tested (`--comp-palette-keymap`).
- [ ] Matching is fuzzy with typeahead; "usr set" finds User Settings (`--comp-palette-matching`).
- [ ] Ranking blends frecency + recency and persists per user (`--comp-palette-ranking`).
- [ ] The overlay implements the dialog contract: trap, return focus, Escape, scroll lock (`--comp-palette-dialog-contract`).
- [ ] First-run teaching examples ship, zero-result queries are logged, counts announce politely (`--comp-palette-empty-state`, `--comp-palette-analytics`, `--comp-palette-announce`).

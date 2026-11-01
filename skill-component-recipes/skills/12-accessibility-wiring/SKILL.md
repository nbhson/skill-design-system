---
name: accessibility-wiring
description: The cross-cutting a11y layer every recipe shares — focus contracts, announcements, target sizes, and reduced-motion, checked per component.
tags: [accessibility, keyboard, focus, announcements, wcag]
related: [buttons-badges, forms-inputs, modals-dialogs]
---

# Component Recipe: Component A11y Wiring

## 1. Definition

Every recipe in this repo shares one wiring layer: keyboard operability, focus contracts, live announcements, target sizes, contrast through tokens, and reduced-motion behavior. Rather than repeating it twelve times, this guide is the component-level a11y checklist: the per-component pass that verifies a recipe's accessibility wiring before it ships — the bridge between the accessibility repo's WCAG criteria and this repo's components. It exists to make component-level accessibility systematic: the checklist is the deliverable, and it gates every component merge.

## 2. Core Principles

- **Every recipe ships its a11y wiring:** the component spec includes keyboard map, focus behavior, announcements, and target size — not an appendix.
- **Keyboard map before styling:** each component declares its keymap (per APG where applicable) before pixels — the map is the spec.
- **Focus contracts per surface:** what receives focus on open/expand/select, what returns on close/collapse — per component, tested per state.
- **Announcements are designed:** state changes users must hear (loading done, error, selection) wire to live regions or focus moves deliberately.
- **44px touch targets are the floor:** all interactive surfaces meet the effective-target minimum (2.5.8) — dense variants use spacing, not smaller targets.
- **Contrast comes from tokens:** component colors consume validated alias pairs — components never introduce unvalidated colors.
- **Reduced-motion is wired per component:** entrance/exit/loading motion collapses under `prefers-reduced-motion` — the component owns its fallback.
- **The checklist runs per component, per PR:** the wiring pass is a review gate — components merge only with the checklist green.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Keymap | `--comp-wiring-keymap` | `declared-per-component` | The keymap IS the spec |
| Focus contract | `--comp-wiring-focus-contract` | `open/expand/close-returns` | Per surface, tested per state |
| Announce | `--comp-wiring-announce` | `designed-per-state-change` | Live region or focus move, deliberate |
| Target minimum | `--comp-wiring-target-min` | `44px` | WCAG 2.5.8 effective floor |
| Contrast source | `--comp-wiring-contrast-source` | `validated-aliases-only` | No unvalidated colors in components |
| Reduced motion | `--comp-wiring-reduced-motion` | `collapse-with-fallback` | prefers-reduced-motion per component |
| Visible focus | `--comp-wiring-visible-focus` | `3:1-ring` | Focus ring contract (a11y 2.4.13) |
| Names required | `--comp-wiring-name-required` | `all-interactive-named` | Accessible names mandatory |
| Checklist gate | `--comp-wiring-checklist-gate` | `per-component-per-PR` | Review gate; merge requires green |
| Test tier | `--comp-wiring-test-tier` | `keyboard-then-sr` | Keyboard pass first, then screen reader |

Consume them by linking `assets/css/accessibility-wiring.css` and referencing `var(--comp-...)` for the values that are CSS-visible — the 44px target floor (`min-width`/`min-height` on interactive surfaces) and the 3:1 focus ring are style contracts; the rest are process tokens enforced in specs and PR review. `--comp-wiring-checklist-gate` is the operational heart: CI and review templates reference it so the checklist cannot be silently skipped.

## 4. Composition

- **Composes with every recipe here:** this guide is the shared checklist they all reference — buttons, fields, dialogs, tables, palettes, and states each pass the same six-section wiring pass before publishing.
- **Composes with the a11y repo guides 03/04/05/06:** those guides own the criteria layer (keyboard navigation, focus management, target sizes, APG patterns); this wiring implements them at component level — criteria and mechanics stay separated on purpose.
- **Composes with skill-design-review:** the design-side review consumes this checklist as its component section — design and engineering review the same document, so gaps surface before build, not after.

## 5. Signature Patterns

- **The wiring checklist block:** a standardized checklist — keymap, focus, announce, target, contrast, motion — pasted into every component's spec and PR template; identical structure everywhere makes gaps visible in seconds.
- **Wiring-first reviews:** PRs touching components route to reviewers who run the checklist — a11y review is scheduled, not aspirational, and "fix in follow-up" does not pass the gate.

## 6. Real-World Use Cases

- **Design systems:** the gate every new component passes before publishing to the shared library.
- **Component audits:** scoring existing components against the wiring checklist produces a prioritized remediation list.
- **Onboarding engineers:** the single page that teaches component-level accessibility without reading twelve guides.

## 7. Combination Notes

### With other component-recipe skills

- **Pairs with every recipe in this repo — buttons-badges, forms-inputs, tables-data-grid, modals-dialogs, toasts-notifications, navigation-patterns, cards-lists, tabs-accordions, dropdowns-menus, command-palette, and empty-loading-error:** each one's Accessibility Notes section is this checklist applied to its specifics; wiring is what makes those recipes shippable rather than merely styled.
- **The relationship is gate, not peer:** recipes define behavior; this guide verifies it. A component that fails the checklist is an incomplete component, whatever its other qualities — which is why the caution/avoid lists are empty: no recipe is exempt from its own wiring.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** both styles favor high-contrast, low-decoration surfaces where focus rings, target sizes, and token-driven color pairs stay clearly visible — decoration-heavy styles have to work harder to keep the 3:1 focus ring and contrast contracts intact.
- **Caution is empty, with one boundary:** style choices never override wiring — if a style direction (e.g. ultra-subtle borders) breaks the focus-ring or contrast tokens, the wiring wins and the style adapts.

### With motion skills (companion repo skill-animation)

- **Good affinity with reduced-motion and micro-interactions:** this guide owns the collapse behavior (`prefers-reduced-motion` with a documented fallback per component) and motion supplies the token discipline for the micro-transitions that remain — the two contracts are written together in the same spec section.
- **Caution is empty, with one hard rule:** any component adding motion must add its reduced-motion fallback in the same PR — motion without a documented collapse fails the checklist gate.

## 8. Anti-Patterns

- **A11y-as-appendix** — wiring considered after styling, patched in at review
- **Checklist theater** — boxes ticked without running the keyboard pass
- **Style-first specs** — component specs with no keymap or focus section
- **Unvalidated colors** — one-off hex values inside components escaping the token system

### Accessibility Notes

This guide exists to make component-level accessibility systematic: the per-component checklist operationalizes WCAG 2.1.1 (keyboard), 2.4.7/2.4.13 (visible, 3:1 focus indication), 2.5.8 (44px targets), 4.1.3 (status announcements), and 1.4.3 (contrast through validated aliases) across every recipe. The test tier is keyboard first, then screen reader (`--comp-wiring-test-tier`): a keyboard pass catches most wiring failures cheaply, and the screen-reader pass verifies narration quality. The fallback rule: when a component cannot pass the full checklist, it does not ship as a shared primitive — it ships as an app-local component with documented gaps, keeping the system clean.

## 9. Code Examples

### Example 1 — The wiring checklist, rendered as a runnable gate

Tokens: `assets/css/accessibility-wiring.css`

```html
<form class="wiring" id="wiring">
  <h3>Component a11y wiring — per component, per PR</h3>
  <fieldset>
    <legend>Keymap <code>--comp-wiring-keymap</code></legend>
    <label><input type="checkbox" data-sec="keymap"> Keyboard map declared before styling (APG where applicable)</label>
    <label><input type="checkbox" data-sec="keymap"> Every action reachable and operable by keyboard (2.1.1)</label>
  </fieldset>
  <fieldset>
    <legend>Focus <code>--comp-wiring-focus-contract</code></legend>
    <label><input type="checkbox" data-sec="focus"> Open/expand lands focus on a declared target; close/collapse returns to the trigger</label>
    <label><input type="checkbox" data-sec="focus"> Visible focus ring meets 3:1 (2.4.13)</label>
  </fieldset>
  <fieldset>
    <legend>Announce <code>--comp-wiring-announce</code></legend>
    <label><input type="checkbox" data-sec="announce"> State changes users must hear wire to live regions or focus moves (4.1.3)</label>
  </fieldset>
  <fieldset>
    <legend>Target & contrast <code>--comp-wiring-target-min</code></legend>
    <label><input type="checkbox" data-sec="target"> Interactive surfaces meet 44px effective targets (2.5.8)</label>
    <label><input type="checkbox" data-sec="target"> Colors consume validated alias pairs only (1.4.3)</label>
    <label><input type="checkbox" data-sec="target"> All interactive elements have accessible names</label>
  </fieldset>
  <fieldset>
    <legend>Motion <code>--comp-wiring-reduced-motion</code></legend>
    <label><input type="checkbox" data-sec="motion"> Motion collapses under prefers-reduced-motion with a documented fallback</label>
  </fieldset>
  <p id="gate" role="status" aria-live="polite">Incomplete — do not merge.</p>
</form>
<style>
  .wiring { font: 14px/1.5 system-ui, sans-serif; max-width: 560px; border: 1px solid var(--comp-border, #e5e5e5); border-radius: 12px; padding: 20px; }
  .wiring fieldset { border: none; margin: 0 0 12px; padding: 0; }
  .wiring legend { font-weight: 600; color: var(--comp-ink, #171717); margin-bottom: 4px; }
  .wiring label { display: flex; gap: 8px; align-items: start; padding: 8px 4px; min-height: 44px; box-sizing: border-box; cursor: pointer; }
  .wiring input[type="checkbox"] { width: 24px; height: 24px; accent-color: var(--comp-accent, #2563eb); }
  .wiring code { font-size: 12px; color: var(--comp-muted, #737373); }
  #gate { font-weight: 600; margin: 0; color: var(--comp-warn, #b45309); }
  #gate.ok { color: var(--comp-ok, #15803d); }
</style>
<script>
  // The gate: merge requires every section green (--comp-wiring-checklist-gate)
  const boxes = [...document.querySelectorAll('#wiring input[type="checkbox"]')];
  const gate = document.getElementById('gate');
  boxes.forEach(b => b.addEventListener('change', () => {
    const sections = [...new Set(boxes.map(b => b.dataset.sec))];
    const done = sections.every(s => boxes.filter(b => b.dataset.sec === s).every(b => b.checked));
    gate.textContent = done ? 'Wiring checklist green — ready to merge.' : 'Incomplete — do not merge.';
    gate.classList.toggle('ok', done);
  }));
</script>
```

### Example 2 — Component spec template, filled for a Switch

```html
<!-- Spec: Switch — keymap/focus/announce/target/contrast/motion all declared -->
<label class="switch-row">
  <span id="swLabel">Email notifications</span>
  <button id="sw" class="switch" role="switch" aria-checked="true" aria-labelledby="swLabel"></button>
  <span class="sr" id="swLive" role="status" aria-live="polite"></span>
</label>
<style>
  /* Keymap: Space/Enter toggles (declared in spec). Focus: stays on the switch. */
  .switch-row { display: flex; align-items: center; gap: 12px; font: 14px/1.4 system-ui, sans-serif; }
  .switch { width: 44px; height: 44px; padding: 0; border: none; background: transparent; cursor: pointer;
            display: grid; place-items: center; border-radius: 22px; } /* 44px target floor (2.5.8) */
  .switch { position: relative; }
  .switch::before { content: ''; width: 40px; height: 24px; border-radius: 12px; background: var(--comp-switch-off, #d4d4d4); transition: background 150ms ease; }
  .switch::after  { content: ''; position: absolute; width: 20px; height: 20px; border-radius: 50%; background: #fff; transform: translateX(-9px); box-shadow: 0 1px 2px rgba(0,0,0,0.3); transition: transform 150ms ease; }
  .switch[aria-checked="true"]::before { background: var(--comp-switch-on, #15803d); }
  .switch[aria-checked="true"]::after  { transform: translateX(9px); }
  .switch:focus-visible { outline: 3px solid var(--comp-focus, #1d4ed8); outline-offset: 2px; } /* 3:1 ring (2.4.13) */
  .sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }
  @media (prefers-reduced-motion: reduce) { .switch::before, .switch::after { transition: none; } }
</style>
<script>
  // Keymap + announce: Space/Enter toggles; state narrates politely (4.1.3)
  const sw = document.getElementById('sw'), live = document.getElementById('swLive');
  sw.addEventListener('click', () => {
    const on = sw.getAttribute('aria-checked') === 'true';
    sw.setAttribute('aria-checked', String(!on));
    live.textContent = 'Email notifications ' + (!on ? 'on' : 'off');
  });
</script>
```

## 10. Implementation Checklist

- [ ] The component spec declares its keymap, focus contract, announcements, target size, contrast source, and motion fallback before styling (`--comp-wiring-keymap`, `--comp-wiring-focus-contract`).
- [ ] Every interactive element is keyboard-operable with an accessible name (`--comp-wiring-name-required`, WCAG 2.1.1).
- [ ] Focus lands on a declared target on open/expand and returns to the trigger on close/collapse, tested per state.
- [ ] Visible focus indication meets the 3:1 ring contract on every interactive surface (`--comp-wiring-visible-focus`).
- [ ] Interactive surfaces meet the 44px effective target floor, using spacing for dense variants (`--comp-wiring-target-min`).
- [ ] All state changes users must hear announce via live region or deliberate focus move (`--comp-wiring-announce`).
- [ ] Component colors come only from validated alias pairs — zero one-off hexes (`--comp-wiring-contrast-source`).
- [ ] The checklist ran per component, per PR, keyboard pass first then screen reader (`--comp-wiring-checklist-gate`, `--comp-wiring-test-tier`).

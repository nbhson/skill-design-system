---
name: component-microcopy
description: The small strings with big jobs — tooltips, hints, placeholders, helper text, and toggle labels, governed by the placeholder-is-not-a-label rule.
tags: [microcopy, tooltips, placeholders, labels, ux-writing]
related: [forms-labels, writing-principles, copy-audit]
---

# UX Writing Guide: Component Microcopy

## 1. Definition

Component microcopy is the connective tissue of UI: tooltips, hint text, placeholder examples, helper text, toggle labels, and section headers. Small strings, large cumulative effect — a settings page is nothing but microcopy stacked in rows. The discipline covers what each string type is for (the hint persists, the placeholder is an example and disappears, the tooltip is a supplement), the placeholder-is-not-a-label rule, and the writing mechanics: parallel phrasing in lists, consistent verb forms in toggles, and tooltip length budgets. Because these strings live inside components rather than pages, they are specified per component — with budgets and examples shipped alongside the component doc, not improvised at build time.

## 2. Core Principles

- **Placeholders are examples, not labels:** the placeholder disappears on focus and must never carry the only instruction — a field with only a placeholder is unlabeled the moment the user types (WCAG 3.3.2).
- **Hints persist, placeholders vanish:** helper text lives below the field and stays; format hints (`MM/YYYY`) may appear inside the field but repeat in the label context so they survive focus.
- **Tooltips supplement, never replace:** the control carries its own accessible name — a tooltip is bonus context delivered under the WCAG 1.4.13 contract (dismissible, hoverable, persistent).
- **Parallel phrasing in lists:** menu items, settings rows, and options share grammatical form — verbs with verbs, nouns with nouns; mixed grammar reads as broken.
- **Toggles read as states or actions, one way:** `Email notifications: On` — not `Enable email notifications` beside a switch that already shows state; pick a convention per system and hold it.
- **Microcopy has length budgets:** tooltips ~100 chars, hints one line, toggle labels 1–3 words — budgets are not a constraint on quality, they are what forces clarity.
- **Link labels are destinations:** `Pricing` or `View pricing`, never `Click here` — links are read out of context by assistive technology and scanned out of context by everyone (WCAG 2.4.4).
- **Consistency is enforced by inventory:** shipped strings live in the string inventory (copy-audit guide) with their component, so identical situations produce identical words.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Placeholder role | `--uxw-placeholder-role` | `example-only` | Never the only label (3.3.2) |
| Hint persistence | `--uxw-hint-persistence` | `always-visible` | Helper text below the field |
| Tooltip budget | `--uxw-tooltip-budget` | `~100-chars` | Supplement; control has own name |
| Tooltip contract | `--uxw-tooltip-contract` | `dismissible-hoverable-persistent` | WCAG 1.4.13 behavior triple |
| Toggle label form | `--uxw-toggle-label-form` | `state-or-action-pick-one` | Consistent per system |
| List parallelism | `--uxw-list-parallelism` | `shared-grammar` | Menu/option phrasing in parallel |
| Link label rule | `--uxw-link-label-rule` | `destination-named` | No 'click here' (2.4.4) |
| Hint length | `--uxw-hint-length` | `1-line` | Budget forces precision |
| Microcase | `--uxw-microcase` | `sentence-case` | Inherited from writing-principles |
| String inventory | `--uxw-string-inventory` | `component-owned` | Shipped strings tracked (copy-audit) |

Consume these spec tokens by linking `assets/css/component-microcopy.css` at the app root and reading `var(--uxw-...)` from component-level styles and lint rules — they are behavior contracts expressed as custom properties, so a placeholder styled without the `example-only` role or a tooltip missing the 1.4.13 triple is a checkable violation, not a taste debate.

## 4. Composition

- **Composes with forms-labels (guide 08):** field labels, hints, and errors are microcopy's densest surface — the string budgets and slot contracts defined here are shared with the form layer.
- **Composes with component-recipes (dropdowns-menus + forms-inputs):** menu parallelism and field wiring are the component layer; microcopy supplies the strings those components render.
- **Composes with copy-audit (guide 12):** the string inventory is where microcopy consistency is enforced — every shipped string is tracked against its component so drift is detectable, not anecdotal.

## 5. Signature Patterns

- **The string spec per component:** every component doc ships its string slots (label / hint / placeholder / tooltip) with budgets and examples — copy is spec, not afterthought. A button doc without its label slot is incomplete the way a button doc without its disabled state is incomplete.
- **The parallelism pass:** before shipping lists or menus, read all items as one column — `Add user / Removing / Deletion of file` stops being invisible when read vertically; broken grammar jumps out, and the fix is choosing one form.

## 6. Real-World Use Cases

- **Design systems documenting component copy slots** — defining label/hint/placeholder/tooltip budgets once, so every product team writes within the same contracts.
- **Product surfaces dense with small strings:** settings, filters, and toolbars, where dozens of toggles, tooltips, and link labels decide whether the surface reads as crafted or assembled.
- **Audits hunting placeholder-as-label, tooltip-only names, and 'click here' links** — the three cheapest, most common microcopy failures with the highest accessibility cost.

## 7. Combination Notes

### With other ux-writing skills

- **Pairs naturally with forms-labels (guide 08):** forms are microcopy's densest consumer — hint persistence, placeholder rules, and slot budgets are defined here and applied there, so the two guides share one contract rather than duplicating it.
- **Pairs with writing-principles and voice-tone:** sentence case, brevity, and tone are inherited from the foundation guide; microcopy is where those principles are compressed hardest, since budgets leave no room to hide.
- **Pairs with button-labels, empty-states, error-messages, notifications, and onboarding-copy:** these guides consume microcopy slots — button labels follow link/destination rules, error messages live in hint slots, toasts reuse object+result structures.
- **Pairs with accessible-writing and localization-i18n:** the 1.4.13 tooltip contract and 2.4.4 link rules are accessibility obligations written as copy, and string budgets must survive 30% expansion when translated.
- **Pairs with copy-audit (guide 12):** the string inventory makes consistency enforceable — without it, "we always use sentence case" is aspiration, not governance.
- **No avoid list:** microcopy is consumed everywhere, so no skill is incompatible — only component strings that bypass the slot spec, which is the failure mode the inventory exists to catch.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** both styles strip chrome and let text carry meaning, which raises the stakes on every small string — disciplined microcopy is what makes low-chrome surfaces self-explanatory.
- **Good affinity with class-morphism:** its soft, component-forward surfaces still need persistent hints and labeled controls; the string-spec pattern slots into component docs cleanly.
- **Caution, generally:** styles that trade chrome for density (data-heavy tables, dense toolbars) will feel budget pressure; hold the budgets and cut features, not the labels.

### With motion skills (companion repo skill-animation)

- **Good affinity with micro-interactions:** tooltip fade-ins, toggle state changes, and hint reveals should use motion tokens — but the string rules stay constant: motion may reveal copy, never replace it.
- **Good affinity with easing-timing:** tooltips that appear on hover need entrance timing tuned to the 1.4.13 hoverability requirement — dismissal and persistence behavior must survive any animation delay.
- **Caution, generally:** animated placeholders (typing effects, cycling examples) fight the example-only rule by drawing attention to the slot that must not carry instruction; keep placeholders static.

## 8. Anti-Patterns

- **Placeholder-as-label:** instructions that vanish on first keystroke
- **Tooltip-only names:** icon controls whose identity lives in hover
- **Click here:** link labels that name the mechanism, not the destination
- **Broken parallelism:** 'Add user / Removing / Deletion of file' in one menu

### Accessibility Notes

Microcopy is WCAG 3.3.2, 2.4.4, and 1.4.13 territory: visible labels or instructions, descriptive link text, and the dismissible/hoverable/persistent tooltip contract — accessible names must exist independent of hover. In practice that means every icon control carries an `aria-label` (or visible text) that survives the tooltip never appearing, every placeholder is paired with a persistent label or hint, and every tooltip can be dismissed with Escape without moving focus, stays visible while the pointer or focus hovers over it, and persists until dismissed or triggers a condition. The fallback rule is equally explicit: where tooltips cannot meet 1.4.13, convert them to always-visible hint text - persistent text is always the safer default, whether the constraint is a custom renderer, a kiosk surface, or a legacy stack; the hint-persistence token exists precisely to make that the zero-cost option.

## 9. Code Examples

### Example 1 — String-spec panel and parallel-grammar menu

Tokens: `assets/css/component-microcopy.css`

```html
<div class="spec-panel">
  <h3>Settings row — string spec</h3>
  <div class="slot"><span class="slot-name">Label</span>
    <code>Email notifications</code><span class="budget">1–3 words</span></div>
  <div class="slot"><span class="slot-name">Hint</span>
    <code>Received at your work address</code><span class="budget">1 line, persists</span></div>
  <div class="slot"><span class="slot-name">Placeholder</span>
    <code>name@company.com</code><span class="budget">Example only — never the label</span></div>
  <div class="slot"><span class="slot-name">Tooltip</span>
    <code>Applies after 24h. Check spam if missing.</code>
    <span class="budget">~100 chars, 1.4.13 triple</span></div>
  <label class="toggle-row">Email notifications: On
    <input type="checkbox" role="switch" checked aria-label="Email notifications"></label>
</div>

<nav class="menu" aria-label="File actions">
  <button type="button">Add user</button>
  <button type="button">Rename file</button>
  <button type="button">Remove user</button> <!-- parallel: verb+noun throughout -->
</nav>
<style>
  :root { /* production: consume var(--uxw-...) from assets/css/component-microcopy.css */
    --uxw-hint-persistence: always-visible;
    --uxw-tooltip-budget: ~100-chars;
    --uxw-microcase: sentence-case;
  }
  body { font: 14px/1.5 Inter, system-ui, sans-serif; margin: 24px; }
  .spec-panel { max-width: 460px; border: 1px solid #d4d4d4; border-radius: 8px; padding: 16px; }
  .spec-panel h3 { margin: 0 0 12px; font-size: 14px; }
  .slot { display: flex; gap: 8px; align-items: baseline; margin-bottom: 8px; }
  .slot-name { min-width: 88px; font-weight: 600; }
  .slot code { font-size: 13px; }
  .budget { margin-left: auto; color: #404040; font-size: 11px; }
  .toggle-row { display: flex; gap: 8px; margin-top: 12px; }
  .menu { display: flex; flex-direction: column; width: 180px; margin-top: 20px; gap: 2px; }
  .menu button { text-align: left; padding: 8px 12px; border: 0; border-radius: 6px; background: none; cursor: pointer; }
  .menu button:hover { background: #f5f5f5; }
</style>
```

### Example 2 — WCAG 1.4.13-compliant tooltip on a control with its own name

Tokens: `assets/css/component-microcopy.css`

```html
<button class="icon-btn" id="exportBtn" aria-label="Export report">
  <svg width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M8 1v10M4 7l4 4 4-4M2 14h12" stroke="currentColor" stroke-width="1.5" fill="none"/></svg>
</button>
<div class="tooltip" id="exportTip" role="tooltip" hidden>Download as CSV. Files delete after 30 days.</div>
<script>
  const btn = document.getElementById('exportBtn'), tip = document.getElementById('exportTip');
  const show = () => { tip.hidden = false; }, hide = () => { tip.hidden = true; };
  btn.addEventListener('mouseenter', show);
  btn.addEventListener('focus', show);
  btn.addEventListener('mouseleave', () => { if (!tip.matches(':hover')) hide(); });
  btn.addEventListener('blur', hide);
  tip.addEventListener('mouseenter', () => { /* persistent: pointer moved into tooltip */ });
  tip.addEventListener('mouseleave', hide);
  document.addEventListener('keydown', e => { if (e.key === 'Escape') hide(); }); // dismissible
</script>
<style>
  :root { --uxw-tooltip-contract: dismissible-hoverable-persistent; --uxw-tooltip-budget: ~100-chars; }
  body { font: 14px/1.5 Inter, system-ui, sans-serif; padding: 32px; }
  .icon-btn { padding: 10px; border: 1px solid #d4d4d4; border-radius: 8px; background: #fff; cursor: pointer; }
  .icon-btn:focus-visible { outline: 2px solid #1d4ed8; outline-offset: 2px; }
  .tooltip { position: absolute; margin: 8px 0 0 4px; max-width: 240px; background: #171717; color: #fff;
    padding: 8px 12px; border-radius: 6px; font-size: 13px; } /* 62 chars — within ~100-char budget */
</style>
```

## 10. Implementation Checklist

- [ ] Every placeholder is example-only per `--uxw-placeholder-role` — no field's only instruction lives in a placeholder (3.3.2).
- [ ] Hints are persistent, one-line, and sit below the field per `--uxw-hint-persistence` and `--uxw-hint-length`.
- [ ] Tooltips stay within `--uxw-tooltip-budget` (~100 chars) and implement the full `--uxw-tooltip-contract` triple: dismissible, hoverable, persistent (1.4.13).
- [ ] Every icon control has an accessible name independent of its tooltip, and every link label names its destination per `--uxw-link-label-rule` (2.4.4).
- [ ] Toggle labels pick one convention — state or action — per `--uxw-toggle-label-form`, and the choice is consistent system-wide.
- [ ] All menus and option lists pass a parallelism read under `--uxw-list-parallelism` before ship.
- [ ] All microcopy uses sentence case per `--uxw-microcase` and inherits tone from writing-principles.
- [ ] Every shipped string is registered in the string inventory per `--uxw-string-inventory` — copy-audit can trace each string to its component.

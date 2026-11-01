---
name: focus-management
description: Where focus goes when UI changes — visible focus styling, modal traps, focus return, and announcements that keep orientation.
tags: [accessibility, focus, modals, keyboard, wcag]
related: [keyboard-navigation, aria-patterns-widgets, screen-readers]
---

# Accessibility Skill: Focus Management

## 1. Definition

Focus management answers the question keyboard navigation assumes: when the UI changes — a modal opens, a route changes, a dialog closes — where does focus go, where does it return, and can users always see where they are. Bad focus management is the difference between an accessible component and an accessible-looking one: focus that vanishes, lands somewhere random, or gets trapped is disorienting at best and blocking at worst. It spans four concerns that ship together: visible focus styling (WCAG 2.4.7/2.4.13), programmatic focus moves on open/close/route transitions, modal trap-and-return contracts, and announcements (aria-live or labelled targets) so screen reader users hear the landing, not silence. Treat it as a per-surface contract: every overlay and route declares its open target, close target, and narration before implementation begins.

## 2. Core Principles

- **Focus is never allowed to be lost:** after any UI change, focus lands on something meaningful — the new content, its heading, or its first control.
- **Moving focus = announcing context:** programmatic focus moves should carry a label (dialog title, "results updated") so screen readers narrate the landing.
- **Modals trap and return:** focus enters the dialog on open, cycles inside, and returns to the exact trigger element on close.
- **Route changes move focus to the new page's heading:** SPA navigation must emulate what a full page load does for screen readers.
- **Focus visible always:** `:focus-visible` styling reaches 3:1 (WCAG 2.4.13); removing outlines without replacement is a build failure.
- **Never reset scroll without consent:** programmatic focus that jumps the viewport mid-read is hostile; scroll into view only on deliberate moves.
- **One thing at a time:** autofocus fights users — only autofocus inside deliberately-focused surfaces (modals, search overlays).

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Visible focus | `--a11y-focus-visible-style` | `outline 2px + offset 2px` | Default visible focus treatment; token-driven color |
| Focus contrast | `--a11y-focus-contrast-min` | `3:1` | WCAG 2.4.13 against adjacent colors |
| Modal open target | `--a11y-modal-open-target` | `first-control-or-title` | Dialog focus lands on panel or first interactive |
| Modal close target | `--a11y-modal-close-target` | `trigger-element` | Return to the exact button that opened it |
| Route change target | `--a11y-route-change-target` | `h1-or-main` | SPA routes move focus to page heading (tabindex=-1) |
| In-place update target | `--a11y-in-place-update-target` | `live-region` | Background updates announce; focus does not move |
| Autofocus policy | `--a11y-autofocus-policy` | `modals-only` | Never autofocus page loads; always inside dialogs/overlays |
| Scroll on focus | `--a11y-scroll-on-focus` | `deliberate-only` | scrollIntoView only for intentional focus moves |
| Focus order review | `--a11y-focus-order-review` | `per-component` | Open/close/submit flows tested for landing + return |
| Hidden focus policy | `--a11y-hidden-focus-policy` | `inert-offscreen` | Offscreen content uses inert, not just visibility, so focus cannot land there |

Consume them by linking `assets/css/focus-management.css` once at the app root and referencing `var(--a11y-...)` from component styles — the focus ring treatment, contrast floor, and landing-point policies live in tokens so every overlay inherits the same contract. If a surface needs a different landing target, change the token decision through review, not the component's ad-hoc script.

## 4. Composition

- **Composes with keyboard-navigation:** tab order defines the circuit; focus management handles the state changes that reroute it.
- **Composes with aria-patterns-widgets and dialog recipes:** trap-and-return is the shared contract across modals, drawers, and sheets.
- **Composes with skill-animation:** focus transitions animate with motion tokens; reduced-motion collapses them but never removes the focus move.

## 5. Signature Patterns

- **Focus router per surface:** each overlay/route declares open-target, close-target, and announcement; the component library implements it once.
- **Landing announcement:** focus moves are paired with aria-live or labelled targets so screen readers narrate context, not silence.

## 6. Real-World Use Cases

- **SPAs where route changes otherwise strand focus at the document top.**
- **Modal/drawer/sheet components:** the trap-and-return contract.
- **Search overlays, command palettes, and wizards with multi-step focus choreography.**

## 7. Combination Notes

### With other accessibility skills

- **Good with keyboard-navigation:** keyboard defines the tab stops; focus management defines where focus lands when surfaces change — a correct tab order with bad landings is still disorienting.
- **Good with aria-fundamentals and aria-patterns-widgets:** dialogs and composite widgets carry the trap-and-return and labelled-target contracts; this skill supplies the behavior their markup assumes.
- **Good with screen-readers, testing-audit, and forms-errors:** focus landings and announcements are what automation cannot judge — listening scripts verify narrated landing points, and a failed submit moves focus to the error summary while success announces without stealing focus.
- **No caution or avoid list:** this skill has no incompatible partners — the failure mode to prevent is surfaces that bypass the focus router, not skills that conflict with it.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** both favor crisp, high-contrast outlines that make the 2px/2px focus treatment read cleanly without extra ornament; focus states stay honest in disciplined visual systems.
- **Caution with brutalism-ui:** raw aesthetic trends sometimes drop outlines as "ugly defaults" — the focus ring must survive the style, with the styled ring tokenized rather than deleted.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing and page-transitions:** focus moves and route transitions animate with duration tokens, giving sighted users continuity while the focus move itself stays instantaneous for AT.
- **No caution list:** motion never gates focus here — reduced-motion collapses the animation but the focus move and announcement still fire, so there is no conflicting partner.

## 8. Anti-Patterns

- **Vanishing focus** — closing a dialog drops focus to body - keyboard users restart the page
- **Outline: none with nothing** — removing visible focus without any replacement treatment
- **Autofocus everywhere** — page-load autofocus that steals typing and scrolls mid-read
- **Silent focus jumps** — moving focus programmatically with no announcement or visible change

### Accessibility Notes

Focus management serves WCAG 2.4.3, 2.4.7, 2.4.13, and 3.2.1: it is the difference between reachable and usable, and screen reader orientation depends on announced landing points. The fallback rule is explicit: if a landing point cannot be meaningful (transient UI), announce via aria-live instead of moving focus — never move focus to nothing. In practice that means every surface declares its open-target, close-target, and narration up front, hidden or offscreen regions are made `inert` so focus cannot land there, and the per-component review tests each open/close/submit flow for both landing and return.

## 9. Code Examples

### Example 1 — Modal with trap-and-return

Tokens: `assets/css/focus-management.css`

```html
<button id="open-settings" class="btn">Open settings</button>

<div class="overlay" id="overlay" hidden>
  <div class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title" id="modal">
    <h2 id="modal-title">Settings</h2>
    <label>Display name <input type="text" id="first-field"></label>
    <div class="modal-actions">
      <button class="btn" id="cancel">Cancel</button>
      <button class="btn btn-primary" id="save">Save</button>
    </div>
  </div>
</div>

<style>
  .btn { font: 600 14px/1 system-ui, sans-serif; padding: 10px 18px; border-radius: 8px; cursor: pointer; }
  .btn:focus-visible { outline: var(--a11y-focus-visible-style); outline-color: var(--a11y-focus-ring, #1D4ED8); }
  .overlay { position: fixed; inset: 0; background: rgb(0 0 0 / 0.5); display: grid; place-items: center; }
  .modal { background: #fff; border-radius: 12px; padding: 24px; width: min(360px, 90vw); }
  h2 { margin: 0 0 16px; font-size: 18px; }
  label { display: grid; gap: 4px; font-size: 14px; }
  .modal-actions { display: flex; gap: 8px; justify-content: flex-end; margin-top: 20px; }
  .btn-primary { background: #2563EB; color: #fff; border: none; }
</style>
<script>
  const overlay = document.getElementById('overlay');
  const modal = document.getElementById('modal');
  const trigger = document.getElementById('open-settings');
  const firstField = document.getElementById('first-field');
  // --a11y-modal-open-target: focus lands on the first control inside the dialog
  function openModal() {
    overlay.hidden = false;
    document.body.style.overflow = 'hidden'; // --a11y-scroll-on-focus: deliberate move only
    firstField.focus();
  }
  // --a11y-modal-close-target: focus returns to the exact trigger element
  function closeModal() {
    overlay.hidden = true;
    document.body.style.overflow = '';
    trigger.focus();
  }
  // Trap Tab inside the modal (WCAG 2.1.2: Escape always releases the trap)
  modal.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') { closeModal(); return; }
    if (e.key !== 'Tab') return;
    const stops = modal.querySelectorAll('button, input');
    const first = stops[0], last = stops[stops.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  });
  trigger.addEventListener('click', openModal);
  document.getElementById('cancel').addEventListener('click', closeModal);
  document.getElementById('save').addEventListener('click', closeModal);</script>
```

### Example 2 — SPA route change: focus to the new heading

Tokens: `assets/css/focus-management.css`

```html
<main>
  <h1 id="page-title" tabindex="-1">Billing overview</h1>
  <p>Route navigation lands focus here, so screen readers announce the new page.</p>
  <button class="btn" id="nav-invoices">Go to invoices</button>
</main>

<style>
  .btn { font: 600 14px/1 system-ui, sans-serif; padding: 10px 18px; border-radius: 8px; cursor: pointer; }
  .btn:focus-visible { outline: var(--a11y-focus-visible-style); outline-color: var(--a11y-focus-ring, #1D4ED8); }
  /* --a11y-route-change-target: h1-or-main receives focus after navigation */
  #page-title:focus { outline: none; } /* focus ring suppressed only on this programmatic target */
</style>
<script>
  // --a11y-in-place-update-target: live region is registered before it announces
  const announcer = document.createElement('div');
  announcer.setAttribute('aria-live', 'polite');
  announcer.className = 'sr-only';
  document.body.appendChild(announcer);
  function navigate(routeTitle) {
    const heading = document.getElementById('page-title');
    heading.textContent = routeTitle;
    heading.focus(); // lands on --a11y-route-change-target (h1)
    announcer.textContent = `${routeTitle} loaded`;
  }
  document.getElementById('nav-invoices').addEventListener('click', () => navigate('Invoices'));
</script>
```

## 10. Implementation Checklist

- [ ] Every interactive element shows visible focus via `var(--a11y-focus-visible-style)` reaching the `--a11y-focus-contrast-min` floor.
- [ ] Each modal implements trap-and-return: focus to `--a11y-modal-open-target` on open, back to `--a11y-modal-close-target` on close, Escape releases.
- [ ] SPA route changes move focus to `--a11y-route-change-target` (heading with `tabindex="-1"`) and announce the new page.
- [ ] Background updates use `--a11y-in-place-update-target` (live region) — focus never moves for non-interactive changes.
- [ ] Autofocus appears only inside dialogs/overlays, per `--a11y-autofocus-policy`; page loads never steal focus.
- [ ] Offscreen and hidden content follows `--a11y-hidden-focus-policy` (`inert`), so focus cannot land on invisible elements.
- [ ] Every open/close/submit flow is tested for landing + return per `--a11y-focus-order-review` before merge.

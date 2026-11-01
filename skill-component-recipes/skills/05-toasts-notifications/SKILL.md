---
name: toasts-notifications
description: Transient feedback done politely: aria-live narration, timing that respects reading speed, stacking, and the undo pattern.
tags: [toasts, notifications, feedback, aria-live, a11y]
related: [modals-dialogs, buttons-badges, accessibility-wiring]
---

# Component Recipe: Toasts & Notifications

## 1. Definition

Toasts deliver post-action feedback without stealing focus: 'Saved', 'Invitation sent', 'Item archived — Undo'. The recipe covers the politeness contract (aria-live=polite, focus never stolen), timing (4–8s scaled by content length, dismissible, paused on hover), stacking limits, and the undo pattern that replaces confirm dialogs for reversible actions. Bad toasts are noise; good toasts are the feedback layer.

## 2. Core Principles

- **Toasts never steal focus:** they narrate via aria-live=polite — focus stays where the user is (a11y 4.1.3).
- **Timing scales with content:** 4s minimum, +1s per extra line, 8s cap; errors persist until dismissed — users read at their own pace.
- **Dismissible + hover-pause:** every toast has a close control and pauses its timer on hover/focus — auto-dismissal never outruns a screen reader.
- **The undo pattern beats confirmation:** 'Archived — Undo' replaces confirm dialogs for reversible actions (a11y cognitive-content contract).
- **Max 3 stacked:** older toasts collapse into a digest or a notification center — a toast column is not a feed.
- **Placement is consistent and non-blocking:** bottom-right (desktop) / top (mobile) over content, never covering the action just performed.
- **Success is quiet, error is loud:** success toasts are subtle; error toasts persist, pair with an icon, and link to the fix.
- **Notifications have a home:** high-volume products route history to a notification center/drawer — toasts are the ephemeral layer only.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| toast-announcing | `--comp-toast-announcing` | `aria-live-polite` | Never assertive for success; focus never stolen |
| toast-duration-min | `--comp-toast-duration-min` | `4s` | Minimum read time |
| toast-duration-cap | `--comp-toast-duration-cap` | `8s` | Long toasts cap; errors persist |
| toast-dismissibility | `--comp-toast-dismissibility` | `close+hover-pause` | Timer pauses on hover/focus |
| toast-stack-max | `--comp-toast-stack-max` | `3` | Overflow → digest/notification center |
| toast-placement | `--comp-toast-placement` | `bottom-right-desktop-top-mobile` | Consistent; non-blocking |
| toast-undo-window | `--comp-toast-undo-window` | `5-8s` | Undo action window for reversible actions |
| toast-error-persist | `--comp-toast-error-persist` | `until-dismissed` | Errors never auto-dismiss |
| toast-success-quiet | `--comp-toast-success-quiet` | `subtle-single-line` | Success stays understated |
| toast-center-overflow | `--comp-toast-center-overflow` | `notification-center` | History lives in a dedicated surface |

Consume them by linking `assets/css/toasts-notifications.css` once at the app root; the toast service reads `var(--comp-toast-duration-min)`, `--comp-toast-duration-cap`, and `--comp-toast-stack-max` as its operating constants, while the stylesheet resolves placement and styling from `var(--comp-...)` values. Components never hand-build a toast or hardcode a duration — anything outside the table goes back through review.

## 4. Composition

- **Composes with buttons-badges:** undo/close actions inside toasts use the button contract — toast actions are real buttons, not text spans with click handlers.
- **Composes with modals-dialogs:** the when-to-modal table routes reversible actions to toasts-with-undo instead of confirm dialogs.
- **Composes with feedback-confirmation (skill-animation):** toast entrance/exit uses motion tokens; reduced-motion collapses it (a11y).

## 5. Signature Patterns

- **Toast service:** one app-level toast manager owning queue, stack cap, placement, and the polite live region — components call `toast()`, never build their own.
- **Undo-first flow:** reversible actions skip confirmation entirely and announce 'done — Undo' — the confirmation budget is reserved for the irreversible.

## 6. Real-World Use Cases

- **Post-save/post-send feedback** in any app — the quiet workhorse 'Saved' that confirms without interrupting.
- **Destructive-but-reversible actions** (archive, remove from list) where undo replaces a confirm dialog.
- **Audit** for toast floods, unreadable auto-dismiss, and toasts covering the button just clicked.

## 7. Combination Notes

### With other component-recipe skills

- **Good with modals-dialogs:** the two share the interruption budget — dialogs take the irreversible, toasts take the reversible with undo; together they keep confirm-dialog count near zero.
- **Good with buttons-badges, forms-inputs, tables-data-grid, empty-loading-error, and accessibility-wiring:** toast actions use the button contract, save/send and bulk-action feedback from forms and tables all land through the toast service, and wiring skills verify the aria-live contract.
- **Good with dropdowns-menus, cards-lists, navigation-patterns, tabs-accordions, and command-palette:** any recipe that performs actions can call `toast()` — the service is app-level infrastructure, so no pairing needs special handling.
- **No caution or avoid list:** the service is additive and app-wide; failures come from components bypassing it, not from pairing.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and glassmorphism:** toasts should be quiet — a single line, subtle elevation, one accent — and a translucent surface over content reads naturally as long as text on glass passes contrast.
- **Caution with collage-art:** collage styling pushes decorative layering and mixed typography that can make a 4-second transient message hard to scan; keep toast typography plain even in expressive styles.

### With motion skills (companion repo skill-animation)

- **Good affinity with feedback-confirmation and entrance-exit:** toasts are confirmation feedback — a small entrance (slide-up + fade) and a respectful exit, tuned with motion tokens, give actions a felt completion while the service animates the stack shift when a toast above expires.
- **No caution list:** reduced-motion collapses entrance/exit to opacity, and animation never extends the undo window or delays dismissal logic.

## 8. Anti-Patterns

- **Toast flood** — every action toasting until the stack is a feed nobody reads
- **Speed-read dismissal** — 2s toasts vanishing before the text registers
- **Assertive success** — aria-live=assertive interrupting the user for 'Saved'
- **Blocking placement** — toasts covering the button the user just clicked

### Accessibility Notes

Toasts implement WCAG 4.1.3 (status messages): polite narration without focus theft, durations a screen reader user can meet (hover-pause), and dismissal controls — the toast service is a11y infrastructure, not decoration. The live region is a single app-level `aria-live=polite` container the service writes into, so screen readers narrate new toasts without asserting over the user's current task; focus never moves to a toast, and the close control is the only focusable element inside one. Timing respects reading speed — 4s minimum scaled by content, paused on hover/focus — and errors persist until dismissed precisely because an error the user never read is an error that never happened. The fallback rule: If a toast cannot be announced (legacy stack), pair critical feedback with an inline status region on the page — narration must exist somewhere, even if not transient.

## 9. Code Examples

### Example 1 — Toast service: queue, 3-stack cap, polite live region, hover-pause, undo

```html
<button id="archive-btn" class="btn">Archive item</button>
<div id="toast-region" class="toasts" role="region" aria-label="Notifications"></div>
<style>
  .btn { background: #2563EB; color: #fff; border: none; border-radius: 8px; padding: 10px 18px; font: 600 13px Inter, sans-serif; cursor: pointer; }
  .toasts { position: fixed; bottom: 24px; right: 24px; display: flex; flex-direction: column; gap: 8px; z-index: 1000; }
  @media (max-width: 639px) { .toasts { bottom: auto; top: 16px; right: 16px; left: 16px; } }
  .toast { display: flex; align-items: center; gap: 12px; background: #171717; color: #F5F5F5; border-radius: 10px; padding: 12px 16px; font: 14px/1.4 Inter, sans-serif; }
  .toast-success { border-left: 3px solid #22C55E; } .toast-error { border-left: 3px solid #EF4444; }
  .toast-action { background: none; border: none; color: #93C5FD; font: 600 13px Inter, sans-serif; cursor: pointer; padding: 4px; } .toast-close { background: none; border: none; color: #A3A3A3; cursor: pointer; font-size: 16px; padding: 4px; }
  .toast[data-leaving] { opacity: 0; transition: opacity 150ms ease; }
</style>
<script>
  const MIN = 4000, CAP = 8000, STACK_MAX = 3, region = document.getElementById('toast-region');
  function toast(message, { type = 'success', action = null } = {}) {
    while (region.children.length >= STACK_MAX) dismiss(region.firstElementChild); // stack cap: oldest leaves first
    const el = document.createElement('div');
    el.className = `toast toast-${type}`; el.textContent = message;
    const close = document.createElement('button');
    close.className = 'toast-close'; close.setAttribute('aria-label', 'Dismiss'); close.textContent = '×';
    close.addEventListener('click', () => dismiss(el)); el.append(close);
    if (action) { // undo action uses the button contract (buttons-badges)
      const undo = document.createElement('button');
      undo.className = 'toast-action'; undo.textContent = action.label;
      undo.addEventListener('click', () => { action.onAction(); dismiss(el); }); el.append(undo);
    }
    region.setAttribute('aria-live', 'polite'); // polite narration; focus never moves to the toast
    region.appendChild(el);
    if (type !== 'error') { // errors persist until dismissed; the rest scale with content
      const ttl = Math.min(MIN + Math.max(0, Math.ceil(message.length / 60) - 1) * 1000, CAP);
      const t = setTimeout(() => dismiss(el), ttl); el._t = t;
      // Hover/focus pauses the timer — auto-dismiss never outruns a reader.
      const pause = () => clearTimeout(el._t);
      el.addEventListener('mouseenter', pause); el.addEventListener('focusin', pause);
      el.addEventListener('mouseleave', () => el._t = setTimeout(() => dismiss(el), ttl / 2));
    }
    return el;
  }
  function dismiss(el) { // fade out, then remove
    if (!el || !el.isConnected) return; clearTimeout(el._t); el.setAttribute('data-leaving', '');
    setTimeout(() => el.remove(), 150);
  }
  // Undo-first flow: reversible actions skip confirmation entirely.
  document.getElementById('archive-btn').addEventListener('click', () => {
    const item = { name: 'Q3 report' };
    toast(`"${item.name}" archived`, { action: { label: 'Undo', onAction: () => console.log('restore', item) } });
  });
</script>
```

### Example 2 — Success is quiet, error is loud (persist + fix link)

```html
<button class="btn" id="save-btn">Save draft</button>
<button class="btn btn-ghost" id="sync-btn">Sync now</button>
<div id="region2" class="toasts" role="region" aria-label="Notifications"></div>
<style>
  .btn { background: #2563EB; color: #fff; border: none; border-radius: 8px; padding: 10px 18px; font: 600 13px Inter, sans-serif; cursor: pointer; margin: 4px; }
  .btn-ghost { background: #fff; color: #171717; border: 1px solid #D4D4D4; }
  .toasts { position: fixed; bottom: 24px; right: 24px; display: flex; flex-direction: column; gap: 8px; }
  .toast { max-width: 360px; border-radius: 10px; padding: 12px 16px; font: 14px/1.4 Inter, sans-serif; display: flex; align-items: center; gap: 10px; }
  /* Success: subtle-single-line, quiet accent */
  .toast-success { background: #F5F5F5; color: #404040; border: 1px solid #E5E5E5; border-left: 3px solid #22C55E; }
  /* Error: persists, pairs with an icon, links to the fix */
  .toast-error { background: #FEF2F2; color: #7F1D1D; border: 1px solid #FECACA; border-left: 3px solid #EF4444; }
  .toast-icon { font-size: 15px; } .toast a { color: #B91C1C; font-weight: 600; }
  .toast-close { margin-left: auto; background: none; border: none; cursor: pointer; color: inherit; opacity: 0.6; }
</style>
<script>
  const region = document.getElementById('region2');
  region.setAttribute('aria-live', 'polite'); // set once at service init, never per-toast
  function addToast(cls, html) {
    const el = document.createElement('div');
    el.className = `toast ${cls}`; el.innerHTML = html;
    const close = document.createElement('button');
    close.className = 'toast-close'; close.setAttribute('aria-label', 'Dismiss'); close.textContent = '×';
    close.addEventListener('click', () => el.remove());
    el.appendChild(close);
    region.appendChild(el); // polite narration happens on insertion
  }
  document.getElementById('save-btn').addEventListener('click', () =>
    addToast('toast-success', '<span class="toast-icon">✓</span> Draft saved'));
  document.getElementById('sync-btn').addEventListener('click', () =>
    addToast('toast-error', '<span class="toast-icon">⚠</span> Sync failed — <a href="#fix">Retry sync</a>'));
  // No timer is set for .toast-error: it persists until dismissed by design.
</script>
```

## 10. Implementation Checklist

- [ ] One app-level toast service exists; components call `toast()` and never build their own stack or live region (`--comp-toast-announcing`).
- [ ] The live region is `aria-live=polite` and set once — assertive is reserved for genuinely urgent system events, never success feedback.
- [ ] Durations follow 4s minimum, +1s per extra line, 8s cap; nothing auto-dismisses faster (`--comp-toast-duration-min/cap`).
- [ ] Every toast has a close control and pauses its timer on hover/focus (`--comp-toast-dismissibility`).
- [ ] The stack holds at most 3 toasts; overflow collapses into a digest or notification center (`--comp-toast-stack-max`, `--comp-toast-center-overflow`).
- [ ] Placement is bottom-right on desktop and top on mobile, never covering the control just used (`--comp-toast-placement`).
- [ ] Reversible actions ship with an Undo action inside the 5–8s window instead of a confirm dialog (`--comp-toast-undo-window`).
- [ ] Errors persist until dismissed, pair with an icon, and link to the fix; success toasts stay subtle and single-line (`--comp-toast-error-persist`, `--comp-toast-success-quiet`).

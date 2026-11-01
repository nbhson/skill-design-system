---
name: modals-dialogs
description: The dialog contract done once: role/label, focus trap-and-return, Escape, scrim, and the when-NOT-to-modal decision table.
tags: [modals, dialogs, focus-management, a11y, overlays]
related: [forms-inputs, toasts-notifications, buttons-badges]
---

# Component Recipe: Modals & Dialogs

## 1. Definition

Modal dialogs interrupt flow for a focused task: confirmations, short forms, critical notices. The recipe is the full dialog contract — role=dialog, accessible name, focus trap-and-return, Escape/scrim close, scroll lock, and stacked-dialog handling — implemented once in a Dialog primitive. Equally important is the decision table of when NOT to modal: most confirmations belong inline or as toasts; modality is for tasks that must complete before proceeding.

## 2. Core Principles

- **Modal earns its interruption:** use for confirmation of destructive/irreversible actions, focused subtasks, and blocking notices — everything else is inline or a toast.
- **The contract is uniform:** role=dialog + aria-modal + labelled-by title, focus enters on open, traps inside, returns to trigger on close (a11y repo guide 04).
- **Escape and scrim both close (except blocking):** destructive-task dialogs keep Escape dismissible with confirmation — blocking alerts document the exception.
- **Scroll lock without layout shift:** body scroll locks with scrollbar-width compensation — the page must not jump when the dialog opens.
- **Dialogs are short:** one task, one primary action, one escape hatch — multi-step flows are routes or wizards, not nested modals.
- **Stacking is capped and ordered:** dialog-on-dialog is capped at 2 with managed focus order; 3+ signals the flow needs redesign.
- **Size variants by task:** sm (confirmations), md (short forms), lg (content-heavy) — with mobile behavior declared (full-screen sheet under 640px).
- **Native <dialog> where possible:** the platform element carries focus management and `:modal` styling — the primitive builds on it.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| dialog-role | `--comp-dialog-role` | `dialog+aria-modal+labelledby` | The AT contract triple |
| dialog-focus-policy | `--comp-dialog-focus-policy` | `trap-and-return` | Enter on open, return to trigger |
| dialog-escape | `--comp-dialog-escape` | `escape+scrim-close` | Blocking dialogs document exceptions |
| dialog-scrim | `--comp-dialog-scrim` | `rgba(0,0,0,0.60)` | Consistent scrim across surfaces |
| dialog-scroll-lock | `--comp-dialog-scroll-lock` | `locked+compensated` | No layout shift on open |
| dialog-size-sm | `--comp-dialog-size-sm` | `400px` | Confirmations |
| dialog-size-md | `--comp-dialog-size-md` | `560px` | Short forms |
| dialog-size-lg | `--comp-dialog-size-lg` | `800px` | Content-heavy tasks |
| dialog-mobile | `--comp-dialog-mobile` | `full-sheet-under-640px` | Declared mobile behavior |
| dialog-stack-cap | `--comp-dialog-stack-cap` | `2` | Max nested dialogs; 3+ = redesign |

Consume them by linking `assets/css/modals-dialogs.css` once at the app root, then reading the contract through `var(--comp-...)` in the Dialog primitive's CSS and JS (the stack cap and focus policy are read as constants, not re-declared per component). No dialog stylesheet hardcodes a width, a scrim color, or an escape rule; anything the table does not define goes back through review.

## 4. Composition

- **Composes with forms-inputs:** dialog forms use the field recipe; dialog buttons use the button contract — a modal never invents its own field or button styling.
- **Composes with focus-management (skill-accessibility guide 04):** that guide owns the focus criteria; this recipe implements the dialog around them.
- **Composes with toasts-notifications:** post-dialog feedback lands as a toast — dialogs close, confirmation narrates politely.

## 5. Signature Patterns

- **Dialog primitive:** one component (native `<dialog>`-based) exposing size variants, the focus contract, and scrim/escape handling — every modal composes it, none re-implements the contract.
- **When-to-modal decision table:** confirmation/subtask/blocking vs inline/toast/route — reviewed at design time, not built time, so modal count stays intentional.

## 6. Real-World Use Cases

- **Destructive confirmations** (delete, revoke, transfer) where the cost of a misclick is irreversible.
- **Focused subtasks** (invite member, edit record) that must finish or abort before the user returns to the page.
- **Audit** for modal fatigue, trap-less dialogs, scroll-jump on open, and 3-deep stacking.

## 7. Combination Notes

### With other component-recipe skills

- **Good with forms-inputs, buttons-badges, dropdowns-menus, and tabs-accordions:** dialogs are containers — their fields, buttons, menus, and tabs must come from those recipes so a modal looks like the rest of the product.
- **Good with toasts-notifications, empty-loading-error, tables-data-grid, cards-lists, command-palette, and navigation-patterns:** post-close feedback narrates as a toast, async results land in page-level loading/error states, and lg dialogs embed grid/list recipes — command palettes and nav drawers reuse the same overlay contract.
- **Good with accessibility-wiring:** this recipe is the a11y dialog pattern made concrete — wiring skills verify role/name/trap/return rather than rebuild them.
- **No caution or avoid list:** the contract is strictly additive; any skill can sit inside a compliant dialog. Failures come from bypassing the primitive, not from pairing.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** a modal is an interruption — reduced chrome, one accent, and flat surfaces keep the interruption short and the task legible.
- **Good affinity with glassmorphism:** translucent scrims and surfaces read naturally here, provided text on glass still passes contrast and the scrim token stays the single source of dimming.
- **Caution with brutalism-ui:** raw borders and harsh shadow language can make the scrim boundary unclear; keep the `--comp-dialog-scrim` dim strong enough that the modal edge is unmistakable.

### With motion skills (companion repo skill-animation)

- **Good affinity with entrance-exit and easing-timing:** dialogs are the canonical enter/exit pair — scale/fade in on open, reverse on close, using shared duration/easing tokens (fast in, slightly faster out) so no dialog feels heavier than another.
- **No caution list:** motion never changes the contract — animation is decorative on top of trap/return/Escape, must respect reduced-motion, and can never delay focus entering the dialog.

## 8. Anti-Patterns

- **Modal fatigue** — everything in a modal until users reflex-click through the one that mattered
- **Trap-less dialogs** — focus escapes to the dead page behind the scrim
- **Focus-to-nowhere** — dialogs that close and drop focus to body
- **Scroll-jump opens** — scrollbar loss shifting the whole page sideways

### Accessibility Notes

Dialogs implement the WAI-ARIA dialog pattern: role/name/trap/escape/return are the five non-negotiables (a11y repo guides 03/04) — a dialog missing any one is a build failure in review. The accessible name comes from the visible title via `aria-labelledby`, `aria-modal="true"` is declared only when the dialog is truly modal, and focus returns to the exact trigger element on close so keyboard and screen reader users resume where they left off. Escape and scrim dismissal are the default; blocking dialogs are the documented exception, and destructive-task dialogs stay Escape-dismissible but confirm before applying the irreversible action. The fallback rule: If the trap implementation cannot be completed, use the native <dialog> element with showModal() — it carries the focus contract natively. That native contract is why the primitive builds on the platform element wherever possible.

## 9. Code Examples

### Example 1 — Native `<dialog>` confirmation with full contract

Tokens: `assets/css/modals-dialogs.css`

```html
<button id="delete-trigger" class="btn-danger">Delete project</button>
<dialog id="confirm-dlg" class="dialog dialog-sm" aria-labelledby="dlg-title">
  <h2 id="dlg-title" class="dialog-title">Delete project?</h2>
  <p class="dialog-body">This permanently removes "Aurora" and all its boards.</p>
  <div class="dialog-actions"><button class="btn-ghost" data-close>Cancel</button><button class="btn-danger" id="confirm-delete">Delete</button></div>
</dialog>
<style>
  .dialog { border: none; border-radius: 12px; padding: 24px; box-shadow: 0 24px 64px rgba(0,0,0,0.25);
            font: 14px/1.5 Inter, system-ui, sans-serif; }
  .dialog::backdrop { background: var(--comp-dialog-scrim); } /* rgba(0,0,0,0.60) */
  .dialog-sm { width: min(var(--comp-dialog-size-sm), calc(100vw - 32px)); } /* md 560px / lg 800px same pattern */
  @media (max-width: 639px) { .dialog { width: 100vw; height: 100dvh; border-radius: 0; } } /* --comp-dialog-mobile */
  .dialog-title { margin: 0 0 8px; font-size: 18px; font-weight: 650; } .dialog-body { margin: 0 0 20px; color: #404040; }
  .dialog-actions { display: flex; gap: 8px; justify-content: flex-end; }
  .btn-danger, .btn-ghost { border-radius: 8px; padding: 9px 16px; font: 600 13px/1 Inter, sans-serif; cursor: pointer; }
  .btn-danger { background: #DC2626; color: #fff; border: none; }
  .btn-ghost  { background: transparent; color: #171717; border: 1px solid #D4D4D4; }
</style>
<script>
  const dlg = document.getElementById('confirm-dlg');
  const trigger = document.getElementById('delete-trigger');
  // Scroll lock with scrollbar compensation — no layout shift on open.
  const lock = (on) => {
    document.body.style.overflow = on ? 'hidden' : '';
    document.body.style.paddingRight = on ? (window.innerWidth - document.documentElement.clientWidth) + 'px' : '';
  };
  trigger.addEventListener('click', () => { lock(true); dlg.showModal(); }); // showModal() traps focus (a11y fallback rule)
  dlg.addEventListener('close', () => { lock(false); trigger.focus(); });    // return-to-trigger
  // Scrim click closes; native Escape stays enabled. Blocking dialogs would
  // preventDefault() on 'cancel' and document the exception.
  dlg.addEventListener('click', (e) => { if (e.target === dlg) dlg.close(); });
  dlg.querySelectorAll('[data-close]').forEach((b) => b.addEventListener('click', () => dlg.close()));
  document.getElementById('confirm-delete').addEventListener('click', () => dlg.close()); // feedback → toast
</script>
```

### Example 2 — Size variants + the when-to-modal decision table

Tokens: `assets/css/modals-dialogs.css`

```html
<div class="demo">
  <button class="chip" data-open="dlg-sm">Open sm — confirmation</button><button class="chip" data-open="dlg-md">Open md — short form</button><button class="chip" data-open="dlg-lg">Open lg — content-heavy</button>
</div>
<dialog id="dlg-sm" class="dialog dialog-sm" aria-labelledby="s1"><h2 id="s1">Revoke key?</h2><p>The integration stops working immediately.</p><div class="dialog-actions"><button class="btn-ghost" data-close>Cancel</button><button class="btn-danger" data-close>Revoke</button></div></dialog>
<dialog id="dlg-md" class="dialog dialog-md" aria-labelledby="s2"><h2 id="s2">Invite member</h2><label>Email <input type="email" placeholder="teammate@acme.co"></label><div class="dialog-actions"><button class="btn-ghost" data-close>Abort</button><button class="btn-primary" data-close>Send invite</button></div></dialog>
<dialog id="dlg-lg" class="dialog dialog-lg" aria-labelledby="s3"><h2 id="s3">Usage report — November</h2><div class="report">…tables/lists from their own recipes…</div><div class="dialog-actions"><button class="btn-primary" data-close>Done</button></div></dialog>
<style>
  .dialog { border: none; border-radius: 12px; padding: 24px; font: 14px/1.5 Inter, sans-serif; }
  .dialog::backdrop { background: var(--comp-dialog-scrim); }
  .dialog-sm { width: min(var(--comp-dialog-size-sm), calc(100vw - 32px)); }
  .dialog-md { width: min(var(--comp-dialog-size-md), calc(100vw - 32px)); }
  .dialog-lg { width: min(var(--comp-dialog-size-lg), calc(100vw - 32px)); }
  .chip { border: 1px solid #D4D4D4; background: #fff; border-radius: 999px; padding: 8px 14px;
          font: 500 13px Inter, sans-serif; cursor: pointer; margin: 4px; }
  .dialog-actions { display: flex; gap: 8px; justify-content: flex-end; margin-top: 16px; }
  .btn-primary, .btn-danger, .btn-ghost { border-radius: 8px; padding: 9px 16px; cursor: pointer; border: none; font: 600 13px Inter, sans-serif; }
  .btn-primary { background: #2563EB; color: #fff; } .btn-danger { background: #DC2626; color: #fff; }
  .btn-ghost { background: transparent; border: 1px solid #D4D4D4; }
  label { display: block; margin-top: 12px; font-weight: 600; }
  input { width: 100%; margin-top: 6px; padding: 9px 12px; border: 1px solid #D4D4D4; border-radius: 8px; }
  .report { min-height: 160px; background: #F5F5F5; border-radius: 8px; margin-top: 12px; }
</style>
<script>
  document.querySelectorAll('[data-open]').forEach((btn) =>
    btn.addEventListener('click', () => document.getElementById(btn.dataset.open).showModal()));
  document.querySelectorAll('dialog').forEach((d) => {
    d.addEventListener('click', (e) => { if (e.target === d) d.close(); });
    d.querySelectorAll('[data-close]').forEach((b) => b.addEventListener('click', () => d.close()));
  });
</script>
```

When-to-modal decision table:

| Situation | Route to | Why |
|---|---|---|
| Irreversible action (delete, revoke) | **Modal (sm)** | Must be confirmed before proceeding |
| Focused subtask (invite, edit record) | **Modal (md)** | Must finish or abort before returning |
| Blocking notice (downtime, legal) | **Modal, documented exception** | Escape/scrim disabled on purpose |
| Reversible action (archive, remove from list) | **Toast + Undo** | Confirmation wastes a click; undo beats a dialog |
| Inline validation, small status | **Inline** | No interruption warranted |
| Multi-step flow | **Route or wizard** | Dialogs are short; never nest modals |

## 10. Implementation Checklist

- [ ] Every modal renders through the Dialog primitive with `role=dialog`, `aria-modal`, and an `aria-labelledby` title (`--comp-dialog-role`).
- [ ] Focus enters the dialog on open, traps inside, and returns to the trigger on close (`--comp-dialog-focus-policy`).
- [ ] Escape and scrim both close the dialog; blocking dialogs document their exception (`--comp-dialog-escape`).
- [ ] The scrim uses `var(--comp-dialog-scrim)` — no per-component rgba values.
- [ ] Body scroll locks with scrollbar compensation; opening a dialog causes zero layout shift (`--comp-dialog-scroll-lock`).
- [ ] Size variants map to task type: sm 400px confirmations, md 560px forms, lg 800px content (`--comp-dialog-size-*`).
- [ ] Mobile behavior is declared: full-screen sheet under 640px (`--comp-dialog-mobile`).
- [ ] Stacked dialogs never exceed 2 with managed focus order; a 3-deep flow goes back to design (`--comp-dialog-stack-cap`).

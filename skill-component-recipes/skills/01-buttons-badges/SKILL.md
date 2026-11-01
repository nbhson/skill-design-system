---
name: buttons-badges
description: The action vocabulary: button variants and sizes, loading/disabled contracts, icon buttons with names, and badge/status chips.
tags: [buttons, badges, components, states, action-vocabulary]
related: [forms-inputs, tables-data-grid, modals-dialogs]
---

# Component Recipe: Buttons & Badges

## 1. Definition

Buttons and badges are the action vocabulary of an interface: buttons commit actions (primary, secondary, tertiary, destructive), badges label state (status chips, counts, categories). The craft is a closed variant system — every button variant has a documented hierarchy role, size ramp, and state set (hover/active/focus/disabled/loading) — so products compose actions instead of redesigning them. A button system done well is invisible: users learn the hierarchy once and trust it everywhere; a badge system done well reads at a glance because color, icon, and text always arrive together. Both components are usually the first ones built in a design system, so their contract sets the quality bar for everything after.

## 2. Core Principles

- **One primary per view:** the primary variant marks the single most-likely action; competing primaries dissolve hierarchy.
- **Variants are hierarchy, not decoration:** primary (filled), secondary (outline), tertiary (ghost), destructive (danger-filled) — each has a documented use contract.
- **Sizes come from the ramp:** sm 32px, md 40px, lg 48px heights; touch surfaces meet 44px minimum (a11y 2.5.8).
- **Loading replaces label with spinner + 'Processing':** the button stays sized (no reflow), disabled, and announces via aria-live.
- **Disabled is styled AND explained:** tooltip or helper text says why — a bare disabled button is a dead end.
- **Icon-only buttons have accessible names:** aria-label minimum; visible tooltip recommended — icon alone is never the name.
- **Badges carry status triples:** color + icon + text (a11y 1.4.1); count badges cap at 99+; dot badges pair with screen reader text.
- **Destructive actions confirm or undo:** destructive buttons either open a confirmation or ship an undo path — never a single-click delete.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Variants | `--comp-btn-variants` | `primary,secondary,tertiary,destructive` | Closed variant set; no ad-hoc buttons |
| Height sm | `--comp-btn-height-sm` | `32px` | Compact tier (dense tables, toolbars) |
| Height md | `--comp-btn-height-md` | `40px` | Default tier |
| Height lg | `--comp-btn-height-lg` | `48px` | Emphasis tier (heroes, forms) |
| Touch min | `--comp-btn-touch-min` | `44px` | WCAG 2.5.8 effective touch target |
| Focus ring | `--comp-btn-focus-ring` | `2px + offset 2px` | Focus treatment (a11y repo contracts) |
| Loading policy | `--comp-btn-loading-policy` | `spinner+disabled+announce` | No size change; aria-live busy |
| Disabled policy | `--comp-btn-disabled-policy` | `styled+explained` | Reason visible in tooltip/helper |
| Badge signal triple | `--comp-badge-signal-triple` | `color+icon+text` | Never color alone (a11y 1.4.1) |
| Badge count cap | `--comp-badge-count-cap` | `99+` | Count badges cap; overflow reads as 99+ |

Consume them by linking `assets/css/buttons-badges.css` once at the app root, then reading `var(--comp-btn-...)` / `var(--comp-badge-...)` from component CSS — never re-declaring heights, rings, or policies inline. The policy tokens (`loading-policy`, `disabled-policy`, `signal-triple`) are behavioral contracts encoded as custom properties so linters and reviews can assert them, not just styles.

## 4. Composition

- **Composes with skill-design-tokens:** button colors, radii, and spacing consume semantic/alias tokens — buttons never hardcode values.
- **Composes with semantic-color-system (skill-color-theory guide 06):** destructive and status badges consume status ramps.
- **Composes with forms-inputs (guide 02):** submit buttons and input heights share the size ramp — a form is one rhythm.

## 5. Signature Patterns

- **Button component contract:** one component exposing variants × sizes × states, with the loading/disabled/announcement behavior implemented once. Teams never hand-roll a spinner inside a `<button>`; they flip the component's `loading` prop and the size pinning, disabling, and live-region narration all happen together.
- **Badge role matrix:** badges map to status/label/count categories, each with its signal triple and overflow behavior documented. A reviewer can trace any badge in the product to a row in the matrix — an unlisted badge is a bug, not a style choice.

## 6. Real-World Use Cases

- **Any product UI:** forms, toolbars, cards, dialogs all consume the button system.
- **Design systems:** buttons are usually the first component built — the contract sets the pattern for the rest.
- **Audit:** competing primaries, icon buttons without names, unexplained disabled states.

## 7. Combination Notes

### With other component-recipe skills

- **Good with forms-inputs:** submit buttons and inputs share the size ramp, so a form reads as one rhythm; the loading contract is also shared (submitting forms pin buttons).
- **Good with tables-data-grid:** row actions and toolbar buttons consume sm-tier heights and the kebab/menu pattern; count badges express selection and row totals.
- **Good with modals-dialogs and toasts-notifications:** dialog primary/secondary buttons follow the one-primary rule; toast undo actions use the button contract.
- **Good with navigation-patterns, cards-lists, tabs-accordions, dropdowns-menus, command-palette:** these surfaces all embed buttons or badges as their action layer — the closed variant set is what keeps them consistent.
- **Good with empty-loading-error and accessibility-wiring:** empty states end in a primary action; accessibility wiring verifies the naming and live-region halves of the contract.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and neumorphism:** a closed variant set with a strict height ramp suits disciplined, low-noise styling; neumorphism's soft-surface buttons still map cleanly onto the four documented variants.
- **Caution with collage-art:** collage aesthetics push torn, rotated, mixed-material buttons that fight the closed variant set — if a style demands deviation, add a documented variant through review rather than ad-hoc one-offs.

### With motion skills (companion repo skill-animation)

- **Good affinity with micro-interactions:** hover/press transitions and the spinner are classic micro-interaction territory, animated with duration tokens so state changes stay under ~150ms.
- **Good affinity with feedback-confirmation:** loading-to-success swaps and destructive confirmation flows rely on animated state feedback — but the button must never resize mid-animation (the no-reflow rule holds).

## 8. Anti-Patterns

- **Two primaries:** filled CTA next to filled CTA - the eye picks neither
- **Icon-only mystery buttons:** unlabeled glyph buttons screen readers read as 'button'
- **Reflow loading:** button shrinking to a spinner and shifting the layout
- **Dead-end disabled:** greyed actions with no explanation of what unlocks them

### Accessibility Notes

Buttons are WCAG 2.1.1/2.4.7/2.5.8 territory: real `<button>` elements, visible focus, 44px touch floors, and loading announced via aria-live — icon-only controls carry accessible names (a11y repo guides 03/05). The state contract is the accessibility contract in disguise: a button that pins its height while loading protects users from layout shift, and a `aria-live` region narrating "Processing…" tells non-visual users the click registered. Badges inherit 1.4.1 (use of color): the color+icon+text triple means a deuteranope can still tell "failed" from "passed," and count caps (99+) keep announced numbers meaningful. If a custom button variant cannot meet the state contract (loading/announce), ship the native button with the closest variant — native semantics beat custom styling without states.

## 9. Code Examples

### Example 1 — Button variants, sizes, loading, disabled, icon button

Tokens: `assets/css/buttons-badges.css`

```html
<div class="demo">
  <button class="btn primary md">Save changes</button>
  <button class="btn secondary md">Preview</button>
  <button class="btn tertiary md">Cancel</button>
  <button class="btn destructive md" data-confirm>Delete workspace</button>

  <button class="btn primary md" id="saveBtn" aria-busy="false">
    <span class="spinner" hidden aria-hidden="true"></span>
    <span class="label">Publish post</span>
  </button>
  <p aria-live="polite" class="sr-only" id="saveLive"></p>

  <button class="btn secondary md" disabled aria-describedby="lockHint">Invite members</button>
  <span id="lockHint" class="hint">Disabled: verify your email to unlock invites.</span>

  <button class="btn primary md icon-only" aria-label="Open settings">
    <svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M8 5a3 3 0 100 6 3 3 0 000-6zm7 3l-1.8 1 .3 2-2 1-1.5-1.4-2 .8L7.6 14H5.4l-.4-2.6-2-.8L1.5 12l-2-1 .3-2L-2 8l1.8-1-.3-2 2-1L3 5.4l2-.8L5.4 2h2.2l.4 2.6 2 .8L11.5 4l2 1-.3 2z"/></svg>
  </button>
</div>
<script>
  const btn = document.getElementById('saveBtn');
  const live = document.getElementById('saveLive');
  btn.addEventListener('click', () => {
    btn.setAttribute('aria-busy', 'true');
    btn.disabled = true; // pinned height: no reflow
    btn.querySelector('.spinner').hidden = false;
    btn.querySelector('.label').textContent = 'Processing…';
    live.textContent = 'Publishing post, please wait.';
    setTimeout(() => {
      btn.setAttribute('aria-busy', 'false');
      btn.disabled = false;
      btn.querySelector('.spinner').hidden = true;
      btn.querySelector('.label').textContent = 'Publish post';
      live.textContent = 'Post published.';
    }, 2000);
  });
</script>
<style>
  .demo { display: flex; flex-wrap: wrap; gap: 12px; align-items: center; font: 14px/1.4 Inter, system-ui, sans-serif; }
  .btn { border: 1px solid transparent; border-radius: 8px; cursor: pointer; font-weight: 600;
       display: inline-flex; align-items: center; justify-content: center; gap: 8px; }
  .btn.sm { height: var(--comp-btn-height-sm); padding: 0 12px; }
  .btn.md { height: var(--comp-btn-height-md); padding: 0 16px; } .btn.lg { height: var(--comp-btn-height-lg); padding: 0 20px; }
  .btn.primary   { background: #2563EB; color: #fff; }
  .btn.primary:hover { background: #1D4ED8; } /* hover step keeps 4.5:1+ */
  .btn.secondary { background: #fff; color: #171717; border-color: #D4D4D4; }
  .btn.tertiary  { background: transparent; color: #2563EB; }
  .btn.destructive { background: #DC2626; color: #fff; }
  .btn:focus-visible { outline: var(--comp-btn-focus-ring); outline-offset: 2px; }
  .btn:disabled { opacity: 0.5; cursor: not-allowed; }
  .spinner { width: 14px; height: 14px; border: 2px solid #fff; border-top-color: transparent;
             border-radius: 50%; animation: spin 0.8s linear infinite; }
  @keyframes spin { to { transform: rotate(360deg); } }
  @media (prefers-reduced-motion: reduce) { .spinner { animation-duration: 1.6s; } }
  .hint { color: #737373; font-size: 12px; } .sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }

</style>
```

### Example 2 — Badge set with signal triples and count cap

Tokens: `assets/css/buttons-badges.css`

```html
<ul class="badge-demo" role="list">
  <li><span class="badge status success"><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M2 6l3 3 5-6" fill="none" stroke="currentColor" stroke-width="2"/></svg> Active</span></li>
  <li><span class="badge status warning"><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M6 1v6M6 9.5v1.5" stroke="currentColor" stroke-width="2"/></svg> Pending review</span></li>
  <li><span class="badge status danger"><svg viewBox="0 0 12 12" aria-hidden="true"><path d="M3 3l6 6M9 3l-6 6" stroke="currentColor" stroke-width="2"/></svg> Failed</span></li>
  <li><span class="badge count" aria-label="128 unread notifications">99+</span></li>
  <li><span class="badge dot" aria-label="3 new messages"><span class="dot" aria-hidden="true"></span></span></li>
</ul>
<style>
  .badge-demo { display: flex; gap: 12px; list-style: none; padding: 0; font: 600 12px/1 Inter, system-ui, sans-serif; }
  .badge { display: inline-flex; align-items: center; gap: 4px; padding: 4px 10px; border-radius: 999px; }
  .badge svg { width: 12px; height: 12px; }
  .badge.status.success { background: #DCFCE7; color: #166534; }
  .badge.status.warning { background: #FEF3C7; color: #92400E; }
  .badge.status.danger  { background: #FEE2E2; color: #991B1B; }
  .badge.count { background: #2563EB; color: #fff; min-width: 28px; justify-content: center; }
  .badge.dot { background: transparent; padding: 4px; }
  .dot { width: 8px; height: 8px; border-radius: 50%; background: #DC2626; display: block; }
</style>
```

## 10. Implementation Checklist

- [ ] The closed variant set (`var(--comp-btn-variants)`) covers every button in the product — zero ad-hoc styled buttons.
- [ ] All heights read from the ramp (`--comp-btn-height-sm/md/lg`); touch-critical controls meet `var(--comp-btn-touch-min)`.
- [ ] Every button has hover, active, and `:focus-visible` states with the shared `var(--comp-btn-focus-ring)` treatment.
- [ ] Loading state pins the button's size, swaps in the spinner per `var(--comp-btn-loading-policy)`, and narrates via a live region.
- [ ] Every disabled button explains itself per `var(--comp-btn-disabled-policy)` — tooltip or helper text naming the unlock condition.
- [ ] Every icon-only button carries an aria-label (and ideally a visible tooltip); a screenshot audit finds zero "mystery buttons."
- [ ] Every status badge implements the `var(--comp-badge-signal-triple)` — color, icon, and text together, never color alone.
- [ ] Count badges cap at `var(--comp-badge-count-cap)` with the real total in aria-label; destructive actions confirm or undo.

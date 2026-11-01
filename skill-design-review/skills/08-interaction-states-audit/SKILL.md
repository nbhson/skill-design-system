---
name: interaction-states-audit
description: Every interactive element in every state — hover, focus, active, disabled, loading — designed, visible, and consistent, verified per surface.
tags: [interaction, states, focus, keyboard, audit]
related: [a11y-audit, motion-audit, consistency-audit]
---

# Design Review Guide: Interaction States Audit

## 1. Definition

Most surfaces ship with half their interaction states: hover works, focus is invisible, disabled is unexplained. The audit enumerates every interactive element and verifies all states exist and are visible: hover/active feedback, focus rings (2px + offset, 3:1 contrast), loading/disabled contracts, selected states, and error states — plus keyboard-only verification that focus is never lost and tab order is sensible. States are the difference between a surface that feels alive and one that feels like a printed screenshot; because the state list is finite and shared across components, the audit is a matrix rather than an open-ended judgment, and incomplete rows are concrete, fileable findings.

## 2. Core Principles

- **Every interactive element is enumerated:** buttons, links, cards, rows, tabs — each checked against the full state list.
- **The state list is complete:** hover, focus-visible, active/pressed, disabled, loading, selected, error — missing states are findings.
- **Focus is unmissable:** visible ring meeting 3:1 contrast (2.4.13), never `outline: none` without replacement.
- **Keyboard parity:** every state reachable and visible via keyboard — hover-only affordances are findings (shared with a11y-audit).
- **Disabled is explained:** the reason visible near the control (component-recipes contract) — bare disabled is a finding.
- **Loading replaces without reflow:** in-button spinners keep size (component-recipes contract).
- **Selected state is doubly signaled:** color + check/icon (1.4.1) — color-only selection is a finding.
- **Press feedback exists everywhere:** active states confirm the tap on touch surfaces — dead-feeling buttons are findings.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| State enumeration | `--rev-state-enumeration` | `all-interactives-listed` | Nothing skipped |
| State list | `--rev-state-list` | `hover,focus,active,disabled,loading,selected,error` | The complete set |
| Focus ring | `--rev-focus-ring` | `2px+offset-3:1` | WCAG 2.4.13 contract |
| No outline none | `--rev-no-outline-none` | `replacement-required` | Focus removal = blocker |
| Keyboard parity | `--rev-keyboard-parity` | `all-states-via-kb` | Hover-only = finding |
| Disabled explained | `--rev-disabled-explained` | `reason-visible` | Bare disabled = finding |
| Loading no reflow | `--rev-loading-no-reflow` | `size-stable` | In-place spinners |
| Selection signal | `--rev-selection-signal` | `color+icon` | 1.4.1 double signal |
| Press feedback | `--rev-press-feedback` | `active-state-everywhere` | Touch confirmation |
| States score | `--rev-states-score` | `per-surface` | Feeds report template |

Consume them by linking `assets/css/interaction-states-audit.css` at the review harness root; the audit matrix and its pass/fail markup read `var(--rev-...)` values so a contract change (for example, a stricter focus ring) updates the criteria everywhere at once.

## 4. Composition

- **Composes with component-recipes accessibility-wiring:** the wiring checklist is this audit's per-component criteria — a component wired per that checklist should pass its row of the state matrix by construction, which makes divergence between the two a signal that either the wiring or the matrix is stale.
- **Composes with a11y-audit (guide 04):** focus and keyboard passes are shared — coordinated scheduling, not duplicate work; the a11y audit owns the full WCAG sweep while this audit owns per-component state completeness, and both consume the same keyboard-only session log.
- **Composes with skill-animation micro-interactions:** state feedback motion uses motion tokens — verified here; a hover or pressed transition must use duration and easing tokens from the animation system, and a state with motion that ignores those tokens fails this audit's consistency check.

## 5. Signature Patterns

- **The state matrix walk:** per interactive element, a row of states checked (hover/focus/active/disabled/loading/selected/error) — incomplete rows are findings. The matrix is produced once per surface and kept in the review record, so regressions between reviews are diffs, not rediscoveries.
- **The keyboard-only pass:** complete the flow without the mouse, logging every invisible or stuck state — the parity proof. Anything operable by pointer but invisible or unreachable by keyboard is recorded against `--rev-keyboard-parity` with the exact keystroke where it failed.

## 6. Real-World Use Cases

- **Pre-release gates on interactive surfaces,** where a surface ships only when every row of the state matrix is complete.
- **Design system component audits,** where states are the usual gap between a polished default state and a production-ready component.
- **Audit deliverables:** outline:none regressions, hover-only menus, and bare disabled reported with blocker severity.

## 7. Combination Notes

### With other design-review skills

- **Good with review-process and report-template:** state findings map to a fixed severity scale (focus removal = blocker) and roll up into the per-surface states score.
- **Good with a11y-audit and content-microcopy-audit:** focus/keyboard parity overlaps a11y directly, and disabled/loading states need the copy audit's "reason visible" strings — the three audits share one keyboard session and one string dump.
- **Good with visual-hierarchy-audit, consistency-audit, typography-audit, spacing-rhythm-audit, perceived-performance, responsive-audit, and motion-audit:** each contributes context — hierarchy ranks which states matter most, consistency catches states styled differently per instance, motion checks the feedback transitions, and responsive/perceived-performance verify states hold at breakpoints and under latency.
- **No caution or avoid list:** state completeness is orthogonal to every other review lens; nothing about auditing states conflicts with another skill's scope.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** all three keep decoration low, which leaves the focus ring, pressed state, and selection signal as the strongest affordances on the surface — states do the expressive work the style declines to do with ornament, so the audit and the style pull in the same direction.
- **No caution entries:** none of the audited styles reward hiding states; even high-contrast or expressive styles keep focus visible, so the state contract survives every style pairing.

### With motion skills (companion repo skill-animation)

- **Good affinity with micro-interactions:** hover, pressed, and loading are the primary micro-interaction surface; the audit verifies each state exists and the micro-interactions skill verifies the transition between them is tokenized and non-decorative.
- **Good affinity with feedback-confirmation:** active states, loading spinners, and selection signals are confirmation patterns — the two skills share criteria, so a press-feedback finding here is usually a feedback-confirmation finding there, and they are filed once.

## 8. Anti-Patterns

- **outline:none regressions:** focus invisible to keyboard users
- **Hover-only affordances:** actions unreachable by touch/keyboard
- **Bare disabled:** greyed controls with no explanation
- **Color-only selection:** chosen states signaled by tint alone

### Accessibility Notes

This audit enforces WCAG 2.4.7 (focus visible), 2.4.13 (focus appearance), 1.4.1 (use of color), and 4.1.2 (name/role/value): state visibility and keyboard parity are blockers — the state matrix is the a11y contract in per-component form. The focus ring token encodes the appearance contract (2px ring, offset, 3:1 contrast against adjacent colors), so a failing ring is checked against the token before it is argued about; selection must double-signal beyond color; and every state change must remain exposed to assistive tech via name, role, and value, which is why the keyboard-only pass doubles as a screen-reader smoke test. The fallback rule: if the full matrix is too heavy, audit focus + disabled + loading first — those three states carry most user and a11y impact, and the remaining rows can be batched into a follow-up pass without losing blocker coverage.

## 9. Code Examples

### Example 1 — State matrix walker: each interactive row checked pass/fail

Tokens: `assets/css/interaction-states-audit.css`

```html
<div class="matrix-demo">
  <button class="btn" type="button">Save changes</button>
  <a class="link" href="#preview">Preview report</a>
  <input class="field" type="text" placeholder="Project name" />
</div>
<pre id="matrix-out"></pre>
<style>
  :root {
    /* mirrors assets/css/interaction-states-audit.css */
    --rev-focus-ring: 2px+offset-3:1;
    --rev-state-list: hover,focus,active,disabled,loading,selected,error;
    --rev-press-feedback: active-state-everywhere;
    --brand: #2563EB; --brand-press: #1D4ED8; --ring: #1D4ED8;
  }
  .btn {
    background: var(--brand); color: #fff; border: 0; border-radius: 8px;
    padding: 10px 20px; font: 600 14px/1 Inter, system-ui, sans-serif; cursor: pointer;
  }
  .btn:hover  { background: var(--brand-press); }
  .btn:active { background: var(--brand-press); transform: translateY(1px); }
  .btn:focus-visible { outline: 2px solid var(--ring); outline-offset: 2px; } /* 2px+offset-3:1 */
  .btn:disabled { opacity: .5; cursor: not-allowed; }
  .link { color: var(--brand); }
  .link:focus-visible { outline: 2px solid var(--ring); outline-offset: 2px; }
  .field:focus-visible { outline: 2px solid var(--ring); outline-offset: 2px; }
  pre { font: 12px/1.6 ui-monospace, monospace; }
</style>
<script>
  // Walker per --rev-state-enumeration: one row per element, one cell per state
  const STATES = '--rev-state-list'.length ? ['hover','focus','active','disabled','loading','selected','error'] : [];
  const rules = [...document.styleSheets[0].cssRules].map(r => r.selectorText || '').join(' ');
  const rows = [];
  for (const el of document.querySelectorAll('.btn, .link, .field')) {
    const row = { element: el.className, cells: {} };
    for (const s of STATES) {
      const pseudo = s === 'focus' ? 'focus-visible' : s;
      row.cells[s] = rules.includes('.' + el.className.split(' ')[0] + ':' + pseudo) ? 'PASS' : 'FAIL';
    }
    rows.push(row);
  }
  document.getElementById('matrix-out').textContent =
    rows.map(r => r.element + ': ' + STATES.map(s => s + '=' + r.cells[s]).join(' ')).join('\n');
</script>
```

### Example 2 — Keyboard-only flow: logging invisible and stuck states

```html
<div class="kb-flow">
  <input class="kb-field" type="email" placeholder="Email" />
  <button class="kb-btn" type="button">Send invite</button>
</div>
<ol id="kb-log"></ol>
<style>
  :root { --rev-keyboard-parity: all-states-via-kb; --rev-no-outline-none: replacement-required; }
  .kb-flow { max-width: 320px; font: 14px/1.5 Inter, system-ui, sans-serif; }
  .kb-field, .kb-btn { display: block; width: 100%; box-sizing: border-box; margin: 0 0 8px; padding: 10px; }
  .kb-btn { background: #2563EB; color: #fff; border: 0; border-radius: 8px; cursor: pointer; }
  /* Contract styles; the logger below audits them */
  .kb-field:focus-visible, .kb-btn:focus-visible { outline: 2px solid #1D4ED8; outline-offset: 2px; }
</style>
<script>
  // Keyboard-only pass: Tab through, log every stop and whether focus stayed visible.
  // Per --rev-keyboard-parity, a stop with no visible indicator is logged as stuck/invisible.
  const log = document.getElementById('kb-log');
  document.addEventListener('focusin', (e) => {
    const cs = getComputedStyle(e.target);
    const visible = cs.outlineStyle !== 'none' && parseFloat(cs.outlineWidth) >= 2;
    const li = document.createElement('li');
    li.textContent = (visible ? 'PASS — ' : 'FAIL — ') + (e.target.placeholder || e.target.textContent) +
      ' (per --rev-keyboard-parity)';
    log.appendChild(li);
  });
</script>
```

## 10. Implementation Checklist

- [ ] Every interactive element on the surface appears in the matrix per `var(--rev-state-enumeration)` — cards, rows, and tabs included, not just buttons and links.
- [ ] Each matrix row covers the full `var(--rev-state-list)` set — hover, focus-visible, active, disabled, loading, selected, error — with no empty cells.
- [ ] Every focus indicator meets the `var(--rev-focus-ring)` contract (2px + offset, 3:1) and zero instances of bare `outline: none` exist per `var(--rev-no-outline-none)`.
- [ ] The keyboard-only pass completed with `var(--rev-keyboard-parity)` results logged — no hover-only affordances, no lost focus.
- [ ] Disabled controls show a visible reason per `var(--rev-disabled-explained)`; bare greyed controls are filed as findings.
- [ ] Loading states hold size per `var(--rev-loading-no-reflow)` — in-place spinners, no layout shift.
- [ ] Selection double-signals per `var(--rev-selection-signal)` (color + check/icon) and every control answers per `var(--rev-press-feedback)` with an active state.
- [ ] The per-surface `var(--rev-states-score)` is recorded in the report template alongside the matrix artifact.

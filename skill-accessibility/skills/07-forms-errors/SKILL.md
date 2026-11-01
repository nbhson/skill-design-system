---
name: forms-errors
description: Labels, descriptions, and error wiring that make forms operable and recoverable - 3.3.1, 3.3.2, 3.3.3, 4.1.3 done as wiring, not styling.
tags: [forms, errors, labels, wcag, validation]
related: [focus-management, aria-fundamentals, screen-readers]
---

# Accessibility Skill: Forms & Error Handling

## 1. Definition

Forms are where accessibility failures cost users the most - a mislabeled field or a lost error can block a purchase, a signup, or a benefits application. This skill covers the full wiring: programmatic label association (1.3.1, 4.1.2), required and format hints (3.3.2), error identification in text (3.3.1), suggested corrections (3.3.3), and status announcements (4.1.3) - the mechanics that make forms work for screen readers, not just look clean. The organizing idea is that accessible forms are a wiring problem, not a styling problem: every hint, error, required marker, and status message must be programmatically connected to the field it serves, so assistive technology narrates the form exactly as a sighted user experiences it.

## 2. Core Principles

- **Every input has a programmatic label:** `<label for>` or aria-labelledby - placeholder text is not a label (it vanishes on type).
- **Instructions before the field, errors after it:** hints and errors wire via aria-describedby so screen readers read them in context.
- **Errors identify the field in text:** 'Email is invalid' - never color or icon alone (WCAG 3.3.1).
- **Announce form status politely:** error summaries and 'saved' confirmations via aria-live=polite (4.1.3); focus moves to the summary on failed submit.
- **Suggest the fix:** 'Enter a valid email like name@domain.com' beats 'Invalid input' (WCAG 3.3.3).
- **Preserve user input on errors:** a failed submit never wipes the form - the cruelest failure mode.
- **Do not rely on autocomplete alone, but do support it:** proper name/email/tel autocomplete attributes help everyone (1.3.5).
- **Validation timing is forgiving:** validate on blur or submit, never on every keystroke - mid-typing errors are noise.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Label policy | `--a11y-label-policy` | `programmatic-required` | `<label for>` or aria-labelledby; lint-blocks orphans |
| Hint wiring | `--a11y-hint-wiring` | `aria-describedby` | Format hints read after the label, before input |
| Error wiring | `--a11y-error-wiring` | `aria-describedby+aria-invalid` | Error text linked per field; flag on the input |
| Error summary | `--a11y-error-summary` | `focus-on-submit-fail` | Summary list receives focus; each item links to its field |
| Status announce | `--a11y-status-announce` | `aria-live-polite` | Saved/sent confirmations; never assertive for success |
| Required signal | `--a11y-required-signal` | `text-plus-aria-required` | Asterisk alone is not enough; say 'required' |
| Error message style | `--a11y-error-message-style` | `cause-plus-fix` | 3.3.3: state what is wrong and how to fix it |
| Input preservation | `--a11y-input-preservation` | `never-wipe` | Failed submits keep all user input |
| Validation timing | `--a11y-validation-timing` | `blur-or-submit` | No per-keystroke validation noise |
| Autocomplete attrs | `--a11y-autocomplete-attrs` | `name,email,tel...` | WCAG 1.3.5: standard autocomplete attributes |

Consume them by linking `assets/css/forms-errors.css` once at the app root: the policy tokens are read by form components and validation utilities (e.g. the timing a field validates on, whether a summary receives focus), while visual error/hint styling draws on design-token colors referenced through `var(--a11y-...)` contracts. A form that hardcodes its own validation behavior instead of reading these tokens forks the pattern - the summary, timing, and announcement rules must stay identical across every form in the product.

## 4. Composition

- **Composes with aria-fundamentals:** label, hint, and error wiring is `aria-describedby` traffic - the fundamentals skill governs the mechanics (names, idrefs, live regions) and this skill applies them to the highest-stakes surface in the product.
- **Composes with focus-management:** a failed submit moves focus to the error summary and each summary item jumps to its field; success announcements use live regions precisely so they never steal focus mid-task.
- **Composes with ux-writing (skill-ux-writing guides 03/08):** error cause-and-fix phrasing is a shared craft - the a11y wiring guarantees the message is read, the writing skill guarantees it is worth reading.

## 5. Signature Patterns

- **Error summary pattern:** on failed submit, render a list of linked errors at the top of the form and move focus to it; each item is a link that jumps to its field with describedby wiring intact, so keyboard and screen reader users get an index of everything wrong before touching a single control.
- **Inline-plus-summary:** field-level messages (via `aria-describedby` + `aria-invalid`) support immediate correction, while the summary provides orientation after submit - ship both, not either; inline-only loses the overview, summary-only loses the local context.

## 6. Real-World Use Cases

- **Checkout, signup, and application forms** - the highest-stakes surfaces where a lost error is a lost conversion or a denied benefit.
- **Multi-step wizards** where errors must not strand users mid-flow; each step validates, summarizes, and preserves.
- **Auditing existing forms:** hunting unlabeled fields, color-only errors, wiped inputs, and mid-typing scolding.

## 7. Combination Notes

### With other accessibility skills

- **Pairs naturally with aria-fundamentals and focus-management:** the label/describedby wiring and the focus-on-summary behavior are this skill's core mechanics, borrowed directly from those guides - a form without them is decoration.
- **Pairs with screen-readers and testing-audit:** listening scripts verify that error announcements and summary landings actually narrate; the audit lane stores those scripts as release evidence.
- **Pairs with color-contrast and cognitive-content:** error text must pass 4.5:1 and never signal by color alone, and cause-plus-fix phrasing serves cognitive-needs users as much as screen reader users.
- **Caution: none, avoid: none.** Forms sit in the center of the accessibility graph - every sibling skill has a claim on at least one form behavior, so there is no incompatible partner, only wiring that was never done.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** clean label-above-input layouts keep the label-field association visually and programmatically obvious, and flat error treatments (text + icon + border) pair naturally with the non-color-signal rule.
- **Caution with brutalism-ui:** oversized raw inputs and intentional label/input collisions tempt designers toward placeholder-as-label and color-only error states; if the style is adopted, the wiring tokens stay non-negotiable and the visual treatment adapts around them.

### With motion skills (companion repo skill-animation)

- **Good affinity with feedback-confirmation:** a polite 'saved' live-region announcement pairs with a subtle confirm animation - the motion reinforces the status message without replacing it.
- **Caution (general):** error shake or pulse animations must never be the only signal of failure, and per the companion repo's reduced-motion guidance, animation near error text collapses under `prefers-reduced-motion` while the text announcement remains.

## 8. Anti-Patterns

- **Placeholder-as-label** — hints that disappear on first keystroke and fail contrast at 4.5:1
- **Red-only errors** — color-coded failures with no text association - unreadable by AT and color-blind users
- **Error wipe** — failed submit resetting the form, destroying twenty minutes of user input
- **Keystroke scolding** — inline 'invalid' warnings firing mid-typing before the user finishes

### Accessibility Notes

This guide owns WCAG 3.3.1-3.3.8 and 4.1.2/4.1.3: forms are where legal risk concentrates because they are the path to every service - a form that cannot be completed by assistive technology is a service that does not exist for that user. The wiring tokens above encode the criteria as contracts: `--a11y-label-policy` and `--a11y-autocomplete-attrs` cover 4.1.2 and 1.3.5, `--a11y-hint-wiring` covers 3.3.2, `--a11y-error-wiring` and `--a11y-error-message-style` cover 3.3.1/3.3.3, and `--a11y-status-announce` plus `--a11y-error-summary` cover 4.1.3. The fallback rule: if field-level wiring fails or cannot be completed, the error summary pattern alone (focus + linked list + plain text) keeps the form accessible even with imperfect inline wiring - and failed submits must always preserve every keystroke the user entered.

## 9. Code Examples

### Example 1 — Signup form with hints, per-field errors, and a focused error summary

Tokens: `assets/css/forms-errors.css`

```html
<form id="signup" novalidate>
  <div id="summary" class="summary" tabindex="-1" hidden></div>
  <div class="field">
    <label for="name">Full name <span class="req">(required)</span></label>
    <input id="name" name="name" type="text" autocomplete="name" required aria-describedby="name-hint" />
    <p class="hint" id="name-hint">As it appears on your ID.</p>
    <p class="error" id="name-error" hidden></p>
  </div>
  <div class="field">
    <label for="email">Email <span class="req">(required)</span></label>
    <input id="email" name="email" type="email" autocomplete="email" required
           aria-describedby="email-hint email-error" aria-invalid="false" />
    <p class="hint" id="email-hint">Enter a valid email like name@domain.com.</p>
    <p class="error" id="email-error" hidden></p>
  </div>
  <button type="submit">Create account</button>
</form>
<script>
  const form = document.getElementById('signup'), summary = document.getElementById('summary');
  const rules = {
    name:  v => v.trim() ? null : 'Enter your full name.',
    email: v => /.+@.+\..+/.test(v) ? null : 'Enter a valid email like name@domain.com.'
  };
  // --a11y-validation-timing: blur-or-submit; never per keystroke
  form.addEventListener('blur', e => rules[e.target.name] && validateField(e.target), true);
  form.addEventListener('submit', e => {
    e.preventDefault();
    const failed = [...form.elements].filter(el => rules[el.name] && validateField(el));
    if (!failed.length) return; // success announces politely elsewhere; no focus steal
    summary.innerHTML =
      `<p>${failed.length} answers need fixing before you continue:</p><ul>` +
      failed.map(f => `<li><a href="#${f.id}">${f.labels[0].firstChild.textContent}: ${rules[f.name](f.value)}</a></li>`).join('') + `</ul>`;
    summary.hidden = false; summary.focus(); // --a11y-error-summary: focus-on-submit-fail
  });

  function validateField(input) {
    const msg = rules[input.name](input.value);
    const err = document.getElementById(input.id + '-error');
    input.setAttribute('aria-invalid', String(Boolean(msg))); // --a11y-error-wiring
    err.hidden = !msg; err.textContent = msg || '';
    return msg;
  }
</script>
<style>
  .field { max-width: 380px; margin-bottom: 16px; font: 14px/1.5 system-ui, sans-serif; }
  label  { display: block; font-weight: 600; margin-bottom: 4px; }
  .req   { font-weight: 400; color: #404040; } /* --a11y-required-signal: text, not just * */
  input  { width: 100%; padding: 8px 10px; border: 1px solid #737373; border-radius: 6px; }
  input[aria-invalid="true"] { border-color: #DC2626; border-width: 2px; }
  .hint  { margin: 4px 0 0; color: #525252; font-size: 13px; }
  .error { margin: 4px 0 0; color: #B91C1C; font-weight: 600; } .error::before { content: "Error: "; }
  .summary { border: 2px solid #DC2626; border-radius: 8px; padding: 12px 16px; margin-bottom: 16px; }
  .summary:focus { outline: 2px solid #1D4ED8; outline-offset: 2px; }
</style>
```

### Example 2 — Autosave status announced politely (never assertive for success)

Tokens: `assets/css/forms-errors.css`

```html
<form id="profile">
  <label for="bio">Short bio</label>
  <textarea id="bio" rows="3"></textarea>
  <p id="status" role="status"></p> <!-- --a11y-status-announce: aria-live-polite -->
</form>
<script>
  // Live region exists in the DOM before changes — injected regions announce nothing
  const status = document.getElementById('status');
  let t;
  // --a11y-validation-timing is blur-or-submit: save on change, not keystroke
  document.getElementById('bio').addEventListener('change', () => {
    clearTimeout(t);
    t = setTimeout(() => { save(); status.textContent = 'Changes saved.'; }, 600);
  });
  function save() { /* persist draft; user input is never wiped on failure */ }
</script>
<style>
  #profile { max-width: 380px; font: 14px/1.5 system-ui, sans-serif; }
  label { display: block; font-weight: 600; margin-bottom: 4px; }
  textarea { width: 100%; padding: 8px 10px; border: 1px solid #737373; border-radius: 6px; }
  #status { min-height: 1.5em; color: #15803D; font-weight: 600; }
</style>
```

## 10. Implementation Checklist

- [ ] Every input has a programmatic label per `--a11y-label-policy` (`<label for>` or aria-labelledby) - zero placeholder-only fields.
- [ ] Hints and errors wire through `var(--a11y-hint-wiring)` / `var(--a11y-error-wiring)` (aria-describedby + aria-invalid) and all idrefs resolve.
- [ ] Error text follows `--a11y-error-message-style` (cause-plus-fix) and identifies the field in words, never color or icon alone.
- [ ] Failed submit moves focus to the error summary (`--a11y-error-summary`) and each summary item links to its field.
- [ ] Success and saved messages announce via `--a11y-status-announce` (aria-live=polite) - assertive is reserved for real failures.
- [ ] Required state signals as `--a11y-required-signal` (text plus aria-required), not an asterisk alone.
- [ ] Validation timing respects `--a11y-validation-timing` (blur-or-submit) with no per-keystroke messages.
- [ ] Standard autocomplete attributes (`--a11y-autocomplete-attrs`) are present, and failed submits never wipe user input.

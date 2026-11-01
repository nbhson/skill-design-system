---
name: forms-inputs
description: Text fields, selects, checkboxes, and validation layouts: the label-hint-error wiring recipe and forgiving-validation timing.
tags: [forms, inputs, validation, accessibility, field-components]
related: [buttons-badges, tables-data-grid, modals-dialogs]
---

# Component Recipe: Forms & Input Recipes

## 1. Definition

Form inputs are the highest-traffic, highest-stakes components: text fields, selects, checkboxes, radios, switches, and their validation choreography. The recipe is structural, not cosmetic: visible labels wired programmatically, hints via aria-describedby, errors flagged with aria-invalid, and validation timing that forgives mid-typing — the same wiring the a11y repo mandates, expressed as a component recipe. Because every user passes through a signup, checkout, or settings form, the quality of this one component family disproportionately shapes product trust; the recipe turns scattered per-form decisions into a single Field contract implemented once and consumed everywhere.

## 2. Core Principles

- **Visible labels always:** placeholder-only inputs are banned — labels persist above or beside the field (WCAG 3.3.2).
- **The wiring recipe:** label-for + hint-describedby + error-describedby + aria-invalid — implemented once in the field component, consumed everywhere.
- **Input heights match the button ramp:** 40px default, 48px on mobile forms — a form is one rhythm.
- **Validation timing:** validate on blur or submit; inline errors clear on fix; never per-keystroke scolding.
- **Errors state cause + fix:** 'Enter a valid email like name@domain.com' — the message content is part of the recipe (ux-writing guide 08).
- **Choice controls are honest:** checkbox = independent toggles, radio = exclusive pick, switch = instant-effect setting — semantics match behavior.
- **Disabled vs readonly are distinct:** disabled removes from tab order (and needs explanation); readonly stays focusable and copyable.
- **Autocomplete attributes ship:** name/email/tel autofill (WCAG 1.3.5) is part of the recipe, not a nice-to-have.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Height md | `--comp-input-height-md` | `40px` | Matches btn-height-md; one rhythm |
| Height lg | `--comp-input-height-lg` | `48px` | Mobile/primary forms |
| Label policy | `--comp-input-label-policy` | `visible-always` | Placeholder-only banned (3.3.2) |
| Wiring | `--comp-input-wiring` | `label+hint+error-wired` | The field component implements once |
| Error flag | `--comp-input-error-flag` | `aria-invalid+describedby` | Programmatic error association |
| Validation timing | `--comp-input-validation-timing` | `blur-or-submit` | No per-keystroke validation |
| Error style | `--comp-input-error-style` | `cause-plus-fix` | Message format shared with ux-writing |
| Choice semantics | `--comp-input-choice-semantics` | `checkbox-radio-switch-distinct` | Control semantics match behavior |
| Readonly vs disabled | `--comp-input-readonly-vs-disabled` | `readonly-focusable` | Readonly keeps focus/copy |
| Autocomplete | `--comp-input-autocomplete` | `standard-attrs` | WCAG 1.3.5 autofill support |

Consume them by linking `assets/css/forms-inputs.css` once at the app root and styling fields against `var(--comp-input-...)`. Like the button system, several tokens are behavioral contracts (`label-policy`, `wiring`, `validation-timing`, `error-style`) — they exist so reviews and linters can assert the wiring, not just the pixel heights. Heights reference the button ramp values so forms and actions share one rhythm.

## 4. Composition

- **Composes with buttons-badges:** submit/primary actions share the size ramp and loading contract.
- **Composes with forms-errors (skill-accessibility guide 07):** that guide owns the WCAG criteria; this recipe implements the component.
- **Composes with ux-writing (skill-ux-writing):** label and error phrasing follow the voice & tone and error message guides.

## 5. Signature Patterns

- **Field component with slots:** one Field wrapper owns label/hint/error/error-flag wiring; inputs plug in — wiring drift becomes impossible. Teams stop hand-wiring `<label for>` per form; they compose `<Field label hint error>` and the accessibility wiring is guaranteed by construction.
- **Error summary on submit:** failed submits focus a linked error list at top + per-field inline messages (a11y repo pattern). Each summary entry is an anchor to its field, so keyboard and screen reader users land directly on the first broken input instead of tab-hunting.

## 6. Real-World Use Cases

- **Any form:** signup, checkout, settings, search.
- **Design systems:** the field component is the second component built (after button).
- **Audit:** placeholder-labels, unwired errors, per-keystroke validation noise.

## 7. Combination Notes

### With other component-recipe skills

- **Good with buttons-badges:** submits share the 40/48px ramp and the loading contract, so a form reads as one rhythm from input to action.
- **Good with modals-dialogs, dropdowns-menus, and tables-data-grid:** dialog forms consume the Field recipe; select-style inputs align with the menu keyboard contract; filter rows and inline editors reuse field heights and validation wiring.
- **Good with empty-loading-error, toasts-notifications, tabs-accordions, cards-lists, navigation-patterns, command-palette:** forms appear inside all these containers; the Field recipe keeps them identical wherever embedded.
- **Good with accessibility-wiring:** the wiring recipe (label/hint/error/invalid) is exactly the layer that skill verifies — the recipe builds it, the wiring skill audits it.
### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** clean bordered fields with persistent labels suit restrained styles; class-morphism's layered surfaces still keep the label-hint-error anatomy intact.
- **Caution with brutalism-ui:** brutalist styling favors raw, borderless, or unconventional inputs that tend to erase the visible-label and focus contracts — any deviation must preserve the wiring even if it restyles the chrome.

### With motion skills (companion repo skill-animation)

- **Good affinity with feedback-confirmation:** success/error state changes (border color, inline error entrance) should animate with duration tokens, and the error summary appearing on submit benefits from a quick, non-blocking reveal.
- **Good affinity with micro-interactions:** focus rings, label transitions, and switch toggles are micro-interaction territory — but validation must never animate in per-keystroke; timing tokens serve the blur/submit contract, not contradict it.

## 8. Anti-Patterns

- **Placeholder-as-label:** hints vanishing on first keystroke
- **Unwired errors:** red borders with no aria-invalid or text association
- **Keystroke scolding:** 'invalid' firing mid-typing before the user finishes
- **Mixed control semantics:** switches that submit forms, checkboxes that act instantly

### Accessibility Notes

The recipe implements WCAG 3.3.1–3.3.5, 1.3.5, and 4.1.2 at the component level: programmatic labels, described-by wiring, forgiving timing, and autofill — a11y repo guide 07 owns the criteria, this recipe ships the mechanics. Concretely that means every input has a persistent visible label tied with `for`/`id`, hints and errors are appended into the control's describedby chain so screen readers hear "Email — we never share it — Enter a valid email like name@domain.com — invalid," and `autocomplete` attributes let browsers and password managers fill correctly. Timing is an accessibility feature: validating on blur or submit respects users who type slowly, use SIPs, or compose with dictation. If the field wrapper cannot be adopted repo-wide, ship the wiring checklist per form (label-for, describedby, invalid, summary) — the wiring is the deliverable, the wrapper is the convenience.

## 9. Code Examples

### Example 1 — Field wrapper: label/hint/error wiring, blur validation, error summary

Tokens: `assets/css/forms-inputs.css`

```html
<form id="signup" novalidate>
  <div id="summary" class="summary" hidden tabindex="-1" role="alert">
    <strong>Fix 1 error to continue:</strong> <a href="#email">Email — Enter a valid email like name@domain.com</a>
  </div>
  <div class="field" data-field="email">
    <label for="email">Work email</label>
    <span id="emailHint" class="hint">We only use this for account recovery.</span>
    <input id="email" name="email" type="email" autocomplete="email" aria-describedby="emailHint emailError">
    <p id="emailError" class="error" hidden></p>
  </div>
  <button class="btn primary" type="submit" style="height: var(--comp-input-height-md)">Create account</button>
</form>
<script>
  const form = document.getElementById('signup');
  const input = document.getElementById('email');
  const err = document.getElementById('emailError');
  const summary = document.getElementById('summary');
  const valid = v => /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v);
  function validate() { // blur-or-submit timing, never per keystroke
    if (valid(input.value)) {
      input.removeAttribute('aria-invalid');
      err.hidden = true; input.setAttribute('aria-describedby', 'emailHint');
      return true;
    }
    err.textContent = 'Enter a valid email like name@domain.com'; // cause + fix
    err.hidden = false;
    input.setAttribute('aria-invalid', 'true');
    input.setAttribute('aria-describedby', 'emailHint emailError');
    return false;
  }
  input.addEventListener('blur', validate);
  input.addEventListener('input', () => { if (input.getAttribute('aria-invalid') === 'true') validate(); }); // clears on fix
  form.addEventListener('submit', e => {
    e.preventDefault();
    if (!validate()) { summary.hidden = false; summary.focus(); return; } // summary receives focus on failed submit
    summary.hidden = true;
  });
</script>
<style>
  form { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 360px; display: grid; gap: 12px; }
  .field { display: grid; gap: 4px; } label { font-weight: 600; }
  .hint { color: #737373; font-size: 12px; }
  input { border: 1px solid #D4D4D4; border-radius: 8px; padding: 0 12px; font: inherit; height: var(--comp-input-height-md); }
  input[aria-invalid="true"] { border-color: #DC2626; } input:focus-visible { outline: 2px solid #2563EB; outline-offset: 2px; }
  .summary { background: #FEE2E2; border: 1px solid #DC2626; border-radius: 8px; padding: 10px 12px; }
  .summary a { color: #991B1B; } .error { color: #B91C1C; margin: 0; font-size: 13px; }
</style>
```

### Example 2 — Choice controls: checkbox vs radio vs switch semantics

Tokens: `assets/css/forms-inputs.css`

```html
<fieldset style="height:auto">
  <legend>Notification channels</legend> <!-- checkboxes: independent toggles -->
  <label><input type="checkbox" name="channels" value="email" checked> Email</label>
  <label><input type="checkbox" name="channels" value="sms"> SMS</label>
</fieldset>
<fieldset>
  <legend>Plan</legend> <!-- radios: exclusive pick -->
  <label><input type="radio" name="plan" value="free" checked> Free</label> <label><input type="radio" name="plan" value="pro"> Pro</label>
</fieldset>
<!-- switch: instant-effect setting, role=switch, no submit button -->
<label class="switch-row">
  <span id="betaLabel">Beta features</span>
  <button type="button" role="switch" aria-checked="false" aria-labelledby="betaLabel" id="beta"></button>
</label>
<script>
  const sw = document.getElementById('beta');
  sw.addEventListener('click', () => { // instant effect: applies immediately, no form submit
    const on = sw.getAttribute('aria-checked') === 'true';
    sw.setAttribute('aria-checked', String(!on));
    document.documentElement.classList.toggle('beta', !on);
  });
</script>
<style>
  fieldset { border: 1px solid #D4D4D4; border-radius: 8px; font: 14px/1.6 Inter, system-ui, sans-serif; max-width: 320px; }
  .switch-row { display: flex; align-items: center; gap: 10px; font: 14px Inter, system-ui, sans-serif; margin-top: 12px; }
  [role="switch"] { width: 40px; height: var(--comp-input-height-md); border-radius: 999px; border: 1px solid #D4D4D4;
                    background: #F5F5F5; cursor: pointer; position: relative; padding: 0; }
  [role="switch"][aria-checked="true"] { background: #2563EB; border-color: #2563EB; }
  [role="switch"]::after { content: ""; position: absolute; top: 50%; left: 4px; width: 14px; height: 14px; border-radius: 50%; background: #fff; transform: translateY(-50%); transition: left 150ms ease; }
  [role="switch"][aria-checked="true"]::after { left: 20px; } [role="switch"]:focus-visible { outline: 2px solid #2563EB; outline-offset: 2px; }
</style>```

## 10. Implementation Checklist

- [ ] Every input has a persistent visible label wired with `for`/`id` per `var(--comp-input-label-policy)` — zero placeholder-only fields.
- [ ] All fields go through the Field wiring (`var(--comp-input-wiring)`): hint and error join the control's describedby chain.
- [ ] Errors set `aria-invalid` per `var(--comp-input-error-flag)` and clear programmatically when the user fixes the value.
- [ ] Validation runs only on blur or submit (`var(--comp-input-validation-timing)`) — no per-keystroke error messaging anywhere.
- [ ] Error messages follow `var(--comp-input-error-style)`: they name the cause and the fix, in the product's voice.
- [ ] Choice controls honor `var(--comp-input-choice-semantics)`: checkboxes toggle independently, radios are exclusive, switches apply instantly with `role="switch"`.
- [ ] Disabled fields are explained; readonly fields stay focusable and copyable per `var(--comp-input-readonly-vs-disabled)`.
- [ ] Inputs ship `autocomplete` attributes per `var(--comp-input-autocomplete)`, and heights match the shared 40/48px ramp.

---
name: forms-labels
description: The form copy layer — label phrasing, hint placement, required/optional marking, and validation copy timed to forgive rather than scold.
tags: [forms, labels, validation, errors, ux-writing]
related: [error-messages, component-microcopy, accessible-writing]
---

# UX Writing Guide: Form Labels & Help Text

## 1. Definition

Forms are where copy and structure fuse: label phrasing (questions vs imperatives), hint placement (above, beside, below), the required/optional convention (mark optional, not required), inline validation copy (timing that forgives mid-typing), and the error summary. This guide owns the strings of the form layer; the component-recipes field recipe owns the wiring, and the skill-accessibility forms-errors guide owns the criteria — three layers, one contract. The copy decisions are not decoration: a mislabeled field, a vanished hint, or a scolding validator directly changes completion rates, and the discipline exists to make those decisions once, per form, before build.

## 2. Core Principles

- **Labels are questions or imperatives - pick one per form:** `What's your email?` or `Email address`, never mixed within a form; the switch is invisible to writers and jarring to readers.
- **Mark optional, not required:** an asterisk convention requires teaching a legend most users never read; marking the few optional fields teaches nothing and reads instantly.
- **Hints live below labels, above errors:** persistent helper text, never placeholder-only — a hint inside the field disappears exactly when the user needs it (WCAG 3.3.2).
- **Validation forgives:** validate on blur or submit, never per-keystroke — `Enter a valid email` firing mid-typing is scolding the user for not being finished.
- **Error copy shows the fix inline:** `Enter a valid email like name@domain.com` — the format is part of the message, not a support article the user must go find.
- **Error summaries on submit:** a top-of-form list with anchor links + focus — never a silent return to the top of the form with nothing highlighted.
- **Input purpose copy matches autofill:** labels align with autocomplete tokens (`name`, `email`, `tel`) so browsers can help — WCAG 1.3.5 support as a copy decision.
- **Group labels for choice sets:** fieldsets with legends for radio/checkbox groups — `Notification preferences` wrapping its options, so the question travels with the choices.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Label form | `--uxw-label-form` | `question-or-imperative` | One style per form, not mixed |
| Optional marking | `--uxw-optional-marking` | `mark-optional` | Asterisks require teaching; (optional) does not |
| Hint position | `--uxw-hint-position` | `below-label-persistent` | Never placeholder-only |
| Validation timing | `--uxw-validation-timing` | `blur-or-submit` | Forgiving; no keystroke scolding |
| Validation copy | `--uxw-validation-copy` | `fix-inline-with-example` | Format shown in the message |
| Error summary | `--uxw-error-summary` | `top-of-form+anchors+focus` | Failed submits are loud |
| Error clear | `--uxw-error-clear` | `clears-on-fix` | Errors retract when corrected |
| Autofill alignment | `--uxw-autofill-alignment` | `label-matches-attr` | WCAG 1.3.5 support |
| Group labelling | `--uxw-group-labelling` | `fieldset+legend` | Choice sets have group labels |
| Required policy | `--uxw-required-policy` | `explained-once` | If asterisks used, legend explains |

Consume these spec tokens by linking `assets/css/forms-labels.css` at the app root and reading `var(--uxw-...)` from form styles and validation logic — they encode behavior (timing, clearing, focus) as named contracts, so a validator that fires on keystroke or an error that never retracts is a token violation reviewable in code, not a UX opinion.

## 4. Composition

- **Composes with error-messages (guide 03):** validation copy is the error taxonomy's validation class applied to fields — the three-part contract (what happened, why, the fix) shrinks into one inline line per field.
- **Composes with component-microcopy (guide 07):** labels and hints are microcopy slots with form-specific budgets — persistence rules and the placeholder ban are defined there and enforced here.
- **Composes with the skill-accessibility forms-errors guide and component-recipes forms-inputs recipe:** the criteria layer and the wiring layer of the same contract; this guide supplies the strings those layers carry.

## 5. Signature Patterns

- **The form copy sheet:** per form — label style, optional convention, validation copy per field, summary behavior — reviewed before build. Like an API contract, it is cheap to review early and expensive to rework after wiring.
- **The forgiving-validation pattern:** blur validation with clearing-on-fix copy — the timing and the retract are one pattern. An error that validates late but never clears is half the pattern; the user can't tell whether the fix landed.

## 6. Real-World Use Cases

- **Signup, checkout, settings, and any multi-field surface** — the default consumer of this guide's label, hint, and validation contracts.
- **High-stakes forms (payments, applications)** where copy errors cost conversions — forgiving timing and inline fixes matter most when the user is tense and the fields are long.
- **Audits hunting placeholder-labels, asterisk sprawl, keystroke scolding, and silent failed submits** — four findings that predictably trace back to missing form copy conventions.

## 7. Combination Notes

### With other ux-writing skills

- **Pairs naturally with error-messages (guide 03):** form validation is the taxonomy's most frequent consumer; the guide's fix-first copy style is what inline validation copy shrinks from, so the two must agree on voice and structure.
- **Pairs with component-microcopy (guide 07) and writing-principles:** labels and hints inherit microcopy's persistence rules and sentence case; forms are simply the densest application of those foundations.
- **Pairs with button-labels, onboarding-copy, and empty-states:** submit buttons follow verb-object rules, onboarding forms lean on encouraging hints, and empty results after a form shares the same voice.
- **Pairs with accessible-writing and copy-audit:** the 3.3.1–3.3.5 criteria are expressed as strings here, and the copy sheet is a natural audit artifact — every field's strings reviewed in one place.
- **Pairs with notifications and voice-tone:** submit outcomes surface as toasts or inline banners governed by the tone matrix's error row.
- **Pairs with localization-i18n:** label lengths and validation copy must survive expansion; the one-style-per-form rule also has to survive translation, which favors imperative labels for flexibility.
- **No avoid list:** every skill that touches a form-compatible surface composes cleanly — the risk is wiring forms without the copy sheet, which is a sequencing problem, not an incompatibility.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** all three keep form chrome minimal, which puts the burden of clarity on labels and hints — persistent helper text and (optional) marks do the work borders and icons no longer do.
- **Caution with brutalism-ui:** its deliberately raw, rule-breaking surfaces may want stark all-caps labels or stripped helper text; if the style wins, keep the 3.3.2 persistence and the error summary — those are contracts, not styling.

### With motion skills (companion repo skill-animation)

- **Good affinity with feedback-confirmation:** an error appearing on blur and retracting on fix is a feedback moment — animate retraction so the clear-on-fix token feels like relief, not flicker.
- **Good affinity with micro-interactions:** focus transitions from summary anchor to field, and hint reveals, should use motion tokens; keep animations short enough that the read budget of the error copy is respected.
- **Caution, generally:** animated label-to-placeholder morphs (floating labels) quietly reintroduce the placeholder-as-label failure when the label shrinks into the field — if the style demands floating labels, the visible label must remain persistent at rest.

## 8. Anti-Patterns

- **Placeholder-as-label:** the vanish-on-focus instruction
- **Asterisk sprawl:** every field starred, meaning nothing is required
- **Keystroke scolding:** 'Invalid' firing before the user finishes typing
- **Silent failed submits:** form returns to top with no summary and no focus

### Accessibility Notes

This guide implements the copy layer of WCAG 3.3.1–3.3.5 and 1.3.5: visible labels, correct-by-construction hints, suggested fixes, purpose-matched autofill — the a11y repo guide 07 criteria expressed as strings. Concretely: every input has a persistent visible label tied by `for`/`id`, hints are programmatically associated (`aria-describedby`), error messages identify the field and suggest the fix (3.3.3), errors that constrain format show it (`name@domain.com`), and labels match their autocomplete attributes so browsers and AT can offer the right assistance. The fallback rule keeps the contract shippable in stages: if per-field validation copy cannot ship in v1, ship submit-time summary + inline red text at minimum - the summary carries the a11y contract, because a focused, anchor-linked list of errors satisfies 3.3.1 and 3.3.3 even when the per-field copy is still generic.

## 9. Code Examples

### Example 1 — Forgiving validation with error summary

Tokens: `assets/css/forms-labels.css`

```html
<form id="signup" novalidate>
  <div id="summary" class="summary" tabindex="-1" hidden></div>
  <div class="field">
    <label for="email">Email address</label>
    <p class="hint" id="emailHint">We send a confirmation here — no marketing.</p>
    <input type="email" id="email" name="email" autocomplete="email" aria-describedby="emailHint" required>
    <p class="error" id="emailErr" hidden></p>
  </div>
  <div class="field">
    <label for="phone">Phone <span class="opt">(optional)</span></label>
    <input type="tel" id="phone" name="phone" autocomplete="tel">
  </div>
  <button type="submit">Create account</button>
</form>
<script>
  const form = document.getElementById('signup'), email = document.getElementById('email');
  const err = document.getElementById('emailErr'), hint = document.getElementById('emailHint');
  const summary = document.getElementById('summary');
  const re = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
  function validate() {
    const ok = re.test(email.value);
    err.hidden = ok; email.setAttribute('aria-invalid', String(!ok));
    if (!ok) err.textContent = 'Enter a valid email like name@domain.com'; // fix shown inline
    return ok; // hidden when fixed — clears-on-fix
  }
  email.addEventListener('blur', () => { if (email.value) validate(); }); // blur, not keystroke
  form.addEventListener('submit', e => {
    e.preventDefault();
    const links = [];
    if (!validate()) links.push({ id: 'email', msg: 'Enter a valid email like name@domain.com' });
    if (links.length) {
      summary.hidden = false;
      summary.innerHTML = 'Fix 1 error to continue:<ul>' +
        links.map(l => `<li><a href="#${l.id}">${l.msg}</a></li>`).join('') + '</ul>';
      summary.focus(); // loud submit: summary + focus
    }
  });
</script>
<style>
  :root { /* production: var(--uxw-...) from assets/css/forms-labels.css */
    --uxw-validation-timing: blur-or-submit; --uxw-error-clear: clears-on-fix; }
  body { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 400px; margin: 24px; }
  .field { margin-bottom: 16px; }
  label { display: block; font-weight: 600; margin-bottom: 4px; }
  .opt { font-weight: 400; color: #404040; }
  .hint, .error { margin: 4px 0 0; font-size: 13px; }
  .error { color: #b91c1c; font-weight: 500; }
  input { width: 100%; padding: 8px 10px; border: 1px solid #d4d4d4; border-radius: 6px; box-sizing: border-box; }
  input[aria-invalid="true"] { border-color: #b91c1c; }
  .summary { border: 2px solid #b91c1c; border-radius: 8px; padding: 12px; margin-bottom: 16px; }
</style>
```

### Example 2 — Group labels and autofill-aligned fields

Tokens: `assets/css/forms-labels.css`

```html
<form>
  <fieldset>
    <legend>Notification preferences</legend>
    <label><input type="radio" name="pref" value="email" checked> Email me weekly</label>
    <label><input type="radio" name="pref" value="none"> No notifications</label>
  </fieldset>
  <div>
    <label for="fname">Full name</label> <!-- matches autocomplete token "name" (1.3.5) -->
    <input type="text" id="fname" autocomplete="name">
  </div>
  <button type="submit">Save preferences</button>
</form>
<style>
  :root { --uxw-group-labelling: fieldset+legend; --uxw-autofill-alignment: label-matches-attr; }
  body { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 360px; margin: 24px; }
  fieldset { border: 1px solid #d4d4d4; border-radius: 8px; margin: 0 0 16px; }
  legend { font-weight: 600; padding: 0 6px; }
  label { display: block; margin: 6px 0; font-weight: 500; }
  input[type="text"] { width: 100%; padding: 8px 10px; border: 1px solid #d4d4d4; border-radius: 6px; box-sizing: border-box; }
  button { padding: 10px 20px; border: 0; border-radius: 8px; background: #1d4ed8; color: #fff; cursor: pointer; }
</style>
```

## 10. Implementation Checklist

- [ ] Every form declares one label style per `--uxw-label-form` — question or imperative, never mixed.
- [ ] Optional fields are marked with `(optional)` per `--uxw-optional-marking`; if asterisks are used anyway, a legend explains them once per `--uxw-required-policy`.
- [ ] Hints sit below labels, stay visible, and are associated via `aria-describedby` per `--uxw-hint-position` — zero placeholder-only fields (3.3.2).
- [ ] Validation fires on blur or submit per `--uxw-validation-timing` — no keystroke-time error messages anywhere.
- [ ] Validation copy shows the fix with an example per `--uxw-validation-copy`, and errors retract on fix per `--uxw-error-clear`.
- [ ] Failed submits render a top-of-form summary with anchor links and move focus there per `--uxw-error-summary`.
- [ ] Labels match their autocomplete attributes per `--uxw-autofill-alignment` (1.3.5), and choice sets use fieldset + legend per `--uxw-group-labelling`.
- [ ] Each form ships a copy sheet — label style, optional convention, per-field validation copy — reviewed before wiring.

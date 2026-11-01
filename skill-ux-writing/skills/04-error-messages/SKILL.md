---
name: error-messages
description: The three-part contract: what went wrong, why (in user terms), and the fix - blame-free, specific, and never a stack trace.
tags: [errors, microcopy, ux-writing, forms, accessibility]
related: [writing-principles, forms-labels, notifications]
---

# UX Writing Guide: Error Messages

## 1. Definition

Error messages are where products are judged: users meeting an error are already stressed, and the copy either recovers trust or burns it. The discipline is the three-part contract - what happened, why (translated to user terms), what to do next - phrased blame-free ("We couldn't process your card" not "You entered an invalid card"), with specific fixes ("Enter a valid email like name@domain.com"), and a hard ban on error codes as primary text, stack traces, and dead ends.

## 2. Core Principles

- **The three-part contract is mandatory:** what + why + fix; any message missing a part is incomplete.
- **Blame-free framing:** the system takes responsibility - "We couldn't load this page", never "You made an error".
- **Fixes are specific and actionable:** "Enter a valid email like name@domain.com", not "Invalid input".
- **No error codes as primary text:** codes (0x8007) go in a details expander for support - humans read the sentence.
- **Errors are visible and persistent where it matters:** form errors stay until fixed; toast errors do not auto-dismiss.
- **Position at the point of failure:** inline next to the field, or as an error summary with anchor links on submit.
- **One voice for all errors:** the error taxonomy (network/permission/not-found/validation) ships approved copy patterns - engineers pick, not invent.
- **Errors pair with recovery paths:** retry, request access, contact support - a message without a path is a dead end.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Structure | `--uxw-error-structure` | `what+why+fix` | The three-part message contract |
| Blame | `--uxw-error-blame` | `system-responsibility` | Blame-free phrasing always |
| Fix specificity | `--uxw-error-fix-specificity` | `example-included` | Show the correct format inline |
| Code policy | `--uxw-error-code-policy` | `details-expander-only` | Codes for support, not primary text |
| Persistence | `--uxw-error-persistence` | `until-fixed-or-dismissed` | No auto-dismiss for errors |
| Position | `--uxw-error-position` | `inline-or-anchored-summary` | At the point of failure |
| Taxonomy | `--uxw-error-taxonomy` | `network,permission,not-found,validation` | Approved copy pattern per class |
| Recovery | `--uxw-error-recovery` | `retry-or-alternative` | Every error has a path forward |
| Error flag | `--uxw-error-flag` | `aria-invalid+describedby` | Programmatic association (a11y) |
| Error focus | `--uxw-error-focus` | `summary-on-submit` | Failed submit focuses the error list |

Consume them by linking `assets/css/error-messages.css` at the app root and reading `var(--uxw-error-<role>)` wherever error copy or its wiring is configured - persistence timers, focus targets, and taxonomy keys resolve through tokens, never hardcoded per screen.

## 4. Composition

- **Composes with writing-principles (guide 01):** blame-free framing and plain language are inherited contracts - this guide applies them under stress, where they matter most.
- **Composes with forms-labels (guide 08):** field-level validation copy is the highest-traffic error surface; the validation timing and retract rules there are this taxonomy's validation class applied to fields.
- **Composes with skill-accessibility forms-errors + component-recipes forms-inputs:** the wiring layer (aria-invalid, describedby, summaries with focus) is the component implementation of this copy contract - copy and wiring ship together or the message fails silently for AT users.

## 5. Signature Patterns

- **The error taxonomy:** one approved copy pattern per error class (network/permission/not-found/validation) with slots for specifics - scale without drift, because engineers pick from a list instead of inventing phrasing under deadline.
- **The three-part template:** "We couldn't [action]. [Why in user terms]. [Fix/next step]." - engineers fill slots; the structure itself guarantees completeness, so a missing why or fix is visible in review.

## 6. Real-World Use Cases

- **Form validation, payments, uploads, and any async failure surface:** wherever the system can fail, the three-part contract applies.
- **Support deflection:** specific errors with concrete fixes reduce ticket volume measurably - each ambiguous message is a future ticket.
- **Audit:** bare "Error" toasts, codes shown as primary text, dead-end messages with no recovery path.

## 7. Combination Notes

### With other ux-writing skills

- **Good with writing-principles and voice-tone:** blame-free phrasing and the calm-error tone row are this guide's foundation; error paths are where both contracts are tested hardest, and the stress rule (humor off) is non-negotiable here.
- **Good with forms-labels, notifications, button-labels, and empty-states:** validation copy and toast errors are the densest error surfaces with persistence shared (`until-fixed-or-dismissed`), recovery paths need specific action labels ("Retry upload"), and not-found errors often resolve into empty states.
- **Good with accessible-writing, copy-audit, and localization-i18n:** programmatic association is copy's a11y half, the string inventory catches error-copy drift, and idiom-heavy error phrasing is flagged for i18n review. There is no caution or avoid list: error copy composes safely with every sibling discipline - the only incompatible practice is bypassing the taxonomy entirely.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** error states in these styles read as calm, text-first blocks - the three-part contract needs no decoration, and design tokens supply the danger ramp and surface pairings.
- **Caution with collage-art:** expressive, layered compositions can bury the error text or let the illustration compete with the fix; if the style demands it, the error copy block stays visually isolated and carries the full message on its own.

### With motion skills (companion repo skill-animation)

- **Good affinity with feedback-confirmation and easing-timing:** errors enter with a brief, attention-earning transition (a short fade/translate at token durations) - enough to draw the eye, never so much that reading is delayed.
- **No caution list:** motion never conflicts with error copy, but the persistence rule bounds it - entrance animation must not delay visibility, and errors never animate out before they are read or fixed.

## 8. Anti-Patterns

- **The dead-end error** — 'Something went wrong' with no cause and no path
- **Stack traces in UI** — technical internals shown to users as primary content
- **Blame framing** — 'You entered an invalid...' - the system owns the failure
- **Disappearing errors** — toast errors that vanish before they are read

### Accessibility Notes

Errors implement WCAG 3.3.1/3.3.3 and 4.1.3: text identification of errors, suggestions for correction, and polite narration - error copy must be programmatically associated (`aria-describedby`, `aria-invalid`) or narrated, never color-only (a11y repo guide 07). The error-flag and error-focus tokens encode this as contract: every invalid field is flagged programmatically, and a failed submit moves focus to the error summary so the failure is the first thing a screen reader announces. The fallback is equally concrete: if programmatic association cannot ship per field, an error summary on submit with focus + anchor links satisfies the contract - completeness of message before per-field elegance, and the anchor links give keyboard and AT users a direct path back to each failing field.

## 9. Code Examples

### Example 1 — Error taxonomy demo (network / permission / not-found / validation)

```html
<main class="page">
  <article class="err" data-class="network">
    <h2>Connection problem</h2>
    <p>We couldn't load your projects. The network dropped mid-request.</p>
    <p class="fix">Check your connection, then retry.</p>
    <button type="button" class="btn" onclick="retry(this)">Retry</button>
  </article>
  <article class="err" data-class="permission">
    <h2>No access</h2>
    <p>You don't have permission to view this billing report.</p>
    <p class="fix">Ask a workspace admin for billing access.</p>
    <button type="button" class="btn" onclick="retry(this)">Request access</button>
  </article>
  <article class="err" data-class="not-found">
    <h2>Page not found</h2>
    <p>The project "acme-2025" was deleted or the link is outdated.</p>
    <p class="fix">Browse all projects instead.</p>
    <button type="button" class="btn" onclick="retry(this)">View projects</button>
  </article>
  <article class="err" data-class="validation">
    <h2>Check one field</h2>
    <p>We couldn't save the form. The email is missing an @.</p>
    <p class="fix">Use a format like name@domain.com.</p>
    <button type="button" class="btn" onclick="retry(this)">Fix email</button>
  </article>
</main>
<style>
  :root { --uxw-error-taxonomy: network,permission,not-found,validation; --uxw-error-recovery: retry-or-alternative; --color-danger: #b91c1c; }
  .page { font: 15px/1.5 system-ui, sans-serif; color: #171717; max-width: 460px; margin: 24px auto; }
  .err { border: 1px solid #e5e5e5; border-left: 4px solid var(--color-danger); border-radius: 8px; padding: 14px 16px; margin-bottom: 12px; }
  .err h2, .err p { margin: 0 0 4px; font-size: 15px; } .fix { color: var(--color-danger); font-weight: 500; }
  .btn { border: 1px solid #d4d4d4; background: #fff; border-radius: 6px; padding: 6px 14px; font: inherit; font-weight: 600; cursor: pointer; }
</style>
<script>
  const css = getComputedStyle(document.documentElement);
  console.assert(css.getPropertyValue('--uxw-error-taxonomy').split(',').length === 4, 'taxonomy token must ship all four classes');
  function retry(btn) {
    const card = btn.closest('.err');
    card.querySelector('h2').textContent = card.dataset.class === 'validation' ? 'Email looks valid now' : 'Retrying…';
  }
</script>
```

### Example 2 — Form submit failure: summary + focus + anchored inline errors

```html
<form id="signup" novalidate>
  <div id="summary" class="summary" hidden tabindex="-1" role="alert"></div>
  <label for="email">Email address</label>
  <input id="email" name="email" type="email" autocomplete="email" aria-describedby="email-err" />
  <p id="email-err" class="inline-err" hidden></p>
  <label for="phone">Phone number</label>
  <input id="phone" name="phone" type="tel" autocomplete="tel" aria-describedby="phone-err" />
  <p id="phone-err" class="inline-err" hidden></p>
  <button type="submit" class="btn-primary">Create account</button>
</form>
<style>
  :root { --uxw-error-position: inline-or-anchored-summary; --uxw-error-focus: summary-on-submit; --color-danger: #b91c1c; }
  body { font: 15px/1.5 system-ui, sans-serif; max-width: 380px; margin: 24px auto; }
  label { display: block; font-weight: 600; margin: 12px 0 4px; }
  input { width: 100%; box-sizing: border-box; padding: 8px 10px; border: 1px solid #d4d4d4; border-radius: 6px; font: inherit; }
  input[aria-invalid="true"] { border-color: var(--color-danger); }
  .inline-err { margin: 4px 0 0; color: var(--color-danger); font-size: 13px; }
  .summary { border: 1px solid var(--color-danger); border-radius: 8px; padding: 12px 14px; color: var(--color-danger); } .summary a { color: var(--color-danger); }
  .btn-primary { margin-top: 14px; background: #2563eb; color: #fff; border: none; border-radius: 6px; padding: 10px 18px; font: 600 14px system-ui, sans-serif; cursor: pointer; }
</style>
<script>
  const RULES = {
    email: { test: v => /.+@.+\..+/.test(v), msg: () => "The email is missing or malformed. Use a format like name@domain.com." },
    phone: { test: v => /^\+?[\d\s()-]{7,}$/.test(v), msg: () => "The phone number is too short. Include the country code, like +1 555 010 1234." }
  };
  const form = document.getElementById('signup'), summary = document.getElementById('summary');
  form.addEventListener('submit', e => {
    e.preventDefault();
    const failed = Object.entries(RULES).filter(([id, r]) => !r.test(document.getElementById(id).value));
    if (!failed.length) { summary.hidden = true; return; }
    summary.innerHTML = '<strong>We couldn\u2019t create your account. Fix ' + failed.length + ':</strong><ul>' +
      failed.map(([id]) => '<li><a href="#' + id + '">' + document.querySelector('label[for="' + id + '"]').textContent + '</a></li>').join('') + '</ul>';
    summary.hidden = false;
    failed.forEach(([id, r]) => {
      document.getElementById(id).setAttribute('aria-invalid', 'true');
      const err = document.getElementById(id + '-err');
      err.textContent = "We couldn't create your account yet. " + r.msg(); err.hidden = false;
    });
    summary.focus(); // --uxw-error-focus: failed submit focuses the error list
  });
</script>
```

## 10. Implementation Checklist

- [ ] Every shipped error passes the `--uxw-error-structure` contract: what + why + fix present in review.
- [ ] Phrasing is blame-free per `--uxw-error-blame` - no "you entered/made/failed" strings in the codebase.
- [ ] Validation copy includes a concrete example per `--uxw-error-fix-specificity` (e.g. name@domain.com).
- [ ] Error codes appear only inside a details expander per `--uxw-error-code-policy`, and error toasts persist per `--uxw-error-persistence` - no auto-dismissing error surfaces.
- [ ] Errors render inline or as an anchored summary per `--uxw-error-position`, with focus moved to the summary on failed submit per `--uxw-error-focus`.
- [ ] All four taxonomy classes (`--uxw-error-taxonomy`) have approved copy patterns; engineers pick, not invent.
- [ ] Invalid fields carry `aria-invalid` + `aria-describedby` per `--uxw-error-flag`, and every error offers a recovery action.

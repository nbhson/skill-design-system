---
name: button-labels
description: Verb-first, specific, outcome-visible button labels — what the action does, phrased in the user's terms, never 'OK', 'Submit', or 'Yes' on consequential actions.
tags: [ux-writing, buttons, microcopy, labels, actions]
related: [writing-principles, forms-labels, component-microcopy]
---

# UX Writing Guide: Button & Action Labels

## 1. Definition

Button labels are microcopy's highest-stakes surface: they are the moment of commitment. The discipline is verb-first phrasing ("Save changes", "Delete project"), specificity over abstraction (the vague "OK"/"Submit"/"Continue" family is banned from consequential actions), outcome visibility ("Send invitation" not "Send"), and consequence signaling for destructive actions ("Delete 3 files" with the count). Labels also carry the undo affordance decision: destructive-but-reversible actions label the action plainly, then offer "Undo" as a toast — moving reassurance from a confirmation dialog the user must parse into a recovery path they never need. A label is read in isolation by screen readers and under pressure by everyone else, so it must carry its meaning alone.

## 2. Core Principles

- **Verb first, always:** labels start with the verb — "Save changes", not "Changes" or "Saving".
- **Specific beats generic:** "Create project" not "OK"; the generic family (OK/Yes/Submit/Apply) is reserved for genuinely symmetric confirmations.
- **Name the outcome:** the label states what happens — "Send invitation", "Publish post", not "Send", not "Done".
- **Destructive labels carry the count:** "Delete 3 files", not "Delete" — the label itself is the confirmation surface.
- **Symmetric pairs read as a question:** dialog button pairs answer the title ("Discard draft?" → "Discard" / "Keep editing") — never "Yes/No" where the question requires re-reading.
- **Primary hierarchy is positional + labeled:** the primary action sits right (LTR), and its label is more specific than the secondary's.
- **Length budget: 2-4 words for actions:** longer labels become sentences — if it needs 6 words, the flow is wrong.
- **Loading/disabled copy is planned:** the loading state announces ("Saving..."), and disabled buttons explain the unlock condition nearby.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Label structure | `--uxw-label-structure` | `verb-first+specific` | The two-part label contract |
| Label length | `--uxw-label-length` | `2-4-words` | Longer labels signal flow problems |
| Banned generics | `--uxw-banned-generic` | `ok-yes-submit-for-consequential` | Generic labels only for symmetric confirms |
| Destructive labels | `--uxw-destructive-count` | `verb+count` | 'Delete 3 files' - label as confirmation |
| Pair symmetry | `--uxw-pair-symmetry` | `answer-the-title` | Dialog pairs respond to the question |
| Primary position | `--uxw-primary-position` | `right-ltr` | Primary action placement convention |
| Undo label | `--uxw-undo-label` | `undo+object` | Toast undo path for reversible actions |
| Loading copy | `--uxw-loading-announce` | `verb+ing-ellipsis` | 'Saving...' state copy planned |
| Disabled copy | `--uxw-disabled-explain` | `unlock-condition-visible` | Why disabled, near the button |
| Icon buttons | `--uxw-icon-button-name` | `aria-label-required` | Icon-only buttons named (a11y contract) |

Consume them by linking `assets/css/button-labels.css` at the app root and reading `var(--uxw-...)` values from the label spec sheet and button component docs — every shipped action string is checked against structure, length, and state-copy tokens at review and in lint. If a label cannot satisfy a token, the fix is usually upstream: a flow that needs a 6-word label is a flow to redesign, not a token to bend.

## 4. Composition

- **Composes with writing-principles (guide 01):** verb-first and plain language are inherited contracts — button labels are the densest application of the base rules, compressed into 2-4 words.
- **Composes with buttons-badges (skill-component-recipes):** the component recipe owns states, sizes, and visual hierarchy; this guide owns the string that lives inside it — neither layer ships without the other.
- **Composes with modals-dialogs (component-recipes confirmation-destructive flows):** label pairs must read against the dialog title — the pair test (title + buttons as one sentence) is executed where the modal recipe is implemented.

## 5. Signature Patterns

- **The label spec sheet:** every shipped action string listed with variant, state copy (loading/disabled), and undo pairing — a string inventory for actions. Buttons fail in their states, not their defaults; the sheet forces loading, disabled, and undo copy to be written before build, not improvised after.
- **The pair test:** for every two-button dialog, read title + buttons aloud as one sentence — "Discard draft? Discard / Keep editing" parses; "Discard draft? Yes / No" forces the user back to the title. If the sentence does not parse, rewrite the pair.

## 6. Real-World Use Cases

- **Any action surface: forms, toolbars, dialogs, cards, empty states** — wherever a click commits something, the label contract applies identically.
- **Design systems: the label conventions ship inside the button component docs** — so product teams inherit correct defaults instead of inventing them per feature.
- **Audit: OK/Submit sprawl, unnamed destructive buttons, Yes/No dialogs** — the three most common and cheapest-to-fix copy defects in any mature product.

## 7. Combination Notes

### With other ux-writing skills

- **Good with writing-principles, forms-labels, and component-microcopy:** writing-principles supplies the base grammar (verb-first, sentence case, plain language); forms-labels coordinates the submit button with the form's label style; component-microcopy handles the surrounding hints and tooltips so the button label never has to over-explain.
- **Good with error-messages, empty-states, onboarding-copy, and notifications:** each surface ends in an action — an error offers "Try again", an empty state offers "Create project", a toast offers "Undo" — and every one of those labels follows this guide's contract.
- **Good with voice-tone and accessible-writing:** tone sets how warm a label may be (never at clarity's expense on consequential actions); accessible-writing contributes the icon-button naming contract (`--uxw-icon-button-name`) and the read-in-isolation test.
- **Good with copy-audit and localization-i18n:** the audit enforces the spec sheet and flags banned generics automatically; localization benefits directly — specific, verb-first labels survive translation far better than "OK", which languages render inconsistently or verbatim.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** all three favor compact, functional action surfaces where a 2-4 word verb-first label is the natural visual unit — specificity and brevity are the typographic match for their economy.
- **Caution with collage-art:** collage styling may encourage decorative, evocative button text ("Do it", "Let's go"); where the style wants playfulness, confine it to low-stakes actions and keep consequential and destructive labels strictly specific.

### With motion skills (companion repo skill-animation)

- **Good affinity with micro-interactions and feedback-confirmation:** the planned loading state ("Saving...", per `--uxw-loading-announce`) is a motion contract as much as a copy one — the label change, spinner, and duration must be spec'd together so the label doesn't flicker or outlast the animation.
- **Good affinity with toasts and undo:** the toast undo path ("Item deleted / Undo") pairs the label with entrance/exit timing; motion should keep the toast readable long enough for the undo label to be acted on, especially with reduced-motion settings.

## 8. Anti-Patterns

- **The OK family** — 'OK' on a payment, 'Submit' on an adoption form - specificity is free
- **Yes/No labyrinths** — confirmations whose buttons force re-reading the title
- **Unlabeled destruction** — 'Delete' with no object and no count
- **Label sentences** — 9-word button labels that are really paragraph copy

### Accessibility Notes

Accessible names are WCAG 2.4.6/4.1.2 territory: labels describe purpose, icon-only buttons carry `aria-label`, and label text must survive being read in isolation — assistive technology users hear "button" + label without surrounding context, so "Discard" must mean something even when the dialog title it answers is not read first (in practice the accessible name of the dialog travels with it, but the label still cannot lean on visual context). This is also why the length budget exists alongside the specificity demand: a label that is specific within 2-4 words is narrated instantly; a paragraph-label becomes a listening chore. The fallback: if a label cannot be specific within the length budget, add the specificity to the dialog title or helper text instead — the pair (title + label) carries the meaning together, and the pair test confirms the combination parses aloud.

## 9. Code Examples

### Example 1 — Dialog with pair-symmetry labels and destructive count

Tokens: `assets/css/button-labels.css`

```html
<div class="dialog" role="alertdialog" aria-labelledby="dlg-title" aria-describedby="dlg-body">
  <h2 id="dlg-title">Delete 3 files?</h2>
  <p id="dlg-body">This permanently removes draft-v1.sketch, draft-v2.sketch, and assets.png.</p>
  <div class="actions">
    <button class="secondary">Keep files</button>
    <button class="danger">Delete 3 files</button>
  </div>
</div>
<style>
  .dialog { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 380px; border: 1px solid #E5E5E5; border-radius: 8px; padding: 16px; }
  .dialog h2 { margin: 0 0 6px; font-size: 16px; }          /* pair test: "Delete 3 files? Delete 3 files / Keep files" */
  .dialog p { margin: 0 0 16px; color: #525252; }
  .actions { display: flex; justify-content: flex-end; gap: 8px; }
  .actions button { padding: 8px 16px; border-radius: 6px; font-weight: 600; cursor: pointer; }
  .secondary { background: transparent; border: 1px solid #D4D4D4; color: #171717; }
  .danger    { background: #DC2626; border: none; color: #fff; }  /* destructive carries the count */
  /* Primary sits right (LTR) per --uxw-primary-position */
</style>
```

### Example 2 — Button state machine with planned state copy and toast undo

Tokens: `assets/css/button-labels.css`

```html
<div class="demo">
  <button id="save" class="primary">Save changes</button>
  <p id="unlock" class="unlock" hidden>Enable saving: add a project name above.</p>
  <div id="toast" class="toast" role="status" hidden>
    <span>Changes discarded</span>
    <button id="undo" class="undo">Undo discard</button>
  </div>
</div>
<script>
  const btn = document.getElementById('save');
  const unlock = document.getElementById('unlock');
  const toast = document.getElementById('toast');
  btn.addEventListener('click', () => {
    btn.disabled = true;
    btn.textContent = 'Saving...';                 // --uxw-loading-announce: verb+ing-ellipsis
    setTimeout(() => {
      btn.disabled = false;
      btn.textContent = 'Save changes';
      toast.hidden = false;                        // --uxw-undo-label: undo+object
      setTimeout(() => { toast.hidden = true; }, 5000);
    }, 1200);
  });
  // Disabled buttons explain the unlock condition nearby (--uxw-disabled-explain)
  btn.dataset.blocked = 'true';
  btn.disabled = true;
  unlock.hidden = false;
</script>
<style>
  .demo { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 360px; }
  .primary { padding: 10px 20px; border: none; border-radius: 6px; background: #171717; color: #fff; font-weight: 600; cursor: pointer; }
  .primary:disabled { background: #A3A3A3; cursor: not-allowed; }
  .primary:focus-visible { outline: 2px solid #171717; outline-offset: 2px; }
  .unlock { color: #525252; margin: 8px 0 0; }
  .toast { display: flex; align-items: center; justify-content: space-between; gap: 16px; margin-top: 12px; padding: 10px 14px; background: #171717; color: #fff; border-radius: 6px; }
  .undo { background: transparent; border: none; color: #fff; text-decoration: underline; cursor: pointer; font-weight: 600; }
</style>
```

## 10. Implementation Checklist

- [ ] Every action label is verb-first and specific per `--uxw-label-structure` — zero OK/Submit/Yes on consequential actions (`--uxw-banned-generic`).
- [ ] All labels fit the 2-4 word budget (`--uxw-label-length`); any 6+ word label triggers a flow review, not a longer string.
- [ ] Destructive buttons carry the count per `--uxw-destructive-count` ("Delete 3 files"), and reversible ones ship a toast undo per `--uxw-undo-label`.
- [ ] Every two-button dialog passes the pair test: title + buttons read aloud as one sentence (`--uxw-pair-symmetry`).
- [ ] Primary actions sit right in LTR layouts (`--uxw-primary-position`) with a more specific label than the secondary.
- [ ] Loading and disabled copy is planned before build: "Saving..." per `--uxw-loading-announce`, unlock conditions visible per `--uxw-disabled-explain`.
- [ ] Icon-only buttons carry `aria-label` per `--uxw-icon-button-name`; no name depends on hover.
- [ ] The label spec sheet lists every shipped action string with variant, state copy, and undo pairing — audited by copy-audit.

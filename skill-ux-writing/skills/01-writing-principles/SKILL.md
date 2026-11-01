---
name: writing-principles
description: The foundation of UX writing — clarity-first, user-first, plain language, active voice, and brevity, the rules every other copy discipline inherits.
tags: [ux-writing, plain-language, active-voice, clarity, voice]
related: [voice-tone, button-labels, error-messages]
---

# UX Writing Guide: Writing Principles

## 1. Definition

Interface writing has one job: help users act with confidence. The foundational principles are clarity before cleverness, the user's words before the system's, brevity before completeness, and verbs before nouns. Every other guide in this repo — errors, empties, forms, notifications — inherits these rules; this guide is the constitution the rest cite. Where later guides add craft (tone matrices, taxonomies, state copy), they must never contradict this layer: a witty error that fails clarity, a short label that drops the fix, or a jargon term that replaces the user's word violates this constitution no matter how well it executes its own guide.

## 2. Core Principles

- **Clarity beats cleverness:** a joke that confuses is a bug; if a line can be misread, rewrite it.
- **User-first ordering:** lead with what the user can do, not what the system did — "Save your draft" not "Draft saved to server".
- **Active voice, present tense:** "We couldn't process your card" not "Your card could not be processed by the system".
- **Brevity with a floor:** cut every wasted word, but never cut the why or the fix — short and complete beats short and hollow.
- **Plain language is for everyone:** 8th-grade reading level is a target, not a concession — experts skim, novices depend on it.
- **Sentence case everywhere:** "Save changes" not "Save Changes" — capitalization is not emphasis.
- **One idea per sentence, one action per paragraph:** interface copy is scanned in foveal gulps, not read linearly.
- **Consistency is grammar:** one concept, one term — "workspace" everywhere, never "workspace/team/project/site" interchangeably.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Reading level | `--uxw-reading-level-target` | `grade-8` | Plain-language floor for all UI copy |
| Case | `--uxw-voice-case` | `sentence-case` | Titles, buttons, labels - no title case |
| Person | `--uxw-voice-person` | `second-person-active` | Address the user as 'you'; active voice |
| Line budget | `--uxw-line-max` | `2-lines` | Body copy in UI rarely earns a third line |
| Button structure | `--uxw-button-verb-first` | `verb+object` | 'Save changes', not 'Changes will be saved' |
| Error structure | `--uxw-error-structure` | `what+why+fix` | The three-part message contract |
| Jargon policy | `--uxw-no-jargon-rule` | `banned-unless-domain` | System terms translated to user terms |
| Terminology | `--uxw-terminology-single-source` | `glossary-owned` | copy-audit guide owns the glossary |
| Numbers | `--uxw-numbers-format` | `digits-in-ui` | '3 files' not 'three files' in interfaces |
| Punctuation | `--uxw-punctuation-policy` | `minimal` | No periods on buttons/labels; full sentences keep periods |

Consume them by linking `assets/css/writing-principles.css` once at the app root, then reading `var(--uxw-...)` values from the copy spec, lint rules, and component docs — strings are checked against these tokens the way colors are checked against contrast maps. If a proposed string cannot satisfy a token (a 3-line explanation, a title-case heading, a spelled-out number), the string is rewritten or the token is amended through review; components never silently fork the policy.

## 4. Composition

- **Composes with accessible-writing (guide 11):** plain language and reading level are shared contracts — this guide sets the target (grade-8, second person, active voice) and that guide operationalizes it for assistive technology, so a string that passes lint but fails AT narration is still unfinished.
- **Composes with copy-audit (guide 12):** the glossary and lint rules are the enforcement arm — these principles stay aspirational until the audit flags term drift, title case, and system-voice strings automatically.
- **Composes with component-recipes (skill-component-recipes):** every component's copy slots (labels, errors, empties, hints) inherit these rules by default; a recipe that ships a placeholder-as-label or a title-case button contradicts this layer and gets rejected in review.

## 5. Signature Patterns

- **The voice charter:** one page documenting person, tense, case, and tone range — reviewed with brand once, then cited in every copy PR so debates end by pointing at the charter instead of relitigating taste.
- **The rewrite ladder:** for any string, test system-voice → user-voice → shorter → plainest; each pass removes a specific failure mode (distance, passivity, waste, jargon), and the first pass that satisfies the tokens wins.

## 6. Real-World Use Cases

- **New products establishing their writing voice from zero** — the charter and tokens give day-one writers a complete default instead of a blank page.
- **Teams with inconsistent copy across surfaces** (the usual state) — a single glossary plus lint rules converges four screens calling the same object four names.
- **Onboarding writers and engineers to a shared copy standard** — the principles are short enough to internalize in one read and strict enough to settle review arguments.

## 7. Combination Notes

### With other ux-writing skills

- **Pairs with everything — and that is the point:** button-labels, error-messages, empty-states, onboarding-copy, component-microcopy, forms-labels, and notifications all quote these rules rather than redefining them; a guide-level contradiction with this file is treated as a bug in the guide.
- **Pairs with voice-tone:** this guide defines the voice's baseline (plain, active, user-first); voice-tone defines how personality flexes within that baseline — tone never overrides clarity.
- **Pairs with accessible-writing and copy-audit:** the reading-level target and glossary are the two contracts this guide hands off for operationalization — one for AT users, one for scale.
- **Pairs with localization-i18n with caution toward expansion:** plain, short, verb-first strings translate best; the guide's brevity floor exists partly to keep strings translatable.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** all three favor restrained, functional surfaces where copy carries meaning without decoration — sentence case, short lines, and plain words are the textual equivalent of their visual economy.
- **Caution with maximalism:** maximalist visuals invite exuberant copy, but this guide's floor (clarity, brevity, one idea per sentence) still applies; express maximalism through layout and color, and keep the strings inside the tokens.

### With motion skills (companion repo skill-animation)

- **Good affinity with micro-interactions and feedback-confirmation:** short, active copy pairs naturally with quick confirmatory motion — "Saved" plus a 150ms fade is one composite feedback unit; copy and motion should be specced together so neither compensates for the other's weakness.

## 8. Anti-Patterns

- **System-voice strings** — 'An error has occurred in module X' - the user is the subject, not the server
- **Cleverness first** — puns and jokes in error paths that confuse under stress
- **Capitalization-as-emphasis** — SHOUTING LABELS and Title Case Everything
- **Term drift** — the same object called four names across four screens

### Accessibility Notes

Plain language is WCAG 3.1.5 (reading level) territory: an 8th-grade target, abbreviations expanded on first use, and meaning carried by words — not by case, punctuation, or decoration (the a11y repo's cognitive-content guide says the same). This is why the tokens fix case, person, and reading level rather than leaving them to style: screen reader users hear strings in isolation, and cognitive load is a real accessibility constraint, not a nicety. The fallback is explicit: if a legal or domain string cannot reach grade-8 (a compliance disclosure, a medical term), pair it with a plain-language summary beside it — the summary carries comprehension, the original carries precision, and neither pretends to do the other's job.

## 9. Code Examples

### Example 1 — Before/after rewrite ladder rendered as HTML

Tokens: `assets/css/writing-principles.css`

```html
<table class="rewrites">
  <caption>System voice vs user voice — the first two ladder passes</caption>
  <thead>
    <tr><th scope="col">Before (system voice)</th><th scope="col">After (user voice)</th></tr>
  </thead>
  <tbody>
    <tr><td>Draft saved to server.</td><td>Save your draft</td></tr>
    <tr><td>Your card could not be processed by the system.</td><td>We couldn't process your card. Check the number or try another card.</td></tr>
    <tr><td>3 files have been removed from the repository.</td><td>You deleted 3 files</td></tr>
  </tbody>
</table>
<style>
  .rewrites {
    font: 14px/1.5 Inter, system-ui, sans-serif;
    border-collapse: collapse;
    max-width: 560px;
  }
  .rewrites th, .rewrites td {
    text-align: left;
    padding: 8px 12px;
    border-bottom: 1px solid #E5E5E5;
  }
  .rewrites caption { font-weight: 600; text-align: left; padding-bottom: 8px; }
  /* Sentence case, 2-line budget, minimal punctuation — per --uxw-voice-case and --uxw-line-max */
</style>
```

### Example 2 — Settings panel copy following every principle

Tokens: `assets/css/writing-principles.css`

```html
<section class="settings" aria-labelledby="settings-title">
  <h2 id="settings-title">Notification settings</h2>
  <p class="hint">Choose what we email you about.</p>
  <div class="row">
    <label for="digest">Email me a weekly digest</label>
    <button id="digest" class="toggle" role="switch" aria-checked="true">On</button>
  </div>
  <div class="row">
    <label for="mentions">Email me when someone mentions you</label>
    <button id="mentions" class="toggle" role="switch" aria-checked="false">Off</button>
  </div>
  <p class="note">You have 3 unread mentions.</p>
  <button class="primary">Save changes</button>
</section>
<style>
  .settings {
    font: 14px/1.5 Inter, system-ui, sans-serif;
    max-width: 420px;
    padding: 16px;
    border: 1px solid #E5E5E5;
    border-radius: 8px;
  }
  .settings h2 { font-size: 16px; margin: 0 0 4px; }         /* sentence case, not title case */
  .hint { margin: 0 0 12px; color: #525252; }                 /* persistent hint, 1 line */
  .row { display: flex; justify-content: space-between; align-items: center; gap: 16px; margin-bottom: 8px; }
  .toggle { min-width: 48px; padding: 4px 12px; border-radius: 999px; border: 1px solid #D4D4D4; background: #F5F5F5; cursor: pointer; }
  .toggle[aria-checked="true"] { background: #171717; color: #fff; border-color: #171717; }
  .note { color: #525252; }                                   /* digits: '3 unread mentions' */
  .primary { margin-top: 12px; padding: 8px 16px; border: none; border-radius: 6px; background: #171717; color: #fff; font-weight: 600; cursor: pointer; }
</style>
<script>
  for (const t of document.querySelectorAll('.toggle')) {
    t.addEventListener('click', () => {
      t.setAttribute('aria-checked', t.getAttribute('aria-checked') !== 'true');
      t.textContent = t.getAttribute('aria-checked') === 'true' ? 'On' : 'Off';
    });
  }
</script>
```

## 10. Implementation Checklist

- [ ] Every UI string passes the grade-8 reading-level floor enforced by `--uxw-reading-level-target`; legal strings get plain-language summaries beside them.
- [ ] All titles, buttons, and labels use sentence case per `--uxw-voice-case` — zero title-case strings in shipped UI.
- [ ] Body copy stays within the `--uxw-line-max` budget (2 lines) or is restructured into scannable chunks.
- [ ] Every error and confirmation string follows the `--uxw-error-structure` contract: what + why + fix.
- [ ] Buttons are verb+object per `--uxw-button-verb-first`, with no periods per `--uxw-punctuation-policy`.
- [ ] Numbers render as digits per `--uxw-numbers-format` ('3 files', not 'three files').
- [ ] The glossary owns terminology per `--uxw-terminology-single-source`; the copy-audit lint fails on term drift.
- [ ] The voice charter is published, versioned, and cited in copy PRs; new strings are linted before merge.

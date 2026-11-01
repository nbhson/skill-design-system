---
name: cognitive-content
description: Plain language, predictable behavior, helpful errors, and memory-friendly flows - WCAG 3.x for users with cognitive and learning disabilities.
tags: [cognitive, plain-language, predictability, error-recovery, wcag]
related: [forms-errors, zoom-reflow, testing-audit]
---

# Accessibility Skill: Cognitive & Content Accessibility

## 1. Definition

Cognitive accessibility is the least-automated and most-human layer: plain language, consistent navigation, predictable interactions, generous timing, and error recovery that does not punish. It serves users with learning disabilities, ADHD, memory limitations, and situational stress (rushing, multitasking) - which is to say, effectively everyone. Most of it maps to WCAG 3.x Understandable criteria plus emerging COGA guidance, and unlike contrast or keyboard checks it cannot be reduced to a computed ratio: every criterion here needs a human judgment call, which is why it lives in design-review checklists and scripted walkthroughs rather than linters. The payoff is universal - plain language, saved progress, and undoable actions measurably improve completion rates for every user, not only those with diagnosed disabilities.

## 2. Core Principles

- **Plain language is the default:** short sentences, common words, one idea per paragraph; define terms on first use.
- **Reading level matters:** aim for lower-secondary reading level on task-critical content (WCAG 3.1.5 AAA where feasible).
- **Consistency is navigation:** same actions, same order, same location across screens (WCAG 3.2.3) - surprises cost cognition.
- **No context change on focus or input:** focus does not trigger navigation; inputs do not auto-submit (WCAG 3.2.1/3.2.2).
- **Help before error, recovery after:** input assistance (3.3.x), undo for irreversible actions, and no session timeouts without warning and extension (2.2.1).
- **Instructions survive memory limits:** steps visible while needed, progress saved, no reliance on remembering across pages.
- **Chunk and structure:** headings, lists, and progress indicators break complex tasks into oriented steps.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Plain language | `--a11y-plain-language-target` | `grade-8` | Lower-secondary reading level for task content |
| Sentence length | `--a11y-sentence-length-guide` | `under-25-words` | One idea per sentence; paragraphs 2-4 sentences |
| Consistency | `--a11y-consistency-policy` | `same-place-same-action` | WCAG 3.2.3 consistent navigation/help placement |
| Focus change | `--a11y-focus-change-policy` | `no-navigation` | WCAG 3.2.1: focus never triggers context change |
| Input change | `--a11y-input-change-policy` | `confirm-or-undo` | WCAG 3.2.2: no auto-submit surprises |
| Timeout | `--a11y-timeout-policy` | `warn-and-extend` | WCAG 2.2.1: 20s+ warning, extension, no data loss |
| Undo | `--a11y-undo-policy` | `irreversible-only` | Destructive actions get undo or explicit confirm |
| Error recovery | `--a11y-error-recovery` | `suggest-fix` | 3.3.3-3.3.6: suggestions, review-before-submit, no re-entry |
| Chunking | `--a11y-chunking-pattern` | `steps-with-progress` | Multi-step flows show position + completion |
| Help | `--a11y-help-availability` | `persistent-location` | WCAG 3.2.6 (2.2): help entry point in a consistent place |

These are policy tokens: they are declared once in `assets/css/cognitive-content.css`, documented beside the token set, and referenced wherever a flow makes a cognitive-affecting decision - `var(--a11y-timeout-policy)` in the session manager, `var(--a11y-chunking-pattern)` in the wizard component, `var(--a11y-undo-policy)` in destructive-action review. A flow that needs a different policy changes the token through governance, never inline.

## 4. Composition

- **Composes with forms-errors:** forgiving validation timing and suggested fixes are cognitive accessibility applied to forms - the two skills share the error-summary and review-before-submit mechanics.
- **Composes with ux-writing (skill-ux-writing):** plain language, button labels, and error phrasing are the writing-side execution of this skill; the token thresholds here are that craft's acceptance criteria.
- **Composes with skill-animation:** reduced-motion and pauseable ambient motion serve cognitive load as much as vestibular safety - a distracting page is an unreadable page.

## 5. Signature Patterns

- **Stepwise flows with save-and-resume:** wizards persist progress and show position - memory-friendly by architecture. The user can leave, come back tomorrow, and find step 3 of 5 exactly as they left it; nothing depends on remembering across pages.
- **Undo-first destructiveness:** 'Archive' with undo replaces confirm dialogs for low-stakes deletions; explicit confirm only for the irreversible. This inverts the default: protection becomes a forgiving recovery path instead of an interrogation gate.

## 6. Real-World Use Cases

- **Government, health, and financial products** where comprehension failures have real consequences.
- **Onboarding and multi-step wizards** for any audience under stress or time pressure.
- **Audit:** reading-level scan, consistency review, timeout and error-recovery walkthrough.

## 7. Combination Notes

### With other accessibility skills

- **Good with forms-errors:** form validation timing, error phrasing, and input preservation are this skill's criteria expressed on the highest-stakes surface; fixing one fixes both.
- **Good with keyboard-navigation and focus-management:** predictable focus behavior is cognitive accessibility - focus that jumps or triggers navigation (WCAG 3.2.1) disorients twice over.
- **Good with screen-readers and media-alt-text:** plain language and chunking determine whether narration is comprehensible, not just technically correct.
- **Good with zoom-reflow and testing-audit:** reflow walkthroughs and audit checklists include the reading-level and timeout items defined here.
- **Caution/avoid: none.** Cognitive accessibility has no incompatible partners - every other skill's output is content a stressed reader must eventually parse.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** both reduce visual noise and decoration, leaving fewer distractors competing for limited attention - the closest stylistic match to a low-cognitive-load page.
- **Caution with collage-art and maximalism:** dense, layered, high-novelty layouts raise scanning cost and break the same-place-same-action consistency policy. If a brand demands them, contain the density to marketing surfaces and keep task-critical flows conventional.

### With motion skills (companion repo skill-animation)

- **Good affinity with reduced-motion:** animation that respects the reduced-motion preference also lowers cognitive load; both aim at attention as a finite resource.
- **Caution with ambient-motion:** background loops, parallax, and auto-playing movement continuously consume attention and break reading flow. Any ambient motion must be pauseable and off by default on task-critical pages.

## 8. Anti-Patterns

- **Legalese defaults** — dense jargon on task-critical content because 'the lawyers wrote it'
- **Surprise auto-submit** — select changes that fire navigation without confirmation
- **Punishing timeouts** — session expiry wiping forms with no warning or extension
- **Confirm-dialog everything** — modal fatigue that trains users to click through the one dialog that mattered

### Accessibility Notes

Cognitive accessibility is the largest underserved group and the hardest to automate: every criterion here needs human review, which is why it lives in the design-review checklists of sibling repos rather than in axe or Lighthouse. Reading level, consistency, and timeout behavior are judged by walkthrough, and the findings feed the same audit report as computed violations. The fallback is layered content: when formal criteria conflict with content constraints (a legal text, a regulated disclosure), ship the plain-language summary alongside the original - layered content serves both audiences without hiding the source, and `var(--a11y-error-recovery)` still governs what happens when the user gets it wrong.

## 9. Code Examples

### Example 1 — Save-and-resume wizard step with progress

Tokens: `assets/css/cognitive-content.css`

```html
<main>
  <ol class="steps" aria-label="Application progress">
    <li aria-current="step">1. Personal details</li>
    <li>2. Income</li>
    <li>3. Review &amp; submit</li>
  </ol>
  <p id="resume-note" class="resume-note">Progress is saved automatically. Leave anytime - we will bring you back here.</p>
  <form class="wizard-step">
    <label for="city">City you live in</label>
    <input id="city" name="city" type="text" autocomplete="address-level2">
    <button type="submit" class="btn">Save and continue</button>
  </form>
</main>
<script>
  // WCAG 2.2.1 (--a11y-timeout-policy: warn-and-extend): never expire silently
  const saved = localStorage.getItem('wizard.city');
  if (saved) document.getElementById('city').value = saved; // resume exactly where the user left off
  document.querySelector('.wizard-step').addEventListener('submit', (e) => {
    e.preventDefault();
    localStorage.setItem('wizard.city', document.getElementById('city').value);
    location.href = '/step-2';
  });
</script>
<style>
  .steps { display: flex; gap: 16px; padding: 0; list-style: none; font: 600 14px/1.4 system-ui, sans-serif; }
  .steps [aria-current="step"] { text-decoration: underline; } /* position + completion (--a11y-chunking-pattern) */
  .resume-note { font: 14px/1.5 system-ui, sans-serif; }
  .wizard-step label { display: block; margin-bottom: 4px; font: 600 14px/1.4 system-ui, sans-serif; }
  .wizard-step input { padding: 10px; min-height: 44px; border: 1px solid gray; border-radius: 8px; }
  .btn { padding: 10px 20px; min-height: 44px; border: none; border-radius: 8px; background: #1D4ED8; color: #fff; font: 600 14px/1 system-ui, sans-serif; cursor: pointer; }
</style>
```

### Example 2 — Destructive action with undo instead of a confirm dialog

Tokens: `assets/css/cognitive-content.css`

```html
<div class="row">
  <span id="item-name">Q3 expense report.pdf</span>
  <button class="btn btn-quiet" id="archive-btn">Archive</button>
</div>
<div id="undo" class="undo" role="status" hidden>
  Archived. <button class="btn-link" id="undo-btn">Undo</button>
</div>
<script>
  const item = document.getElementById('item-name');
  const undoBar = document.getElementById('undo');
  // --a11y-undo-policy (irreversible-only): low-stakes delete gets undo, not a modal
  document.getElementById('archive-btn').addEventListener('click', () => {
    item.parentElement.hidden = true;
    undoBar.hidden = false; // polite live region announces "Archived." via role=status
  });
  document.getElementById('undo-btn').addEventListener('click', () => {
    undoBar.hidden = true;
    item.parentElement.hidden = false;
  });
</script>
<style>
  .row { display: flex; align-items: center; gap: 12px; font: 14px/1.5 system-ui, sans-serif; }
  .btn { padding: 8px 16px; min-height: 44px; border: none; border-radius: 8px; background: #1D4ED8; color: #fff; font: 600 14px/1 system-ui, sans-serif; cursor: pointer; }
  .btn-quiet { background: transparent; color: #1D4ED8; border: 1px solid #1D4ED8; }
  .btn-link { background: none; border: none; color: #1D4ED8; text-decoration: underline; font: inherit; cursor: pointer; }
  .undo { margin-top: 8px; padding: 8px 12px; border-radius: 8px; background: #F5F5F5; font: 14px/1.5 system-ui, sans-serif; }
</style>
```

## 10. Implementation Checklist

- [ ] Task-critical content passes a grade-8 reading-level check, per `--a11y-plain-language-target`.
- [ ] Sentences stay under 25 words and paragraphs at 2-4 sentences, per `--a11y-sentence-length-guide`.
- [ ] No select/input change auto-submits or navigates without confirmation or undo (`--a11y-input-change-policy`).
- [ ] Multi-step flows persist progress and show position (step N of M) per `--a11y-chunking-pattern`.
- [ ] Session timeouts warn 20+ seconds ahead, offer extension, and lose no data (`--a11y-timeout-policy`).
- [ ] Destructive actions ship undo or an explicit confirm, never both as a habit (`--a11y-undo-policy`).
- [ ] Error messages state the cause and the fix (`--a11y-error-recovery: suggest-fix`).
- [ ] Help sits in one persistent, consistent location on every screen (`--a11y-help-availability`).

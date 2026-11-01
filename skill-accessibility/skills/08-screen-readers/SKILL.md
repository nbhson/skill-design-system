---
name: screen-readers
description: Testing with NVDA, JAWS, and VoiceOver - the pairing matrix, listening scripts, and what automated checks can never catch.
tags: [screen-readers, testing, nvda, voiceover, wcag]
related: [aria-fundamentals, forms-errors, testing-audit]
---

# Accessibility Skill: Screen Reader Testing

## 1. Definition

Automated accessibility testing catches roughly 30-40% of issues; the rest only surface when a human listens. Screen reader testing validates the actual experience: does the page make sense in reading order, do widgets narrate correctly, can a user complete the task by ear. This skill covers the platform/reader pairing matrix, core keystrokes, and repeatable listening scripts that turn 'it feels fine' into evidence - because a page can pass every automated rule and still be unusable the moment someone navigates it non-linearly, the way screen reader users actually browse.

## 2. Core Principles

- **Test the supported matrix:** NVDA+Firefox/Chrome (Windows), JAWS+Chrome (enterprise), VoiceOver+Safari (macOS/iOS), TalkBack+Chrome (Android).
- **Automated checks are the floor, not the verdict:** axe finds missing alt; only listening finds nonsense reading order and unnamed controls in context.
- **Navigate as users do:** by headings (H), landmarks (D), forms (F), and links (K) - linear Tab-walking is not how screen reader users browse.
- **Reading order is semantic order:** visual layout must not diverge from DOM order or narration becomes nonsense.
- **Widgets get full-flow scripts:** open, navigate, select, close - every APG pattern has a listening script (aria-patterns-widgets).
- **Test both browse and focus modes:** NVDA browse vs focus mode behaves differently - virtual cursor confusion is a real finding.
- **Record findings as tasks:** quote the narration, name the reader, note the keystroke - 'NVDA reads button twice on focus' is an actionable bug.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Reader matrix | `--a11y-reader-matrix` | `nvda,jaws,voiceover,talkback` | Supported pairing matrix; each release tests core flows |
| NVDA pairing | `--a11y-nvda-pairing` | `firefox-chrome` | Primary Windows open-source pairing |
| VoiceOver pairing | `--a11y-voiceover-pairing` | `safari-macos-ios` | Apple platforms; rotor navigation |
| JAWS pairing | `--a11y-jaws-pairing` | `chrome` | Enterprise Windows; strictest HTML expectations |
| TalkBack pairing | `--a11y-talkback-pairing` | `chrome-android` | Android touch exploration |
| Nav by headings | `--a11y-nav-by-headings` | `h-key` | Heading structure is the primary page map |
| Nav by landmarks | `--a11y-nav-by-landmarks` | `d-key` | Landmarks skeleton must be complete |
| Core flow script | `--a11y-core-flow-script` | `per-feature` | Signup/checkout/search listening scripts in the test plan |
| Auto coverage ceiling | `--a11y-auto-coverage-ceiling` | `40%` | What axe-class tools can catch; listening covers the rest |
| Finding format | `--a11y-finding-format` | `reader+keystroke+quote` | Bugs cite narration verbatim for reproducibility |

Consume them by linking `assets/css/screen-readers.css` at the app root of the testing harness (not the product UI): the matrix tokens drive which pairings a release gate runs, and utilities such as the test-plan page template read `var(--a11y-reader-matrix)` and `var(--a11y-finding-format)` to render checklists and bug-report stubs in the canonical format. A team that tests ad hoc pairings instead of reading these tokens discovers reader-specific breakage in production, not in the gate.

## 4. Composition

- **Composes with aria-fundamentals and aria-patterns-widgets:** those skills write the markup - roles, states, and APG keymaps; this one listens to the result and files what breaks, closing the loop between authoring and verification.
- **Composes with testing-audit:** screen reader passes are a required lane in the audit framework, with the listening scripts stored in the test plan alongside CI results, so release evidence includes what ears heard, not just what linters said.
- **Composes with forms-errors and focus-management:** listening verifies error announcements and focus landings that automation cannot judge - whether the summary read naturally, whether focus landed somewhere meaningful, whether the polite live region fired at all.

## 5. Signature Patterns

- **Listening scripts per core flow:** each critical user journey (signup, checkout, search) has a numbered script - open page, heading nav, complete task, step by step, with expected narration written in advance - run per reader before release; improvisation is not a test plan.
- **Narration quotes as acceptance criteria:** bugs and fixes cite the exact spoken output ('NVDA announces "button button" on focus'), so regressions are measurable and a fix is verifiable by re-running the same keystroke and comparing quotes.

## 6. Real-World Use Cases

- **Pre-release validation of core flows** on the supported reader matrix, before a release is allowed to ship.
- **Verifying custom widgets** (tabs, combobox, dialog) narrate per the APG pattern they claim to implement.
- **Triage:** converting vague 'a11y feels broken' reports into quoted narration bugs anyone can reproduce.

## 7. Combination Notes

### With other accessibility skills

- **Pairs naturally with aria-fundamentals and aria-patterns-widgets:** ARIA is only half the contract - markup declares intent, and listening verifies delivery; a pattern library without a listening script is a claim without evidence.
- **Pairs with forms-errors and focus-management:** error summaries, aria-invalid announcements, and focus landings are exactly the behaviors automated tools cannot judge; these skills define what should happen, this skill confirms it did.
- **Pairs with keyboard-navigation:** both are manual passes, and the keystrokes overlap - a keyboard walkthrough doubles as the focus-mode half of the listening script.
- **Pairs with media-alt-text and cognitive-content:** listening is how you hear that alt text reads sensibly in context and that content order makes narrative sense.
- **Caution: none, avoid: none.** Every sibling skill produces something that must ultimately be verified by ear; nothing about this skill conflicts with another - it is the verification layer for the entire graph.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** lean DOMs with clear landmarks and a tight heading hierarchy narrate cleanly and make listening scripts short and deterministic; the styles' restraint in decorative elements keeps narration noise low.
- **Caution with collage-art and maximalism:** layered, overlapping, decorative-heavy layouts produce narration order that diverges from what eyes see and flood the soundscape with aria-hidden'd decoration; if these styles are used, listening scripts must pay special attention to reading order and decorative suppression.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** predictable, token-driven transition durations keep narration timing stable - elements that fade in too slowly can be announced before they are visible, or intercept focus mid-transition; consistent easing keeps the ear and the eye synchronized.
- **Caution with ambient-motion:** continuously animating surfaces generate repeated live-region or visibility changes that interleave with narration; ambient effects near announced content need reduced-motion fallbacks per the companion repo's guidance.

## 8. Anti-Patterns

- **Axe-and-done** — zero automated violations claimed as 'accessible' while flows fail by ear
- **Tab-only testing** — walking links linearly and calling it screen reader testing
- **One-reader release gates** — NVDA passing on Windows tells nothing about iOS VoiceOver
- **Vague bug reports** — 'screen reader is confusing' findings nobody can reproduce or fix

### Accessibility Notes

Screen reader testing is the reality check for WCAG 4.1.2/4.1.3 and the whole robustness principle: if it does not work by ear, it does not work - the screen reader experience is not an alternative rendering, it is the only rendering for a substantial group of users. The tokens here encode the discipline as contracts: `--a11y-reader-matrix` fixes which pairings count as tested, `--a11y-core-flow-script` requires every critical journey to have a numbered script, and `--a11y-finding-format` (`reader+keystroke+quote`) makes findings reproducible by construction. The fallback rule: if a flow fails by ear and the fix needs time, ship the documented workaround (native control, simplified view) in the interim - never block the whole flow while waiting for the polished fix.

## 9. Code Examples

### Example 1 — Listening-script test plan template (checkout flow, NVDA pass)

Tokens: `assets/css/screen-readers.css`

```html
<article class="script">
  <h2>Listening script — Checkout, NVDA + Firefox</h2>
  <p>Pairing token: <code>var(--a11y-nvda-pairing)</code> · Finding format:
     <code>var(--a11y-finding-format)</code></p>
  <ol class="steps">
    <li>
      Open /checkout. Press <kbd>H</kbd> repeatedly.
      <em>Expected:</em> "Checkout, heading level 1" → "Shipping address, heading level 2" → "Payment, heading level 2".
    </li>
    <li>
      Press <kbd>D</kbd> to cycle landmarks.
      <em>Expected:</em> "banner landmark" → "main landmark" → "contentinfo landmark"; exactly one main.
    </li>
    <li>
      Press <kbd>F</kbd> to reach the first field.
      <em>Expected:</em> "Email, edit, required, blank" — label, state, and hint read in one stop.
    </li>
    <li>
      Leave email empty, press the Submit button (<kbd>B</kbd> then <kbd>Enter</kbd>).
      <em>Expected:</em> focus lands on the error summary; NVDA reads "2 answers need fixing" followed by linked items.
    </li>
    <li>
      Fix the fields and submit. <em>Expected:</em> polite announcement "Order placed. Confirmation sent." — no focus steal.
    </li>
  </ol>
  <p><label><input type="checkbox" /> Pass on <code>nvda,jaws,voiceover,talkback</code> matrix — record narration quotes for any deviation.</label></p>
</article>
<style>
  .script { max-width: 640px; font: 14px/1.6 system-ui, sans-serif; color: #171717; }
  .steps  { padding-left: 20px; }
  .steps li { margin-bottom: 12px; }
  .steps em { color: #404040; }
  kbd { background: #F5F5F5; border: 1px solid #D4D4D4; border-radius: 4px;
        padding: 1px 6px; font: 600 12px ui-monospace, monospace; }
  code { background: #F5F5F5; padding: 1px 4px; border-radius: 4px; }
</style>
```

### Example 2 — Live-region status demo (polite save confirmation)

Tokens: `assets/css/screen-readers.css`

```html
<main>
  <h1>Notification preferences</h1>
  <button id="save" type="button">Save preferences</button>
  <p id="status" role="status" aria-live="polite"></p>
</main>
<script>
  // The live region exists in the DOM BEFORE content changes —
  // a region injected at save time announces nothing (aria-fundamentals).
  const status = document.getElementById('status');
  document.getElementById('save').addEventListener('click', async () => {
    status.textContent = 'Saving…';                       // heard immediately, politely
    await persist();
    status.textContent = 'Preferences saved.';            // --a11y-status-announce style
    // Listening script expectation: "Preferences saved." — narration quote goes in the bug
    // tracker verbatim if anything else is heard.
  });
  function persist() { return Promise.resolve(); }
</script>
<style>
  main { max-width: 380px; font: 14px/1.5 system-ui, sans-serif; }
  button { background: #2563EB; color: #fff; border: none; border-radius: 6px;
           padding: 8px 16px; font-weight: 600; cursor: pointer; }
  #status { min-height: 1.5em; color: #15803D; font-weight: 600; }
</style>
```

## 10. Implementation Checklist

- [ ] Every core flow has a numbered listening script (`--a11y-core-flow-script`) with expected narration written before the test runs.
- [ ] The full `--a11y-reader-matrix` (NVDA, JAWS, VoiceOver, TalkBack) ran on the release; per-pairing results are recorded, not assumed.
- [ ] Navigation passes used `var(--a11y-nav-by-headings)` (H) and `var(--a11y-nav-by-landmarks)` (D), not Tab-walking alone.
- [ ] Both NVDA browse and focus modes were exercised; virtual-cursor behavior is part of the script.
- [ ] Findings follow `--a11y-finding-format`: reader name, exact keystroke, and verbatim narration quote.
- [ ] Automated axe results are treated as the `--a11y-auto-coverage-ceiling` floor, never as the verdict.
- [ ] Widget listening scripts (open/navigate/select/close) exist for every custom APG pattern in the product.
- [ ] Any by-ear failure ships a documented interim workaround while the real fix is in progress.

---
name: onboarding-copy
description: First-run guidance that respects intelligence: progressive disclosure, show-don't-tour, and copy that gets users to value fast.
tags: [onboarding, first-run, microcopy, ux-writing, progressive-disclosure]
related: [empty-states, writing-principles, component-microcopy]
---

# UX Writing Guide: Onboarding & First-Run Copy

## 1. Definition

Onboarding copy is the first conversation with a new user, and its success metric is time-to-value - not tour completion. The discipline covers first-run copy (welcome without wall-of-text), progressive disclosure (explain at the moment of need, not upfront), empty-state-first onboarding (the best tour is a well-written empty state plus a CTA), and the anti-tour principle: users skip carousels and dismiss tooltips; copy that intervenes at the moment of action survives.

## 2. Core Principles

- **Time-to-value is the metric:** every onboarding string either shortens the path to first value or gets deleted.
- **Show, don't tour:** the best onboarding is an empty state with a CTA - not a carousel explaining a product the user can't touch yet.
- **Explain at the moment of need:** contextual hints ("Your API key lives here") beat upfront documentation every time.
- **Progressive disclosure, not firehose:** one concept per screen; the next concept waits until this one is done.
- **Respect the skip:** every tour dismisses persistently and never re-shows - re-forcing onboarding teaches resentment.
- **First session earns the second:** "Do this one thing" beats "Complete all 12 setup steps" - momentum over completionism.
- **Checklists externalize progress:** "Set up your profile" with visible completion state - progress motivates better than prose.
- **Sample data beats explanation:** pre-filled demo content with a "replace with yours" path teaches by example.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Metric | `--uxw-onboarding-metric` | `time-to-value` | The only success measure |
| Mode | `--uxw-onboarding-mode` | `empty-state-first` | Well-written empties over tours |
| Disclosure | `--uxw-onboarding-disclosure` | `at-moment-of-need` | Contextual over upfront |
| Concept load | `--uxw-onboarding-concept-load` | `1-per-screen` | Firehose is failure |
| Skip | `--uxw-onboarding-skip` | `persistent-dismiss` | Never re-show skipped tours |
| Checklist | `--uxw-onboarding-checklist` | `visible-progress` | Externalized completion state |
| First CTA | `--uxw-onboarding-first-cta` | `one-thing` | Single first action, not a list |
| Sample data | `--uxw-onboarding-sample-data` | `demo+replace-path` | Example over explanation |
| Hint timing | `--uxw-onboarding-hint-timing` | `after-first-idle` | Hints appear on dwell, not on load |
| Copy length | `--uxw-onboarding-copy-length` | `headline+1-line` | Overlays stay tiny |

Consume them by linking `assets/css/onboarding-copy.css` at the app root and reading `var(--uxw-onboarding-<role>)` wherever first-run behavior is configured - the metric gates what ships, the skip token forces persistence in storage, and the hint-timing token keeps hints off the load path and on dwell.

## 4. Composition

- **Composes with empty-states (guide 04):** empty-state-first onboarding makes guide 04 the primary surface - the first-run welcome is usually an empty panel with a value statement and CTA, so the two guides share formulas and tone rules.
- **Composes with component-microcopy (guide 07):** contextual hints are microcopy with onboarding timing - the tooltip/hint budgets, phrasing, and the WCAG 1.4.13 contract all come from that guide; this guide supplies when and whether to show them.
- **Composes with component-recipes empty-loading-error + cards-lists:** checklists and welcome cards are component surfaces carrying this copy - the recipe owns structure and states, this guide owns the strings and the sequencing.

## 5. Signature Patterns

- **The setup checklist:** 3-6 tasks with visible progress and per-task copy - the durable onboarding pattern that respects skip behavior, because each task can be completed, skipped, or ignored without blocking the product.
- **The contextual hint:** one tooltip/spotlight per surface, timed to dwell, dismissed persistently - intervention at need; the hint appears only after the user pauses on the surface, proving attention, and its dismissal is stored so it never returns.

## 6. Real-World Use Cases

- **SaaS first-run:** workspace setup, first project, invite flow - the classic time-to-value sprint.
- **Feature adoption:** launching a new capability to existing users, who need orientation without re-onboarding.
- **Audit:** unskippable tours, wall-of-text welcomes, re-forced onboarding that ignores stored dismissals.

## 7. Combination Notes

### With other ux-writing skills

- **Good with writing-principles, voice-tone, component-microcopy, and button-labels:** brevity and user-first ordering decide whether an onboarding string survives, tone-safe warmth must collapse into plain clarity the moment a task begins, contextual hints are microcopy slots, and the first CTA is a full button-label contract - the most-read label in the product.
- **Good with forms-labels, notifications, error-messages, accessible-writing, copy-audit, localization-i18n:** setup tasks end in forms (labels and validation rules apply), progress and completion are quiet notifications, first-run failures need the error contract, dismissals must be operable by AT, and idiom-heavy welcome copy is flagged for i18n. There is no avoid list: onboarding consumes every other copy discipline at the highest-attention moment in the product's life.
- **Caution with empty-states:** the strongest partnership in the guide carries one governance risk - both skills claim the first-use surface. The boundary: an empty state teaches one feature's value with one action; onboarding decides the sequence and the single next step. Let the empty panel stay atomic and put the sequencing in the checklist, or the empty state grows into the empty-essay anti-pattern.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and glassmorphism:** minimalism enforces the one-concept-per-screen rule, flat-design keeps checklists and CTAs unambiguous, and glassmorphism's layered surfaces suit spotlight-style contextual hints that sit above the UI without restructuring it.
- **Caution with brutalism-ui:** its deliberately raw, dense, high-contrast surfaces fight the calm, skimmable first-run moment - a checklist drowned in brutalist noise reads as an obstacle. If the product is brutalist, isolate onboarding surfaces into calmer islands and keep the copy budget strict.

### With motion skills (companion repo skill-animation)

- **Good affinity with entrance-exit and illustration-lottie:** welcome cards and checklists earn a short entrance at token durations, and looping illustration is the friendly mood layer - both must stay brief enough not to delay time-to-value. There is no caution list: motion in onboarding is welcome but bounded - every animated overlay is keyboard-operable, dismissible, and pauses under reduced-motion, so animation never becomes the trap the anti-tour principle bans.

## 8. Anti-Patterns

- **The mandatory tour** — carousels blocking first use of the product
- **Firehose onboarding** — twelve concepts on the first screen
- **Re-forced onboarding** — dismissals ignored, hints returning forever
- **Prose over example** — paragraphs explaining what a pre-filled demo would show

### Accessibility Notes

Onboarding must not trap or rush: tours are keyboard-operable, dismissible, and pause under reduced-motion (a11y repo cognitive-content) - hint timing must respect screen reader pacing, and overlays announce politely. Concretely: the dwell trigger must not be hover-only (focus counts as dwell too), the hint enters the accessibility tree with a polite announcement, and the persistent dismissal is a real control, not a click-away accident. The fallback is the strongest in this repo: if interactive tours cannot be made a11y-clean, replace them with written setup checklists (plain HTML) - a checklist is inherently accessible and respects the skip, which is why it is the default pattern rather than the fallback.

## 9. Code Examples

### Example 1 — Setup checklist with visible progress and persistent dismiss

```html
<aside class="checklist" id="setup" aria-labelledby="setup-h">
  <div class="head">
    <h2 id="setup-h">Get started</h2>
    <button type="button" class="close" id="dismiss" aria-label="Dismiss setup checklist">&#215;</button>
  </div>
  <p class="progress"><span id="done">1</span> of 3 done</p>
  <div class="bar" role="progressbar" aria-valuemin="0" aria-valuemax="3" aria-valuenow="1" id="bar"><span id="fill"></span></div>
  <ul id="tasks">
    <li class="task done"><span class="tick" aria-hidden="true">&#10003;</span> Set up your profile</li>
    <li class="task"><a href="#invite">Invite your team</a><span class="tick" aria-hidden="true"></span></li>
    <li class="task"><a href="#project">Create your first project</a><span class="tick" aria-hidden="true"></span></li>
  </ul>
</aside>
<p id="gone" hidden>Checklist dismissed. You can reopen it anytime from Settings.</p>
<style>
  :root { --uxw-onboarding-checklist: visible-progress; --uxw-onboarding-skip: persistent-dismiss; --color-brand: #2563eb; }
  .checklist { font: 15px/1.5 system-ui, sans-serif; max-width: 320px; border: 1px solid #e5e5e5; border-radius: 12px; padding: 16px; color: #171717; }
  .head { display: flex; justify-content: space-between; align-items: center; } h2 { margin: 0; font-size: 16px; }
  .close { background: none; border: none; font-size: 18px; cursor: pointer; color: #737373; } .progress { margin: 8px 0 4px; color: #525252; font-size: 13px; }
  .bar { height: 6px; background: #eee; border-radius: 3px; margin-bottom: 12px; }
  .bar span { display: block; height: 100%; width: 33%; background: var(--color-brand); border-radius: 3px; transition: width 200ms ease; }
  ul { margin: 0; padding: 0; list-style: none; } .task { display: flex; justify-content: space-between; padding: 8px 0; border-top: 1px solid #f0f0f0; }
  .task a { color: var(--color-brand); font-weight: 600; text-decoration: none; } .task.done { color: #404040; } .tick { color: #16a34a; font-weight: 700; }
</style>
<script>
  const KEY = 'onboarding.checklist.dismissed';
  if (localStorage.getItem(KEY)) { // --uxw-onboarding-skip: never re-show
    document.getElementById('setup').hidden = true;
    document.getElementById('gone').hidden = false;
  }
  document.getElementById('dismiss').addEventListener('click', () => {
    localStorage.setItem(KEY, '1'); // persistent: the skip survives reloads
    document.getElementById('setup').hidden = true;
    document.getElementById('gone').hidden = false;
  });
  function complete(el) { // completing a task updates count, bar, aria-valuenow
    el.classList.add('done');
    const done = document.querySelectorAll('.task.done').length, total = document.querySelectorAll('.task').length;
    document.getElementById('done').textContent = done;
    document.getElementById('fill').style.width = (done / total * 100) + '%';
    document.getElementById('bar').setAttribute('aria-valuenow', done);
  }
</script>
```

### Example 2 — Contextual hint timed to dwell, dismissed persistently

```html
<section class="surface" id="apikey" tabindex="0">
  <h3>API keys</h3>
  <p>Manage the keys your integrations use.</p>
</section>
<div class="hint" id="hint" role="note" hidden>
  <p><strong>Your API key lives here.</strong> Create one, then paste it into your integration.</p>
  <button type="button" class="got" id="gotIt">Got it</button>
</div>
<style>
  :root { --uxw-onboarding-hint-timing: after-first-idle; --uxw-onboarding-copy-length: headline+1-line; --color-brand: #2563eb; }
  body { font: 15px/1.5 system-ui, sans-serif; max-width: 340px; margin: 24px auto; }
  .surface { border: 1px solid #e5e5e5; border-radius: 10px; padding: 16px; position: relative; }
  .surface h3 { margin: 0 0 4px; font-size: 15px; } .surface p { margin: 0; color: #525252; }
  .hint { position: absolute; margin-top: 8px; background: #111827; color: #f9fafb; border-radius: 8px; padding: 12px 14px; max-width: 300px; box-shadow: 0 4px 12px rgb(0 0 0 / .15); animation: rise 180ms ease; }
  .hint p { margin: 0 0 8px; } .hint strong { color: #fff; }
  .got { background: var(--color-brand); color: #fff; border: none; border-radius: 6px; padding: 5px 12px; font: 600 13px system-ui, sans-serif; cursor: pointer; }
  @keyframes rise { from { opacity: 0; transform: translateY(4px); } to { opacity: 1; transform: none; } }
  @media (prefers-reduced-motion: reduce) { .hint { animation: none; } }
</style>
<script>
  const KEY = 'onboarding.hint.apikey.dismissed';
  const hint = document.getElementById('hint');
  let timer = null;
  if (!localStorage.getItem(KEY)) {
    // Dwell = mouseenter or keyboard focus, then idle -- never on page load
    const arm = () => { timer = setTimeout(() => { hint.hidden = false; }, 1200); };
    const disarm = () => { if (timer) clearTimeout(timer); timer = null; };
    const surface = document.getElementById('apikey');
    surface.addEventListener('mouseenter', arm);
    surface.addEventListener('focusin', arm);
    surface.addEventListener('mouseleave', disarm);
    surface.addEventListener('focusout', disarm);
  }
  document.getElementById('gotIt').addEventListener('click', () => { // persistent dismiss
    localStorage.setItem(KEY, '1');
    hint.hidden = true;
  });
</script>
```

## 10. Implementation Checklist

- [ ] Every onboarding string is scored against `--uxw-onboarding-metric` (time-to-value) - strings that do not shorten the path are cut.
- [ ] First-run surfaces use `--uxw-onboarding-mode` (empty-state-first) - no blocking carousels before the product is usable.
- [ ] Hints appear on dwell per `--uxw-onboarding-hint-timing`, never on page load, and never hover-only.
- [ ] One concept per screen per `--uxw-onboarding-concept-load`; overlays fit `--uxw-onboarding-copy-length` (headline + 1 line).
- [ ] All tours and hints honor `--uxw-onboarding-skip`: dismissals persist in storage and never re-show.
- [ ] The first session asks one thing per `--uxw-onboarding-first-cta`, expressed as a verb-first, specific button label.
- [ ] Setup uses a checklist with visible progress per `--uxw-onboarding-checklist`, or sample data with a replace path per `--uxw-onboarding-sample-data`.
- [ ] Every overlay is keyboard-operable, dismissible, politely announced, and pauses under reduced-motion.

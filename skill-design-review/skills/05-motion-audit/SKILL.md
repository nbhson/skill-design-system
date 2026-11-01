---
name: motion-audit
description: Is motion serving the interface — purpose classification, token adherence, the duration ladder, and reduced-motion verification for every animated surface.
tags: [motion, animation, audit, reduced-motion, timing]
related: [review-process, a11y-audit, perceived-performance]
---

# Design Review Guide: Motion Audit

## 1. Definition

The motion audit asks one question of every animated surface: does this motion communicate, orient, or reward — or is it decoration fighting the user? The pass checks purpose (each animation is classified as feedback, orientation, state-change, reward, or decoration), token adherence (durations and easings come from skill-animation's motion tokens, not one-off values), the duration ladder (UI feedback 100–300ms, transitions 300–500ms, nothing over 1s without documented reason), looping restraint, and the reduced-motion collapse. The output is an animation inventory per surface — every motion listed with type, duration, easing, loop, and fallback — which is what makes purposelessness visible.

## 2. Core Principles

- **Every animation is classified:** feedback, orientation, state-change, reward, or decoration — purposeless decoration is a finding.
- **Durations come from the ladder:** 100–300ms feedback, 300–500ms transitions, 1s max without documented reason (the skill-animation easing-timing contract).
- **Easings come from tokens:** one-out easings for entrances, standard curves elsewhere — random cubic-bezier values are findings.
- **Loops are rationed:** one ambient loop per viewport max, none on data-heavy surfaces — competing loops are a finding.
- **Reduced-motion collapses everything:** the audit flips the media query and verifies every animation degrades to static — no exceptions.
- **Motion never blocks:** animations under 500ms don't gate interaction; long sequences are interruptible (WCAG 2.2.2).
- **Interruptibility is tested:** mid-animation clicks and taps work — animations that lock the UI are major findings.
- **Entrances respect the user's position:** scroll-triggered motion doesn't re-trigger on scroll-up jitter, and never hides content from assistive technology.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Classification | `--rev-motion-classification` | `feedback,orientation,state,reward,decoration` | Purposeless = finding |
| Threshold | `--rev-duration-ladder` | `feedback-100-300,transition-300-500,max-1s` | skill-animation contract |
| Contract | `--rev-easing-adherence` | `tokens-only` | No random bezier values |
| Threshold | `--rev-loop-ration` | `one-per-viewport` | None on data-dense surfaces |
| Check | `--rev-reduced-motion` | `collapse-verified` | Audited with media query flipped |
| Contract | `--rev-non-blocking` | `under-500ms-or-interruptible` | 2.2.2 contract |
| Test | `--rev-interruptibility-test` | `mid-animation-interaction` | UI lock = major finding |
| Check | `--rev-scroll-trigger-check` | `no-jitter-retrigger` | Scroll-up stability |
| Rule | `--rev-at-parallel` | `motion-never-only-signal` | State also announced |
| Score | `--rev-motion-score` | `per-surface` | Feeds report template |

Consume them by linking `assets/css/motion-audit.css` once at the review workspace root, then referencing `var(--rev-duration-ladder)` and the other tokens from audit scripts, inventory templates, and scorecards — no audit hardcodes a duration threshold inline. If a surface seems to need motion outside the ladder, that is a documented-exception conversation through review-process, never a silent 1.4s entrance.

## 4. Composition

- **Composes with skill-animation:** that repo defines the motion tokens and disciplines (easing-timing, micro-interactions, ambient-motion); this audit verifies their application on real surfaces.
- **Composes with a11y-audit (guide 04):** reduced-motion and interruptibility checks are shared passes — the two audits run them together and file findings once.
- **Composes with perceived-performance (guide 10):** motion shapes perceived speed; skeleton shimmer, progress motion, and the duration ladder are read together with the response-time bands.

## 5. Signature Patterns

- **The animation inventory:** per surface, every animation listed with type/duration/easing/loop/fallback — the inventory makes purposelessness visible and turns "does it feel busy?" into a countable table.
- **The reduced-motion flip:** audit once with the media query on — anything still moving (or vanished without a static state) is a finding; the flip doubles as the accessibility contract for guide 04.

## 6. Real-World Use Cases

- **Motion-rich products** (marketing, consumer apps) auditing restraint before a launch.
- **Products adopting skill-animation tokens** verifying adherence across surfaces.
- **Audit triage:** flarb everywhere, UI-locking sequences, and missing fallbacks, ranked by severity.

## 7. Combination Notes

### With other design-review skills

- **Pairs with review-process and report-template:** findings flow through the shared severity scale; the animation inventory becomes a scored section of the report.
- **Pairs with a11y-audit:** reduced-motion, interruptibility, and the "motion never the only signal" rule are shared checklist sections — one pass, one set of findings.
- **Pairs with perceived-performance (with caution):** the two audits read together because motion shapes perceived speed — but they can pull in opposite directions: perceived-performance rewards continuous motion while motion-audit rations it. Resolve by classifying each animated wait as honest progress (keep) versus decoration (cut).
- **Pairs with visual-hierarchy-audit, interaction-states-audit, and consistency-audit:** entrance motion must not fight hierarchy, state feedback must use motion tokens, and easing values must be consistent across surfaces — the audits share evidence.
- **No avoid list:** every sibling can run before or after the motion pass without conflict.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and aurora-ui:** these styles either need very little motion (minimalism, flat) or motion as atmosphere (aurora) — both are easy to audit against the classification and loop-ration tokens.
- **Caution with maximalism:** expressive styles lean on layered entrances and ambient loops; the audit still enforces the ladder and the one-loop rule, so expect documented exceptions rather than free rein.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing, micro-interactions, and reduced-motion:** these are the contracts this audit enforces — durations, easings, and feedback motion come from tokens, and the collapse behavior is verified with the media query flipped.
- **Caution with ambient-motion:** ambient loops are permitted but rationed; the audit flags any viewport with more than one loop and bans them outright on data-dense surfaces, so ambient-heavy designs need a per-surface loop budget up front.

## 8. Anti-Patterns

- **Flarb-everything** — entrance animations on every element fighting for attention
- **UI-locking motion** — sequences that ignore input until finished
- **Loop soup** — multiple ambient animations competing in one viewport
- **Fallback-less motion** — reduced-motion users getting vanished content

### Accessibility Notes

The motion audit enforces WCAG 2.2.2 (pause/stop/hide), 2.3.3 (animation from interactions), and `prefers-reduced-motion`: every animation must have a static fallback and must never be the only state signal — a toast that appears only via slide-and-fade fails twice, once for reduced-motion users and once for screen reader users who never hear it. This is why `--rev-at-parallel` requires state to be announced through text or ARIA alongside any motion cue, and why the reduced-motion flip is run with content-visibility verified, not just animation-stopping verified. The fallback rule when classification is contested: apply the strict test — motion must communicate something text or position cannot; if the team can't articulate the purpose in one sentence, it's decoration and gets removed.

## 9. Code Examples

### Example 1 — Animation inventory extractor (type/duration/easing/loop/fallback)

Tokens: `assets/css/motion-audit.css`

```html
<div class="demo">
  <button class="btn">Save changes</button>
  <div class="toast" role="status">Saved</div>
  <div class="ambient"></div>
  <table class="inventory" id="inventory">
    <caption>Animation inventory</caption>
    <thead><tr><th>Element</th><th>Type</th><th>Duration</th><th>Easing</th><th>Loop</th><th>Verdict</th></tr></thead>
    <tbody></tbody>
  </table>
</div>
<style>
  :root { /* mirrors assets/css/motion-audit.css */
    --rev-duration-ladder: feedback-100-300,transition-300-500,max-1s; --rev-easing-adherence: tokens-only;
    --motion-fast: 150ms; --motion-normal: 300ms; --ease-out: cubic-bezier(0, 0, 0.2, 1);
  }
  .demo { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 520px; }
  .btn { padding: 8px 16px; border: none; border-radius: 6px; background: #2563EB; color: #fff; cursor: pointer; transition: background var(--motion-fast) var(--ease-out); }
  .toast { opacity: 0; transform: translateY(8px); transition: opacity var(--motion-normal) var(--ease-out); }
  .toast.show { opacity: 1; transform: none; }
  .ambient { height: 24px; background: #E5E7EB; animation: pulse 2.4s infinite; } /* rationed: the one loop */
  @keyframes pulse { 50% { opacity: 0.4; } }
  .inventory { margin-top: 12px; border-collapse: collapse; width: 100%; font-size: 12px; }
  .inventory th, .inventory td { border: 1px solid #D4D4D4; padding: 4px 8px; text-align: left; }
</style>
<script>
  // Inventory pass: enumerate animated elements, diff against the duration ladder.
  const parseMs = (t) => t.endsWith('ms') ? +t.slice(0, -2) : +t.slice(0, -1) * 1000;
  document.querySelectorAll('.btn, .toast, .ambient').forEach((el) => {
    const cs = getComputedStyle(el);
    const row = document.querySelector('#inventory tbody').insertRow();
    const animated = cs.animationName !== 'none' || parseMs(cs.transitionDuration) > 0;
    const dur = parseMs(cs.animationDuration !== '0s' ? cs.animationDuration : cs.transitionDuration);
    const kind = cs.animationIterationCount === 'infinite' ? 'ambient loop' : 'state/feedback';
    const verdict = !animated ? 'static'
      : dur > 1000 ? 'FAIL: over 1s ladder max'
      : dur < 100 ? 'FAIL: under feedback floor'
      : 'PASS';
    row.innerHTML = `<td>.${el.className.split(' ')[0]}</td><td>${kind}</td><td>${dur}ms</td><td>${cs.animationTimingFunction === 'ease' ? cs.animationTimingFunction : cs.transitionTimingFunction}</td><td>${cs.animationIterationCount}</td><td>${verdict}</td>`;
  });
  document.querySelector('.btn').addEventListener('click', () => document.querySelector('.toast').classList.add('show'));
</script>
```

### Example 2 — Reduced-motion flip: all animations collapse to static

Tokens: `assets/css/motion-audit.css`

```html
<div class="rm-demo">
  <button class="card" id="flip-btn">Hover / focus me</button>
  <label class="toggle"><input type="checkbox" id="rm-toggle"> Simulate prefers-reduced-motion</label>
  <p class="note" id="rm-note">Animations active — flip the toggle to verify the collapse.</p>
</div>
<style>
  :root { /* mirrors assets/css/motion-audit.css */
    --rev-reduced-motion: collapse-verified;
    --motion-normal: 300ms; --ease-out: cubic-bezier(0, 0, 0.2, 1);
  }
  .rm-demo { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 380px; display: grid; gap: 12px; }
  .card { padding: 20px; border: 1px solid #D4D4D4; border-radius: 8px; background: #fff; cursor: pointer;
          transition: transform var(--motion-normal) var(--ease-out), box-shadow var(--motion-normal) var(--ease-out);
          animation: rise 600ms var(--ease-out) both; }
  .card:hover, .card:focus-visible { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.12); }
  @keyframes rise { from { opacity: 0; transform: translateY(12px); } }
  .toggle { display: flex; gap: 8px; align-items: center; }
  .note { color: #404040; font-size: 12px; }
  .rm .card { animation: none; opacity: 1; transform: none; transition: none; } /* audit target: static collapse */
  .rm .card:hover, .rm .card:focus-visible { transform: none; box-shadow: none; }
</style>
<script>
  // Flip harness mirroring the audit's media-query flip; real audits test the OS setting.
  const root = document.documentElement, note = document.getElementById('rm-note');
  document.getElementById('rm-toggle').addEventListener('change', (e) => {
    root.classList.toggle('rm', e.target.checked);
    note.textContent = e.target.checked
      ? 'Reduced motion ON — entrance and hover motion collapsed to static; content still visible.'
      : 'Animations active — flip the toggle to verify the collapse.';
    // Contract check: collapsed state must keep content visible (no vanished fallbacks).
    const card = document.querySelector('.card');
    console.assert(getComputedStyle(card).opacity === '1', 'reduced-motion fallback must not hide content');
  });
</script>
```

## 10. Implementation Checklist

- [ ] Every animation on the surface is classified (feedback/orientation/state/reward/decoration) in the inventory, and decoration entries are queued for removal.
- [ ] All durations sit inside `--rev-duration-ladder`: 100–300ms feedback, 300–500ms transitions, nothing over 1s without a documented exception.
- [ ] Every easing value comes from motion tokens — zero random cubic-bezier literals in the audited CSS.
- [ ] At most one ambient loop per viewport, and none on data-heavy surfaces.
- [ ] The reduced-motion flip is run: every animation collapses to a visible static state, verified with `--rev-reduced-motion`.
- [ ] No animation gates interaction: everything under 500ms or interruptible mid-sequence.
- [ ] Motion is never the only state signal — text or ARIA announces every state motion signals.
- [ ] The completed inventory feeds `--rev-motion-score` in the per-surface report.

---
name: a11y-audit
description: The conformance pass over any surface — keyboard walks, screen reader runs, contrast checks, and severity-ranked WCAG findings that gate the release.
tags: [accessibility, wcag, audit, keyboard, contrast]
related: [review-process, motion-audit, interaction-states-audit]
---

# Design Review Guide: Accessibility Audit

## 1. Definition

The a11y audit is the conformance pass over a surface: a keyboard-only walk (is every action reachable and operable?), a screen reader run on critical flows (are names, roles, and states announced correctly?), programmatic contrast checks (text 4.5:1, UI components 3:1), zoom and reflow testing at 400%, and reduced-motion verification — with every finding ranked by WCAG success criterion and severity. This guide is the audit translation of skill-accessibility: the criteria guides live there; the pass protocol and scoring live here. Automated scanners are treated as the floor, not the audit — axe-class tooling catches roughly 30% of issues, and the human passes (keyboard, screen reader, zoom) find the rest.

## 2. Core Principles

- **Keyboard first:** a full keyboard-only walk of every flow — unreachable controls, traps without escape, and invisible focus are all blocker-severity findings.
- **Screen reader pass on key flows:** critical flows (signup, checkout) run with NVDA/VoiceOver — narration failures (unnamed buttons, unannounced errors) are major findings.
- **Contrast is checked programmatically:** text 4.5:1 (3:1 for large text), UI components 3:1 (WCAG 1.4.3 / 1.4.11) — sampled by eye during review, verified by tool before sign-off.
- **Zoom and reflow at 400%:** content remains usable at 320px width / 400% zoom (WCAG 1.4.4/1.4.10) — clipped or overlapping controls are findings.
- **Reduced motion honored:** animations collapse under the media query (2.3.3) — the audit flips the setting and re-checks every animated surface.
- **Forms get the full pass:** labels present, errors announced, focus moves to the failing field — forms are the highest-density a11y failure surface.
- **Findings cite criteria:** every finding maps to a WCAG SC plus severity — "a11y could be better" is not a finding.
- **Automated scans are the floor, not the audit:** axe catches ~30%; the human passes find the remaining majority.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Protocol | `--rev-keyboard-walk` | `full-flow-blocker-gate` | First pass; traps/invisible focus = blocker |
| Protocol | `--rev-sr-pass` | `critical-flows-nvda-voiceover` | Names/roles/states verified |
| Threshold | `--rev-contrast-text` | `4.5:1-3:1-large` | WCAG 1.4.3 |
| Threshold | `--rev-contrast-ui` | `3:1-components` | WCAG 1.4.11 |
| Threshold | `--rev-zoom-reflow` | `400%-320px` | WCAG 1.4.4/1.4.10 |
| Check | `--rev-reduced-motion-check` | `media-query-flipped` | WCAG 2.3.3 |
| Pass | `--rev-forms-focus` | `highest-density-pass` | Labels/errors/focus |
| Finding | `--rev-findings-cite-criteria` | `wcag-sc+severity` | Machine-checkable findings |
| Tooling | `--rev-auto-scan-role` | `floor-not-audit` | axe ~30% coverage |
| Gate | `--rev-a11y-gate` | `blockers-block-release` | Release gate integration |

Consume them by linking `assets/css/a11y-audit.css` once at the review workspace root, then referencing `var(--rev-keyboard-walk)`, `var(--rev-contrast-text)`, and the rest from audit scripts, scorecard templates, and gate checklists — review tooling never hardcodes thresholds inline. If a pass seems to need a threshold not in this table, the protocol is incomplete; extend it through the review-process guide, not through per-audit improvisation.

## 4. Composition

- **Composes with skill-accessibility:** that repo owns the criteria guides (keyboard-navigation, color-contrast, screen-readers); this guide runs the pass protocol that scores surfaces against them.
- **Composes with review-process (guide 01):** a11y blockers gate the release — the binary integration where `var(--rev-a11y-gate)` decides ship/no-ship.
- **Composes with interaction-states-audit (guide 08):** focus visibility and state styling overlap — the two passes are scheduled together to avoid auditing the same controls twice.

## 5. Signature Patterns

- **The keyboard walk protocol:** unplug the mouse, complete the flow end to end, log every failure point with its step — the single highest-yield a11y pass, and the first one run.
- **The criteria-mapped scorecard:** a findings table (surface, WCAG SC, severity, fix, owner) reused across audits — the schema makes findings machine-checkable and enables trend tracking between releases.

## 6. Real-World Use Cases

- **Pre-release gates on any user-facing surface:** the a11y section of the release gate runs this protocol in full.
- **Conformance targets for regulated products:** WCAG 2.1/2.2 AA documentation built from the criteria-cited findings table.
- **Audit triage:** traps, unnamed controls, contrast fails, and zoom breakage, ranked by severity for the fix backlog.

## 7. Combination Notes

### With other design-review skills

- **Pairs with review-process, report-template, and interaction-states-audit:** the process defines how the protocol runs, the report template carries its findings table, and the states audit shares the focus/keyboard passes — coordinated, not duplicated.
- **Pairs with motion-audit, typography-audit, and consistency-audit:** reduced-motion, text contrast, and pattern consistency are shared checks; findings cite the same severity scale regardless of which guide surfaced them.
- **Pairs with visual-hierarchy-audit, content-microcopy-audit, and responsive-audit:** heading structure, link/label text, and reflow behavior are a11y-adjacent — the audit reuses their outputs rather than re-running them.
- **No caution or avoid list:** as the enforcement pass, this guide is compatible with every sibling — the failure mode to prevent is any audit that bypasses it (shipping without the gate).

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and class-morphism:** these styles rely on restrained palettes and clear state treatment, which makes the 4.5:1/3:1 contrast thresholds and focus-visibility contracts straightforward to satisfy.
- **No style is exempt:** even deliberately expressive styles pass the same protocol — if a style choice (low-contrast text, invisible focus) conflicts with a WCAG criterion, the criterion wins and the style adapts.

### With motion skills (companion repo skill-animation)

- **Good affinity with reduced-motion and easing-timing:** the audit flips `prefers-reduced-motion` and verifies every animation degrades to a static state, and checks that state-transition durations stay inside the duration ladder so motion never gates interaction.
- **Shared checklist section:** the reduced-motion collapse verified here is the same contract skill-animation's reduced-motion guide defines — motion-audit and a11y-audit run it together (see guide 05).

## 8. Anti-Patterns

- **Scan-only audits** — axe green while the keyboard walk fails at step one
- **Retrofitted a11y** — conformance attempted at launch week
- **Criteria-less findings** — 'make it more accessible' with no SC cited
- **Unchecked zoom** — 400% users finding clipped controls

### Accessibility Notes

This guide IS the a11y enforcement pass: it operationalizes WCAG 2.1/2.2 AA as a surface-level protocol — keyboard, screen reader, contrast, zoom, motion — and produces severity-ranked, criteria-cited findings that feed the release gate's a11y section. The ordering matters: keyboard first because it is the highest-yield and cheapest pass, screen reader on critical flows because narration failures are invisible to sighted reviewers, contrast programmatically because eyedropper guesses are wrong at the margin, zoom and motion last because they are fast once the others pass. The fallback rule is equally practical: if tooling is limited, the keyboard walk plus manual contrast sampling cover the majority of critical findings — no scanner is required to run a defensible audit.

## 9. Code Examples

### Example 1 — Keyboard-walk harness for a sample form

Tokens: `assets/css/a11y-audit.css`

```html
<form class="signup" id="walk-form">
  <label for="email">Work email</label>
  <input id="email" type="email" autocomplete="email">
  <label for="team">Team name</label>
  <input id="team" type="text">
  <button type="submit">Create account</button>
  <p class="walk-log" id="walk-log" aria-live="polite">Tab through the form; stops are logged.</p>
</form>
<style>
  :root { /* mirrors assets/css/a11y-audit.css */
    --rev-contrast-text: 4.5:1-3:1-large;
    --rev-contrast-ui: 3:1-components;
  }
  .signup { max-width: 360px; font: 14px/1.5 Inter, system-ui, sans-serif; display: grid; gap: 8px; }
  .signup input { padding: 10px; border: 1px solid #767676; border-radius: 6px; font: inherit; }
  .signup :is(input, button):focus-visible { outline: 2px solid #1D4ED8; outline-offset: 2px; } /* 2px + offset, 3:1+ (2.4.13) */
  .walk-log { color: #404040; font-size: 12px; }
</style>
<script>
  // Keyboard-walk logger: records every focusable stop and flags traps/skips.
  const log = document.getElementById('walk-log');
  let stops = 0, last = null;
  document.addEventListener('focusin', (e) => {
    stops++;
    const back = e.target === last; // immediate return = possible trap or focus loss
    log.textContent = `stop ${stops}: ${e.target.id || e.target.tagName}${back ? ' — TRAP CHECK: returned to previous stop' : ''}`;
    last = e.target;
  });
  document.getElementById('walk-form').addEventListener('submit', (e) => {
    e.preventDefault();
    console.assert(stops >= 3, 'keyboard walk: expected >= 3 stops (2 inputs + button)');
  });
</script>
```

### Example 2 — Programmatic contrast checker on sampled pairs

Tokens: `assets/css/a11y-audit.css`

```html
<div class="panel" id="contrast-panel">
  <h2>Contrast sample</h2>
  <p class="sample body">Body text sample</p>
  <p class="sample muted">Muted text sample</p>
  <button class="sample-btn">Primary action</button>
  <pre class="report" id="report"></pre>
</div>
<style>
  :root { /* mirrors assets/css/a11y-audit.css */
    --rev-contrast-text: 4.5:1-3:1-large;
    --rev-contrast-ui: 3:1-components;
  }
  .panel { max-width: 380px; padding: 16px; border: 1px solid #D4D4D4; border-radius: 8px; font: 14px/1.5 Inter, system-ui, sans-serif; }
  .panel h2 { margin: 0 0 8px; font-size: 16px; }
  .body  { color: #171717; }            /* sample pair 1 */
  .muted { color: #A3A3A3; }            /* sample pair 2: expected fail */
  .sample-btn { background: #22C55E; color: #FFFFFF; border: none; border-radius: 6px; padding: 8px 16px; }
  .report { background: #F5F5F5; padding: 8px; font: 12px/1.5 ui-monospace, monospace; }
</style>
<script>
  const lum = (hex) => {
    const [r, g, b] = [1, 3, 5].map((i) => {
      const c = parseInt(hex.slice(i, i + 2), 16) / 255;
      return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * r + 0.7152 * g + 0.0722 * b;
  };
  const ratio = (fg, bg) => {
    const [a, b] = [lum(fg), lum(bg)].sort((x, y) => y - x);
    return ((a + 0.05) / (b + 0.05)).toFixed(2);
  };
  const css = getComputedStyle(document.documentElement);
  const rows = [
    ['body on white', '#171717', '#FFFFFF', 4.5], ['muted on white', '#A3A3A3', '#FFFFFF', 4.5],
    ['white on green', '#FFFFFF', '#22C55E', 4.5], ['btn border (UI)', '#D4D4D4', '#FFFFFF', 3.0],
  ];
  const out = rows.map(([name, fg, bg, min]) => {
    const r = +ratio(fg, bg);
    return `${r >= min ? 'PASS' : 'FAIL'}  ${name}: ${r}:1 (needs ${min}:1)`;
  });
  document.getElementById('report').textContent = out.join('\n');
</script>
```

## 10. Implementation Checklist

- [ ] A full keyboard-only walk is logged for every flow, with traps and invisible focus recorded as blockers per `--rev-keyboard-walk`.
- [ ] Critical flows run under NVDA/VoiceOver with names, roles, and states verified (`--rev-sr-pass`).
- [ ] All text pairs pass 4.5:1 (3:1 large) and UI component pairs pass 3:1, computed programmatically, not eyedropped.
- [ ] The surface is verified at 400% zoom / 320px width with no clipped or overlapping controls.
- [ ] `prefers-reduced-motion` is flipped and every animation collapses to a static state with no vanished content.
- [ ] Every form on the surface has labels, announced errors, and focus moved to the failing field.
- [ ] Every finding in the scorecard cites a WCAG SC and severity — no criteria-less findings ship.
- [ ] The release gate consults `--rev-a11y-gate`: any open blocker blocks the release.

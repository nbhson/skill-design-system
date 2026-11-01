---
name: mascot-character
description: Brand characters done responsibly: proportion systems, emotion ranges, do/don't placements, and the restraint rule.
tags: [mascot, character-design, branding, illustration, placement]
related: [illustration-direction, empty-error-illustrations, svg-optimization]
---

# Visual Asset Guide: Mascot & Character Design

## 1. Definition

A mascot is a brand investment with a maintenance cost: proportion systems (head-height ratios), emotion ranges (the expressions the character can show), pose libraries, and placement rules (where the character appears and where it never does). This guide covers building the character system - turnaround sheets, expression sheets, usage do/don'ts - and the restraint rule: mascots appear at decision-relevant moments (onboarding, celebration, recovery), not on every surface.

## 2. Core Principles

- **The character system is documented:** turnaround (front/side/back), proportions (head counts), and construction - artists reproduce, not reinterpret.
- **Emotion range is a defined set:** the character has an approved expression sheet - new emotions extend the sheet, not improvisation.
- **Placement has do/don't rules:** mascot in onboarding/empty/success yes; mascot in error-payment/destructive-confirm no - placement is a documented matrix.
- **The restraint rule:** mascots at the moments that matter create delight; mascots everywhere create eye-rolling - ration appearances.
- **Mascot never blocks the task:** the character decorates, guides, or celebrates - it never occupies the space the user needs to act in.
- **Consistency across animation and static:** the animated mascot uses the same proportions and voice - Lottie rigs built from the same construction.
- **Cultural review for global mascots:** gestures, colors, and expressions reviewed per market (ux-writing guide 10 cultural discipline).
- **The character has an alt-text story:** when informative (guiding), it's named; when decorative, hidden - mascot does not escape the aria contract.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Character system | `--icon-character-system` | `turnaround+proportions` | Documented construction |
| Proportion rule | `--icon-proportion-rule` | `head-count-ratio` | The character's build formula |
| Emotion sheet | `--icon-emotion-sheet` | `defined-range` | Approved expressions only |
| Pose library | `--icon-pose-library` | `curated-set` | Reused poses; no ad-hoc drawing |
| Placement matrix | `--icon-placement-matrix` | `do/dont-per-surface` | Onboarding yes; payment errors no |
| Restraint rule | `--icon-restraint-rule` | `moments-that-matter` | Rationed appearances |
| Task priority | `--icon-task-priority` | `never-blocks-cta` | Character decorates; user acts |
| Animation parity | `--icon-animation-parity` | `same-construction` | Rigs from the same sheets |
| Cultural review | `--icon-cultural-review` | `per-market` | Gestures/colors checked |
| Mascot aria | `--icon-mascot-aria` | `named-or-hidden` | Same contract as all icons/art |

Consume them by linking `assets/css/mascot-character.css` and referencing `var(--icon-<role>)` in the character kit's documentation page and review tooling - the tokens turn "where may the mascot go" from tribal knowledge into a checkable contract. Any new pose, expression, or placement not covered by a token goes through extension review, not a freelancer's improvisation.

## 4. Composition

- **Composes with illustration-direction (guide 06):** the mascot is the character system within the broader illustration spec - it obeys the same palette, stroke, and perspective rules as every other illustration.
- **Composes with empty-error-illustrations (guide 07):** the mascot is a common empty/error actor - mood rules apply. It may celebrate an empty first-use state; it may not grin on a payment failure.
- **Composes with skill-animation illustration-lottie:** animated mascot states are built as Lottie scenes under motion tokens, rigged from the same construction sheets as the static art (`--icon-animation-parity: same-construction`).

## 5. Signature Patterns

- **The character kit:** turnaround + expression sheet + pose library + placement matrix - one package that any artist or animator can work from. The kit is the deliverable; without it, every new artist restarts the character from scratch.
- **The moment mapping:** mascot appearances mapped to journey moments (welcome, first success, recovery) with approved art per moment - the restraint is pre-decided, so no team meeting debates whether the mascot "fits" a screen; the matrix already answered.

## 6. Real-World Use Cases

- **Consumer products building long-term brand recognition.** A character remembered across sessions is compounding brand equity - if, and only if, it stays consistent.
- **Onboarding-heavy products where guidance benefits from a guide character.** The mascot as named guide (informative, alt-texted) walking users through first-run flows.
- **Audit: mascot overexposure, proportion drift, characters blocking CTAs.** The three decay modes of an aging mascot system this guide's matrix and checklist catch.

## 7. Combination Notes

### With other icons-illustration skills

- **Good with illustration-direction (guide 06):** the mascot lives inside the illustration spec - shared palette, stroke weight, and construction discipline are what keep it recognizably "one character" across artists.
- **Good with empty-error-illustrations (guide 07):** the mascot is a frequent empty/error actor, so the mood ladder applies directly - hopeful on first-use empty states, sympathetic (not cheerful) on errors, full personality only in the 404 slot.
- **Good with animation-integration and svg-optimization:** animated mascot states are Lottie scenes under motion tokens, and static poses go through the optimization pipeline like any illustration - the kit's construction sheets are the source for both.
- **Good with icon-grid-sizing, icon-style-selection, accessible-icons, icon-library-management, icon-usability, favicon-app-icons, and icon-system-audit:** the character consumes the same library, accessibility, and audit contracts as the rest of the asset system.
- **Caution with icon-style-selection:** the mascot's style is fixed by its documented construction - a system-wide style pivot (e.g. flat to textured) must explicitly decide whether the character re-draws or stays, and the matrix must record that decision; an unreviewed pairing silently forks the character's look from the icon set's.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with claymorphism, collage-art, and retro:** claymorphism's soft, dimensional forms flatter rounded character builds; collage-art and retro give the mascot expressive, personality-rich contexts where the emotion sheet's range can actually be used.
- **Caution with brutalism-ui:** brutalism's raw, type-first aesthetic tends to read as anti-character - if the product pivots brutalist, the mascot either becomes an ironic exception (documented in the placement matrix) or retires; do not let the two aesthetics fight on the same screen.

### With motion skills (companion repo skill-animation)

- **Good affinity with illustration-lottie and ambient-motion:** Lottie is the home for rigged mascot states built from the same construction (`--icon-animation-parity`), and ambient-motion's rationing aligns exactly with the restraint rule - at most one idle ambient loop per viewport, and only at a mapped journey moment.
- **Caution notes:** none listed, but the restraint rule outranks motion enthusiasm - an ambient loop counts as an appearance in the moment mapping, and appearance budgets are spent deliberately.

## 8. Anti-Patterns

- **Mascot overexposure** — the character on every surface until users resent it
- **Blocking the task** — mascot art pushing the primary CTA below the fold
- **Proportion drift** — the character's build changing per illustrator
- **Grief moments with the mascot** — cheerful character on payment failures

### Accessibility Notes

Mascots follow the standard art contract: informative guide-moments get text alternatives, decorative appearances are hidden, and animated states respect reduced-motion - the character never becomes an unnamed interactive element. Per `--icon-mascot-aria: named-or-hidden`, a guiding mascot is named (the alt text says who it is and what it signals), while purely decorative poses ship an empty alt so screen readers skip straight to the content the character decorates. The fallback rule: if the character system cannot be fully documented, restrict the mascot to pre-approved static placements (onboarding/empty) - a small consistent set beats an ambitious inconsistent one.

## 9. Code Examples

### Example 1 — The character kit: turnaround sheet + expression strip

Tokens: `assets/css/mascot-character.css`

```html
<article class="kit" aria-label="Character kit: mascot Waffle">
  <h2>Turnaround (front / side / back) - proportions: 2.5 heads</h2>
  <svg class="sheet" viewBox="0 0 220 90" role="img"
       aria-label="Turnaround sheet of mascot Waffle, a rounded blob character, 2.5 heads tall">
    <g class="ink">
      <circle cx="40" cy="45" r="24"/>                        <!-- front -->
      <ellipse cx="110" cy="45" rx="16" ry="24"/>             <!-- side -->
      <circle cx="180" cy="45" r="24"/>                       <!-- back -->
      <path d="M40 69v14M30 90h20" stroke-width="3" fill="none"/>
    </g>
    <g class="face">
      <circle cx="33" cy="40" r="3"/><circle cx="47" cy="40" r="3"/>
      <path d="M34 52q6 5 12 0" stroke-width="3" fill="none"/>
    </g>
    <path class="guide" d="M12 21h196" stroke-dasharray="4 4"/>
  </svg>
  <h2>Expression strip (approved range)</h2>
  <svg class="sheet" viewBox="0 0 220 60" role="img"
       aria-label="Approved expressions: neutral, happy, sympathetic, celebrating">
    <g class="ink">
      <circle cx="35" cy="30" r="20"/><circle cx="90" cy="30" r="20"/>
      <circle cx="145" cy="30" r="20"/><circle cx="200" cy="30" r="20"/>
    </g>
    <g class="face">
      <circle cx="29" cy="27" r="2.5"/><circle cx="41" cy="27" r="2.5"/><path d="M30 36h10"/>
      <circle cx="84" cy="27" r="2.5"/><circle cx="96" cy="27" r="2.5"/><path d="M84 35q6 6 12 0"/>
      <path d="M139 27q3-3 6 0M145 27q3-3 6 0"/><path d="M139 38q6-4 12 0"/>
      <path d="M192 24l4-6M208 24l-4-6" stroke-width="3"/><path d="M194 35q6 7 12 0"/>
    </g>
  </svg>
</article>
<style>
  .kit { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 520px; }
  .kit h2 { font-size: 14px; margin: 16px 0 8px; }
  .sheet { width: 100%; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 8px; }
  .sheet .ink { fill: var(--kit-body, #FCD34D); stroke: var(--kit-line, #92400E); stroke-width: 2.5; }
  .sheet .face { stroke: var(--kit-line, #92400E); stroke-width: 2.5; fill: var(--kit-line, #92400E); }
  .sheet .guide { stroke: #94A3B8; stroke-width: 1.5; }
  /* Restraint rule in code: the kit page itself is documentation, not product chrome */
  </style>
  <script>
    console.assert(getComputedStyle(document.documentElement)
      .getPropertyValue('--icon-restraint-rule').trim() === 'moments-that-matter',
      'mascot appearances must be rationed to moments-that-matter');
  </script>
```

### Example 2 — Placement do/don't matrix

```html
<table class="matrix">
  <caption>Mascot placement: approved vs banned (token: do/dont-per-surface)</caption>
  <thead><tr><th>Surface</th><th>Status</th><th>Why</th></tr></thead>
  <tbody>
    <tr class="do"><td>Onboarding welcome</td><td>Do</td><td>Decision-relevant moment; guide role</td></tr>
    <tr class="do"><td>First-use empty state</td><td>Do</td><td>Hopeful mood matches taxonomy</td></tr>
    <tr class="do"><td>First success / celebration</td><td>Do</td><td>Earned delight; mapped moment</td></tr>
    <tr class="dont"><td>Payment failure</td><td>Don't</td><td>Grief moment - cheer reads as mockery</td></tr>
    <tr class="dont"><td>Destructive confirm dialog</td><td>Don't</td><td>Character must never soften a serious choice</td></tr>
    <tr class="dont"><td>Next to primary CTA</td><td>Don't</td><td>never-blocks-cta: character decorates, user acts</td></tr>
  </tbody>
</table>
<style>
  .matrix { font: 13px/1.5 Inter, system-ui, sans-serif; border-collapse: collapse; }
  .matrix caption { text-align: left; font-weight: 600; padding-bottom: 6px; }
  .matrix th, .matrix td { border: 1px solid #E2E8F0; padding: 6px 10px; text-align: left; }
  .matrix .do td:first-child { border-left: 4px solid #16A34A; }
  .matrix .dont td:first-child { border-left: 4px solid #DC2626; }
</style>
```

## 10. Implementation Checklist

- [ ] The character kit exists as a package: turnaround, proportions (`--icon-proportion-rule: head-count-ratio`), construction notes, expression sheet, pose library, and placement matrix.
- [ ] Every shipped expression appears on the approved expression sheet (`--icon-emotion-sheet: defined-range`) - no improvised faces.
- [ ] Every pose comes from the curated pose library (`--icon-pose-library: curated-set`); ad-hoc drawing is a review failure.
- [ ] Every placement is checked against `--icon-placement-matrix: do/dont-per-surface` - onboarding/empty/success yes; payment-error/destructive-confirm no.
- [ ] Appearance budget is respected (`--icon-restraint-rule: moments-that-matter`) - ambient loops and banners each count as an appearance.
- [ ] No mascot art occupies or displaces a CTA (`--icon-task-priority: never-blocks-cta`).
- [ ] Animated mascot states are rigged from the same construction (`--icon-animation-parity: same-construction`) and honor reduced-motion.
- [ ] Informative guide-moments are alt-texted and decorative ones hidden (`--icon-mascot-aria: named-or-hidden`), with per-market cultural review (`--icon-cultural-review: per-market`).

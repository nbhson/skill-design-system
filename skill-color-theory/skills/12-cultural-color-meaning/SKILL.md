---
name: cultural-color-meaning
description: Color connotations by market: red's three meanings, white's weddings and funerals, and localization discipline for global palettes.
tags: [localization, culture, global, color-meaning, markets]
related: [color-psychology, semantic-color-system, color-harmony]
---

# Color Theory Skill: Cultural Color Meaning

## 1. Definition

The same hue carries different meanings across cultures: red is danger in the US, luck in China, mourning in parts of Africa; white is purity in Western weddings and mourning in parts of East Asia. Global products audit their palettes per market - especially status colors, error states, and campaign visuals - so a palette that celebrates in one market does not mourn in another.

## 2. Core Principles

- **Status colors are the highest-stakes localization:** error-red and success-green have regional variations (e.g., red's positive meanings in CN markets) - status systems are validated per market before launch.
- **Audit per market, not per hue:** launch markets get a documented color review (connotations of the palette's primary hues in that market's contexts).
- **UI conventions vs cultural connotation:** global product UI (error red, link blue) mostly follows platform convention; marketing/brand visuals carry the cultural load.
- **White-space is color:** whitespace-heavy minimalism reads differently in markets where white is mourning-adjacent - density decisions consult the review.
- **Campaign palettes localize:** global campaigns re-check color symbolism per market (gifting, festivals, mourning seasons) - one global campaign visual is a known risk.
- **Local teams review, not just dictionaries:** in-market reviewers catch connotation that color-symbolism tables miss.
- **Do not over-rotate:** users are habituated to global UI conventions; the audit catches genuine collisions, not imaginary ones - over-localization fragments the system.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Culture | `--clr-market-audit-required` | `per-launch-market` | Documented color review per market before launch |
| Culture | `--clr-reviewer-source` | `in-market-teams` | Local review; not symbolism tables alone |
| Culture | `--clr-status-localization-policy` | `platform-convention-default` | UI status follows platform; brand follows market |
| Culture | `--clr-campaign-review` | `per-market-per-campaign` | Campaign visuals re-checked per market |
| Culture | `--clr-high-risk-contexts` | `gift-festival-mourning-finance` | Contexts where connotation bites hardest |
| Culture | `--clr-collision-log` | `documented-exceptions` | Found collisions + resolutions recorded |
| Culture | `--clr-over-localization-guard` | `collisions-only` | Audit catches real collisions; system stays unified |
| Culture | `--clr-market-palette-delta` | `brand-only` | Only brand/campaign layers localize; semantic stays global |
| Culture | `--clr-review-cadence` | `pre-launch-annual` | Launch review + annual refresh per market |
| Culture | `--clr-color-festival-calendar` | `per-market` | Festivals/observances mapped for campaign timing |

Consume them by linking `assets/css/cultural-color-meaning.css` once at the app root, then referencing `var(--clr-...)` from review templates and localization checklists — the audit cadence, reviewer source, and localization policy are recorded configuration. Market deltas re-bind brand-layer aliases via `var(--clr-...)` overrides; the semantic and neutral layers stay global.

## 4. Composition

- **Composes with color-psychology:** psychology gives the baseline associations; this guide localizes them per market.
- **Composes with color-harmony:** caution pair - harmony's hue relationships are chosen globally; cultural review may force per-market accent swaps.
- **Composes with semantic-color-system:** status conventions are validated per market (the guide's highest-stakes audit surface).

## 5. Signature Patterns

- **Market color review template:** per-market checklist (status hues, brand primaries, campaign visuals, whitespace density) with in-market sign-off.
- **Collision log:** documented findings (hue, market, connotation, resolution) become the institutional memory future launches consult.

## 6. Real-World Use Cases

- **Products launching into new markets (APAC, MENA, LATAM).**
- **Global campaign planning with festival calendars.**
- **Audit: pre-launch connotation review of status + brand colors.**

## 7. Combination Notes

### With other color-theory skills

- **Good with color-psychology:** the natural pipeline — psychology establishes the (Western-biased) baseline associations, and this guide localizes them per launch market; one without the other ships either globally tone-deaf or locally invented palettes.
- **Good with semantic-color-system:** status hues are the highest-stakes audit surface — red's positive meanings in some CN contexts collide with error-red conventions, so the policy (`platform-convention-default`) decides per layer: UI status follows platform convention, brand follows market.
- **Good with oklch-perceptual, brand-ramp-construction, gray-ramp-neutrals, dark-mode-palette, data-viz-palettes, contrast-models, cvd-safe-design, and gradient-theory:** these produce the palette layers that the market review audits; localized brand layers re-bind aliases while ramps and validated pairings stay intact underneath.
- **Caution with color-harmony:** harmony schemes are chosen once, globally — but a cultural review can force per-market accent swaps, meaning the scheme relationship holds while specific hues re-point. Plan schemes with a swappable accent so localization does not fork the whole palette.
- **No avoid entries:** cultural review governs when and where hues are deployed, not which color skills are usable.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and retro:** minimalism's whitespace-heavy density is exactly where the "white-space is color" principle applies — density decisions consult the market review; flat and retro styles carry bold, symbolic palettes whose connotations are worth reviewing per market.
- **Caution with collage-art:** collage visuals mix many found colors and images whose cultural references are hard to inventory per market; campaign-grade collage work needs the per-market review applied to every source asset, not just the palette.

### With motion skills (companion repo skill-animation)

- **Good affinity with feedback-confirmation:** confirmation moments (success flashes, celebration states) are precisely where connotation bites — a market's celebratory color motion is validated in the same review as the palette, and festival-timed campaigns pair with celebratory animation kits.
- **General caution:** motion itself carries little cultural color risk, but any animation that recolors brand surfaces per market must keep the validated contrast and CVD properties of the underlying tokens — localization changes hues, never the validated pairing structure.

## 8. Anti-Patterns

- **One-global-palette-by-default** — launching everywhere with zero market review because 'red is universal'
- **Symbolism-table over-rotation** — re-greening error states in China because a table said red is lucky
- **Campaign blind spots** — festival visuals shipping in markets where the palette mourns
- **Dictionary localization** — 'local review' meaning a search, never an in-market human

### Accessibility Notes

Cultural review intersects accessibility: in-market review includes disabled users' context (assistive tech conventions, local a11y norms) - a palette correct for one market's culture may still fail that market's WCAG-equivalent floors (guide 10 governs the numbers everywhere). Localization never relaxes contrast: a per-market brand swap re-points hues through the same validated ramps and re-runs the pairing manifest in that market's theme. The fallback is unambiguous: when a cultural collision conflicts with a status convention, status convention wins and the cultural adjustment moves to non-status surfaces - vocabulary is never recolored for connotation. This keeps error/success/warning legible and conventional for all users while brand and campaign layers absorb the localization.

## 9. Code Examples

### Example 1 — Market color review template

```html
<div class="review">
  <h2>Market color review — launch: Japan</h2>
  <table>
    <thead><tr><th>Layer</th><th>Hue / decision</th><th>Local connotation</th><th>Verdict</th></tr></thead>
    <tbody>
      <tr><td>Status UI</td><td>error-red <code>#DC2626</code></td><td>Follows platform convention</td><td class="pass">Keep global</td></tr>
      <tr><td>Status UI</td><td>success-green <code>#16A34A</code></td><td>Neutral-to-positive</td><td class="pass">Keep global</td></tr>
      <tr><td>Brand primary</td><td>brand-red <code>#E11D48</code></td><td>Celebratory; fine outside status</td><td class="pass">Keep, review campaign use</td></tr>
      <tr><td>Whitespace density</td><td>Minimalist white surfaces</td><td>White is mourning-adjacent in contexts</td><td class="warn">Reviewer input required</td></tr>
      <tr><td>Campaign visual</td><td>Festival hero, Q1</td><td>Must clear festival calendar</td><td class="warn">Per-campaign review</td></tr>
    </tbody>
  </table>
  <p class="signoff">Reviewer: <em>in-market team</em> · Cadence: pre-launch + annual · Logged to collision log</p>
</div>
<style>
  .review { font: 14px/1.5 Inter, system-ui, sans-serif; max-width: 620px; border: 1px solid #e5e5e5;
            border-radius: 10px; padding: 16px; }
  table { border-collapse: collapse; width: 100%; margin: 8px 0; }
  th, td { border-bottom: 1px solid #e5e5e5; padding: 6px 8px; text-align: left; font-size: 13px; }
  th { background: #fafafa; font-weight: 600; }
  code { font-size: 12px; background: #f5f5f5; padding: 1px 4px; border-radius: 4px; }
  .pass { color: #15803d; font-weight: 600; }
  .warn { color: #b45309; font-weight: 600; }
  .signoff { color: #525252; font-size: 12px; margin: 0; }
</style>
```

### Example 2 — Campaign visual localization demo card

```html
<div class="campaigns">
  <h2>Q1 festival campaign — per-market palette</h2>
  <article class="card global">
    <span class="tag">Global default</span>
    <div class="hero" style="background: linear-gradient(135deg, #1D4ED8, #F59E0B)">
      <strong>New Year, New Goals</strong>
    </div>
    <p>Blue↔orange brand axis; validated contrast, CVD-safe.</p>
  </article>
  <article class="card localized">
    <span class="tag">CN market — Lunar New Year</span>
    <div class="hero" style="background: linear-gradient(135deg, #B91C1C, #F59E0B)">
      <strong>新年新目标</strong>
    </div>
    <p>Brand layer re-pointed to festival red-gold; status/error UI stays global red.</p>
  </article>
</div>
<style>
  .campaigns { font: 14px/1.5 Inter, system-ui, sans-serif; display: grid; gap: 12px; max-width: 560px; }
  .card { border: 1px solid #e5e5e5; border-radius: 10px; padding: 12px; }
  .card.localized { border-color: #fca5a5; }
  .tag { font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.04em; color: #525252; }
  .hero { border-radius: 8px; padding: 20px 16px; margin: 8px 0; }
  .hero strong { color: #fff; font-size: 18px; text-shadow: 0 1px 2px rgba(0,0,0,0.45); }
  .card p { margin: 0; color: #525252; font-size: 12px; }
</style>
```

## 10. Implementation Checklist

- [ ] Every launch market has a documented color review before launch (`--clr-market-audit-required`), signed off by in-market teams (`--clr-reviewer-source`).
- [ ] Status/error/success hues follow platform convention by default (`--clr-status-localization-policy`) and are validated per market.
- [ ] Campaign visuals are reviewed per market per campaign (`--clr-campaign-review`) against the festival calendar (`--clr-color-festival-calendar`).
- [ ] High-risk contexts (gift, festival, mourning, finance) are explicitly checked (`--clr-high-risk-contexts`).
- [ ] Whitespace-density decisions in white-adjacent markets consult the review — white-space is treated as color.
- [ ] Found collisions and resolutions are recorded in the collision log (`--clr-collision-log`) and consulted at future launches.
- [ ] Only the brand/campaign layer localizes (`--clr-market-palette-delta`); semantic and neutral layers stay global.
- [ ] The audit catches genuine collisions only (`--clr-over-localization-guard`) — error states are never re-greened, and reviews refresh annually (`--clr-review-cadence`).

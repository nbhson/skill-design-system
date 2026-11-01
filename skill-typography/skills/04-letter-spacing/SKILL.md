---
name: letter-spacing
description: Tracking that tightens with size and loosens for uppercase — the micro-typography that makes headlines breathe and labels read.
tags: [typography, letter-spacing, tracking, uppercase, micro-typography]
related: [type-scale, visual-hierarchy, line-height]
---

# Typography Skill: Letter-Spacing & Tracking

## 1. Definition

Letter-spacing (tracking) adjusts the space between characters: display sizes need negative tracking (large glyphs carry their own air), uppercase labels need positive tracking (+0.04-0.08em) to separate uniform-height letters, and body text stays at 0. It is the smallest typographic token with an outsized effect — good tracking makes headlines look typeset, bad tracking makes them look broken. Because it is so easy to apply and so costly to undo, tracking is never styled ad hoc: it ships as a small closed token set, bundled into text roles alongside size and weight so no consumer ever invents a letter-spacing value in isolation.

## 2. Core Principles

- **Track inversely to size:** display -0.02 to -0.04em, headings -0.01 to -0.02em, body 0, small caps/labels +0.04 to +0.08em.
- **Never letter-space lowercase body:** tracking body text destroys letterform recognition and reading speed — it is for display and labels only.
- **Uppercase earns its tracking:** ALL-CAPS text without +0.04em reads as a dense wall; the tracking IS the readability.
- **Bold + tight is the display pairing:** heavy weights at large sizes with -0.02em tracking is the modern headline look.
- **Tracking in em, not px:** em-based values scale with font size and survive zoom and fluid type.
- **Pairs with the face's design:** some families ship with optical tracking built in (SF Pro, Inter display cuts) — do not double-track.
- **Arabic/Indic scripts never track:** connected scripts break when letter-spaced; tracking tokens apply to Latin/CJK display only.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Display | `--type-tracking-display` | `-0.025em` | Hero/h1 at 48px+; heavy weights |
| Heading | `--type-tracking-heading` | `-0.01em` | h2-h4 at 24-39px |
| Body | `--type-tracking-body` | `0` | Default; body text never tracked |
| Label | `--type-tracking-label` | `0.05em` | Uppercase overlines, nav labels, table headers |
| Microcopy | `--type-tracking-microcopy` | `0.08em` | Eyebrows, badges, tiny uppercase meta |
| Button | `--type-tracking-button` | `0.01em` | Uppercase buttons get minimal air; lowercase buttons stay 0 |
| Tight limit | `--type-tracking-tight-limit` | `-0.04em` | Never tighter; ligature and kerning collisions begin |
| Script exemption | `--type-script-exemption` | `arabic-indic-thai` | Connected scripts exempt from all tracking |
| Optical sizing | `--type-optical-sizing` | `face-built-first` | Prefer optical size axes/Display cuts over manual tracking |
| Tracking bundle | `--type-tracking-bundle` | `with-size-weight` | Tracking ships bundled in text roles, never standalone |

Consume them by linking `assets/css/letter-spacing.css` once at the app root, then referencing `var(--type-tracking-<role>)` from text roles and components — product code never writes a raw `letter-spacing` value. `--type-tracking-body` at `0` is the explicit default the accessibility override assumes; `--type-tracking-tight-limit` is the floor that code review rejects below. If a needed value is not in this table, fix the text role, not the component.

## 4. Composition

- **Composes with type-scale:** tracking values bundle into the scale's text roles (size + weight + tracking are one decision).
- **Composes with uppercase patterns in component design (skill-component-recipes):** table headers, badges, and eyebrows consume tracking-label/microcopy.
- **Composes with variable-fonts:** optical size axes may replace manual tracking — the token records which strategy the family uses.

The bundling rule is what makes this set stable: a text role like `.text-display` carries size, weight, line-height, and tracking together, so a family swap or a fluid-size change re-evaluates tracking in the same review rather than leaking it as a per-component tweak.

## 5. Signature Patterns

- **Bundled text roles:** tracking never appears as an inline style; it lives inside `.text-display`/`.text-label` role definitions. This keeps the seven tracking values reviewable in one place and makes off-token tracking a diff you can see, not a mystery to hunt.
- **Uppercase checklist:** any ALL-CAPS style must ship with tracking >= 0.04em and a lint rule — uppercase-without-tracking is the classic failure. The lint pairs `text-transform: uppercase` with a `var(--type-tracking-label)` (or stronger) declaration; a caps style that fails the pair is rejected in CI, not in design review six weeks later.

## 6. Real-World Use Cases

- **Marketing headlines and hero sections** — negative tracking on display turns big bold type from "WordArt" into something typeset.
- **Dense enterprise UI:** uppercase table headers and nav labels that stay readable — exactly where untracked caps collapse into gray walls.
- **Auditing micro-typography:** tracked-out body text and untracked caps walls — the two failures that signal a team styling tracking by hand.

## 7. Combination Notes

### With other typography skills

- **Good with type-scale, line-height, and font-pairing:** tracking bundles into scale steps (a display size without its negative tracking looks unfinished), compensates leading visually on caps (tracked labels tolerate tighter lines), and depends on the chosen face's built-in optical behavior — the pairing decision decides whether manual tracking applies at all.
- **Good with visual-hierarchy, readability-legibility, and accessible-typography:** tracking is a hierarchy lever for labels and a readability constraint everywhere else — tracked body text fails readability, untracked caps fail scanning; both skills enforce the same body-stays-at-0 rule from opposite directions.
- **Good with fluid-responsive and variable-fonts:** em-based tracking scales with fluid clamps without re-tuning, and optical-size axes can replace manual tracking when the family provides it — the `--type-optical-sizing` token records which strategy wins.
- **Good with multilingual-vietnamese and numeric-tabular:** Vietnamese caps need slightly more tracking for taller mark stacks, while connected-script exemptions (Arabic/Indic/Thai) are the one hard "never" in this set.
- **Caution/avoid list is empty by design:** tracking has no incompatible partners — only misuses (tracked body, px values, connected scripts), which the anti-patterns and the script-exemption token exist to prevent.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, class-morphism, and brutalism-ui:** minimalism lives on generous negative display tracking; class-morphism uses tracked uppercase micro-labels as its technical texture; brutalism's oversized headlines are the strongest case for the tight-limit token.
- **Caution with skeuomorphism and retro:** both styles historically favor loose, ornamental letterforms and face-built spacing; applying the modern tight-display pairing to a retro face fights the style's own typography, so track against the face's intent, not the trend.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** when text reveals or sizes animate, em-based tracking interpolates cleanly with duration tokens — a tracked label fading in reads as one motion, not two desynchronized properties.
- **Caution beyond that:** animating letter-spacing itself (per-character tracking ramps) re-lays-out text every frame and can sever connected scripts mid-animation; treat tracking as a resting property the motion reveals, not a value the motion drives.

## 8. Anti-Patterns

- **Tracked-out body** — +0.1em on paragraphs - slower reading, worse recognition, zero benefit
- **Untracked caps walls** — ALL-CAPS labels at 0 tracking reading as dense blocks
- **Px tracking** — fixed values that break at zoom and fluid sizes
- **Tracking connected scripts** — letter-spacing on Arabic/Indic/Thai that severs the joins

### Accessibility Notes

WCAG 1.4.12 protects the user's right to override text spacing — letter-spacing, word-spacing, and line-height overrides must not break layouts or lose content. Tracking tokens must not fight user stylesheets, and body tracking of 0 is exactly the default the override assumes: any positive tracking on paragraphs compounds with the user's override into unreadable text, which is why tracked-out body is banned outright. Em-based tokens (never px) guarantee the author's intent scales with the user's font-size preference at 200% zoom. The fallback rule: if a display face needs extreme tracking for the brand, apply it only above the reading-size threshold — reading text keeps user-controllable default spacing. Finally, the `arabic-indic-thai` exemption is itself an accessibility rule: letter-spacing on connected scripts severs the joins that encode the letters, destroying legibility for those readers rather than merely looking off.

## 9. Code Examples

### Example 1 — Tracked display headline vs tracked caps label

Tokens: `assets/css/letter-spacing.css`

```html
<header class="hero">
  <p class="eyebrow">Platform Release</p>
  <h1 class="display">Ship typography that scales</h1>
</header>
<style>
  .hero {
    padding: 48px 24px;
    background: #FAFAFA;
    font-family: Inter, system-ui, sans-serif;
  }
  .eyebrow {
    /* Caps micro-label: positive tracking IS the readability */
    margin: 0 0 12px;
    text-transform: uppercase;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: var(--type-tracking-microcopy); /* 0.08em */
    color: #525252;
  }
  .display {
    /* Bold + tight: the display pairing */
    margin: 0;
    font-size: var(--dt-size-3xl, 3.052rem);
    font-weight: 700;
    line-height: 1.1;
    letter-spacing: var(--type-tracking-display); /* -0.025em */
    max-width: 22ch;
    color: #171717;
  }
</style>
```

### Example 2 — Caps table header with the connected-script exemption

Tokens: `assets/css/letter-spacing.css`

```html
<table class="data">
  <thead>
    <tr><th>Name</th><th>Region</th><th>Status</th></tr>
  </thead>
  <tbody>
    <tr><td>deploy-api</td><td>ap-southeast-1</td><td>Passing</td></tr>
  </tbody>
</table>
<script>
  // Script exemption guard: connected scripts are exempt from ALL tracking.
  const CONNECTED = /[\u0600-\u06FF\u0900-\u097F\u0E00-\u0E7F]/; // Arabic, Indic, Thai
  document.querySelectorAll("th, .tracked").forEach((el) => {
    if (CONNECTED.test(el.textContent)) {
      el.style.letterSpacing = "0"; // exemption overrides the token
      console.warn("Tracking suppressed for connected script:", el.textContent);
    }
  });
</script>
<style>
  .data {
    width: 100%;
    max-width: 480px;
    border-collapse: collapse;
    font: 14px/1.5 Inter, system-ui, sans-serif;
  }
  .data th {
    text-align: left;
    text-transform: uppercase;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: var(--type-tracking-label); /* 0.05em — caps earn their air */
    color: #525252;
    border-bottom: 2px solid #E5E5E5;
    padding: 8px 12px;
  }
  .data td {
    letter-spacing: var(--type-tracking-body); /* 0 — body never tracked */
    border-bottom: 1px solid #E5E5E5;
    padding: 10px 12px;
  }
</style>
```

## 10. Implementation Checklist

- [ ] All seven tracking values ship as `--type-tracking-*` tokens in `assets/css/letter-spacing.css`; no raw `letter-spacing` values in product code.
- [ ] Tracking is bundled into text roles (`with-size-weight`) — zero inline tracking styles exist.
- [ ] Every `text-transform: uppercase` style pairs with `var(--type-tracking-label)` or stronger; the lint rejects untracked caps.
- [ ] Body and paragraph text carry `var(--type-tracking-body)` (0) — no tracked-out body anywhere.
- [ ] No tracking value is tighter than `--type-tracking-tight-limit` (-0.04em) or expressed in px.
- [ ] Connected scripts (Arabic/Indic/Thai) are exempt via `--type-script-exemption`; a UI review confirms no tracked joins render.
- [ ] Families with optical-size axes use `--type-optical-sizing: face-built-first` — manual tracking does not double-track Display cuts.
- [ ] Fluid heading roles re-verify tracking at the 320px and 2560px extremes with the fluid-responsive test points.

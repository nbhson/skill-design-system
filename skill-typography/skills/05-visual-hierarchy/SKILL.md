---
name: visual-hierarchy
description: Directing the eye with size, weight, color, and position — the four hierarchy levers applied through text roles instead of per-screen decoration.
tags: [typography, hierarchy, scanning, text-roles, contrast]
related: [type-scale, letter-spacing, line-height]
---

# Typography Skill: Typographic Hierarchy

## 1. Definition

Typographic hierarchy is the deliberate ranking of text so users parse a page's structure in milliseconds: what is the title, what supports it, what is meta. It is built from four levers — size (strongest), weight, color, and position — applied sparingly through a closed set of text roles. Pages with clear hierarchy scan well; pages without it force users to read everything to find anything. The discipline that separates systems from one-off design is the closed set: a screen draws from four fixed ranks, so "what is this text" has one answer per screen and the same answer across every screen.

## 2. Core Principles

- **Size is the strongest lever:** one 2x step says more than any weight change — use it for the single primary element per view.
- **Weight before color:** bold/semibold creates hierarchy without leaving the accessible color set — color changes must still pass contrast.
- **Color ranks last and passes contrast:** secondary text gets its own validated alias (design-tokens guide 05), not an arbitrary gray.
- **One focal point per screen:** exactly one element gets the strongest treatment; two competing 'tops' read as none.
- **Three to four levels per screen:** title / heading / body / meta — more levels fragment into noise.
- **Hierarchy is consistent across screens:** the same role means the same rank everywhere (governance enforces it).
- **Position and grouping support, not replace, type:** proximity and alignment from the layout system back up the type hierarchy.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Hierarchy levels | `--type-hierarchy-levels` | `4` | title / heading / body / meta per screen |
| Title | `--type-text-title` | `2xl semibold, heading leading` | Page title; the single focal rank |
| Heading | `--type-text-heading` | `lg semibold` | Section headers |
| Body | `--type-text-body` | `sm regular, body leading` | Default reading text |
| Meta | `--type-text-meta` | `xs regular, secondary color` | Timestamps, captions, helper text |
| Emphasis policy | `--type-emphasis-policy` | `weight-first` | Bold before color before size for inline emphasis |
| Focal rule | `--type-focal-rule` | `one-per-view` | Exactly one strongest treatment per screen |
| Secondary color alias | `--type-secondary-color-alias` | `color-text-secondary` | De-ranking text uses the validated secondary alias |
| Scale jump rule | `--type-scale-jump-rule` | `min-2-steps` | Title vs body differs by >= 2 scale steps to register |
| Role consistency | `--type-role-consistency` | `cross-screen` | Same role = same rank everywhere; lint-checked |

Consume them by linking `assets/css/visual-hierarchy.css` once at the app root, then referencing `var(--type-text-<role>)` from components — the four role classes are the only sanctioned ranks, and de-ranking text must use `var(--type-secondary-color-alias)` rather than an invented gray. Because these roles are descriptors (a size+weight+leading policy, not raw values), they resolve against the type-scale tokens; if a fifth rank seems necessary, restructure the screen, do not add a role.

## 4. Composition

- **Hierarchy consumes the type-scale roles and validated color aliases** — it is the application layer of both. The scale says what sizes exist; the color tokens say which grays pass contrast; this skill decides which element gets which.
- **It composes with skill-ui-ux styles:** each style weights the levers differently (minimalism: size+space; maximalism: size+color). The role set stays constant; only the lever emphasis shifts per style.
- **It composes with skill-design-review guide 02:** the hierarchy audit applies this guide's rules as its checklist — one focal point, 3-4 levels, weight-first emphasis are auditable claims, not taste. Position completes the composition: proximity and alignment from the layout system (spacing tokens, grid) back up the type ranks, but never substitute for them — a small gray heading with perfect placement is still unreadable structure.

## 5. Signature Patterns

- **Role-mapping session:** for each screen type, map every text element to one of the 4 roles before styling — orphan elements become decisions, not defaults. The session output is a table (element → role) that review and lint both consume; anything unmapped is a defect, and the mapping doubles as documentation of the screen's intended structure.
- **Squint test:** blur the screen; if the structure is invisible, hierarchy failed — fix levers, not pixels. Practically: apply a `filter: blur(4px)` in devtools or step back from the monitor; if title/heading/body/meta still separate into distinct bands, the levers are working. If everything merges into one texture, the ranks are too close — jump the title at least 2 scale steps and re-test.

## 6. Real-World Use Cases

- **Landing pages where the eye must land on one thing first** — the focal rule makes the hero title the only 2x-step element on the view.
- **Dense dashboards ranking KPIs, labels, and meta consistently** — the exact case where ad-hoc hierarchy collapses and the 4-role set pays for itself.
- **Documentation:** title/heading/body/meta roles across thousands of pages — consistency is the only thing that makes 10,000 pages scannable.

## 7. Combination Notes

### With other typography skills

- **Good with type-scale, line-height, and letter-spacing:** hierarchy is expressed through the scale's roles — the size jumps (`min-2-steps`), the leading bundles, and the display tracking all arrive together; hierarchy without a scale to jump along is just "make it bigger" improvisation.
- **Good with font-pairing and variable-fonts:** weight levers depend on the loaded weight set (a 600 weight that never shipped cannot rank anything), so the emphasis policy is constrained by the pairing's weight budget.
- **Good with readability-legibility and accessible-typography:** every de-ranking decision (secondary color, smaller size) must stay inside those skills' floors — 4.5:1 contrast and the 12px/14px size floors; hierarchy never buys emphasis by spending legibility. On data-dense screens it also meets numeric-tabular (KPIs combine the semibold title rank with tabular figures), and with fluid-responsive the clamps interpolate heading roles while preserving the size *relationships*, so hierarchy holds at every viewport.
- **No caution/avoid list:** hierarchy is the application layer — it consumes everything above it and has no incompatible partners, only screens that bypass the roles (per-screen improvisation, the anti-pattern below).

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and maximalism:** minimalism needs hierarchy more than any other style — with no borders or shadows, size and space do all the ranking. Flat design is similar: type is the primary depth cue. Maximalism relies on strong size+color contrast so dense compositions still scan.
- **Caution with skeuomorphism:** bevels, shadows, and textures add non-typographic depth cues that compete with the size/weight/color levers; hierarchy still works, but the focal point must be coordinated with the styled elements so the type rank and the visual rank do not disagree.

### With motion skills (companion repo skill-animation)

- **Good affinity with entrance-exit:** entrance animations should reveal hierarchy in rank order — title first, then headings, then body — reinforcing the scan pattern instead of shuffling it; the focal rule also names the animation's starting element.
- **Caution beyond that:** motion that re-emphasizes text after load (pulsing, looping weight shifts) creates a second, moving focal point that violates `one-per-view`; once the entrance sequence completes, hierarchy must return to its static ranks.

## 8. Anti-Patterns

- **Everything emphasized** — bold + color + size everywhere leaves nothing emphasized
- **Gray-on-gray de-ranking** — secondary text below 4.5:1 to 'de-emphasize' (fails 1.4.3)
- **Five-plus levels** — hierarchy fragments into noise when every element gets its own treatment
- **Per-screen improvisation** — inventing hierarchy styles per page instead of consuming shared roles

### Accessibility Notes

Hierarchy must survive without color (WCAG 1.4.1) and pass contrast at every rank (1.4.3): a screen whose structure depends on gray shading fails the first, and de-ranking text below 4.5:1 fails the second — which is why the weight-first emphasis policy exists (bold ranks without touching color) and why de-ranking uses the validated `color-text-secondary` alias. Heading structure is also the screen reader's map: h1-h6 markup IS the non-visual hierarchy (see the a11y repo's nav-by-headings guidance), so visual ranks must map onto semantic heading levels rather than restyled divs. The fallback rule is absolute: if visual hierarchy and semantic heading structure conflict, semantic wins — restyle the visuals to match the outline, never re-outline the document to match the styling. Finally, the 4-level cap is itself an accessibility feature: fewer, more distinct ranks are easier to parse for low-vision and cognitive-load-sensitive users than six subtly different treatments.

## 9. Code Examples

### Example 1 — Dashboard card using the 4 hierarchy levels

Tokens: `assets/css/visual-hierarchy.css`

```html
<article class="kpi-card">
  <p class="meta">Monthly active users · updated 2m ago</p>
  <h2 class="title">142,803</h2>
  <p class="body">Up 8.4% versus last month, driven by the onboarding relaunch.</p>
</article>
<script>
  // Squint test: blur the card — structure must still read as meta/title/body.
  function squintTest() {
    document.body.style.filter = "blur(4px)";
    setTimeout(() => (document.body.style.filter = ""), 800);
  }
  console.log("Run squintTest() in console to verify hierarchy survives blur.");
</script>
<style>
  .kpi-card {
    background: #FFFFFF;
    border: 1px solid #E5E5E5;
    border-radius: 8px;
    padding: 20px;
    max-width: 360px;
    font-family: Inter, system-ui, sans-serif;
  }
  .meta {
    /* Rank 4: meta — smallest, validated secondary color */
    margin: 0 0 8px;
    font-size: 0.875rem;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: #525252; /* 7.4:1 on white */
  }
  .title {
    /* Rank 1: title — the single focal element, 2x step above body */
    margin: 0 0 8px;
    font-size: 2.441rem; /* 2xl */
    font-weight: 600;
    line-height: 1.2;
    letter-spacing: -0.01em;
    font-variant-numeric: tabular-nums;
    color: #171717;
  }
  .body {
    /* Rank 3: body — default reading text */
    margin: 0;
    font-size: 1rem;
    line-height: 1.5;
    color: #404040;
  }
</style>
```

### Example 2 — Section stack mapping headings to semantic ranks

Tokens: `assets/css/visual-hierarchy.css`

```html
<section class="doc">
  <h1 class="role-title">Billing settings</h1>
  <h2 class="role-heading">Payment method</h2>
  <p class="role-body">Cards are charged on the first day of each cycle.</p>
  <p class="role-meta">Last reviewed Oct 2026</p>
</section>
<script>
  // Role consistency check: every heading maps to exactly one of the 4 roles.
  const ranks = new Map([
    ["H1", "title"], ["H2", "heading"], ["H3", "heading"],
    ["P", "body"],
  ]);
  document.querySelectorAll("h1, h2, h3, p").forEach((el) => {
    console.assert(
      el.className.startsWith("role-"),
      "Unmapped element breaks role consistency: " + el.tagName
    );
  });
</script>
<style>
  .doc {
    max-width: 66ch;
    font: 16px/1.5 Inter, system-ui, sans-serif;
  }
  .role-title   { font-size: 2.441rem; font-weight: 600; line-height: 1.2; letter-spacing: -0.01em; margin: 0 0 16px; color: #171717; }
  .role-heading { font-size: 1.563rem; font-weight: 600; line-height: 1.25; margin: 24px 0 8px; color: #171717; }
  .role-body    { font-size: 1rem; margin: 0 0 8px; color: #404040; }
  .role-meta    { font-size: 0.875rem; margin: 0; color: #737373; } /* validated secondary alias */
</style>
```

## 10. Implementation Checklist

- [ ] Every screen maps all text elements to one of 4 roles (`--type-text-title/heading/body/meta`) — zero orphan styles.
- [ ] Exactly one element per view uses the strongest treatment (`--type-focal-rule: one-per-view`).
- [ ] Title vs body differs by at least 2 scale steps (`--type-scale-jump-rule`); closer pairs are re-ranked.
- [ ] Inline emphasis follows `--type-emphasis-policy: weight-first` — bold before color before size.
- [ ] De-ranked text uses `--type-secondary-color-alias` and passes 4.5:1 — no arbitrary grays below AA.
- [ ] Visual ranks map onto semantic h1-h6 structure; screen-reader outline matches the visual outline.
- [ ] The squint test (blur) passes on every new screen type before sign-off.
- [ ] Role definitions are identical across screens (`--type-role-consistency`) and lint-checked in CI.

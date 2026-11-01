---
name: minimalism
description: A 'less is more' philosophy where only essential elements remain and white space is an active design component.
tags: [minimal, clean, whitespace]
related: [flat-design, aurora-ui]
---

# UI/UX Skill: Minimalism

## 1. Definition

Minimalism is a design philosophy that emphasizes simplicity: retaining only elements truly essential to function and message, eliminating all superfluous decoration. The core tenet is "Less is more" — every pixel, every word, every color must justify its existence. White space (negative space) is treated as an active design element, not merely empty area.

## 2. Core Design Principles

- **White space is priority one:** generous padding and line-height guide the eye; content density is deliberately low.
- **One focal point per screen:** only one primary action/content is emphasized; everything else assumes a supporting role.
- **Strict grid alignment:** build layouts on an 8pt grid, with perfect alignment; no element should "float" outside the grid.
- **Limited color palette:** maximum 2–3 colors, with a single accent color.
- **Typography as the visual anchor:** hierarchy is created through size and weight, not borders, backgrounds, or icons.
- **Eliminate non-functional decoration:** no decorative shadows, no meaningless gradients, no texture for its own sake; icons are used only when they improve recognition.
- **Concise content:** microcopy is succinct, copy is trimmed to the minimum needed for comprehension.

## 3. Suggested Color Palette

| Role | Hex Code | Notes |
|---|---|---|
| Primary background | `#FFFFFF` | Pure white, clean feel |
| Secondary background | `#F7F7F7` | Very light gray for alternating sections |
| Primary text | `#111111` | Near-absolute black, high contrast |
| Secondary text | `#6B7280` | Medium gray for meta and captions |
| Single accent | `#2563EB` | Blue 600 — used for CTA, links, active states |

**Dark variant:** background `#0A0A0A`, text `#FAFAFA`, accent `#3B82F6`.

## 4. Typography

| Role | Font | Size / Weight |
|---|---|---|
| Header | Inter (or Helvetica Now) | H1: 48–64px / 600–700; H2: 32–40px / 600 |
| Body | Inter (or SF Pro Text) | 16–18px / 400, line-height 1.6 |
| Caption | Inter | 12–14px / 400, secondary color |

Hierarchy is created primarily through **size and weight**, limiting font families to 1–2 maximum.

## 5. Signature Visual Elements

- No heavy borders, no bold shadows; if shadows exist they are extremely subtle (`0 1px 2px rgba(0,0,0,.05)`).
- Border-radius is small or absent (0–8px), and consistent throughout.
- Thin line-style icons (1.5–2px stroke), consistent with typographic weight.
- High-quality images with ample breathing room, no heavy filters.
- Dividers: thin 1px lines or white space alone.

## 6. Real-World Use Cases

- **SaaS / B2B:** dashboards, tech landing pages (Linear, Notion, Stripe style) — minimalism helps users focus on data and tasks.
- **Fintech:** banking apps, e-wallets — minimalism conveys reliability and makes numerical data easy to read.
- **Premium brands / design studios:** portfolio, agency intro pages — minimalism reflects sophistication and expertise.

## 7. Combination Notes

- **Combining with Glassmorphism/Aurora UI:** allow only one effect layer (one gentle gradient block or one frosted panel), keep everything else pure minimal — otherwise the "single focal point" principle breaks.
- **Combining with Neumorphism/Claymorphism:** minimize strictly; if unavoidable, apply only to one component group (e.g., toggles, buttons) to avoid diluting the overall cleanliness.

## 8. Anti-Patterns

- **Removing too much:** stripping away essential elements like navigation labels, progress indicators, or status cues leaves users without the context they need to make decisions.
- **Unintentional imbalance:** excessive whitespace can make layouts feel disconnected, while too little creates visual crowding—white space must serve a purpose, not merely exist.
- **No hierarchy:** without typography or color to establish focal points, users cannot discern what matters most on the screen.
- **Grayscale for the wrong reasons:** avoiding color entirely when a single accent would improve navigation and user experience is a missed opportunity, not a virtue.

### Accessibility Notes

Contrast is computed per the WCAG relative-luminance formula (AA threshold 4.5:1 for body text); values are precomputed in `skills/data.json` → `sections.contrast`.

| Pair | Ratio | WCAG AA (4.5:1) |
|---|---|---|
| body text on primary background: `#111111` on `#FFFFFF` | 18.88:1 | ✅ pass |
| muted/secondary text on primary background: `#6B7280` on `#FFFFFF` | 4.83:1 | ✅ pass |

Both core text pairs pass WCAG AA comfortably. The single accent `#2563EB` carrying white text measures 5.17:1, so it is safe for buttons and links. The main risk is **over-lightening** the secondary gray `#6B7280` (4.83:1 has almost no headroom) — keep it at this value or darker for text under 18px. No motion or transparency is intrinsic to the style, so no reduced-motion handling is required; do keep a visible `:focus-visible` outline, since minimal layouts remove most other affordances.

## 9. Code Examples

### Example 1 — Hero with a single focal point

Tokens: `assets/css/minimalism.css`

```html
<section class="hero">
  <h1>Ship less, mean more</h1>
  <p>One focal point per screen. Everything else supports it.</p>
  <a class="cta" href="/start">Start free</a>
</section>
<style>
.hero {
  max-width: 640px; margin: 0 auto; padding: 96px 32px; /* 8pt-grid multiples */
  background: var(--color-primary-background); /* #FFFFFF */
  color: var(--color-primary-text);            /* #111111 — 18.88:1 */
  font-family: var(--font-body); text-align: center;
}
.hero h1 { font-family: var(--font-heading); font-size: 56px; font-weight: 700;
           line-height: 1.1; letter-spacing: -0.02em; margin: 0 0 16px; }
.hero p  { font-size: 18px; line-height: 1.6; color: var(--color-secondary-text); /* #6B7280 — 4.83:1 */
           margin: 0 0 32px; }
.cta     { display: inline-block; background: var(--color-single-accent); /* #2563EB */
           color: #FFFFFF; padding: 12px 24px; border-radius: 6px;
           font-weight: 600; text-decoration: none; }
.cta:focus-visible { outline: 2px solid var(--color-primary-text); outline-offset: 2px; }
</style>
```

### Example 2 — Quiet data row

Tokens: `assets/css/minimalism.css`

```html
<div class="row">
  <span class="label">Monthly active users</span>
  <strong class="value">48,210</strong>
</div>
<style>
.row { display: flex; justify-content: space-between; align-items: baseline;
       padding: 16px 0; border-bottom: 1px solid #EEEEEE; /* 1px divider, no shadow */
       font-family: var(--font-body); max-width: 480px; }
.value { font-size: 24px; font-weight: 600; color: var(--color-primary-text); }
</style>
```

## 10. Implementation Checklist

- [ ] Body text contrast ≥ 4.5:1 — `#111111` on `#FFFFFF` (18.88:1) and `#6B7280` (4.83:1); never lighten the secondary gray further.
- [ ] Palette stays at 2–3 colors plus a single accent; the accent appears only on interactive elements.
- [ ] All spacing and sizing land on the 8pt grid; no element floats outside the grid.
- [ ] Exactly one focal point per screen — everything else is typographically quieter.
- [ ] Border-radius is 0–8px and identical across all components.
- [ ] Thin 1.5–2px stroke icons; icon weight matches typographic weight.
- [ ] Interactive elements show a visible `:focus-visible` outline and ≥ 44×44px touch targets.

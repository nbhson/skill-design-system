---
name: cards-lists
description: Content containers: card anatomy, list-item patterns, media-object rows, and the whole-card-clickable done accessibly.
tags: [cards, lists, content-containers, media-object, accessibility]
related: [buttons-badges, navigation-patterns, tabs-accordions]
---

# Component Recipe: Cards & Lists

## 1. Definition

Cards and list items are the content containers of every feed, dashboard, and catalog: a card bundles media, title, meta, and actions into one composable unit; a list row does the same in compact form. The recipe covers card anatomy (header/body/media/footer slots), the media-object row pattern, hover/elevation contracts, and the whole-card-clickable pattern done accessibly (one link, stretched, with named actions preserved).

## 2. Core Principles

- **Card anatomy is slotted:** media, title, meta, body, actions — the card component owns slots, content decides what fills them.
- **One action per card, visually primary:** a card may hold multiple actions, but exactly one is the primary link — the card's identity action.
- **Whole-card-clickable without nested links:** the primary link stretches over the card (pseudo-element), while other buttons sit above it (z-index) — no link-in-link markup.
- **Media-object rows for repeating content:** avatar/icon + text + trailing action as one shared pattern (responsive-layout guide 04).
- **Elevation is a state language:** resting cards sit flat (border), hoverable cards lift — elevation changes mean interactivity, nothing else.
- **List rows keep rhythm:** 48–72px row heights, dividers or spacing (never both), and consistent trailing-action alignment.
- **Card grids inherit the layout system:** cards are content; the grid (responsive-layout guides 01/05) decides their geometry.
- **Titles are the semantic anchors:** card titles are headings in context (h2/h3 level in the page outline) — not styled divs.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Card slots | `--comp-card-slots` | media,title,meta,body,actions | Anatomy slot set |
| Card radius | `--comp-card-radius` | 12px | From the radius scale (design-tokens guide 04) |
| Card border (resting) | `--comp-card-border-resting` | 1px solid border-alias | Resting state: border, no shadow |
| Card hover elevation | `--comp-card-hover-elevation` | shadow-2 + translateY(-1px) | Hover lift; motion tokens |
| Card primary link | `--comp-card-primary-link` | stretched-pseudo-element | Whole-card clickable, no nested links |
| Card actions above | `--comp-card-actions-above` | z-above-stretched | Secondary actions stay clickable |
| List row height | `--comp-list-row-height` | 48-72px | Row rhythm by density tier |
| List divider policy | `--comp-list-divider-policy` | divider-or-spacing | Never both |
| Card title semantic | `--comp-card-title-semantic` | heading-in-outline | Titles are real headings in context |
| Card grid owner | `--comp-card-grid-owner` | layout-system | Geometry from responsive-layout, not card CSS |

Consume them by linking `assets/css/cards-lists.css` once at the app root and referencing `var(--comp-card-...)` / `var(--comp-list-...)` from card and list CSS. The tokens encode contracts, not just pixels — if a card ships without `--comp-card-primary-link` or `--comp-card-actions-above` wired, the whole-card-clickable pattern is not implemented, only drawn.

## 4. Composition

- **Composes with responsive-layout guides 04/05:** media-object and grid geometry are shared contracts — the card declares its slots, the layout decides width, column count, and gutters, and card CSS never sets its own grid geometry.
- **Composes with buttons-badges:** card actions consume the button/badge contract, so every action inside a card is a real button or link from that recipe, not a restyled span.
- **Composes with skill-ui-ux styles:** card styling (radius, elevation, borders) is where design styles surface most — styleAffinity records the lean, and style overrides land in the slot styling, never in the anatomy.

## 5. Signature Patterns

- **Card component with anatomy slots:** one card primitive; products compose media/title/actions into catalog, dashboard, and feed variants. The primitive defines the slot seams; variants only fill them, so a new surface is markup, not a forked card.
- **Stretched-link recipe:** primary link with `::after` covering the card; interactive children raise above it — accessible whole-card clicking without nested links. The pseudo-element carries the hit area, the z-index contract keeps secondary actions clickable, and screen readers hear exactly one link with one name.

## 6. Real-World Use Cases

- **Feeds, catalogs, and dashboards** — every product has a card somewhere; these are the three surfaces where the anatomy pays for itself first.
- **Notification lists, search results, and settings groups** as list rows, where the 48–72px rhythm and trailing-action alignment keep scanning cheap.
- **Audit** — nested interactive markup, hover-only affordances, styled-div titles: the three findings this recipe's checklist exists to catch.

## 7. Combination Notes

### With other component-recipe skills

- **Good with buttons-badges:** card actions are real buttons and links from that recipe — the card owns placement, the button recipe owns appearance and states.
- **Good with toasts-notifications, empty-loading-error, and tables-data-grid:** lists and grids hand off naturally — an empty list renders the empty-state recipe in the same container, and table rows needing richness graduate to card rows without a new contract.
- **Good with navigation-patterns, tabs-accordions, dropdowns-menus, modals-dialogs, command-palette, forms-inputs:** cards routinely host these widgets in their action or body slots; because the card is slotted, each widget arrives with its own contract intact.
- **Good with accessibility-wiring:** the stretched-link recipe is an accessibility contract first — wiring validates exactly one primary link and zero nested interactives per card.
- **No caution or avoid list:** cards are pure containers; as long as slots consume sibling recipes rather than re-implement them, nothing conflicts.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism, flat-design, and glassmorphism:** cards are the primary canvas of all three — minimalism lives in the border/resting state, flat-design in the no-shadow hover contract, glassmorphism in surface treatments that slot styling absorbs without touching anatomy.
- **Good affinity with neumorphism:** the soft-extrusion look maps cleanly onto `--comp-card-border-resting` and the hover elevation token, with elevation still reserved for interactive cards only.
- **Caution with brutalism-ui:** hard edges, raw borders, and deliberate rejection of lift can fight the resting/hover elevation contract; if the style wants zero hover feedback, keep the border-color or outline change so interactivity remains visible — do not delete the state language entirely.

### With motion skills (companion repo skill-animation)

- **Good affinity with entrance-exit:** card grids are the canonical staggered-entrance surface; the entrance animates the container while the hover lift token stays independent, so list virtualization does not fight the motion.
- **Good affinity with micro-interactions:** the `translateY(-1px)` hover lift and its motion tokens are exactly the scale micro-interactions governs — short, interruptible, and never blocking the click target.

## 8. Anti-Patterns

- **Link-in-link markup** — a whole clickable card containing buttons - invalid HTML, broken AT
- **Everything-lifts** — elevation on static cards until lift means nothing
- **Divider-and-spacing** — double separation reading as heavy-handed noise
- **Styled-div titles** — card titles outside the page heading outline

### Accessibility Notes

Cards are a hot spot for 1.3.1/2.4.4/4.1.2: single-link semantics (stretched pattern), real headings, and named actions — the stretched-link recipe exists specifically to make whole-card clicking compatible with AT. In practice that means the primary link is the only element whose hit area expands, every secondary action remains a real button layered above the stretched pseudo-element, and card titles are headings at the correct level in the page outline so screen-reader users can navigate the feed by heading. The fallback rule: if the stretched pattern is unavailable, make only the title a link with a clearly-sized hit area — a smaller clickable is better than invalid nesting.

## 9. Code Examples

### Example 1 — Card grid with anatomy slots

Tokens: `assets/css/cards-lists.css`

```html
<div class="card-grid">
  <article class="card">
    <div class="card-media"><img src="thumb.png" alt="" width="320" height="180"></div>
    <div class="card-body">
      <h3 class="card-title">Quarterly design review</h3>
      <p class="card-meta">Updated Nov 1 · 12 pages</p>
      <p class="card-text">Summary of decisions and open questions.</p>
    </div>
    <div class="card-actions">
      <button class="btn-secondary" type="button">Share</button>
    </div>
  </article>
</div>
<style>
  /* Grid geometry comes from the layout system, not the card */
  .card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
    gap: var(--comp-list-row-height, 24px);
  }
  .card {
    display: flex;              /* slots stack vertically */
    flex-direction: column;
    background: #fff;
    border: var(--comp-card-border-resting);
    border-radius: var(--comp-card-radius);
    overflow: hidden;           /* media clips to the radius */
  }
  .card:hover { box-shadow: var(--comp-card-hover-elevation); } /* lift = interactive */
  .card-media img { display: block; width: 100%; height: auto; }
  .card-body    { padding: 16px; display: grid; gap: 4px; }
  .card-title   { margin: 0; font: 600 16px/1.3 Inter, system-ui, sans-serif; } /* h3 = real heading in outline */
  .card-meta    { margin: 0; font: 13px/1.4 Inter, system-ui, sans-serif; color: #737373; }
  .card-text    { margin: 0; font: 14px/1.5 Inter, system-ui, sans-serif; color: #404040; }
  .card-actions { padding: 0 16px 16px; display: flex; justify-content: flex-end; }
</style>
```

### Example 2 — Whole-card-clickable stretched link

Tokens: `assets/css/cards-lists.css`

```html
<article class="card card-linked">
  <h3 class="card-title"><a class="card-link" href="/projects/4821">Project Aurora</a></h3>
  <p class="card-meta">Last deployed 14:02 · passing</p>
  <div class="card-actions">
    <button class="btn-secondary" type="button">Settings</button>
    <button class="btn-secondary" type="button">Share</button>
  </div>
</article>
<style>
  .card {
    position: relative;                 /* anchor for the stretched link */
    max-width: 380px; padding: 16px;
    border: var(--comp-card-border-resting);
    border-radius: var(--comp-card-radius);
    transition: transform 150ms ease, box-shadow 150ms ease;
  }
  .card:hover {
    transform: translateY(-1px);        /* --comp-card-hover-elevation */
    box-shadow: var(--comp-card-hover-elevation);
  }
  .card-title { margin: 0 0 4px; font: 600 16px/1.3 Inter, system-ui, sans-serif; }
  .card-meta  { margin: 0 0 12px; font: 13px/1.4 Inter, system-ui, sans-serif; color: #737373; }
  /* Stretched link: one link, whole-card hit area, zero nested interactives */
  .card-link::after {
    content: "";
    position: absolute;
    inset: 0;                           /* covers the entire card */
    border-radius: inherit;
  }
  .card-link { color: #1D4ED8; text-decoration: none; }
  .card-link:hover { text-decoration: underline; }
  .card-link:focus-visible { outline: 2px solid #1D4ED8; outline-offset: 2px; }
  /* Secondary actions rise above the stretched pseudo-element */
  .card-actions { position: relative; z-index: 1; display: flex; gap: 8px; }</style>
```

## 10. Implementation Checklist

- [ ] Every card declares the slot anatomy (`--comp-card-slots`) and fills slots with content — no bespoke one-off card markup.
- [ ] Resting cards use `var(--comp-card-border-resting)` with no shadow; only interactive cards lift via `var(--comp-card-hover-elevation)`.
- [ ] Each card has exactly one primary link implementing the stretched pattern (`--comp-card-primary-link`), with no link-in-link markup anywhere.
- [ ] Secondary actions sit above the stretched link (`--comp-card-actions-above`) and remain fully clickable.
- [ ] List rows keep the 48–72px rhythm (`--comp-list-row-height`) with dividers or spacing — never both (`--comp-list-divider-policy`).
- [ ] Card titles are real headings in the page outline (`--comp-card-title-semantic`), not styled divs.
- [ ] Card grids get geometry from the layout system (`--comp-card-grid-owner`); card CSS sets no grid columns.
- [ ] Audit sweeps pass: no nested interactive markup, no hover-only affordances, no orphaned action buttons outside the button contract.

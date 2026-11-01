# 📐 Professional Responsive Layout Skill Set — 12 Layout Disciplines

A professional reference guide for 12 responsive-layout disciplines, each covering: definition, core principles, spec tokens (policies/thresholds/contracts), composition, signature patterns, real-world applications, combination notes, anti-patterns, accessibility notes, code examples, and an implementation checklist.

Companion repos: **skill-ui-ux** (12 design styles), **skill-animation** (12 motion disciplines), **skill-design-tokens** (12 token disciplines). This repo answers *"does it work at every width?"* — the layout layer every other skill renders inside. Every skill declares a `styleAffinity` mapping to skill-ui-ux style ids and a `motionAffinity` mapping to skill-animation discipline ids.

## 📂 Skill List

| # | Skill | Folder | Summary |
|---|-------|--------|---------|
| 1 | [Grid Systems](./skills/01-grid-systems/SKILL.md) | 01-grid-systems | Column grids, gutters, and content max-widths: the alignment skeleton every layout composes on, from 12-col desktop to single-column mobile. |
| 2 | [Breakpoints Strategy](./skills/02-breakpoints-strategy/SKILL.md) | 02-breakpoints-strategy | Content-driven breakpoints (not device names): a small tier set, mobile-first queries, and when container queries replace them. |
| 3 | [Fluid Layout & Container Queries](./skills/03-fluid-container-queries/SKILL.md) | 03-fluid-container-queries | Components that adapt to their container, not the viewport: container queries, cqi units, and fluid spacing/type between bounds. |
| 4 | [Flexbox Patterns](./skills/04-flexbox-patterns/SKILL.md) | 04-flexbox-patterns | One-dimensional layout patterns: nav bars, media objects, toolbars, and the alignment/gap idioms that solve 80% of component layout. |
| 5 | [CSS Grid Patterns](./skills/05-css-grid-patterns/SKILL.md) | 05-css-grid-patterns | Two-dimensional layout: page shells, card grids with auto-fit, named areas, and subgrid - the patterns that replaced framework grids. |
| 6 | [Named Layout Compositions](./skills/06-layout-compositions/SKILL.md) | 06-layout-compositions | The catalog: sidebar, split, stack, cluster, bento, holy-grail - named, token-driven compositions instead of re-solved layout problems. |
| 7 | [Responsive Images & Media](./skills/07-responsive-images/SKILL.md) | 07-responsive-images | srcset/sizes, art direction, modern formats, and lazy loading: images that ship the right bytes for every slot and bandwidth. |
| 8 | [Mobile Navigation](./skills/08-mobile-navigation/SKILL.md) | 08-mobile-navigation | Bottom bars, drawers, and the thumb zone: navigation patterns that work at 360px with one thumb - and when to collapse what. |
| 9 | [Responsive Data Tables](./skills/09-data-tables-responsive/SKILL.md) | 09-data-tables-responsive | Tables that survive narrow screens: priority columns, card fallback, sticky headers, and horizontal scroll done honestly. |
| 10 | [Intrinsic Layout](./skills/10-intrinsic-design/SKILL.md) | 10-intrinsic-design | Layouts from content, not viewport: min/max/clamp sizing, aspect-ratio, and the Every-Layout approach that needs fewer breakpoints. |
| 11 | [RTL & i18n Layout](./skills/11-rtl-i18n-layout/SKILL.md) | 11-rtl-i18n-layout | Layouts that flip, reflow, and re-text for every locale: logical properties, RTL mirroring, text expansion, and internationalization-safe responsive design. |
| 12 | [Responsive Testing & QA](./skills/12-responsive-testing/SKILL.md) | 12-responsive-testing | The verification layer: viewport test matrix, visual regression, real-device checks, and zoom/RTL/locale passes that prove layouts work. |

## 🤖 Machine-Readable Data / AI Agents

[`data.json`](./skills/data.json) — the full skill set as structured JSON (definitions, principles, spec tokens, composition, patterns, use cases, combinations, style/motion affinity, anti-patterns, accessibility contracts). The root [`SKILL.md`](./SKILL.md) acts as a router for AI agents.

```json
{
  "skills": [{
    "id": "css-grid-patterns",
    "sections": {
      "tokens": [{ "role": "grid-card-template", "value": "repeat(auto-fill, minmax(240px, 1fr))", "notes": "..." }],
      "combinations": { "good": [], "caution": [], "avoid": [] },
      "styleAffinity": { "good": [], "caution": [], "avoid": [] },
      "motionAffinity": { "good": [], "caution": [], "avoid": [] },
      "antiPatterns": ["..."],
      "accessibility": { "required": true, "notes": "...", "fallback": "..." }
    }
  }]
}
```

## 📚 References

[`assets/references.md`](./skills/assets/references.md) — curated spec links (CSS Grid, container queries, logical properties), tool docs (Every Layout, Utopia, visual regression), and responsive testing resources.

## 🎯 How to Use

1. **Select a discipline:** use the summary table to pick the skill that matches the layout task.
2. **Read SKILL.md:** each guide follows the 10-section standard (definition → principles → tokens → composition → patterns → applications → combinations → anti-patterns → code examples → checklist).
3. **Apply:** treat the spec tokens from `assets/css/<skill-id>.css` as hard standards — one grid, few tiers, gap from the spacing scale. For AI agents: use the root `SKILL.md` router, then the specific guide.

## 🔄 Quick Combination Matrix

Symbols: ✅ combines well · ⚠️ conditional — follow the pairing tips in section 7 · ❌ do not combine.

| | grid | tiers | cq | flex | gridpat | comp | images | mobnav | tables | intrinsic | rtl | test |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Grid Systems** | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| **Breakpoints Strategy** | ✅ | — | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ | ✅ |
| **Fluid Layout & Container Queries** | ✅ | ⚠️ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Flexbox Patterns** | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **CSS Grid Patterns** | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Named Layout Compositions** | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Responsive Images & Media** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Mobile Navigation** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ |
| **Responsive Data Tables** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ |
| **Intrinsic Layout** | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| **RTL & i18n Layout** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ |
| **Responsive Testing & QA** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |

## 🧭 Design Style Affinity (skill-ui-ux / skill-design-tokens)

| Skill | Styles it elevates | Styles it clashes with |
|---|---|---|
| Grid Systems | minimalism, flat-design, class-morphism | collage-art |
| Breakpoints Strategy | minimalism, flat-design | collage-art, maximalism |
| Fluid Layout & Container Queries | minimalism, flat-design, maximalism | collage-art |
| Flexbox Patterns | minimalism, flat-design | collage-art |
| CSS Grid Patterns | minimalism, flat-design, maximalism | — |
| Named Layout Compositions | minimalism, flat-design, maximalism | — |
| Responsive Images & Media | minimalism, flat-design, collage-art | — |
| Mobile Navigation | minimalism, flat-design, glassmorphism | skeuomorphism |
| Responsive Data Tables | minimalism, flat-design, class-morphism | collage-art |
| Intrinsic Layout | minimalism, flat-design, class-morphism | collage-art, maximalism |
| RTL & i18n Layout | minimalism, flat-design | collage-art, brutalism-ui |
| Responsive Testing & QA | minimalism, flat-design, class-morphism | — |

## 🏃 Motion Affinity (skill-animation)

| Skill | Motion it pairs with | Motion to handle with care |
|---|---|---|
| Grid Systems | entrance-exit | — |
| Breakpoints Strategy | easing-timing | — |
| Fluid Layout & Container Queries | easing-timing | — |
| Flexbox Patterns | scroll-animation | — |
| CSS Grid Patterns | entrance-exit | — |
| Named Layout Compositions | page-transitions, entrance-exit | — |
| Responsive Images & Media | scroll-animation | — |
| Mobile Navigation | page-transitions, feedback-confirmation | — |
| Responsive Data Tables | easing-timing | data-animation |
| Intrinsic Layout | easing-timing | — |
| RTL & i18n Layout | page-transitions, easing-timing | scroll-animation |
| Responsive Testing & QA | easing-timing | — |

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12
- **Token prefix:** `--layout-*` (CSS custom properties; see `assets/css/`)
- **CI:** `python3 scripts/validate_skills.py` — 10 checks covering guides, data.json, CSS files, README matrix, and repo hygiene

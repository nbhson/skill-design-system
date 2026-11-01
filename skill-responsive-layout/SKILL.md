---
name: responsive-layout
description: Professional responsive layout skill guide covering 12 disciplines (grid systems, breakpoints strategy, fluid layout & container queries, flexbox patterns, CSS grid patterns, named layout compositions, responsive images, mobile navigation, responsive data tables, intrinsic layout, RTL & i18n layout, responsive testing & QA). Use when building responsive pages or app shells, adapting components to any width, fixing overflow/CLS, or auditing layouts across viewports, zoom levels, and locales.
---

# Responsive Layout — Skill Router

This skill provides 12 curated responsive-layout discipline guides. Each guide covers definition, core principles, spec tokens (policies/thresholds/contracts), composition, signature patterns, real-world use cases, combination notes, anti-patterns, code examples, and an implementation checklist.

## Step 1 — Choose a discipline

Match the layout task to a discipline:

| Discipline | Best for | Avoid for |
|---|---|---|
| Grid Systems | The 12-col alignment skeleton + max-widths | Component-internal layout (→ flexbox) |
| Breakpoints Strategy | Few, content-driven viewport tiers | Device-named breakpoint soup |
| Fluid Layout & Container Queries | Components adapting to their slot | Page-shell chrome decisions |
| Flexbox Patterns | One-dimensional component layout | Two-dimensional page scaffolding |
| CSS Grid Patterns | Page shells, card grids, named areas | One-dimensional rows (→ flexbox) |
| Named Layout Compositions | Reusable sidebar/split/stack/bento | Bespoke per-page layout CSS |
| Responsive Images & Media | srcset, formats, lazy, zero-CLS | Decorative handling of hero bytes |
| Mobile Navigation | Bottom bars, drawers, thumb zone | Desktop nav squeezed onto phones |
| Responsive Data Tables | Priority columns, honest scroll, cards | Comparison tables stacked as cards |
| Intrinsic Layout | Content-driven sizing, fewer queries | Fixed-tier token governance surfaces |
| RTL & i18n Layout | Logical properties, mirroring, expansion | English-only layout assumptions |
| Responsive Testing & QA | Viewport matrix, visual regression, zoom | Two-width sign-offs |

If the user names a task explicitly ("sidebar collapses into a drawer", "table overflows on mobile"), go straight to its guide. If the task is "build a responsive page", start with **grid-systems** + **breakpoints-strategy**, then pull patterns as needed.

## Step 2 — Read the discipline guide

Each guide lives in `skills/<NN-<skill>>/SKILL.md` and follows a 10-section standard:

1. Definition — core concept in 2–3 sentences
2. Core Principles — mandatory rules
3. Spec Tokens — policy/threshold/contract values + role of each
4. Composition — how the skill pairs with siblings and companion repos
5. Signature Patterns — the 2–3 canonical implementation patterns
6. Real-World Use Cases — suitable products/contexts
7. Combination Notes — pairing with sibling skills + affinity to skill-ui-ux / skill-animation / skill-design-tokens
8. Anti-Patterns — common mistakes (incl. Accessibility Notes)
9. Code Examples — complete HTML+CSS (±JS) snippets using the spec tokens
10. Implementation Checklist — pre-delivery quality checks

| # | Discipline | Guide |
|---|-----------|-------|
| 1 | Grid Systems | [skills/01-grid-systems/SKILL.md](./skills/01-grid-systems/SKILL.md) |
| 2 | Breakpoints Strategy | [skills/02-breakpoints-strategy/SKILL.md](./skills/02-breakpoints-strategy/SKILL.md) |
| 3 | Fluid Layout & Container Queries | [skills/03-fluid-container-queries/SKILL.md](./skills/03-fluid-container-queries/SKILL.md) |
| 4 | Flexbox Patterns | [skills/04-flexbox-patterns/SKILL.md](./skills/04-flexbox-patterns/SKILL.md) |
| 5 | CSS Grid Patterns | [skills/05-css-grid-patterns/SKILL.md](./skills/05-css-grid-patterns/SKILL.md) |
| 6 | Named Layout Compositions | [skills/06-layout-compositions/SKILL.md](./skills/06-layout-compositions/SKILL.md) |
| 7 | Responsive Images & Media | [skills/07-responsive-images/SKILL.md](./skills/07-responsive-images/SKILL.md) |
| 8 | Mobile Navigation | [skills/08-mobile-navigation/SKILL.md](./skills/08-mobile-navigation/SKILL.md) |
| 9 | Responsive Data Tables | [skills/09-data-tables-responsive/SKILL.md](./skills/09-data-tables-responsive/SKILL.md) |
| 10 | Intrinsic Layout | [skills/10-intrinsic-design/SKILL.md](./skills/10-intrinsic-design/SKILL.md) |
| 11 | RTL & i18n Layout | [skills/11-rtl-i18n-layout/SKILL.md](./skills/11-rtl-i18n-layout/SKILL.md) |
| 12 | Responsive Testing & QA | [skills/12-responsive-testing/SKILL.md](./skills/12-responsive-testing/SKILL.md) |

## Step 3 — Apply

- Treat the spec tokens as **hard standards**: one grid definition, few named tiers, gap values from the spacing scale - off-grid values are violations.
- Respect the **ownership split**: media queries own the page shell; container queries own components - never both on the same decision.
- ALWAYS honor the guide's **Accessibility Notes**: DOM order = visual order, zoom/reflow floors (WCAG 1.4.4/1.4.10), and 44px touch targets are layout contracts, not polish.
- Check the **Combination Matrix** in [README.md](./README.md) before pairing disciplines: ✅ combines well, ⚠️ conditional, ❌ do not combine.
- When the task also involves visual style, motion, or tokens, consult companions **skill-ui-ux**, **skill-animation**, and **skill-design-tokens** via the guides' affinity notes.

## Machine-Readable Data

For programmatic use (layout linting, CI wiring, AI agents), read [`skills/data.json`](./skills/data.json) — all 12 disciplines as structured JSON with a fully symmetric combination matrix, affinity mappings, and per-skill accessibility contracts:

```json
{ "skills": [{ "id": "css-grid-patterns", "sections": { "tokens": [...], "combinations": {...}, "antiPatterns": [...], "accessibility": { "required": true, "notes": "...", "fallback": "..." } } }] }
```

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12 (duyệt `skills/*/SKILL.md` hoặc `data.json` → `skills[].id`)
- **Compatibility:** framework-agnostic — spec tokens ở `assets/css/` dùng CSS custom properties chuẩn (`--layout-*`); container queries Baseline 2023; sinh lại tokens bằng `scripts/generate_css_tokens.py`
- **Companion repos:** skill-ui-ux (12 design styles) — `sections.styleAffinity`; skill-animation (12 motion disciplines) — `sections.motionAffinity`; skill-design-tokens (12 token disciplines) — spacing/margin/gutter contracts

Khi thay đổi cấu trúc `data.json` (thêm/xóa section), tăng `meta.version` và cập nhật section này.

## References & Inspiration

Curated spec links, tool documentation, and inspiration sources: [`skills/assets/references.md`](./skills/assets/references.md).

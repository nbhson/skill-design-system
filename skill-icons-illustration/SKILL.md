---
name: icons-illustration
description: Professional icon & illustration skill guide covering 12 disciplines (icon style selection, icon grid & sizing, library management, icon usability, accessible icons, illustration direction, empty & error illustrations, mascot & character design, SVG optimization, animation integration, favicons & app icons, system audit). Use when building icon systems, choosing illustration direction, optimizing SVGs, or auditing visual assets.
---

# Icons & Illustration — Skill Router

This skill provides 12 curated visual-asset guides. Each guide covers definition, core principles, spec tokens (policies/budgets/contracts), composition, signature patterns, real-world use cases, combination notes, anti-patterns, code examples, and an implementation checklist.

## Step 1 — Choose a discipline

Match the asset task to a discipline:

| Discipline | Best for | Avoid for |
|---|---|---|
| Icon Style Selection | Filled vs outline, stroke, corner language | Style salad in one toolbar |
| Icon Grid & Sizing | 24px grid, keylines, size ramp, pixel snap | Blurry 1x strokes |
| Icon Library Management | Naming, pipeline, versioning, pruning | Hand-copied SVG drift |
| Icon Usability | Recognition, labels, 44px targets | Mystery meat icons |
| Accessible Icons | aria names, hidden decoration, contrast | Unnamed icon buttons |
| Illustration Direction | Purpose matrix, style spec, consistency | Purposeless decoration |
| Empty & Error Illustrations | The state slots: mood + copy + action | Mocking error art |
| Mascot & Character Design | Character systems, restraint | Mascot overexposure |
| SVG Optimization | SVGO, currentColor, budgets | 400KB icons |
| Icon & Illustration Animation | Draw-ins, Lottie, reduced-motion | Motion everywhere |
| Favicons & App Icons | Modern minimal set, maskable, PWA | Maskable crop casualties |
| Icon & Illustration System Audit | Consistency, a11y sweep, weight | Audit theater |

If the user names an asset task explicitly ("our icons are inconsistent", "optimize the SVGs"), go straight to its guide. If the task is "stand up the visual-asset layer", start with **icon-style-selection** + **icon-grid-sizing**, then **icon-library-management** for the pipeline.

## Step 2 — Read the discipline guide

Each guide lives in `skills/<NN-<skill>>/SKILL.md` and follows a 10-section standard:

1. Definition — core concept in 2–3 sentences
2. Core Principles — mandatory rules
3. Spec Tokens — policy/budget/contract values + role of each
4. Composition — how the skill pairs with siblings and companion repos
5. Signature Patterns — the 2–3 canonical implementation patterns
6. Real-World Use Cases — suitable products/contexts
7. Combination Notes — pairing with sibling skills + affinity to skill-ui-ux / skill-animation / skill-design-tokens
8. Anti-Patterns — common mistakes (incl. Accessibility Notes)
9. Code Examples — complete HTML+CSS (±JS) snippets using the spec tokens
10. Implementation Checklist — pre-delivery quality checks

| # | Discipline | Guide |
|---|-----------|-------|
| 1 | Icon Style Selection | [skills/01-icon-style-selection/SKILL.md](./skills/01-icon-style-selection/SKILL.md) |
| 2 | Icon Grid & Sizing | [skills/02-icon-grid-sizing/SKILL.md](./skills/02-icon-grid-sizing/SKILL.md) |
| 3 | Icon Library Management | [skills/03-icon-library-management/SKILL.md](./skills/03-icon-library-management/SKILL.md) |
| 4 | Icon Usability | [skills/04-icon-usability/SKILL.md](./skills/04-icon-usability/SKILL.md) |
| 5 | Accessible Icons | [skills/05-accessible-icons/SKILL.md](./skills/05-accessible-icons/SKILL.md) |
| 6 | Illustration Direction | [skills/06-illustration-direction/SKILL.md](./skills/06-illustration-direction/SKILL.md) |
| 7 | Empty & Error Illustrations | [skills/07-empty-error-illustrations/SKILL.md](./skills/07-empty-error-illustrations/SKILL.md) |
| 8 | Mascot & Character Design | [skills/08-mascot-character/SKILL.md](./skills/08-mascot-character/SKILL.md) |
| 9 | SVG Optimization | [skills/09-svg-optimization/SKILL.md](./skills/09-svg-optimization/SKILL.md) |
| 10 | Icon & Illustration Animation | [skills/10-animation-integration/SKILL.md](./skills/10-animation-integration/SKILL.md) |
| 11 | Favicons & App Icons | [skills/11-favicon-app-icons/SKILL.md](./skills/11-favicon-app-icons/SKILL.md) |
| 12 | Icon & Illustration System Audit | [skills/12-icon-system-audit/SKILL.md](./skills/12-icon-system-audit/SKILL.md) |

## Step 3 — Apply

- Treat the spec tokens as **hard standards**: one style family, grid discipline, weight budgets, and the aria contract - visual assets are engineered, not dropped in.
- Respect the **functional/decorative rule**: every icon instance is classified - functional icons carry accessible names; decorative icons are hidden. Never an unnamed interactive icon.
- ALWAYS honor the guide's **Accessibility Notes**: names, contrast (1.4.11), target sizes (2.5.8), and reduced-motion fallbacks are asset contracts, not polish.
- Check the **Combination Matrix** in [README.md](./README.md) before pairing disciplines: ✅ combines well, ⚠️ conditional, ❌ do not combine.
- When the task also involves components, copy, or motion, consult companions **skill-component-recipes**, **skill-ux-writing**, and **skill-animation** via the guides' affinity notes.

## Machine-Readable Data

For programmatic use (asset linting, CI wiring, AI agents), read [`skills/data.json`](./skills/data.json) — all 12 disciplines as structured JSON with a fully symmetric combination matrix, affinity mappings, and per-skill accessibility contracts:

```json
{ "skills": [{ "id": "accessible-icons", "sections": { "tokens": [...], "combinations": {...}, "antiPatterns": [...], "accessibility": { "required": true, "notes": "...", "fallback": "..." } } }] }
```

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12 (duyệt `skills/*/SKILL.md` hoặc `data.json` → `skills[].id`)
- **Compatibility:** framework-agnostic — spec tokens ở `assets/css/` dùng CSS custom properties chuẩn (`--icon-*`); sinh lại tokens bằng `scripts/generate_css_tokens.py`
- **Companion repos:** skill-ui-ux (12 design styles) — `sections.styleAffinity`; skill-animation (12 motion disciplines) — `sections.motionAffinity`; skill-design-tokens (12 token disciplines) — color/spacing/radius contracts; skill-ux-writing — empty/error copy pairing

Khi thay đổi cấu trúc `data.json` (thêm/xóa section), tăng `meta.version` và cập nhật section này.

## References & Inspiration

Curated spec links, tool documentation, and inspiration sources: [`skills/assets/references.md`](./skills/assets/references.md).

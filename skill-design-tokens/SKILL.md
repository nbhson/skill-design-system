---
name: design-tokens
description: Professional design token skill guide covering 12 token disciplines (color scales, typography, spacing & sizing, radius & elevation, semantic alias naming, dark mode, multi-brand theming, contrast validation, cross-platform mapping, token pipeline & Figma sync, component tokens, governance & migration). Use when defining, consuming, reviewing, or migrating design tokens, building themes (dark mode, brands, density), or auditing a codebase for token coverage and WCAG contrast.
---

# Design Tokens — Skill Router

This skill provides 12 curated token-discipline guides. Each guide covers definition, core principles, token set (role/value/notes), composition & layering, signature patterns, real-world use cases, combination notes, anti-patterns, accessibility contract, code examples, and an implementation checklist.

## Step 1 — Choose a discipline

Match the token task to a discipline:

| Discipline | Best for | Avoid for |
|---|---|---|
| Color Token Scales | Building primitive color ramps (50–950) | Deciding where a color is used (→ alias naming) |
| Typography Token System | Font families, type scale, weights, line-height | Choosing fonts per screen (ad-hoc) |
| Spacing & Sizing | 4px-base spacing scale, icon sizes, touch targets | One-off layout tweaks |
| Radius & Elevation | Corner steps, shadow levels, z-index layers | Decorative one-off shadows |
| Semantic & Alias Naming | The 3-tier architecture (primitive → alias → component) | Renaming without deprecation |
| Dark Mode Theming | Light/dark re-mapping of aliases | Inverting colors with filters |
| Multi-Brand Theming | White-label alias overrides, brand matrix | Per-brand component forks |
| Contrast Validation | WCAG 1.4.3/1.4.11/2.4.13 as CI gates | Spot-checking contrast by eye |
| Cross-Platform Mapping | CSS/iOS/Android/Tailwind codegen contracts | Hand-synced platform files |
| Token Pipeline & Figma Sync | DTCG format, Figma variables → code | Screenshot-driven sync |
| Component Tokens | Component styling slots derived from aliases | Exposing every CSS property |
| Governance & Migration | Review, semver, deprecation, lint, adoption | "Move fast" token changes |

If the user names a task explicitly (e.g. "dark mode", "spacing scale", "brand theming"), go straight to its guide. If the task is "set up tokens for X", start with **semantic-alias-naming** (the architecture), then pull in the domain guides it needs.

## Step 2 — Read the discipline guide

Each guide lives in `skills/<NN-<skill>>/SKILL.md` and follows a 10-section standard:

1. Definition — core concept in 2–3 sentences
2. Core Token Principles — mandatory rules
3. Token Set — role/value/notes table (the legal values)
4. Composition & Layering — how the tier composes with others
5. Signature Patterns — the 2–3 canonical implementation patterns
6. Real-World Use Cases — suitable products/contexts
7. Combination Notes — pairing with sibling skills + style affinity (skill-ui-ux) + motion affinity (skill-animation)
8. Anti-Patterns — common mistakes (incl. Accessibility Notes)
9. Code Examples — complete HTML+CSS (±JS) snippets using the skill's tokens
10. Implementation Checklist — pre-delivery quality checks

| # | Discipline | Guide |
|---|-----------|-------|
| 1 | Color Token Scales | [skills/01-color-tokens/SKILL.md](./skills/01-color-tokens/SKILL.md) |
| 2 | Typography Token System | [skills/02-typography-tokens/SKILL.md](./skills/02-typography-tokens/SKILL.md) |
| 3 | Spacing & Sizing Tokens | [skills/03-spacing-sizing/SKILL.md](./skills/03-spacing-sizing/SKILL.md) |
| 4 | Radius & Elevation | [skills/04-radius-elevation/SKILL.md](./skills/04-radius-elevation/SKILL.md) |
| 5 | Semantic & Alias Naming | [skills/05-semantic-alias-naming/SKILL.md](./skills/05-semantic-alias-naming/SKILL.md) |
| 6 | Dark Mode Theming | [skills/06-dark-mode/SKILL.md](./skills/06-dark-mode/SKILL.md) |
| 7 | Multi-Brand Theming | [skills/07-multi-brand-theming/SKILL.md](./skills/07-multi-brand-theming/SKILL.md) |
| 8 | Contrast Validation | [skills/08-contrast-validation/SKILL.md](./skills/08-contrast-validation/SKILL.md) |
| 9 | Cross-Platform Mapping | [skills/09-platform-mapping/SKILL.md](./skills/09-platform-mapping/SKILL.md) |
| 10 | Token Pipeline & Figma Sync | [skills/10-token-pipeline-figma/SKILL.md](./skills/10-token-pipeline-figma/SKILL.md) |
| 11 | Component Tokens | [skills/11-component-tokens/SKILL.md](./skills/11-component-tokens/SKILL.md) |
| 12 | Governance & Migration | [skills/12-governance-migration/SKILL.md](./skills/12-governance-migration/SKILL.md) |

## Step 3 — Apply

- Treat the token tables as **hard standards**: components consume `var(--dt-*)` aliases — raw hexes, px spacing, and ad-hoc shadows are build failures, not style nits.
- Respect the **three-tier direction**: primitive → semantic alias → component. Nothing references downward or sideways.
- ALWAYS honor the guide's **Accessibility Notes** (section 8) and the global contrast contract in `skills/08-contrast-validation/SKILL.md`: pairings pass WCAG 1.4.3 / 1.4.11 / 2.4.13 in every theme cell.
- Check the **Combination Matrix** in [README.md](./README.md) before pairing two disciplines: ✅ combines well, ⚠️ conditional (follow section 7 tips), ❌ do not combine.
- When the task also involves visual style or motion, consult the companion repos **skill-ui-ux** (12 design styles) and **skill-animation** (12 motion disciplines) via the guides' `styleAffinity` / `motionAffinity` notes.

## Machine-Readable Data

For programmatic use (token linting, codegen, AI agents), read [`skills/data.json`](./skills/data.json) — all 12 disciplines as structured JSON with a fully symmetric combination matrix, style affinity to skill-ui-ux, motion affinity to skill-animation, and a per-skill accessibility contract:

```json
{ "skills": [{ "id": "color-tokens", "sections": { "tokens": [...], "combinations": {...}, "antiPatterns": [...], "accessibility": { "required": true, "notes": "...", "fallback": "..." } } }] }
```

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12 (duyệt `skills/*/SKILL.md` hoặc `data.json` → `skills[].id`)
- **Compatibility:** framework-agnostic — CSS tokens ở `assets/css/` dùng CSS custom properties chuẩn (`--dt-*`); mapping sang iOS/Android/Tailwind theo guide 09; sinh lại tokens bằng `scripts/generate_css_tokens.py`
- **Companion repos:** skill-ui-ux (12 design styles) — liên kết qua `sections.styleAffinity`; skill-animation (12 motion disciplines) — liên kết qua `sections.motionAffinity`

Khi thay đổi cấu trúc `data.json` (thêm/xóa section), tăng `meta.version` và cập nhật section này.

## References & Inspiration

Curated spec links, tool documentation, and inspiration sources: [`skills/assets/references.md`](./skills/assets/references.md).

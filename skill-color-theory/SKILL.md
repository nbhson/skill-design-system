---
name: color-theory
description: Professional color theory skill guide covering 12 disciplines (color harmony & schemes, OKLCH perceptual spaces, color psychology, gray ramps & tinted neutrals, brand ramp construction, semantic status color, dark mode palette, data-viz palettes, gradient theory, contrast models & math, CVD-safe design, cultural color meaning). Use when building palettes, choosing brand colors, designing dark themes, fixing contrast, or auditing color systems across markets.
---

# Color Theory — Skill Router

This skill provides 12 curated color-discipline guides. Each guide covers definition, core principles, spec tokens (policies/thresholds/contracts), composition, signature patterns, real-world use cases, combination notes, anti-patterns, code examples, and an implementation checklist.

## Step 1 — Choose a discipline

Match the color task to a discipline:

| Discipline | Best for | Avoid for |
|---|---|---|
| Color Harmony & Schemes | Scheme intent + 60-30-10 proportions | Shipping a scheme as a palette |
| OKLCH & Perceptual Spaces | Ramp math, interpolation, gamut | HSL-by-habit palette work |
| Color Psychology | Brand personality → palette brief | "Purple is creative" folklore |
| Gray Ramps & Tinted Neutrals | The neutral backbone + elevation | Invisible borders, mud grays |
| Brand Ramp Construction | Brand point → 11-step usable ramp | Hand-picked hex ramps |
| Semantic Status Color | Success/warning/danger/info systems | Brand-recoloring error states |
| Dark Mode Palette | Designed dark, not inverted light | #000 + neon brand buttons |
| Data Visualization Palettes | Categorical/sequential/diverging | Rainbow categorical chaos |
| Gradient Design | OKLab interpolation, banding, scrims | Text on unscrimmed gradients |
| Contrast Models & Math | WCAG + APCA pairing manifests | Contrast-by-eye |
| CVD-Safe Design | Colorblind-safe pairs + simulation | Red-green differentiators |
| Cultural Color Meaning | Per-market palette audits | One-global-palette-by-default |

If the user names a task explicitly ("brand color into a palette", "dark mode looks wrong", "chart colors unreadable"), go straight to its guide. If the task is "build the color system", start with **oklch-perceptual** → **brand-ramp-construction** → **gray-ramp-neutrals**, then pull the rest as needed.

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
| 1 | Color Harmony & Schemes | [skills/01-color-harmony/SKILL.md](./skills/01-color-harmony/SKILL.md) |
| 2 | OKLCH & Perceptual Spaces | [skills/02-oklch-perceptual/SKILL.md](./skills/02-oklch-perceptual/SKILL.md) |
| 3 | Color Psychology & Brand Fit | [skills/03-color-psychology/SKILL.md](./skills/03-color-psychology/SKILL.md) |
| 4 | Gray Ramps & Tinted Neutrals | [skills/04-gray-ramp-neutrals/SKILL.md](./skills/04-gray-ramp-neutrals/SKILL.md) |
| 5 | Brand Ramp Construction | [skills/05-brand-ramp-construction/SKILL.md](./skills/05-brand-ramp-construction/SKILL.md) |
| 6 | Semantic Status & Feedback Color | [skills/06-semantic-color-system/SKILL.md](./skills/06-semantic-color-system/SKILL.md) |
| 7 | Dark Mode Palette | [skills/07-dark-mode-palette/SKILL.md](./skills/07-dark-mode-palette/SKILL.md) |
| 8 | Data Visualization Palettes | [skills/08-data-viz-palettes/SKILL.md](./skills/08-data-viz-palettes/SKILL.md) |
| 9 | Gradient Design | [skills/09-gradient-theory/SKILL.md](./skills/09-gradient-theory/SKILL.md) |
| 10 | Contrast Models & Math | [skills/10-contrast-models/SKILL.md](./skills/10-contrast-models/SKILL.md) |
| 11 | Color Vision Deficiency Safety | [skills/11-cvd-safe-design/SKILL.md](./skills/11-cvd-safe-design/SKILL.md) |
| 12 | Cultural Color Meaning | [skills/12-cultural-color-meaning/SKILL.md](./skills/12-cultural-color-meaning/SKILL.md) |

## Step 3 — Apply

- Treat the spec tokens as **hard standards**: ramps are generated curves with per-step contracts; hand-picked hex ramps are violations.
- Respect the **validation order**: palette → pairing manifest (WCAG + APCA) → CVD simulation → market review - aesthetics come last in the chain, never first.
- ALWAYS honor the guide's **Accessibility Notes**: contrast floors and CVD safety are palette-level contracts; a harmonious palette that fails 4.5:1 is not a palette.
- Check the **Combination Matrix** in [README.md](./README.md) before pairing disciplines: ✅ combines well, ⚠️ conditional, ❌ do not combine.
- When the task also involves visual style, motion, or tokens, consult companions **skill-ui-ux**, **skill-animation**, and **skill-design-tokens** via the guides' affinity notes.

## Machine-Readable Data

For programmatic use (palette linting, CI wiring, AI agents), read [`skills/data.json`](./skills/data.json) — all 12 disciplines as structured JSON with a fully symmetric combination matrix, affinity mappings, and per-skill accessibility contracts:

```json
{ "skills": [{ "id": "brand-ramp-construction", "sections": { "tokens": [...], "combinations": {...}, "antiPatterns": [...], "accessibility": { "required": true, "notes": "...", "fallback": "..." } } }] }
```

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12 (duyệt `skills/*/SKILL.md` hoặc `data.json` → `skills[].id`)
- **Compatibility:** framework-agnostic — spec tokens ở `assets/css/` dùng CSS custom properties chuẩn (`--clr-*`); OKLCH/OKLab syntax Baseline 2023; sinh lại tokens bằng `scripts/generate_css_tokens.py`
- **Companion repos:** skill-ui-ux (12 design styles) — `sections.styleAffinity`; skill-animation (12 motion disciplines) — `sections.motionAffinity`; skill-design-tokens (12 token disciplines) — color primitives/alias/theming contracts

Khi thay đổi cấu trúc `data.json` (thêm/xóa section), tăng `meta.version` và cập nhật section này.

## References & Inspiration

Curated spec links, tool documentation, and inspiration sources: [`skills/assets/references.md`](./skills/assets/references.md).

# Plan — skill-color-theory

> Kế hoạch khởi tạo chuẩn enterprise theo mẫu các skill repo trước — cập nhật: 02/11/2026

## Tổng quan

Skill bộ 12 color-theory disciplines (Color Harmony → Cultural Color Meaning) cho OpenCode:
mỗi discipline có SKILL.md đầy đủ 10 sections + `data.json` machine-readable + CSS spec
tokens (`--clr-*`) + validator CI. Companion repos: `skill-ui-ux` (styleAffinity),
`skill-animation` (motionAffinity), `skill-design-tokens` (color primitives/alias/theming).

## Phân loại 12 disciplines

1. color-harmony — schemes, 60-30-10, proportion rules
2. oklch-perceptual — OKLCH/OKLab ramp math, interpolation, gamut
3. color-psychology — brand personality → palette brief
4. gray-ramp-neutrals — tinted vs pure neutrals, elevation steps
5. brand-ramp-construction — brand point → 11-step ramp với contracts
6. semantic-color-system — success/warning/danger/info ramps + multi-signal
7. dark-mode-palette — dark design, không invert, desaturated tints
8. data-viz-palettes — categorical/sequential/diverging, CVD-safe
9. gradient-theory — oklab interpolation, banding, mesh/aurora
10. contrast-models — WCAG ratio vs APCA, pairing manifest
11. cvd-safe-design — simulation gates, blue-orange axis
12. cultural-color-meaning — per-market palette audits

## Tiến độ

- [x] plan/readme.md
- [x] skills/data.json (12 skills, matrix đối xứng, affinity hợp lệ)
- [x] SKILL.md router
- [x] 12 guides 10 sections (01→12)
- [x] assets/css × 12 (generated)
- [x] scripts (generate + validate, adapted từ skill-typography)
- [x] README.md (skill list, matrix, affinity tables)
- [x] skills/assets/references.md
- [x] CI workflow + LICENSE + .gitignore
- [x] Validator pass 100%

# Plan — skill-icons-illustration

> Kế hoạch khởi tạo chuẩn enterprise theo mẫu các skill repo trước — cập nhật: 02/11/2026

## Tổng quan

Skill bộ 12 icon/illustration disciplines (Icon Style Selection → Icon & Illustration System
Audit) cho OpenCode: mỗi discipline có SKILL.md đầy đủ 10 sections + `data.json`
machine-readable + CSS spec tokens (`--icon-*`) + validator CI. Companion repos:
`skill-ui-ux` (styleAffinity), `skill-animation` (motionAffinity), `skill-design-tokens`
(color/spacing contracts), `skill-ux-writing` (empty/error copy pairing).

## Phân loại 12 disciplines

1. icon-style-selection — filled vs outline, stroke, corner, one-style rule
2. icon-grid-sizing — 24px grid, keylines, size ramp, pixel snap
3. icon-library-management — naming, pipeline, versioning, pruning
4. icon-usability — recognition, labels, 44px targets
5. accessible-icons — aria names, hidden decoration, 1.4.11 contrast
6. illustration-direction — purpose matrix, style spec, consistency
7. empty-error-illustrations — state slots: mood + copy + action
8. mascot-character — character systems, restraint rule
9. svg-optimization — SVGO, currentColor, budgets
10. animation-integration — draw-ins, Lottie, reduced-motion
11. favicon-app-icons — modern minimal set, maskable, PWA
12. icon-system-audit — consistency scoring, a11y sweep, weight audit

## Tiến độ

- [x] plan/readme.md
- [x] skills/data.json (12 skills, matrix đối xứng, affinity hợp lệ)
- [x] SKILL.md router
- [x] 12 guides 10 sections (01→12)
- [x] assets/css × 12 (generated)
- [x] scripts (generate + validate, adapted từ skill-ux-writing)
- [x] README.md (skill list, matrix, affinity tables)
- [x] skills/assets/references.md
- [x] CI workflow + LICENSE + .gitignore
- [x] Validator pass 100%

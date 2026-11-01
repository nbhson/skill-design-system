# Plan — skill-typography

> Kế hoạch khởi tạo chuẩn enterprise theo mẫu các skill repo trước — cập nhật: 01/11/2026

## Tổng quan

Skill bộ 12 typography disciplines (Font Pairing → Accessible Typography) cho OpenCode:
mỗi discipline có SKILL.md đầy đủ 10 sections + `data.json` machine-readable + CSS spec
tokens (`--type-*`) + validator CI. Companion repos: `skill-ui-ux` (styleAffinity),
`skill-animation` (motionAffinity), `skill-design-tokens` (typography tokens + contrast).

## Phân loại 12 disciplines

1. font-pairing — chọn family, superfamily, license, fallback
2. type-scale — modular scale root 16, ratio 1.25
3. line-height — leading per role, grid rhythm, diacritic headroom
4. letter-spacing — tracking display/caps, script exemption
5. visual-hierarchy — 4 levers (size/weight/color/position), text roles
6. fluid-responsive — clamp() giữa các scale stops
7. multilingual-vietnamese — diacritics, subsets, fallback chain
8. readability-legibility — 45-75ch, paragraph rhythm, glyph legibility
9. webfont-loading — subsets, font-display, CLS prevention
10. numeric-tabular — tnum, slashed-zero, data typography
11. variable-fonts — axes, named instances, optical sizing
12. accessible-typography — WCAG floors cho text

## Tiến độ

- [x] plan/readme.md
- [x] skills/data.json (12 skills, matrix đối xứng, affinity hợp lệ)
- [x] SKILL.md router
- [x] 12 guides 10 sections (01→12)
- [x] assets/css × 12 (generated)
- [x] scripts (generate + validate, adapted từ skill-design-tokens)
- [x] README.md (skill list, matrix, affinity tables)
- [x] skills/assets/references.md
- [x] CI workflow + LICENSE + .gitignore
- [x] Validator pass 100%

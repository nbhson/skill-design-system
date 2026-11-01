# Plan — skill-design-tokens

> Kế hoạch khởi tạo chuẩn enterprise theo mẫu skill-ui-ux / skill-animation — cập nhật: 01/11/2026

## Tổng quan

Skill bộ 12 token disciplines (Color Scales → Governance) cho OpenCode: mỗi discipline có
SKILL.md đầy đủ 10 sections + `data.json` machine-readable + CSS tokens (`--dt-*`) +
validator CI. Companion repos: `skill-ui-ux` (liên kết qua `sections.styleAffinity`) và
`skill-animation` (liên kết qua `sections.motionAffinity`).

## Phân loại 12 disciplines

1. color-tokens — primitive color ramps 50-950 (neutral/brand/feedback)
2. typography-tokens — font family, modular scale, weight, line-height
3. spacing-sizing — scale 4px, icon sizing, touch target 44px
4. radius-elevation — radius steps, shadow levels, z-index enum
5. semantic-alias-naming — kiến trúc 3 tầng primitive → alias → component
6. dark-mode — re-point alias tier cho dark theme
7. multi-brand-theming — brand overrides ở alias tier, brand matrix
8. contrast-validation — WCAG 1.4.3/1.4.11/2.4.13 thành CI gates
9. platform-mapping — CSS/iOS/Android/Tailwind codegen contracts
10. token-pipeline-figma — Figma variables → DTCG → codegen, PR-gated
11. component-tokens — component slots derived từ aliases
12. governance-migration — review, semver, deprecation, lint, adoption

## Cấu trúc

- `SKILL.md` (root) — router: chọn discipline theo task → guide tương ứng
- `skills/<NN-id>/SKILL.md` × 12 — 10 sections chuẩn
- `skills/data.json` — machine-readable: meta + sections + combinations (đối xứng)
  + styleAffinity (→ skill-ui-ux) + motionAffinity (→ skill-animation) + accessibility
- `assets/css/<id>.css` × 12 — sinh từ data.json bởi `scripts/generate_css_tokens.py`
- `scripts/validate_skills.py` — 10 checks CI: guides ↔ data.json ↔ README matrix ↔ CSS
- `.github/workflows/validate.yml` — chạy validator trên push/PR

## Tiến độ

- [x] plan/readme.md
- [x] skills/data.json (12 skills, matrix đối xứng, affinity hợp lệ)
- [x] SKILL.md router
- [x] 12 guides 10 sections (01→12)
- [x] assets/css × 12 (generated)
- [x] scripts/generate_css_tokens.py + validate_skills.py
- [x] README.md (skill list, matrix, affinity tables)
- [x] skills/assets/references.md
- [x] CI workflow + LICENSE + .gitignore
- [x] Validator pass 100%

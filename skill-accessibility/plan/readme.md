# Plan — skill-accessibility

> Kế hoạch khởi tạo chuẩn enterprise theo mẫu skill-ui-ux / skill-animation / skill-design-tokens — cập nhật: 01/11/2026

## Tổng quan

Skill bộ 12 accessibility disciplines (WCAG Fundamentals → Testing & Audit) cho OpenCode:
mỗi discipline có SKILL.md đầy đủ 10 sections + `data.json` machine-readable + CSS spec
tokens (`--a11y-*`) + validator CI. Companion repos: `skill-ui-ux` (styleAffinity),
`skill-animation` (motionAffinity), `skill-design-tokens` (contrast/focus/target contracts).

## Phân loại 12 disciplines

1. wcag-fundamentals — POUR, levels, criteria map, legal baselines
2. color-contrast — WCAG 1.4.3/1.4.11/1.4.1/2.4.13 như thiết kế từ đầu
3. keyboard-navigation — tab order, skip link, roving tabindex (2.1.1/2.4.3)
4. focus-management — focus landing/return, modal trap, announcements
5. aria-fundamentals — roles/states/names/live regions, native-first
6. aria-patterns-widgets — APG patterns: tabs, menu, combobox, dialog, grid
7. forms-errors — labels, hints, error wiring (3.3.x, 4.1.3)
8. screen-readers — NVDA/JAWS/VoiceOver matrix + listening scripts
9. media-alt-text — alt writing, captions, transcripts (1.1.1, 1.2.x)
10. cognitive-content — plain language, consistency, timeouts (3.x, 2.2.1)
11. zoom-reflow — 200%/400% zoom, 320px reflow, 2.5.x pointer criteria
12. testing-audit — CI (axe) + manual passes + listening scripts + report

## Cấu trúc

- `SKILL.md` (root) — router
- `skills/<NN-id>/SKILL.md` × 12 — 10 sections chuẩn
- `skills/data.json` — machine-readable, matrix đối xứng, affinity chéo
- `assets/css/<id>.css` × 12 — sinh từ data.json
- `scripts/generate_css_tokens.py` + `validate_skills.py` (10 checks)
- `.github/workflows/validate.yml`, README matrix, references, LICENSE, .gitignore

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

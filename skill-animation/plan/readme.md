# Plan — skill-animation

> Kế hoạch khởi tạo chuẩn enterprise theo mẫu skill-ui-ux — cập nhật: 01/11/2026

## Tổng quan

Skill bộ 12 animation disciplines (Duration & Easing → Reduced Motion) cho OpenCode:
mỗi discipline có SKILL.md đầy đủ 10 sections + `data.json` machine-readable +
CSS motion tokens + validator CI. Companion repo: `skill-ui-ux` (liên kết qua
`sections.styleAffinity`).

## Phân loại 12 disciplines

1. easing-timing — nền tảng duration/easing tokens
2. micro-interactions — hover/press/toggle/like feedback
3. entrance-exit — reveal, stagger, choreography vào/ra
4. page-transitions — route/view transitions, shared element
5. loading-states — skeleton, progress, optimistic UI
6. feedback-confirmation — toast, checkmark, undo, error
7. scroll-animation — parallax, reveal, progress, scrollytelling
8. gesture-drag — drag/swipe/fling, spring physics
9. data-animation — count-up, chart entrance, live update
10. ambient-motion — aurora, particles, marquee (decorative loops)
11. illustration-lottie — Lottie/Rive, character, empty states
12. reduced-motion — tầng accessibility cho toàn bộ skill set

## Cấu trúc

- `SKILL.md` (root) — router: chọn discipline theo task → guide tương ứng
- `skills/<NN-id>/SKILL.md` × 12 — 10 sections chuẩn
- `skills/data.json` — nguồn truth: tokens, combinations (đối xứng 66/66 pairs),
  styleAffinity (12 design styles của skill-ui-ux), reducedMotion contract
- `assets/css/<id>.css` × 12 — motion tokens sinh tự động từ data.json
  (`--motion-*` custom properties + global reduced-motion override)
- `scripts/generate_css_tokens.py` — sinh lại tokens từ data.json (idempotent)
- `scripts/validate_skills.py` — 10 checks CI
- `.github/workflows/validate.yml` — chạy validator trên push/PR main

## Kiểm chứng

```
python3 scripts/validate_skills.py  →  All checks passed ✓
python3 scripts/generate_css_tokens.py  →  idempotent, 12/12 files
```

## Backlog đề xuất

- [ ] Thêm demo HTML gallery (1 file preview mọi discipline)
- [ ] Spring physics token generator (stiffness/damping → cubic-bezier xấp xỉ)
- [ ] Motion lint plugin mẫu (bắt magic durations trong component code)
- [ ] Đồng bộ ngược: script check `styleAffinity` ids tồn tại trong skill-ui-ux/data.json

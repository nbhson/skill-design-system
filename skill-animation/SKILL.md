---
name: ui-animation
description: Professional UI animation skill guide covering 12 motion disciplines (duration & easing, micro-interactions, entrance/exit choreography, page/view transitions, loading states, feedback & confirmation, scroll-driven animation, gesture & drag physics, data & chart animation, ambient motion, illustration & Lottie, reduced-motion accessibility). Use when adding or reviewing any animation, transition, or micro-interaction, choosing motion tokens, or auditing an interface for motion quality and accessibility.
---

# UI Animation — Skill Router

This skill provides 12 curated motion-discipline guides. Each guide covers definition, core principles, motion tokens (duration/easing/spring), choreography, signature patterns, real-world use cases, combination notes, anti-patterns, reduced-motion fallbacks (WCAG 2.3.3 / vestibular safety), code examples, and an implementation checklist.

## Step 1 — Choose a discipline

Match the motion task to a discipline:

| Discipline | Best for | Avoid for |
|---|---|---|
| Duration & Easing | Establishing a product-wide motion token system | One-off decorative effects |
| Micro-interactions | Hover, press, toggle, like, copy feedback | Long storytelling moments |
| Entrance & Exit | First paint, list reveals, modal in/out | Continuous live data grids |
| Page & View Transitions | Route changes, shared-element morphs, drill-downs | Lateral tab jumps at depth |
| Loading States | Waits > 300ms: skeletons, progress, optimistic UI | Waits that are actually instant |
| Feedback & Confirmation | Toasts, success checkmarks, undo, error states | Decorative ambience |
| Scroll-Driven | Landing pages, scrollytelling, progress, parallax | Forms and reading surfaces |
| Gesture & Drag | Swipe actions, reorder, pull-to-refresh, sheets | Mouse-first enterprise tables |
| Data & Chart | KPI count-ups, chart entrances, live updates | Dense tables (keep them still) |
| Ambient Motion | Heroes, empty states, brand moments | Task-critical screens |
| Illustration & Lottie | Characters, mascots, empty/celebration states | Icon-scale micro-feedback |
| Reduced Motion | The accessibility layer for ALL of the above | (never skippable) |

If the user names a discipline explicitly (e.g., "toast animation", "page transition", "spring drag"), go straight to its guide. If the task is "add motion to X", pick by X's category using the table above.

## Step 2 — Read the discipline guide

Each guide lives in `skills/<NN-<skill>>/SKILL.md` and follows a 10-section standard:

1. Definition — core concept in 2–3 sentences
2. Core Motion Principles — mandatory rules
3. Motion Tokens — duration/easing/spring values + role of each
4. Choreography — sequencing, stagger, layer order
5. Signature Patterns — the 2–3 canonical implementation patterns
6. Real-World Use Cases — suitable products/contexts
7. Combination Notes — pairing with sibling skills + design-style affinity (skill-ui-ux)
8. Anti-Patterns — common mistakes (incl. reduced-motion Accessibility Notes)
9. Code Examples — complete HTML+CSS (±JS) snippets using the skill's tokens
10. Implementation Checklist — pre-delivery quality checks

| # | Discipline | Guide |
|---|-----------|-------|
| 1 | Duration & Easing | [skills/01-easing-timing/SKILL.md](./skills/01-easing-timing/SKILL.md) |
| 2 | Micro-interactions | [skills/02-micro-interactions/SKILL.md](./skills/02-micro-interactions/SKILL.md) |
| 3 | Entrance & Exit | [skills/03-entrance-exit/SKILL.md](./skills/03-entrance-exit/SKILL.md) |
| 4 | Page & View Transitions | [skills/04-page-transitions/SKILL.md](./skills/04-page-transitions/SKILL.md) |
| 5 | Loading States | [skills/05-loading-states/SKILL.md](./skills/05-loading-states/SKILL.md) |
| 6 | Feedback & Confirmation | [skills/06-feedback-confirmation/SKILL.md](./skills/06-feedback-confirmation/SKILL.md) |
| 7 | Scroll-Driven | [skills/07-scroll-animation/SKILL.md](./skills/07-scroll-animation/SKILL.md) |
| 8 | Gesture & Drag | [skills/08-gesture-drag/SKILL.md](./skills/08-gesture-drag/SKILL.md) |
| 9 | Data & Chart | [skills/09-data-animation/SKILL.md](./skills/09-data-animation/SKILL.md) |
| 10 | Ambient Motion | [skills/10-ambient-motion/SKILL.md](./skills/10-ambient-motion/SKILL.md) |
| 11 | Illustration & Lottie | [skills/11-illustration-lottie/SKILL.md](./skills/11-illustration-lottie/SKILL.md) |
| 12 | Reduced Motion | [skills/12-reduced-motion/SKILL.md](./skills/12-reduced-motion/SKILL.md) |

## Step 3 — Apply

- Use the skill's **motion tokens** (`assets/css/<skill-id>.css`, `--motion-*` custom properties) as hard standards; no magic durations or ad-hoc curves.
- Respect the **Anti-Patterns** section — these are the mistakes that most often make motion feel wrong.
- ALWAYS apply the guide's **reduced-motion fallback** (see `skills/12-reduced-motion/SKILL.md` for the global strategy): remove loops/parallax, replace travel with opacity/color, retain short fades.
- Check the **Combination Matrix** in [README.md](./README.md) before pairing two disciplines: ✅ combines well, ⚠️ conditional (follow section 7 tips), ❌ do not combine.
- When the task also involves visual style, consult the companion repo **skill-ui-ux** and the guide's `styleAffinity` notes.

## Machine-Readable Data

For programmatic use (motion linting, token generation, AI agents), read [`skills/data.json`](./skills/data.json) — all 12 disciplines as structured JSON with a fully symmetric combination matrix, style affinity to skill-ui-ux, and per-skill reduced-motion fallback contracts:

```json
{ "skills": [{ "id": "easing-timing", "sections": { "tokens": [...], "combinations": {...}, "antiPatterns": [...], "reducedMotion": { "required": true, "notes": "...", "fallback": "..." } } }] }
```

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12 (duyệt `skills/*/SKILL.md` hoặc `data.json` → `skills[].id`)
- **Compatibility:** framework-agnostic — CSS tokens ở `assets/css/` dùng CSS custom properties chuẩn; JS patterns chỉ dùng Web APIs (View Transitions, IntersectionObserver, Pointer Events, Web Animations); sinh lại tokens bằng `scripts/generate_css_tokens.py`
- **Companion repo:** skill-ui-ux (12 design styles) — liên kết qua `sections.styleAffinity`

Khi thay đổi cấu trúc `data.json` (thêm/xóa section), tăng `meta.version` và cập nhật section này.

## References & Inspiration

Curated spec links, tool documentation, easing libraries, and inspiration sources: [`skills/assets/references.md`](./skills/assets/references.md).

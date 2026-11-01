# 🖼️ Professional Icons & Illustration Skill Set — 12 Visual-Asset Disciplines

A professional reference guide for 12 icon/illustration disciplines, each covering: definition, core principles, spec tokens (policies/budgets/contracts), composition, signature patterns, real-world applications, combination notes, anti-patterns, accessibility notes, code examples, and an implementation checklist.

Companion repos: **skill-ui-ux** (12 design styles), **skill-animation** (12 motion disciplines), **skill-design-tokens** (12 token disciplines), **skill-ux-writing** (12 writing disciplines). This repo answers *"what do the visual assets look like and how are they engineered?"* — the asset layer beneath components. Every skill declares a `styleAffinity` mapping to skill-ui-ux style ids and a `motionAffinity` mapping to skill-animation discipline ids.

## 📂 Skill List

| # | Skill | Folder | Summary |
|---|-------|--------|---------|
| 1 | [Icon Style Selection](./skills/01-icon-style-selection/SKILL.md) | 01-icon-style-selection | Choosing the icon language: filled vs outline, stroke weight, corner radius, and the one-style rule across a product. |
| 2 | [Icon Grid & Sizing](./skills/02-icon-grid-sizing/SKILL.md) | 02-icon-grid-sizing | The construction grid: 24px base, 16/20/24/32 scale, padding budgets, keyline shapes, and pixel-snapping for crisp strokes. |
| 3 | [Icon Library Management](./skills/03-icon-library-management/SKILL.md) | 03-icon-library-management | The pipeline: naming conventions, source-of-truth files, versioning, contribution workflow, and pruning dead icons. |
| 4 | [Icon Usability](./skills/04-icon-usability/SKILL.md) | 04-icon-usability | Recognition over recall: when icons need labels, the familiar-glyph rule, target sizes, and testing that catches mystery icons. |
| 5 | [Accessible Icons](./skills/05-accessible-icons/SKILL.md) | 05-accessible-icons | The aria contract: accessible names for functional icons, aria-hidden for decorative ones, and contrast that survives WCAG 1.4.11. |
| 6 | [Illustration Direction](./skills/06-illustration-direction/SKILL.md) | 06-illustration-direction | Defining the illustration language: purpose matrix, style lock-up with brand, color discipline, and consistency across artists. |
| 7 | [Empty & Error Illustrations](./skills/07-empty-error-illustrations/SKILL.md) | 07-empty-error-illustrations | The highest-traffic illustration slots: empty states, errors, 404s, and offline - mood-matched, copy-paired, and light-weight. |
| 8 | [Mascot & Character Design](./skills/08-mascot-character/SKILL.md) | 08-mascot-character | Brand characters done responsibly: proportion systems, emotion ranges, do/don't placements, and the restraint rule. |
| 9 | [SVG Optimization](./skills/09-svg-optimization/SKILL.md) | 09-svg-optimization | Lean vectors: SVGO discipline, viewBox hygiene, currentColor theming, sprite strategies, and what never to hand-edit. |
| 10 | [Icon & Illustration Animation](./skills/10-animation-integration/SKILL.md) | 10-animation-integration | Motion on vector assets: when icons animate, Lottie vs SMIL vs CSS, weight costs, and reduced-motion fallbacks. |
| 11 | [Favicons & App Icons](./skills/11-favicon-app-icons/SKILL.md) | 11-favicon-app-icons | The smallest brand surfaces: favicon sets, PWA icons, maskable variants, touch icons, and generation over hand-export. |
| 12 | [Icon & Illustration System Audit](./skills/12-icon-system-audit/SKILL.md) | 12-icon-system-audit | The system health check: consistency scoring, a11y sweep, weight audit, and the per-surface review pass. |

## 🤖 Machine-Readable Data / AI Agents

[`data.json`](./skills/data.json) — the full skill set as structured JSON (definitions, principles, spec tokens, composition, patterns, use cases, combinations, style/motion affinity, anti-patterns, accessibility contracts). The root [`SKILL.md`](./SKILL.md) acts as a router for AI agents.

```json
{
  "skills": [{
    "id": "accessible-icons",
    "sections": {
      "tokens": [{ "role": "functional-name", "value": "aria-label-required", "notes": "..." }],
      "combinations": { "good": [], "caution": [], "avoid": [] },
      "styleAffinity": { "good": [], "caution": [], "avoid": [] },
      "motionAffinity": { "good": [], "caution": [], "avoid": [] },
      "antiPatterns": ["..."],
      "accessibility": { "required": true, "notes": "...", "fallback": "..." }
    }
  }]
}
```

## 📚 References

[`assets/references.md`](./skills/assets/references.md) — curated spec links (WCAG non-text content, SVGO), tool docs (Lottie, Lighthouse), and icon/illustration learning resources.

## 🎯 How to Use

1. **Select a discipline:** use the summary table to pick the skill that matches the visual-asset task.
2. **Read SKILL.md:** each guide follows the 10-section standard (definition → principles → tokens → composition → patterns → applications → combinations → anti-patterns → code examples → checklist).
3. **Apply:** treat the spec tokens from `assets/css/<skill-id>.css` as hard standards — one style family, grid discipline, weight budgets, the aria contract. For AI agents: use the root `SKILL.md` router, then the specific guide.

## 🔄 Quick Combination Matrix

Symbols: ✅ combines well · ⚠️ conditional — follow the pairing tips in section 7 · ❌ do not combine.

| | style | grid | library | usability | a11y | illusdir | emptyerr | mascot | svg | anim | favicon | audit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Icon Style Selection** | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Icon Grid & Sizing** | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Icon Library Management** | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Icon Usability** | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Accessible Icons** | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Illustration Direction** | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Empty & Error Illustrations** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Mascot & Character Design** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ |
| **SVG Optimization** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ |
| **Icon & Illustration Animation** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| **Favicons & App Icons** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ |
| **Icon & Illustration System Audit** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |

## 🧭 Design Style Affinity (skill-ui-ux / skill-design-tokens)

| Skill | Styles it elevates | Styles it clashes with |
|---|---|---|
| Icon Style Selection | minimalism, flat-design, class-morphism | maximalism |
| Icon Grid & Sizing | minimalism, flat-design, class-morphism | — |
| Icon Library Management | minimalism, flat-design, class-morphism | — |
| Icon Usability | minimalism, flat-design, class-morphism | — |
| Accessible Icons | minimalism, flat-design, class-morphism | — |
| Illustration Direction | collage-art, maximalism, retro | minimalism |
| Empty & Error Illustrations | collage-art, minimalism, flat-design | — |
| Mascot & Character Design | claymorphism, collage-art, retro | brutalism-ui |
| SVG Optimization | minimalism, flat-design, class-morphism | — |
| Icon & Illustration Animation | claymorphism, aurora-ui, glassmorphism | minimalism |
| Favicons & App Icons | minimalism, flat-design, class-morphism | — |
| Icon & Illustration System Audit | minimalism, flat-design, class-morphism | — |

## 🏃 Motion Affinity (skill-animation)

| Skill | Motion it pairs with | Motion to handle with care |
|---|---|---|
| Icon Style Selection | micro-interactions, easing-timing | — |
| Icon Grid & Sizing | easing-timing, micro-interactions | — |
| Icon Library Management | easing-timing | — |
| Icon Usability | micro-interactions, feedback-confirmation | — |
| Accessible Icons | reduced-motion, micro-interactions | — |
| Illustration Direction | illustration-lottie, ambient-motion | — |
| Empty & Error Illustrations | illustration-lottie, entrance-exit | — |
| Mascot & Character Design | illustration-lottie, ambient-motion | — |
| SVG Optimization | easing-timing, illustration-lottie | — |
| Icon & Illustration Animation | micro-interactions, illustration-lottie, loading-states | ambient-motion |
| Favicons & App Icons | easing-timing | — |
| Icon & Illustration System Audit | easing-timing | — |

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12
- **Token prefix:** `--icon-*` (CSS custom properties; see `assets/css/`)
- **CI:** `python3 scripts/validate_skills.py` — 10 checks covering guides, data.json, CSS files, README matrix, and repo hygiene

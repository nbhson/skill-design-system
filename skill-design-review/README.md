# 🔍 Professional Design Review Skill Set — 12 Review Disciplines

A professional reference guide for 12 design-review disciplines, each covering: definition, core principles, spec tokens (protocols/thresholds/contracts), composition, signature patterns, real-world applications, combination notes, anti-patterns, accessibility notes, code examples, and an implementation checklist.

Companion repos: **skill-ui-ux** (12 design styles), **skill-animation** (12 motion disciplines), **skill-design-tokens**, **skill-accessibility**, **skill-component-recipes**, **skill-ux-writing**. This repo answers *"is the surface good — and by which standard?"* — the review layer that audits every other discipline's contracts. Every skill declares a `styleAffinity` mapping to skill-ui-ux style ids and a `motionAffinity` mapping to skill-animation discipline ids.

## 📂 Skill List

| # | Skill | Folder | Summary |
|---|-------|--------|---------|
| 1 | [Review Process](./skills/01-review-process/SKILL.md) | 01-review-process | The design review operating system: critique formats, severity scales, roles, cadence, and decisions that stick. |
| 2 | [Visual Hierarchy Audit](./skills/02-visual-hierarchy-audit/SKILL.md) | 02-visual-hierarchy-audit | Does the page guide the eye: primary action dominance, scanning patterns, and the squint test. |
| 3 | [Consistency Audit](./skills/03-consistency-audit/SKILL.md) | 03-consistency-audit | Token adherence, component reuse, and pattern discipline: is the product speaking one visual language? |
| 4 | [Accessibility Audit](./skills/04-a11y-audit/SKILL.md) | 04-a11y-audit | The conformance pass: keyboard walks, screen reader runs, contrast checks, and severity-ranked WCAG findings. |
| 5 | [Motion Audit](./skills/05-motion-audit/SKILL.md) | 05-motion-audit | Is motion serving the interface: purpose check, token adherence, duration/easing review, and reduced-motion verification. |
| 6 | [Typography Audit](./skills/06-typography-audit/SKILL.md) | 06-typography-audit | Scale adherence, hierarchy in text, line-length/readability, and the type crimes: justified widows, tracking all-caps, mixed scales. |
| 7 | [Spacing & Rhythm Audit](./skills/07-spacing-rhythm-audit/SKILL.md) | 07-spacing-rhythm-audit | The 4/8px grid check: off-scale spacing, grouping errors, and vertical rhythm that holds across the surface. |
| 8 | [Interaction States Audit](./skills/08-interaction-states-audit/SKILL.md) | 08-interaction-states-audit | Every interactive element in every state: hover, focus, active, disabled, loading - designed, visible, and consistent. |
| 9 | [Content & Microcopy Audit](./skills/09-content-microcopy-audit/SKILL.md) | 09-content-microcopy-audit | The strings pass: error completeness, label specificity, reading level, and glossary adherence - checked per surface. |
| 10 | [Perceived Performance](./skills/10-perceived-performance/SKILL.md) | 10-perceived-performance | Speed as the user feels it: skeleton discipline, optimistic UI, progress honesty, and the response-time bands. |
| 11 | [Responsive Audit](./skills/11-responsive-audit/SKILL.md) | 11-responsive-audit | Every surface at every size: 320px to ultrawide, touch vs pointer, orientation, and the breakpoint behaviors that were promised. |
| 12 | [Audit Report Template](./skills/12-report-template/SKILL.md) | 12-report-template | The artifact that makes findings stick: scorecard structure, severity-tagged findings, evidence, and trend tracking. |

## 🤖 Machine-Readable Data / AI Agents

[`data.json`](./skills/data.json) — the full skill set as structured JSON (definitions, principles, spec tokens, composition, patterns, use cases, combinations, style/motion affinity, anti-patterns, accessibility contracts). The root [`SKILL.md`](./SKILL.md) acts as a router for AI agents.

```json
{
  "skills": [{
    "id": "a11y-audit",
    "sections": {
      "tokens": [{ "role": "contrast-text", "value": "4.5:1-3:1-large", "notes": "..." }],
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

[`assets/references.md`](./skills/assets/references.md) — curated spec links (WCAG understanding docs, axe), tool docs (contrast checkers, screen readers), and design-critique learning resources.

## 🎯 How to Use

1. **Select a discipline:** use the summary table to pick the review axis that matches the task.
2. **Read SKILL.md:** each guide follows the 10-section standard (definition → principles → tokens → composition → patterns → applications → combinations → anti-patterns → code examples → checklist).
3. **Apply:** treat the spec tokens from `assets/css/<skill-id>.css` as hard standards — severity scales, duration ladders, response bands. For AI agents: use the root `SKILL.md` router, then the specific guide.

## 🔄 Quick Combination Matrix

Symbols: ✅ combines well · ⚠️ conditional — follow the pairing tips in section 7 · ❌ do not combine.

| | process | hierarchy | consistency | a11y | motion | typo | spacing | states | content | perf | responsive | report |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Review Process** | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Visual Hierarchy Audit** | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Consistency Audit** | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Accessibility Audit** | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Motion Audit** | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Typography Audit** | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Spacing & Rhythm Audit** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Interaction States Audit** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ |
| **Content & Microcopy Audit** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ |
| **Perceived Performance Audit** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| **Responsive Audit** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ |
| **Audit Report Template** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |

## 🧭 Design Style Affinity (skill-ui-ux / skill-design-tokens)

| Skill | Styles it elevates | Styles it clashes with |
|---|---|---|
| Review Process | minimalism, class-morphism, flat-design | — |
| Visual Hierarchy Audit | minimalism, flat-design, class-morphism | maximalism |
| Consistency Audit | minimalism, flat-design, class-morphism | collage-art |
| Accessibility Audit | minimalism, flat-design, class-morphism | — |
| Motion Audit | minimalism, flat-design, aurora-ui | maximalism |
| Typography Audit | minimalism, class-morphism, retro | brutalism-ui |
| Spacing & Rhythm Audit | minimalism, flat-design, class-morphism | brutalism-ui |
| Interaction States Audit | minimalism, flat-design, class-morphism | — |
| Content & Microcopy Audit | minimalism, flat-design, class-morphism | — |
| Perceived Performance Audit | minimalism, flat-design, class-morphism | — |
| Responsive Audit | minimalism, flat-design, class-morphism | — |
| Audit Report Template | minimalism, class-morphism, flat-design | — |

## 🏃 Motion Affinity (skill-animation)

| Skill | Motion it pairs with | Motion to handle with care |
|---|---|---|
| Review Process | easing-timing | — |
| Visual Hierarchy Audit | easing-timing, entrance-exit | — |
| Consistency Audit | easing-timing | — |
| Accessibility Audit | reduced-motion, easing-timing | — |
| Motion Audit | easing-timing, micro-interactions, reduced-motion | ambient-motion |
| Typography Audit | easing-timing | — |
| Spacing & Rhythm Audit | easing-timing | — |
| Interaction States Audit | micro-interactions, feedback-confirmation | — |
| Content & Microcopy Audit | easing-timing | — |
| Perceived Performance Audit | loading-states, easing-timing | ambient-motion |
| Responsive Audit | easing-timing | — |
| Audit Report Template | easing-timing | — |

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12
- **Token prefix:** `--rev-*` (CSS custom properties; see `assets/css/`)
- **CI:** `python3 scripts/validate_skills.py` — 10 checks covering guides, data.json, CSS files, README matrix, and repo hygiene

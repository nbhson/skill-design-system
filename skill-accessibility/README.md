# ♿ Professional Accessibility Skill Set — 12 A11y Disciplines

A professional reference guide for 12 accessibility disciplines, each covering: definition, core principles, spec tokens (policies/thresholds/contracts), composition, signature patterns, real-world applications, combination notes, anti-patterns, accessibility notes, code examples, and an implementation checklist.

Companion repos: **skill-ui-ux** (12 design styles), **skill-animation** (12 motion disciplines), **skill-design-tokens** (12 token disciplines). This repo answers *"is it accessible?"* — the WCAG contract every other skill must satisfy. Every skill declares a `styleAffinity` mapping to skill-ui-ux style ids and a `motionAffinity` mapping to skill-animation discipline ids.

## 📂 Skill List

| # | Skill | Folder | Summary |
|---|-------|--------|---------|
| 1 | [WCAG Fundamentals](./skills/01-wcag-fundamentals/SKILL.md) | 01-wcag-fundamentals | The POUR principles, conformance levels, and the WCAG 2.2 success-criteria map that anchors every other accessibility decision. |
| 2 | [Color & Contrast](./skills/02-color-contrast/SKILL.md) | 02-color-contrast | WCAG 1.4.3/1.4.11 as designed-in properties: ratio thresholds, safe pairings, and contrast that survives dark mode and brands. |
| 3 | [Keyboard Navigation](./skills/03-keyboard-navigation/SKILL.md) | 03-keyboard-navigation | Everything operable by mouse works by keyboard: tab order, skip links, roving tabindex, and shortcut discipline (WCAG 2.1.1/2.4.3). |
| 4 | [Focus Management](./skills/04-focus-management/SKILL.md) | 04-focus-management | Where focus goes when UI changes: visible focus styling, modal traps, focus return, and announcements that keep orientation. |
| 5 | [ARIA Fundamentals](./skills/05-aria-fundamentals/SKILL.md) | 05-aria-fundamentals | The first rule of ARIA and the core vocabulary: roles, states, properties, live regions, and when native HTML wins. |
| 6 | [ARIA Widget Patterns](./skills/06-aria-patterns-widgets/SKILL.md) | 06-aria-patterns-widgets | The APG patterns - tabs, menus, combobox, dialog, listbox, grid - implemented exactly as specified: roles, keymaps, and state wiring. |
| 7 | [Forms & Error Handling](./skills/07-forms-errors/SKILL.md) | 07-forms-errors | Labels, descriptions, and error wiring that make forms operable and recoverable: 3.3.1, 3.3.2, 3.3.3, 4.1.3 done as wiring, not styling. |
| 8 | [Screen Reader Testing](./skills/08-screen-readers/SKILL.md) | 08-screen-readers | Testing with NVDA, JAWS, and VoiceOver: the pairing matrix, listening scripts, and what automated checks can never catch. |
| 9 | [Images, Media & Alt Text](./skills/09-media-alt-text/SKILL.md) | 09-media-alt-text | Alt text that carries meaning, audio descriptions, captions, and transcripts - WCAG 1.1.1, 1.2.1-1.2.6 as a content workflow. |
| 10 | [Cognitive & Content Accessibility](./skills/10-cognitive-content/SKILL.md) | 10-cognitive-content | Plain language, predictable behavior, helpful errors, and memory-friendly flows - WCAG 3.x for users with cognitive and learning disabilities. |
| 11 | [Zoom, Reflow & Responsive A11y](./skills/11-zoom-reflow/SKILL.md) | 11-zoom-reflow | 200% zoom, 320px reflow, orientation lock, and pointer alternatives - the responsive side of WCAG (1.4.4, 1.4.10, 1.3.4, 2.5.x). |
| 12 | [Testing & Audit Framework](./skills/12-testing-audit/SKILL.md) | 12-testing-audit | The three-layer a11y test strategy: automated CI, manual keyboard/zoom passes, and screen reader listening scripts - plus the audit report format. |

## 🤖 Machine-Readable Data / AI Agents

[`data.json`](./skills/data.json) — the full skill set as structured JSON (definitions, principles, spec tokens, composition, patterns, use cases, combinations, style/motion affinity, anti-patterns, accessibility contracts). The root [`SKILL.md`](./SKILL.md) acts as a router for AI agents.

```json
{
  "skills": [{
    "id": "color-contrast",
    "sections": {
      "tokens": [{ "role": "contrast-body-min", "value": "4.5:1", "notes": "..." }],
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

[`assets/references.md`](./skills/assets/references.md) — curated spec links (WCAG 2.2 understanding docs, ARIA APG), tool docs (axe-core, NVDA, VoiceOver), and screen reader keystroke references.

## 🎯 How to Use

1. **Select a discipline:** use the summary table to pick the skill that matches the accessibility task.
2. **Read SKILL.md:** each guide follows the 10-section standard (definition → principles → tokens → composition → patterns → applications → combinations → anti-patterns → code examples → checklist).
3. **Apply:** treat WCAG AA as the release gate; use `assets/css/<skill-id>.css` spec tokens as hard standards. For AI agents: use the root `SKILL.md` router, then the specific guide.

## 🔄 Quick Combination Matrix

Symbols: ✅ combines well · ⚠️ conditional — follow the pairing tips in section 7 · ❌ do not combine.

| | wcag | contrast | kbd | focus | aria | widgets | forms | sr | media | cog | zoom | audit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **WCAG Fundamentals** | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Color & Contrast** | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Keyboard Navigation** | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Focus Management** | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **ARIA Fundamentals** | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **ARIA Widget Patterns** | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Forms & Error Handling** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Screen Reader Testing** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ |
| **Images, Media & Alt Text** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ |
| **Cognitive & Content Accessibility** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| **Zoom, Reflow & Responsive A11y** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ |
| **Testing & Audit Framework** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |

## 🧭 Design Style Affinity (skill-ui-ux / skill-design-tokens)

| Skill | Styles it elevates | Styles it clashes with |
|---|---|---|
| WCAG Fundamentals | minimalism, flat-design | neumorphism, brutalism-ui |
| Color & Contrast | minimalism, flat-design, glassmorphism | brutalism-ui, collage-art |
| Keyboard Navigation | minimalism, flat-design | collage-art |
| Focus Management | minimalism, flat-design | brutalism-ui |
| ARIA Fundamentals | minimalism, flat-design | collage-art, maximalism |
| ARIA Widget Patterns | minimalism, flat-design, glassmorphism | collage-art |
| Forms & Error Handling | minimalism, flat-design | brutalism-ui |
| Screen Reader Testing | minimalism, flat-design | collage-art, maximalism |
| Images, Media & Alt Text | minimalism, flat-design | collage-art, maximalism |
| Cognitive & Content Accessibility | minimalism, flat-design | collage-art, maximalism |
| Zoom, Reflow & Responsive A11y | minimalism, flat-design | collage-art, maximalism |
| Testing & Audit Framework | minimalism, flat-design | — |

## 🏃 Motion Affinity (skill-animation)

| Skill | Motion it pairs with | Motion to handle with care |
|---|---|---|
| WCAG Fundamentals | reduced-motion, easing-timing | ambient-motion |
| Color & Contrast | reduced-motion | — |
| Keyboard Navigation | micro-interactions, easing-timing | gesture-drag |
| Focus Management | easing-timing, page-transitions | — |
| ARIA Fundamentals | easing-timing | — |
| ARIA Widget Patterns | micro-interactions, feedback-confirmation | — |
| Forms & Error Handling | feedback-confirmation | — |
| Screen Reader Testing | easing-timing | — |
| Images, Media & Alt Text | illustration-lottie | ambient-motion |
| Cognitive & Content Accessibility | reduced-motion | ambient-motion |
| Zoom, Reflow & Responsive A11y | reduced-motion, easing-timing | scroll-animation, ambient-motion |
| Testing & Audit Framework | reduced-motion | — |

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12
- **Token prefix:** `--a11y-*` (CSS custom properties; see `assets/css/`)
- **CI:** `python3 scripts/validate_skills.py` — 10 checks covering guides, data.json, CSS files, README matrix, and repo hygiene

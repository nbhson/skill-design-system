# ✍️ Professional Typography Skill Set — 12 Type Disciplines

A professional reference guide for 12 typography disciplines, each covering: definition, core principles, spec tokens (values/policies), composition, signature patterns, real-world applications, combination notes, anti-patterns, accessibility notes, code examples, and an implementation checklist.

Companion repos: **skill-ui-ux** (12 design styles), **skill-animation** (12 motion disciplines), **skill-design-tokens** (12 token disciplines). This repo answers *"how does the text work?"* — the reading layer of the design system. Every skill declares a `styleAffinity` mapping to skill-ui-ux style ids and a `motionAffinity` mapping to skill-animation discipline ids.

## 📂 Skill List

| # | Skill | Folder | Summary |
|---|-------|--------|---------|
| 1 | [Font Pairing & Selection](./skills/01-font-pairing/SKILL.md) | 01-font-pairing | Choosing type families that work together: contrast strategies, superfamily and companion approaches, licensing, and fallback stacks. |
| 2 | [Modular Type Scale](./skills/02-type-scale/SKILL.md) | 02-type-scale | A root-16px modular scale (ratio ~1.25) that covers body through display in 9 steps - hierarchy by stepping, never by improvising. |
| 3 | [Line-Height & Rhythm](./skills/03-line-height/SKILL.md) | 03-line-height | Leading inversely proportional to size: 1.1-1.2 display, 1.5 body, 1.7 long-form - plus the vertical rhythm that aligns text to the 4px grid. |
| 4 | [Letter-Spacing & Tracking](./skills/04-letter-spacing/SKILL.md) | 04-letter-spacing | Tracking that tightens with size and loosens for uppercase: the micro-typography that makes headlines breathe and labels read. |
| 5 | [Typographic Hierarchy](./skills/05-visual-hierarchy/SKILL.md) | 05-visual-hierarchy | Directing the eye with size, weight, color, and position - the four hierarchy levers applied through text roles instead of per-screen decoration. |
| 6 | [Fluid & Responsive Typography](./skills/06-fluid-responsive/SKILL.md) | 06-fluid-responsive | clamp()-interpolated type that scales with the viewport between scale stops - smooth scaling without breakpoint soup. |
| 7 | [Multilingual & Vietnamese Typography](./skills/07-multilingual-vietnamese/SKILL.md) | 07-multilingual-vietnamese | Diacritic stacking, line-height headroom, fallback stacks, and locale conventions - first-class type for Vietnamese and other marked scripts. |
| 8 | [Readability & Measure](./skills/08-readability-legibility/SKILL.md) | 08-readability-legibility | Line length (45-75ch), contrast of reading surfaces, paragraph spacing, and the legibility properties that make long text effortless. |
| 9 | [Webfont Loading & Performance](./skills/09-webfont-loading/SKILL.md) | 09-webfont-loading | Fast, stable font delivery: subsets, font-display, preload discipline, and layout-shift prevention (CLS) that keeps text readable while fonts arrive. |
| 10 | [Numeric & Tabular Figures](./skills/10-numeric-tabular/SKILL.md) | 10-numeric-tabular | Proportional vs tabular figures, OpenType features, and data-typography: numbers that align in tables and count in dashboards. |
| 11 | [Variable Fonts](./skills/11-variable-fonts/SKILL.md) | 11-variable-fonts | One file, many styles: weight/optical axes, named instances, and when a variable font beats static weights - plus the loading math. |
| 12 | [Accessible Typography](./skills/12-accessible-typography/SKILL.md) | 12-accessible-typography | The a11y floors for text: contrast, zoom, spacing overrides, dyslexia-friendly defaults, and semantic structure that AT can navigate. |

## 🤖 Machine-Readable Data / AI Agents

[`data.json`](./skills/data.json) — the full skill set as structured JSON (definitions, principles, spec tokens, composition, patterns, use cases, combinations, style/motion affinity, anti-patterns, accessibility contracts). The root [`SKILL.md`](./SKILL.md) acts as a router for AI agents.

```json
{
  "skills": [{
    "id": "type-scale",
    "sections": {
      "tokens": [{ "role": "size-lg", "value": "1.563rem", "notes": "..." }],
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

[`assets/references.md`](./skills/assets/references.md) — curated spec links (OpenType features, unicode-range), tool docs (Google Fonts, Fontsource, wakamaifondue), and typography learning resources.

## 🎯 How to Use

1. **Select a discipline:** use the summary table to pick the skill that matches the typography task.
2. **Read SKILL.md:** each guide follows the 10-section standard (definition → principles → tokens → composition → patterns → applications → combinations → anti-patterns → code examples → checklist).
3. **Apply:** treat the spec tokens from `assets/css/<skill-id>.css` as hard standards — one scale, closed weights, unitless leading, rem sizes. For AI agents: use the root `SKILL.md` router, then the specific guide.

## 🔄 Quick Combination Matrix

Symbols: ✅ combines well · ⚠️ conditional — follow the pairing tips in section 7 · ❌ do not combine.

| | pairing | scale | leading | tracking | hierarchy | fluid | multiling | reading | loading | numeric | variable | a11y |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Font Pairing & Selection** | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Modular Type Scale** | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Line-Height & Rhythm** | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Letter-Spacing & Tracking** | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Typographic Hierarchy** | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Fluid & Responsive Typography** | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Multilingual & Vietnamese Typography** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Readability & Measure** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ | ✅ |
| **Webfont Loading & Performance** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ | ✅ |
| **Numeric & Tabular Figures** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | ✅ |
| **Variable Fonts** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ |
| **Accessible Typography** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — |

## 🧭 Design Style Affinity (skill-ui-ux / skill-design-tokens)

| Skill | Styles it elevates | Styles it clashes with |
|---|---|---|
| Font Pairing & Selection | minimalism, flat-design, brutalism-ui | skeuomorphism |
| Modular Type Scale | minimalism, flat-design, class-morphism | collage-art |
| Line-Height & Rhythm | minimalism, flat-design | brutalism-ui, collage-art |
| Letter-Spacing & Tracking | minimalism, class-morphism, brutalism-ui | skeuomorphism, retro |
| Typographic Hierarchy | minimalism, flat-design, maximalism | skeuomorphism |
| Fluid & Responsive Typography | minimalism, flat-design, aurora-ui | collage-art, brutalism-ui |
| Multilingual & Vietnamese Typography | minimalism, flat-design, class-morphism | retro |
| Readability & Measure | minimalism, flat-design, class-morphism | collage-art, maximalism |
| Webfont Loading & Performance | minimalism, flat-design | maximalism |
| Numeric & Tabular Figures | minimalism, flat-design, class-morphism | collage-art |
| Variable Fonts | minimalism, flat-design, brutalism-ui | skeuomorphism |
| Accessible Typography | minimalism, flat-design, class-morphism | collage-art, brutalism-ui |

## 🏃 Motion Affinity (skill-animation)

| Skill | Motion it pairs with | Motion to handle with care |
|---|---|---|
| Font Pairing & Selection | easing-timing | — |
| Modular Type Scale | easing-timing | — |
| Line-Height & Rhythm | easing-timing | — |
| Letter-Spacing & Tracking | easing-timing | — |
| Typographic Hierarchy | entrance-exit | — |
| Fluid & Responsive Typography | easing-timing | — |
| Multilingual & Vietnamese Typography | easing-timing | — |
| Readability & Measure | easing-timing | — |
| Webfont Loading & Performance | easing-timing | — |
| Numeric & Tabular Figures | data-animation | — |
| Variable Fonts | easing-timing | ambient-motion |
| Accessible Typography | reduced-motion, easing-timing | — |

## Version

- **Schema version:** 1.0 (`skills/data.json` → `meta.version`)
- **Skills:** 12
- **Token prefix:** `--type-*` (CSS custom properties; see `assets/css/`)
- **CI:** `python3 scripts/validate_skills.py` — 10 checks covering guides, data.json, CSS files, README matrix, and repo hygiene

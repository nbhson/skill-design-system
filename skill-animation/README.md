# ⏱️ Professional UI Animation Skill Set — 12 Motion Disciplines

A professional reference guide for 12 UI animation disciplines, each covering: definition, core motion principles, duration/easing tokens, choreography, signature patterns, real-world applications, combination notes, anti-patterns, reduced-motion (accessibility) fallbacks, code examples, and an implementation checklist.

Companion repo: **skill-ui-ux** (12 design styles) — this repo answers *"how should it move?"*, that repo answers *"how should it look?"*. Every skill declares a `styleAffinity` mapping to the design-style ids of the companion repo.

## 📂 Skill List

| # | Skill | Folder | Summary |
|---|-------|--------|---------|
| 1 | [Duration & Easing Fundamentals](./skills/01-easing-timing/SKILL.md) | 01-easing-timing | The token foundation of all motion: a duration hierarchy and a small set of easing curves that make movement feel intentional instead of arbitrary. |
| 2 | [Micro-interactions](./skills/02-micro-interactions/SKILL.md) | 02-micro-interactions | Small, single-purpose feedback animations on interactive elements: hover, press, toggle, like, copy - the details that make UI feel alive. |
| 3 | [Entrance & Exit Choreography](./skills/03-entrance-exit/SKILL.md) | 03-entrance-exit | How elements appear and disappear: reveals, staggers, and coordinated sequences that establish hierarchy instead of dumping everything on screen at once. |
| 4 | [Page & View Transitions](./skills/04-page-transitions/SKILL.md) | 04-page-transitions | Movement between screens and routes: shared elements, directional slides, and the View Transitions API - keeping spatial context across navigation. |
| 5 | [Loading States](./skills/05-loading-states/SKILL.md) | 05-loading-states | Spinners, skeletons, progress, and optimistic UI: motion that manages waiting honestly, communicates progress, and hands off smoothly to real content. |
| 6 | [Feedback & Confirmation](./skills/06-feedback-confirmation/SKILL.md) | 06-feedback-confirmation | System-to-user communication: toasts, success checkmarks, destructive-action confirms, undo flows - motion that makes outcomes unambiguous. |
| 7 | [Scroll-Driven Animation](./skills/07-scroll-animation/SKILL.md) | 07-scroll-animation | Motion tied to scroll position: parallax, reveals, progress indicators, and sticky choreography - driven by the user's own input, not the clock. |
| 8 | [Gesture & Drag Physics](./skills/08-gesture-drag/SKILL.md) | 08-gesture-drag | Direct manipulation: drag, swipe, pull-to-refresh, fling with momentum and springs - motion that stays glued to the finger and lands with physics. |
| 9 | [Data & Chart Animation](./skills/09-data-animation/SKILL.md) | 09-data-animation | Animating numbers, charts, and live data: count-ups, bar/draw-in reveals, morphs between states, and updates that make change perceptible without lying. |
| 10 | [Ambient & Background Motion](./skills/10-ambient-motion/SKILL.md) | 10-ambient-motion | Slow, looping, atmospheric motion: aurora gradients, particles, blobs, marquee - depth and mood that must never compete with content. |
| 11 | [Illustration & Lottie](./skills/11-illustration-lottie/SKILL.md) | 11-illustration-lottie | Baked motion: character animation, mascots, empty states, and celebration via Lottie/Rive - designer-authored motion embedded as data. |
| 12 | [Reduced Motion & Accessibility](./skills/12-reduced-motion/SKILL.md) | 12-reduced-motion | The accessibility layer of motion: prefers-reduced-motion strategy, vestibular safety, focus management, and per-category fallbacks that keep meaning while removing movement. |

## 🤖 Machine-Readable Data / AI Agents

[`data.json`](./skills/data.json) — the full skill set as structured JSON (definitions, principles, tokens, choreography, patterns, use cases, combinations, style affinity, anti-patterns, reduced-motion fallbacks). The root [`SKILL.md`](./SKILL.md) acts as a router for AI agents.

```json
{
  "skills": [{
    "id": "easing-timing",
    "sections": {
      "tokens": [{ "role": "duration-fast", "value": "150ms", "notes": "..." }],
      "combinations": { "good": [], "caution": [], "avoid": [] },
      "styleAffinity": { "good": [], "caution": [], "avoid": [] },
      "antiPatterns": ["..."],
      "reducedMotion": { "required": true, "notes": "...", "fallback": "..." }
    }
  }]
}
```

## 📚 References

[`assets/references.md`](./skills/assets/references.md) — curated spec links (View Transitions API, CSS scroll-driven animations, WCAG 2.3.3), tool docs (Framer Motion, GSAP, Lottie, Rive), and easing curve libraries.

## 🎯 How to Use

1. **Select a discipline:** use the summary table to pick the skill that matches the motion task.
2. **Read SKILL.md:** each guide follows the 10-section standard (definition → principles → tokens → choreography → patterns → applications → combinations → anti-patterns → code examples → checklist).
3. **Apply:** consume the motion tokens from `assets/css/<skill-id>.css` as hard standards. For AI agents: use the root `SKILL.md` router, then the specific guide.

## 🔄 Quick Combination Matrix

Symbols: ✅ combines well · ⚠️ conditional — follow the pairing tips in section 7 · ❌ do not combine.

| | ease | micro | enter | page | load | feed | scroll | drag | data | amb | lottie | rm |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Duration & Easing Fundamentals** | — | ✅ | ✅ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ |
| **Micro-interactions** | ✅ | — | ✅ | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ | ❌ | ⚠️ | ⚠️ |
| **Entrance & Exit Choreography** | ✅ | ✅ | — | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | ⚠️ | ⚠️ | ⚠️ |
| **Page & View Transitions** | ✅ | ⚠️ | ✅ | — | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ | ❌ | ⚠️ | ⚠️ |
| **Loading States** | ✅ | ⚠️ | ✅ | ⚠️ | — | ✅ | ⚠️ | ✅ | ✅ | ❌ | ✅ | ⚠️ |
| **Feedback & Confirmation** | ✅ | ✅ | ✅ | ⚠️ | ✅ | — | ⚠️ | ✅ | ⚠️ | ❌ | ✅ | ⚠️ |
| **Scroll-Driven Animation** | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | — | ⚠️ | ✅ | ⚠️ | ✅ | ⚠️ |
| **Gesture & Drag Physics** | ⚠️ | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | — | ✅ | ❌ | ⚠️ | ⚠️ |
| **Data & Chart Animation** | ⚠️ | ⚠️ | ✅ | ⚠️ | ✅ | ⚠️ | ✅ | ✅ | — | ❌ | ⚠️ | ⚠️ |
| **Ambient & Background Motion** | ⚠️ | ❌ | ⚠️ | ❌ | ❌ | ❌ | ⚠️ | ❌ | ❌ | — | ✅ | ⚠️ |
| **Illustration & Lottie** | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ✅ | — | ⚠️ |
| **Reduced Motion & Accessibility** | ✅ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | ⚠️ | — |

## 🧭 Motion × Design Style Affinity (skill-ui-ux)

| Animation skill | Styles it elevates | Styles it clashes with |
|---|---|---|
| Duration & Easing Fundamentals | Minimalism, Flat Design, Glassmorphism | Retro, Brutalism UI |
| Micro-interactions | Neumorphism, Claymorphism, Glassmorphism | Minimalism, Flat Design |
| Entrance & Exit Choreography | Minimalism, Aurora UI, Glassmorphism | Brutalism UI, Retro |
| Page & View Transitions | Minimalism, Flat Design, Class Morphism | Brutalism UI, Collage Art |
| Loading States | Minimalism, Flat Design, Aurora UI | Neumorphism, Brutalism UI |
| Feedback & Confirmation | Minimalism, Flat Design, Neumorphism | Maximalism, Brutalism UI |
| Scroll-Driven Animation | Aurora UI, Collage Art, Maximalism | Minimalism, Neumorphism |
| Gesture & Drag Physics | Glassmorphism, Neumorphism, Claymorphism | Class Morphism, Retro |
| Data & Chart Animation | Minimalism, Flat Design, Aurora UI | Maximalism, Skeuomorphism |
| Ambient & Background Motion | Aurora UI, Glassmorphism, Maximalism | Minimalism, Flat Design |
| Illustration & Lottie | Claymorphism, Maximalism, Retro | Minimalism, Brutalism UI |
| Reduced Motion & Accessibility | Minimalism, Flat Design | Aurora UI, Maximalism, Retro |

## 🤖 AI Agent Usage

The root [`SKILL.md`](./SKILL.md) is a motion router: it maps tasks ("make a toast", "page should transition", "animate the chart") to the right discipline guide. Load it whenever a task involves animation, transitions, motion design, or micro-interactions. Every guide's Accessibility Notes declare the `prefers-reduced-motion` fallback — always apply it.

## ✅ Validation

```bash
python3 scripts/validate_skills.py
```

10 checks: SKILL.md existence, data.json validity, anti-patterns MD↔JSON consistency, token formats, combination symmetry, README matrix ↔ data.json, reference URLs, CSS tokens ↔ data.json, repo hygiene, extended sections + reducedMotion coverage.

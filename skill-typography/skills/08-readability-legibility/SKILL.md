---
name: readability-legibility
description: Line length (45–75ch), contrast of reading surfaces, paragraph spacing, and the legibility properties that make long text effortless.
tags: [readability, measure, legibility, contrast, long-form]
related: [line-height, type-scale, accessible-typography]
---

# Typography Skill: Readability & Measure

## 1. Definition

Readability is how effortlessly users process running text: line length (45–75 characters), comfortable leading, adequate contrast, and clean paragraphs. Legibility is the glyph-level property — open apertures, tall x-height, distinct 1/I/l and O/0. Together they decide whether users read the page or bounce; both are tokenizable (measure, leading, size) and both have WCAG floors (contrast 1.4.3, spacing 1.4.12). The reading triangle — size × leading × measure — must be tuned together, not individually.

## 2. Core Principles

- **Measure 45–75ch, ideal ~66:** longer lines lose the return path; shorter ones chop the reading rhythm.
- **Body size 16–18px minimum:** below 16px, screen-distance reading degrades measurably — 14px is the floor for UI labels, not paragraphs.
- **Contrast of reading surfaces:** body text passes 4.5:1 (AA) always; long-form reading surfaces target 7:1 (AAA).
- **Left-align, ragged right:** justified text creates rivers and uneven word spacing; hyphenation needs care per language.
- **Paragraph rhythm:** 1.7 leading + one blank line (or space-4) between paragraphs — spacing signals structure more than indenting.
- **Legibility check the letterforms:** open apertures (a, e, c), tall x-height, distinct 1/l/I and O/0 — test at 14px where detail collapses first.
- **Reading width shrinks on zoom:** at 200% zoom the 66ch paragraph reflows — the measure is in ch, so it self-adapts.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Measure ideal | `--type-measure-ideal` | `66ch` | Default paragraph max-width |
| Measure range | `--type-measure-range` | `45-75ch` | The acceptable band; outside it, split columns |
| Body size floor | `--type-body-size-floor` | `1rem` | 16px minimum for paragraphs |
| UI label floor | `--type-ui-label-floor` | `0.875rem` | 14px floor for UI labels/captions |
| Reading contrast | `--type-reading-contrast` | `7:1` | AAA target for long-form surfaces |
| Paragraph spacing | `--type-paragraph-spacing` | `1em` | One blank line between paragraphs |
| Alignment policy | `--type-alignment-policy` | `left-ragged` | Justify only with hyphenation review |
| Line height (longform) | `--type-line-height-longform` | `1.7` | Relaxed leading for articles/docs |
| Legibility glyph test | `--type-legibility-glyph-test` | `1lI-O0-pass` | Letterform disambiguation check at 14px |
| Zoom measure | `--type-zoom-measure` | `ch-based` | Measure adapts at zoom (ch scales with font) |

Consume by linking `assets/css/readability-legibility.css` in the article/documentation layout shell, then applying `var(--type-measure-ideal)`, `var(--type-line-height-longform)`, and `var(--type-paragraph-spacing)` to the `.prose` container — product components never hardcode these values.

## 4. Composition

- Composes with line-height and type-scale: the reading triangle (size × leading × measure) must be tuned together — a 1.5 leading at 66ch reads differently than the same leading at 45ch.
- Composes with color-contrast (skill-design-tokens): the 7:1 reading target is enforced on text aliases drawn from the color ramp — the contrast decision and the measure decision are co-dependent.
- Composes with accessible-typography: every readability floor is also an accessibility floor — the WCAG articles they cite are the same documents.

## 5. Signature Patterns

- **Reading component:** one `.prose` class owns measure, leading, size, and spacing for all articles — long-form text is never styled ad hoc in product components.
- **Glyph stress test:** render `1lI O0` and dense paragraphs at 14px in QA — the face that fails here fails everywhere; no face with ambiguous 1/l/I at 14px enters the stack.

## 6. Real-World Use Cases

- **Documentation platforms and news sites** (the 66ch measure is their spine) — tune the prose container once and it propagates to every article.
- **Email readers and RSS clients** where users read for minutes — message bodies that break the 75ch ceiling lose the reader in the first scroll.
- **Audit:** measuring actual rendered line lengths and paragraph spacing on existing content — many products ship at 120ch and don't realize it until measured.

## 7. Combination Notes

### With other typography skills

- **Pairs naturally with line-height and type-scale:** the reading triangle is the canonical composition — size, leading, and measure tuned together as one decision, not three.
- **Pairs with accessible-typography:** every readability floor doubles as an accessibility floor — the WCAG citations are identical.
- **Pairs with fluid-responsive:** measure in ch handles reflow at zoom naturally; combining fluid type tokens with ch-based measure produces the most resilient reading layout.
- **Caution with numeric-tabular:** tabular figures in long-form prose create stiff, unnatural rhythm — `tabular-nums` is a data-table concern, not an article concern.

### With design styles (companion repo skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** both styles use restrained columns and whitespace that naturally accommodate the 66ch measure.
- **Caution with collage-art and maximalism:** both may deliberately break the measure ceiling for editorial effect — if so, the break must be conscious and annotated, not accidental.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** reading-progress indicators and scroll-driven paragraph reveals should respect the `--type-line-height-longform` token — fast reveals disrupt reading flow.
- **Caution with ambient-motion:** animated backgrounds that pulse or shift can break the static-contrast requirement mid-cycle — resting state must hold 7:1 for long-form surfaces.

## 8. Anti-Patterns

- **Full-width paragraphs** — 120ch lines that make eyes lose the return path
- **Tiny gray text** — 13px #999 body that fails contrast and legibility simultaneously
- **Justified rivers** — text-align: justify without hyphenation — uneven word gaps
- **Wall-of-text** — no paragraph breaks, no headings, 2000-word blocks

### Accessibility Notes

This guide enforces the reading-side WCAG floors: 1.4.3 (contrast), 1.4.4 (zoom reflow — the ch-based measure self-adapts at 200% zoom), 1.4.8 (visual presentation — measure, leading, justification), and 1.4.12 (text spacing overrides — the `--type-paragraph-spacing` and `--type-line-height-longform` tokens are the implementation of that requirement). The fallback rule: when a design needs a wider measure, split into columns using CSS `columns` rather than stretching lines — the 75ch ceiling is a hard limit, not a suggestion.

## 9. Code Examples

### Example 1 — `.prose` article block with reading triangle tokens

```html
<article class="prose">
  <h1>On the Craft of Reading</h1>
  <p>The measure — the length of a line — is the most undervalued constraint in
     editorial design. Too wide and the eye loses the return path; too narrow and
     the rhythm shatters.</p>
  <p>Combined with comfortable leading, a disciplined measure creates reading
     that feels effortless.</p>
  <div class="glyph-test" aria-hidden="true">1lI O0</div>
</article>
<style>
  @import url('assets/css/readability-legibility.css');
  @import url('assets/css/color-tokens.css');

  .prose {
    max-width: var(--type-measure-ideal, 66ch);
    margin-inline: auto;
    padding-inline: 1.5rem;
    font-size: var(--type-body-size-floor, 1rem);
    line-height: var(--type-line-height-longform, 1.7);
    color: var(--dt-color-neutral-900);
  }
  .prose h1 {
    font-size: 2rem;
    font-weight: 700;
    line-height: 1.2;
    margin-bottom: 1em;
    color: var(--dt-color-neutral-900);
  }
  .prose p {
    margin-bottom: var(--type-paragraph-spacing, 1em);
    color: var(--dt-color-neutral-700);
  }
  /* Legibility stress row — must remain readable at label size */
  .glyph-test {
    font-size: var(--type-ui-label-floor, 0.875rem);
    letter-spacing: 0.05em;
    color: var(--dt-color-neutral-500);
    margin-top: 2rem;
  }
</style>
```

### Example 2 — Two-column layout respecting the 75ch ceiling

```html
<section class="article-section">
  <h2>Typography in Practice</h2>
  <div class="two-col">
    <p>Readable type scales with the viewport and with the user's chosen font
       size. Using rem and ch units together produces layouts that hold up under
       magnification.</p>
    <p>The ch unit is tied to the zero glyph of the current font — it is not a
       fixed pixel value. This means a 66ch measure adapts when the font changes,
       when the user zooms, or when the browser's default font size changes.</p>
  </div>
</section>
<style>
  @import url('assets/css/readability-legibility.css');

  .article-section { padding: 2rem 1.5rem; }
  .article-section h2 {
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 1rem;
  }
  .two-col {
    columns: 2;
    column-gap: 2.5rem;
    column-fill: auto;
    max-width: var(--type-measure-ideal, 66ch);
    /* Each column is ~33ch — within the 45-75ch band */
  }
  .two-col p {
    font-size: var(--type-body-size-floor, 1rem);
    line-height: var(--type-line-height-longform, 1.7);
    margin-bottom: var(--type-paragraph-spacing, 1em);
    text-align: left; /* ragged right: no justify rivers */
    break-inside: avoid-column;
  }
</style>
```

## 10. Implementation Checklist

- [ ] All prose/article containers set `max-width: var(--type-measure-ideal, 66ch)` — no full-width paragraphs anywhere.
- [ ] `--type-body-size-floor` (1rem / 16px) is the paragraph minimum; UI labels use the separate `--type-ui-label-floor` (0.875rem).
- [ ] `--type-line-height-longform` (1.7) applied to all long-form text containers; `--type-paragraph-spacing` (1em) used for paragraph breaks.
- [ ] `text-align: left` with ragged right is the default; `justify` is only applied after hyphenation review per language.
- [ ] Contrast on reading surfaces targets `--type-reading-contrast` (7:1) — alias colors drawn from the ramp, not arbitrary hexes.
- [ ] Measure uses `ch` units throughout — `var(--type-zoom-measure, ch-based)` — so reflow at 200% zoom is automatic.
- [ ] Font adoption scorecard includes the `--type-legibility-glyph-test` (1lI-O0) check at `--type-ui-label-floor` — ambiguous letterforms disqualify the face.
- [ ] CSS `columns` used for multi-column layouts instead of stretching measure past 75ch.

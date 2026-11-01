---
name: accessible-writing
description: Writing for assistive tech and cognition: alt text as copy, descriptive links, reading order, and plain-language inclusion.
tags: [accessibility, alt-text, plain-language, screen-readers, inclusion]
related: [writing-principles, component-microcopy, copy-audit]
---

# UX Writing Guide: Accessible & Inclusive Writing

## 1. Definition

Accessible writing treats every string as something that may be read aloud or processed under cognitive load. Alt text is copy — descriptive, purposeful, brief — not a caption exercise; link text names destinations because screen reader users navigate by link list; headings form an outline that must be traversable without skips; aria-labels follow the same voice standards as visible text; and reading order matches visual order unless a deviation is a documented pattern. The discipline bridges ux-writing and skill-accessibility: the criteria (WCAG success criteria, AT behavior) live there, while the phrasing craft — how a string is worded so it survives being heard out of context, truncated at 40 characters, or read under stress — lives here.

## 2. Core Principles

- **Alt text is copy:** it describes purpose ('Chart: revenue up 34% Q3'), not appearance ('bar chart image') — and decorative images get empty alt.
- **Link text names the destination:** 'Read the migration guide', never 'Click here' — AT users navigate by link list.
- **Headings are the outline:** h1–h6 without skips; users with screen readers navigate by heading — heading text must summarize its section.
- **Aria-labels follow the voice charter:** machine-read strings get the same clarity, specificity, and tone as visible copy.
- **Reading order = visual order (or is deliberate):** DOM order matches presentation unless the deviation is a documented pattern.
- **Plain language is the cognitive default:** 8th-grade target, expanded abbreviations, meaning carried by words not formatting.
- **Front-load meaning in strings:** AT and truncated previews both cut the tail — put the payload first ('Error: payment declined').
- **Inclusive by default:** people-first, gender-neutral where the language allows, and no idioms that exclude non-native readers in critical paths.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Alt text rule | `--uxw-alt-text-rule` | `purpose-descriptive` | Decorative images: alt empty |
| Alt length | `--uxw-alt-length` | `~1-sentence` | Longer descriptions: longdesc/adjacent text |
| Link text | `--uxw-link-text` | `destination-named` | WCAG 2.4.4; never 'click here' |
| Heading outline | `--uxw-heading-outline` | `no-skips+summaries` | Heading text summarizes its section |
| Aria-label voice | `--uxw-aria-label-voice` | `same-charter-as-visible` | Machine-read strings are copy too |
| Reading order | `--uxw-reading-order` | `dom-matches-visual` | Deviations documented |
| Front-load rule | `--uxw-front-load-rule` | `payload-first` | 'Error: ...' not 'Oops, ...: error' |
| Reading level | `--uxw-reading-level` | `grade-8` | Shared with writing-principles |
| Inclusive language | `--uxw-inclusive-language` | `people-first+neutral` | Default stance; house style may adjust |
| Abbrev expansion | `--uxw-abbr-expansion` | `first-use` | Abbreviations expanded once, then free |

Consume them by linking `assets/css/accessible-writing.css` and referencing `var(--uxw-...)` wherever copy policy meets presentation — front-loaded status text, alt-length budgets, and link styling all resolve through these custom properties so the writing contract is inspectable, not tribal.

## 4. Composition

- **Composes with writing-principles (guide 01):** plain language and front-loading are inherited contracts — this guide operationalizes them for assistive tech and cognition, not just readability.
- **Composes with skill-accessibility screen-readers + cognitive-content:** those guides own the criteria and the testing method; this guide owns the phrasing that makes surfaces pass them well.
- **Composes with component-microcopy (guide 07):** aria-labels, tooltips, and hint text are the machine-read half of microcopy — same voice charter, different channel.

## 5. Signature Patterns

- **The AT read-through:** any new surface is read with a screen reader (or VoiceOver rotator) before ship — the copy is edited exactly where the narration stumbles, which is the only test that surfaces aria-label drift.
- **The alt-text decision tree:** informative (describe purpose) → functional (state action: 'Search') → decorative (empty alt) — every image is classified before alt text is written, because the wrong branch produces the wrong sentence.

## 6. Real-World Use Cases

- **Every surface with images, links, or headings** — which is every surface; this guide is a default, not a special case.
- **Government and education products with WCAG conformance mandates,** where copy-level failures are audit findings.
- **Auditing an existing product** for 'click here' links, appearance-describing alt text, and skipped heading levels.

## 7. Combination Notes

### With other ux-writing skills

- **Good with writing-principles, error-messages, forms-labels, empty-states, button-labels, notifications, onboarding-copy, and component-microcopy:** these guides produce the strings this guide stress-tests — every error message, toast, and button label must survive being read aloud out of context, which is exactly the AT condition.
- **Good with copy-audit and localization-i18n:** alt text, link text, and heading outline are audit scorecard rows, and translated strings inherit the same accessibility contract per locale — an audit that skips them is incomplete.
- **No caution or avoid list:** accessible phrasing never conflicts with sibling guides — when a tension appears (e.g. brevity vs description), the three-part contracts usually resolve it, and the fallback rules carry the rest.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism, flat-design, and class-morphism:** these styles keep visual hierarchy clean and text-forward, which makes DOM-order-matches-visual-order cheap and heading outlines natural — the copy and the structure agree.
- **No caution list:** no style mandates inaccessible copy; the risk in expressive styles (collage, maximalism) is layout complexity, which this guide flags through reading-order review rather than banning the style.

### With motion skills (companion repo skill-animation)

- **Good affinity with reduced-motion and easing-timing:** surfaces written for cognitive load benefit directly from motion that respects vestibular triggers — `prefers-reduced-motion` handling is part of the same inclusive default, and easing tokens keep state changes readable.
- **No caution list:** animation and accessible writing intersect only at motion-triggered text reveals, where the rule is simple — meaning must not depend on catching a transient animation.

## 8. Anti-Patterns

- **Appearance alt** — 'image of a graph' telling screen reader users nothing
- **Click here** — link lists rendered useless in AT navigation
- **Heading skips** — h2 to h5 jumps breaking the document outline
- **Verbose aria-labels** — machine strings stuffed with marketing copy

### Accessibility Notes

This guide is the phrasing layer of WCAG 1.1.1 (non-text content), 1.3.1/1.3.2 (info and relationships, meaningful sequence), 2.4.4 (link purpose), 2.4.6 (headings and labels), and 3.1.5 (reading level): descriptive alt text, named links, ordered reading, headings that summarize, and plain language — the craft decisions that make the a11y repo's structural criteria read well rather than merely pass. The fallback for teams without AT testing in the loop is concrete: run the link-list review and the heading-outline review manually (browser extensions surface both in seconds) — those two passes catch the majority of copy-level accessibility failures, and they double as documentation of the page's information architecture.

## 9. Code Examples

### Example 1 — Alt-text decision tree: informative, functional, decorative

Tokens: `assets/css/accessible-writing.css`

```html
<div class="alt-demo">
  <figure>
    <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='60'%3E%3Crect width='120' height='60' fill='%232563EB'/%3E%3Ctext x='60' y='35' fill='white' text-anchor='middle' font-size='18'%3E+34%25%3C/text%3E%3C/svg%3E"
         alt="Chart: revenue up 34% in Q3">
    <figcaption>Informative → describe the purpose, not the pixels</figcaption>
  </figure>
  <figure>
    <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24'%3E%3Ccircle cx='11' cy='11' r='8' fill='none' stroke='%23171717' stroke-width='2'/%3E%3Cline x1='16' y1='16' x2='22' y2='22' stroke='%23171717' stroke-width='2'/%3E%3C/svg%3E"
         alt="Search">
    <figcaption>Functional → state the action the control performs</figcaption>
  </figure>
  <figure>
    <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='8'%3E%3Crect width='120' height='8' fill='%23D4D4D4'/%3E%3C/svg%3E"
         alt="">
    <figcaption>Decorative → empty alt, so AT skips it entirely</figcaption>
  </figure>
</div>
<style>
  .alt-demo { display: flex; gap: 16px; font: 13px/1.5 Inter, system-ui, sans-serif; }
  .alt-demo figure { margin: 0; padding: 12px; border: 1px solid var(--uxw-alt-text-rule, #ddd); border-radius: 8px; max-width: 180px; }
  .alt-demo img { display: block; margin-bottom: 8px; }
  .alt-demo figcaption { color: var(--uxw-reading-level, #404040); font-size: 12px; }
</style>
```

### Example 2 — Link-list read-through and heading outline (the AT view)

Tokens: `assets/css/accessible-writing.css`

```html
<article class="doc">
  <h1>Migrating workspaces</h1>
  <p>Before you start, <a href="#">read the migration guide</a> — the old
     <a href="#">click here</a> page is deprecated.</p>
  <h2>Step 1: Export your data</h2>
  <p>Export first. <a href="#">Click here</a> to open the export tool.</p>
  <h3>Export formats</h3>
  <p>CSV and JSON are supported.</p>
  <h4>Skipped to h4 — this breaks the outline</h4>
  <p id="at-report" class="at-report"></p>
</article>
<script>
  // AT navigation aids: the link list and the heading outline, as a screen reader sees them
  const links = [...document.querySelectorAll('.doc a')];
  const headings = [...document.querySelectorAll('.doc h1, .doc h2, .doc h3, .doc h4, .doc h5, .doc h6')];
  const violations = [];
  // --uxw-link-text: 'click here' names the mechanism, not the destination (WCAG 2.4.4)
  links.forEach(a => { if (/click here/i.test(a.textContent)) violations.push(`Link "click here" → use: ${dest(a)}`); });
  function dest(a) { return a.href.includes('guide') ? 'Read the migration guide' : 'Open the export tool'; }
  // --uxw-heading-outline: no level skips
  let prev = 0;
  headings.forEach(h => {
    const level = +h.tagName[1];
    if (prev && level > prev + 1) violations.push(`Heading skip: h${prev} → h${level} on "${h.textContent}"`);
    prev = level;
  });
  document.getElementById('at-report').innerHTML =
    '<strong>Link list (AT view):</strong> ' + links.map(a => `“${a.textContent}”`).join(', ') +
    '<br><strong>Heading outline:</strong> ' + headings.map(h => h.tagName + ': ' + h.textContent).join(' · ') +
    '<br><strong>Findings:</strong> ' + (violations.length ? violations.join(' | ') : 'none');
</script>
<style>
  .doc { font: 14px/1.6 Inter, system-ui, sans-serif; max-width: 460px; padding: 16px; border: 1px solid var(--uxw-front-load-rule, #ddd); border-radius: 8px; }
  .doc h1 { font-size: 18px; } .doc h2 { font-size: 16px; } .doc h3 { font-size: 14px; } .doc h4 { font-size: 13px; }
  .doc a { color: #1D4ED8; }
  .at-report { border-top: 1px solid #e5e5e5; padding-top: 8px; font-size: 12px; color: #404040; }
</style>
```

## 10. Implementation Checklist

- [ ] Every image is classified via the decision tree (informative/functional/decorative) and its alt follows the branch (`--uxw-alt-text-rule`, `--uxw-alt-length`).
- [ ] No link reads 'click here', 'read more', or a bare URL — every link names its destination (`--uxw-link-text`).
- [ ] Heading levels run h1–h6 without skips, and each heading summarizes its section (`--uxw-heading-outline`).
- [ ] Aria-labels meet the same voice charter as visible copy — no marketing strings in machine-read text (`--uxw-aria-label-voice`).
- [ ] DOM order matches visual order; any deviation is a documented pattern (`--uxw-reading-order`).
- [ ] Status and error strings front-load the payload ('Error: payment declined') so truncation and narration keep the meaning (`--uxw-front-load-rule`).
- [ ] Copy targets grade-8 reading level with abbreviations expanded on first use (`--uxw-reading-level`, `--uxw-abbr-expansion`).
- [ ] Critical-path strings avoid idiom and use people-first, gender-neutral language (`--uxw-inclusive-language`).

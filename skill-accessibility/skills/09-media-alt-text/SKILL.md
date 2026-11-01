---
name: media-alt-text
description: Alt text that carries meaning, audio descriptions, captions, and transcripts - WCAG 1.1.1, 1.2.1-1.2.6 as a content workflow.
tags: [alt-text, images, media, captions, wcag]
related: [aria-fundamentals, cognitive-content, screen-readers]
---

# Accessibility Skill: Images, Media & Alt Text

## 1. Definition

Non-text content must have a text alternative (WCAG 1.1.1), and prerecorded media needs captions and audio description (1.2.x). Alt text is a writing discipline, not a formality: good alt conveys the image's purpose in context, bad alt ('image', 'photo123.jpg') or missing alt excludes screen reader users from the content's meaning. This skill covers alt writing rules, decorative handling, complex images, and the media timeline (captions, transcripts, descriptions) - treating every image, icon, chart, and video as a content decision that ships through the CMS and the component library, not a last-minute attribute someone fills in at deploy time.

## 2. Core Principles

- **Alt describes purpose, not appearance:** 'CEO shaking hands with the minister at the signing' - not 'two people in suits'.
- **Decorative images get empty alt:** alt='' removes them from narration; omitting the attribute makes readers announce the filename.
- **Functional images describe the action:** a magnifier icon button is 'Search', not 'magnifying glass'.
- **Complex images need long descriptions:** charts and diagrams pair short alt with adjacent text or a data table.
- **Text in images is a smell:** real text scales, translates, and translates contrast; images-of-text fail 1.4.5 unless essential.
- **Captions are not subtitles:** captions include speaker IDs and relevant sound cues (WCAG 1.2.2-1.2.4).
- **Audio description for prerecorded video:** 1.2.3/1.2.5 - narration of visual information between dialogue.
- **Icons adjacent to visible text are decorative:** the label already says it; alt='' prevents double narration.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Alt policy | `--a11y-alt-policy` | `purpose-driven` | Alt answers 'why is this image here' in its context |
| Alt length guide | `--a11y-alt-length-guide` | `under-150-chars` | Concise; complex images get longdesc/adjacent text instead |
| Decorative handling | `--a11y-decorative-handling` | `alt-empty` | alt='' + never omitted attribute |
| Functional alt | `--a11y-functional-alt` | `describe-action` | Icon buttons name the action, not the glyph |
| Complex image policy | `--a11y-complex-image-policy` | `alt-plus-data-table` | Charts: short alt + accessible data table nearby |
| Images of text | `--a11y-images-of-text` | `avoid` | WCAG 1.4.5 unless logotype/essential |
| Captions policy | `--a11y-captions-policy` | `closed+speaker-ids` | WCAG 1.2.2/1.2.4: speaker identification + sound cues |
| Audio description | `--a11y-audio-description` | `prerecorded-required` | WCAG 1.2.3/1.2.5 for video |
| Transcript policy | `--a11y-transcript-policy` | `audio-required` | Podcasts/audio get full transcripts (1.2.1) |
| Icon with label | `--a11y-icon-with-label` | `alt-empty` | Visible text label carries the name; icon is decorative |

Consume them by linking `assets/css/media-alt-text.css` once: the policy tokens are read by the CMS templates and image components (the editor prompt that asks an image's purpose, the figure component that renders the alt-plus-table pattern) via `var(--a11y-...)` references, so alt conventions are enforced by the templates rather than by every author's memory. A component library that invents its own icon-button labeling instead of reading `--a11y-functional-alt` produces double narration that no individual audit fully catches.

## 4. Composition

- **Composes with aria-fundamentals:** empty alt is aria-hidden's sibling - both remove decoration from the AT tree; the fundamentals skill defines the mechanism, this skill defines when decoration is decoration.
- **Composes with icons-illustration (skill-icons-illustration):** icon systems and illustration sets ship with alt/label conventions baked in - the icon component decides functional vs decorative once, and consumers inherit the decision.
- **Composes with cognitive-content:** transcripts and captions serve deaf, blind, and cognitive-needs users simultaneously - the same artifact satisfies 1.2.1 and plain-language goals, which is why transcripts are `audio-required`, not optional.

## 5. Signature Patterns

- **Alt review in CMS workflow:** content templates enforce alt presence - empty allowed, missing not - with an editor prompt asking the image's purpose in context; the check is structural (a required field that may be left blank), so it survives staff turnover.
- **Chart alt pattern:** short alt states the takeaway ('Sales up 20% Q3'), followed by the full data table for users who want the numbers - one artifact, two depths, and the table is reusable by analysts as well.

## 6. Real-World Use Cases

- **Content-heavy sites** - editorial images, charts, and infographics where meaning lives in visuals.
- **Video/audio products** - captions, transcripts, and description pipelines for prerecorded media.
- **Icon buttons and image links** - functional naming across the entire UI chrome.

## 7. Combination Notes

### With other accessibility skills

- **Pairs naturally with aria-fundamentals:** the decorative/functional distinction is the same AT-tree decision as aria-hidden vs accessible name - learn the fundamentals once and alt decisions follow the same model.
- **Pairs with screen-readers and testing-audit:** listening is how you hear that alt reads sensibly in context (a filename or 'image of' is unmistakable by ear), and the audit stores alt checks as a manual lane because automation only detects presence, not quality.
- **Pairs with cognitive-content:** transcripts and captions double as plain-language artifacts - the fallback text and the readability pass are the same writing work.
- **Pairs with keyboard-navigation and forms-errors:** functional images are usually interactive (icon buttons, image links), so their accessible names must compose with label policy and focus treatment.
- **Caution: none, avoid: none.** Alt and media access are leaf concerns consumed by every surface; no sibling skill conflicts with a text alternative - conflicts arise only when alt is skipped.

### With design styles (companion repos skill-ui-ux / skill-design-tokens)

- **Good affinity with minimalism and flat-design:** fewer, purposeful images make purpose-driven alt cheap - a disciplined visual layer means every image has a reason to be there, which is exactly the question `--a11y-alt-policy` asks.
- **Caution with collage-art and maximalism:** layered compositions and image-dense layouts multiply decorative-vs-functional decisions and invite images-of-text; if adopted, the CMS alt review gate becomes the load-bearing control, and decorative clusters should be grouped under one empty-alt container rather than narrated individually.

### With motion skills (companion repo skill-animation)

- **Good affinity with illustration-lottie:** animated illustrations are still non-text content - they need text alternatives, and the animation token system should carry the alt/label convention alongside the motion spec.
- **Caution with ambient-motion:** looping background media is almost always decorative and must be alt='' (or aria-hidden) so it never enters narration - and it must respect reduced-motion fallbacks per the companion repo.

## 8. Anti-Patterns

- **Filename alt** — IMG_2384.jpg narrated as content
- **Alt on everything** — 'logo: logo' decoration read aloud twice on every page
- **Alt that starts 'image of'** — screen readers already announce it as an image
- **Auto-captions only** — raw ASX captions with no speaker IDs, punctuation, or review

### Accessibility Notes

This guide owns WCAG 1.1.1 and the 1.2.x media criteria - Level A essentials that block conformance entirely when missing: a page with a meaningful image and no alt fails Level A, full stop, regardless of how strong the rest of the product is. The tokens encode the discipline as contracts: `--a11y-alt-policy` (purpose-driven) and `--a11y-alt-length-guide` (under-150-chars) govern the writing, `--a11y-decorative-handling` and `--a11y-icon-with-label` govern suppression, `--a11y-complex-image-policy` governs charts, and `--a11y-captions-policy`, `--a11y-audio-description`, and `--a11y-transcript-policy` govern the media timeline. The fallback rule: if quality alt cannot be produced in time, ship a descriptive caption below the image rather than an empty guess - a plain-text description is always better than silence.

## 9. Code Examples

### Example 1 — Alt-writing review table (good vs bad, per `--a11y-alt-policy`)

Tokens: `assets/css/media-alt-text.css`

```html
<table class="alt-review">
  <caption>Alt review — editorial batch 2026-10 (policy: var(--a11y-alt-policy))</caption>
  <thead>
    <tr><th scope="col">Image context</th><th scope="col">Bad alt</th><th scope="col">Good alt</th></tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Signing ceremony photo atop a trade-deal article</th>
      <td class="bad">IMG_2384.jpg</td>
      <td class="good">CEO shaking hands with the minister at the signing</td>
    </tr>
    <tr>
      <th scope="row">Q3 revenue chart in a results page</th>
      <td class="bad">Chart</td>
      <td class="good">Bar chart: sales up 20% in Q3 — full data below</td>
    </tr>
    <tr>
      <th scope="row">Magnifier icon next to the search box</th>
      <td class="bad">magnifying glass</td>
      <td class="good">alt="" — the visible label "Search" carries the name</td>
    </tr>
    <tr>
      <th scope="row">Divider flourish between article sections</th>
      <td class="bad">divider.png</td>
      <td class="good">alt="" — decorative, suppressed from narration</td>
    </tr>
  </tbody>
</table>
<style>
  .alt-review { max-width: 720px; border-collapse: collapse; font: 14px/1.5 system-ui, sans-serif; }
  .alt-review caption { caption-side: top; text-align: left; font-weight: 600; padding: 8px 0; }
  .alt-review th, .alt-review td { border: 1px solid #D4D4D4; padding: 8px 12px; text-align: left; }
  .alt-review thead th { background: #F5F5F5; }
  .bad  { color: #B91C1C; font-family: ui-monospace, monospace; font-size: 13px; }
  .good { color: #166534; }
</style>
```

### Example 2 — Figure with short alt + adjacent data table, and a captioned video

Tokens: `assets/css/media-alt-text.css`

```html
<figure>
  <img src="q3-revenue.png"
       alt="Bar chart: sales up 20% in Q3, led by the EMEA region."
       aria-describedby="q3-table" /> <!-- --a11y-complex-image-policy: alt-plus-data-table -->
  <figcaption>Q3 revenue by region — full figures in the table below.</figcaption>
  <table id="q3-table">
    <caption>Q3 revenue by region (USD millions)</caption>
    <tr><th scope="col">Region</th><th scope="col">Q2</th><th scope="col">Q3</th><th scope="col">Change</th></tr>
    <tr><th scope="row">EMEA</th><td>4.1</td><td>5.2</td><td>+27%</td></tr>
    <tr><th scope="row">Americas</th><td>6.0</td><td>6.8</td><td>+13%</td></tr>
    <tr><th scope="row">APAC</th><td>2.4</td><td>2.7</td><td>+12%</td></tr>
  </table>
</figure>

<video controls preload="none" poster="townhall.jpg">
  <source src="townhall.mp4" type="video/mp4" />
  <track kind="captions" src="townhall-captions.vtt" srclang="en" label="English CC" default />
  <!-- --a11y-captions-policy: closed + speaker IDs; --a11y-audio-description: prerecorded-required -->
  <track kind="descriptions" src="townhall-desc.vtt" srclang="en" label="Audio descriptions" />
  Your browser does not support embedded video.
  <a href="townhall-transcript.html">Read the full transcript</a> <!-- --a11y-transcript-policy -->
</video>
<style>
  figure, video { max-width: 560px; font: 14px/1.5 system-ui, sans-serif; }
  figcaption { color: #404040; font-size: 13px; margin: 8px 0; }
  figure table { width: 100%; border-collapse: collapse; margin-top: 8px; }
  figure th, figure td { border: 1px solid #D4D4D4; padding: 6px 10px; text-align: left; }
  figure thead th, body > figure table tr:first-child th { background: #F5F5F5; }
  video { width: 100%; border-radius: 8px; }
</style>
```

## 10. Implementation Checklist

- [ ] Every image has an alt attribute - empty for decorative (`--a11y-decorative-handling`), purpose-driven text otherwise (`--a11y-alt-policy`), never omitted.
- [ ] No alt begins with 'image of' or a filename, and decorative/label-adjacent icons read nothing (`var(--a11y-icon-with-label)`).
- [ ] Functional images name the action per `--a11y-functional-alt` ('Search', not 'magnifying glass').
- [ ] Charts pair a short takeaway alt with an accessible data table (`var(--a11y-complex-image-policy)`).
- [ ] Alt length respects `--a11y-alt-length-guide` (under 150 chars); longer descriptions move to adjacent text.
- [ ] No images-of-text except logotypes (`--a11y-images-of-text`).
- [ ] Video ships closed captions with speaker IDs (`--a11y-captions-policy`) plus audio description tracks (`--a11y-audio-description`).
- [ ] All audio content has a full transcript (`var(--a11y-transcript-policy)`).

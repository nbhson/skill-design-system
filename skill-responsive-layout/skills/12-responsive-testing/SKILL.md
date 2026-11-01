---
name: responsive-testing
description: The verification layer: viewport test matrix, visual regression, real-device checks, and zoom/RTL/locale passes that prove layouts work.
tags: [testing, qa, visual-regression, accessibility, responsive]
related: [breakpoints-strategy, rtl-i18n-layout, fluid-container-queries]
---

# Responsive Layout Skill: Responsive Testing & QA

## 1. Definition

Responsive testing is the discipline that keeps every other layout skill honest: a defined viewport/device matrix, automated visual regression at each width, manual passes for zoom (200%/400%), RTL, and long-locale strings, and real-device spot checks for touch behaviors. Layout quality claims ('it's responsive') are replaced by evidence: which widths, which locales, and which zoom levels passed, and when.

## 2. Core Principles

- **A written viewport matrix, not vibes:** the tier widths (320/640/768/1024/1280/1536) plus 200%/400% zoom are the documented pass set.
- **Visual regression automates the matrix:** screenshot diffs at every tier width on every PR catch the overflow nobody eyeballed.
- **Zoom IS a responsive test:** 400% zoom on a 1280px laptop renders a 320px effective width — low-vision users live in your mobile tier (WCAG 1.4.4/1.4.10).
- **Locale passes are layout passes:** German (35% longer), Arabic (RTL), and Japanese (CJK line rules) are the minimum string-stress set.
- **Real devices verify what emulators cannot:** touch targets, safe areas, scroll physics, and OS-level font scaling (iOS/Android accessibility sizes).
- **Test content, not lorem ipsum:** longest real strings, empty states, and worst-case data volumes are the fixtures that find overflow.
- **Findings are tickets with a width attached:** 'broken at 768px with German copy' — reproducible beats 'looks weird sometimes'.

## 3. Spec Tokens

| Role | Token | Value | Notes |
|---|---|---|---|
| Viewport matrix | `--layout-test-viewport-matrix` | `320,640,768,1024,1280,1536` | The documented width pass set |
| Zoom levels | `--layout-test-zoom-levels` | `200%,400%` | Zoom passes included in the matrix (1.4.4/1.4.10) |
| Locale set | `--layout-test-locale-set` | `ar,de,ja` | RTL + long-word + CJK stress locales |
| Content fixtures | `--layout-test-content-fixtures` | `longest-real-strings` | Overflow fixtures: longest label, empty state, max rows |
| Visual regression | `--layout-test-visual-regression` | `per-PR-all-widths` | Screenshot diff gate on every pull request |
| Device pass | `--layout-test-device-pass` | `quarterly-real-devices` | iOS/Android spot checks: targets, safe areas, OS font scale |
| RTL smoke | `--layout-test-rtl-smoke` | `per-release` | dir=rtl page render vs the mirror list |
| Orientation | `--layout-test-orientation` | `portrait-and-landscape` | Both orientations where supported (WCAG 1.3.4) |
| OS font scale | `--layout-test-os-font-scale` | `largest-accessibility-size` | OS-level text scaling verified on devices |
| Finding format | `--layout-test-finding-format` | `width+locale+evidence` | Bugs cite width, locale, and screenshot |

Consume them by linking `assets/css/responsive-testing.css` once at the app root and, more importantly, by loading `var(--layout-test-...)` values into your test tooling config — the matrix, locale set, and zoom levels are read by the screenshot runner, not the stylesheet alone. A width added to `--layout-test-viewport-matrix` must appear in the config file in the same PR; the token is the source of truth and the tooling is its consumer.

## 4. Composition

- **Composes with breakpoints-strategy and fluid-container-queries:** the tier set and slot list define exactly which widths and containers the matrix covers.
- **Composes with sibling layout guides:** every layout pattern ships with its test slot (sidebar/main/modal) registered in the matrix.
- **Composes with zoom-reflow (skill-accessibility guide 11):** the zoom and reflow passes are shared contracts between both repos.

## 5. Signature Patterns

- **Matrix-as-config:** the viewport/locale/zoom matrix lives in a config file consumed by the visual-regression tool — tests and docs stay in sync.
- **Overflow canary:** an automated probe walks pages at each width and fails on horizontal scroll of reading content or clipped interactive elements.

## 6. Real-World Use Cases

- **Design systems gating component releases on the full matrix.**
- **i18n product launches: locale stress passes before market open.**
- **Ongoing QA: regression gates keeping responsive debt from accumulating.**

## 7. Combination Notes

### With other responsive-layout skills

- **Composes with all of them — the caution and avoid lists are empty:** responsive-testing is the verification layer; it does not make layout decisions, it proves the other skills' claims, which is why every skill in the catalog (grid-systems, breakpoints-strategy, fluid-container-queries, flexbox-patterns, css-grid-patterns, layout-compositions, responsive-images, mobile-navigation, data-tables-responsive, intrinsic-design, rtl-i18n-layout) lists it as good.
- **Good with breakpoints-strategy:** the tier definitions ARE the matrix; when a tier is added or renamed, the test matrix and the breakpoint tokens change in the same commit.
- **Good with fluid-container-queries:** container-aware components register their slots (sidebar/main/modal) in the matrix, so slot coverage is generated, not remembered.
- **Good with rtl-i18n-layout:** the locale stress set (ar, de, ja) and the per-release RTL smoke page are defined by the i18n skill and executed here.
- **Good with intrinsic-design:** intrinsic layouts claim 'fewer queries, flexes anywhere' — the continuous-resize probe (240px-2560px) is exactly the evidence that claim needs.
- **Good with mobile-navigation and data-tables-responsive:** the trickiest surfaces (drawers, sticky-scroll tables) get explicit matrix entries; touch and safe-area items land in the quarterly real-device pass.

### With design styles (companion repo skill-ui-ux)

- **Good affinity with minimalism, flat-design, and class-morphism:** these styles render deterministically across widths — flat surfaces and restrained palettes produce stable screenshot diffs with fewer false positives from texture or lighting noise.
- **No caution pairs:** even maximalist or collage-art layouts benefit from the matrix; the only adjustment is per-style snapshot tolerance, since expressive styles may diff more on anti-aliasing and imagery.

### With motion skills (companion repo skill-animation)

- **Good affinity with easing-timing:** motion tokens define how UI behaves during the animation frames screenshots may catch; tests disable or fast-forward animations per the shared duration tokens so visual diffs stay stable.
- **No caution pairs:** visual regression simply honors reduced-motion and the animation repo's settled-state convention — screenshots are taken at rest states, and animated states are tested by the animation repo's own timing checks.

## 8. Anti-Patterns

- **Two-width testing:** signing off at 375px and 1440px while the 768-1024 middle tier rots
- **Lorem ipsum QA:** placeholder strings that never overflow, hiding the German-label explosion
- **Emulator-only trust:** declaring touch and safe-area work without ever holding a device
- **Ungated regressions:** visual diffs run manually, after the overflow already shipped

### Accessibility Notes

Zoom and OS-font-scale passes are accessibility conformance tests (WCAG 1.4.4/1.4.10), not polish: low-vision users browse at widths your matrix must include — the 400% zoom pass IS a responsive test. The fallback rule keeps releases honest under time pressure: if the full matrix cannot run before release, run the subset in priority order — 320px, 400% zoom, RTL locale, then widest — and ship the remainder as documented known issues with owners. Note also that findings are only as useful as their format: every bug cites width, locale, and screenshot (`--layout-test-finding-format`), because 'broken at 768px with German copy' is a ticket; 'looks weird sometimes' is noise.

## 9. Code Examples

### Example 1 — Matrix-as-config (viewports/locales/zoom drive the screenshot runner)

Tokens: `assets/css/responsive-testing.css`

```html
<script>
  // The matrix lives in config, mirroring --layout-test-* tokens 1:1.
  const MATRIX = {
    viewports: [320, 640, 768, 1024, 1280, 1536],          // --layout-test-viewport-matrix
    zoomLevels: ["200%", "400%"],                          // --layout-test-zoom-levels
    locales: ["ar", "de", "ja"],                           // --layout-test-locale-set
    orientations: ["portrait", "landscape"],               // --layout-test-orientation
    fixtures: "longest-real-strings",                      // --layout-test-content-fixtures
    gate: "per-PR-all-widths",                             // --layout-test-visual-regression
  };

  // Screenshot every page x viewport x locale x zoom; diff against baseline.
  async function runMatrix(pages, screenshot) {
    const jobs = [];
    for (const page of pages) {
      for (const width of MATRIX.viewports) {
        for (const locale of MATRIX.locales) {
          for (const zoom of MATRIX.zoomLevels) {
            const id = `${page}@${width}w_${locale}_${zoom}`;
            await screenshot(page, { width, locale, zoom, id });
          }
        }
      }
    }
    return `${pages.length * MATRIX.viewports.length * MATRIX.locales.length * MATRIX.zoomLevels.length} shots captured`;
  }

  // Priority fallback when the full matrix cannot run before release:
  const PRIORITY = ["320px", "400% zoom", "RTL locale", "widest"];
</script>
```

### Example 2 — Overflow canary probe (walk widths, fail on horizontal scroll)

```html
<div class="page" id="canary-target">
  <h1>Orders</h1>
  <p class="reading">Reading content must never force horizontal scroll at any width.</p>
  <div class="table-wrap" role="region" aria-label="Orders table" tabindex="0">
    <table><tr><th>ID</th><th>Customer</th><th>Total</th></tr>
      <tr><td>#1042</td><td>Klärenfreund-Straßenbau GmbH</td><td>1,204.00</td></tr></table>
  </div>
</div>
<script>
  // Overflow canary: --layout-test-viewport-matrix widths; the scrollable TABLE
  // region is a sanctioned exception; the PAGE itself must not scroll sideways.
  const WIDTHS = [320, 640, 768, 1024, 1280, 1536];
  const failures = [];
  for (const width of WIDTHS) {
    window.resizeTo(width, 900); // or drive viewport in the harness
    document.documentElement.style.setProperty("--probe-width", width + "px");
    const page = document.documentElement;
    const pageOverflow = page.scrollWidth > page.clientWidth;
    const clipped = [...document.querySelectorAll("button, a, input")]
      .filter(el => el.getBoundingClientRect().right > page.clientWidth + 1).length;
    if (pageOverflow || clipped) {
      failures.push({ width, pageOverflow, clippedInteractive: clipped });
    }
  }
  // Finding format per --layout-test-finding-format: width + locale + evidence
  failures.forEach(f => console.error(`overflow at ${f.width}px (locale pass: de) — attach screenshot`, f));
  console.assert(failures.length === 0, "overflow canary failed: see findings above");
</script>
<style>
  .page { max-width: 100%; overflow-x: clip; }
  .reading { max-width: 66ch; }              /* reading measure bound */
  .table-wrap { overflow-x: auto; }          /* honest scroll, scoped to the table */
  table { min-width: 100%; border-collapse: collapse; }
  th, td { padding: 0.5rem 0.75rem; border-block-end: 1px solid #ddd; white-space: nowrap; }
</style>
```

## 10. Implementation Checklist

- [ ] The screenshot config consumes `--layout-test-viewport-matrix` (320/640/768/1024/1280/1536) — tests and docs read from one source.
- [ ] 200% and 400% zoom passes (`--layout-test-zoom-levels`) run in CI, not just device widths.
- [ ] The locale stress set (`--layout-test-locale-set`: ar, de, ja) is part of every release pass, with real translation fixtures per `--layout-test-content-fixtures`.
- [ ] Visual regression runs per-PR at all widths (`--layout-test-visual-regression`) — diffs are a merge gate, not a manual task.
- [ ] The overflow canary walks every page at every matrix width and fails on page-level horizontal scroll or clipped interactive elements.
- [ ] The quarterly real-device pass (`--layout-test-device-pass`) verifies touch targets, safe areas, and OS font scale (`--layout-test-os-font-scale`).
- [ ] Portrait and landscape are both covered where supported (`--layout-test-orientation`).
- [ ] Every responsive bug cites width + locale + screenshot per `--layout-test-finding-format`, and the RTL smoke (`--layout-test-rtl-smoke`) runs per release.

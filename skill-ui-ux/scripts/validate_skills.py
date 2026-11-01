#!/usr/bin/env python3
"""
validate_skills.py — CI check for skill-ui-ux repository.

Checks:
  1. All 12 style SKILL.md files exist and parseable
  2. data.json is valid JSON and has all 12 style IDs
  3. anti-patterns in data.json match SKILL.md section 8
  4. palette hex values are plain #RGB / #RRGGBB
  5. data.json combination graph is symmetric (good↔good, caution↔caution, avoid↔avoid)
  6. README Combination Matrix symbols (✅/⚠️/❌) match data.json combinations exactly
  7. Figma reference links are well-formed URLs
  8. CSS token files in assets/css/ exist per style and match data.json palettes
  9. .gitignore covers noise files and no .DS_Store exists (auto-removed if found)
  10. SKILL.md guides expose sections 9 (Code Examples) & 10 (Implementation Checklist);
      data.json exposes a WCAG `contrast` section per style

Exit 0 on success, non-zero on any failure.
"""

import json, re, sys, urllib.parse, pathlib

ROOT = pathlib.Path(__file__).parent.parent
EXIT_CODE = 0

def fail(msg: str):
    global EXIT_CODE
    print(f"FAIL: {msg}")
    EXIT_CODE = 1

def norm_key(text: str) -> str:
    return re.sub(r'\s+', ' ', re.sub(r'\*\*|`', '', text)).strip()[:60]

# ── 1. SKILL.md existence & parseability ────────────────────────────────────

expected_styles = [
    "minimalism","maximalism","flat-design","neumorphism","claymorphism",
    "aurora-ui","brutalism-ui","collage-art","skeuomorphism","retro",
    "class-morphism","glassmorphism",
]

print("1. SKILL.md existence check:")
skills_dir = ROOT / "skills"
for sid in expected_styles:
    found = False
    for p in (skills_dir).glob("*/SKILL.md"):
        fm = re.search(r"^name:\s*(\S+)\s*$", p.read_text(), re.M)
        if fm and fm.group(1) == sid:
            found = True
            break
    status = "✓" if found else "✗"
    print(f"  {status} {sid}")

# ── 2. data.json validity ─────────────────────────────────────────────────────

print("\n2. data.json validity:")
try:
    with (skills_dir / "data.json").open() as f:
        data = json.load(f)
    print(f"  ✓ valid JSON, {len(data['styles'])} styles")
    style_ids = {s["id"] for s in data["styles"]}
    missing = set(expected_styles) - style_ids
    extra = style_ids - set(expected_styles)
    if missing: fail(f"Missing styles in data.json: {missing}")
    if extra:   fail(f"Extra styles in data.json: {extra}")
    if not missing and not extra: print(f"  ✓ All 12 styles present")
except json.JSONDecodeError as e:
    fail(f"data.json is not valid JSON: {e}")

# ── 3. anti-patterns match ────────────────────────────────────────────────────

print("\n3. Anti-patterns consistency:")
for s in data["styles"]:
    sid = s["id"]
    # find SKILL.md
    md_path = None
    for p in (skills_dir).glob("*/SKILL.md"):
        fm = re.search(r"^name:\s*(\S+)\s*$", p.read_text(), re.M)
        if fm and fm.group(1) == sid:
            md_path = p; break

    ap_json = [norm_key(x) for x in s["sections"].get("antiPatterns", [])]
    if not md_path:
        fail(f"  {sid}: no SKILL.md found")
        continue

    md_text = md_path.read_text()
    m = re.search(r'\n## 8\. Anti-Patterns\s*\n(.*?)(?=\n## |\Z)', md_text, re.S)
    ap_md = []
    if m:
        for line in m.group(1).splitlines():
            line = line.strip()
            if line.startswith('- **'):
                cleaned = re.sub(r'^- \*\*', '', line)
                cleaned = re.sub(r'\*\*$', '', cleaned).strip()
                cleaned = re.sub(r':\s*$', '', cleaned).strip()
                ap_md.append(norm_key(cleaned))
            elif line.startswith('- '):
                ap_md.append(norm_key(line[2:].strip()))

    if not ap_md:
        fail(f"  {sid}: no anti-patterns in MD")
        continue

    # compare
    md_keys = set(ap_md)
    json_keys = set(ap_json)
    diff = md_keys ^ json_keys
    if diff:
        fail(f"  {sid}: anti-patterns mismatch — {diff}")
    else:
        print(f"  ✓ {sid} ({len(ap_md)} items)")

# ── 4. palette hex format ─────────────────────────────────────────────────────

print("\n4. Palette hex format:")
for s in data["styles"]:
    for c in s["sections"].get("palette", []):
        h = c.get("hex", "")
        if not re.match(r"^#[0-9A-Fa-f]{3,6}$", h):
            fail(f"  {s['id']}/{c['role']}: invalid hex '{h}'")

style_with_bad_hex = [s["id"] for s in data["styles"]
                      if any(not re.match(r"^#[0-9A-Fa-f]{3,6}$", c.get("hex",""))
                             for c in s["sections"].get("palette",[]))]
if not style_with_bad_hex:
    total = sum(len(s["sections"]["palette"]) for s in data["styles"])
    print(f"  ✓ All {total} palette entries have valid hex format")

# ── 5. Combination graph symmetry (data.json) ────────────────────────────────

print("\n5. Combination graph symmetry:")
sym_errors = 0
for s in data["styles"]:
    sid = s["id"]
    com = s["sections"].get("combinations", {})
    if not com:
        continue
    for tier in ("good", "caution", "avoid"):
        for other_id in com.get(tier, []):
            if other_id not in style_ids:
                fail(f"  {sid} → {other_id}: target not in style list")
                sym_errors += 1
                continue
            other_com = next((x["sections"].get("combinations", {}) for x in data["styles"]
                              if x["id"] == other_id), {})
            # Combos are symmetric: A good-with B must mean B good-with A (same for caution/avoid)
            reverse = other_com.get(tier, [])
            if sid not in reverse:
                fail(f"  {sid} —{tier}→ {other_id}: not reciprocated "
                     f"({other_id} lists {other_id} {tier} as {reverse})")
                sym_errors += 1

if sym_errors == 0:
    pairs_checked = sum(len(s["sections"].get("combinations", {}).get(t, []))
                        for s in data["styles"] for t in ("good", "caution", "avoid"))
    print(f"  ✓ All {pairs_checked} combination entries are mutually symmetric")

# ── 6. README matrix ↔ data.json consistency ─────────────────────────────────

print("\n6. README matrix ↔ data.json consistency:")
readme = (ROOT / "README.md").read_text()

# Locate the matrix table under its own heading (not other README tables)
m_heading = re.search(r'^#+.*Combination Matrix.*$', readme, re.M)
if not m_heading:
    fail("  README: Combination Matrix heading not found")
    m_matrix = None
else:
    after_heading = readme[m_heading.end():]
    m_matrix = re.search(r'((?:^\|.*\|\s*$\n?)+)', after_heading, re.M)

MATRIX_ABBS = {
    "min": "minimalism", "max": "maximalism", "flat": "flat-design",
    "neu": "neumorphism", "clay": "claymorphism", "aurora": "aurora-ui",
    "brutal": "brutalism-ui", "collage": "collage-art", "skeuo": "skeuomorphism",
    "retro": "retro", "class": "class-morphism", "glass": "glassmorphism",
}
# full-name row label → style id (row cells use full names, e.g. "**Minimalism**")
FULL_NAME_TO_ID = {
    "minimalism": "minimalism", "maximalism": "maximalism",
    "flat design": "flat-design", "neumorphism": "neumorphism",
    "claymorphism": "claymorphism", "aurora ui": "aurora-ui",
    "brutalism ui": "brutalism-ui", "collage art": "collage-art",
    "skeuomorphism": "skeuomorphism", "retro": "retro",
    "class morphism": "class-morphism", "glassmorphism": "glassmorphism",
}
SYMBOL_TO_TIER = {"✅": "good", "⚠": "caution", "❌": "avoid"}

def norm_symbol(cell: str):
    cell = cell.strip().replace("\ufe0f", "")  # strip variation selector from ⚠️
    for sym, tier in SYMBOL_TO_TIER.items():
        if cell.startswith(sym):
            return tier
    if cell in ("—", "-", ""):
        return None  # diagonal / empty
    return "UNKNOWN"

def tier_of(row_id: str, col_id: str):
    """Expected README symbol tier from data.json: row's combination tier for col."""
    com = next((s["sections"].get("combinations", {}) for s in data["styles"]
                if s["id"] == row_id), {})
    for tier in ("good", "caution", "avoid"):
        if col_id in com.get(tier, []):
            return tier
    return None

if not m_matrix:
    fail("  README: Combination matrix table not found")
else:
    table_rows = [r for r in m_matrix.group(1).strip().splitlines()]
    # parse header: | | min | max | ... |
    header_cells = [c.strip() for c in table_rows[0].strip().strip("|").split("|")]
    col_ids = [MATRIX_ABBS.get(c.lower()) for c in header_cells[1:]]
    if any(c is None for c in col_ids):
        fail(f"  README: unrecognized matrix header columns: "
             f"{[c for c, cid in zip(header_cells[1:], col_ids) if cid is None]}")
    row_errors = 0
    checked = 0
    seen_pairs = set()
    matrix_symbols = {}
    for row in table_rows[2:]:  # skip header + |---| separator
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        row_label = cells[0].replace("*", "").strip().lower()
        row_id = FULL_NAME_TO_ID.get(row_label)
        if row_id is None:
            fail(f"  README: unrecognized matrix row '{cells[0].strip()}'")
            row_errors += 1
            continue
        for i, col_id in enumerate(col_ids):
            if col_id is None:
                continue
            cell_tier = norm_symbol(cells[i + 1])
            matrix_symbols[(row_id, col_id)] = cell_tier
            if col_id == row_id:
                if cell_tier is not None:
                    fail(f"  README: diagonal cell {row_id}×{row_id} should be '—'")
                    row_errors += 1
                continue
            if cell_tier == "UNKNOWN":
                fail(f"  README: {row_id}×{col_id}: unknown symbol '{cells[i + 1].strip()}'")
                row_errors += 1
                continue
            expected = tier_of(row_id, col_id)
            checked += 1
            seen_pairs.add((row_id, col_id))
            if cell_tier != expected:
                fail(f"  README: {row_id}×{col_id} shows '{cell_tier or '—'}' "
                     f"but data.json says '{expected or 'no combination'}'")
                row_errors += 1

    # matrix must be internally symmetric (cell(A,B) == cell(B,A))
    for (a, b), tier in matrix_symbols.items():
        if a == b or (a, b) not in seen_pairs:
            continue
        rev = matrix_symbols.get((b, a))
        if rev != tier and (b, a) in seen_pairs:
            fail(f"  README: matrix not symmetric — {a}×{b}='{tier}' vs {b}×{a}='{rev}'")
            row_errors += 1

    # coverage: every ordered pair of distinct styles must appear in the matrix
    missing_pairs = [(a, b) for a in style_ids for b in style_ids
                     if a != b and (a, b) not in seen_pairs]
    if missing_pairs:
        fail(f"  README: matrix missing cells for {len(missing_pairs)} pair(s): "
             f"{missing_pairs[:5]}")
        row_errors += 1

    if row_errors == 0:
        print(f"  ✓ All {checked} matrix cells match data.json combinations "
              f"(full 12×12 coverage, symmetric)")

# ── 7. Figma reference URLs ───────────────────────────────────────────────────

print("\n7. Figma reference URLs:")
fr_path = skills_dir / "assets" / "figma-references.md"
if fr_path.exists():
    urls = re.findall(r'https?://[^\s\)]+', fr_path.read_text())
    bad_urls = [u for u in urls if not urllib.parse.urlparse(u).netloc]
    if bad_urls:
        fail(f"  Malformed URLs: {bad_urls}")
    else:
        print(f"  ✓ {len(urls)} URL(s) well-formed")
else:
    fail("  figma-references.md not found")

# ── 8. CSS token files ↔ data.json consistency ──────────────────────────────

print("\n8. CSS token files (assets/css):")
css_dir = ROOT / "assets" / "css"
styles = data.get("styles", []) if "data" in dir() else []
for s in styles:
    sid = s["id"]
    css_path = css_dir / f"{sid}.css"
    if not css_path.exists():
        fail(f"missing assets/css/{sid}.css")
        continue
    css_text = css_path.read_text()
    # Mỗi hex trong data.json palette phải xuất hiện trong file token
    for entry in s["sections"].get("palette", []):
        hx = entry["hex"].lower()
        if hx not in css_text.lower():
            fail(f"assets/css/{sid}.css missing hex {hx} ({entry['role']})")
    print(f"  ✓ {sid}.css matches data.json palette")
if styles:
    extra_css = {p.stem for p in css_dir.glob("*.css")} - {s["id"] for s in styles}
    if extra_css:
        fail(f"CSS files without matching style in data.json: {extra_css}")

# ── 9. .gitignore coverage & .DS_Store hygiene ───────────────────────────────

print("\n9. .gitignore coverage & .DS_Store:")
gi_path = ROOT / ".gitignore"
gi = gi_path.read_text() if gi_path.exists() else ""
for f in [".DS_Store", "*.pyc", "__pycache__"]:
    if f in gi or f.replace("*", "") in gi:
        print(f"  ✓ '{f}' covered")
    else:
        fail(f"  '{f}' not covered in .gitignore")

# .DS_Store must not exist anywhere in the repo (tracked working tree, excluding .git).
# The validator deletes any it finds, then fails so the issue is surfaced in CI.
ds_found = [p for p in ROOT.rglob(".DS_Store") if ".git/" not in str(p.relative_to(ROOT))]
for p in ds_found:
    try:
        p.unlink()
        print(f"  🗑 removed {p.relative_to(ROOT)}")
    except OSError as e:
        fail(f"  could not delete {p}: {e}")
if ds_found:
    fail(f"{len(ds_found)} .DS_Store file(s) found and deleted — "
         "commit them never; re-run after cleaning git index if they were tracked")
else:
    print("  ✓ no .DS_Store files in repo")

# ── 10. Extended sections (9 & 10) + contrast data ───────────────────────────

print("\n10. Extended guide sections & contrast data:")
for s in data["styles"]:
    sid = s["id"]
    md_path = None
    for p in (skills_dir).glob("*/SKILL.md"):
        fm = re.search(r"^name:\s*(\S+)\s*$", p.read_text(), re.M)
        if fm and fm.group(1) == sid:
            md_path = p
            break
    if not md_path:
        fail(f"  {sid}: no SKILL.md found")
        continue
    md_text = md_path.read_text()
    for heading, label in ((r"## 9\. Code Examples", "9. Code Examples"),
                           (r"## 10\. Implementation Checklist", "10. Implementation Checklist")):
        if not re.search(heading, md_text):
            fail(f"  {sid}: SKILL.md missing section '{label}'")
    # contrast section in data.json with >= 2 computed pairs
    contrast = s["sections"].get("contrast", {})
    pairs = contrast.get("pairs", [])
    if len(pairs) < 2:
        fail(f"  {sid}: data.json `contrast` missing or has < 2 pairs")
    else:
        bad_ratio = [p for p in pairs if not isinstance(p.get("ratio"), (int, float))]
        if bad_ratio:
            fail(f"  {sid}: contrast pairs missing computed ratio: {bad_ratio}")
        else:
            worst = min(p["ratio"] for p in pairs)
            aa_fails = sum(1 for p in pairs if p["ratio"] < 4.5)
            flagged = aa_fails > 0
            print(f"  ✓ {sid}: {len(pairs)} contrast pairs (worst {worst}:1"
                  f"{', ' + str(aa_fails) + ' pair(s) flagged <4.5:1 in notes' if flagged else ''})")
            if flagged and "4.5" not in contrast.get("notes", "") and "4.5" not in str(contrast.get("pairs", [])):
                fail(f"  {sid}: contrast pair < 4.5:1 but no warning documented in `notes`")


# ── summary ────────────────────────────────────────────────────────────────────

print(f"\n{'─'*40}")
if EXIT_CODE == 0:
    print("All checks passed ✓")
else:
    print(f"FAILED — {EXIT_CODE} check(s) failed")
sys.exit(EXIT_CODE)

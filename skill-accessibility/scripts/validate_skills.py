#!/usr/bin/env python3
"""
validate_skills.py - CI check for skill-design-tokens repository.

Checks:
  1. All 12 token SKILL.md files exist and parseable (frontmatter name)
  2. data.json is valid JSON and has all 12 skill ids
  3. Anti-patterns in data.json match SKILL.md section 8
  4. Token values are well-formed (colors, lengths, shadows, ratios, var(), identifiers)
  5. data.json combination graph is symmetric (good/good, caution/caution, avoid/avoid)
  6. README Combination Matrix symbols match data.json combinations exactly
  7. Reference links are well-formed URLs
  8. CSS token files in assets/css/ exist per skill and match data.json token values
  9. .gitignore covers noise files and no .DS_Store exists (auto-removed if found)
  10. SKILL.md guides expose sections 9 & 10; data.json exposes an `accessibility`
      contract per skill; alias values only reference --dt-* primitives/aliases

Exit 0 on success, non-zero on any failure.
"""

import json
import re
import sys
import urllib.parse
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
EXIT_CODE = 0

PREFIX = "--a11y-"

expected_skills = [
    "wcag-fundamentals", "color-contrast", "keyboard-navigation", "focus-management",
    "aria-fundamentals", "aria-patterns-widgets", "forms-errors", "screen-readers",
    "media-alt-text", "cognitive-content", "zoom-reflow", "testing-audit",
]

matrix_cols = ["wcag", "contrast", "kbd", "focus", "aria", "widgets",
               "forms", "sr", "media", "cog", "zoom", "audit"]

companion_ids = {
    "skill-ui-ux": ["minimalism", "maximalism", "flat-design", "neumorphism",
                    "claymorphism", "aurora-ui", "brutalism-ui", "collage-art",
                    "skeuomorphism", "retro", "class-morphism", "glassmorphism"],
    "skill-animation": ["easing-timing", "micro-interactions", "entrance-exit",
                        "page-transitions", "loading-states", "feedback-confirmation",
                        "scroll-animation", "gesture-drag", "data-animation",
                        "ambient-motion", "illustration-lottie", "reduced-motion"],
}


def fail(msg: str):
    global EXIT_CODE
    print(f"FAIL: {msg}")
    EXIT_CODE = 1


def ok(msg: str):
    print(f"  ok {msg}")


def norm_key(text: str) -> str:
    # unify colon (data.json "title: rest") and em/en dash (md "**title** — rest"),
    # strip md bullet markers, lowercase, keep full length for exact comparison
    text = re.sub(r"^\s*-\s*", "", text)
    return re.sub(r"\s+", " ", re.sub(r"[\*\`'\"“”‘’]", "", re.sub(r"[:—–]| - ", " ", text))).strip().lower()


def is_well_formed(value: str) -> bool:
    v = value.strip()
    if not v:
        return False
    if v.startswith("var(") and v.endswith(")"):
        return True
    if re.fullmatch(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})", v):
        return True
    if re.fullmatch(r"-?\d+(\.\d+)?(px|rem|em|ms|s|%)", v):
        return True
    if v == "0" or re.fullmatch(r"\d+", v):
        return True
    if re.fullmatch(r"\d+(\.\d+)?:1", v):  # contrast ratios 4.5:1
        return True
    if v.startswith("rgba(") or v.startswith("rgb("):
        return True
    if v.startswith("0 ") and "rgba" in v:  # box-shadow lists
        return True
    if v == "linear" or v.startswith("cubic-bezier("):
        return True
    # declarative/meta string tokens (theming-strategy, pipeline-*...)
    if re.fullmatch(r"[A-Za-z0-9 ,.\-_=/'\"#(){}@+>]+", v):
        return True
    return False


print("1. SKILL.md existence check:")
skills_dir = ROOT / "skills"
md_by_id = {}
for p in sorted(skills_dir.glob("*/SKILL.md")):
    fm = re.search(r"^name:\s*(\S+)\s*$", p.read_text(), re.M)
    if fm:
        md_by_id[fm.group(1)] = p
for sid in expected_skills:
    mark = "✓" if sid in md_by_id else "✗"
    print(f"  {mark} {sid}")
    if sid not in md_by_id:
        fail(f"missing SKILL.md for {sid}")

data_path = ROOT / "skills" / "data.json"
print("2. data.json check:")
try:
    data = json.loads(data_path.read_text())
    json_ids = [s["id"] for s in data["skills"]]
    missing = [i for i in expected_skills if i not in json_ids]
    extra = [i for i in json_ids if i not in expected_skills]
    ok(f"{len(json_ids)} ids, meta.version={data['meta']['version']}")
    if data["meta"]["totalSkills"] != 12:
        fail("meta.totalSkills must be 12")
    if missing:
        fail(f"data.json missing ids: {missing}")
    if extra:
        fail(f"data.json unexpected ids: {extra}")
except Exception as exc:
    fail(f"data.json unreadable: {exc}")
    sys.exit(1)

print("3. Anti-patterns data.json vs SKILL.md:")
for sid in expected_skills:
    entry = next(s for s in data["skills"] if s["id"] == sid)
    ap_data = [norm_key(a) for a in entry["sections"]["antiPatterns"]]
    md = md_by_id[sid].read_text()
    m = re.search(r"## 8\. Anti-Patterns(.*?)(?=\n## 9\.|\Z)", md, re.S)
    if not m:
        fail(f"{sid}: section 8 not found")
        continue
    ap_md = set(norm_key(line) for line in m.group(1).splitlines() if line.strip().startswith("- **"))
    for a in ap_data:
        if a not in ap_md:
            fail(f"{sid}: anti-pattern not mirrored in SKILL.md: {a[:50]}")
ok("anti-patterns mirrored" if EXIT_CODE == 0 else "see failures above")

print("4. Token value well-formedness:")
for sid in expected_skills:
    entry = next(s for s in data["skills"] if s["id"] == sid)
    for tok in entry["sections"]["tokens"]:
        if not is_well_formed(tok["value"]):
            fail(f"{sid}: suspicious token value {tok['role']!r} = {tok['value']!r}")
        if " " in tok["role"] or tok["role"] != tok["role"].lower():
            fail(f"{sid}: token role must be lowercase-kebab: {tok['role']}")
ok("token values checked")

print("5. Combination graph symmetry:")
combos = {s["id"]: s["sections"]["combinations"] for s in data["skills"]}
for sid, c in combos.items():
    for rel in ("good", "caution", "avoid"):
        for other in c.get(rel, []):
            if other not in combos:
                fail(f"{sid}: unknown partner id {other}")
            elif sid not in combos[other].get(rel, []):
                fail(f"{sid}: {rel} edge to {other} is not symmetric")
            if sid == other:
                fail(f"{sid}: self-edge in combinations")
ok("combination graph symmetric")

print("5b. Companion affinity ids exist:")
for sid, c in ((s["id"], s["sections"]) for s in data["skills"]):
    for field, repo in (("styleAffinity", "skill-ui-ux"), ("motionAffinity", "skill-animation")):
        aff = c.get(field, {})
        for rel in ("good", "caution", "avoid"):
            for ref in aff.get(rel, []):
                if ref not in companion_ids[repo]:
                    fail(f"{sid}.{field}: unknown {repo} id {ref}")
ok("affinity ids valid")

print("6. README Combination Matrix vs data.json:")
readme = (ROOT / "README.md").read_text()
matrix_rows = {}
for line in readme.splitlines():
    m = re.match(r"\|\s*\*\*(.+?)\*\*\s*\|", line)
    if m:
        cells = [c.strip() for c in line.split("|")[2:-1]]
        matrix_rows[norm_key(m.group(1))] = cells
name_order = {sid: i for i, sid in enumerate(expected_skills)}
for sid in expected_skills:
    entry = next(s for s in data["skills"] if s["id"] == sid)
    row = matrix_rows.get(norm_key(entry["name"]))
    if row is None:
        fail(f"README matrix missing row for {entry['name']}")
        continue
    if len(row) != 12:
        fail(f"README matrix row {sid}: expected 12 cells, got {len(row)}")
        continue
    expected = []
    for i, other in enumerate(expected_skills):
        if i == name_order[sid]:
            expected.append("—")
        elif other in entry["sections"]["combinations"]["good"]:
            expected.append("✅")
        elif other in entry["sections"]["combinations"]["caution"]:
            expected.append("⚠️")
        elif other in entry["sections"]["combinations"]["avoid"]:
            expected.append("❌")
        else:
            fail(f"{sid}: partner {other} missing from all combination lists")
            expected.append("?")
    for i, (got, exp) in enumerate(zip(row, expected)):
        if got != exp:
            fail(f"README matrix {sid} vs {matrix_cols[i]}: got {got!r}, expected {exp!r}")
ok("matrix matches data.json")

print("7. Reference links:")
refs = ROOT / "skills" / "assets" / "references.md"
if refs.exists():
    for line in refs.read_text().splitlines():
        for url in re.findall(r"https?://\S+", line):
            parsed = urllib.parse.urlparse(url.rstrip(".,)"))
            if not parsed.netloc or "." not in parsed.netloc:
                fail(f"malformed reference URL: {url}")
    ok("reference URLs well-formed")
else:
    fail("skills/assets/references.md missing")

print("8. CSS token files vs data.json:")
for sid in expected_skills:
    css_path = ROOT / "assets" / "css" / f"{sid}.css"
    if not css_path.exists():
        fail(f"missing assets/css/{sid}.css")
        continue
    css = css_path.read_text()
    entry = next(s for s in data["skills"] if s["id"] == sid)
    for tok in entry["sections"]["tokens"]:
        expected_decl = f"{PREFIX}{tok['role']}: {tok['value']};"
        if expected_decl not in css:
            fail(f"{sid}.css: declaration mismatch for {tok['role']} (expected {expected_decl!r})")
    # every declaration in the css file must be a known token
    for decl in re.findall(r"^\s+(--dt-[\w-]+):\s*([^;]+);", css, re.M):
        roles = {t["role"] for t in entry["sections"]["tokens"]}
        if decl[0].removeprefix(PREFIX) not in roles:
            fail(f"{sid}.css: unknown token in generated file: {decl[0]}")
ok("css files match data.json")

print("9. Repo hygiene:")
ds_store = list(ROOT.rglob(".DS_Store"))
for p in ds_store:
    p.unlink()
    print(f"  removed {p}")
if ds_store:
    fail(".DS_Store present (auto-removed)")
gitignore = ROOT / ".gitignore"
gi = gitignore.read_text() if gitignore.exists() else ""
if ".DS_Store" not in gi:
    fail(".gitignore must cover .DS_Store")
ok("hygiene checked")

print("10. Guide completeness + accessibility contract:")
for sid in expected_skills:
    entry = next(s for s in data["skills"] if s["id"] == sid)
    md = md_by_id[sid].read_text()
    for sec_no in ("9", "10"):
        if not re.search(rf"^## {sec_no}\. ", md, re.M):
            fail(f"{sid}: missing section {sec_no}")
    acc = entry["sections"].get("accessibility")
    if not acc or not acc.get("required") or not acc.get("fallback"):
        fail(f"{sid}: data.json accessibility contract incomplete")
    if "### Accessibility Notes" not in md:
        fail(f"{sid}: SKILL.md missing '### Accessibility Notes'")
ok("sections 9/10 + accessibility contracts present")


if EXIT_CODE:
    print("\nRESULT: FAIL")
else:
    print("\nRESULT: all checks passed")
sys.exit(EXIT_CODE)

#!/usr/bin/env python3
"""
generate_css_tokens.py — regenerate assets/css/<style-id>.css from skills/data.json.

data.json is the single source of truth. This script regenerates every CSS token
file (overwriting existing ones) using the same format as the original hand-off:

  - header comment block (style name, id, summary, do-not-edit-by-hand note)
  - :root block with --color-<role-kebab>: <hex> tokens (lowercase hex, notes comment)
  - --font-heading / --font-body tokens derived from typography
  - a contrast comment block (WCAG ratios from the `contrast` section, if present)

Usage:  python3 scripts/generate_css_tokens.py
"""

import json, pathlib, re

ROOT = pathlib.Path(__file__).parent.parent
DATA = ROOT / "skills" / "data.json"
CSS_DIR = ROOT / "assets" / "css"


def kebab(text: str) -> str:
    """'Primary background' -> 'primary-background'; '50s cherry red' -> '50s-cherry-red'."""
    s = re.sub(r"[^A-Za-z0-9]+", "-", text.strip()).strip("-").lower()
    return s


def font_token(font_spec: str) -> str:
    """'Inter (or SF Pro Display)' -> '"Inter", sans-serif'.
    Keeps the full spec when no parenthesised alternative exists (matches legacy files)."""
    primary = font_spec.split("(")[0].strip().rstrip(";").strip()
    if not primary:
        primary = font_spec.strip()
    return f'"{primary}", sans-serif'


def render(style: dict) -> str:
    sid = style["id"]
    sections = style["sections"]
    lines = []
    lines.append("/* ============================================================")
    lines.append(f" * {style['name']} — starter design tokens (CSS custom properties)")
    lines.append(f" * Style id: {sid}")
    lines.append(" *")
    lines.append(f" * {style['summary']}")
    lines.append(" *")
    lines.append(" * Sinh tự động từ skills/data.json (nguồn truth đã được")
    lines.append(" * scripts/validate_skills.py kiểm chứng). KHÔNG sửa tay hex values —")
    lines.append(" * sửa data.json rồi chạy lại script sinh token.")
    lines.append(" * ============================================================ */")
    lines.append("")
    lines.append(":root {")
    for entry in sections.get("palette", []):
        var = f"--color-{kebab(entry['role'])}"
        hx = entry["hex"].lower()
        notes = entry.get("notes", "")
        lines.append(f"  {var}: {hx}; /* {notes} */")
    typo = sections.get("typography", {})
    lines.append(f'  --font-heading: {font_token(typo.get("header", {}).get("font", "system-ui"))}; /* {typo.get("header", {}).get("font", "")} */')
    lines.append(f'  --font-body: {font_token(typo.get("body", {}).get("font", "system-ui"))}; /* {typo.get("body", {}).get("font", "")} */')
    lines.append("}")

    # Contrast block — comment-only, ratios come precomputed in data.json (WCAG formula)
    contrast = sections.get("contrast")
    if contrast:
        lines.append("")
        lines.append("/* Contrast (WCAG relative luminance, AA body-text threshold = 4.5:1) */")
        for pair in contrast.get("pairs", []):
            status = "PASS" if pair["wcagAA"] == "pass" else "FAIL"
            lines.append(
                f"/* {pair['role']}: {pair['foreground']} on {pair['background']} "
                f"= {pair['ratio']}:1 — {status} */"
            )
        if "fail" in [p["wcagAA"] for p in contrast.get("pairs", [])]:
            lines.append("/* WARNING: at least one pair fails AA — see data.json `contrast.notes` for mitigations. */")

    return "\n".join(lines) + "\n"


def main():
    data = json.loads(DATA.read_text())
    CSS_DIR.mkdir(parents=True, exist_ok=True)
    for style in data["styles"]:
        out = CSS_DIR / f"{style['id']}.css"
        out.write_text(render(style))
        print(f"  wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

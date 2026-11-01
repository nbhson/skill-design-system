#!/usr/bin/env python3
"""Add WCAG contrast data to skills/data.json (one-off migration, run once)."""
import json, pathlib

ROOT = pathlib.Path(__file__).parent.parent

def lum(h):
    h = h.lstrip('#')
    if len(h) == 3:
        h = ''.join(c * 2 for c in h)
    r, g, b = (int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = f(r), f(g), f(b)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def cr(a, b):
    la, lb = lum(a), lum(b)
    if la < lb:
        la, lb = lb, la
    return round((la + 0.05) / (lb + 0.05), 2)

def pair(fg, bg, role):
    r = cr(fg, bg)
    return {"foreground": fg, "background": bg, "role": role,
            "ratio": r, "wcagAA": "pass" if r >= 4.5 else "fail"}

# sid -> (pairs, note)
P = {
 'minimalism': ([
    ('#111111', '#FFFFFF', 'body text on primary background'),
    ('#6B7280', '#FFFFFF', 'muted/secondary text on primary background')],
    'All pairs pass WCAG AA (>= 4.5:1). Do not lighten #6B7280 further for small text.'),
 'maximalism': ([
    ('#1A1024', '#FFF1F2', 'body text on soft background'),
    ('#7C3AED', '#FFF1F2', 'accent text on soft background')],
    'Body and accent pairs pass WCAG AA on the light soft background. Neon pink (#FF3EA5) and cyan (#22D3EE) on #FFF1F2 are decoration only — never body text.'),
 'flat-design': ([
    ('#1E293B', '#F8FAFC', 'body text on primary background'),
    ('#64748B', '#F8FAFC', 'secondary text on primary background')],
    'All pairs pass WCAG AA. #64748B sits at 4.55:1 — use it only at >= 15px; for small labels darken to #475569.'),
 'neumorphism': ([
    ('#4A5568', '#ECF0F3', 'body text on element background'),
    ('#4A5568', '#E4E9F2', 'body text on primary background')],
    'All pairs pass WCAG AA, but gray-on-gray leaves little headroom: never use lighter grays for text, and keep text off the shadowed edges of elements.'),
 'claymorphism': ([
    ('#1A1A2E', '#E8EEF5', 'recommended body text on primary background'),
    ('#4A5568', '#E8EEF5', 'recommended muted text on primary background')],
    'The original palette defines no text color. The two text hexes above are RECOMMENDED values (not part of the original palette) that pass WCAG AA. Do not place white text on the mint (#34D399) or pink (#F472B6) clay blocks for small text.'),
 'aurora-ui': ([
    ('#FFFFFF', '#0F0C29', 'body text on darkest background layer'),
    ('#FFFFFF', '#302B63', 'body text on mid background layer')],
    'White on the deep background layers passes WCAG AA. Text over the bright light layers (#6366F1 / #06B6D4) is NOT verified — always keep text over the darkest zones or on a glass panel.'),
 'brutalism-ui': ([
    ('#000000', '#FFFEF0', 'body text on primary background'),
    ('#000000', '#FFE600', 'body text on yellow accent block')],
    'All black-on-bright pairs pass WCAG AA. White text on #FF5C00 or #FF00FF fails AA for small text — invert to black text or use these accents for decoration only.'),
 'collage-art': ([
    ('#1E293B', '#F5F0E8', 'body text on textured background'),
    ('#FFFFFF', '#C026D3', 'text overlay on magenta layer')],
    'Both core pairs pass WCAG AA, but the magenta pair has almost no headroom: any image/texture behind white text on #C026D3 will drop it below 4.5:1 — put text on solid fills.'),
 'skeuomorphism': ([
    ('#FFFFFF', '#8B5A2B', 'body text on brown leather background'),
    ('#FFFFFF', '#3D3D3D', 'text on black leather')],
    'White-on-leather passes WCAG AA at 18px+ and passes AA-large only for smaller/italic text. Avoid dark text on leather (#3D3D3D text on #8B5A2B is ~2.9:1, fail) — engraved/dark text is decoration, not for body copy.'),
 'retro': ([
    ('#FFFFFF', '#0D0221', 'synthwave body text on dark background'),
    ('#FFFFFF', '#663399', 'Y2K text on deep purple')],
    'Dark-era pairs pass WCAG AA. The 50s diner palette is the risk zone: #FF2D2D cherry red on cream #F7E7CE is below 4.5:1 — use cherry red for large display text only, or darken to #D01F1F for body-size text.'),
 'class-morphism': ([
    ('#1A1A1A', '#F5F0EB', 'body text on primary background'),
    ('#6B5B4F', '#F5F0EB', 'secondary text on primary background')],
    'All pairs pass WCAG AA. Champagne gold #C9A96E on the off-white background is ~2.1:1 — decorative accents only, never text.'),
 'glassmorphism': ([
    ('#FFFFFF', '#667EEA', 'body text on gradient start'),
    ('#FFFFFF', '#764BA2', 'body text on gradient end')],
    'WARNING: white text directly on the lighter gradient end (#667EEA) FAILS WCAG AA (3.66:1) — and the rgba(255,255,255,0.15) glass fill lowers it further. Mitigations (in order of preference): (1) keep text over the darker #764BA2 end of the gradient, (2) raise glass fill opacity to 0.30-0.40 behind text, (3) add a soft dark text-shadow. Verify contrast over the BUSIEST background region, not the average.'),
}

path = ROOT / 'skills' / 'data.json'
data = json.loads(path.read_text())
for s in data['styles']:
    pairs, note = P[s['id']]
    s['sections']['contrast'] = {
        'pairs': [pair(fg, bg, role) for fg, bg, role in pairs],
        'notes': note,
    }
data['meta']['version'] = '1.1'
path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '\n')
print('done, version =', data['meta']['version'])

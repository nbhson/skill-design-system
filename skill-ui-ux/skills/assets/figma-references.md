# 🎨 Design References & Inspiration Sources

Curated reference sources for each of the 12 styles. Figma Community search links are stable URLs (`figma.com/community/search?resource_type=files&search=...`) that always return current results.

## Figma Community Search Links

| Style | Figma Community Search |
|---|---|
| Minimalism | [figma.com/community — minimalism UI](https://www.figma.com/community/search?resource_type=files&sort_by=relevancy&query=minimalism%20ui&editor_type=all) |
| Maximalism | [figma.com/community — maximalism](https://www.figma.com/community/search?resource_type=files&sort_by=relevancy&query=maximalism%20ui) |
| Flat Design | [figma.com/community — flat design](https://www.figma.com/community/search?resource_type=files&sort_by=relevancy&query=flat%20design%20ui) |
| Neumorphism | [figma.com/community — neumorphism](https://www.figma.com/community/search?resource_type=files&sort_by=relevancy&query=neumorphism) |
| Claymorphism | [figma.com/community — claymorphism](https://www.figma.com/community/search?resource_type=files&sort_by=relevancy&query=claymorphism) |
| Aurora UI | [figma.com/community — aurora gradient](https://www.figma.com/community/search?resource_type=files&sort_by=relevancy&query=aurora%20gradient) |
| Brutalism UI | [figma.com/community — brutalism](https://www.figma.com/community/search?resource_type=files&sort_by=relevancy&query=brutalism%20web) |
| Collage Art | [figma.com/community — collage web](https://www.figma.com/community/search?resource_type=files&sort_by=relevancy&query=collage%20website) |
| Skeuomorphism | [figma.com/community — skeuomorphism](https://www.figma.com/community/search?resource_type=files&sort_by=relevancy&query=skeuomorphism) |
| Retro | [figma.com/community — retro UI](https://www.figma.com/community/search?resource_type=files&sort_by=relevancy&query=retro%20ui%20kit) |
| Class Morphism | [figma.com/community — luxury glassmorphism](https://www.figma.com/community/search?resource_type=files&sort_by=relevancy&query=luxury%20glassmorphism) |
| Glassmorphism | [figma.com/community — glassmorphism](https://www.figma.com/community/search?resource_type=files&sort_by=relevancy&query=glassmorphism) |

## Real-World Reference Sites

| Style | Exemplary References |
|---|---|
| Minimalism | linear.app, notion.so, stripe.com, Things by Cultured Code |
| Maximalism | gucci.com campaigns, dropbox.com/brand, gumroad.com |
| Flat Design | windows.com (Metro heritage), material.io (baseline), gov.uk |
| Neumorphism | neumorphism.io (generator), Apple Fitness+ marketing pages |
| Claymorphism | Apple iOS 15+ widgets, macOS System Settings previews, dribbble.com/shots "claymorphism" |
| Aurora UI | apple.com/macbook-air, apple.com/vision-pro, vercel.com, linear.app homepage |
| Brutalism UI | balenciaga.com, bloomberg.com (early web), brutalistwebsites.com (gallery) |
| Collage Art | itsnicethat.com, nytimes.com feature pages, behance editorial projects |
| Skeuomorphism | iOS 6 (archival), garageband (plugin UIs), flight simulator dashboards |
| Retro | synthwave UI kits on UI8, y2k.neocities.org (90s web revival), spacejam.com (archival) |
| Class Morphism | awwwards.com luxury category, cartier.com, netflix top-10 premium pages |
| Glassmorphism | apple.com/vision-pro (visionOS windows), iOS Control Center, dribbble.com/shots "glassmorphism", glass.style |

## Stock Asset Sources

| Asset Type | Free Sources |
|---|---|
| Textures (grain, paper) | unsplash.com, texturelabs.org |
| Gradients (aurora, mesh) | meshgradient.com, csshero.org/mesher |
| Noise/shimmer overlays | grainy-gradients.vercel.app |
| Retro pixel fonts | dafont.com, fonts.google.com (Press Start 2P, VT323) |
| Clay 3D shapes | shapecatcher.com, 3dicons.co |
| Glass blur recipes | glass.style, hype4.academy/tools/glassmorphism-generator |

## Quick-Start CSS/Design Tokens

Minimal tokens to begin a project per style (see each style's `SKILL.md` for full palettes):

- **Glassmorphism:** `background: rgba(255,255,255,.15); backdrop-filter: blur(20px) saturate(180%); border: 1px solid rgba(255,255,255,.3); box-shadow: 0 8px 32px rgba(31,38,135,.2);`
- **Minimalism:** `--bg: #FFFFFF; --text: #111111; --text-secondary: #6B7280; --accent: #2563EB; --radius: 4px;`
- **Maximalism:** `--dominant: #7C3AED; --accent-hot: #FF3EA5; --accent-cool: #22D3EE; --text: #1A1024; --border: 3px solid #000;`
- **Flat Design:** `--bg: #F8FAFC; --primary: #3B82F6; --success: #10B981; --warning: #F59E0B; --danger: #EF4444; --text: #1E293B; --radius: 8px;`
- **Collage Art:** `--bg-texture: #F5F0E8; --layer-1: #C026D3; --layer-2: #F59E0B; --layer-3: #06B6D4; --text: #1E293B;`
- **Skeuomorphism:** `--leather: #8B5A2B; --metal: linear-gradient(#C0C0C0, #E8E8E8); --bevel-light: rgba(255,255,255,.3); --bevel-dark: rgba(0,0,0,.4);`
- **Retro (synthwave 80s):** `--bg: #0D0221; --neon-pink: #FF6EC7; --neon-cyan: #00FFFF; --neon-purple: #FF00FF; --glow: 0 0 10px #FF6EC7;`

**Full starter token files (mỗi style 1 file, sinh từ data.json):** [`assets/css/<style-id>.css`](../../assets/css/) — ví dụ `assets/css/minimalism.css`. Tất cả 12 style có file riêng với màu + font tokens dạng CSS custom properties.

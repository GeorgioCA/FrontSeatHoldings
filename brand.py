#!/usr/bin/env python3
"""
Front Seat Holdings — Brand Generator & Dev Server
Usage:
  python3 brand.py logo          # Generate SVG logo files
  python3 brand.py colors        # Print brand color palette
  python3 brand.py export        # Export full brand kit to /brand/
  python3 brand.py serve         # Start local dev server
"""

import http.server
import os
import socketserver
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BRAND_DIR = ROOT / "brand"

# ── BRAND SYSTEM ──────────────────────────────────────────────

BRAND = {
    "name": "Front Seat Holdings Inc.",
    "name_fr": "Holdings Siège Avant Inc.",
    "short": "FSH",
    "tagline": "Leading from the Front",
    "tagline_fr": "À l'avant-garde",
    "year": 2026,
    "domain": "frontseatview.com",
    "email": "contact@frontseatview.com",
    "jurisdiction": "Federal Canada",
    "provinces": ["Ontario", "Alberta"],
    "colors": {
        "primary":      {"name": "Front Amber",   "hex": "#f59e0b", "rgb": (245, 158, 11),  "css": "front-500"},
        "primary-dark": {"name": "Front Bronze",  "hex": "#d97706", "rgb": (217, 119, 6),   "css": "front-600"},
        "primary-light":{"name": "Front Gold",    "hex": "#fbbf24", "rgb": (251, 191, 36),  "css": "front-400"},
        "navy":         {"name": "Navy 900",      "hex": "#0a1c30", "rgb": (10, 28, 48),    "css": "navy-950"},
        "navy-light":   {"name": "Navy 800",      "hex": "#102a43", "rgb": (16, 42, 67),    "css": "navy-900"},
        "surface":      {"name": "Navy 700",      "hex": "#1e3a5f", "rgb": (30, 58, 95),    "css": "navy-800"},
        "white":        {"name": "White",         "hex": "#ffffff", "rgb": (255, 255, 255), "css": "white"},
        "text":         {"name": "Slate Text",    "hex": "#94a3b8", "rgb": (148, 163, 184), "css": "navy-300"},
    },
    "fonts": {
        "primary": "Inter",
        "fallback": "system-ui, -apple-system, sans-serif",
        "weights": [300, 400, 500, 600, 700, 800, 900],
        "headings_weight": 800,
        "body_weight": 400,
    },
    "divisions": [
        {"name": "Front Seat Fiber",     "fr": "Fibre Siège Avant",     "industry": "Telecom",    "emoji": "⚡"},
        {"name": "Front Seat Software",  "fr": "Logiciels Siège Avant", "industry": "Technology", "emoji": "⌨️"},
        {"name": "Front Seat Foods",     "fr": "Aliments Siège Avant",  "industry": "Food",       "emoji": "🥬"},
        {"name": "Front Seat Consulting","fr": "Conseil Siège Avant",   "industry": "Professional Services", "emoji": "📊"},
        {"name": "Front Seat Rentals",   "fr": "Location Siège Avant",  "industry": "Automotive", "emoji": "🚗"},
    ],
}


# ── LOGO GENERATORS ───────────────────────────────────────────

def logo_full() -> str:
    """Full horizontal logo: mark + wordmark (SVG)."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 80" width="480" height="80">
  <defs>
    <linearGradient id="fg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BRAND['colors']['primary-light']['hex']}"/>
      <stop offset="100%" stop-color="{BRAND['colors']['primary']['hex']}"/>
    </linearGradient>
  </defs>
  <!-- Mark -->
  <rect x="4" y="10" width="60" height="60" rx="16" fill="url(#fg)" transform="rotate(4, 34, 40)"/>
  <text x="34" y="55" font-family="Inter, sans-serif" font-weight="900" font-size="34"
        fill="{BRAND['colors']['navy']['hex']}" text-anchor="middle" letter-spacing="-2">FS</text>
  <!-- Wordmark -->
  <text x="84" y="42" font-family="Inter, sans-serif" font-weight="600" font-size="24"
        fill="{BRAND['colors']['navy']['hex']}" letter-spacing="-0.5">Front Seat</text>
  <text x="236" y="42" font-family="Inter, sans-serif" font-weight="800" font-size="24"
        fill="{BRAND['colors']['primary']['hex']}" letter-spacing="-0.5">Holdings</text>
  <text x="84" y="62" font-family="Inter, sans-serif" font-weight="400" font-size="11"
        fill="#94a3b8" letter-spacing="1">HOLDINGS SIÈGE AVANT INC. • CANADA</text>
</svg>"""


def logo_mark() -> str:
    """Square icon mark only (SVG)."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <linearGradient id="fg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{BRAND['colors']['primary-light']['hex']}"/>
      <stop offset="100%" stop-color="{BRAND['colors']['primary-dark']['hex']}"/>
    </linearGradient>
  </defs>
  <rect x="15" y="15" width="90" height="90" rx="22" fill="url(#fg)" transform="rotate(4, 60, 60)"/>
  <text x="60" y="76" font-family="Inter, sans-serif" font-weight="900" font-size="52"
        fill="{BRAND['colors']['navy']['hex']}" text-anchor="middle" letter-spacing="-3">FS</text>
</svg>"""


def favicon() -> str:
    """32x32 favicon SVG."""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" width="32" height="32">
  <rect width="32" height="32" rx="7" fill="{BRAND['colors']['primary']['hex']}"/>
  <text x="16" y="22" font-family="Inter, sans-serif" font-weight="900" font-size="18"
        fill="{BRAND['colors']['navy']['hex']}" text-anchor="middle">FS</text>
</svg>"""


# ── COLOR EXPORT ──────────────────────────────────────────────

def color_swatches() -> str:
    """ASCII color swatch output for terminal."""
    lines = ["\n  ╔══════════════ FRONT SEAT HOLDINGS ══════════════╗"]
    for key, c in BRAND["colors"].items():
        hex_code = c["hex"]
        name = c["name"]
        lines.append(f"  ║  {hex_code}  │  {name:<20} │ {key}  ║")
    lines.append("  ╚═══════════════════════════════════════════════════╝")
    return "\n".join(lines)


def tailwind_config() -> str:
    """Generate Tailwind CSS config colors object."""
    lines = ["// Front Seat Holdings — Tailwind Color Config", "colors: {"]
    for key, c in BRAND["colors"].items():
        lines.append(f'  "{key}": "{c["hex"]}",  // {c["name"]}')
    lines.append("}")
    return "\n".join(lines)


def css_variables() -> str:
    """Generate CSS custom properties."""
    lines = [":root {", "  /* Front Seat Holdings — Brand Colors */"]
    for key, c in BRAND["colors"].items():
        lines.append(f"  --fs-{key}: {c['hex']};  /* {c['name']} */")
    lines.append("}")
    return "\n".join(lines)


# ── BRAND KIT EXPORT ──────────────────────────────────────────

def export_brand_kit():
    """Write all brand assets to /brand/ directory."""
    BRAND_DIR.mkdir(exist_ok=True)

    assets = {
        "logo-full.svg": logo_full(),
        "logo-mark.svg": logo_mark(),
        "favicon.svg": favicon(),
        "colors.css": css_variables(),
        "tailwind-colors.js": tailwind_config(),
    }

    for filename, content in assets.items():
        path = BRAND_DIR / filename
        path.write_text(content)
        print(f"  ✓ {path}")

    # Brand guide markdown
    guide = brand_guide_md()
    (BRAND_DIR / "GUIDE.md").write_text(guide)
    print(f"  ✓ {BRAND_DIR / 'GUIDE.md'}")

    print(f"\n✨ Brand kit exported to {BRAND_DIR}/")


def brand_guide_md() -> str:
    """Generate brand guide markdown."""
    c = BRAND["colors"]
    divisions_md = "\n".join(
        f"| {d['name']} | {d['emoji']} | {d['industry']} | {d['fr']} |"
        for d in BRAND["divisions"]
    )
    colors_md = "\n".join(
        f"| {v['name']} | `{v['hex']}` | {v['rgb']} | {v['css']} |"
        for v in c.values()
    )
    return f"""# Front Seat Holdings — Brand Guide

**Version:** 1.0 · **Year:** {BRAND['year']}

---

## Identity

| Key | Value |
|-----|-------|
| Legal Name (EN) | {BRAND['name']} |
| Legal Name (FR) | {BRAND['name_fr']} |
| Short Code | {BRAND['short']} |
| Tagline | {BRAND['tagline']} |
| Tagline (FR) | {BRAND['tagline_fr']} |
| Domain | {BRAND['domain']} |
| Contact | {BRAND['email']} |
| Jurisdiction | {BRAND['jurisdiction']} |
| Provinces | {', '.join(BRAND['provinces'])} |

---

## Color Palette

{colors_md}

---

## Typography

**Primary Font:** {BRAND['fonts']['primary']}
**Fallback:** `{BRAND['fonts']['fallback']}`
**Weights:** {', '.join(str(w) for w in BRAND['fonts']['weights'])}
**Headings:** Weight {BRAND['fonts']['headings_weight']}
**Body:** Weight {BRAND['fonts']['body_weight']}

---

## Business Divisions

| Division | | Industry | French Name |
|----------|---|----------|-------------|
{divisions_md}

---

## Logo Files

| File | Use |
|------|-----|
| `logo-full.svg` | Header, letterhead, documents |
| `logo-mark.svg` | App icons, social avatars, favicon |
| `favicon.svg` | Browser tab icon (32×32) |

---

## Usage Notes

- Always use the gradient mark on dark backgrounds; flat Front Amber on light.
- Minimum clear space around the logo mark = 1× the mark's height.
- Never rotate, stretch, or recolor the mark outside the approved palette.
- French version preferred in Québec-facing materials: **Holdings Siège Avant Inc.**
"""


# ── DEV SERVER ────────────────────────────────────────────────

def serve(port=8888):
    """Start a simple HTTP server for local preview."""
    os.chdir(ROOT)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"\n  🚀 Front Seat Holdings site live at:")
        print(f"     http://localhost:{port}\n")
        print(f"  Press Ctrl+C to stop.\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n  ✋ Server stopped.")


# ── CLI ───────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    cmd = sys.argv[1]

    if cmd == "logo":
        print(logo_full())
        BRAND_DIR.mkdir(exist_ok=True)
        for name, fn in [("logo-full.svg", logo_full), ("logo-mark.svg", logo_mark), ("favicon.svg", favicon)]:
            (BRAND_DIR / name).write_text(fn())
            print(f"  ✓ {BRAND_DIR / name}")

    elif cmd == "colors":
        print(color_swatches())

    elif cmd == "tailwind":
        print(tailwind_config())

    elif cmd == "css":
        print(css_variables())

    elif cmd == "export":
        export_brand_kit()

    elif cmd == "guide":
        print(brand_guide_md())

    elif cmd == "serve":
        port = int(sys.argv[2]) if len(sys.argv) > 2 else 8888
        serve(port)

    elif cmd == "all":
        export_brand_kit()
        print(f"\nNext:  python3 brand.py serve    # preview site")
        print(f"       open {BRAND_DIR}         # brand assets")

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)


if __name__ == "__main__":
    main()

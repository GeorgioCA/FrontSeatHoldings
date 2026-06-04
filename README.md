# Front Seat Holdings — Corporate Website

**frontseatview.com** — static bilingual corporate site for Front Seat Holdings Inc. (Holdings Siège Avant Inc.), a federal Canadian holding company with six business divisions.

[![Deploy](https://img.shields.io/badge/deploy-Coolify-6C5CE7)](https://coolify.io)
[![Stack](https://img.shields.io/badge/stack-HTML%20%2B%20Tailwind-06B6D4)](https://tailwindcss.com)
[![Server](https://img.shields.io/badge/server-Nginx%20Alpine-009639)](https://nginx.org)

---

## Pages

| Path | Language | Description |
|------|----------|-------------|
| `/` | EN | Homepage — hero, six divisions, story, contact |
| `/fr` | FR | French homepage |
| `/about` | EN | About — company overview, founder profile, office gallery |
| `/fr/a-propos` | FR | À propos (French about) |
| `/careers` | EN | Job listings — 4 expandable postings |
| `/carrieres` | FR | Carrières (French careers) |

---

## Business Divisions

Front Seat Fiber · Front Seat Software · Front Seat Foods · Front Seat Consulting · Front Seat Rentals · Front Seat Recruitment

---

## Tech Stack

- **HTML5** + **Tailwind CSS** (CDN, no build step)
- **Inter** font (Google Fonts)
- **Nginx 1.27 Alpine** (Docker)
- **Coolify** for CI/CD (watches `main` branch)

---

## Brand

| Asset | Location |
|-------|----------|
| Color palette | `brand/colors.css`, `brand/tailwind-colors.js` |
| Logo (full) | `brand/logo-full.svg` |
| Logo (mark) | `brand/logo-mark.svg` |
| Favicon | `brand/favicon.svg` |
| Full guide | `brand/GUIDE.md` |

**Colors:** Navy `#0a1c30` · Front Amber `#f59e0b` · Front Gold `#fbbf24`

---

## Run Locally

### Docker

```bash
docker compose up -d
# → http://localhost:8080
```

### Or just static files

```bash
python3 -m http.server 8080
# → http://localhost:8080
```

---

## Project Structure

```
.
├── index.html          # EN homepage
├── fr.html             # FR homepage
├── about.html          # EN about
├── a-propos.html       # FR about
├── careers.html        # EN careers
├── carrieres.html      # FR careers
├── Dockerfile          # Nginx Alpine image
├── docker-compose.yaml # Local dev
├── nginx.conf          # Routes, caching, security headers
├── img/                # Site images
│   ├── Founder-Georgio.png
│   └── office-*.webp
├── brand/              # Logo, colors, brand guide
└── .gitignore
```

---

## Deployment

Push to `main` → Coolify rebuilds the Docker image → deploys to production.

All static assets must be in the Dockerfile `COPY` instructions. Nginx routes defined in `nginx.conf`.

---

## License

MIT — see [LICENSE](LICENSE)

# ViceBase — GTA VI Resource Hub

A mobile-friendly, neon gaming-themed GTA VI resource website built on static HTML, CSS and vanilla JavaScript. This version contains 36 editorially sourced guides across 8 categories, 53 indexed routes including a dedicated GTA 6 Leonida map, first-party video links, a live local search index, a PS5/Xbox storage calculator, a download-time estimator, and a saved launch checklist, a native 24-pin interactive Leonida concept atlas with filters/zoom/bookmarks, a live store-region-selectable release countdown, and a "Where to Buy" deal desk with manually checked PS5/Xbox storefront prices and 6 money-saving tips.

**Editorial as-of:** 2026-11-18. The game is scheduled to launch 2026-11-19. Update launch-day articles as soon as actual play can be verified; guides marked `VERIFY AT LAUNCH` are not claims to contain tested gameplay before release.

## Repo layout

- `site/` — **Vercel root directory**; contains pre-generated static pages, JS/CSS, images, `robots.txt`, `sitemap.xml`, metadata, `vercel.json`.
- `source/content.py` — guide content, categories, roadmap and video links.
- `source/build.py` — generates the complete static website from the editorial content.
- `source/map_atlas.py` — original illustrated GTA 6 map SVG and sourced region/theme-marker metadata.
- `site/map/` + `site/assets/map.js` / `map.css` — interactive native map experience, drag/zoom, filters, search and device-local bookmarks.
- `source/validate.py` — tests metadata, JSON-LD, and internal links.
- `source/make_og.py` — generates share-preview artwork (requires Pillow and CairoSVG).
- `database/schema.sql` — Neon Postgres tables for guide metadata, resource requests and feedback, created in the separate `gta6-vicebase` Neon project.

## Deploy to a NEW GitHub and Vercel project

1. Use the separate `jeffreyjk1991/gta6-vicebase` repository.
2. Unzip this folder and push **the contents** (including both `site` and `source`) to the repository's `main` branch.
3. In Vercel, **Add New Project** and import that new GitHub repository. Set **Root Directory = `site`**. Choose `Other` / static framework, with no build command. This publishes the already-generated files. Use a distinct Vercel project name (for example, `gta6-vicebase`).
4. Connect the GitHub integration. On future commits, Vercel will deploy the updated `site/` files automatically.
5. Get the actual production URL, then regenerate SEO metadata if it differs from the initial planned `https://gta6-vicebase.vercel.app`. Run `BASE_URL=https://<your-deployed-domain> python source/build.py` and push updated `site/`.
6. Optionally connect the separate Neon project `gta6-vicebase`. Its database is `vicebase`. The static build **does not require database credentials**. The Neon schema is ready for later authenticated moderation, guide request forms and user feedback, but those APIs are **not enabled** in this version.

No credentials, API tokens or `.env` files are included. Do not add database connection credentials to client-side JavaScript or commit them to GitHub.

## Editing content

From repo root:

```bash
python source/build.py
python source/validate.py
```

Static generated pages are source-controlled so a GitHub + Vercel deployment needs no Python build step. Update a guide in `source/content.py`, run the build, validate, and commit both the source and regenerated `site/` outputs.

## SEO notes

- Individual guide URLs, canonical links, unique titles/descriptions, Open Graph markup, FAQ structured data, articles, breadcrumbs, search, `robots.txt` and `sitemap.xml` are generated.
- The build's default canonical hostname is a **planned** domain, not proof that it is deployed. Set `BASE_URL` to the live domain before indexing.
- Editorial pages distinguish Rockstar/PlayStation/Xbox-supported facts from guidance requiring in-game verification. No keyword-stuffed fake cheats or missions.
- After the site is live, submit the correct sitemap via Google Search Console and monitor indexing. Search engines and AI systems do not guarantee a top ranking.

## Included original resources

- Vice City-inspired skyline vector artwork, typography and brand icon, all created for ViceBase rather than copied game artwork.
- Official Rockstar and platform information linked from every guide; video links go to the publisher's original pages.

ViceBase is an independent fan project unaffiliated with Rockstar Games, Take-Two, Sony or Microsoft.

## Price desk policy (November 18, 2026)

The `/buy/` prices are a manually verified U.S. snapshot of $79.99 Standard Edition at mainstream sellers, not an automated price tracking service. Check the seller at checkout. Target Circle Card may have a 5% discount on eligible orders, but Target excludes GTA software from some general promotions; no savings are guaranteed. Retail cases are code-in-box, not game discs.

## Map licensing and accuracy

The Leonida map illustration is original and does not reproduce a third-party tile set, leaked data or an official Rockstar map. Region names are sourced from Rockstar; exact coastlines, roads and pin placements are illustrative. The map's six primary regions are labeled as officially named; the other 18 markers are clearly identified as noncanonical exploration themes. It also offers an outbound link to the detailed fan map at vice-city.app/map, with no asset scraping or embedding.

Run `python source/test_map_inline.py` to smoke-test the atlas with Chromium in a network-restricted environment (the QA harness inlines local assets).

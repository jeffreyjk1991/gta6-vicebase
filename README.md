# GTASIX — GTA VI Resource Hub

A mobile-friendly GTA VI resource website built with static HTML, CSS and vanilla JavaScript. It includes 49 source-linked guides, 79 indexable routes, a mission and gameplay helper, a community Leonida map, character profiles, settings recommendations, technical troubleshooting, storage and download calculators, and device-local saved checklists.

**Player-help update: November 20, 2026.** The obsolete release countdown is removed. The homepage, navigation and tools now prioritize what players can use while playing. Individual articles retain their own review dates and verification labels.

## Mission and gameplay helper

`/gta-6-mission-help/` offers eight problem paths and sourced hints for Prologue, Gone Fishing, Gear Up and Lab Fees. Detailed hints and solutions are opt-in. Coverage is deliberately limited to the cited walkthroughs; general checklists are editorial suggestions.

- `source/mission_helper.py` owns content, crawlable HTML, metadata and structured data.
- `site/assets/mission-help.js` handles matching, hints, checklist completion, explicit Save/Resume/Clear and safe copy/share fallback.
- `site/assets/mission-help.css` provides responsive presentation.
- Objective notes never leave the page, are never saved, and are excluded from copied text and URLs. Saved choices and check marks remain only in that browser.
- `source/gameplay_guides.json` supplies new navigation, driving and original Vice City comparison guides to content, metadata and related sections.

## Build and validation

```bash
python3 -m pip install -r source/requirements.txt
python3 source/build.py
python3 source/validate.py
python3 source/seo_audit.py
```

The build defaults to `https://www.gtasix.tech`, the live final hostname after the apex-domain redirect. `BASE_URL` overrides it for alternate build targets. Search Console's verification token is retained as a verification resource, not treated as an HTML content page by the validator.

## Repo layout

- `site/` — **Vercel root directory**; contains pre-generated static pages, JS/CSS, images, `robots.txt`, `sitemap.xml`, metadata, `vercel.json`.
- `source/content.py` — guide content, categories, roadmap and video links.
- `source/build.py` — generates the complete static website from the editorial content.
- `source/map_atlas.py` — original illustrated GTA 6 map SVG and sourced region/theme-marker metadata.
- `site/map/` + `site/assets/map.js` / `map.css` — interactive native map experience, drag/zoom, filters, search and device-local bookmarks.
- `source/validate.py` — tests metadata, JSON-LD, and internal links.
- `source/make_og.py` — generates share-preview artwork (requires Pillow and CairoSVG).
- `database/schema.sql` — Neon Postgres tables for guide metadata, resource requests and feedback, created in the separate `gta6-vicebase` Neon project.

## Deployment and domain setup

1. Use the separate `jeffreyjk1991/gta6-vicebase` repository.
2. Unzip this folder and push **the contents** (including both `site` and `source`) to the repository's `main` branch.
3. In Vercel, **Add New Project** and import that new GitHub repository. Set **Root Directory = `site`**. Choose `Other` / static framework, with no build command. This publishes the already-generated files. Use a distinct Vercel project name (for example, `gta6-vicebase`).
4. Connect the GitHub integration. On future commits, Vercel will deploy the updated `site/` files automatically.
5. The canonical URL now defaults to `https://www.gtasix.tech`. Attach the domain in the actual Vercel project before search indexing. See [`DOMAIN-SETUP.md`](DOMAIN-SETUP.md) for verification, DNS and redirects.
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
- The canonical hostname is **`https://www.gtasix.tech`**. That does not prove DNS or a Vercel domain assignment is active. Verify the live host before asking search engines to index it.
- Editorial pages distinguish Rockstar/PlayStation/Xbox-supported facts from guidance requiring in-game verification. No keyword-stuffed fake cheats or missions.
- After the site is live, submit the correct sitemap via Google Search Console and monitor indexing. Search engines and AI systems do not guarantee a top ranking.

## Included original resources

- Vice City-inspired skyline vector artwork, typography and brand icon, all created for GTASIX rather than copied game artwork.
- Official Rockstar and platform information linked from every guide; video links go to the publisher's original pages.

GTASIX is an independent fan project unaffiliated with Rockstar Games, Take-Two, Sony or Microsoft.

## Price desk policy (November 18, 2026)

The `/buy/` prices are a manually verified U.S. snapshot of $79.99 Standard Edition at mainstream sellers, not an automated price tracking service. Check the seller at checkout. Target Circle Card may have a 5% discount on eligible orders, but Target excludes GTA software from some general promotions; no savings are guaranteed. Retail cases are code-in-box, not game discs.

## Detailed GTA VI map and official poster (November 18, 2026)

- The homepage references the **Official Cover Art**, served from Rockstar Games' published artwork page. Copyright is retained by Rockstar. The previous original skyline remains as a fallback; the GTASIX identity replaces the old site name.
- `/map/` defaults to a high-resolution **community reconstruction** of Leonida, using YANIS/GTADB CC BY 4.0 imagery processed by GTAMI. Zooming progressively requests a 4096px or 8192px map, which includes streets, blocks, building footprints and routes. It is *not* the officially confirmed in-game map. Building interiors, accessible doors and exact layouts cannot be verified before release.
- The map also includes 771 named community places, derived from GTADB community landmark data, filtered by confidence and category. Pins are community-estimated, not guaranteed exact in-game positions. The default source data is `site/assets/gtadb-landmarks.json` (already committed on GitHub). When packaging without that optional large asset, the map can load the exact current index from the GitHub repository; it falls back to the concept atlas when imagery is unavailable.
- Map interface supports pointer drag, mouse-wheel and touch-pinch zoom, region shortcuts, place search, category filters, bookmarks, and device-local custom pins, plus a switch back to our original neon concept map.
- See `source/GTADB_DATA_CREDITS.md` for links, sources, attribution and licensing. The externally hosted map image must remain credited. Third-party map and Rockstar artwork remain the rights of their respective owners.

This is an independent, unofficial fan guide. Map accuracy will need launch-day verification. Do not label the reconstruction as official or a screenshot of the retail game.

## November 18 SEO and AI search readiness update

- New source-checked `/gta-6-facts/` question-and-answer hub with official links to game platforms, regions, and edition details.
- Descriptive metadata for high-intent guides, character, map, storefront and tool pages, preserving the existing GTASIX design.
- Stronger supplementary guidance on PS5 storage, M.2 SSD compatibility, launch timings, download errors, price comparisons and region restrictions.
- Simplified sitemap and clearer structured data; 404 pages are marked `noindex`. Public crawling is explicitly allowed for OAI-SearchBot, Googlebot and Bingbot. These are technical prerequisites, **not ranking guarantees**.
- Regenerate and audit with `python source/build.py && python source/seo_audit.py && python source/validate.py`.
- See [`SEO-OPERATIONS.md`](SEO-OPERATIONS.md) for the manual actions: confirm a publicly accessible Vercel production URL, verify the site in Search Console and submit the sitemap.

## GTASIX identity and domain migration (November 18, 2026)

The public brand is now **GTASIX** (`gtasix.tech`). Header, footer, page titles, canonical links, Open Graph/Twitter cards, Article/Organization/WebSite JSON-LD, XML sitemap, robots.txt, installable web manifest, favicon and social sharing artwork are updated from the source generator. The old Github and Neon project identifiers remain untouched to preserve integrations. Browser-local saved items use new `gtasix-` storage keys with backward-compatible fallback to their earlier names when viewed on the same origin. See [`DOMAIN-SETUP.md`](DOMAIN-SETUP.md) for registrar and Vercel configuration.

## Verification for the November 20 player-help update

The source build and static audits cover all 79 indexable pages, canonical URLs, distinct page titles, schema parsing, sitemap membership and more than 3,100 internal links. The mission helper additionally validates URL options, stored plans and unavailable clipboard/storage behavior. Browser verification should cover the homepage entry point, mission hint disclosure, saved plan resume, search, technical fallback and narrow-screen layout whenever these features change.

Historical one-off scripts such as `fix_countdown.py` and `update_buy.py` are migration artifacts; do not run them as part of the current build. The supported entry point is `source/build.py`.

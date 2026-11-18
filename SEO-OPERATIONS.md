# ViceBase: search discovery and AI answer visibility

Last checked: November 18, 2026. These actions improve technical readiness; they **cannot guarantee a #1 ranking** or inclusion in an AI answer.

## What this release implements

- Individual crawlable HTML documents; distinct SEO titles, descriptions and one primary H1 per page.
- Correct absolute canonical URLs, 404 marked noindex, robots.txt and XML sitemap.
- Explicit allowance for OAI-SearchBot (ChatGPT Search), Googlebot and Bingbot.
- Source-checked, concise first-paragraph answers; supporting official links and prominent dates.
- A single GTA 6 confirmed-facts page linking players to details, regional map, character pages, storage utilities and store comparisons.
- Structured data that matches the visible pages: WebPage, Organization, WebSite, VideoGame, Article, BreadcrumbList and visible FAQs.
- Nine detailed high-intent guide supplements containing specific platform instructions and comparison tables.
- Static HTML accessibility and internal-link tests via `source/seo_audit.py`.

## Most urgent manual actions

1. **Check production hostname.** Open the live Vercel project and confirm that `https://gta6-vicebase.vercel.app/`, `/gta-6-facts/`, `/map/`, `/characters/`, `/robots.txt` and `/sitemap.xml` all return successful public responses (not Vercel Authentication). If the actual production domain differs, run `BASE_URL=https://YOUR-DOMAIN python source/build.py`, then deploy the generated changes.
2. **Verify ownership in Google Search Console.** Add the exact canonical site/domain. Submit `https://gta6-vicebase.vercel.app/sitemap.xml`. Inspect the homepage, confirmed-facts hub, map and top-five guide URLs with URL Inspection and request indexing where available. Monitor page indexing, indexing exclusions and query performance; Google chooses whether and when to index.
3. **Add the site in Bing Webmaster Tools.** Submit the same sitemap. IndexNow can be configured later once domain ownership/key are verified; never deploy a fake verification key.
4. **Check Vercel Deployment Protection and bot firewall.** Search engines and OAI-SearchBot must be able to fetch the public pages with HTTP 200; a robots.txt allow rule does not override login or 403.
5. **Check launch-day facts.** When GTA VI launches, personally verify gameplay guides and release updates. Keep `VERIFY AT LAUNCH` labels until testing has been performed; write original mission, achievement, map and vehicle coverage rather than large sets of thin pages.

## How to verify the update

```sh
python source/build.py
python source/seo_audit.py
python source/validate.py
```

Metadata must describe information **actually visible on the page**. Do not add fake review scores, search snippets, or unverifiable first-person expertise. Re-check external references when prices or game build details change.

## Signals that determine what to improve next

- Search Console: queries, impressions, CTR, index coverage, pages that earn clicks, mobile usability and Core Web Vitals.
- Bing Webmaster Tools: crawl/index errors and the URLs actually discovered.
- Vercel: runtime error logs, public accessibility and map/font image load times.
- Referral analysis from permitted traffic analytics, if enabled; do not assume an AI result mentioned the site just because a particular test did.

## Primary guidance

- Google Search Central: `https://developers.google.com/search/docs/appearance/ai-features`
- Google Search Central: `https://developers.google.com/search/docs/fundamentals/seo-starter-guide`
- OpenAI search crawler guidance: `https://developers.openai.com/api/docs/bots`
- Rockstar GTA VI: `https://www.rockstargames.com/VI`

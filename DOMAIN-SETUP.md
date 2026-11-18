# GTASIX.tech domain deployment checklist

**Canonical host:** `https://gtasix.tech` (without `www`).
**Public site name:** `GTASIX`; branding: GTASIX.TECH and GTA 6 independent field guide.
**Existing repository:** `jeffreyjk1991/gta6-vicebase` — **do not rename** without explicitly migrating Git integration.
**Site root for Vercel:** `site/` — static HTML output (no build command).

## Attach the purchased domain to the actual Vercel project

1. In the Vercel account/team **where the GTA 6 site actually lives**, open its project > **Settings > Domains**. Add `gtasix.tech` as its production domain. Add `www.gtasix.tech` as well and set it to redirect to the apex `gtasix.tech` (308 preferred).
2. In the domain registrar's DNS dashboard, follow Vercel's verification records. The standard Vercel suggestions for an externally hosted zone were an `A` record for `@` to `76.76.21.21` and a `CNAME` for `www` to `cname.vercel-dns.com` when checked November 18, 2026; if Vercel displays project-specific values, **follow the project's values instead**. Clear conflicting A/AAAA or CNAME records only after confirming what they are used for. Do not modify MX or unrelated TXT records.
3. Check the project shows the new domain **Verified** with a valid HTTPS certificate and that `https://gtasix.tech/`, `/map/`, `/characters/`, `/robots.txt` and `/sitemap.xml` return HTTP 200 publicly.
4. Once the new host works, add a permanent redirect from the old `.vercel.app` hostname to `https://gtasix.tech` if you control the Vercel project. Keep paths. Do **not** force a redirect while the new domain is unconfigured, or visitors can lose access to the site.
5. In Google Search Console verify the `gtasix.tech` Domain property; submit `https://gtasix.tech/sitemap.xml`. Update Bing Webmaster Tools and analytics site settings. Inspect Google indexed canonical URLs after DNS propagates.

**Important access limitation as of November 18, 2026:** The connected Vercel team here lists only `chattopaper` and `scroll-my-faith`; the GTA 6 project is not visible in that team and Vercel reports the new domain is not yet registered to it. The repository code is prepared but this does not, by itself, connect the domain or DNS.

## Local regeneration

Run `python source/build.py && python source/seo_audit.py && python source/validate.py`. Default canonical origin is now `https://gtasix.tech`. Optional override: `BASE_URL=https://custom-domain python source/build.py`.

GTASIX is an unofficial fan-made resource and is not associated with Rockstar Games.

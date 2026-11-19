"""Human-edited SEO descriptions and titles for important GTA VI user intents.

Do not fabricate game details or use search-volume claims. Metadata must summarize
content visible on each page, and search rankings cannot be guaranteed.
"""
import re

TITLE_OVERRIDES = {
    '/guides/gta-6-how-to-save/': 'How to Save in GTA 6: Autosave & 15 Slots | GTASIX',
    '/guides/gta-6-how-to-switch-characters/': 'GTA 6: How to Switch Jason & Lucia | GTASIX',
    '/guides/gta-6-jason-lucia-voice-actors/': 'GTA 6 Voice Actors: Jason, Lucia & Cast | GTASIX',
    '/guides/gta-6-reviews-scores/': 'GTA 6 Reviews: Metacritic Score & Verdict | GTASIX',
    '/': 'GTA 6 Guides: Saves, Cheats, Map & Settings | GTASIX',
    '/map/': 'GTA 6 Map: Detailed Leonida & Vice City | GTASIX',
    '/characters/': 'GTA 6 Characters: Jason, Lucia & More | GTASIX',
    '/buy/': 'Where to Buy GTA 6: PS5 & Xbox Prices | GTASIX',
    '/videos/': 'Official GTA 6 Trailers & Gameplay Videos | GTASIX',
    '/tools/': 'GTA 6 Storage Calculator & Download Timer | GTASIX',
    '/guides/': 'GTA 6 Guides: Saves, Cheats, Map & Settings | GTASIX',
    '/guides/gta-6-best-settings/': 'GTA 6 Best Settings: PS5, Xbox, Controls & Camera | GTASIX',
    '/gta-6-facts/': 'GTA 6 Confirmed Facts: Launch, Map & Cast | GTASIX',
    '/guides/gta-6-download-size-ps5-xbox/': 'GTA 6 Download Size: PS5 & Xbox Storage | GTASIX',
    '/guides/best-ps5-ssd-requirements-for-gta-6/': 'Best PS5 SSD Specs for GTA 6 | GTASIX',
    '/guides/gta-6-pc-release-system-requirements/': 'GTA 6 PC Release & Requirements: What Is Known | GTASIX',
    '/guides/gta-6-release-date-and-time/': 'GTA 6 Out Now: Release Date & Platforms | GTASIX',
    '/guides/gta-6-console-performance-fps/': 'GTA 6 FPS & Console Performance: Confirmed | GTASIX',
    '/guides/gta-6-leonida-vice-city-map/': 'GTA 6 Map: Leonida Regions Explained | GTASIX',
    '/guides/gta-6-cheat-codes/': 'GTA 6 Cheats: PS5, Xbox Codes & Unlocks | GTASIX',
    '/guides/gta-6-vehicles-best-cars/': 'GTA 6 Cars & Vehicles: What Is Verified | GTASIX',
    '/guides/gta-6-missions-walkthroughs/': 'GTA 6 Missions & Walkthroughs: Guide Hub | GTASIX',
    '/guides/gta-6-best-price-where-to-buy/': 'GTA 6 Price Comparison & Buying Tips | GTASIX',
    '/guides/gta-6-jason-lucia-characters/': 'GTA 6 Jason & Lucia: Character Guide | GTASIX',
    '/guides/gta-6-preload-not-working/': 'GTA 6 Preload Not Working? PS5 & Xbox Fixes | GTASIX',
}

META_OVERRIDES = {
    '/guides/gta-6-release-date-and-time/': 'GTA 6 released November 19, 2026 for PS5 and Xbox Series X|S. Rockstar confirms availability; PC release date remains unannounced.',
    '/guides/gta-6-cheat-codes/': 'GTA 6 cheats reported by hands-on reviewers: story unlocks, how to enter them, money codes, and warnings about saving and trophies.',
    '/guides/gta-6-how-to-save/': 'How to save GTA 6 on PS5 and Xbox: 15 manual save slots, autosave, and why Save Game is greyed out during missions.',
    '/guides/gta-6-how-to-switch-characters/': 'GTA 6 controls for switching Jason and Lucia on PS5 and Xbox, when the Partner Menu unlocks, and why swapping is unavailable.',
    '/guides/gta-6-jason-lucia-voice-actors/': 'GTA 6 voice actor confirmations: Dylan Rourke as Jason, Manni L. Perez as Lucia, and Stephen Root as Brian.',
    '/guides/gta-6-reviews-scores/': 'GTA 6 reviews and ratings: dated November 19 Metacritic 99/100 report, critic impressions, and current review links.',
    '/': 'GTA 6 launch guides: saving progress, switching characters, cheat codes, reviews, voice actors, gameplay settings and the Leonida map.',
    '/map/': 'Explore the GTA 6 Leonida and Vice City community map with street-level zoom, location search and saved pins. Unofficial reconstruction, clearly labeled.',
    '/characters/': 'Meet GTA 6 characters Jason Duval, Lucia Caminos, Cal Hampton and more. Read verified backgrounds, connections and official Rockstar sources.',
    '/buy/': 'Compare GTA 6 PS5 and Xbox retailer listings, Standard and Ultimate editions, legitimate discounts and code-in-box warnings. Prices are dated snapshots.',
    '/videos/': 'Watch official GTA 6 trailers, extended gameplay footage and launch videos from Rockstar Games. Find real sources, not fake gameplay or leaks.',
    '/tools/': 'Check GTA 6 PS5 storage space, estimate download time and use the launch checklist. Understand the 212 GB PS5 recommendation and Xbox differences.',
    '/guides/': 'Browse GTA 6 settings, gameplay tips, maps, PS5 and Xbox guides, characters, storage fixes, walkthroughs and official-source answers.',
    '/guides/gta-6-best-settings/': 'Best GTA 6 settings for PS5, PS5 Pro and Xbox: tune aim assist, motion blur, driving camera, HDR and comfort. Use our interactive settings finder.',
    '/gta-6-facts/': 'GTA 6 confirmed facts: November 19, 2026 launch, PS5 and Xbox platforms, Leonida regions, Jason and Lucia, storage, editions and open questions.',
    '/guides/gta-6-download-size-ps5-xbox/': 'PS5 recommends at least 212 GB free for GTA 6. Learn what that number means, how to check Xbox storage and how to make space safely.',
    '/guides/best-ps5-ssd-requirements-for-gta-6/': 'Need more GTA 6 space on PS5? Check Sony-compatible M.2 SSD specifications, heatsink requirements and installation guidance before you buy.',
    '/guides/gta-6-pc-release-system-requirements/': 'Is GTA 6 coming to PC? See what Rockstar has confirmed about launch platforms, and why unannounced PC release dates and system specs are guesses.',
    '/guides/gta-6-release-date-and-time/': 'GTA 6 launches November 19, 2026, on PS5 and Xbox Series X|S. Check store-region unlock timing, preload status and official sources.',
    '/guides/gta-6-console-performance-fps/': 'What is confirmed about GTA 6 frame rates and PS5, PS5 Pro and Xbox performance? Separate official statements from benchmark guesses.',
    '/guides/gta-6-leonida-vice-city-map/': 'Explore Rockstar-named GTA 6 locations including Vice City and Leonida Keys. Compare official regions with the unofficial fan-made interactive map.',
    '/guides/gta-6-cheat-codes/': 'Looking for GTA 6 cheat codes? Learn which claims remain unverified and how to spot fake code generators before the launch build can be tested.',
    '/guides/gta-6-missions-walkthroughs/': 'Find the GTA 6 mission guide hub and see what will be tested after launch. No invented mission lists, spoilers or unverified objectives.',
    '/guides/gta-6-best-price-where-to-buy/': 'Compare GTA 6 Standard Edition prices on PS5 and Xbox, digital versus code-in-box copies and safe ways to save at checkout.',
    '/guides/gta-6-jason-lucia-characters/': 'Who are Jason Duval and Lucia Caminos in GTA 6? See Rockstar-confirmed story details and links to full character dossiers.',
    '/guides/gta-6-preload-not-working/': 'GTA 6 preload missing or stuck? Check store entitlement, console storage, download queues, network status and safer first troubleshooting steps.',
}

def _tidy(text, limit=158):
    text = ' '.join(text.split())
    if len(text) <= limit:
        return text
    candidate = text[:limit].rsplit(' ', 1)[0].rstrip(' ,;:-')
    return candidate + '…'


def meta_for(path, title, description, articles):
    t = TITLE_OVERRIDES.get(path, title)
    if path.startswith('/guides/') and path.endswith('/') and path not in ('/guides/',):
        # Brand should not consume the useful query phrase.
        if path not in TITLE_OVERRIDES:
            t = re.sub(r'\s*\| GTASIX GTA VI$', ' | GTASIX', t)
    d = META_OVERRIDES.get(path)
    if not d:
        d = description
        if len(' '.join(d.split())) < 102 and path.startswith('/guides/'):
            slug = path.strip('/').split('/')[-1]
            matching = next((a for a in articles if a['slug'] == slug), None)
            if matching:
                d = matching['answer']
                if len(d) < 90:
                    d += ' ' + matching['summary']
    return t, _tidy(d)

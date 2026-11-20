"""Compact homepage navigation, with secondary resources in native disclosures."""
from html import escape


def render_home(guide_count, search_markup, icon):
    shortcuts = [
        ('gamepad-2', 'Mission help', 'Hints and your next step.', '/gta-6-mission-help/'),
        ('map-pin', 'Interactive map', 'Explore and save places.', '/map/'),
        ('crosshair', 'Settings finder', 'Tune your controls and camera.', '/guides/gta-6-best-settings/'),
        ('wrench', 'Fix a problem', 'Crashes, loading and errors.', '/gta-6-help/'),
    ]
    groups = [
        {
            'id': 'trending-gta-6-questions', 'icon': 'gamepad-2',
            'title': 'Missions & gameplay', 'description': 'Walkthroughs, driving, saving & secrets',
            'links': [
                ('Mission walkthroughs', 'Find a guide for your current objective.', '/guides/gta-6-missions-walkthroughs/'),
                ('No mission marker?', 'Work out what to do next.', '/guides/gta-6-no-mission-marker-what-to-do/'),
                ('How to save', 'Save slots, autosave and progress.', '/guides/gta-6-how-to-save/'),
                ('Switch characters', 'Jason, Lucia and the Partner Menu.', '/guides/gta-6-how-to-switch-characters/'),
                ('Driving tips & physics', 'Cornering, controls and route practice.', '/guides/gta-6-driving-tips-and-physics/'),
                ('Cheat codes', 'Reported codes and their restrictions.', '/guides/gta-6-cheat-codes/'),
                ('Money guide', 'Money-making tips and what to verify.', '/guides/gta-6-money-making-guide/'),
                ('100% completion', 'Trophies, achievements and tracking.', '/guides/gta-6-achievements-trophies-100-percent/'),
            ],
            'categories': [('Gameplay guides', 'gameplay'), ('Completion & secrets', 'collectibles')],
        },
        {
            'id': 'world-map-preview', 'icon': 'map-pin',
            'title': 'Explore Leonida', 'description': 'Map, familiar places, characters & story',
            'links': [
                ('Map & saved places', 'Browse the community map of Leonida.', '/map/'),
                ('Vice City: then & now', 'Compare locations and familiar themes.', '/guides/gta-6-map-vs-vice-city/'),
                ('Leonida & Vice City', 'Get to know the regions and setting.', '/guides/gta-6-leonida-vice-city-map/'),
                ('Meet the characters', 'Explore the cast and their connections.', '/characters/'),
                ('Jason & Lucia', 'Get to know the two lead characters.', '/guides/gta-6-jason-lucia-characters/'),
                ('Voice actors', 'The voices behind Jason and Lucia.', '/guides/gta-6-jason-lucia-voice-actors/'),
                ('Easter eggs & secrets', 'Track discoveries and source checks.', '/guides/gta-6-easter-eggs-and-secrets/'),
            ],
            'categories': [('World & story guides', 'world')],
        },
        {
            'id': 'settings-spotlight', 'icon': 'wrench',
            'title': 'Setup, tools & fixes', 'description': 'Settings, calculators, downloads & troubleshooting',
            'links': [
                ('Settings finder', 'Choose your console and play style.', '/guides/gta-6-best-settings/'),
                ('Storage calculator', 'Check how much space to clear.', '/tools/#storage'),
                ('Download estimator', 'Estimate your wait before installing.', '/tools/#download'),
                ('Ready-to-play checklist', 'Save your setup progress.', '/tools/#checklist'),
                ('Technical Help Center', 'Find steps for your console and issue.', '/gta-6-help/'),
                ('Install & download size', 'Check platform storage guidance.', '/guides/gta-6-download-size-ps5-xbox/'),
                ('PS5 SSD guide', 'Check expansion-drive requirements.', '/guides/best-ps5-ssd-requirements-for-gta-6/'),
                ('Xbox storage guide', 'Understand expansion options.', '/guides/xbox-series-x-s-storage-expansion-gta-6/'),
                ('Audio & controller help', 'Work through sound and input problems.', '/guides/gta-6-audio-controller-problems/'),
            ],
            'categories': [('Troubleshooting', 'troubleshooting'), ('Storage & SSD', 'storage'), ('Platforms & performance', 'platforms')],
        },
        {
            'id': 'buy-spotlight', 'icon': 'clapperboard',
            'title': 'Buying & game updates', 'description': 'Editions, official videos, release info & Online',
            'links': [
                ('Where to buy', 'Compare retailers and dated prices.', '/buy/'),
                ('Editions compared', 'Understand what each edition includes.', '/guides/gta-6-editions-compared/'),
                ('Release & platforms', 'Check the official availability status.', '/guides/gta-6-release-date-and-time/'),
                ('GTA 6 Online', 'Multiplayer news and confirmed details.', '/gta-6-online/'),
                ('PC release information', 'What is known about a PC version.', '/guides/gta-6-pc-release-system-requirements/'),
                ('Confirmed facts', 'Source-linked answers in one place.', '/gta-6-facts/'),
                ('Official videos', 'Watch trailers and gameplay footage.', '/videos/'),
                ('Reviews & ratings', 'Read the critic-score snapshot.', '/guides/gta-6-reviews-scores/'),
            ],
            'categories': [('Launch & editions', 'launch'), ('Videos & news', 'media')],
        },
    ]

    cards = ''.join(
        f'<a class="home-shortcut{ " home-shortcut-featured" if i == 0 else ""}" href="{url}">'
        f'<span class="home-shortcut-top">{icon(symbol, 23)}<span aria-hidden="true">↗</span></span>'
        f'<h3>{escape(title)}</h3><p>{escape(description)}</p></a>'
        for i, (symbol, title, description, url) in enumerate(shortcuts)
    )
    disclosures = []
    for group in groups:
        # Keep existing bookmarked homepage sections at their new topic groups.
        summary_id = {'world-map-preview': 'people-of-leonida', 'buy-spotlight': 'gta-6-quick-answers'}.get(group['id'])
        summary_attrs = f' id="{summary_id}"' if summary_id else ''
        label_attrs = ' id="gta-6-quick-answers-heading"' if group['id'] == 'buy-spotlight' else ''
        links = ''.join(
            f'<li><a href="{url}"><strong>{escape(title)}</strong><span>{escape(description)}</span></a></li>'
            for title, description, url in group['links']
        )
        categories = ''.join(
            f'<a href="/categories/{slug}/">{escape(title)} <span aria-hidden="true">↗</span></a>'
            for title, slug in group['categories']
        )
        disclosures.append(
            f'<details class="home-group" id="{group["id"]}" name="home-resources">'
            f'<summary{summary_attrs}><span class="home-group-icon">{icon(group["icon"], 22)}</span>'
            f'<span class="home-group-copy"><strong{label_attrs}>{escape(group["title"])}</strong>'
            f'<span>{escape(group["description"])}</span></span>'
            f'<span class="home-group-toggle" aria-hidden="true"></span></summary>'
            f'<div class="home-group-body"><ul class="home-resource-links">{links}</ul>'
            f'<div class="home-category-links"><span>More guides</span>{categories}</div></div></details>'
        )

    return f'''<main class="home-main">
<section class="hero home-hero" aria-labelledby="home-title">
  <div class="wrap hero-wrap"><div class="hero-copy">
    <div class="eyebrow"><span class="dash"></span> THE UNOFFICIAL GTA VI FIELD GUIDE</div>
    <h1 id="home-title"><span class="home-title-game">GTA <em>6</em></span><span class="home-title-tagline">Own the streets.</span></h1>
    <p class="hero-text">Mission help, maps and practical guides.<br>Find your next move.</p>
    {search_markup}
    <p class="home-search-note"><span>Free. No account needed.</span><a href="#resources">Browse all resources <span aria-hidden="true">↓</span></a></p>
  </div></div>
  <div class="hero-art-credit">OFFICIAL GTA VI COVER ART &copy; ROCKSTAR GAMES</div>
</section>
<div class="wrap home-content">
  <section class="home-start" aria-labelledby="home-start-title">
    <h2 id="home-start-title">Start here</h2>
    <div class="home-shortcuts">{cards}</div>
  </section>
  <section class="home-resources" id="resources" aria-labelledby="resource-hub-title">
    <div class="home-section-heading"><div><h2 id="resource-hub-title">Browse all resources</h2><p>Open a topic to find its guides and tools.</p></div><a class="home-all-guides" href="/guides/">All {guide_count} guides <span aria-hidden="true">↗</span></a></div>
    <div class="home-directory" id="topics">{''.join(disclosures)}</div>
    <p class="home-editorial-note">Independent fan guide. Sources and review dates are listed in each guide. <a href="/editorial-policy/">How we check our content <span aria-hidden="true">↗</span></a></p>
  </section>
</div></main>'''

"""Generate the complete SEO-first GTASIX static website.
Run: python source/build.py. BASE_URL is optional for custom domains.
"""
from pathlib import Path
from html import escape as h
from datetime import datetime, timezone
import sys, os, json, re, shutil
from xml.sax.saxutils import escape as xh
BASE=Path(__file__).resolve().parent.parent
OUT=BASE/'site'
sys.path.insert(0,str(BASE/'source'))
from content import articles,categories,roadmap,videos,ROCKSTAR,PS5,RELEASE,STORE
from map_atlas import MAP_ITEMS,REGIONS,atlas_body,write_atlas_assets
from character_pages import views as character_views
from homepage import render_home
from seo_metadata import meta_for
from search_hubs import hub_views, hubs_index, llms_summary
from mission_helper import mission_views, mission_index
from updates_hub import update_views, updates_index
from seo_content import extra_sections
SITE_URL=os.environ.get('BASE_URL','https://www.gtasix.tech').rstrip('/')
UPDATED='2026-11-18'
CATS={k:(title,description,ic,num) for k,title,description,ic,num in categories}
URLS=[]
def icon(name,size=21):
    paths={
       'search':'<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/>',
       'arrow':'<path d="M5 12h14m-6-6 6 6-6 6"/>',
       'calendar-days':'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M7 3v4M17 3v4M3 10h18M7 14h3M14 14h3"/>',
       'hard-drive':'<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M6 13h.01M9 13h.01M3 10h18"/>',
       'wrench':'<path d="M14 7a5 5 0 0 1-6 6L3 18a2 2 0 0 0 3 3l5-5a5 5 0 0 0 6-6l-3 3-3-3z"/>',
       'gamepad-2':'<path d="M6 10H4c-1.5 0-3 1-3 4l1 5a2 2 0 0 0 3 1l4-3h6l4 3a2 2 0 0 0 3-1l1-5c0-3-1.5-4-3-4h-2zM8 10V6M16 10V6M5 14h6m-3-3v6M16 13h.01M19 15h.01"/>',
       'crosshair':'<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="2"/><path d="M12 2v4M12 18v4M2 12h4M18 12h4"/>',
       'map-pin':'<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/>',
       'trophy':'<path d="M7 3h10v8a5 5 0 0 1-10 0zM7 5H3v3a4 4 0 0 0 4 4M17 5h4v3a4 4 0 0 1-4 4M12 16v4M8 21h8"/>',
       'clapperboard':'<rect x="3" y="8" width="18" height="13" rx="2"/><path d="m3 8 1-5h17l-1 5M7 3l4 5M14 3l4 5M10 12l5 3-5 3z"/>',
       'play':'<path d="m8 5 11 7-11 7z"/>',
       'menu':'<path d="M3 6h18M3 12h18M3 18h18"/>',
       'shield':'<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/>',
       'check':'<path d="m4 12 5 5L20 6"/>',
       'clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l4 2"/>',
       'spark':'<path d="m12 2 2.5 7.5L22 12l-7.5 2.5L12 22l-2.5-7.5L2 12l7.5-2.5z"/>',
       'link':'<path d="M10 13a5 5 0 0 0 8 1l3-3a5 5 0 0 0-7-7l-2 2M14 11a5 5 0 0 0-8-1l-3 3a5 5 0 0 0 7 7l2-2"/>',
       'download':'<path d="M12 3v13m-5-5 5 5 5-5M4 18v3h16v-3"/>',
    }
    return f'<svg aria-hidden="true" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{paths.get(name,paths["spark"])}</svg>'

def uri(path): return SITE_URL+path

def write(path,text,index=True):
    path=path.strip('/')
    if not path or path.endswith('/'):
       full=OUT/path/'index.html'; url='/'+path
    elif path.endswith('.html') or '.' in path.rsplit('/',1)[-1]:
       full=OUT/path;url='/'+path
    else:
       full=OUT/path/'index.html';url='/'+path+'/'
    full.parent.mkdir(parents=True,exist_ok=True)
    full.write_text(text,encoding='utf8')
    if index and url.endswith('/'): URLS.append(url)
    return full

def brand():return f'<a href="/" class="brand" aria-label="GTASIX home"><span class="brand-icon"><b>6</b></span><span><span class="brand-word">GTA<em>SIX</em></span><span class="brand-sub">GTASIX.TECH / GTA VI FAN GUIDE</span></span></a>'

def header(active=''):
    nav=[('MISSION HELP','/gta-6-mission-help/','missions'),('GUIDES','/guides/','guides'),('GTA 6 MAP','/map/','map'),('SETTINGS','/guides/gta-6-best-settings/','settings'),('TOOLS','/tools/','tools'),('FIX GAME','/gta-6-help/','help')]
    links=''.join(f'<a href="{u}" class="nav-link {"active" if active==key else ""}">{n}</a>' for n,u,key in nav)
    return f'''<div class="topbar"><div class="wrap"><span class="tiny-pulse"></span><strong>YOUR GTA VI FIELD GUIDE</strong> Missions, maps &amp; practical fixes. <a href="/gta-6-mission-help/">Find your next step</a></div></div>
<header class="site-header"><div class="wrap header-grid">{brand()}<nav class="nav-links" id="nav-links" aria-label="Main navigation">{links}</nav><div class="header-actions"><a class="player-help-chip" href="/gta-6-mission-help/">{icon('gamepad-2',17)} <span>GET UNSTUCK</span></a><button id="mobile-menu" class="icon-btn mobile-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links">{icon('menu',22)}</button></div></div></header>'''

def footer(compact=False):
    if compact:
        return f'''<footer class="footer home-footer"><div class="wrap"><div class="home-footer-top">{brand()}<nav aria-label="About GTASIX"><a href="/about/">About</a><a href="/editorial-policy/">Editorial standards</a><a href="/privacy/">Privacy</a><a href="{ROCKSTAR}" target="_blank" rel="noopener noreferrer">Official GTA VI site <span class="home-link-arrow" aria-hidden="true">{icon("arrow",14)}</span></a></nav></div><div class="foot-bottom"><span>&copy; 2026 GTASIX. An independent fan guide, unaffiliated with Rockstar Games or Take-Two Interactive.</span></div></div></footer>'''
    return f'''<footer class="footer"><div class="wrap"><div class="footer-cols"><div>{brand()}<p>The unofficial GTA VI resource hub. Mission hints, practical checklists, source links and a community map, all in one place.</p></div><div><h4>Explore</h4><a href="/gta-6-mission-help/">Mission &amp; gameplay helper</a><a href="/guides/">All guides</a><a href="/gta-6-facts/">Confirmed GTA 6 facts</a><a href="/map/">Interactive GTA 6 map</a><a href="/characters/">GTA 6 characters</a><a href="/videos/">Official videos</a><a href="/buy/">Buy GTA 6</a><a href="/tools/">Free tools</a><a href="/gta-6-online/">GTA 6 Online status</a><a href="/gta-6-help/">Troubleshooting Help</a><a href="/categories/gameplay/">Gameplay</a></div><div><h4>Popular</h4><a href="/guides/gta-6-download-size-ps5-xbox/">Install size</a><a href="/guides/install-ps5-m2-ssd-step-by-step/">Install an SSD</a><a href="/guides/gta-6-preload-not-working/">Preload problems</a><a href="/guides/gta-6-editions-compared/">Editions compared</a></div><div><h4>About GTASIX</h4><a href="/about/">Our mission</a><a href="/editorial-policy/">Editorial standards</a><a href="/privacy/">Privacy</a><a href="{ROCKSTAR}" rel="noopener noreferrer" target="_blank">Official GTA VI site</a></div></div><div class="foot-bottom"><span>&copy; 2026 GTASIX. An independent fan guide, unaffiliated with Rockstar Games or Take-Two Interactive.</span><span>SOURCE LINKS &amp; REVIEW DATES IN EACH GUIDE</span></div></div></footer>'''

def page(title,desc,body,active='',path='/',ld=None,extra_head=''):
    # Readable, topic-specific metadata rather than artificially stuffing "GTA 6".
    title,desc=meta_for(path,title,desc,articles)
    og='/assets/og-cover.png'
    url=uri(path)
    is_article=any(isinstance(item,dict) and item.get('@type') in ('Article','NewsArticle') for item in (ld if isinstance(ld,list) else ([ld] if ld else [])))
    graph=[{'@context':'https://schema.org','@type':'WebPage','@id':url+'#webpage','url':url,'name':title,'description':desc,'inLanguage':'en-US','isPartOf':{'@id':SITE_URL+'/#website'},'about':{'@id':ROCKSTAR}}]
    if path=='/':
        graph += [
           {'@context':'https://schema.org','@type':'Organization','@id':SITE_URL+'/#organization','name':'GTASIX','url':SITE_URL,'description':'Independent, unofficial Grand Theft Auto VI guide and gaming resource website.'},
           {'@context':'https://schema.org','@type':'WebSite','@id':SITE_URL+'/#website','name':'GTASIX — GTA 6 Guides and Interactive Map','alternateName':'GTASIX.tech — independent GTA 6 guides','url':SITE_URL,'inLanguage':'en-US','publisher':{'@id':SITE_URL+'/#organization'}},
           {'@context':'https://schema.org','@type':'VideoGame','@id':ROCKSTAR,'name':'Grand Theft Auto VI','alternateName':'GTA 6','url':ROCKSTAR,'gamePlatform':['PlayStation 5','Xbox Series X|S'],'publisher':{'@type':'Organization','name':'Rockstar Games'}}
        ]
    for item in (ld if isinstance(ld,list) else ([ld] if ld else [])):
        if isinstance(item,dict):
            item=dict(item)
            item.setdefault('@context','https://schema.org')
            if item.get('@type')=='Article':
                item['@id']=url+'#article'
                item['publisher']={'@id':SITE_URL+'/#organization'}
                item['isAccessibleForFree']=True
                item['datePublished']=item.get('datePublished',UPDATED)
                item['dateModified']=item.get('dateModified',UPDATED)
                item['mainEntityOfPage']=url
            graph.append(item)
    js=json.dumps(graph,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')
    css='<meta name="theme-color" content="#11121d">'
    ogtype='article' if is_article else 'website'
    robots='noindex,follow' if path=='/404.html' else 'index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1'
    # /map/ alone needs the large interactive-map stylesheet.
    map_css='<link rel="stylesheet" href="/assets/map.css">' if path=='/map/' else ''
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><title>{h(title)}</title><meta name="description" content="{h(desc,quote=True)}"><meta name="robots" content="{robots}"><meta name="author" content="GTASIX Editorial"><link rel="canonical" href="{h(url,quote=True)}"><meta property="og:type" content="{ogtype}"><meta property="og:site_name" content="GTASIX"><meta property="og:title" content="{h(title,quote=True)}"><meta property="og:description" content="{h(desc,quote=True)}"><meta property="og:url" content="{h(url,quote=True)}"><meta property="og:image" content="{h(uri(og),quote=True)}"><meta property="og:image:alt" content="GTA 6 GTASIX resource hub — independent guides and Leonida map"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{h(title,quote=True)}"><meta name="twitter:description" content="{h(desc,quote=True)}"><meta name="twitter:image" content="{h(uri(og),quote=True)}"><link rel="icon" href="/assets/icon.svg" type="image/svg+xml"><link rel="manifest" href="/site.webmanifest"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>{css}<link rel="stylesheet" href="/assets/styles.css?v=20261120-gameplay">{map_css}{extra_head}<script type="application/ld+json">{js}</script><script defer src="/assets/app.js?v=20261120-gameplay"></script></head><body>{header(active)}{body}{footer(compact=path=='/')}</body></html>'''

def topic_card(c):
    slug,title,desc,ic,num=c
    return f'<a href="/categories/{slug}/" class="topic-card"><span class="topic-num">{num} / INTEL CATEGORY</span><span class="topic-arrow">↗</span><div class="topic-icon">{icon(ic)}</div><h3>{h(title)}</h3><p>{h(desc)}</p></a>'

def top_line(num,subtitle,title,note='',link=None):
    return f'''<div class="section-top"><div><div class="section-label">// {h(num)} &nbsp; {h(subtitle)}</div><h2 class="section-title">{h(title)}</h2>{'<p class="section-note">'+h(note)+'</p>' if note else ''}</div>{f'<a class="section-link" href="{link[1]}">{h(link[0])} &nbsp; {icon("arrow",15)}</a>' if link else ''}</div>'''

def feature_card(a,i=1):
    status=a['status']
    return f'''<a href="/guides/{a['slug']}/" class="feature-card"><div class="feature-art"><span class="art-type">{h(CATS[a['category']][0]).upper()}</span><span class="visual-num">{i:02}</span></div><div class="feature-body"><span class="tag {'confirmed' if status=='CONFIRMED' else 'planned'}">{status}</span><h3>{h(a['title'])}</h3><p>{h(a['summary'])}</p><div class="feature-foot"><span>{a['read']} MIN READ</span><span>READ GUIDE &nbsp; →</span></div></div></a>'''

def guide_card(a):
    status=a['status'];c=CATS[a['category']][0]
    ds=h(' '.join([a['title'],a['summary'],c,*a.get('aliases',[])]) ,quote=True)
    return f'''<a href="/guides/{a['slug']}/" class="guide-item" data-guide-card data-cat="{a['category']}" data-search="{ds.lower()}"><span class="tag {'confirmed' if status=='CONFIRMED' else 'planned'}">{h(status)}</span><h3>{h(a['title'])}</h3><p>{h(a['summary'])}</p><div class="guide-end"><span>{h(c.upper())} · {a['read']} MIN</span><b>EXPLORE →</b></div></a>'''

def bread(pairs):
    links=['<a href="/">HOME</a>']+[f'<a href="{u}">{h(t).upper()}</a>' for t,u in pairs[:-1]]
    return '<div class="crumb">'+'<span> / </span>'.join(links+[h(pairs[-1][0]).upper()])+'</div>'

def page_intro(title,desc,crumbs):
    return f'<section class="page-intro"><div class="wrap">{bread(crumbs)}<h1>{h(title)}</h1><p class="lead">{h(desc)}</p></div></section>'

def search_bar(hero=False):
    c='hero-search' if hero else 'page-search'
    return f'''<div class="search-area"><form id="search-form" action="/guides/" role="search" class="{c}">{icon('search')}<input class="site-search" name="q" type="search" placeholder="Try 'no mission marker', 'driving', 'save game'..." aria-label="Search guides" autocomplete="off"><button class="search-go" type="submit">SEARCH {icon('arrow',15)}</button></form><div class="search-results" role="region" aria-live="polite" aria-label="Search suggestions"></div></div>'''

def home():
    body=render_home(len(articles),search_bar(True),icon)
    ld=[{'@context':'https://schema.org','@type':'CollectionPage','name':'GTA VI resources, walkthroughs, troubleshooting and gameplay','url':SITE_URL,'about':{'@type':'VideoGame','name':'Grand Theft Auto VI','url':ROCKSTAR}}]
    write('',page('GTA 6 Guides, Interactive Map, Gameplay & Videos | GTASIX','Explore GTA 6 with an interactive Leonida map, walkthroughs, gameplay videos, release guide, PS5 and Xbox troubleshooting, storage tips and best places to buy.',body,'','/',ld,extra_head='<link rel="stylesheet" href="/assets/home.css?v=20261120-organized-2">'))


def facts_page():
    """A source-first, entity-focused reference page for web and AI retrieval."""
    path='/gta-6-facts/'
    desc='A current, source-checked breakdown of what Rockstar has confirmed about GTA VI, plus unknown details that should not be presented as facts.'
    facts=[
        ('Release date','Released November 19, 2026 for PlayStation 5 and Xbox Series X|S.','/guides/gta-6-release-date-and-time/'),
        ('Launch platforms','PlayStation 5 and Xbox Series X|S. No official PC release date or PC minimum specifications are announced.','/guides/gta-6-pc-release-system-requirements/'),
        ('Setting','The fictional state of Leonida includes Vice City, Leonida Keys, Grassrivers, Port Gellhorn, Ambrosia and Mount Kalaga.','/map/'),
        ('Playable leads','Rockstar introduces Jason Duval and Lucia Caminos as the central protagonists.','/characters/'),
        ('PS5 storage','PlayStation advises at least 212 GB of free space before installing GTA VI. Download sizes and Xbox storage are not necessarily identical.','/guides/gta-6-download-size-ps5-xbox/'),
        ('Editions','Rockstar offers Standard and Ultimate editions; confirm what extras are included in your country.','/guides/gta-6-editions-compared/'),
        ('Physical retail','Listings described as Code-in-Box contain a redeemable download code rather than a game disc.','/buy/'),
        ('Gameplay help','Use the mission helper for four sourced early mission hints and practical objective, driving and control checklists.','/gta-6-mission-help/')
    ]
    questions=[
      ('When is GTA 6 released?','Rockstar lists November 19, 2026 for the PS5 and Xbox Series X|S release.'),
      ('Will GTA 6 launch on PC?','A PC date and official PC specifications have not been announced in Rockstar’s published launch information.'),
      ('Who are the two central GTA 6 characters?','Jason Duval and Lucia Caminos.'),
      ('Is the GTASIX map the official GTA 6 map?','No. Rockstar offers an official printable Leonida map. The GTASIX interactive map is a community reconstruction; use in-game navigation for exact mission objectives.'),
      ('What storage space is needed on PS5?','PlayStation recommends freeing at least 212 GB on PS5. Actual file download size is not the same as the advised space target.')
    ]
    fact_html=''.join(f'<div class="fact-block"><span class="section-label">// {h(label.upper())}</span><p>{h(value)}</p><a href="{url}">SEE DETAILS &#8594;</a></div>' for label,value,url in facts)
    q_html=''.join(f'<details class="faq"><summary>{h(q)}</summary><p>{h(a)}</p></details>' for q,a in questions)
    source_html=''.join(f'<a href="{u}" target="_blank" rel="noopener noreferrer">{h(n)}</a>' for n,u in [('Rockstar launch announcement','https://www.rockstargames.com/newswire/article/39akk424a9oo53/grand-theft-auto-vi-now-available'),('Rockstar GTA VI',ROCKSTAR),('Rockstar preload FAQ','https://support.rockstargames.com/articles/7nPqOA2uCbpEQHXx7KVrYd/grand-theft-auto-vi-pre-load-faq'),('PlayStation GTA VI',PS5),('Rockstar game editions','https://support.rockstargames.com/articles/4QfG4FmZCf5W1gS8jy4UVT/grand-theft-auto-vi-platform-editions-and-versions')])
    body=page_intro('GTA 6: confirmed facts',desc,[('GTA 6 facts',path)])+f'''<main class="wrap info-page"><p class="lead">Launch and help resources updated <strong>November 20, 2026</strong>. Individual linked guides show their own review dates and distinguish official facts, editorial reporting and practical suggestions.</p><h2>What is confirmed about GTA VI?</h2><div class="facts-grid">{fact_html}</div><h2>What is still unknown?</h2><p><strong>The complete building-by-building map:</strong> Rockstar now offers an <a href="https://www.rockstargames.com/VI/media" target="_blank" rel="noopener noreferrer">official printable Leonida map</a>. Our interactive map remains a community reconstruction and does not establish exact objective positions or enterable interiors. <a href="/map/">Explore the labeled map</a>.</p><p><strong>PC specifications, cheat lists, vehicle speed rankings and a complete mission list:</strong> claims about these details require actual released-game evidence. We will not label untested rumors as confirmed.</p><h2>GTA 6 questions answered</h2><div class="faqs">{q_html}</div><h2>Original sources</h2><p>Read the source pages yourself. Rockstar defines the game's story and scope; platform guidance comes from the console makers. Do not substitute fan-made data for those disclosures.</p><div class="source-list">{source_html}</div><div class="note-box">GTASIX is an independent fan guide, not affiliated with or endorsed by Rockstar Games. For fast answers, start with our <a href="/guides/">guide library</a> or <a href="/characters/">character profiles</a>.</div></main>'''
    ld=[{'@context':'https://schema.org','@type':'FAQPage','@id':uri(path)+'#faq','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in questions]},
        {'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':SITE_URL+'/'},{'@type':'ListItem','position':2,'name':'GTA 6 facts','item':uri(path)}]}]
    write(path,page('GTA 6 Confirmed Facts | GTASIX',desc,body,'',path,ld))

def map_page():
    path='/map/'
    desc='Detailed interactive GTA 6 community map: zoom to buildings, streets and districts across Leonida. Search GTADB community landmarks, filter, and save private pins. Not the official in-game map.'
    ld=[{'@context':'https://schema.org','@type':'CollectionPage','name':'GTA 6 interactive Leonida map','description':desc,'url':uri(path),'about':{'@type':'VideoGame','name':'Grand Theft Auto VI','url':ROCKSTAR}},
        {'@context':'https://schema.org','@type':'ItemList','name':'Rockstar-named GTA 6 regions','itemListElement':[{'@type':'ListItem','position':i+1,'name':v[1],'url':f'https://www.rockstargames.com/VI/only-in-leonida/{"kalaga" if v[0]=="mount-kalaga" else v[0]}'} for i,v in enumerate(REGIONS)]}]
    safe_data=json.dumps(MAP_ITEMS,ensure_ascii=True,separators=(',',':')).replace('<','\\u003c')
    body=atlas_body()+'<script id="atlas-data" type="application/json">'+safe_data+'</script>'
    write(path,page('GTA 6 Detailed Map of Leonida, Streets & Buildings | GTASIX',desc,body,'map',path,ld,extra_head='<script defer src="/assets/map.js"></script>'))

def buy_page():
    path='/buy/'
    intro='Where to buy GTA VI for the lowest verified U.S. price, PS5 and Xbox listings, safe discounts and what the code-in-box format means.'
    sources=[('Rockstar official store','https://store.rockstargames.com/game/buy-gta-vi'),('PlayStation Store','https://store.playstation.com/en-us/product/EP1004-PPSA01547_00-GTAVISTANDARD001/'),('Microsoft Xbox Store','https://www.xbox.com/en-US/games/store/p/9P3H4968GRSM'),('Target Circle Card terms','https://www.target.com/c/target-circle-card-program-rules/-/N-4tgj0'),('Target promotional exclusions','https://www.target.com/help/article/000164337')]
    rows=[
      ('PlayStation Store','Digital','79.99','https://store.playstation.com/en-us/product/EP1004-PPSA01547_00-GTAVISTANDARD001/','https://www.xbox.com/en-US/games/store/p/9P3H4968GRSM','Instant digital entitlement; preload available'),
      ('Walmart','Code in box','79.99','https://www.walmart.com/ip/20482917228','https://www.walmart.com/ip/Grand-Theft-Auto-VI-Xbox-Series-X-Game/20459958275','Look for official retailer stock and shipping'),
      ('Target','Code in box','79.99','https://www.target.com/p/grand-theft-auto-vi-playstation-5/-/A-1011529119','https://www.target.com/p/-/A-1011545811','Circle Card 5% may apply; check checkout'),
      ('Best Buy','Code in box','79.99','https://www.bestbuy.com/product/grand-theft-auto-vi-code-in-box-ships-11-12-26-playable-11-19-26-playstation-5/6684968','https://www.bestbuy.com/product/grand-theft-auto-vi-code-in-box-playable-11-19-26-xbox-series-x-xbox-series-s/JXHY5RKPCY','Check delivery and pickup dates for your ZIP'),
      ('GameStop','Code in box','79.99','https://www.gamestop.com/video-games/playstation-5/products/grand-theft-auto-vi---playstation-5-code-in-box/448295.html','https://www.gamestop.com/video-games/xbox-series-x%7Cs/products/grand-theft-auto-vi---xbox-series-x-s-code-in-box/448297.html','Existing store credit or eligible trade-in can help'),
    ]
    cards=''.join(f'<div class="retailer-card" data-buy-row data-ps5-url="{h(ps,quote=True)}" data-xbox-url="{h(xb,quote=True)}"><div class="retailer-heading"><h3>{h(name)}</h3><span class="deal-type">{h(kind)}</span></div><div class="retailer-price"><strong>${h(price)}</strong><span>USD / STANDARD</span></div><p>{h(note)}</p><a class="retailer-link" target="_blank" rel="noopener noreferrer sponsored" href="{h(ps,quote=True)}">CHECK PRICE &amp; AVAILABILITY &rarr;</a></div>' for name,kind,price,ps,xb,note in rows)
    tips=[('01','Compare final checkout price','Taxes, shipping and retailer fulfillment can change the best total. Prices here are a manually verified snapshot, not a live feed.'),('02','Check an existing Target Circle Card','The 5% Card benefit may reduce eligible purchases from $79.99 to about $75.99 before tax. Some Grand Theft Auto software is excluded from general Target promotions. Confirm whether this item receives the separate Card discount at checkout.'),('03','Buy Standard, upgrade later if needed','Start with the base edition if you only need the full game. Do not pay more for Ultimate extras unless you value them.'),('04','Use store credit or legitimate trade-in','If you already hold earned rewards or have games to trade, compare the actual credit and any conditions. Do not buy gift cards just to chase a discount.'),('05','Choose digital for fastest access','A direct store download avoids delivery uncertainty. Code-in-box purchases still require redeeming and downloading; a shipping label is not a playable disc.'),('06','Skip gray-market account and region tricks','Avoid marketplace accounts, unusual region changes, fake “early access” keys and untrusted sellers; entitlement restrictions and revoked codes can cost more than any advertised savings.')]
    tip_html=''.join(f'<div class="savings-item"><span class="step-num">{num}</span><div><h3>{h(title)}</h3><p>{h(details)}</p></div></div>' for num,title,details in tips)
    schema={'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in [('What is the cheapest verified GTA 6 Standard Edition price in the US?','The mainstream U.S. retail prices checked November 18, 2026 were $79.99 before tax. Qualifying card and reward savings may reduce the final checkout price.'),('Do GTA 6 physical boxes contain a game disc?','No. Rockstar says the current physical version is a code-in-box release with a download code, not a playable disc.'),('Can I play early by buying a different region?','Rockstar lists unlock at midnight local time; avoid unverified region tricks and account-sharing offers.')]]}
    body=page_intro('GTA 6: where to buy it cheapest',intro,[('Buy / Deals',path)])+f'''<main class="wrap buy-page"><div class="deal-alert"><span class="tiny-pulse"></span><strong>U.S. PRICE CHECK &nbsp; / &nbsp; NOV 18, 2026</strong><p>Regular Standard Edition pricing at the trusted stores below is $79.99 before tax. This is NOT live pricing; follow each seller link to verify.</p></div><div class="buy-layout"><div><h2>COMPARE VERIFIED RETAILERS</h2><p class="helper">Choose your console. Store links change to match your platform.</p></div><div class="platform-switch" role="group" aria-label="Select game platform"><button type="button" class="selected" data-buy-platform="ps5" aria-pressed="true">PS5 / PS5 PRO</button><button type="button" data-buy-platform="xbox" aria-pressed="false">XBOX SERIES X|S</button></div></div><div class="retailer-grid">{cards}</div><div class="deal-warning"><strong>BEFORE YOU ORDER: IT'S A DOWNLOAD CODE.</strong><p>Physical retail “Code-in-Box” packages do not contain a game disc. Check the console region of the code and make sure your game account can redeem it. GTA VI is listed for PS5 and Xbox Series X|S, not PC at launch.</p><a href="{STORE}" target="_blank" rel="noopener noreferrer">VERIFY AT ROCKSTAR &rarr;</a></div><section class="section" id="savings">{top_line('01','SAVINGS PLAYBOOK','Legit ways to spend less','No suspicious promo codes, VPN region tricks or account resellers.')}<div class="savings-grid">{tip_html}</div></section><section class="section">{top_line('02','BUYER ANSWERS','Questions before checkout','Current U.S. store listings should be rechecked before purchasing.')}<div class="faqs"><details class="faq"><summary>What is the cheapest price?</summary><p>At the trusted mainstream stores reviewed on November 18, the standard price is $79.99 before tax. Check all carts for actual discounts, shipping and availability. We cannot guarantee a lowest price across every seller.</p></details><details class="faq"><summary>Does the boxed version have a disc?</summary><p>No. Rockstar's current physical edition is a code-in-box release that requires downloading the game.</p></details><details class="faq"><summary>Is Target Circle Card 5% guaranteed?</summary><p>No. The Card discount applies to eligible purchases and Target excludes GTA software from some separate promotions. The checkout total controls; do not assume it will work.</p></details><details class="faq"><summary>Can I buy the Ultimate upgrade later?</summary><p>Rockstar lists an Ultimate Edition upgrade from the Standard Edition through participating digital storefronts.</p></details></div></section><div class="note-box"><strong>EDITORIAL DISCLOSURE.</strong> These are independent, manually checked listings, not automated live offers. Retail availability, coupons, region and tax vary. This website is not affiliated with Rockstar or retailers. Links go to store pages. <a href="/editorial-policy/">How we verify information &rarr;</a></div><div class="source-list">{''.join(f'<a href="{h(u,quote=True)}" rel="noopener noreferrer" target="_blank">{h(n)}</a>' for n,u in sources)}</div></main>'''
    write(path,page('Where to Buy GTA 6 Cheapest: PS5 & Xbox Prices, Deals | GTASIX',intro,body,'buy',path,schema))

def listing(category=None):
    if category:
        title,desc,_,_=CATS[category];arr=[a for a in articles if a['category']==category];head=f'{title}: GTA VI Guides';intro=f'{desc} {len(arr)} source-linked guides and practical resources.';p=f'/categories/{category}/'
    else:
        title='All';arr=list(articles);head='The GTA VI Guide Library';intro=f'Search {len(arr)} practical guides, tutorials and answers. Official information, attributed reporting and editorial advice are clearly labeled.';p='/guides/'
    navs='<div class="filter-list"><button class="tab selected" data-filter="all">ALL</button>'+''.join(f'<button class="tab" data-filter="{k}">{h(t)}</button>' for k,t,_,_,_ in categories)+'</div>'
    feature_order=["gta-6-update-1-002-002-patch-notes","gta-6-autosave-not-working-lost-progress","gta-6-phone-call-not-triggering-next-mission","gta-6-wanted-level-stuck-how-to-lose-police","gta-6-bag-handover-fence-not-working","gta-6-safe-codes-keypad-combinations","gta-6-best-aim-assist-settings","gta-6-chapter-1-missables-tourist-trap","gta-6-fast-travel-taxi-bus-train","gta-6-how-long-to-beat-story-100-percent"]+["gta-6-missions-walkthroughs","gta-6-no-mission-marker-what-to-do","gta-6-map-vs-vice-city","gta-6-driving-tips-and-physics","gta-6-crashing-freezing-ps5-xbox","gta-6-stuck-loading-screen-black-screen","gta-6-game-locked-wont-start","gta-6-blurry-graphics-fps","gta-6-audio-controller-problems"]+['gta-6-how-to-save','gta-6-how-to-switch-characters','gta-6-cheat-codes','gta-6-jason-lucia-voice-actors','gta-6-reviews-scores','gta-6-best-settings']
    arr.sort(key=lambda a: feature_order.index(a['slug']) if a['slug'] in feature_order else 999)
    body=page_intro(head,intro,[(title,p)])+f'''<main class="wrap"><div class="gameplay-entry"><div><strong>Stuck on an objective?</strong><p>Get mission hints and a checklist for what to try next.</p></div><a class="btn" href="/gta-6-mission-help/">OPEN MISSION HELPER</a><a href="/gta-6-help/">Technical fixes</a></div><div class="list-controls"><div>{navs}<div class="guide-filter-note"><span id="guide-count">{len(arr)} guides</span> &nbsp; / &nbsp; UPDATED 24 NOV 2026</div></div><div class="search-box-mini">{icon('search',18)} <input id="guide-list-search" type="search" aria-label="Filter guides" placeholder="Filter guides..." /></div></div><div class="guides-grid" id="guide-list">{''.join(guide_card(a) for a in arr)}</div><div id="guide-empty" class="empty-state hidden">No guides match those filters. <a href="/gta-6-mission-help/">Try the mission helper</a>, or choose a different search or category.</div><div class="trust-strip"><strong>Never trust unverified game tricks.</strong><span>VERIFICATION STATUS ON EVERY ARTICLE</span><span>OFFICIAL SOURCES LINKED</span></div></main>'''
    # HTML data filters need correct page-specific count: for category, keep a category-only active filter (JS list if filter different -> 0); hide filters on category page instead.
    if category:
       start=body.find('<div class="filter-list">');end=body.find('</div>',start)
       if start>=0:body=body[:start]+'<div class="filter-list"><a class="tab selected" href="/guides/">SEE ALL CATEGORIES</a></div>'+body[end+6:]
    write(p,page(f'{head} | GTASIX',intro,body,'guides',p))

def article_page(a):
    ct=CATS[a['category']][0]
    p=f"/guides/{a['slug']}/"
    related=[b for b in articles if b['category']==a['category'] and b['slug']!=a['slug']][:3]
    if len(related)<3:related+=( [b for b in articles if b['slug']!=a['slug'] and b not in related][:3-len(related)] )
    source_html=''.join(f'<a target="_blank" rel="noopener noreferrer" href="{h(link,quote=True)}">{h(re.sub(r"^www\\.","",link.split("/")[2]))} / source</a>' for link in dict.fromkeys(a['sources']))
    status=a['status'];stcl='orange' if status!='CONFIRMED' else ''
    supplement=extra_sections(a['slug'])
    if a['slug']=='gta-6-best-settings':
        supplement=(BASE/'source'/'settings-widget.html').read_text(encoding='utf8')+supplement
    warning='' if status=='CONFIRMED' else (f'<div class="note-box"><strong>ATTRIBUTED REPORTING.</strong> This guide summarizes third-party sources; GTASIX has not independently tested each input or game setting. Consult the originals for updates.</div>' if a['slug'] in ('gta-6-cheat-codes','gta-6-how-to-save','gta-6-how-to-switch-characters','gta-6-reviews-scores') else f'<div class="note-box"><strong>VERIFICATION NOTE.</strong> This guide contains preparation or details not independently tested by GTASIX.</div>')
    if a['slug'] in ["gta-6-crashing-freezing-ps5-xbox","gta-6-stuck-loading-screen-black-screen","gta-6-game-locked-wont-start","gta-6-blurry-graphics-fps","gta-6-audio-controller-problems"]:
        warning='<div class="note-box"><strong>SAFE TROUBLESHOOTING.</strong> Official manufacturer steps are separated from community-reported symptoms. These checks are not a guaranteed fix.</div>'
    steps=''.join(f'<div class="step"><span class="step-num">{i:02}</span><p>{h(v)}</p></div>' for i,v in enumerate(a['steps'],1))
    faqs=''.join(f'<details class="faq"><summary>{h(q)}</summary><p>{h(answer)}</p></details>' for q,answer in a['faqs'])
    side=''.join(f'<a href="/guides/{r["slug"]}/">{h(r["title"])}</a>' for r in related)
    breadcrumb=[('Guides','/guides/'),(ct,f'/categories/{a["category"]}/'),(a['title'],p)]
    updated_label='NOV 20, 2026' if a['slug'] in ["gta-6-crashing-freezing-ps5-xbox","gta-6-stuck-loading-screen-black-screen","gta-6-game-locked-wont-start","gta-6-blurry-graphics-fps","gta-6-audio-controller-problems"] else ('NOV 19, 2026' if a['slug'] in ["gta-6-how-to-save","gta-6-how-to-switch-characters","gta-6-jason-lucia-voice-actors","gta-6-reviews-scores","gta-6-cheat-codes","gta-6-release-date-and-time","gta-6-best-settings"] else 'NOV 18, 2026')
    article_date='2026-11-20' if a['slug'] in ["gta-6-crashing-freezing-ps5-xbox","gta-6-stuck-loading-screen-black-screen","gta-6-game-locked-wont-start","gta-6-blurry-graphics-fps","gta-6-audio-controller-problems"] else ('2026-11-19' if a['slug'] in ["gta-6-how-to-save","gta-6-how-to-switch-characters","gta-6-jason-lucia-voice-actors","gta-6-reviews-scores","gta-6-cheat-codes","gta-6-release-date-and-time","gta-6-best-settings"] else UPDATED)
    if a.get('updated'):
        article_date=a['updated']
        updated_label=datetime.strptime(article_date,'%Y-%m-%d').strftime('%b %d, %Y').upper()
    body=page_intro(a['title'],a['summary'],breadcrumb)+f'''<main class="wrap detail-grid"><article class="article-main"><div class="caption-row"><span class="status-chip {stcl}">{icon('shield',15)} {h(status)}</span> <span>UPDATED {updated_label}</span><span>{a['read']} MIN READ</span></div><div class="answer-box"><div class="eyebrow">{icon('spark',16)} QUICK ANSWER</div><p>{h(a['answer'])}</p></div>{supplement}{warning}<h2>Step-by-step guide</h2><div class="steps">{steps}</div><h2>Frequently asked questions</h2><div class="faqs">{faqs}</div><h2>Sources & verification</h2><p>These sources are the basis for the factual claims above. Platform menu labels can change after software updates; confirm on the console if a step differs.</p><div class="source-list">{source_html}</div><div class="note-box">Independent fan resource. No affiliation with Rockstar Games. If official guidance changes after launch, the official source takes precedence.</div><button type="button" class="btn btn-outline copy-link">{icon('link',16)} COPY LINK</button><h2>Read next</h2><div class="related">{''.join(f'<a href="/guides/{b["slug"]}/">{h(b["title"])}</a>' for b in related[:2])}</div></article><aside class="detail-aside"><div class="aside-block"><span class="section-label">// THE QUICK BRIEF</span><h3>At a glance</h3><p class="mini-summary">{h(a['summary'])}</p><hr><span class="status-chip {stcl}">{icon('shield',15)} {h(status)}</span><p class="mini-summary">Reviewed: {updated_label}<br>Reading time: {a['read']} minutes</p><h3>Related intel</h3>{side}<a href="/gta-6-facts/">CONFIRMED GTA 6 FACTS →</a><a href="/guides/">VIEW ALL GUIDES →</a></div></aside></main>'''
    b=[{'@type':'ListItem','position':1,'name':'Home','item':SITE_URL},{'@type':'ListItem','position':2,'name':'Guides','item':uri('/guides/')},{'@type':'ListItem','position':3,'name':a['title'],'item':uri(p)}]
    ld=[{'@context':'https://schema.org','@type':'Article','headline':a['title'],'description':a['summary'],'datePublished':article_date,'dateModified':article_date,'inLanguage':'en-US','author':{'@type':'Organization','name':'GTASIX Editorial'},'publisher':{'@type':'Organization','name':'GTASIX'},'mainEntityOfPage':uri(p),'citation':a['sources'],'about':{'@type':'VideoGame','name':'Grand Theft Auto VI'}},{'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':b},{'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':answer}} for q,answer in a['faqs']]}]
    extra='<link rel="stylesheet" href="/assets/settings.css"><script defer src="/assets/settings.js"></script>' if a['slug']=='gta-6-best-settings' else ''
    write(p,page(f'{a["title"]} | GTASIX GTA VI',a['summary'],body,'settings' if a['slug']=='gta-6-best-settings' else 'guides',p,ld,extra_head=extra))

def videos_page():
    cards=[]
    for v in videos:
        pic=f'<img src="{h(v["image"],quote=True)}" loading="lazy" alt="Official video thumbnail: {h(v["title"],quote=True)}" />' if v.get('image') else '<span class="play-ring">'+icon('play',28)+'</span>'
        cards.append(f'''<a class="video-card" href="{h(v['link'],quote=True)}" target="_blank" rel="noopener noreferrer"><div class="video-thumb">{pic}</div><div class="video-text"><span class="tag confirmed">{h(v['kind'])}</span><h3>{h(v['title'])}</h3><p>{h(v['sub'])}</p><div class="video-foot"><span>{h(v['date'])}</span><span>ROCKSTAR GAMES ↗</span></div></div></a>''')
    path='/videos/';intro='Every official GTA VI trailer, pre-load video and the extended gameplay presentation. Verified Rockstar sources only.'
    body=page_intro('Official GTA 6 videos',intro,[('Videos',path)])+f'''<main class="wrap"><div class="watch-grid">{''.join(cards)}</div><div class="note-box">All videos are linked to Rockstar's official website or verified Rockstar YouTube uploads. Fan edits, non-official leak clips and speculative thumbnails are intentionally excluded. <a href="https://www.rockstargames.com/VI/media/videos" target="_blank" rel="noopener noreferrer">Open official media library ↗</a>.</div></main>'''
    ld={'@context':'https://schema.org','@type':'CollectionPage','name':'Official Grand Theft Auto VI videos','description':intro,'url':uri(path)}
    write(path,page('Official GTA 6 Trailers, Gameplay & Videos | GTASIX',intro,body,'videos',path,ld))

def tools_page():
    path='/tools/';intro='Get mission help, tune your settings, check storage, estimate downloads and keep a personal checklist without making an account.'
    checks=['Game purchased or download code redeemed','Correct PS5 / PS5 Pro / Xbox Series X|S ready','Enough storage cleared (up to 212 GB)','Game installed and updates checked','System software and controller updated','Account sign-in and network working','Mission helper and save guide bookmarked']
    body=page_intro('Free GTA 6 player tools',intro,[('Tools',path)])+f'''<main class="wrap"><div class="gameplay-entry"><div><strong>Need help while playing?</strong><p>Build a mission checklist, find comfortable settings or troubleshoot your console.</p></div><a class="btn" href="/gta-6-mission-help/">MISSION HELPER</a><a href="/guides/gta-6-best-settings/">Settings finder</a><a href="/gta-6-help/">Technical help</a></div><div class="tools-grid"><section class="tool-box" id="storage"><div class="eyebrow">{icon('hard-drive')} STORAGE ANALYZER // 01</div><h2>Will GTA VI fit?</h2><p class="helper">PlayStation and Rockstar advise up to 212 GB. Xbox actual installed size can differ by device.</p><label for="storage-platform">YOUR CONSOLE</label><select id="storage-platform"><option value="ps5">PlayStation 5 / PS5 Pro</option><option value="xbox">Xbox Series X|S</option></select><div class="tool-split"><div><label for="storage-free">FREE SPACE (GB)</label><input id="storage-free" type="number" min="0" max="5000" value="100" inputmode="decimal"></div><div class="hidden" id="xbox-needed"><label for="storage-target">XBOX INSTALL SIZE (GB)</label><input id="storage-target" type="number" min="1" max="5000" value="212" inputmode="decimal"></div></div><button class="btn" id="storage-check" type="button">CALCULATE SPACE {icon('arrow',16)}</button><div class="result-panel" id="storage-result" role="status" aria-live="polite"><strong>CHECKING...</strong><p>Calculate how much more space is needed.</p></div><p class="helper">Verify the Xbox size in its own download queue. <a href="/guides/gta-6-download-size-ps5-xbox/">Read the official storage explainer →</a></p></section>
<section class="tool-box" id="download"><div class="eyebrow">{icon('clock')} DOWNLOAD TIMER // 02</div><h2>When will it finish?</h2><p class="helper">Estimated download time; connection and server throughput may change the result.</p><div class="tool-split"><div><label for="download-size">DOWNLOAD SIZE (GB)</label><input id="download-size" type="number" min="1" value="212" inputmode="decimal"></div><div><label for="download-speed">INTERNET SPEED (MBPS)</label><input id="download-speed" type="number" min="1" value="100" inputmode="decimal"></div></div><button class="btn" id="download-check" type="button">ESTIMATE TIME {icon('arrow',16)}</button><div class="result-panel" id="download-result" role="status" aria-live="polite"><strong>CHECKING...</strong><p>Estimate your download window.</p></div><p class="helper">Math uses decimal GB and Mb/s. Actual transfer rates may vary.</p></section>
<section class="tool-box" id="checklist"><div class="eyebrow">{icon('check')} READY STATUS // 03</div><h2>Ready-to-play checklist</h2><p class="helper">Tap each item as you prepare. Progress is saved on this device only.</p><div id="launch-checklist" class="checklist">{''.join(f'<label class="check-item"><input type="checkbox"><span>{h(item)}</span></label>' for item in checks)}</div><div class="result-panel"><strong id="check-progress">0 / 7 READY</strong><p>Your setup progress, saved on this device.</p></div></section>
<section class="tool-box"><div class="eyebrow">{icon('shield')} OFFICIAL SOURCE DESK // 04</div><h2>Need a verified answer?</h2><p class="helper">Start with the first-party sources. This hub turns them into plain-English instructions without inventing details.</p><div class="source-list"><a href="{ROCKSTAR}" target="_blank" rel="noopener noreferrer">Rockstar Games / GTA VI</a><a href="{PS5}" target="_blank" rel="noopener noreferrer">PlayStation / GTA VI</a><a href="{RELEASE}" target="_blank" rel="noopener noreferrer">Rockstar / regional launch times</a><a href="/guides/">GTASIX / all guides</a></div><div class="note-box">Have a specific error? Search its exact message in the guide library. No fake drivers or download patches.</div><a href="/guides/" class="btn btn-outline">SEARCH TROUBLESHOOTING {icon('arrow',16)}</a></section></div></main>'''
    write(path,page('Free GTA 6 Player Tools & Calculators | GTASIX',intro,body,'tools',path))

def informational():
    policy='''<h2>How we check information</h2><p>Our first choice is Rockstar Games and Rockstar Support, followed by official PlayStation and Xbox documentation. We link sources inside each guide so you can check the same information directly.</p><h2>What CONFIRMED means</h2><p>A claim is supported by an official source as of the visible review date. That does not mean game-mechanics instructions have been independently tested in a pre-release build. "VERIFY AT LAUNCH" means the guide describes safe preparation, a verification framework or a future workflow, not claimed discoveries.</p><h2>How we handle rumors</h2><p>We do not invent cheat codes, locations, missions, PC requirements, FPS targets, collectible coordinates or gameplay footage for search traffic. Confirmed and unconfirmed material stays clearly separated. We favor helpful pages over hundreds of nearly identical keyword pages.</p><h2>Corrections and updates</h2><p>Dates, store policies and hardware guidance can change. Consult the linked official sources for the latest. Each page shows its own review date. Mission hints name the published walkthrough they summarize; editorial checklists are practical suggestions, not claims of independent gameplay testing.</p>'''
    write('/editorial-policy/',page('Editorial Policy & Fact Checking | GTASIX','How GTASIX fact-checks GTA VI information, treats rumors, links to official sources, and labels unverified walkthrough information.',page_intro('Editorial standards','Verified first, speculation clearly marked.',[('Editorial policy','/editorial-policy/')])+f'<main class="wrap info-page">{policy}</main>','', '/editorial-policy/'))
    about='''<h2>What is GTASIX?</h2><p>GTASIX is a free, independent resource library dedicated to Grand Theft Auto VI. Its goal is simple: when a player searches for a GTA 6 question, a useful answer should be easy to find, easy to follow, and supported by evidence.</p><h2>What you will find</h2><p>Mission hints, gameplay checklists, navigation and driving advice, technical fixes, settings, official footage and a community-reconstructed Leonida map. Start with the <a href="/gta-6-mission-help/">mission helper</a>, search the <a href="/guides/">guide library</a>, or save places on the <a href="/map/">interactive map</a>.</p><h2>Independent fan project</h2><p>GTASIX is not owned, endorsed or sponsored by Rockstar Games, Take-Two Interactive, PlayStation, Sony or Microsoft. Names and marks belong to their respective owners. All official video links send you to the original publisher.</p><h2>What the labels mean</h2><p>Each guide identifies official information, attributed hands-on reporting or editorial guidance. Some older preparation resources still require gameplay verification; their labels are not a claim of tested walkthrough coverage. The mission helper currently covers four early missions and offers general next-step checklists.</p>'''
    write('/about/',page('About GTASIX — A GTA VI Fan Resource Hub','GTASIX mission, first-party verification approach and what this unofficial GTA VI gaming resource includes.',page_intro('Built for GTA VI players','Useful next steps, clear sources and free player tools.',[('About','/about/')])+f'<main class="wrap info-page">{about}</main>','', '/about/'))
    privacy='''<h2>Data on this website</h2><p>You do not need an account or login to browse. Guide search is performed locally in your browser using a public search index; your checklist, map bookmarks and private pins are stored in your own browser localStorage and are not transmitted to this website. The mission helper processes optional objective text in the page and never stores it or includes it in copied checklists or shared URLs. Save plan stores only your selected options and completed checks on this device. A shared helper link contains only preset options.</p><h2>Third-party services</h2><p>Google Fonts and official video thumbnails may be requested from their respective providers. Opening an external YouTube, Rockstar, PlayStation or Xbox page is subject to that site's privacy policy.</p><h2>Infrastructure analytics</h2><p>The hosting provider may process normal web requests and operational logs for security and delivery. No advertising trackers or newsletter data collection are bundled into this initial release.</p><h2>Control and deletion</h2><p>Use Clear saved plan in the mission helper to remove that plan. Clear site data in your browser to remove all saved checklists and map items. No personal profile is required to use these tools.</p>'''
    write('/privacy/',page('Privacy Policy | GTASIX','GTASIX privacy: no account required, local search, device-only mission plans and checklists, with clear controls for saved information.',page_intro('Privacy','No account, no ad tracking, no surprises.',[('Privacy','/privacy/')])+f'<main class="wrap info-page">{privacy}</main>','', '/privacy/'))

def machine_files():
    idx=[{'slug':a['slug'],'href':'/guides/'+a['slug']+'/', 'title':a['title'],'summary':a['summary'],'category':CATS[a['category']][0], 'aliases':a['aliases'],'status':a['status']} for a in articles]
    from characters import CHARACTERS
    idx.extend(hubs_index())
    idx.extend(mission_index())
    idx.append(updates_index())
    idx.extend({'slug':c['slug'],'href':'/characters/'+c['slug']+'/', 'title':c['name']+' - GTA 6 Character','summary':c['intro'],'category':'Characters', 'aliases':[c['name'],c['region'],c['role'],'GTA VI cast','GTA 6 '+c['name']], 'status':'CONFIRMED'} for c in CHARACTERS)
    (OUT/'llms.txt').write_text(llms_summary(SITE_URL)+'\n## Gameplay help\n- [Mission and gameplay helper]('+SITE_URL+'/gta-6-mission-help/): spoiler-controlled early mission hints, practical checklists and device-local saved plans.\n- [No mission marker]('+SITE_URL+'/guides/gta-6-no-mission-marker-what-to-do/): objective and navigation checks.\n- [Vice City comparison]('+SITE_URL+'/guides/gta-6-map-vs-vice-city/): original city, Leonida and honest map comparisons.\n- [Driving tips]('+SITE_URL+'/guides/gta-6-driving-tips-and-physics/): control paths and practical driving guidance.\n',encoding='utf8')
    with (OUT/'llms.txt').open('a',encoding='utf8') as _summary:
        _summary.write('\n## November 24 GTA VI search answers\n')
        _summary.write('- Rockstar November 23 update checker: '+SITE_URL+'/gta-6-updates/\n')
        for _item in articles:
            if _item.get('updated')=='2026-11-24':
                _summary.write('- '+_item['title']+': '+SITE_URL+'/guides/'+_item['slug']+'/\n')
    (OUT/'assets'/'search-index.json').write_text(json.dumps(idx,ensure_ascii=False,separators=(',',':')),encoding='utf8')
    (OUT/'robots.txt').write_text('User-agent: *\nAllow: /\n\nUser-agent: OAI-SearchBot\nAllow: /\n\nUser-agent: Googlebot\nAllow: /\n\nUser-agent: Bingbot\nAllow: /\n\nUser-agent: PerplexityBot\nAllow: /\n\nUser-agent: Claude-SearchBot\nAllow: /\n\nUser-agent: Claude-User\nAllow: /\n\nSitemap: '+SITE_URL+'/sitemap.xml\n',encoding='utf8')
    sm='<?xml version="1.0" encoding="utf-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+xh(uri(p))+'</loc><lastmod>'+('2026-11-24' if p in ["/","/guides/","/categories/troubleshooting/","/categories/gameplay/","/categories/collectibles/","/categories/media/","/gta-6-updates/","/guides/gta-6-update-1-002-002-patch-notes/","/guides/gta-6-autosave-not-working-lost-progress/","/guides/gta-6-phone-call-not-triggering-next-mission/","/guides/gta-6-wanted-level-stuck-how-to-lose-police/","/guides/gta-6-bag-handover-fence-not-working/","/guides/gta-6-safe-codes-keypad-combinations/","/guides/gta-6-best-aim-assist-settings/","/guides/gta-6-chapter-1-missables-tourist-trap/","/guides/gta-6-fast-travel-taxi-bus-train/","/guides/gta-6-how-long-to-beat-story-100-percent/"] else ('2026-11-20' if p in ["/gta-6-mission-help/","/guides/gta-6-map-vs-vice-city/","/guides/gta-6-driving-tips-and-physics/","/guides/gta-6-no-mission-marker-what-to-do/","/guides/gta-6-missions-walkthroughs/","/guides/gta-6-beginner-driving-tips/","/guides/gta-6-beginner-preparation-guide/","/categories/gameplay/","/categories/world/","/tools/","/about/","/privacy/","/editorial-policy/","/gta-6-facts/","/","/guides/","/categories/troubleshooting/","/guides/gta-6-crashing-freezing-ps5-xbox/","/guides/gta-6-stuck-loading-screen-black-screen/","/guides/gta-6-game-locked-wont-start/","/guides/gta-6-blurry-graphics-fps/","/guides/gta-6-audio-controller-problems/","/gta-6-online/","/gta-6-help/"] else ('2026-11-19' if p in ["/","/guides/","/categories/gameplay/","/categories/world/","/categories/media/","/categories/collectibles/","/categories/launch/","/guides/gta-6-how-to-save/","/guides/gta-6-how-to-switch-characters/","/guides/gta-6-jason-lucia-voice-actors/","/guides/gta-6-reviews-scores/","/guides/gta-6-cheat-codes/","/guides/gta-6-release-date-and-time/","/guides/gta-6-best-settings/"] else UPDATED)))+'</lastmod></url>' for p in URLS)+'</urlset>'
    (OUT/'sitemap.xml').write_text(sm,encoding='utf8')
    write('404.html',page('Guide not found | GTASIX','The resource you requested could not be found.',page_intro('Wrong exit.','This guide is not available yet. Try the GTA VI library instead.',[('404','/guides/')])+'<main class="wrap info-page"><a href="/guides/" class="btn">SEARCH ALL GUIDES →</a></main>','', '/404.html'),False)

if __name__=='__main__':
    write_atlas_assets(OUT)
    home();facts_page();map_page();listing()
    for c,*_ in categories: listing(c)
    for a in articles:article_page(a)
    for url,title,desc,body,ld,extra in character_views(SITE_URL):
        write(url,page(title,desc,body,'characters',url,ld,extra_head=extra))
    for url,title,desc,body,ld,extra in hub_views(SITE_URL):
        write(url,page(title,desc,body,'help' if url=='/gta-6-help/' else 'guides',url,ld,extra_head=extra))
    for url,title,desc,body,ld,extra in update_views(SITE_URL):
        write(url,page(title,desc,body,'guides',url,ld,extra_head=extra))
    for url,title,desc,body,ld,extra in mission_views(SITE_URL):
        write(url,page(title,desc,body,'missions',url,ld,extra_head=extra))
    videos_page();tools_page();buy_page();informational();machine_files()
    print(f'Generated {len(URLS)} indexed pages; {len(articles)} articles; site {SITE_URL}')

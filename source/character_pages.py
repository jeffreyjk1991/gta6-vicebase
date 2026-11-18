"""Original ViceBase character pages with official-source attribution."""
from html import escape as h
import json
from characters import CHARACTERS, BY_SLUG, SOURCE, DUO

def card(c, index, compact=False):
    title=h(c['name']);intro=h(c['intro']);group=h(c['group_label']);theme=h(c['theme']);
    pos=h(c['position'],quote=True);img=h(c['image'],quote=True)
    search=h((c['name']+' '+c['intro']+' '+c['region']+' '+c['role']).lower(),quote=True)
    data=f' data-character-card data-character-group="{h(c["group"])}" data-character-search="{search}"' if not compact else ''
    return f'''<a class="cast-card cast-{theme}" href="/characters/{c['slug']}/"{data}>
      <div class="cast-art"><img src="{img}" loading="lazy" decoding="async" style="object-position:{pos}" alt="{title}: official GTA VI promotional artwork by Rockstar Games"><span class="cast-id">FILE {index:02}</span><span class="cast-official">ROCKSTAR PROFILE</span></div>
      <div class="cast-copy"><span class="cast-role">{group}</span><h3>{title}</h3><p>{intro}</p><span class="cast-open">VIEW CHARACTER FILE <b aria-hidden="true">&#8599;</b></span></div>
    </a>'''

def home_teaser():
    pics=''.join(card(c,i,True) for i,c in enumerate(CHARACTERS[:4],1))
    return f'''<section class="section" id="people-of-leonida"><div class="section-top"><div><div class="section-label">// THE FACES OF LEONIDA</div><h2 class="section-title">GTA 6 CHARACTERS</h2><p class="section-note">Official Rockstar profiles, original bios and known connections. No invented story spoilers.</p></div><a href="/characters/" class="section-link">MEET THE ENTIRE CAST &nbsp; &#8594;</a></div><div class="cast-home-grid">{pics}</div></section>'''

def directory():
    path='/characters/'
    desc='Explore officially profiled GTA 6 characters: Jason Duval, Lucia Caminos, Cal Hampton, Boobie Ike, Dre\'Quan Priest, Real Dimez, Raul Bautista and Brian Heder. Bios, relationships and Rockstar artwork.'
    chips=''.join(f'<button type="button" class="cast-filter {"selected" if k=="all" else ""}" aria-pressed="{str(k=="all").lower()}" data-character-filter="{k}">{label}</button>' for k,label in [('all','ALL 8'),('lead','PROTAGONISTS'),('underworld','THE UNDERWORLD'),('music','MUSIC & NIGHTLIFE')])
    cards=''.join(card(c,i) for i,c in enumerate(CHARACTERS,1))
    hero=f'''<section class="cast-hero"><div class="wrap cast-hero-row"><div class="cast-hero-text"><div class="cast-eyebrow"><span class="tiny-pulse"></span> GTA 6 // CHARACTER DATABASE // VERIFIED FILES</div><h1>THE PEOPLE OF <em>LEONIDA.</em></h1><p>Meet Jason, Lucia and the characters shaping Rockstar's next crime story. Explore their backgrounds, who they know, and what is genuinely confirmed.</p><div class="cast-stats"><span><b>08</b> ROCKSTAR PROFILES</span><span><b>02</b> CENTRAL LEADS</span><span>STORY DETAILS <b>OFFICIAL ONLY</b></span></div><a class="cast-primary" href="#character-directory">EXPLORE THE CAST <span aria-hidden="true">&#8595;</span></a></div><div class="cast-hero-visual"><img src="{h(DUO,quote=True)}" alt="Official Rockstar GTA VI artwork depicting Lucia Caminos and Jason Duval" decoding="async"><span>OFFICIAL GTA VI ARTWORK &copy; ROCKSTAR GAMES</span></div></div></section>'''
    body=hero+f'''<main class="wrap cast-content" id="character-directory"><div class="cast-summary"><div><div class="section-label">// IDENTITY FILES</div><h2>MEET THE CAST.</h2><p>Everything below is based on Rockstar's published character profiles. Individual profiles link back to the original source.</p></div><div class="cast-verified"><span class="tiny-pulse"></span> FIRST-PARTY VERIFIED</div></div><div class="cast-toolbar"><div class="cast-filter-list" aria-label="Filter GTA 6 characters">{chips}</div><label class="cast-search"><span aria-hidden="true">&#8981;</span><input type="search" id="characters-search" placeholder="Search names, places, connections..." aria-label="Search character profiles"></label></div><div id="characters-count" class="cast-result-count" aria-live="polite">8 OF 8 CHARACTER FILES</div><div class="cast-grid">{cards}</div><p id="characters-empty" class="cast-empty" hidden>No characters match that search. Try a different name or filter.</p><aside class="cast-source-box"><div><strong>CONFIRMED, NOT RUMORED.</strong><p>These eight profiles are the main characters introduced on Rockstar's official GTA VI website. Other faces may appear in promotional footage, but we do not label them as officially profiled without direct supporting material. We do not invent voice actors, mission spoilers or character endings.</p></div><a href="{SOURCE}" target="_blank" rel="noopener noreferrer">VIEW ROCKSTAR CHARACTER PROFILES &#8599;</a></aside></main>'''
    ld=[{'@context':'https://schema.org','@type':'CollectionPage','name':'GTA VI characters and official profiles','url':'https://gta6-vicebase.vercel.app'+path,'about':{'@type':'VideoGame','name':'Grand Theft Auto VI'},'mainEntity':{'@type':'ItemList','itemListElement':[{'@type':'ListItem','position':i+1,'name':c['name'],'url':'https://gta6-vicebase.vercel.app/characters/'+c['slug']+'/'} for i,c in enumerate(CHARACTERS)]}}]
    extra='<link rel="stylesheet" href="/assets/characters.css"><script defer src="/assets/characters.js"></script>'
    return path,'GTA 6 Characters: Jason, Lucia & All Official Profiles | ViceBase',desc,body,ld,extra

def detail(c):
    path='/characters/'+c['slug']+'/'
    role=h(c['role']);name=h(c['name']);intro=h(c['intro']);theme=h(c['theme']);region=h(c['region']);
    img=h(c['image'],quote=True);pos=h(c['position'],quote=True)
    badges=''.join(f'<div class="cast-fact"><span>{h(k)}</span><strong>{h(v)}</strong></div>' for k,v in c['facts'])
    connection_html=''.join(f'<a class="cast-connection" href="/characters/{slug}/"><b>{h(BY_SLUG[slug]["name"])}</b><span>{h(BY_SLUG[slug]["group_label"])}</span><span aria-hidden="true">&#8599;</span></a>' for slug in c['connections']) or '<p>Rockstar has not published specific character connections for this profile yet.</p>'
    paras=''.join('<p>'+h(p)+'</p>' for p in c['paragraphs'])
    others=[x for x in CHARACTERS if x['slug']!=c['slug']][:3]
    related=''.join(card(other,CHARACTERS.index(other)+1,True) for other in others)
    is_lead=c['group']=='lead';playable='Rockstar has confirmed this character as one of the central leads.' if is_lead else 'Rockstar has not announced this character as a playable lead.'
    question=f'Is {c["name"]} playable in GTA 6?'
    faqs=[(f'Who is {c["name"]} in GTA 6?',c['intro']),(question,playable),(f'Who voices {c["name"]}?','Rockstar\'s published character profile does not list a confirmed performer. We do not treat rumor cast lists as official credits.')]
    faq_html=''.join(f'<details class="cast-faq"><summary>{h(q)}</summary><p>{h(a)}</p></details>' for q,a in faqs)
    schema=[{'@context':'https://schema.org','@type':'Article','headline':f'{c["name"]}: GTA 6 character profile, background and connections','description':c['intro'],'author':{'@type':'Organization','name':'ViceBase Editorial'},'about':{'@type':'VideoGame','name':'Grand Theft Auto VI'},'mainEntityOfPage':'https://gta6-vicebase.vercel.app'+path,'citation':SOURCE}, {'@context':'https://schema.org','@type':'FAQPage','mainEntity':[{'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}} for q,a in faqs]}]
    body=f'''<main class="cast-detail-wrap"><section class="wrap cast-file-breadcrumb"><a href="/">HOME</a><span>/</span><a href="/characters/">CHARACTERS</a><span>/</span>{name.upper()}</section><section class="wrap cast-detail-hero cast-{theme}"><div class="cast-file-copy"><span class="cast-eyebrow">GTA 6 // {h(c['group_label'])} // CHARACTER FILE</span><h1>{name}</h1><h2>{h(c['tagline'])}</h2><p>{intro}</p><div class="cast-file-tags"><span>ROCKSTAR CONFIRMED</span><span>{region.upper()}</span></div><a href="{SOURCE}" target="_blank" rel="noopener noreferrer" class="cast-primary">OFFICIAL ROCKSTAR PROFILE &#8599;</a></div><div class="cast-file-image"><img src="{img}" style="object-position:{pos}" alt="{h(c['image_label'])}" decoding="async"><span>ARTWORK &copy; ROCKSTAR GAMES</span></div></section><section class="wrap cast-file-layout"><article class="cast-file-main"><div class="section-label">// THE DOSSIER</div><h2>WHO IS {name.upper()}?</h2><div class="cast-story">{paras}</div><h2>CONFIRMED CONNECTIONS</h2><div class="cast-connections">{connection_html}</div><h2>WHAT ROCKSTAR HAS CONFIRMED</h2><p>{h(c['evidence'])}</p><h2>WHAT REMAINS UNKNOWN</h2><p>{h(c['unknown'])}</p><h2>QUICK QUESTIONS</h2><div class="cast-faqs">{faq_html}</div><div class="cast-source-callout"><strong>PRIMARY SOURCE</strong><p>Fact-checked against the official GTA VI character material, November 18, 2026. Profiles will be updated as new details can be verified.</p><a href="{SOURCE}" target="_blank" rel="noopener noreferrer">ROCKSTAR GAMES — ONLY IN LEONIDA &#8599;</a></div></article><aside class="cast-file-aside"><div class="cast-fact-sheet"><span class="section-label">// FILE DATA</span><h3>{name}</h3>{badges}<a href="/characters/">&#8592; BACK TO ALL CHARACTERS</a></div></aside></section><section class="wrap cast-file-more"><div class="section-label">// MORE FROM LEONIDA</div><h2>MEET THE REST.</h2><div class="cast-home-grid">{related}</div><a href="/characters/" class="cast-primary">ALL 8 OFFICIAL PROFILES &#8594;</a></section></main>'''
    extra='<link rel="stylesheet" href="/assets/characters.css">'
    return path, f'{c["name"]}: GTA 6 Character Profile & Relationships | ViceBase',f'{c["name"]} in GTA VI: {c["intro"]} Background, confirmed connections, official Rockstar artwork and spoiler-free answers.',body,schema,extra

def views():
    yield directory()
    for c in CHARACTERS: yield detail(c)

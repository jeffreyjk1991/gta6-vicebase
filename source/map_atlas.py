"""Independent GTA VI region atlas: editorial schematic, not official coordinates.

Generates an original SVG illustration and an accessible, browser-interactive map.
The six region names are supported by Rockstar's Only in Leonida pages.
Other pins are clearly labeled editorial exploration themes, not game locations.
"""
from pathlib import Path
from html import escape as h
from random import Random
import json

REGIONS = [
    ('vice-city','Vice City','Coastal metropolis','Rockstar-confirmed region','City lights, beachfront energy, nightlife and the heart of Leonida.',950,635,'city'),
    ('leonida-keys','Leonida Keys','Island chain','Rockstar-confirmed region','Water, bridges and island communities south of the mainland.',865,917,'coast'),
    ('grassrivers','Grassrivers','Wetlands','Rockstar-confirmed region','Swamp country, waterways and a very different side of Leonida.',578,712,'nature'),
    ('port-gellhorn','Port Gellhorn','Gulf coast','Rockstar-confirmed region','A faded Gulf-side town where waterfronts meet open roads.',425,440,'coast'),
    ('ambrosia','Ambrosia','Heartland','Rockstar-confirmed region','Agricultural and industrial heartland away from the bright coast.',660,411,'routes'),
    ('mount-kalaga','Mount Kalaga','Northern wilderness','Rockstar-confirmed region','National park and outdoor terrain in the north of Leonida.',735,194,'nature'),
]
BASE = 'https://www.rockstargames.com/VI/only-in-leonida/'
MAP_ITEMS = [
    dict(id=a, title=b, subtitle=c, fact=d, description=e, x=f, y=g, cat='region', region=a, source=BASE+('kalaga' if a=='mount-kalaga' else a), official=True)
    for a,b,c,d,e,f,g,category in REGIONS
]
EXPLORE = [
  ('oceanfront','Oceanfront views','vice-city','city',1110,677,'The big-city waterfront is a central visual theme. This is a suggested exploration area, not a mapped address.'),
  ('nightlife','Nightlife district','vice-city','city',891,566,'A planning pin for the urban nightlife atmosphere shown in GTA VI media. This is not a confirmed district boundary.'),
  ('downtown','Downtown skyline','vice-city','city',1028,550,'An approximate visual landmark for the city skyline. No street-level coordinates have been established here.'),
  ('marina','City marinas','vice-city','coast',1049,762,'Waterfront inspiration and boating routes. Symbolic placement only.'),
  ('bridges','Coastal causeways','vice-city','routes',991,794,'Explore roads crossing urban waterways when the full in-game map can be verified.'),
  ('keys-marina','Keys waterfront','leonida-keys','coast',947,918,'An editorial place to look for boats and waterfront scenery. Exact locations require launch-day checks.'),
  ('islands','Island-hopping','leonida-keys','coast',770,934,'The archipelago is confirmed; this island-hopping point is an illustrative map marker.'),
  ('keys-road','Keys highways','leonida-keys','routes',826,875,'The island road theme is an exploration idea, not a confirmed route overlay.'),
  ('marshes','Wetland trails','grassrivers','nature',510,661,'The wetlands region is official. Trails and their coordinates are not yet verified.'),
  ('airboats','Airboat country','grassrivers','coast',639,770,'Wild waterways and airboat exploration potential; map placement is illustrative.'),
  ('wildlife','Wildlife country','grassrivers','nature',465,765,'Outdoor wildlife is a Leonida theme; not a confirmed spawn location.'),
  ('gulf','Gulf waterfront','port-gellhorn','coast',345,492,'A schematic marker for the Gulf coast atmosphere of Port Gellhorn.'),
  ('roadside','Roadside stops','port-gellhorn','routes',477,500,'A broad reminder to explore the coastal highway scenes. Not an identified business.'),
  ('sugar','Rural heartland','ambrosia','nature',608,475,'Agricultural landscapes are associated with Ambrosia. This point is conceptual.'),
  ('industry','Industry belt','ambrosia','city',735,489,'Broad industrial flavor, with no verified property or mission marked.'),
  ('lake','Inland lakes','ambrosia','coast',753,350,'Illustrative inland-waterway point; do not navigate by these coordinates.'),
  ('trails','Northern trails','mount-kalaga','nature',833,252,'Explore the national park environment. The hiking trail is not a confirmed game path.'),
  ('lookout','Highland lookout','mount-kalaga','nature',688,120,'A notional wilderness scenic point, not a verified collectible or viewpoint.'),
]
for ident,title,region,cat,x,y,desc in EXPLORE:
    MAP_ITEMS.append(dict(id=ident,title=title,subtitle='Explore theme',fact='Illustrative, not a verified location',description=desc,x=x,y=y,cat=cat,region=region,source=BASE+('kalaga' if region=='mount-kalaga' else region),official=False))

def atlas_svg():
    r=Random(617)
    outline='M405 -42 C480 65 443 134 480 188 C439 254 408 299 399 358 C352 388 287 440 280 492 C291 556 350 567 409 615 C446 675 435 729 487 786 C555 809 619 784 675 806 C731 790 795 810 832 783 C877 745 881 714 879 653 C885 590 908 563 930 516 C929 449 950 416 953 366 C979 324 971 274 1014 235 C1008 190 1047 158 1041 98 L1110 -30 Z'
    chunks=[]
    chunks.append('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 1000" role="img" aria-labelledby="map-title map-desc"><title id="map-title">Original conceptual map of Leonida</title><desc id="map-desc">Illustrative locations of six officially named GTA 6 regions, not an official street map.</desc><defs><radialGradient id="sea"><stop stop-color="#173b4b"/><stop offset=".65" stop-color="#102431"/><stop offset="1" stop-color="#101827"/></radialGradient><linearGradient id="land" x1="0" y1="0" x2=".7" y2="1"><stop stop-color="#435850"/><stop offset=".6" stop-color="#29464b"/><stop offset="1" stop-color="#284047"/></linearGradient><linearGradient id="keys"><stop stop-color="#4b6b60"/><stop offset="1" stop-color="#3f796d"/></linearGradient><pattern id="oceanGrid" width="55" height="55" patternUnits="userSpaceOnUse"><path d="M55 0H0V55" fill="none" stroke="#81aac0" stroke-opacity=".08" stroke-width="1"/></pattern><pattern id="landHatch" width="13" height="13" patternUnits="userSpaceOnUse"><path d="M0 13L13 0" stroke="#99c3a1" stroke-width=".6" stroke-opacity=".07"/></pattern><clipPath id="mainClip"><path d="'''+outline+'''"/></clipPath><filter id="softGlow"><feGaussianBlur stdDeviation="4"/></filter><filter id="pinShadow"><feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#020711" flood-opacity=".7"/></filter></defs>''')
    chunks.append('<rect width="1400" height="1000" fill="url(#sea)"/><rect width="1400" height="1000" fill="url(#oceanGrid)"/>')
    chunks.append('<g stroke="#75d7cb" opacity=".07" fill="none">'+''.join(f'<path d="M{100+j*97} 100Q{350+j*50} 300 {90+j*118} 790"/>' for j in range(11))+'</g>')
    chunks.append(f'<path d="{outline}" fill="#50c8bd" stroke="#63d4d3" stroke-opacity=".25" stroke-width="22" filter="url(#softGlow)"/>')
    chunks.append(f'<path d="{outline}" fill="url(#land)" stroke="#7bc4b1" stroke-opacity=".72" stroke-width="3"/><path d="{outline}" fill="url(#landHatch)"/>')
    chunks.append('<g clip-path="url(#mainClip)">')
    # natural parks, agricultural blocks and marshlands
    for x,y,rx,ry,c in [(715,205,220,150,'#35574f'),(610,675,250,190,'#37605c'),(665,414,170,120,'#6a654c'),(435,505,140,140,'#3e5651')]:
        chunks.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" opacity=".4"/>')
    for i in range(95):
        x=r.randint(295,1080); y=r.randint(25,890); rad=r.choice([4,6,7,12]);opacity=r.uniform(.06,.18)
        chunks.append(f'<circle cx="{x}" cy="{y}" r="{rad}" fill="#8bd0a2" opacity="{opacity:.2f}"/>')
    # highland contour rings
    for radius in [35,64,103,144,180]:
        chunks.append(f'<ellipse cx="730" cy="185" rx="{radius*1.3}" ry="{radius*.72}" stroke="#bcda92" opacity=".19" fill="none" stroke-width="2"/>')
    # local tertiary roads running through mainland; clipped to coastline
    for i in range(21):
        y=85+i*38
        chunks.append(f'<path d="M290 {y} Q620 {y-40+r.randint(-40,40)} 1150 {y+r.randint(-60,60)}" fill="none" stroke="#b6aa8a" opacity=".15" stroke-width="{r.choice([1.2,1.5,2])}"/>')
    for i in range(20):
        x=325+i*38
        chunks.append(f'<path d="M{x} -30 Q{x+45} 440 {x+r.randint(-85,80)} 940" fill="none" stroke="#c5b6a2" opacity=".14" stroke-width="1.7"/>')
    # primary routes, schematic and non-navigable
    roads=['M415 70 C490 180 500 260 585 320 S754 510 914 630',
           'M353 486 C510 445 630 555 878 631',
           'M600 74 C710 210 900 298 930 487 S925 725 800 837',
           'M488 740 Q650 616 882 682',
           'M446 388 Q630 330 814 430',
           'M550 715 C580 540 668 438 780 239']
    for i,p in enumerate(roads):
        chunks.append(f'<path d="{p}" stroke="#101d28" stroke-width="12" opacity=".63" fill="none"/><path d="{p}" stroke="{r.choice(["#b8b6ab","#d2a580","#b8b6ab"])}" stroke-width="3.8" opacity=".63" fill="none"/>')
    # City street grid on east coast - lines partially concealed by clip
    chunks.append('<rect x="810" y="480" width="360" height="310" fill="#59606b" opacity=".15"/>')
    for x in range(805,1140,24):
        chunks.append(f'<path d="M{x} 475 L{x+20} 815" stroke="#c6c7bb" stroke-width="{2.8 if x%3 else 4}" opacity=".52"/>')
    for y in range(485,830,22):
        chunks.append(f'<path d="M792 {y} L1173 {y+10}" stroke="#c6c7bb" stroke-width="{2 if y%3 else 4}" opacity=".42"/>')
    chunks.append('</g>')
    # Barrier island, channels, rivers and Keys. All drawn independently.
    chunks.append('<path d="M987 434 C1007 492 982 540 995 615 C1016 694 1009 765 1050 815 C1073 776 1087 712 1071 643 C1080 573 1070 502 1043 430Z" fill="#277a81" stroke="#7de6d0" stroke-opacity=".25" stroke-width="2" opacity=".7"/>')
    chunks.append('<path d="M1081 448 C1126 474 1151 540 1141 602 L1149 725 C1167 756 1175 812 1157 835 C1116 789 1114 710 1125 625 Q1109 530 1081 448Z" fill="#536560" stroke="#b1e6d1" stroke-width="2.5" opacity=".92"/>')
    for y in (545,625,710,770):
        chunks.append(f'<path d="M902 {y} Q1024 {y-22} 1134 {y+2}" stroke="#e6c3a2" stroke-width="4" opacity=".74" fill="none"/>')
    chunks.append('<g fill="url(#keys)" stroke="#93d5be" stroke-width="2" stroke-opacity=".74">')
    islands=[(802,830,62,18,-25),(841,880,66,20,-18),(883,916,60,17,20),(949,941,49,13,16),(1011,959,48,12,27),(1079,967,38,11,10),(1150,975,27,9,10)]
    for x,y,rx,ry,rot in islands:chunks.append(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" transform="rotate({rot} {x} {y})"/>')
    chunks.append('</g>')
    chunks.append('<path d="M760 786 Q793 838 831 871 T921 931 Q986 958 1126 978" stroke="#d5b598" stroke-width="3" fill="none" opacity=".7"/>')
    # muted region labels are cartographic decoration, not precise boundaries
    for x,y,label in [(655,130,'MOUNT KALAGA'),(525,345,'PORT GELLHORN'),(630,550,'AMBROSIA'),(475,735,'GRASSRIVERS'),(987,454,'VICE CITY'),(928,870,'LEONIDA KEYS')]:
        chunks.append(f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" font-size="18" font-weight="700" letter-spacing="3" text-anchor="middle" fill="#d2e5d4" fill-opacity=".28">{h(label)}</text>')
    chunks.append('<text x="123" y="202" font-family="Arial,sans-serif" font-size="11" letter-spacing="8" fill="#a1cbd8" opacity=".42" transform="rotate(-90 123 202)">GULF WATERS</text>')
    chunks.append('<text x="1270" y="560" font-family="Arial,sans-serif" font-size="12" letter-spacing="8" fill="#a1cbd8" opacity=".42" transform="rotate(90 1270 560)">ATLANTIC</text>')
    chunks.append('<rect x="0" y="0" width="1400" height="1000" fill="none" stroke="#b6e7e2" stroke-opacity=".13" stroke-width="5"/>')
    chunks.append('</svg>')
    return ''.join(chunks)

def atlas_body():
    summary = '''<section class="map-intro wrap"><div class="crumb"><a href="/">HOME</a> / GTA 6 MAP</div><div class="map-intro-row"><div><div class="eyebrow">// GTA 6 / WORLD INTEL / STREET-LEVEL EXPLORER</div><h1>LEONIDA<span>UP CLOSE.</span></h1><p>Go from the whole state to individual streets and buildings. Search the GTA VI mapping community's named landmarks, save your own discoveries, or switch back to our original concept atlas.</p></div><div class="map-intro-side"><span class="map-intro-badge">6 <small>ROCKSTAR-NAMED REGIONS</small></span><span class="map-intro-badge" id="atlas-total-badge">… <small>COMMUNITY LOCATIONS</small></span></div></div></section>'''
    fltrs = [('all','All places'),('hotel','Hotels & stays'),('shop','Shops & services'),('transport','Transport'),('food','Food & nightlife'),('nature','Nature'),('landmark','Landmarks')]
    filters=''.join(f'<button class="atlas-filter {"is-selected" if key=="all" else ""}" type="button" data-atlas-filter="{key}" aria-pressed="{str(key=="all").lower()}"><span class="atlas-filter-dot {key}"></span>{h(label)} <b data-filter-count="{key}"></b></button>' for key,label in fltrs)
    chips=''.join(f'<button class="region-chip" type="button" data-jump="{h(slug)}"><span>{h(name)}</span><small>ZOOM IN</small></button>' for slug,name,*_ in REGIONS)
    rows=''.join(f'<li><a href="https://www.rockstargames.com/VI/only-in-leonida/{"kalaga" if slug=="mount-kalaga" else h(slug)}" target="_blank" rel="noopener noreferrer">{h(name)}</a> &mdash; {h(desc)}</li>' for slug,name,desc,*_ in REGIONS)
    return summary + f'''<main class="atlas-wrap wrap" id="atlas"><div class="atlas-banner"><div><span class="tiny-pulse"></span> GTASIX / GTA 6 LIVE WORLD DESK</div><div>MAP DATA: COMMUNITY RECONSTRUCTION &middot; 18 NOV 2026</div></div>
<div class="atlas-shell"><aside class="atlas-sidebar"><div class="atlas-side-title"><span>EXPLORE LEONIDA</span><span>GTA 6 / VI</span></div><label class="atlas-search-label" for="atlas-query">SEARCH COMMUNITY LOCATIONS</label><div class="atlas-search-box"><span aria-hidden="true">&#8981;</span><input id="atlas-query" type="search" autocomplete="off" placeholder="Hotels, ports, neighborhoods..." aria-label="Search GTA 6 community map locations"/><kbd>/</kbd></div><div class="atlas-data-note" id="atlas-data-note" role="status">Loading community landmarks…</div><div class="atlas-filters" aria-label="Map location filters">{filters}</div><div class="atlas-result-heading"><span>DISCOVER PLACES</span><span data-atlas-count>LOADING</span></div><div id="atlas-results" class="atlas-results" role="list" aria-live="polite"></div><div class="atlas-savebox"><div><strong data-atlas-saved>0 saved places</strong><span>Bookmarks and custom pins stay in this browser</span></div><button id="atlas-clear" type="button">CLEAR</button></div></aside>
<div class="atlas-stage"><div class="atlas-map-hud"><div><span class="map-hud-name">GT<span>A 6</span> / LEONIDA</span><small id="atlas-hud-sub">YANIS COMMUNITY MAP &middot; CC BY 4.0</small></div><span class="atlas-live-dot" id="atlas-status">COMMUNITY MAP</span></div><div class="atlas-view-toggle" role="group" aria-label="Select map style"><button type="button" id="atlas-detailed" class="selected" aria-pressed="true">DETAILED MAP</button><button type="button" id="atlas-concept" aria-pressed="false">NEON ATLAS</button></div><div id="atlas-viewport" class="atlas-viewport" aria-label="Interactive GTA 6 community map: drag to pan, pinch or wheel to zoom, use location list to explore" tabindex="0"><div id="atlas-world" class="atlas-world"><img id="atlas-base" src="/assets/leonida-concept.svg" alt="GTA 6 Leonida map; community-drawn streets, not an official in-game map" draggable="false"/><div id="atlas-pins" class="atlas-pins" aria-label="Map locations"></div></div></div><div class="atlas-map-controls"><button type="button" id="atlas-zoom-in" aria-label="Zoom in">+</button><button type="button" id="atlas-zoom-out" aria-label="Zoom out">&minus;</button><button type="button" id="atlas-reset" aria-label="Reset map view">&#8635;</button><button type="button" id="atlas-add" aria-label="Add a private custom pin" title="Add a private map pin">&#43;&#9670;</button></div><div class="atlas-scale" id="atlas-zoom-readout">ZOOM / 1.0X &middot; COMMUNITY</div><div class="atlas-detail" id="atlas-detail" hidden aria-live="polite"><div class="atlas-detail-head"><span class="atlas-detail-kicker">MAP INTEL</span><button type="button" id="atlas-close-detail" aria-label="Close location details">&times;</button></div><span class="atlas-detail-label" id="atlas-detail-label">COMMUNITY MAPPING</span><h2 id="atlas-detail-title">Vice City</h2><p id="atlas-detail-copy"></p><div class="atlas-detail-actions"><button type="button" id="atlas-bookmark" class="atlas-bookmark" aria-pressed="false">SAVE PLACE</button><a id="atlas-detail-source" target="_blank" rel="noopener noreferrer" href="https://map.gtadb.org/">MAPPING SOURCE &#8599;</a><button type="button" id="atlas-delete-custom" hidden>DELETE PIN</button></div></div><form id="atlas-pin-form" class="atlas-pin-form" hidden><strong>DROP YOUR OWN PIN</strong><p>Save a building or street you want to revisit. Private to this browser.</p><label for="atlas-pin-name">Name this place</label><input id="atlas-pin-name" maxlength="70" required placeholder="My favorite corner"/><div><button type="submit">SAVE PIN</button><button type="button" id="atlas-pin-cancel">CANCEL</button></div></form><div class="atlas-hint" id="atlas-hint">DRAG TO PAN &nbsp;/&nbsp; SCROLL OR PINCH TO ZOOM</div></div></div><div class="atlas-under"><span><b>COMMUNITY RECONSTRUCTION, NOT THE OFFICIAL GAME MAP.</b> Roads, buildings and markers are based on pre-release mapping; interiors and accessibility are not confirmed. </span><span class="atlas-credit">Base art: <a href="https://map.gtadb.org" target="_blank" rel="noopener noreferrer">GTADB.ORG / YANIS + contributors</a> (<a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener noreferrer">CC BY 4.0</a>), <a href="https://gtami.com/en/official-map/" target="_blank" rel="noopener noreferrer">GTAMI processed image</a>.</span></div></main>
<section class="wrap atlas-after"><div class="section-top"><div><div class="section-label">// SIX ROCKSTAR-NAMED REGIONS</div><h2 class="section-title">Where to explore first?</h2><p class="section-note">Region names are official; the coordinates shown are community-estimated.</p></div></div><div class="atlas-regions">{chips}</div><div class="atlas-context"><div><span class="section-label">// HONEST MAP INTEL</span><h2>Confirmed vs. community estimated.</h2><p>Rockstar has confirmed the six regions below, but a public, fully verified building-by-building in-game map is not yet available. The detailed imagery is a community reconstruction by YANIS and GTADB contributors. It is not a screenshot or an exact replica of the released game. The matching map coordinates are approximate, and buildings shown may not be accessible.</p><ul>{rows}</ul><a class="atlas-context-link" href="https://www.rockstargames.com/VI" target="_blank" rel="noopener noreferrer">OFFICIAL GTA 6 SOURCE &#8599;</a></div><div class="atlas-tipbox"><span class="eyebrow">// MAPPING COMMUNITY</span><h3>ZOOM INTO THE WORLD.</h3><p>Pan across detailed streets, filter known community place names, open source information, and save your own pins. When official in-game geography can be independently verified, community locations can be updated without losing your saved notes.</p><a href="https://vice-city.app/map" target="_blank" rel="noopener noreferrer">SEE THE REFERENCE MAP &#8599;</a></div></div></section>'''

def write_atlas_assets(site_dir):
    dest=Path(site_dir)/'assets'/'leonida-concept.svg'
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(atlas_svg(),encoding='utf8')
    return dest

if __name__=='__main__':
    write_atlas_assets(Path(__file__).resolve().parent.parent/'site')
    print('Atlas:',len(MAP_ITEMS),'pins')

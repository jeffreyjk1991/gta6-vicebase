from pathlib import Path
p=Path(__file__).with_name('build.py')
s=p.read_text()
checks=[
("from content import articles,categories,roadmap,videos,ROCKSTAR,PS5,RELEASE,STORE", "from content import articles,categories,roadmap,videos,ROCKSTAR,PS5,RELEASE,STORE\nfrom map_atlas import MAP_ITEMS,REGIONS,atlas_body,write_atlas_assets"),
("<span class=\"brand-sub\">THE GTA VI FIELD GUIDE</span></span></a>'", "<span class=\"brand-sub\">THE GTA VI FIELD GUIDE</span></span><span class=\"brand-gta6\">GTA <b>6</b></span></a>'"),
("('THE WORLD','/categories/world/','world')", "('GTA 6 MAP','/map/','map')"),
("<a href=\"/guides/\">All guides</a><a href=\"/videos/\">Official videos</a>","<a href=\"/guides/\">All guides</a><a href=\"/map/\">Interactive GTA 6 map</a><a href=\"/videos/\">Official videos</a>"),
("def page(title,desc,body,active='',path='/',ld=None):", "def page(title,desc,body,active='',path='/',ld=None,extra_head=''):"),
("<link rel=\"stylesheet\" href=\"/assets/styles.css\"><script type=\"application/ld+json\">", "<link rel=\"stylesheet\" href=\"/assets/styles.css\"><link rel=\"stylesheet\" href=\"/assets/map.css\">{extra_head}<script type=\"application/ld+json\">"),
("<h1><span>OWN THE</span><span class=\"gradient\">STREETS.</span></h1>","<h1 class=\"hero-h1-gta\"><span class=\"hero-gta6\">GTA <em>6</em></span><span>OWN THE</span><span class=\"gradient\">STREETS.</span></h1>"),
]
for old,new in checks:
    if old not in s:
        raise RuntimeError('Expected build pattern not found: '+old[:100])
    s=s.replace(old,new,1)
# Home teaser before deal desk
needle='<section class="section" id="buy-spotlight">'
addition='''<section class="section" id="world-map-preview">{top_line('NEW','THE WORLD IS YOURS','Explore the GTA 6 map','Six official regions. An original, interactive GTASIX map with zoom, filters and saved places.',('OPEN THE FULL MAP','/map/'))}<a class="atlas-teaser" href="/map/"><div class="atlas-teaser-copy"><span class="eyebrow">// GTA 6 / STATE OF LEONIDA</span><h3>VICE CITY.<span>AND BEYOND.</span></h3><p>Explore all six regions, search the atlas, and bookmark your favorite spots. An original conceptual overview that separates Rockstar-confirmed names from fan speculation.</p><span class="btn">ENTER THE GTA 6 MAP {icon('arrow',17)}</span></div><div class="atlas-teaser-visual"><img src="/assets/leonida-concept.svg" loading="lazy" alt="Original illustrated map preview of Leonida in GTA 6"><span class="atlas-preview-label">06 OFFICIAL REGIONS</span><span class="atlas-preview-pin">VICE CITY</span></div></a></section>
'''
assert needle in s
s=s.replace(needle,addition+needle,1)
# map page function before buy_page
needle='def buy_page():'
func='''def map_page():
    path='/map/'
    desc='Interactive GTA 6 Leonida map: explore Vice City, Leonida Keys, Grassrivers, Port Gellhorn, Ambrosia and Mount Kalaga. Search, filter, zoom and save places.'
    ld=[{'@context':'https://schema.org','@type':'CollectionPage','name':'GTA 6 interactive Leonida map','description':desc,'url':uri(path),'about':{'@type':'VideoGame','name':'Grand Theft Auto VI','url':ROCKSTAR}},
        {'@context':'https://schema.org','@type':'ItemList','name':'Rockstar-named GTA 6 regions','itemListElement':[{'@type':'ListItem','position':i+1,'name':v[1],'url':f'https://www.rockstargames.com/VI/only-in-leonida/{v[0]}'} for i,v in enumerate(REGIONS)]}]
    safe_data=json.dumps(MAP_ITEMS,ensure_ascii=True,separators=(',',':')).replace('<','\\\\u003c')
    body=atlas_body()+'<script id="atlas-data" type="application/json">'+safe_data+'</script>'
    write(path,page('GTA 6 Interactive Map of Leonida & Vice City | GTASIX',desc,body,'map',path,ld,extra_head='<script defer src="/assets/map.js"></script>'))

'''
assert needle in s
s=s.replace(needle,func+needle,1)
needle='    home();listing()'
assert needle in s
s=s.replace(needle,'    write_atlas_assets(OUT)\n    home();map_page();listing()',1)
p.write_text(s)
print('Updated',p)

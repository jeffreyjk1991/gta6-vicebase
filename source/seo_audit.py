"""Static SEO/AI discoverability checks; run after python source/build.py.
Tests enforce accurate metadata, indexability, structured data, sitemaps and links.
Passing is not a promise of indexing or rankings.
"""
from pathlib import Path
from urllib.parse import urlparse, unquote
from bs4 import BeautifulSoup
from collections import Counter
import json, xml.etree.ElementTree as ET, sys
ROOT=Path(__file__).resolve().parent.parent
SITE=ROOT/'site'
base='https://gtasix.tech'
errors=[]
pages=list(SITE.rglob('index.html'))
all_titles=[]; all_urls=[]; all_checks=0
for file in sorted(pages):
    rel=file.relative_to(SITE)
    url='/' if rel==Path('index.html') else '/'+str(rel.parent).replace('\\','/')+'/'
    html=file.read_text(encoding='utf8')
    s=BeautifulSoup(html,'html.parser')
    title=(s.title.get_text(' ',strip=True) if s.title else '')
    description=s.find('meta',attrs={'name':'description'})
    description=description.get('content','') if description else ''
    canon=s.find('link',rel='canonical')
    canon=canon.get('href') if canon else None
    robots=s.find('meta',attrs={'name':'robots'})
    robots=robots.get('content','') if robots else ''
    if not title:errors.append(f'{url}: missing title')
    if not (90 <= len(description) <= 160):errors.append(f'{url}: description length {len(description)}')
    if canon!=base+url:errors.append(f'{url}: bad canonical {canon}')
    if 'noindex' in robots:errors.append(f'{url}: index page is noindex')
    if len(s.find_all('h1'))!=1:errors.append(f'{url}: h1 count {len(s.find_all("h1"))}')
    graph_scripts=s.find_all('script',attrs={'type':'application/ld+json'})
    if not graph_scripts:errors.append(f'{url}: no structured data')
    for script in graph_scripts:
        try:
            graph=json.loads(script.string or script.get_text())
            nodes=graph.get('@graph',[]) if isinstance(graph,dict) else graph
            if not isinstance(nodes,list):nodes=[nodes]
            if not any(n.get('@type')=='WebPage' and n.get('url')==base+url for n in nodes if isinstance(n,dict)):
                errors.append(f'{url}: missing matching WebPage schema')
        except Exception as exc:
            errors.append(f'{url}: malformed JSON-LD {exc}')
    for a in s.find_all('a',href=True):
        h=a.get('href','').strip(); parsed=urlparse(h)
        if parsed.scheme in ('mailto','tel') or parsed.netloc or h.startswith('//') or h.startswith('#'):continue
        if parsed.scheme and parsed.scheme not in ('http','https'):continue
        path=unquote(parsed.path)
        if not path.startswith('/'):continue
        dest=SITE/path.lstrip('/')
        if path.endswith('/'):dest=dest/'index.html'
        if not dest.is_file():errors.append(f'{url}: broken internal link {h}')
        all_checks+=1
    all_titles.append(title);all_urls.append(base+url)
for title,n in Counter(all_titles).items():
    if n>1:errors.append(f'duplicate title: {title}')
robots=(SITE/'robots.txt').read_text(encoding='utf8')
if 'User-agent: OAI-SearchBot\nAllow: /' not in robots:errors.append('OAI-SearchBot not explicitly allowed')
if base+'/sitemap.xml' not in robots:errors.append('Sitemap not in robots.txt')
try:
    root=ET.parse(SITE/'sitemap.xml').getroot()
    sm={e.text for e in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
    if set(all_urls)!=sm: errors.append(f'sitemap mismatch missing={sorted(set(all_urls)-sm)} extra={sorted(sm-set(all_urls))}')
    if root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}priority'):errors.append('obsolete sitemap priority tags')
except Exception as exc: errors.append(f'sitemap XML failed: {exc}')
err_html=BeautifulSoup((SITE/'404.html').read_text(encoding='utf8'),'html.parser')
if 'noindex' not in err_html.find('meta',attrs={'name':'robots'}).get('content',''):errors.append('404 not marked noindex')
for path in ('gta-6-facts/index.html','map/index.html','characters/index.html','buy/index.html'):
    if not (SITE/path).is_file():errors.append(f'important page missing: {path}')
for slug in ('gta-6-download-size-ps5-xbox','best-ps5-ssd-requirements-for-gta-6','gta-6-preload-not-working'):
    if 'class="seo-extra"' not in (SITE/'guides'/slug/'index.html').read_text():errors.append(f'key guide lacks editorial detail: {slug}')
print(f'Checked {len(pages)} indexable pages, {all_checks} internal links, sitemap, JSON-LD and crawler rules. Errors: {len(errors)}')
for err in errors[:30]:print(' -',err)
sys.exit(1 if errors else 0)

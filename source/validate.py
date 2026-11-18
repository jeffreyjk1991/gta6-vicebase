from pathlib import Path
from bs4 import BeautifulSoup
import json,re
from urllib.parse import urlparse,unquote
root=Path(__file__).resolve().parent.parent/'site';htmls=list(root.rglob('*.html'))
errors=[];checks=0;external=set();titles=set();paths=set()
for file in htmls:
 s=BeautifulSoup(file.read_text(), 'html.parser')
 title=s.title.get_text(strip=True) if s.title else ''
 if not title:errors.append(f'{file}: empty title')
 if title in titles:errors.append(f'{file}: duplicate title {title}')
 titles.add(title)
 if not s.find('meta',attrs={'name':'description'}):errors.append(f'{file}: no description')
 if file.name=='index.html' and not s.h1:errors.append(f'{file}: no h1')
 for a in s.find_all('a',href=True):
  link=a['href'];u=urlparse(link)
  if u.scheme in ['mailto','tel']:continue
  if u.scheme and u.scheme not in ['http','https']:continue
  if u.netloc:external.add(u.netloc);continue
  if u.path.startswith('/'):
   path=unquote(u.path)
   target=root/path.strip('/')
   if path.endswith('/'):target=target/'index.html'
   if not target.is_file():errors.append(f'{file.relative_to(root)} -> broken {link}')
  checks+=1
 for script in s.find_all('script',type='application/ld+json'):
  try:json.loads(script.string or script.get_text())
  except Exception as e:errors.append(f'{file}: schema invalid {e}')
print('HTML PAGES',len(htmls),'INTERNAL LINK CHECKS',checks,'EXTERNAL DOMAINS',sorted(external),'ERRORS',len(errors))
for err in errors[:60]:print(' -',err)
if errors:exit(1)

import asyncio, mimetypes
from pathlib import Path
from urllib.parse import urlsplit
from playwright.async_api import async_playwright
ROOT=Path('/mnt/data/gta6-vicebase/site')
async def serve(route):
  u=urlsplit(route.request.url)
  if u.hostname!='gtasix.test': await route.abort(); return
  target=ROOT/u.path.lstrip('/')
  if u.path.endswith('/'): target=target/'index.html'
  if not target.is_file(): await route.fulfill(status=404,body='Missing'); return
  await route.fulfill(status=200,content_type=mimetypes.guess_type(str(target))[0] or 'text/html',body=target.read_bytes())
async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  for width,height in [(1440,900),(390,844)]:
   pg=await b.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
   errors=[]
   pg.on('pageerror',lambda e:errors.append(str(e)))
   await pg.route('**/*',serve)
   await pg.goto('https://gtasix.test/',wait_until='load',timeout=20000)
   await pg.wait_for_timeout(200)
   print(width,'home H1',await pg.locator('h1').inner_text(),'days',await pg.locator('[data-count-days]').inner_text(),'hour',await pg.locator('[data-count-hours]').inner_text(),'horizontal overflow',await pg.evaluate('document.documentElement.scrollWidth > window.innerWidth'))
   await pg.screenshot(path=f'/mnt/data/gta6-vicebase/home-new-{width}.png',full_page=True)
   await pg.goto('https://gtasix.test/buy/',wait_until='load',timeout=20000)
   print(width,'retailers',await pg.locator('[data-buy-row]').count(),'buy platform',await pg.locator('[data-buy-platform].selected').inner_text(),'overflow',await pg.evaluate('document.documentElement.scrollWidth > window.innerWidth'))
   a=pg.locator('[data-buy-row] .retailer-link').first
   ps=await a.get_attribute('href');await pg.locator('[data-buy-platform="xbox"]').click();xb=await a.get_attribute('href');print('switch',ps,xb,'changed',ps!=xb)
   await pg.screenshot(path=f'/mnt/data/gta6-vicebase/buy-new-{width}.png',full_page=True)
   print('JS errors',errors)
   await pg.close()
  await b.close()
asyncio.run(main())

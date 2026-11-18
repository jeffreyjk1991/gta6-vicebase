import asyncio, json
from pathlib import Path
from playwright.async_api import async_playwright
R=Path('/mnt/data/gta6-vicebase/site')
async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  for tag,w,h in [('desktop',1440,900),('mobile',390,844)]:
   page=await browser.new_page(viewport={'width':w,'height':h})
   errors=[]
   page.on('pageerror',lambda e:errors.append(str(e)))
   fixture=[{'id':'gtadb-a','title':'Ocean View Hotel','subtitle':'Ocean Beach / Vice City','cat':'hotel','x':3620,'y':2810},{'id':'gtadb-b','title':'Port Gellhorn Marina','subtitle':'Gulf Coast','cat':'transport','x':760,'y':2700}]
   await page.route('**/assets/gtadb-landmarks.json',lambda route:route.fulfill(status=200,content_type='application/json',body=json.dumps(fixture*12)))
   svg=(R/'assets/leonida-concept.svg').read_text()
   await page.route('**/karta-gta-6-gtami-full-*.jpg',lambda route:route.fulfill(status=200,content_type='image/svg+xml',body=svg))
   await page.route('**/Official_Cover_Art_landscape.*.jpg*',lambda route:route.fulfill(status=200,content_type='image/svg+xml',body=svg))
   async def serve(route):
    from urllib.parse import urlparse
    url=route.request.url
    if 'gtadb-landmarks.json' in url:
     return await route.fulfill(status=200,content_type='application/json',body=json.dumps(fixture*12))
    if 'gtami.com/assets/' in url or 'rockstargames.com/VI/_next' in url:
     return await route.fulfill(status=200,content_type='image/svg+xml',body=svg)
    if url.startswith('https://gtasix.test/'):
     path=urlparse(url).path.lstrip('/')
     file=R/path
     if path=='' or path.endswith('/'):
      file=R/path/'index.html'
     if file.exists() and file.is_file():
      ext=file.suffix
      content_type={'.html':'text/html','.js':'application/javascript','.css':'text/css','.svg':'image/svg+xml','.json':'application/json','.png':'image/png'}.get(ext,'text/plain')
      return await route.fulfill(status=200,content_type=content_type,body=file.read_bytes())
    return await route.abort('blockedbyclient')
   await page.route('**/*',serve)
   await page.goto('https://gtasix.test/map/',wait_until='domcontentloaded')
   await page.wait_for_timeout(1100)
   print(tag,'mode',await page.locator('#atlas-status').inner_text(),'count',await page.locator('[data-atlas-count]').inner_text(),'image src',await page.locator('#atlas-base').get_attribute('src'))
   assert await page.locator('#atlas-status').inner_text()=='COMMUNITY / UNOFFICIAL'
   assert await page.locator('.atlas-result').count() > 0
   await page.locator('#atlas-query').fill('Ocean View')
   assert await page.locator('.atlas-result').count()>0
   await page.locator('.atlas-result').first.click()
   assert await page.locator('#atlas-detail').is_visible()
   await page.locator('#atlas-bookmark').click()
   print(tag,'saved',await page.locator('[data-atlas-saved]').inner_text())
   await page.locator('#atlas-close-detail').click()
   await page.locator('#atlas-concept').click()
   assert 'CONCEPT' in (await page.locator('#atlas-status').inner_text())
   await page.locator('#atlas-detailed').click()
   await page.locator('#atlas-query').fill('')
   await page.locator('#atlas-add').click()
   loc=page.locator('#atlas-viewport');box=await loc.bounding_box()
   await page.mouse.click(box['x']+box['width']*0.5,box['y']+box['height']*.5)
   assert await page.locator('#atlas-pin-form').is_visible()
   await page.locator('#atlas-pin-name').fill('My Favorite Street')
   await page.locator('#atlas-pin-form button[type=submit]').click()
   assert '1 personal pin' in (await page.locator('[data-atlas-saved]').inner_text())
   await page.locator('#atlas-zoom-in').click()
   await page.screenshot(path=f'/mnt/data/gta6-vicebase/{tag}-detailed-map-test.png',full_page=True)
   print(tag,'scrollwidth',await page.evaluate('document.body.scrollWidth'),'inner',w,'errors',errors)
   assert await page.evaluate('document.body.scrollWidth')<=w
   assert not errors,errors
   await page.goto('https://gtasix.test/',wait_until='domcontentloaded')
   await page.wait_for_timeout(250)
   print(tag,'hero poster CSS',await page.locator('.hero').evaluate('(el)=>getComputedStyle(el).backgroundImage.includes("rockstargames.com")'))
   assert await page.locator('.hero').evaluate('(el)=>getComputedStyle(el).backgroundImage.includes("rockstargames.com")')
   await page.close()
  await browser.close()
asyncio.run(main())

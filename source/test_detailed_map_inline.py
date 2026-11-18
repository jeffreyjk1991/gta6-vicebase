import asyncio,base64,json
from pathlib import Path
from playwright.async_api import async_playwright
R=Path('/mnt/data/gta6-vicebase/site')
svg=base64.b64encode((R/'assets/leonida-concept.svg').read_bytes()).decode()
img='data:image/svg+xml;base64,'+svg
fixture=[{'id':'gtadb-a','title':'Ocean View Hotel','subtitle':'Ocean Beach / Vice City','cat':'hotel','x':3620,'y':2810},{'id':'gtadb-b','title':'Port Gellhorn Marina','subtitle':'Gulf Coast','cat':'transport','x':760,'y':2700}]*12

def inline_html(path):
 s=(R/path).read_text()
 for f in ('styles.css','map.css'):
  css=(R/'assets'/f).read_text().replace("url('vice-skyline.svg')",f"url('{img}')")
  if css.startswith('@import'):css=css.split('\n',1)[1]
  s=s.replace(f'<link rel="stylesheet" href="/assets/{f}">','<style>'+css+'</style>')
 s=s.replace('src="/assets/leonida-concept.svg"',f'src="{img}"')
 mock='<script>window.fetch=(url)=>Promise.resolve({ok:true,json:async()=>'+json.dumps(fixture)+'});</script>'
 scripts=[]
 for f in ('app.js','map.js'):
  tag=f'<script defer src="/assets/{f}"></script>'
  if tag in s:
   s=s.replace(tag,'')
   js=(R/'assets'/f).read_text()
   js=js.replace('https://gtami.com/assets/img/karta-gta-6-gtami-full-4096.jpg',img)
   js=js.replace('https://gtami.com/assets/img/karta-gta-6-gtami-full-8192.jpg',img)
   js=js.replace("'/assets/leonida-concept.svg'","'"+img+"'")
   scripts.append('<script>'+js+'</script>')
 return s.replace('</body>',mock+''.join(scripts)+'</body>')

async def main():
 async with async_playwright() as p:
  b=await p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
  for tag,w,h in [('desktop',1440,900),('mobile',390,844)]:
   page=await b.new_page(viewport={'width':w,'height':h});errs=[]
   page.on('pageerror',lambda e:errs.append(str(e)))
   await page.set_content(inline_html('map/index.html'),wait_until='domcontentloaded')
   await page.wait_for_timeout(450)
   print(tag,'mode',await page.locator('#atlas-status').inner_text(),'count',await page.locator('[data-atlas-count]').inner_text(),'pins',await page.locator('.atlas-pin').count())
   assert await page.locator('#atlas-status').inner_text()=='COMMUNITY / UNOFFICIAL'
   assert await page.locator('.atlas-result').count()>0
   await page.locator('#atlas-query').fill('Ocean View')
   assert await page.locator('.atlas-result').count()>0
   await page.locator('.atlas-result').first.click()
   assert await page.locator('#atlas-detail').is_visible()
   await page.locator('#atlas-bookmark').click()
   await page.locator('#atlas-close-detail').click()
   await page.locator('#atlas-concept').click()
   assert 'CONCEPT' in await page.locator('#atlas-status').inner_text()
   await page.locator('#atlas-detailed').click()
   await page.locator('#atlas-query').fill('')
   await page.locator('#atlas-add').click()
   el=page.locator('#atlas-viewport');r=await el.bounding_box()
   await page.mouse.click(r['x']+r['width']*.47,r['y']+r['height']*.45)
   assert await page.locator('#atlas-pin-form').is_visible()
   await page.locator('#atlas-pin-name').fill('My Favorite Street')
   await page.locator('#atlas-pin-form button[type=submit]').click()
   assert '1 personal pin' in await page.locator('[data-atlas-saved]').inner_text()
   await page.locator('#atlas-zoom-in').click()
   await page.screenshot(path=f'/mnt/data/gta6-vicebase/{tag}-detailed-map-test.png',full_page=True)
   print(tag,'scrollwidth',await page.evaluate('document.body.scrollWidth'),'inner',w,'errors',errs)
   assert await page.evaluate('document.body.scrollWidth')<=w
   assert not errs
   await page.set_content(inline_html('index.html'),wait_until='domcontentloaded')
   assert await page.locator('.hero').evaluate('(el)=>getComputedStyle(el).backgroundImage.includes("rockstargames.com")')
   await page.screenshot(path=f'/mnt/data/gta6-vicebase/{tag}-poster-test.png',full_page=True)
   print(tag,'poster style verified')
   await page.close()
  await b.close()
asyncio.run(main())

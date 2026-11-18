import asyncio,base64,pathlib
from playwright.async_api import async_playwright
SITE=pathlib.Path('/mnt/data/gta6-vicebase/site')
css=(SITE/'assets/styles.css').read_text().replace("@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700;800;900&family=DM+Sans:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap');",'')
svg=base64.b64encode((SITE/'assets/vice-skyline.svg').read_bytes()).decode()
css=css.replace("url('vice-skyline.svg')",f"url('data:image/svg+xml;base64,{svg}')")
js=(SITE/'assets/app.js').read_text()
def contents(path):
 s=(SITE/path).read_text()
 return s.replace('<link rel="stylesheet" href="/assets/styles.css">','<style>'+css+'</style>').replace('<script defer src="/assets/app.js"></script>','')
async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage','--disable-background-networking'])
  for name,w,h in [('desktop',1365,900),('mobile',390,844)]:
   page=await browser.new_page(viewport={'width':w,'height':h},device_scale_factor=1)
   page.set_default_timeout(7000)
   errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
   await page.set_content(contents('index.html'),wait_until='domcontentloaded',timeout=10000)
   await page.evaluate(js)
   await page.screenshot(path=f'/mnt/data/gta6-vicebase/{name}-current.png',full_page=True,animations='disabled',timeout=20000)
   print(name,'home',await page.locator('h1').inner_text(),'body overflow?',await page.evaluate('document.body.scrollWidth>innerWidth'))
   if name=='mobile':
    print('OFFENDERS',await page.evaluate('Array.from(document.querySelectorAll("*")).filter(e=>e.getBoundingClientRect().right>window.innerWidth+1).slice(0,20).map(e=>[e.tagName,e.className,e.getBoundingClientRect().right])'))
   if name=='mobile':
    await page.locator('#mobile-menu').click();print('mobile menu visible?',await page.locator('#nav-links').evaluate('(e)=>e.classList.contains("open")'))
   await page.set_content(contents('guides/index.html'),wait_until='domcontentloaded',timeout=10000)
   await page.evaluate(js)
   await page.locator('#guide-list-search').fill('SSD')
   print(name,'filter SSD',await page.locator('[data-guide-card]:not(.hidden)').count())
   await page.set_content(contents('tools/index.html'),wait_until='domcontentloaded',timeout=10000)
   await page.evaluate(js)
   await page.locator('#storage-free').fill('100');await page.locator('#storage-check').click()
   print(name,'storage',await page.locator('#storage-result strong').inner_text())
   await page.locator('#download-check').click();print(name,'download',await page.locator('#download-result strong').inner_text())
   print(name,'js errors',errors)
   await page.close()
  await browser.close()
asyncio.run(main())

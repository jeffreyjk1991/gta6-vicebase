import asyncio,mimetypes
from pathlib import Path
from urllib.parse import urlsplit
from playwright.async_api import async_playwright
ROOT=Path('/mnt/data/gta6-vicebase/site')
async def serve(route):
    u=urlsplit(route.request.url)
    if u.hostname!='gtasix.test':
        await route.abort();return
    target=ROOT/u.path.lstrip('/')
    if u.path.endswith('/'):target=target/'index.html'
    if not target.is_file():
        await route.fulfill(status=404,body='Not found: '+u.path);return
    await route.fulfill(status=200,content_type=mimetypes.guess_type(str(target))[0] or 'text/html',body=target.read_bytes())
async def main():
    async with async_playwright() as p:
      browser=await p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
      for tag,width,height in [('desktop',1440,900),('mobile',390,844)]:
        page=await browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
        errors=[]
        page.on('pageerror',lambda e:errors.append(str(e)))
        # use local http server for browser QA
        await page.goto('http://127.0.0.1:8765/',wait_until='load')
        await page.screenshot(path=f'/mnt/data/gta6-vicebase/{tag}-homepage-map.png',full_page=True)
        print(tag,'home h1',repr(await page.locator('h1').first.inner_text()),'horizontal overflow',await page.evaluate('document.body.scrollWidth > window.innerWidth'))
        await page.goto('http://127.0.0.1:8765/map/',wait_until='load')
        await page.wait_for_timeout(250)
        print(tag,'map title',await page.title(),'pins',await page.locator('.atlas-pin').count(),'results',await page.locator('.atlas-result').count())
        await page.screenshot(path=f'/mnt/data/gta6-vicebase/{tag}-map.png',full_page=True)
        print(tag,'map scroll width:',await page.evaluate('document.body.scrollWidth'),'viewport:',width,'errors',errors)
        await page.locator('#atlas-query').fill('vice city')
        await page.wait_for_timeout(100)
        print(tag,'query results',await page.locator('.atlas-result').count())
        assert await page.locator('.atlas-result').count()>0
        await page.locator('#atlas-query').fill('')
        await page.locator('[data-atlas-filter="region"]').click()
        print(tag,'region filtered',await page.locator('.atlas-result').count())
        assert await page.locator('.atlas-result').count()==6
        await page.locator('.atlas-result').first.click()
        assert await page.locator('#atlas-detail').is_visible()
        print(tag,'selected',await page.locator('#atlas-detail-title').inner_text())
        await page.locator('#atlas-bookmark').click()
        assert '1 place' in await page.locator('[data-atlas-saved]').inner_text()
        await page.reload()
        assert '1 place' in await page.locator('[data-atlas-saved]').inner_text()
        await page.locator('#atlas-zoom-in').click()
        tr=await page.locator('#atlas-world').get_attribute('style')
        print(tag,'zoomed style',tr[:95])
        assert await page.evaluate('document.body.scrollWidth <= window.innerWidth')
        await page.close()
      await browser.close()
asyncio.run(main())

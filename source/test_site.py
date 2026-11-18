import asyncio, mimetypes
from pathlib import Path
from urllib.parse import urlsplit
from playwright.async_api import async_playwright
ROOT=Path('/mnt/data/gta6-vicebase/site')
async def serve(route):
    url=urlsplit(route.request.url)
    if url.hostname!='vicebase.test':
        await route.abort();return
    path=url.path
    target=(ROOT/path.lstrip('/'))
    if path.endswith('/'):target=target/'index.html'
    if not target.is_file():
        await route.fulfill(status=404,body='Missing');return
    typ=mimetypes.guess_type(str(target))[0] or 'text/html'
    await route.fulfill(status=200,content_type=typ,body=target.read_bytes())
async def main():
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        errors=[]
        for title,width,height in [('desktop',1440,900),('mobile',390,844)]:
            page=await browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
            await page.route('**/*',serve)
            page.on('pageerror',lambda exc:errors.append(str(exc)))
            await page.goto('https://vicebase.test/',wait_until='load',timeout=20000)
            await page.screenshot(path=f'/mnt/data/gta6-vicebase/{title}.png',full_page=True)
            print(title, 'title',await page.title(),'scrollHeight',await page.evaluate('document.body.scrollHeight'),'scrollWidth',await page.evaluate('document.body.scrollWidth'))
            inp=page.locator('.site-search').first
            await inp.fill('SSD');await page.wait_for_timeout(200)
            print('search',await page.locator('.search-item').count())
            await page.goto('https://vicebase.test/tools/',wait_until='load',timeout=20000)
            await page.locator('#storage-free').fill('100');await page.locator('#storage-check').click()
            print('storage',await page.locator('#storage-result strong').inner_text())
            await page.locator('#download-check').click()
            print('download',await page.locator('#download-result strong').inner_text())
            await page.goto('https://vicebase.test/guides/gta-6-download-size-ps5-xbox/',wait_until='load',timeout=20000)
            print('guide',await page.locator('h1').inner_text(), 'faqs',await page.locator('.faq').count())
            await page.close()
        print('JS ERRORS:',errors)
        await browser.close()
asyncio.run(main())

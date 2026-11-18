import asyncio,base64,re
from pathlib import Path
from playwright.async_api import async_playwright
ROOT=Path('/mnt/data/gta6-vicebase/site')

def inline_html(path):
    html=(ROOT/path).read_text()
    for f in ('styles.css','map.css'):
        css=(ROOT/'assets'/f).read_text()
        css=css.split('\n',1)[1] if css.startswith('@import') else css
        svg=(ROOT/'assets'/'vice-skyline.svg').read_bytes()
        css=css.replace("url('vice-skyline.svg')", "url('data:image/svg+xml;base64,"+base64.b64encode(svg).decode()+"')")
        html=html.replace(f'<link rel="stylesheet" href="/assets/{f}">','<style>'+css+'</style>')
    atlas='data:image/svg+xml;base64,'+base64.b64encode((ROOT/'assets'/'leonida-concept.svg').read_bytes()).decode()
    html=html.replace('src="/assets/leonida-concept.svg"',f'src="{atlas}"')
    scripts=[]
    for f in ('app.js','map.js'):
        tag=f'<script defer src="/assets/{f}"></script>'
        if tag in html:
            html=html.replace(tag,'')
            scripts.append('<script>'+(ROOT/'assets'/f).read_text()+'</script>')
    html=html.replace('</body>',''.join(scripts)+'</body>')
    return html

async def main():
    async with async_playwright() as p:
        browser=await p.chromium.launch(headless=True,executable_path='/usr/bin/chromium',args=['--no-sandbox'])
        for tag,width,height in [('desktop',1440,900),('mobile',390,844)]:
            page=await browser.new_page(viewport={'width':width,'height':height})
            errors=[];page.on('pageerror',lambda err:errors.append(str(err)))
            await page.set_content(inline_html('index.html'),wait_until='load')
            await page.screenshot(path=f'/mnt/data/gta6-vicebase/{tag}-homepage-map.png',full_page=True)
            print(tag,'home h1',repr(await page.locator('h1').first.inner_text()),'width',await page.evaluate('document.body.scrollWidth'))
            await page.set_content(inline_html('map/index.html'),wait_until='load')
            await page.wait_for_timeout(250)
            print(tag,'map title',await page.title(),'pins',await page.locator('.atlas-pin').count(),'results',await page.locator('.atlas-result').count(),'width',await page.evaluate('document.body.scrollWidth'))
            await page.screenshot(path=f'/mnt/data/gta6-vicebase/{tag}-map.png',full_page=True)
            assert await page.locator('.atlas-pin').count()==24
            await page.locator('#atlas-query').fill('vice city')
            print(tag,'query',await page.locator('.atlas-result').count())
            assert await page.locator('.atlas-result').count()>0
            await page.locator('#atlas-query').fill('')
            await page.locator('[data-atlas-filter="region"]').click()
            assert await page.locator('.atlas-result').count()==6
            await page.locator('.atlas-result').first.click()
            assert await page.locator('#atlas-detail').is_visible()
            await page.locator('#atlas-bookmark').click()
            print(tag,'saved',await page.locator('[data-atlas-saved]').inner_text())
            await page.locator('#atlas-zoom-in').click()
            assert await page.evaluate('document.body.scrollWidth <= window.innerWidth')
            print(tag,'page errors',errors)
            assert not errors,errors
            await page.close()
        await browser.close()
asyncio.run(main())

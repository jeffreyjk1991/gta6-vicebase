"""Browser regression for shared map-coordinate transform, mobile menu & cast pages."""
import asyncio, math, base64, json
from pathlib import Path
from playwright.async_api import async_playwright

ROOT=Path('/mnt/data/gta6-vicebase')
ASSET=(ROOT/'site/assets/leonida-concept.svg').read_bytes()
IMAGE='data:image/svg+xml;base64,'+base64.b64encode(ASSET).decode('ascii')
fixture=[{'id':'gtadb-ocean','title':'Ocean View Hotel','subtitle':'Ocean Beach / Vice City','cat':'hotel','x':3619.44,'y':2820.98}]
fixture += [{'id':'gtadb-'+str(i),'title':'Community Place '+str(i),'subtitle':'Leonida','cat':'landmark','x':400+115*i,'y':400+135*i} for i in range(34)]

def inline_page(relative_path):
 s=(ROOT/'site'/relative_path).read_text()
 for css in ('styles.css','map.css','characters.css'):
  tag=f'<link rel="stylesheet" href="/assets/{css}">'
  if tag in s:
   content=(ROOT/'site/assets'/css).read_text()
   if content.startswith('@import'):content=content.split('\n',1)[1]
   content=content.replace("url('vice-skyline.svg')",f"url('{IMAGE}')")
   s=s.replace(tag,'<style>'+content+'</style>')
 s=s.replace('src="/assets/leonida-concept.svg"',f'src="{IMAGE}"')
 chunks=[]
 for jsname in ('app.js','map.js','characters.js'):
  tag=f'<script defer src="/assets/{jsname}"></script>'
  if tag in s:
   s=s.replace(tag,'')
   code=(ROOT/'site/assets'/jsname).read_text()
   if jsname=='map.js':
    code=code.replace('https://gtami.com/assets/img/karta-gta-6-gtami-full-4096.jpg',IMAGE)
    code=code.replace('https://gtami.com/assets/img/karta-gta-6-gtami-full-8192.jpg',IMAGE)
    code=code.replace("'/assets/leonida-concept.svg'","'"+IMAGE+"'")
   chunks.append('<script>'+code+'</script>')
 mock='<script>window.fetch=(url)=>Promise.resolve({ok:true,json:async()=>'+json.dumps(fixture)+'});</script>'
 return s.replace('</body>',mock+''.join(chunks)+'</body>')

def center(box): return (box['x']+box['width']/2,box['y']+box['height']/2)

async def main():
 async with async_playwright() as p:
  browser=await p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
  for kind,width,height in [('desktop',1440,900),('mobile',390,844),('smallmobile',360,740)]:
   page=await browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
   errors=[]
   page.on('pageerror',lambda e:errors.append(str(e)))
   await page.set_content(inline_page('map/index.html'),wait_until='domcontentloaded')
   await page.locator('[data-atlas-count]').wait_for(state='visible')
   await page.wait_for_timeout(350)
   assert await page.evaluate('document.getElementById("atlas-pins").parentElement.id')=='atlas-world','pins must share transformed world'
   assert await page.locator('.atlas-result').count()>=30
   if width<=750:
    btn=page.locator('#mobile-menu');b=await btn.bounding_box()
    assert b is not None and abs((b['x']+b['width'])-width)<33,(kind,'menu misplaced',b,width)
    await btn.click()
    nav=page.locator('#nav-links')
    assert await nav.is_visible(),'mobile menu not visible'
    n=await nav.bounding_box()
    assert n['x']+n['width']>width-26 and n['x']>=-1,('mobile dropdown misplaced',n,width)
    assert await nav.locator('a[href="/characters/"]').count()==1
    await btn.click()
    assert not await nav.is_visible(),'mobile menu failed to close'
   await page.locator('#atlas-query').fill('Ocean View Hotel')
   await page.locator('.atlas-result').first.click()
   await page.wait_for_timeout(520)
   await page.locator('#atlas-viewport').scroll_into_view_if_needed()
   assert await page.locator('#atlas-detail').is_visible()
   pin=page.locator('.atlas-pin.is-active').first
   assert await pin.count()>0,('selected pin invisible',kind)
   img=await page.locator('#atlas-base').bounding_box()
   pb=await pin.bounding_box()
   scale=img['width']/4096
   # GTADB data measured using original image coordinate system.
   expected_x=img['x']+3619.44*scale
   expected_y=img['y']+2820.98*scale
   px,py=center(pb)
   assert abs(px-expected_x)<12 and abs(py-expected_y)<12,('initial pin geometry mismatch',kind,(px,py),(expected_x,expected_y),scale)
   viewport=await page.locator('#atlas-viewport').bounding_box()
   startx=viewport['x']+min(90,viewport['width']*.23)
   starty=viewport['y']+min(210,viewport['height']*.55)
   if kind!='desktop': print('DEBUG drag target',kind,viewport,await page.evaluate('([x,y])=>{let e=document.elementFromPoint(x,y);return e?e.outerHTML.slice(0,200):null}',[startx,starty]))
   await page.mouse.move(startx,starty)
   await page.mouse.down()
   await page.mouse.move(startx+68,starty+49,steps=7)
   await page.wait_for_timeout(170)
   during_img=await page.locator('#atlas-base').bounding_box()
   during_pin=await pin.bounding_box()
   await page.mouse.up()
   image_dx=during_img['x']-img['x'];image_dy=during_img['y']-img['y']
   pin_dx=center(during_pin)[0]-px;pin_dy=center(during_pin)[1]-py
   assert abs(image_dx-pin_dx)<3 and abs(image_dy-pin_dy)<3,('pin detached from image drag',kind,(image_dx,image_dy),(pin_dx,pin_dy))
   assert abs(image_dx)>15 and abs(image_dy)>15,('drag not registered',kind,(image_dx,image_dy))
   await page.locator('#atlas-zoom-in').click()
   await page.wait_for_timeout(200)
   img2=await page.locator('#atlas-base').bounding_box();pin2=await pin.bounding_box()
   scale2=img2['width']/4096
   ex2=img2['x']+3619.44*scale2;ey2=img2['y']+2820.98*scale2
   assert abs(center(pin2)[0]-ex2)<12 and abs(center(pin2)[1]-ey2)<12,('zoom caused pin drift',kind)
   await page.locator('#atlas-concept').click()
   await page.wait_for_timeout(220)
   assert await page.locator('#atlas-status').inner_text()=='CONCEPT / UNOFFICIAL'
   assert await page.locator('.atlas-pin').count()>0
   assert await page.evaluate('document.documentElement.scrollWidth')<=width+1,(kind,'overflow on map')
   # Home menu and character discovery links.
   await page.set_content(inline_page('index.html'),wait_until='domcontentloaded')
   assert await page.locator('#people-of-leonida .cast-card').count()==4
   assert await page.locator('a[href="/characters/"]').count()>0
   assert await page.evaluate('document.documentElement.scrollWidth')<=width+1,(kind,'overflow on home')
   await page.set_content(inline_page('characters/index.html'),wait_until='domcontentloaded')
   assert await page.locator('[data-character-card]').count()==8
   await page.locator('[data-character-filter="lead"]').click()
   assert await page.locator('[data-character-card]:visible').count()==2,(kind,'filter not working')
   await page.locator('[data-character-filter="all"]').click()
   await page.locator('#characters-search').fill('Real Dimez')
   assert await page.locator('[data-character-card]:visible').count()==1,(kind,'search not working')
   await page.locator('#characters-search').fill('')
   await page.set_content(inline_page('characters/lucia-caminos/index.html'),wait_until='domcontentloaded')
   assert (await page.locator('h1').first.inner_text()).lower()=='lucia caminos'
   assert await page.locator('.cast-faq').count()==3
   assert await page.evaluate('document.documentElement.scrollWidth')<=width+1,(kind,'overflow on character')
   print('PASS',kind,'pin follows map drag:',round(image_dx,1),round(image_dy,1),'zoom anchor error:',round(center(pin2)[0]-ex2,2),'mobile menu:',width<=750,'console errors:',errors)
   assert not errors,errors
   await page.set_content(inline_page('characters/index.html'),wait_until='domcontentloaded')
   await page.screenshot(path=str(ROOT/(f'{kind}-characters.png')),full_page=True)
   await page.set_content(inline_page('map/index.html'),wait_until='domcontentloaded')
   await page.wait_for_timeout(500)
   await page.screenshot(path=str(ROOT/(f'{kind}-map-fixed.png')),full_page=True)
   await page.close()
  await browser.close()

if __name__=='__main__': asyncio.run(main())

from PIL import Image,ImageDraw,ImageFont,ImageEnhance
import cairosvg,io
from pathlib import Path
root=Path(__file__).resolve().parent.parent/'site'/'assets'
base=Image.open(io.BytesIO(cairosvg.svg2png(url=str(root/'vice-skyline.svg'),output_width=1200,output_height=790))).convert('RGB').crop((0,80,1200,710)).convert('RGBA')
# left-hand dark gradient for legibility
layer=Image.new('RGBA',base.size,(0,0,0,0))
p=layer.load()
for x in range(1200):
 alpha=int(226 * (1-max(0,(x-300)/900))**1.25)
 for y in range(630): p[x,y]=(9,10,19,max(10,alpha))
base=Image.alpha_composite(base,layer)
d=ImageDraw.Draw(base)
font='/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf'
small='/usr/share/fonts/truetype/clear-sans/ClearSans-Bold.ttf'
fs=ImageFont.truetype(font,100);sub=ImageFont.truetype(small,33);tag=ImageFont.truetype(small,25)
d.text((65,75),'GTASIX.TECH',font=sub,fill='#ffb5b8')
d.line([(66,130),(390,130)],fill='#fe8eac',width=4)
d.text((56,200),'OWN THE',font=fs,fill='white',stroke_width=1)
d.text((56,300),'STREETS.',font=fs,fill='#f69eae')
d.text((64,450),'GTA VI  /  GUIDES  /  TOOLS  /  VIDEOS',font=tag,fill='#f9e9e7')
d.text((65,495),'An independent field guide for Leonida.',font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',24),fill='#d4cbd7')
base.convert('RGB').save(root/'og-cover.png',optimize=True)
print(root/'og-cover.png')

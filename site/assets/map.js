/* ViceBase GTA 6 map: GTADB/YANIS CC BY 4.0 community reconstruction + original concept map.
 * The game map has not been independently verified building-by-building. This is not
 * a Rockstar asset or a guaranteed in-game map. Map imagery processed by GTAMI.
 */
'use strict';
(() => {
  const host=document.getElementById('atlas');
  const dataNode=document.getElementById('atlas-data');
  if(!host||!dataNode)return;
  const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>Array.from(r.querySelectorAll(s));
  const vp=$('#atlas-viewport'),world=$('#atlas-world'),base=$('#atlas-base'),pinLayer=$('#atlas-pins'),list=$('#atlas-results'),search=$('#atlas-query');
  const concept=JSON.parse(dataNode.textContent||'[]').map(p=>({...p,kind:'concept',cat:p.cat==='city'?'landmark':p.cat==='coast'?'nature':p.cat==='routes'?'transport':p.cat}));
  const assets={low:'https://gtami.com/assets/img/karta-gta-6-gtami-full-4096.jpg',high:'https://gtami.com/assets/img/karta-gta-6-gtami-full-8192.jpg',concept:'/assets/leonida-concept.svg'};
  const modes={detailed:{w:4096,h:5698},concept:{w:1400,h:1000}};
  const regionFocus={
    'vice-city':[3170,2890],'leonida-keys':[1980,5060],'grassrivers':[1900,4130],
    'port-gellhorn':[1080,2210],'ambrosia':[1740,2530],'mount-kalaga':[2100,1150]
  };
  const names={hotel:'HOTELS & STAYS',shop:'SHOPS & SERVICES',transport:'TRANSPORT',food:'FOOD & NIGHTLIFE',nature:'NATURE',landmark:'LANDMARKS',region:'ROCKSTAR-NAMED REGION',custom:'PERSONAL PIN'};
  let community=[],personal=[],mode='detailed',filterMode='all',query='',selected=null;
  let W=4096,H=5698,scale=1,x=0,y=0,fitScale=.1,zoomFrame=0,addPin=false,pinAt=null,imageLoaded=false,highLoaded=false;
  const bookmarks=new Set();
  try{const v=JSON.parse(localStorage.getItem('vicebase-atlas-bookmarks-v1')||'[]');if(Array.isArray(v))v.filter(q=>typeof q==='string').forEach(q=>bookmarks.add(q));}catch{}
  try{const v=JSON.parse(localStorage.getItem('vicebase-private-pins-v1')||'[]');if(Array.isArray(v))personal=v.filter(p=>p&&typeof p.title==='string'&&Number.isFinite(p.x)&&Number.isFinite(p.y)).slice(0,150).map(p=>({...p,kind:'custom',cat:'custom'}));}catch{}
  function save(){try{localStorage.setItem('vicebase-atlas-bookmarks-v1',JSON.stringify([...bookmarks]));localStorage.setItem('vicebase-private-pins-v1',JSON.stringify(personal));}catch{}}
  function clamp(v,a,b){return Math.min(b,Math.max(a,v));}
  function items(){return mode==='concept'?concept:community.concat(personal);}
  function match(p){const cat=filterMode==='all'||filterMode===p.cat||p.cat==='custom';const text=(!query||(p.title+' '+(p.subtitle||'')+' '+(p.description||'')).toLowerCase().includes(query));return cat&&text;}
  function visibleItems(){return items().filter(match);}
  function updateSaved(){const v=$('[data-atlas-saved]');if(v)v.textContent=bookmarks.size+' saved place'+(bookmarks.size===1?'':'s')+' / '+personal.length+' personal pin'+(personal.length===1?'':'s');}
  function pxToWorld(px,py){return {x:(px-x)/scale,y:(py-y)/scale};}
  function position(){world.style.transform=`translate3d(${x}px,${y}px,0) scale(${scale})`;const hud=$('#atlas-zoom-readout');if(hud)hud.textContent='ZOOM '+(scale/fitScale).toFixed(1)+'X / '+(mode==='concept'?'ILLUSTRATED':'COMMUNITY MAP');schedulePins();maybeUpgradeImage();}
  function schedulePins(){if(zoomFrame)return;zoomFrame=requestAnimationFrame(()=>{zoomFrame=0;drawPins();});}
  function recenter(wx,wy,nextScale=scale){scale=clamp(nextScale,fitScale*.8,mode==='detailed'?2.1:3.5);x=vp.clientWidth/2-wx*scale;y=vp.clientHeight/2-wy*scale;position();}
  function reset(){fitScale=Math.max(.018,Math.min((vp.clientWidth-16)/W,(vp.clientHeight-16)/H));recenter(W/2,H/2,fitScale*(mode==='detailed'?1.04:1.1));}
  function zoom(factor,px=vp.clientWidth/2,py=vp.clientHeight/2){const next=clamp(scale*factor,fitScale*.8,mode==='detailed'?2.1:3.5);const ref=pxToWorld(px,py);scale=next;x=px-ref.x*scale;y=py-ref.y*scale;position();}
  function focusItem(item){const target=mode==='detailed'?Math.max(scale,fitScale*4):Math.max(scale,.78);recenter(item.x,item.y,target);}
  function focusRegion(slug){const pos=mode==='concept'?concept.find(p=>p.id===slug):null;const focus=mode==='concept'?[pos?.x||700,pos?.y||500]:regionFocus[slug];if(!focus)return;recenter(focus[0],focus[1],Math.max(scale,fitScale*3.3));if(pos)showDetail(pos,false);vp.scrollIntoView({block:'nearest',behavior:'smooth'});}
  function maybeUpgradeImage(){if(mode!=='detailed'||highLoaded||scale<=fitScale*3.3||!imageLoaded)return;highLoaded=true;const img=new Image();img.onload=()=>{if(mode==='detailed')base.src=assets.high;};img.onerror=()=>{highLoaded=false;};img.src=assets.high;}
  function activateMode(next,reason=''){
    if(next===mode&&imageLoaded)return;
    closeDetail();mode=next;
    const m=modes[mode];W=m.w;H=m.h;world.style.width=W+'px';world.style.height=H+'px';
    $('#atlas-detailed').classList.toggle('selected',mode==='detailed');$('#atlas-concept').classList.toggle('selected',mode==='concept');
    $('#atlas-detailed').setAttribute('aria-pressed',String(mode==='detailed'));$('#atlas-concept').setAttribute('aria-pressed',String(mode==='concept'));
    $('#atlas-hud-sub').textContent=mode==='detailed'?'YANIS COMMUNITY MAP / CC BY 4.0':'ORIGINAL VICEBASE CONCEPT ATLAS';
    $('#atlas-status').textContent=mode==='detailed'?'COMMUNITY / UNOFFICIAL':'CONCEPT / UNOFFICIAL';
    if(mode==='concept'){
      base.src=assets.concept;imageLoaded=true;
      $('#atlas-data-note').textContent=reason||'Original schematic: 6 confirmed region names, 18 illustrative discovery themes. Not street accurate.';
      setTimeout(()=>{if(mode==='concept'){$('#atlas-hint').textContent='24 EDITORIAL MARKERS / DRAG TO EXPLORE';}},0);
    }else{
      imageLoaded=false;
      $('#atlas-data-note').textContent='Community-mapped buildings and places. Names and positions remain unverified in game.';
      $('#atlas-hint').textContent='DRAG TO PAN / SCROLL OR PINCH TO ZOOM';
      const probe=new Image();probe.onload=()=>{if(mode==='detailed'){base.src=assets.low;imageLoaded=true;maybeUpgradeImage();}};
      probe.onerror=()=>{if(mode==='detailed')activateMode('concept','The detailed image could not load. Showing our offline concept atlas; try again when online.');};
      probe.src=assets.low;
    }
    query='';search.value='';filterMode='all';filterButtons();reset();drawList();
  }
  function filterButtons(){$$('[data-atlas-filter]').forEach(btn=>{const on=btn.dataset.atlasFilter===filterMode;btn.classList.toggle('is-selected',on);btn.setAttribute('aria-pressed',String(on));const cat=btn.dataset.atlasFilter;const count=cat==='all'?items().length:items().filter(i=>i.cat===cat).length;const tag=btn.querySelector('[data-filter-count]');if(tag)tag.textContent=String(count);});}
  function closeDetail(){selected=null;$('#atlas-detail').hidden=true;$('#atlas-pin-form').hidden=true;}
  function showDetail(item,focus=true){
    selected=item;
    $('#atlas-detail-label').textContent=item.kind==='custom'?'PRIVATE PIN / YOUR NOTES':item.kind==='community'?'COMMUNITY ESTIMATE / GTADB':item.official?'ROCKSTAR-NAMED REGION':'EDITORIAL CONCEPT MARKER';
    $('#atlas-detail-title').textContent=item.title;
    $('#atlas-detail-copy').textContent=item.kind==='community'?((item.subtitle||'')+'. This position and name are reconstructed by the GTA VI mapping community, not verified against the released game. Building access or interiors are unknown.'):item.kind==='custom'?'Your private map marker. It is stored only in this browser.':item.description+' Map position is an illustration, not a confirmed coordinate.';
    $('#atlas-detail-source').href=item.kind==='community'?'https://map.gtadb.org/':item.kind==='custom'?'https://gtami.com/en/official-map/':(item.source||'https://www.rockstargames.com/VI');
    $('#atlas-detail-source').textContent=item.kind==='community'?'GTADB SOURCE ↗':item.kind==='custom'?'MAP IMAGE SOURCE ↗':'ROCKSTAR SOURCE ↗';
    $('#atlas-delete-custom').hidden=item.kind!=='custom';
    const btn=$('#atlas-bookmark');btn.textContent=bookmarks.has(item.id)?'SAVED / REMOVE':'SAVE PLACE';btn.setAttribute('aria-pressed',String(bookmarks.has(item.id)));
    $('#atlas-pin-form').hidden=true;$('#atlas-detail').hidden=false;
    if(focus)focusItem(item);
    drawList();schedulePins();
  }
  function drawList(){
    const matches=visibleItems();list.replaceChildren();
    const frag=document.createDocumentFragment();
    matches.slice(0,100).forEach(item=>{
      const btn=document.createElement('button');btn.type='button';btn.className='atlas-result'+(selected?.id===item.id?' is-active':'');btn.dataset.atlasId=item.id;
      const glyph=document.createElement('span');glyph.className='atlas-result-glyph '+item.cat;glyph.textContent=item.cat==='custom'?'★':item.kind==='concept'&&item.official?'◆':'●';
      const copy=document.createElement('span');copy.className='atlas-result-copy';const strong=document.createElement('strong');strong.textContent=item.title;const sub=document.createElement('small');sub.textContent=item.kind==='community'?(item.subtitle||names[item.cat]):item.kind==='custom'?'YOUR PRIVATE PIN':item.official?'OFFICIAL REGION NAME':'CONCEPT MARKER';copy.append(strong,sub);
      const star=document.createElement('span');star.className='atlas-result-star';star.textContent=bookmarks.has(item.id)?'★':'↗';btn.append(glyph,copy,star);btn.addEventListener('click',()=>showDetail(item));frag.append(btn);
    });list.append(frag);
    if(matches.length>100){const p=document.createElement('p');p.className='atlas-no-results';p.textContent='Showing first 100 of '+matches.length+' places. Search a name to narrow the list.';list.append(p);}
    if(!matches.length){const p=document.createElement('p');p.className='atlas-no-results';p.textContent='No places found. Try another name or a different filter.';list.append(p);}
    $('[data-atlas-count]').textContent=matches.length+' PLACES';updateSaved();schedulePins();
  }
  function drawPins(){
    if(!vp.clientWidth)return;
    const selectedItems=visibleItems();const vw=vp.clientWidth,vh=vp.clientHeight;
    const nearby=selectedItems.filter(item=>{const sx=x+item.x*scale,sy=y+item.y*scale;return sx>-60&&sx<vw+60&&sy>-60&&sy<vh+60;});
    const step=mode==='concept'?44:(scale<fitScale*3?55:scale<fitScale*7?42:30);
    const cells=new Map();
    for(const item of nearby){
      let sx=x+item.x*scale,sy=y+item.y*scale;
      const key=Math.floor(sx/step)+':'+Math.floor(sy/step);
      if(!cells.has(key))cells.set(key,{item,sx,sy,count:1});else cells.get(key).count++;
    }
    pinLayer.replaceChildren();const frag=document.createDocumentFragment();let rendered=0;
    for(const cell of cells.values()){
      if(rendered++>170)break;
      const {item,sx,sy,count}=cell;
      const btn=document.createElement('button');btn.type='button';btn.className='atlas-pin '+item.cat+(item.kind==='community'?' community':item.kind==='custom'?' custom':item.official?' official':' illustrative')+(selected?.id===item.id?' is-active':'');
      btn.style.left=sx+'px';btn.style.top=sy+'px';btn.title=count>1?count+' community locations (zoom in)':item.title;btn.setAttribute('aria-label',count>1?'Zoom into '+count+' locations':'Open '+item.title);
      const dot=document.createElement('span');dot.className='atlas-pin-dot';dot.textContent=count>1?String(Math.min(count,99)):(item.official?'◆':'•');
      const label=document.createElement('span');label.className='atlas-pin-label';label.textContent=item.title.toUpperCase();btn.append(dot,label);
      if(count>1){btn.classList.add('atlas-cluster');btn.addEventListener('click',e=>{e.stopPropagation();zoom(1.65,sx,sy);});}
      else btn.addEventListener('click',e=>{e.stopPropagation();showDetail(item);});
      frag.append(btn);
    }
    pinLayer.append(frag);
  }
  function showPinForm(pos){pinAt=pos;$('#atlas-detail').hidden=true;$('#atlas-pin-form').hidden=false;$('#atlas-pin-name').value='';$('#atlas-pin-name').focus();addPin=false;$('#atlas-add').classList.remove('selected');$('#atlas-hint').textContent='YOUR PIN WILL ONLY BE SAVED IN THIS BROWSER';}
  $$('#atlas-detailed').forEach(b=>b.addEventListener('click',()=>activateMode('detailed')));
  $('#atlas-concept').addEventListener('click',()=>activateMode('concept'));
  $$('[data-atlas-filter]').forEach(btn=>btn.addEventListener('click',()=>{filterMode=btn.dataset.atlasFilter;filterButtons();drawList();}));
  search.addEventListener('input',()=>{query=search.value.trim().toLowerCase();drawList();});
  $$('#atlas-clear').forEach(b=>b.addEventListener('click',()=>{bookmarks.clear();personal=[];save();drawList();closeDetail();}));
  $('#atlas-close-detail').addEventListener('click',closeDetail);
  $('#atlas-bookmark').addEventListener('click',()=>{if(!selected)return;bookmarks.has(selected.id)?bookmarks.delete(selected.id):bookmarks.add(selected.id);save();showDetail(selected,false);});
  $('#atlas-delete-custom').addEventListener('click',()=>{if(!selected||selected.kind!=='custom')return;personal=personal.filter(p=>p.id!==selected.id);bookmarks.delete(selected.id);save();closeDetail();drawList();});
  $$('[data-jump]').forEach(btn=>btn.addEventListener('click',()=>focusRegion(btn.dataset.jump)));
  $('#atlas-zoom-in').addEventListener('click',()=>zoom(1.6));$('#atlas-zoom-out').addEventListener('click',()=>zoom(1/1.6));$('#atlas-reset').addEventListener('click',()=>{closeDetail();reset();});
  $('#atlas-add').addEventListener('click',()=>{addPin=!addPin;$('#atlas-add').classList.toggle('selected',addPin);$('#atlas-hint').textContent=addPin?'TAP ANY STREET OR BUILDING TO ADD YOUR PRIVATE PIN':'DRAG TO PAN / SCROLL OR PINCH TO ZOOM';});
  $('#atlas-pin-cancel').addEventListener('click',()=>{$('#atlas-pin-form').hidden=true;});
  $('#atlas-pin-form').addEventListener('submit',e=>{e.preventDefault();const title=$('#atlas-pin-name').value.trim().slice(0,70);if(!title||!pinAt)return;const item={id:'private-'+Date.now(),title,subtitle:'Personal map annotation',description:'Your own marked spot.',x:clamp(pinAt.x,0,W),y:clamp(pinAt.y,0,H),cat:'custom',kind:'custom'};personal.push(item);save();$('#atlas-pin-form').hidden=true;filterMode='all';filterButtons();showDetail(item,false);});
  vp.addEventListener('wheel',e=>{e.preventDefault();const r=vp.getBoundingClientRect();zoom(e.deltaY<0?1.23:1/1.23,e.clientX-r.left,e.clientY-r.top);},{passive:false});
  const points=new Map();let drag=null,pinchDist=null,moved=false;
  vp.addEventListener('pointerdown',e=>{if(e.target.closest('button'))return;vp.setPointerCapture(e.pointerId);points.set(e.pointerId,{x:e.clientX,y:e.clientY});if(points.size===1){drag={startX:e.clientX,startY:e.clientY,x,y};moved=false;vp.classList.add('grabbing');}else{drag=null;const arr=[...points.values()];pinchDist=Math.hypot(arr[0].x-arr[1].x,arr[0].y-arr[1].y);}});
  vp.addEventListener('pointermove',e=>{if(!points.has(e.pointerId))return;points.set(e.pointerId,{x:e.clientX,y:e.clientY});if(points.size===2){const arr=[...points.values()],d=Math.hypot(arr[0].x-arr[1].x,arr[0].y-arr[1].y);if(pinchDist){const r=vp.getBoundingClientRect();zoom(d/pinchDist,(arr[0].x+arr[1].x)/2-r.left,(arr[0].y+arr[1].y)/2-r.top);}pinchDist=d;moved=true;}else if(drag){if(Math.hypot(e.clientX-drag.startX,e.clientY-drag.startY)>6)moved=true;x=drag.x+e.clientX-drag.startX;y=drag.y+e.clientY-drag.startY;position();}});
  function pointerEnd(e){if(points.has(e.pointerId)&&!moved&&addPin){const r=vp.getBoundingClientRect();showPinForm(pxToWorld(e.clientX-r.left,e.clientY-r.top));}points.delete(e.pointerId);drag=null;pinchDist=null;vp.classList.remove('grabbing');}
  vp.addEventListener('pointerup',pointerEnd);vp.addEventListener('pointercancel',pointerEnd);vp.addEventListener('lostpointercapture',e=>{points.delete(e.pointerId);drag=null;pinchDist=null;vp.classList.remove('grabbing');});
  vp.addEventListener('keydown',e=>{if(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown','+','-','Escape','0'].includes(e.key))e.preventDefault();if(e.key==='ArrowLeft')x+=70;else if(e.key==='ArrowRight')x-=70;else if(e.key==='ArrowUp')y+=70;else if(e.key==='ArrowDown')y-=70;else if(e.key==='+')zoom(1.25);else if(e.key==='-')zoom(.8);else if(e.key==='0')reset();else if(e.key==='Escape')closeDetail();position();});
  document.addEventListener('keydown',e=>{if(e.key==='/'&&!['INPUT','TEXTAREA','SELECT'].includes(document.activeElement?.tagName||'')){e.preventDefault();search.focus();}});
  const tinyFallback=[
    {id:'gtadb-oceanview',title:'Ocean View Hotel',subtitle:'Ocean Beach / Vice City',cat:'hotel',x:3654,y:2799,kind:'community'},
    {id:'gtadb-albany',title:'Albany Hotel',subtitle:'Vice Beach',cat:'hotel',x:3654,y:2428,kind:'community'},
    {id:'gtadb-yvice',title:'Y Vice City',subtitle:'Vice Beach',cat:'hotel',x:3653,y:2508,kind:'community'}
  ];
  async function loadCommunity(){
    try{const res=await fetch('/assets/gtadb-landmarks.json',{cache:'force-cache'});if(!res.ok)throw new Error('Map source data unavailable');const raw=await res.json();if(!Array.isArray(raw)||raw.length<20)throw new Error('Map data invalid');
      community=raw.filter(v=>Number.isFinite(v.x)&&Number.isFinite(v.y)&&typeof v.title==='string').map(v=>({...v,kind:'community'}));
      $('#atlas-data-note').textContent=community.length.toLocaleString()+' GTADB/YANIS community-mapped places · pre-release estimate';
    }catch(err){community=tinyFallback;$('#atlas-data-note').textContent='Detailed community place list unavailable. Explore the map, or open the original GTADB source.';}
    $('#atlas-total-badge').innerHTML=community.length.toLocaleString()+' <small>COMMUNITY LOCATIONS</small>';filterButtons();drawList();
  }
  activateMode('detailed');loadCommunity();
  let width=vp.clientWidth;
  window.addEventListener('resize',()=>{if(Math.abs(vp.clientWidth-width)>45){width=vp.clientWidth;reset();}});
})();

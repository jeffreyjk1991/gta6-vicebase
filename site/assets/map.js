'use strict';
(()=>{
  const root=document.getElementById('atlas');
  const dataNode=document.getElementById('atlas-data');
  if(!root||!dataNode)return;
  const items=JSON.parse(dataNode.textContent||'[]');
  const $=(s,r=document)=>r.querySelector(s);
  const $$=(s,r=document)=>Array.from(r.querySelectorAll(s));
  const viewport=$('#atlas-viewport'),world=$('#atlas-world'),pinLayer=$('#atlas-pins'),list=$('#atlas-results');
  const q=$('#atlas-query');
  const W=1400,H=1000;
  let scale=1,x=0,y=0,active='all',query='',selected=null;
  const bookmarks=new Set();
  try{const old=JSON.parse(localStorage.getItem('vicebase-atlas-bookmarks-v1')||'[]');if(Array.isArray(old))old.filter(v=>typeof v==='string').forEach(v=>bookmarks.add(v));}catch{}
  const names={region:'OFFICIAL REGION',city:'CITY & CULTURE',coast:'COASTS & WATER',nature:'WILDERNESS',routes:'ROADS & ROUTES'};
  const pinNodes=new Map();
  function persist(){try{localStorage.setItem('vicebase-atlas-bookmarks-v1',JSON.stringify([...bookmarks]));}catch{}}
  function displaySaved(){const node=$('[data-atlas-saved]');if(node)node.textContent=bookmarks.size+' place'+(bookmarks.size===1?'':'s')+' saved';}
  function clamp(v,a,b){return Math.min(b,Math.max(a,v));}
  function position(){world.style.transform=`translate3d(${x}px,${y}px,0) scale(${scale})`;}
  function recenterWorld(worldX,worldY,nextScale=scale){
    scale=clamp(nextScale,.28,2.7);
    x=viewport.clientWidth/2-worldX*scale;
    y=viewport.clientHeight/2-worldY*scale;
    position();
  }
  function reset(){
    const narrow=window.matchMedia('(max-width: 760px)').matches;
    const base=Math.min((viewport.clientWidth-10)/W,(viewport.clientHeight-10)/H);
    scale=narrow?Math.max(.56,base*1.9):clamp(base*1.2,.46,1.25);
    recenterWorld(narrow?885:720,narrow?635:505,scale);
  }
  function zoom(factor,px=viewport.clientWidth/2,py=viewport.clientHeight/2){
    const prev=scale,ns=clamp(scale*factor,.28,2.7);
    if(ns===prev)return;
    const ax=(px-x)/prev,ay=(py-y)/prev;
    scale=ns;x=px-ax*scale;y=py-ay*scale;position();
  }
  function focusPin(item){
    const goal=Math.max(scale,window.innerWidth<760?.80:.86);
    recenterWorld(item.x,item.y,goal);
  }
  function match(item){
    return (active==='all'||item.cat===active) && (query===''||(item.title+' '+item.subtitle+' '+item.description+' '+(items.find(x=>x.id===item.region)?.title||'')).toLowerCase().includes(query));
  }
  function closeDetail(){selected=null;$('#atlas-detail').hidden=true;$$('.atlas-pin.is-active').forEach(el=>el.classList.remove('is-active'));$$('.atlas-result.is-active').forEach(el=>el.classList.remove('is-active'));}
  function showDetail(item,shouldFocus=true){
    selected=item;
    const detail=$('#atlas-detail');
    $('#atlas-detail-title').textContent=item.title;
    $('#atlas-detail-label').textContent=item.official?'OFFICIALLY NAMED BY ROCKSTAR':'ILLUSTRATIVE EXPLORATION IDEA';
    $('#atlas-detail-copy').textContent=item.description+' '+(item.official?'The map placement is an approximation.':'This point is symbolic, not a verified in-game coordinate.');
    const src=$('#atlas-detail-source');src.href=item.source;
    const b=$('#atlas-bookmark');const saved=bookmarks.has(item.id);b.textContent=saved?'SAVED - REMOVE':'SAVE PLACE';b.setAttribute('aria-pressed',String(saved));
    detail.hidden=false;
    $$('.atlas-pin.is-active').forEach(el=>el.classList.remove('is-active'));
    pinNodes.get(item.id)?.classList.add('is-active');
    $$('.atlas-result').forEach(el=>el.classList.toggle('is-active',el.dataset.atlasId===item.id));
    if(shouldFocus)focusPin(item);
  }
  function makePins(){
    items.forEach(item=>{
      const btn=document.createElement('button');btn.type='button';btn.className='atlas-pin '+item.cat+(item.official?' official':' illustrative');
      btn.style.left=(item.x/W*100)+'%';btn.style.top=(item.y/H*100)+'%';
      btn.setAttribute('aria-label','Open '+item.title+(item.official?', officially named region':', illustrative pin'));
      btn.title=item.title;
      const dot=document.createElement('span');dot.className='atlas-pin-dot';dot.textContent=item.official?'◆':'•';
      const lbl=document.createElement('span');lbl.className='atlas-pin-label';lbl.textContent=item.title.toUpperCase();
      btn.append(dot,lbl);btn.addEventListener('click',()=>showDetail(item));
      pinLayer.append(btn);pinNodes.set(item.id,btn);
    });
  }
  function drawList(){
    let count=0;list.replaceChildren();
    items.filter(match).forEach(item=>{
      count++;
      const btn=document.createElement('button');btn.type='button';btn.className='atlas-result'+(selected?.id===item.id?' is-active':'');btn.dataset.atlasId=item.id;
      const icon=document.createElement('span');icon.className='atlas-result-glyph '+item.cat;icon.textContent=item.official?'◆':'●';
      const copy=document.createElement('span');copy.className='atlas-result-copy';
      const name=document.createElement('strong');name.textContent=item.title;
      const sub=document.createElement('small');sub.textContent=item.official?'ROCKSTAR-NAMED REGION':names[item.cat]+' / CONCEPT';
      copy.append(name,sub);const star=document.createElement('span');star.className='atlas-result-star';star.textContent=bookmarks.has(item.id)?'★':'↗';
      btn.append(icon,copy,star);btn.addEventListener('click',()=>showDetail(item));list.append(btn);
    });
    if(!count){const p=document.createElement('p');p.className='atlas-no-results';p.textContent='No matching locations. Try a broader term or reset filters.';list.append(p);}
    $$('#atlas-pins .atlas-pin').forEach(btn=>{const item=items.find(i=>pinNodes.get(i.id)===btn);btn.hidden=!(item&&match(item));});
    $('[data-atlas-count]').textContent=count+' VISIBLE';
    displaySaved();
  }
  function filter(category){active=category;$$('[data-atlas-filter]').forEach(btn=>{const b=btn.dataset.atlasFilter===category;btn.classList.toggle('is-selected',b);btn.setAttribute('aria-pressed',String(b));});drawList();}
  makePins();
  $$('.atlas-filter').forEach(btn=>{const key=btn.dataset.atlasFilter;const node=$(`[data-filter-count="${key}"]`,btn);if(node)node.textContent=key==='all'?items.length:items.filter(i=>i.cat===key).length;btn.addEventListener('click',()=>filter(key));});
  q.addEventListener('input',()=>{query=q.value.trim().toLowerCase();drawList();});
  $('#atlas-clear').addEventListener('click',()=>{bookmarks.clear();persist();displaySaved();drawList();if(selected)showDetail(selected,false);});
  $('#atlas-close-detail').addEventListener('click',closeDetail);
  $('#atlas-bookmark').addEventListener('click',()=>{if(!selected)return;if(bookmarks.has(selected.id))bookmarks.delete(selected.id);else bookmarks.add(selected.id);persist();displaySaved();drawList();showDetail(selected,false);});
  $$('[data-jump]').forEach(btn=>btn.addEventListener('click',()=>{const item=items.find(i=>i.id===btn.dataset.jump);if(item){query='';q.value='';filter('all');showDetail(item);viewport.scrollIntoView({block:'center',behavior:'smooth'});}}));
  $('#atlas-zoom-in').addEventListener('click',()=>zoom(1.3));
  $('#atlas-zoom-out').addEventListener('click',()=>zoom(1/1.3));
  $('#atlas-reset').addEventListener('click',()=>{closeDetail();reset();});
  viewport.addEventListener('wheel',event=>{event.preventDefault();const rect=viewport.getBoundingClientRect();zoom(event.deltaY<0?1.12:1/1.12,event.clientX-rect.left,event.clientY-rect.top);},{passive:false});
  const pointers=new Map();let drag=null,pinchDistance=null;
  viewport.addEventListener('pointerdown',e=>{
    if(e.target.closest('button'))return;
    viewport.setPointerCapture(e.pointerId);pointers.set(e.pointerId,{x:e.clientX,y:e.clientY});
    if(pointers.size===1){drag={startX:e.clientX,startY:e.clientY,x,y};viewport.classList.add('grabbing');}
    if(pointers.size===2){const p=[...pointers.values()];pinchDistance=Math.hypot(p[0].x-p[1].x,p[0].y-p[1].y);drag=null;}
  });
  viewport.addEventListener('pointermove',e=>{
    if(!pointers.has(e.pointerId))return;
    pointers.set(e.pointerId,{x:e.clientX,y:e.clientY});
    if(pointers.size===2){
      const p=[...pointers.values()],distance=Math.hypot(p[0].x-p[1].x,p[0].y-p[1].y);
      if(pinchDistance){const rect=viewport.getBoundingClientRect();zoom(distance/pinchDistance,(p[0].x+p[1].x)/2-rect.left,(p[0].y+p[1].y)/2-rect.top);}pinchDistance=distance;
    }else if(drag){x=drag.x+e.clientX-drag.startX;y=drag.y+e.clientY-drag.startY;position();}
  });
  function release(e){pointers.delete(e.pointerId);drag=null;pinchDistance=null;viewport.classList.remove('grabbing');}
  viewport.addEventListener('pointerup',release);viewport.addEventListener('pointercancel',release);viewport.addEventListener('lostpointercapture',release);
  viewport.addEventListener('keydown',e=>{if(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown','+','-','Escape','0'].includes(e.key))e.preventDefault();if(e.key==='ArrowLeft')x+=60;if(e.key==='ArrowRight')x-=60;if(e.key==='ArrowUp')y+=60;if(e.key==='ArrowDown')y-=60;if(e.key==='+')zoom(1.2);if(e.key==='-')zoom(1/1.2);if(e.key==='0')reset();if(e.key==='Escape')closeDetail();position();});
  document.addEventListener('keydown',e=>{if(e.key==='/'&&!['INPUT','TEXTAREA','SELECT'].includes(document.activeElement.tagName)){e.preventDefault();q.focus();}});
  drawList();reset();
  let width=viewport.clientWidth;
  window.addEventListener('resize',()=>{if(Math.abs(viewport.clientWidth-width)>60){width=viewport.clientWidth;reset();}});
})();

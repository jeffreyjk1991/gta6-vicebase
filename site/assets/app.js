'use strict';
(()=>{
  const $=(selector,root=document)=>root.querySelector(selector);
  const $$=(selector,root=document)=>Array.from(root.querySelectorAll(selector));
  // Replace stale preload copy once the official launch date has arrived.
  if(Date.now()>=Date.parse('2026-11-19T05:00:00Z')){
    const strip=$('.topbar .wrap');if(strip){
      const heading=$('strong',strip),link=$('a',strip);
      if(heading)heading.textContent='GTA VI IS OUT NOW // NOV 19, 2026';
      if(link){link.href='/guides/gta-6-best-settings/';link.textContent='Best in-game settings';}
      for(const node of strip.childNodes)if(node.nodeType===3 && /Preload is live/.test(node.textContent))node.textContent=' Official launch-day guide · ';
    }
  }
  // Link pre-existing static pages to the current support resources.
  const legacyTools=document.querySelector('#nav-links a[href="/tools/"]');
  if(legacyTools){legacyTools.href='/gta-6-help/';legacyTools.textContent='HELP';}
  const footerTools=document.querySelector('.footer-cols a[href="/tools/"]');
  if(footerTools&&!document.querySelector('.footer-cols a[href="/gta-6-online/"]')){
    for(const [label,url] of [['GTA 6 Online','/gta-6-online/'],['GTA 6 Help','/gta-6-help/']]){
      const el=document.createElement('a');el.href=url;el.textContent=label;footerTools.insertAdjacentElement('afterend',el);
    }
  }
  const menu=$('#mobile-menu'),links=$('#nav-links');
  function setMenu(open){
    if(!menu||!links)return;
    links.classList.toggle('open',open);
    menu.setAttribute('aria-expanded',String(open));
    menu.setAttribute('aria-label',open?'Close menu':'Open menu');
  }
  menu?.addEventListener('click',()=>setMenu(!links.classList.contains('open')));
  $$('#nav-links a').forEach(a=>a.addEventListener('click',()=>setMenu(false)));
  document.addEventListener('pointerdown',e=>{if(links?.classList.contains('open')&&!links.contains(e.target)&&!menu?.contains(e.target))setMenu(false);});
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&links?.classList.contains('open')){setMenu(false);menu?.focus();}});
  window.addEventListener('resize',()=>{if(innerWidth>750&&links?.classList.contains('open'))setMenu(false);});
  // Rockstar describes a regional midnight launch. Major regional storefronts
  // typically use one release instant per *store country* (US store = 00:00 ET).
  // Do not use the viewer's wall-clock midnight for the US countdown.
  const releaseTimes={
    US:'2026-11-19T05:00:00Z',UK:'2026-11-19T00:00:00Z',
    EU:'2026-11-18T23:00:00Z',IN:'2026-11-18T18:30:00Z',
    AU:'2026-11-18T13:00:00Z',NZ:'2026-11-18T11:00:00Z',JP:'2026-11-18T15:00:00Z'
  };
  const regionInput=$('#release-region');
  const langRegion=(navigator.language||'en-US').split('-').at(-1).toUpperCase();
  const defaultRegion=({GB:'UK',IE:'UK',DE:'EU',FR:'EU',ES:'EU',IT:'EU',NL:'EU',PL:'EU',AU:'AU',NZ:'NZ',IN:'IN',JP:'JP',CA:'US',US:'US'})[langRegion]||'LOCAL';
  let chosenRegion=defaultRegion;
  try{const saved=(localStorage.getItem('gtasix-store-region')||localStorage.getItem('vicebase-store-region'));if(saved && (saved in releaseTimes || saved==='LOCAL'))chosenRegion=saved;}catch{}
  if(regionInput)regionInput.value=chosenRegion;
  const pad=n=>String(n).padStart(2,'0');
  function updateCountdown(){
    const region=regionInput?.value||chosenRegion;
    const launch=region==='LOCAL'?new Date(2026,10,19,0,0,0):new Date(releaseTimes[region]||releaseTimes.US);
    const diff=Math.max(0,launch.getTime()-Date.now()),el=$('[data-countdown]');
    const d=Math.floor(diff/86400000),hr=Math.floor(diff%86400000/3600000),m=Math.floor(diff%3600000/60000),sec=Math.floor(diff%60000/1000);
    if(el)el.textContent=diff===0?'OUT NOW':d>0?`${d}D ${hr}H TO GO`:`${hr}H ${m}M TO GO`;
    const board=$('[data-release-clock]');
    if(board){
      const set=(sel,val)=>{const node=$(sel,board);if(node)node.textContent=val;};
      set('[data-count-days]',pad(d));set('[data-count-hours]',pad(hr));set('[data-count-minutes]',pad(m));set('[data-count-seconds]',pad(sec));
      const message=$('[data-release-message]',board);
      if(message){const tm=launch.toLocaleString(undefined,{weekday:'short',month:'short',day:'numeric',hour:'numeric',minute:'2-digit',timeZoneName:'short'});
        message.textContent=diff===0?`Estimated launch time reached (${tm}). Check your console store to play.`:`Expected unlock: ${tm}. Your console store countdown is authoritative.`;
      }
      board.classList.toggle('released',diff===0);
    }
  }
  regionInput?.addEventListener('change',()=>{chosenRegion=regionInput.value;try{localStorage.setItem('gtasix-store-region',chosenRegion);}catch{}updateCountdown();});
  updateCountdown();setInterval(updateCountdown,1000);
  const buyButtons=$$('[data-buy-platform]');
  if(buyButtons.length){
    function selectPlatform(platform){buyButtons.forEach(btn=>{const active=btn.dataset.buyPlatform===platform;btn.classList.toggle('selected',active);btn.setAttribute('aria-pressed',String(active));});
      $$('[data-buy-row]').forEach(row=>{const a=$('.retailer-link',row);if(a)a.href=platform==='xbox'?row.dataset.xboxUrl:row.dataset.ps5Url;});}
    buyButtons.forEach(btn=>btn.addEventListener('click',()=>selectPlatform(btn.dataset.buyPlatform)));
    selectPlatform('ps5');
  }
  let indexPromise=null;
  function allGuides(){if(!indexPromise)indexPromise=fetch('/assets/search-index.json').then(r=>{if(!r.ok)throw new Error('Search index unavailable');return r.json();});return indexPromise;}
  const safe=(s)=>String(s||'').toLowerCase();
  const words=(s)=>safe(s).trim().split(/\s+/).filter(Boolean);
  function score(a,q){const hay=safe([a.title,a.summary,a.category,a.aliases?.join(' ')].join(' ')),title=safe(a.title);return words(q).reduce((n,w)=>n+(title.includes(w)?12:hay.includes(w)?3:-50),0)+(title.includes(safe(q))?20:0);}
  $$('.site-search').forEach(input=>{
    const container=input.closest('.search-area')||input.parentElement.parentElement;
    const results=$('.search-results',container);
    let matches=[];
    function hide(){if(results)results.classList.remove('open');}
    input.addEventListener('input',async()=>{
      const q=input.value.trim();if(q.length<2){hide();return;}
      try{
        const data=await allGuides();if(input.value.trim()!==q)return;
        matches=data.map(a=>({...a,score:score(a,q)})).filter(x=>x.score>0).sort((a,b)=>b.score-a.score).slice(0,6);
        if(results){results.replaceChildren();if(!matches.length){const p=document.createElement('p');p.className='search-empty';p.textContent='No exact guide yet. Try “storage”, “preload” or “PS5”.';results.append(p);}else{matches.forEach(a=>{const link=document.createElement('a');link.href=a.href||'/guides/'+a.slug+'/';link.className='search-item';const block=document.createElement('span'),cat=document.createElement('span'),ttl=document.createElement('span');cat.className='search-cat';cat.textContent=a.category;ttl.className='search-title';ttl.textContent=a.title;block.append(cat,ttl);link.append(block);results.append(link);});}results.classList.add('open');}
      }catch(err){hide();}
    });
    input.addEventListener('keydown',e=>{if(e.key==='Escape')hide();if(e.key==='Enter'&&matches[0]&&input.value.trim().length>=2){e.preventDefault();location.href=matches[0].href||'/guides/'+matches[0].slug+'/';}});
    document.addEventListener('click',e=>{if(!container.contains(e.target))hide();});
  });
  const searchForm=$('#search-form');searchForm?.addEventListener('submit',e=>{e.preventDefault();const q=$('.site-search',searchForm)?.value.trim()||'';location.href=q?'/guides/?q='+encodeURIComponent(q):'/guides/';});
  const listing=$('#guide-list');if(listing){const buttons=$$('[data-filter]');const cardEls=$$('[data-guide-card]');const params=new URLSearchParams(location.search);let active=params.get('category')||'all';if(!$$('[data-filter]').some(b=>b.dataset.filter===active))active='all';buttons.forEach(b=>b.classList.toggle('selected',b.dataset.filter===active));const raw=params.get('q')||'';const guideSearch=$('#guide-list-search');if(guideSearch)guideSearch.value=raw;
    function apply(){const term=safe(guideSearch?.value||'');let visible=0;cardEls.forEach(card=>{const passCat=active==='all'||card.dataset.cat===active;const passText=!term||safe(card.dataset.search).includes(term);const show=passCat&&passText;card.classList.toggle('hidden',!show);if(show)visible++;});$('#guide-count').textContent=visible+' guides';$('#guide-empty')?.classList.toggle('hidden',visible>0);}
    buttons.forEach(b=>b.addEventListener('click',()=>{active=b.dataset.filter;buttons.forEach(a=>a.classList.toggle('selected',a===b));apply();}));guideSearch?.addEventListener('input',apply);apply();
  }
  const storageBtn=$('#storage-check');if(storageBtn){function calc(){const platform=$('#storage-platform')?.value,free=Number($('#storage-free')?.value||0),needed=platform==='ps5'?212:Number($('#storage-target')?.value||212),result=$('#storage-result');if(!Number.isFinite(free)||free<0||!Number.isFinite(needed)||needed<=0){result.querySelector('strong').textContent='Enter valid values';result.querySelector('p').textContent='Use a non-negative free-space number and a positive install size.';return;}const deficit=Math.max(0,needed-free);result.querySelector('strong').textContent=deficit?'FREE '+Math.ceil(deficit)+' GB':'READY TO PRELOAD';result.querySelector('p').textContent=deficit?`You have ${free.toLocaleString()} GB free. Reserve at least ${needed.toLocaleString()} GB and allow extra room for updates.`:`You meet the ${needed.toLocaleString()} GB target. Keep additional headroom for game patches and future updates.`;}storageBtn.addEventListener('click',calc);$('#storage-platform')?.addEventListener('change',()=>{const xbox=$('#xbox-needed');if(xbox)xbox.classList.toggle('hidden',$('#storage-platform').value==='ps5');calc();});calc();}
  const downloadBtn=$('#download-check');if(downloadBtn){function calc(){const size=Number($('#download-size')?.value),speed=Number($('#download-speed')?.value),el=$('#download-result');if(size<=0||speed<=0||!Number.isFinite(size)||!Number.isFinite(speed)){el.querySelector('strong').textContent='Enter valid values';el.querySelector('p').textContent='Both size and speed must be greater than zero.';return;}const h=size*8000/speed/3600,lo=h,hi=h*1.3;const fmt=(n)=>n<1?`${Math.round(n*60)} min`:n<24?`${n.toFixed(1)} hr`:`${(n/24).toFixed(1)} days`;el.querySelector('strong').textContent=fmt(lo)+' – '+fmt(hi);el.querySelector('p').textContent='Estimated time at '+speed+' Mbps for '+size+' GB; real speeds depend on Wi‑Fi, network and platform servers.';}downloadBtn.addEventListener('click',calc);calc();}
  const checklist=$('#launch-checklist');if(checklist){const boxes=$$('input[type="checkbox"]',checklist),key='gtasix-checklist-v1';let saved=[];try{saved=JSON.parse(localStorage.getItem(key)||localStorage.getItem('vicebase-checklist-v1')||'[]');}catch{}function draw(){boxes.forEach((b,i)=>{b.checked=saved.includes(i);b.closest('.check-item')?.classList.toggle('done',b.checked);});const done=saved.length,total=boxes.length;$('#check-progress').textContent=`${done} / ${total} READY`;}boxes.forEach((b,i)=>b.addEventListener('change',()=>{saved=boxes.flatMap((x,ix)=>x.checked?[ix]:[]);try{localStorage.setItem(key,JSON.stringify(saved));}catch{}draw();}));draw();}
  $$('.copy-link').forEach(b=>b.addEventListener('click',async()=>{try{await navigator.clipboard.writeText(location.href);b.textContent='COPIED ✓';setTimeout(()=>b.textContent='COPY LINK',2000);}catch{b.textContent='Copy the URL above';}}));
  $$('.video-click').forEach(el=>el.addEventListener('click',()=>{const url=el.dataset.video;if(url)window.open(url,'_blank','noopener,noreferrer');}));
})();

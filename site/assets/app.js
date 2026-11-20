'use strict';
(()=>{
  const $=(selector,root=document)=>root.querySelector(selector);
  const $$=(selector,root=document)=>Array.from(root.querySelectorAll(selector));
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
  const buyButtons=$$('[data-buy-platform]');
  if(buyButtons.length){
    function selectPlatform(platform){buyButtons.forEach(btn=>{const active=btn.dataset.buyPlatform===platform;btn.classList.toggle('selected',active);btn.setAttribute('aria-pressed',String(active));});
      $$('[data-buy-row]').forEach(row=>{const a=$('.retailer-link',row);if(a)a.href=platform==='xbox'?row.dataset.xboxUrl:row.dataset.ps5Url;});}
    buyButtons.forEach(btn=>btn.addEventListener('click',()=>selectPlatform(btn.dataset.buyPlatform)));
    selectPlatform('ps5');
  }
  let indexPromise=null;
  function allGuides(){if(!indexPromise)indexPromise=fetch('/assets/search-index.json').then(r=>{if(!r.ok)throw new Error('Search index unavailable');return r.json();}).catch(err=>{indexPromise=null;throw err;});return indexPromise;}
  const normalize=s=>String(s||'').toLowerCase().normalize('NFKD').replace(/[\u0300-\u036f]/g,'').replace(/[’']/g,'').replace(/\bgta\s*(?:6|vi)\b/g,'gta 6').replace(/[^a-z0-9]+/g,' ').trim();
  const stopwords=new Set('a an the i im ive me my we you your it this that do does did how what where why when can could should would is are am was were be been to for in on of and or with at as please need know help not dont doesnt wont cant cannot gta 6 vi game'.split(' '));
  const wordForms=new Map(Object.entries({missions:'mission',objectives:'objective',controls:'control',settings:'setting',saves:'save',saving:'save',routes:'route',cars:'car',vehicles:'vehicle',crashes:'crash',crashing:'crash',freezes:'freeze',freezing:'freeze',driving:'drive',characters:'character',switching:'switch'}));
  const words=s=>normalize(s).split(' ').filter(Boolean).map(w=>wordForms.get(w)||w);
  const queryWords=s=>[...new Set(words(s).filter(w=>!stopwords.has(w)))];
  // Require every meaningful query word; short terms such as "car" must not match "character".
  const hasWord=(hay,word)=>hay.some(w=>w===word||(word.length>=4&&w.startsWith(word)));
  function matchesText(hay,q){
    const query=normalize(q),terms=queryWords(q);
    if(!query)return true;
    return terms.length?terms.every(w=>hasWord(words(hay),w)):/^(gta(?: 6)?|help)$/.test(query)&&normalize(hay).includes(query);
  }
  function score(a,q){
    const hay=[a.title,a.summary,a.category,a.aliases?.join(' ')].join(' ');
    if(!matchesText(hay,q))return 0;
    const title=words(a.title),terms=queryWords(q);
    return 1+terms.reduce((n,w)=>n+(hasWord(title,w)?12:3),0)+(normalize(a.title).includes(normalize(q))?20:0);
  }
  function addSearchFallback(container,message,query=''){
    container.replaceChildren();
    const p=document.createElement('p');p.className='search-empty';p.textContent=message;container.append(p);
    for(const [label,url] of [['Stuck in the game? Find your next step','/gta-6-mission-help/'],['Browse the guide library',query?'/guides/?q='+encodeURIComponent(query):'/guides/']]){
      const a=document.createElement('a');a.className='search-item';a.href=url;a.textContent=label;container.append(a);
    }
  }
  $$('.site-search').forEach(input=>{
    const container=input.closest('.search-area')||input.parentElement.parentElement;
    const results=$('.search-results',container);
    let matches=[],resolvedQuery='',request=0;
    function hide(){if(results)results.classList.remove('open');}
    input.addEventListener('input',async()=>{
      const q=input.value.trim(),current=++request;
      matches=[];resolvedQuery='';hide();results?.replaceChildren();
      if(q.length<2)return;
      try{
        const data=await allGuides();if(current!==request||input.value.trim()!==q)return;
        matches=data.map(a=>({...a,score:score(a,q)})).filter(x=>x.score>0).sort((a,b)=>b.score-a.score).slice(0,6);
        resolvedQuery=q;
        if(results){results.replaceChildren();if(!matches.length){addSearchFallback(results,'No exact guide matches yet. Try the next-step helper or browse all guides.',q);}else{matches.forEach(a=>{const link=document.createElement('a');link.href=a.href||'/guides/'+a.slug+'/';link.className='search-item';const block=document.createElement('span'),cat=document.createElement('span'),ttl=document.createElement('span');cat.className='search-cat';cat.textContent=a.category;ttl.className='search-title';ttl.textContent=a.title;block.append(cat,ttl);link.append(block);results.append(link);});}results.classList.add('open');}
      }catch(err){if(current!==request)return;matches=[];resolvedQuery='';if(results){addSearchFallback(results,'Search is temporarily unavailable. You can still use the helper or guide library.',q);results.classList.add('open');}}
    });
    input.addEventListener('keydown',e=>{if(e.key==='Escape')hide();if(e.key==='Enter'&&matches[0]&&resolvedQuery===input.value.trim()&&resolvedQuery.length>=2){e.preventDefault();location.href=matches[0].href||'/guides/'+matches[0].slug+'/';}});
    document.addEventListener('click',e=>{if(!container.contains(e.target))hide();});
  });
  const searchForm=$('#search-form');searchForm?.addEventListener('submit',e=>{e.preventDefault();const q=$('.site-search',searchForm)?.value.trim()||'';location.href=q?'/guides/?q='+encodeURIComponent(q):'/guides/';});
  const listing=$('#guide-list');if(listing){const buttons=$$('[data-filter]');const cardEls=$$('[data-guide-card]');const params=new URLSearchParams(location.search);let active=params.get('category')||'all';if(!$$('[data-filter]').some(b=>b.dataset.filter===active))active='all';buttons.forEach(b=>b.classList.toggle('selected',b.dataset.filter===active));const raw=params.get('q')||'';const guideSearch=$('#guide-list-search');if(guideSearch)guideSearch.value=raw;
    const empty=$('#guide-empty');if(empty)addSearchFallback(empty,'No guides match those filters. Try another topic, clear the filters, or get help with your next step.');
    function apply(){const term=guideSearch?.value||'';let visible=0;cardEls.forEach(card=>{const passCat=active==='all'||card.dataset.cat===active;const passText=matchesText(card.dataset.search,term);const show=passCat&&passText;card.classList.toggle('hidden',!show);if(show)visible++;});$('#guide-count').textContent=visible+' guides';empty?.classList.toggle('hidden',visible>0);}
    buttons.forEach(b=>b.addEventListener('click',()=>{active=b.dataset.filter;buttons.forEach(a=>a.classList.toggle('selected',a===b));apply();}));guideSearch?.addEventListener('input',apply);apply();
  }
  const storageBtn=$('#storage-check');if(storageBtn){function calc(){const platform=$('#storage-platform')?.value,free=Number($('#storage-free')?.value||0),needed=platform==='ps5'?212:Number($('#storage-target')?.value||212),result=$('#storage-result');if(!Number.isFinite(free)||free<0||!Number.isFinite(needed)||needed<=0){result.querySelector('strong').textContent='Enter valid values';result.querySelector('p').textContent='Use a non-negative free-space number and a positive install size.';return;}const deficit=Math.max(0,needed-free);result.querySelector('strong').textContent=deficit?'FREE '+Math.ceil(deficit)+' GB':'ENOUGH SPACE TO INSTALL';result.querySelector('p').textContent=deficit?`You have ${free.toLocaleString()} GB free. Reserve at least ${needed.toLocaleString()} GB and allow extra room for updates.`:`You meet the ${needed.toLocaleString()} GB target. Keep additional headroom for game patches and future updates.`;}storageBtn.addEventListener('click',calc);$('#storage-platform')?.addEventListener('change',()=>{const xbox=$('#xbox-needed');if(xbox)xbox.classList.toggle('hidden',$('#storage-platform').value==='ps5');calc();});calc();}
  const downloadBtn=$('#download-check');if(downloadBtn){function calc(){const size=Number($('#download-size')?.value),speed=Number($('#download-speed')?.value),el=$('#download-result');if(size<=0||speed<=0||!Number.isFinite(size)||!Number.isFinite(speed)){el.querySelector('strong').textContent='Enter valid values';el.querySelector('p').textContent='Both size and speed must be greater than zero.';return;}const h=size*8000/speed/3600,lo=h,hi=h*1.3;const fmt=(n)=>n<1?`${Math.round(n*60)} min`:n<24?`${n.toFixed(1)} hr`:`${(n/24).toFixed(1)} days`;el.querySelector('strong').textContent=fmt(lo)+' – '+fmt(hi);el.querySelector('p').textContent='Estimated time at '+speed+' Mbps for '+size+' GB; real speeds depend on Wi‑Fi, network and platform servers.';}downloadBtn.addEventListener('click',calc);calc();}
  const checklist=$('#launch-checklist');if(checklist){const boxes=$$('input[type="checkbox"]',checklist),key='gtasix-checklist-v1';let saved=[];try{saved=JSON.parse(localStorage.getItem(key)||localStorage.getItem('vicebase-checklist-v1')||'[]');}catch{}function draw(){boxes.forEach((b,i)=>{b.checked=saved.includes(i);b.closest('.check-item')?.classList.toggle('done',b.checked);});const done=saved.length,total=boxes.length;$('#check-progress').textContent=`${done} / ${total} READY`;}boxes.forEach((b,i)=>b.addEventListener('change',()=>{saved=boxes.flatMap((x,ix)=>x.checked?[ix]:[]);try{localStorage.setItem(key,JSON.stringify(saved));}catch{}draw();}));draw();}
  $$('.copy-link').forEach(b=>b.addEventListener('click',async()=>{try{await navigator.clipboard.writeText(location.href);b.textContent='COPIED ✓';setTimeout(()=>b.textContent='COPY LINK',2000);}catch{b.textContent='Copy the URL above';}}));
  $$('.video-click').forEach(el=>el.addEventListener('click',()=>{const url=el.dataset.video;if(url)window.open(url,'_blank','noopener,noreferrer');}));
})();

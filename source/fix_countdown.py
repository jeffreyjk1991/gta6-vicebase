from pathlib import Path
root=Path('/mnt/data/gta6-vicebase')
p=root/'source/build.py';s=p.read_text()
old='<span data-release-zone>YOUR LOCAL TIME</span>'
new='''<label class="release-select-label" for="release-region">STORE REGION</label><select id="release-region" class="release-region" aria-label="Choose store region for countdown"><option value="US">US / CANADA</option><option value="UK">UK / IRELAND</option><option value="EU">CENTRAL EUROPE</option><option value="IN">INDIA</option><option value="AU">AUSTRALIA (SYDNEY)</option><option value="NZ">NEW ZEALAND</option><option value="JP">JAPAN</option><option value="LOCAL">OTHER / LOCAL MIDNIGHT</option></select>'''
assert old in s;s=s.replace(old,new)
s=s.replace('Unlocks November 19 at midnight in your local time zone.','Store-region estimate. Confirm the unlock time in your console store.')
s=s.replace('NOV 19 · MIDNIGHT LOCAL','NOV 19 · STORE-REGION UNLOCK')
p.write_text(s)

p=root/'site/assets/app.js';s=p.read_text()
start=s.index('  const launch=new Date(2026,10,19,0,0,0);')
end=s.index('  const buyButtons=$$',start)
new_js='''  // Rockstar describes a regional midnight launch. Major regional storefronts
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
  try{const saved=localStorage.getItem('gtasix-store-region');if(saved && (saved in releaseTimes || saved==='LOCAL'))chosenRegion=saved;}catch{}
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
'''
s=s[:start]+new_js+s[end:]
p.write_text(s)
p=root/'site/assets/styles.css';s=p.read_text();s+='''\n/* Store-region-specific launch clock (US listings use Eastern midnight) */\n.countdown-heading{flex-wrap:wrap}.release-select-label{font:700 9px 'Space Mono',monospace;letter-spacing:.04em;margin-left:auto;color:#b6a8be}.release-region{border:1px solid #775771;background:#251d30;border-radius:5px;color:#ffe4d9;padding:5px 7px;font:700 10px 'Space Mono',monospace;max-width:190px}.release-region:focus{outline:2px solid #ff9c9c}.countdown-board p{line-height:1.5}@media(max-width:520px){.release-select-label{margin-left:0}.release-region{max-width:100%;flex:1;min-width:140px;font-size:9px}}\n''';p.write_text(s)
p=root/'README.md';s=p.read_text().replace('a live local-midnight launch countdown','a live store-region-selectable release countdown');p.write_text(s)
print('Updated countdown for regional stores and selection.')

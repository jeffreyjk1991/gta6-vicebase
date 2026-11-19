'use strict';
(() => {
  const root=document.getElementById('settings-finder');if(!root)return;
  const platform=document.getElementById('settings-platform');
  const goal=document.getElementById('settings-goal');
  const results=document.getElementById('settings-results');
  const title=document.getElementById('settings-profile-title');
  const desc=document.getElementById('settings-profile-desc');
  const copy=document.getElementById('settings-copy');
  const platforms={ps5:'PLAYSTATION 5',pro:'PS5 PRO',xbox:'XBOX SERIES X|S'};
  const descriptions={
    balanced:'A practical starting point for story missions, chases and exploration.',
    combat:'Quicker camera response and assisted targeting for firefights.',
    driving:'Readable roads and a more stable chase camera.',
    cinematic:'Atmosphere and immersion over the most minimal interface.',
    comfort:'Reduce camera motion and make controls and text easier to follow.'
  };
  const sets={
    balanced:[
      ['Motion Blur Strength','Display','0','Cut down visual smearing when turning.'],
      ['Targeting','Gameplay → Combat','Partial','Aim nudges toward a target without full lock-on.'],
      ['Aim Assist Strength','Gameplay → Combat','4','An approachable starting value; tune down for challenge.'],
      ['Look / Aim Sensitivity','Controller','7 / 7','Start close to the menu baseline, then adjust gradually.'],
      ['Movement Speed','Gameplay → Movement','Run','Faster movement through the city.'],
      ['Camera Shake','Camera → Comfort','Off','Keeps chases and shootouts visually calmer.'],
      ['Minimap','UI → Navigation','Always On','See turnoffs and objectives while learning Leonida.'],
      ['HDR Calibration','Display','Calibrate','Match peak brightness to your HDR TV, if supported.']
    ],
    combat:[
      ['Targeting','Gameplay → Combat','Partial or Lock-On','Use Lock-On for easier missions; Partial for more control.'],
      ['Aim Assist Strength','Gameplay → Combat','4–5','Raise it only if target acquisition feels difficult.'],
      ['Look / Aim Sensitivity','Controller','9 / 8','Try quicker look movement without overshooting your aim.'],
      ['Aim Response Curve','Controller','Standard','A predictable baseline; experiment only after familiarizing yourself.'],
      ['Quick Draw','Gameplay → Combat','On','Useful if you want faster reactions in encounters.'],
      ['Motion Blur Strength','Display','0','Keep moving targets easier to track.'],
      ['Camera Shake','Camera → Comfort','Off','Avoid added camera movement during gunfire.'],
      ['Minimap','UI → Navigation','Always On','Keep location context in a fight.']
    ],
    driving:[
      ['Vehicle Camera Height','Camera → Land & Water Vehicles','Medium / Higher','A little more road visibility can help in traffic.'],
      ['Camera Follow Speed','Camera → Land & Water Vehicles','Medium','Test whether recentering is comfortable around corners.'],
      ['Motion Blur Strength','Display','0','Sharper scenery during fast turns.'],
      ['Cinematic Vehicle Crash Frequency','Camera → Cinematic','Low','Fewer forced cinematic interruptions.'],
      ['Look Sensitivity','Controller','7–9','Comfortable side checks during maneuvers.'],
      ['Minimap','UI → Navigation','Always On','See upcoming turns in chases.'],
      ['Camera Shake','Camera → Comfort','Off','Less visual bounce after collisions.'],
      ['GPS Voice','Audio','On','Helpful when watching the road rather than the map.']
    ],
    cinematic:[
      ['Motion Blur Strength','Display','2–3','Preserve some motion softness if you prefer it.'],
      ['Camera Shake','Camera → Comfort','On','Adds impact during action. Turn off if uncomfortable.'],
      ['Cinematic Kill Shot Frequency','Camera → Cinematic','Default','Retain more cinematic interruptions if you enjoy them.'],
      ['Minimap','UI → Navigation','Dynamic','Enjoy a cleaner screen when not navigating.'],
      ['HDR Calibration','Display','Calibrate','Tune highlights and night scenes for your display.'],
      ['Camera Height','Camera → On Foot','Medium','A neutral framing for walking and exploration.'],
      ['Subtitles','UI → Subtitles & Captions','Optional','Turn on if dialogue is hard to catch.'],
      ['Vehicle Radio','Audio','On','Keep the in-world radio experience.']
    ],
    comfort:[
      ['Motion Blur Strength','Display','0','Remove the in-game blur effect.'],
      ['Camera Shake','Camera → Comfort','Off','Avoid jarring shaking.'],
      ['Camera Bob','Camera → Comfort','0–2','Lower head-bob motion.'],
      ['Weapon Sway','Camera → Comfort','Off','Reduce movement while aiming.'],
      ['Persistent Center Dot','UI → Reticle','On','A fixed visual reference can ease motion discomfort.'],
      ['Player / Hit Effects Intensity','Display','Low','Reduce distracting visual effects.'],
      ['Subtitles','UI → Subtitles & Captions','On','Follow dialogue without relying only on audio.'],
      ['UI Text Size','UI → Scaling & Readability','Larger','Improve legibility from the couch.']
    ]
  };
  const extra={
    ps5:['Adaptive Triggers Resistance','Controller → DualSense','Weak / Off','Reduce fatigue during long sessions; preference only.'],
    pro:['PS5 Pro visuals','Console / game','Automatic','Rockstar confirms PSSR clarity and ray-traced shadows; not a 60 FPS toggle.'],
    xbox:['Auto Low-Latency Mode','Xbox settings → TV & display','On (if supported)','Use the TV gaming input for lower display latency.']
  };
  let current=[];
  function render(){
    const g=sets[goal.value]?goal.value:'balanced';
    const p=platforms[platform.value]?platform.value:'ps5';
    const items=[...sets[g],extra[p]];
    current=items;
    title.textContent=goal.options[goal.selectedIndex].text.toUpperCase()+' / '+platforms[p];
    desc.textContent=descriptions[g]+' Suggested values, not Rockstar defaults.';
    results.replaceChildren();
    for(const [name,path,value,why] of items){
      const card=document.createElement('div');card.className='settings-rec';
      const top=document.createElement('div');top.className='settings-rec-top';
      const h=document.createElement('h3');h.textContent=name;
      const val=document.createElement('span');val.className='settings-rec-value';val.textContent=value;
      top.append(h,val);
      const where=document.createElement('div');where.className='settings-rec-path';where.textContent=path;
      const note=document.createElement('p');note.textContent=why;
      card.append(top,where,note);results.append(card);
    }
    const url=new URL(location.href);
    url.searchParams.set('platform',p);url.searchParams.set('style',g);
    try{history.replaceState(null,'',url.pathname+url.search+url.hash);}catch{}
    copy.textContent='COPY MY PRESET ↗';
  }
  const params=new URLSearchParams(location.search);
  if(platforms[params.get('platform')])platform.value=params.get('platform');
  if(sets[params.get('style')])goal.value=params.get('style');
  platform.addEventListener('change',render);goal.addEventListener('change',render);
  copy.addEventListener('click',async()=>{
    const lines=[title.textContent,'GTASIX editorial starting points — confirm options in your copy of GTA VI.','',...current.map(x=>x[0]+': '+x[2]+' ('+x[1]+')'),'',location.href];
    const value=lines.join('\n');
    try{
      if(navigator.clipboard&&window.isSecureContext)await navigator.clipboard.writeText(value);
      else{const ta=document.createElement('textarea');ta.value=value;ta.style.position='fixed';ta.style.opacity='0';document.body.append(ta);ta.select();const ok=document.execCommand('copy');ta.remove();if(!ok)throw Error('copy unavailable');}
      copy.textContent='COPIED ✓';
    }catch{copy.textContent='COPY UNAVAILABLE';}
  });
  render();
})();

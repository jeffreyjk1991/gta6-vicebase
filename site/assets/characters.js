'use strict';
(() => {
  const root=document.querySelector('#character-directory');
  if(!root)return;
  const buttons=[...root.querySelectorAll('[data-character-filter]')];
  const cards=[...root.querySelectorAll('[data-character-card]')];
  const search=root.querySelector('#characters-search');
  const count=root.querySelector('#characters-count');
  const empty=root.querySelector('#characters-empty');
  let selected='all';
  function update(){
    const q=(search?.value||'').trim().toLowerCase();let n=0;
    cards.forEach(card=>{
      const category=card.dataset.characterGroup;
      const searchable=card.dataset.characterSearch||'';
      const show=(selected==='all'||category===selected)&&(!q||searchable.includes(q));
      card.hidden=!show;if(show)n++;
    });
    if(count)count.textContent=n+' OF '+cards.length+' CHARACTER FILES';
    if(empty)empty.hidden=n>0;
    buttons.forEach(btn=>{const on=btn.dataset.characterFilter===selected;btn.classList.toggle('selected',on);btn.setAttribute('aria-pressed',String(on));});
  }
  buttons.forEach(btn=>btn.addEventListener('click',()=>{selected=btn.dataset.characterFilter;update();}));
  search?.addEventListener('input',update);
  update();
})();

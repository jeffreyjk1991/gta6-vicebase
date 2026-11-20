'use strict';
(()=>{
const finder=document.getElementById('help-results');if(!finder)return;
const platform=document.getElementById('help-platform');
const issue=document.getElementById('help-issue');
const error=document.getElementById('help-error');
const title=document.getElementById('help-results-title');
const context=document.getElementById('help-results-context');
const guide=document.getElementById('help-guide');
const official=document.getElementById('help-official');
const copy=document.getElementById('help-copy');
const psg='https://www.playstation.com/en-us/support/games/game-launch-issues/';
const xbox='https://support.xbox.com/help/errors/error-code-search-guide';
const data={
crash:{name:'Crashing or freezing',guide:'/guides/gta-6-crashing-freezing-ps5-xbox/',note:'Player reports exist; no universal fix is established.',shared:['Record the exact error code, the mission, and whether the entire console shuts down or just the game.','Check for a GTA VI game update and a console system update.','Close the game fully and restart the console; then try the same scene once.','If the console overheats, warns about temperature, or powers off unexpectedly, stop and contact manufacturer support.','If the fault persists at the same point, report the game version and reproducible steps to Rockstar.'],ps5:['On PS5, follow the official PlayStation game-launch troubleshooting article before using Safe Mode or reinstalling.'],xbox:['On Xbox, follow the Xbox error-code guide and note whether other games are affected.']},
loading:{name:'Stuck loading / black screen',guide:'/guides/gta-6-stuck-loading-screen-black-screen/',note:'A white-circle loading screen has been reported; its cause is not confirmed.',shared:['Allow normal loading to finish and check that the game is fully installed and updated.','If the screen remains frozen, close the game once and restart the console; do not repeatedly force shutdown while saving.','Check the display input and HDMI connection if the entire console display is black.','If one mission repeatedly locks, record its name and exact point of failure.','Use official support links for error codes rather than deleting saved-game data.'],ps5:['On PS5, PlayStation Safe Mode has Change Video Output for screen compatibility; follow Sony instructions only.'],xbox:['On Xbox, open console display settings to check the supported video mode and use Xbox support for persistent black screens.']},
locked:{name:'Game locked / will not start',guide:'/guides/gta-6-game-locked-wont-start/',note:'This can involve a license, installation or platform error; do not guess.',shared:['Sign in to the account that purchased or redeemed GTA VI and confirm the entitlement.','Check the game installation, game update and console update status.','Record the exact error code and check it on the platform support site.','Check the service-status page for a console-store outage; do not assume GTA VI Online has launched.'],ps5:['PS5: if a padlock appears, check Console Sharing and Offline Play, then Settings → Users and Accounts → Other → Restore Licenses. This does not delete saves.'],xbox:['Xbox: verify the purchased game is in Owned Games and use Microsoft Xbox installation and entitlement troubleshooting.']},
download:{name:'Download or installation stuck',guide:'/guides/gta-6-download-stuck-or-slow-ps5/',note:'Follow official queue and storage steps first.',shared:['Confirm enough free SSD space for the download and updates.','Open the console download queue and confirm it is not paused or waiting behind another download.','Check your network connection and platform service status.','Restart or resume the queue using the official console help steps.','Only consider cancelling and redownloading the game after the official guide recommends it; avoid touching saved-game data.'],ps5:['PS5: open Downloads/Uploads, use Pause and Resume, then follow Sony download troubleshooting.'],xbox:['Xbox: use My games & apps → Manage → Queue and the Microsoft installation help flow.'],officialPs:'https://www.playstation.com/en-us/support/games/troubleshoot-downloaded-playstation-game/',officialXbox:'https://support.xbox.com/help/games-apps/troubleshooting/troubleshoot-game-or-app-installation-problems-on-xbox-one'},
save:{name:'Missing save / progress not saved',guide:'/guides/gta-6-how-to-save/',note:'Do not delete cloud or local saved data during investigation.',shared:['Pause GTA VI and check Game → Load Game for all available manual slots and autosave entries.','Check your platform’s saved-data or cloud-save management page without overwriting anything.','If Save Game is greyed out, leave the active mission and retry during free roam.','Do not delete, reset, or overwrite an existing save while troubleshooting.','Record the time and mission of lost progress for Rockstar Support.'],ps5:['PS5: review console and cloud saved-data options, but avoid choosing a sync direction until you know which copy is newer.'],xbox:['Xbox: check whether a cloud sync prompt is pending; do not choose a copy blindly.']},
graphics:{name:'Blurry graphics / low FPS',guide:'/guides/gta-6-blurry-graphics-fps/',note:'Rockstar described a 30 FPS console target, not a hidden 60 FPS switch.',shared:['First confirm whether motion blur is causing streaking while turning: test Motion Blur Strength at 0.','Check your TV Game Mode, HDMI settings and HDR calibration.','Avoid claiming any menu setting unlocks 60 FPS; PS5 Pro can improve image clarity but is not a guarantee of 60 FPS.','Record whether the image looks blurry all the time or only at a specific distance or scene.','If the issue persists, note console model, display resolution and game version for support.'],ps5:['PS5: review Screen and Video settings and output resolution.'],xbox:['Xbox: review TV & display options and the supported resolution of your display.']},
audio:{name:'Audio cutting out',guide:'/guides/gta-6-audio-controller-problems/',note:'Headset audio problems have been reported but are not diagnosed here.',shared:['Check whether the problem happens through TV speakers, headset, or both.','Review the in-game Audio output and console sound format without resetting other settings.','Disconnect and reconnect the headset once, and confirm its firmware or battery status.','Fully restart GTA VI and confirm the latest available update.','Record the exact mission or moment and whether other games also have the problem.'],ps5:['PS5: check Settings → Sound and the selected Output Device.'],xbox:['Xbox: check Volume & audio output and headset pairing settings.']},
controller:{name:'Controller or vibration issues',guide:'/guides/gta-6-audio-controller-problems/',note:'Unusual controller vibration or inputs have been reported.',shared:['Test the controller in the console home interface to separate game input from hardware failure.','Check the in-game Controller / Control Scheme settings and remapped buttons.','Reduce vibration or adaptive-trigger resistance as a comfort test.','Update controller firmware through the console and reconnect it once.','If only GTA VI is affected, record the mission, controller model and game version for Rockstar Support.'],ps5:['PS5: check Accessories → Controller and DualSense firmware.'],xbox:['Xbox: check Xbox Accessories for controller firmware updates.']}
};
const hasIssue=key=>Object.prototype.hasOwnProperty.call(data,key);
function render(){
 const mode=platform.value==='xbox'?'xbox':'ps5';
 const key=hasIssue(issue.value)?issue.value:'crash';
 const d=data[key];
 let list=[...d.shared,...d[mode]];
 title.textContent=d.name;
 context.textContent=d.note+(mode==='xbox'?' Xbox Series X|S.':' PS5 / PS5 Pro.');
 finder.replaceChildren();
 for(const item of list){const li=document.createElement('li');li.textContent=item;finder.append(li);}
 guide.href=key==='download'?(mode==='xbox'?'/guides/gta-6-download-stuck-xbox/':d.guide):d.guide;
 official.href=mode==='xbox'?(d.officialXbox||xbox):(d.officialPs||psg);
 copy.textContent='COPY STEPS';
 document.getElementById('help-copy-fallback')?.remove();
 const url=new URL(location.href);url.searchParams.set('platform',mode);url.searchParams.set('issue',key);
 try{history.replaceState(null,'',url.pathname+url.search+url.hash);}catch{}
}
const params=new URLSearchParams(location.search);
if(params.get('platform')==='xbox')platform.value='xbox';
if(hasIssue(params.get('issue')))issue.value=params.get('issue');
platform.addEventListener('change',render);issue.addEventListener('change',render);
copy.addEventListener('click',async()=>{
 const code=error.value.trim().slice(0,80);
 const items=[...finder.querySelectorAll('li')].map((el,i)=>(i+1)+'. '+el.textContent);
 const message=['GTASIX GTA VI troubleshooting checklist',title.textContent,platform.value==='xbox'?'Xbox Series X|S':'PS5 / PS5 Pro',code?'Error code: '+code:'',...items,'Full guide: '+new URL(guide.getAttribute('href'),location.origin).href,'Official support: '+official.href].filter(Boolean).join('\n');
 try{await navigator.clipboard.writeText(message);document.getElementById('help-copy-fallback')?.remove();copy.textContent='COPIED ✓';}
 catch{
  document.getElementById('help-copy-fallback')?.remove();
  const panel=document.createElement('div');panel.id='help-copy-fallback';panel.className='note-box';
  const label=document.createElement('label');label.htmlFor='help-copy-text';label.textContent='Copy your checklist';
  const hint=document.createElement('p');hint.textContent='Clipboard access is unavailable. Select and copy the text below.';
  const field=document.createElement('textarea');field.id='help-copy-text';field.readOnly=true;field.rows=10;field.value=message;
  field.style.cssText='display:block;width:100%;max-width:100%;padding:12px;font-size:16px;line-height:1.5;color:inherit;background:#151525;border:1px solid #566073;border-radius:8px';
  panel.append(label,hint,field);copy.insertAdjacentElement('afterend',panel);
  field.focus();field.select();field.setSelectionRange(0,message.length);
  copy.textContent='COPY TEXT SHOWN BELOW';
 }
});
render();
})();

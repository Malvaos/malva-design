/* LionOS Settings behaviour (replaces missing script.js) */
(function(){
const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const root=document.documentElement,frame=$('#pageFrame'),main=$('.main-content');
function theme(t){if(t==='light')root.setAttribute('data-theme','light');else root.removeAttribute('data-theme');
  const dm=$('#darkModeToggle');if(dm)dm.checked=t!=='light';try{frame.contentWindow.postMessage({malvaTheme:t==='light'?'light':'dark'},'*')}catch(e){}}
function toast(m){let t=$('.toast');if(t)t.remove();t=document.createElement('div');t.className='toast';t.textContent=m;main.appendChild(t);setTimeout(()=>t.remove(),2200)}
function show(item){
  $$('.nav-item').forEach(n=>{const on=n===item;n.classList.toggle('active',on);n.setAttribute('aria-selected',on)});
  $$('.settings-section').forEach(s=>s.classList.toggle('active',s.id===item.dataset.target));
  if(item.dataset.page&&frame.getAttribute('data-src')!==item.dataset.page){frame.setAttribute('data-src',item.dataset.page);frame.src=item.dataset.page}
  main.scrollTop=0}
$$('.nav-item').forEach(n=>{n.addEventListener('click',()=>show(n));n.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();show(n)}})});
frame.addEventListener('load',()=>theme(root.getAttribute('data-theme')==='light'?'light':'dark'));
$('.search-input').addEventListener('input',e=>{const q=e.target.value.trim().toLowerCase();$$('.nav-item').forEach(n=>n.style.display=!q||n.textContent.toLowerCase().includes(q)?'':'none');$$('.nav-separator,.nav-heading').forEach(x=>x.style.display=q?'none':'')});
const dm=$('#darkModeToggle');if(dm){dm.checked=true;dm.addEventListener('change',()=>theme(dm.checked?'dark':'light'))}
const mute=$('#muteToggle');if(mute)mute.addEventListener('change',()=>{$$('#sound input[type=range]').forEach(r=>r.disabled=mute.checked);toast(mute.checked?'Silent mode on':'Silent mode off')});
const up=$('#updateBtn');if(up)up.addEventListener('click',()=>{up.disabled=true;up.textContent='Checking...';setTimeout(()=>{up.textContent='Up to date';toast('LionOS is up to date')},1500)});
const rs=$('#resetBtn');if(rs)rs.addEventListener('click',()=>toast('Reset needs administrator approval'));
$$('.wallpaper-item').forEach(w=>w.addEventListener('click',()=>{$$('.wallpaper-item').forEach(x=>x.classList.toggle('active',x===w))}));
const fab=document.createElement('button');fab.className='theme-fab';fab.title='Toggle theme';fab.setAttribute('aria-label','Toggle theme');fab.textContent='\u25d0';fab.onclick=()=>theme(root.getAttribute('data-theme')==='light'?'dark':'light');document.body.appendChild(fab);
show($('.nav-item.active')||$('.nav-item'));
})();

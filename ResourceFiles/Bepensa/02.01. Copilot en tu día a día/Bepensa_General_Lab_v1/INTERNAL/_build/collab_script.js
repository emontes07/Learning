
(function(){
  // copy buttons
  document.querySelectorAll('.copy').forEach(function(b){
    b.addEventListener('click',function(){
      var t=b.closest('.prompt').querySelector('pre').innerText;
      var done=function(){b.textContent='Copiado';b.classList.add('ok');setTimeout(function(){b.textContent='Copiar';b.classList.remove('ok')},1600)};
      if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(t).then(done,function(){fallback(t);done()})}else{fallback(t);done()}
    });
  });
  function fallback(t){var a=document.createElement('textarea');a.value=t;a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();try{document.execCommand('copy')}catch(e){}document.body.removeChild(a)}
  // nav active state
  var links={};document.querySelectorAll('nav.side a').forEach(function(a){links[a.getAttribute('href').slice(1)]=a});
  function setActive(id){Object.keys(links).forEach(function(k){links[k].classList.toggle('active',k===id)});
    var a=links[id],n=document.getElementById('sideNav');if(a&&n&&n.scrollHeight>n.clientHeight){var at=a.getBoundingClientRect().top-n.getBoundingClientRect().top+n.scrollTop;if(at<n.scrollTop+40||at>n.scrollTop+n.clientHeight-60){n.scrollTop=at-n.clientHeight/2}}}
  var targets=Array.prototype.slice.call(document.querySelectorAll('section[id],details.lab[id]'));
  var lock=0,ticking=false;
  function spy(){ticking=false;if(Date.now()<lock)return;var cur=null;for(var i=0;i<targets.length;i++){if(targets[i].getBoundingClientRect().top<=140)cur=targets[i].id;else break}
    if(!cur&&targets.length)cur=targets[0].id;setActive(cur)}
  window.addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(spy)}},{passive:true});
  spy();
  document.querySelectorAll('details.lab').forEach(function(d){d.addEventListener('toggle',function(){if(d.open){lock=Date.now()+700;setActive(d.id)}})});
  // opening a lab from nav
  document.querySelectorAll('nav.side a').forEach(function(a){a.addEventListener('click',function(){var el=document.getElementById(a.getAttribute('href').slice(1));if(el&&el.tagName==='DETAILS')el.open=true;lock=Date.now()+1200;setActive(el?el.id:'');var n=document.querySelector('nav.side');if(window.innerWidth<=960)n.classList.remove('open')})});
  if(location.hash){var el=document.getElementById(location.hash.slice(1));if(el){if(el.tagName==='DETAILS')el.open=true;setTimeout(function(){el.scrollIntoView();setActive(el.id)},60)}}
  // expand / collapse
  document.getElementById('expandAll').addEventListener('click',function(){document.querySelectorAll('details.lab').forEach(function(d){d.open=true})});
  document.getElementById('collapseAll').addEventListener('click',function(){document.querySelectorAll('details.lab').forEach(function(d){d.open=false})});
  document.getElementById('menuBtn').addEventListener('click',function(){var n=document.querySelector('nav.side');n.classList.toggle('open');this.setAttribute('aria-expanded',n.classList.contains('open'))});
  // self-check progress (saved in this browser only)
  var KEY='bepensa-colaboracion-v1',state={};try{state=JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){}
  var boxes=document.querySelectorAll('.selfcheck input');
  function refresh(){var n=0;boxes.forEach(function(b){if(b.checked)n++});var pct=boxes.length?Math.round(n*100/boxes.length):0;
    document.getElementById('progBar').style.width=pct+'%';document.getElementById('progTxt').textContent=n+' of '+boxes.length+' casillas completadas';
    document.querySelectorAll('details.lab').forEach(function(d){var bs=d.querySelectorAll('.selfcheck input');if(!bs.length)return;var all=Array.prototype.every.call(bs,function(b){return b.checked});if(links[d.id])links[d.id].classList.toggle('done',all)})}
  boxes.forEach(function(b){b.checked=!!state[b.dataset.key];b.addEventListener('change',function(){state[b.dataset.key]=b.checked;try{localStorage.setItem(KEY,JSON.stringify(state))}catch(e){}refresh()})});
  document.getElementById('resetProg').addEventListener('click',function(){state={};try{localStorage.removeItem(KEY)}catch(e){}boxes.forEach(function(b){b.checked=false});refresh()});
  refresh();
  window.addEventListener('beforeprint',function(){document.querySelectorAll('details').forEach(function(d){d.open=true})});
})();

document.querySelectorAll('.fac').forEach(function(box){var imgs=box.querySelectorAll('.fac-screen img'),btns=box.querySelectorAll('.fac-swbtn'),cap=box.querySelector('.fac-cap');btns.forEach(function(b,i){b.addEventListener('click',function(){imgs.forEach(function(x){x.classList.remove('on');});btns.forEach(function(x){x.classList.remove('on');x.setAttribute('aria-pressed','false');});imgs[i].classList.add('on');b.classList.add('on');b.setAttribute('aria-pressed','true');cap.textContent=b.getAttribute('data-cap');});});});
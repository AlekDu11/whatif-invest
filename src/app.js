/* WhatIfStack — front-end. Data: window.WI (index of all assets, from index.js),
   page config: window.PAGE, referral links: window.REF / window.REF_DEFAULT (ref.js).
   Price series are loaded on demand from /assets/p/<id>.json. */
(function(){
const WI = window.WI, PAGE = window.PAGE || {}, BASE = PAGE.base || '';
const lang = PAGE.lang || 'uk';
const $ = (s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const IDX = WI.a, BYID = Object.fromEntries(IDX.map(a=>[a.i,a]));
const REF = window.REF||{}, REF_DEFAULT = window.REF_DEFAULT||{};

const T = window.I18N || {};
const fmt = (s,o)=>String(s).replace(/\{(\w+)\}/g,(m,k)=>o[k]!=null?o[k]:m);

/* ---------- helpers ---------- */
const NAMES=PAGE.names||{};
const nm = a => (a.c==='metal'&&NAMES[a.i]) ? NAMES[a.i] : lang==='uk' ? a.n : (a.ne||a.n);
const url = id => { const a=BYID[id]; return (PAGE.full||(a&&a.o<PAGE.topn)) ? `${PAGE.prefix}/${id}/` : `${BASE}/en/${id}/` };
const esc = s => String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function fmtUsd(v){ if(v==null) return '—'; const a=Math.abs(v); let s;
  if(a>=1e9) s=(a/1e9).toFixed(2)+'B'; else if(a>=1e6) s=(a/1e6).toFixed(2)+'M'; else if(a>=1e4) s=Math.round(a).toLocaleString('en-US');
  else s=a.toLocaleString('en-US',{maximumFractionDigits:2}); return (v<0?'−$':'$')+s }
function fmtPrice(v){ if(v==null) return '—'; const d=v>=1000?2:v>=1?2:v>=0.01?4:8;
  return '$'+v.toLocaleString('en-US',{minimumFractionDigits:v>=1?2:0,maximumFractionDigits:d}) }
function fmtPct(p,dec){ if(p==null||!isFinite(p)) return '—'; const a=Math.abs(p*100);
  return (p>=0?'+':'−')+a.toLocaleString('en-US',{maximumFractionDigits:dec!=null?dec:(a>=100?0:a>=10?1:2)})+'%' }
const cls = p => p==null?'':p>=0?'good':'bad';
function hue(s){let h=0;for(const c of s)h=(h*31+c.charCodeAt(0))%360;return h}
function icon(a,big){ const c=big?' lg':'';
  if(a.l) return `<span class="ic${c}"><img src="${esc(a.l)}" alt="" loading="lazy" width="26" height="26"></span>`;
  return `<span class="ic${c}" style="background:hsl(${hue(a.t)} 55% 52%)">${esc(a.t.slice(0,2))}</span>` }
function spark(arr,w=110,h=34){ if(!arr||arr.length<2) return '';
  const mn=Math.min(...arr),mx=Math.max(...arr),r=mx-mn||1, up=arr[arr.length-1]>=arr[0];
  const pts=arr.map((v,i)=>`${(i/(arr.length-1)*w).toFixed(1)},${(h-2-(v-mn)/r*(h-4)).toFixed(1)}`).join(' ');
  return `<svg width="${w}" height="${h}" viewBox="0 0 ${w} ${h}"><polyline points="${pts}" fill="none" stroke="${up?'#14a44d':'#e5484d'}" stroke-width="1.6" stroke-linejoin="round"/></svg>` }
const goUrl=(u,extra)=>u&&u.startsWith('/go/')?`${u}?from=${encodeURIComponent(location.pathname)}&l=${lang}${extra||''}`:u;
function refFor(a){ const r=REF[a.i]||REF_DEFAULT[a.c]; return r&&r.url?Object.assign({},r,{url:goUrl(r.url)}):null }
function buyBtn(a){ const r=refFor(a); return r?`<a class="buy" href="${esc(r.url)}" target="_blank" rel="sponsored noopener" title="${esc(r.where)} · ${T.aff}">${T.buy}</a>`:'' }
window.WIX={T,nm,url,esc,fmtUsd,fmtPrice,fmtPct,cls,icon,spark,buyBtn,BYID,IDX,lang};
const bs=$('#buyslot'); if(bs&&BYID[bs.dataset.id]){ const r=refFor(BYID[bs.dataset.id]); if(r) bs.innerHTML=`<a class="btn" href="${esc(r.url)}" target="_blank" rel="sponsored noopener">${T.buy} ${esc(BYID[bs.dataset.id].t)} · ${esc(r.where)}</a>` }

/* ---------- global search (header) ---------- */
(function(){
  const inp=$('#gs'), box=$('#gres'); if(!inp) return;
  inp.placeholder=T.search; let sel=0, items=[];
  const run=()=>{ const q=inp.value.trim().toLowerCase(); if(!q){box.style.display='none';return}
    items=IDX.filter(a=>a.t.toLowerCase().startsWith(q)||nm(a).toLowerCase().includes(q))
      .sort((x,y)=>(y.t.toLowerCase()===q)-(x.t.toLowerCase()===q)||x.o-y.o).slice(0,8);
    sel=0;
    box.innerHTML=items.length?items.map((a,k)=>`<a href="${url(a.i)}" class="${k?'':'on'}">${icon(a)}<span>${esc(nm(a))} <span class="t">${esc(a.t)}</span></span><span class="t" style="margin-left:auto">${fmtPrice(a.pr)}</span></a>`).join(''):`<div class="empty">${T.nothing}</div>`;
    box.style.display='block' };
  inp.addEventListener('input',run);
  inp.addEventListener('keydown',e=>{ const ls=$$('a',box);
    if(e.key==='ArrowDown'||e.key==='ArrowUp'){e.preventDefault(); if(!ls.length) return; ls[sel].classList.remove('on'); sel=(sel+(e.key==='ArrowDown'?1:-1)+ls.length)%ls.length; ls[sel].classList.add('on')}
    if(e.key==='Enter'&&ls[sel]) location.href=ls[sel].getAttribute('href');
    if(e.key==='Escape') box.style.display='none' });
  document.addEventListener('click',e=>{ if(!e.target.closest('.gsearch')) box.style.display='none' });
})();

/* ---------- main table (home) ---------- */
(function(){
  const tb=$('#mt'); if(!tb) return;
  let tab=PAGE.tab||'all', q='', sortK=PAGE.sort||'o', sortDir=1, shown=100;
  const TABS=['all','crypto','stock','etf','metal','lead','lag'];
  $('#tabs').innerHTML=TABS.map(t=>`<button data-t="${t}" class="${t===tab?'on':''}">${T[t]}</button>`).join('')+(PAGE.wa?`<a class="tablink" href="${PAGE.wau}">🌍 ${esc(PAGE.wa)}</a>`:'');
  $$('#tabs button').forEach(b=>b.onclick=()=>{tab=b.dataset.t; $$('#tabs button').forEach(x=>x.classList.toggle('on',x===b));
    if(tab==='lead'){sortK='r5';sortDir=-1} else if(tab==='lag'){sortK='r5';sortDir=1} else if(sortK==='r5'&&(sortDir)){sortK='o';sortDir=1}
    shown=100; draw()});
  const f=$('#flt'); f.placeholder=T.filter; f.oninput=()=>{q=f.value.trim().toLowerCase(); shown=100; draw()};
  const COLS=[['n','#','l n hide-sm'],['name',T.name,'l'],['buy','',''],['pr',T.price,''],['ch',T.chg,''],['r1',T.d1,'hide-sm'],['r3',T.d3,'hide-sm'],['r5',T.d5,''],['sp',T.spark,'hide-sm'],['go','','hide-sm']];
  function draw(){
    let rows=IDX.filter(a=>{
      if(tab==='crypto'||tab==='stock'||tab==='etf'||tab==='metal'){ if(a.c!==tab) return false }
      if((tab==='lead'||tab==='lag')&&a.r5==null) return false;
      return !q||a.t.toLowerCase().includes(q)||nm(a).toLowerCase().includes(q) });
    const k=sortK==='n'?'o':sortK;
    rows.sort((x,y)=>{ const vx=k==='name'?nm(x):x[k], vy=k==='name'?nm(y):y[k];
      if(vx==null&&vy==null) return x.o-y.o; if(vx==null) return 1; if(vy==null) return -1;
      return (typeof vx==='string'?vx.localeCompare(vy):vx-vy)*sortDir });
    const total=rows.length; rows=rows.slice(0,shown);
    const split=!!$('#mt2'), top=split?rows.slice(0,10):rows, rest=split?rows.slice(10):[];
    const head='<tr>'+COLS.map(([c,l,cl])=>{ const s=(c===sortK||(c==='n'&&sortK==='o'));
      const sortable=!['buy','sp','go'].includes(c);
      return `<th class="${cl}${s?' sorted':''}" ${sortable?`data-k="${c}"`:''}>${l}${sortable&&l?`<span class="ar">${s?(sortDir>0?'↑':'↓'):'↕'}</span>`:''}</th>`}).join('')+'</tr>';
    $('#mthead').innerHTML=head; if(split) $('#mthead2').innerHTML=head;
    $$('#mthead th[data-k],#mthead2 th[data-k]').forEach(th=>th.onclick=()=>{ let kk=th.dataset.k; if(kk==='n') kk='o';
      if(sortK===kk) sortDir=-sortDir; else {sortK=kk; sortDir=(kk==='name'||kk==='o')?1:-1} draw() });
    const tr=(a,i)=>`<tr>
      <td class="l n hide-sm">${i+1}</td>
      <td class="l"><button class="star" data-s="${a.i}" aria-label="☆">☆</button><a class="asset" href="${url(a.i)}">${icon(a)}<span><span class="nm">${esc(nm(a))}</span><span class="tk">${esc(a.t)}</span></span></a></td>
      <td>${buyBtn(a)}</td>
      <td class="num">${fmtPrice(a.pr)}</td>
      <td class="num ${cls(a.ch)}">${fmtPct(a.ch)}</td>
      <td class="num hide-sm ${cls(a.r1)}">${fmtPct(a.r1)}</td>
      <td class="num hide-sm ${cls(a.r3)}">${fmtPct(a.r3)}</td>
      <td><span class="pill ${cls(a.r5)}">${fmtPct(a.r5)}</span></td>
      <td class="hide-sm">${spark(a.sp)}</td>
      <td class="hide-sm"><a class="calc" href="${url(a.i)}">${T.calc} →</a></td></tr>`;
    tb.innerHTML=top.length?top.map(tr).join(''):`<tr><td colspan="10" class="empty">${T.nothing}</td></tr>`;
    if(split){ $('#mt2').innerHTML=rest.map((a,i)=>tr(a,i+10)).join(''); $('#rank2').hidden=!rest.length;
      $('#mttop').innerHTML=total>10?`<a class="more" href="#rank2">${T.more} ↓</a>`:''; }
    $('#mtmore').innerHTML=total>shown?`<button class="more">${T.more} (${fmt(T.shown,{a:shown,b:total})})</button>`:'';
    const mb=$('#mtmore button'); if(mb) mb.onclick=()=>{shown+=100;draw()};
    try{paintStars()}catch(e){}
  }
  draw();
})();

/* ---------- calculator ---------- */
(function(){
  if(!$('#calc')) return;
  const PALETTE=['#1a6dff','#f59e0b','#14a44d','#e5484d','#8b5cf6','#0ea5e9','#ec4899','#64748b','#84cc16','#f97316'];
  const END=WI.u.slice(0,7), END_DAY=+WI.u.slice(8,10), MAXSEL=8;
  const cache={};
  let freq='d', mode='dca', logScale=false, selected=(PAGE.sel||['btc']).filter(id=>BYID[id]); const colorOf={};
  const ym2i=s=>{const [y,m]=s.split('-').map(Number);return y*12+m-1};
  const i2ym=i=>`${Math.floor(i/12)}-${String(i%12+1).padStart(2,'0')}`;
  let DTF; try{DTF=new Intl.DateTimeFormat(T.intl||'en-US',{month:'short',year:'numeric'})}catch(e){}
  const mlabel=s=>{const [y,m]=s.split('-').map(Number);return DTF?DTF.format(new Date(y,m-1,15)):`${T.months[m-1]} ${y}`};
  const daysIn=(y,m)=>new Date(y,m,0).getDate();
  const load=id=>cache[id]||(cache[id]=fetch(`${BASE}/assets/p/${id}.json?v=${WI.v}`).then(r=>r.json()));
  function assignColors(){const used=new Set(selected.map(id=>colorOf[id]).filter(Boolean));selected.forEach(id=>{if(!colorOf[id]){colorOf[id]=PALETTE.find(c=>!used.has(c))||'#999';used.add(colorOf[id])}})}
  function perMonth(i){ let d=daysIn(Math.floor(i/12),i%12+1); if(i2ym(i)===END) d=END_DAY;
    return freq==='d'?d:freq==='w'?d/7:(i2ym(i)===END?0:1) }
  function simulate(P,startI,amt){ const s0=ym2i(P.start), e=ym2i(P.end), from=Math.max(startI,s0);
    if(mode==='lump'){ const u=amt/P.p[from-s0], pts=[]; for(let i=from;i<=e;i++) pts.push({i,inv:amt,val:u*P.p[i-s0]}); return {units:u,inv:amt,val:u*P.p[e-s0],pts,from} }
    let u=0,inv=0; const pts=[]; for(let i=from;i<=e;i++){ const c=amt*perMonth(i); u+=c/P.p[i-s0]; inv+=c; pts.push({i,inv,val:u*P.p[i-s0]}) }
    return {units:u,inv,val:u*P.p[e-s0],pts,from} }

  // since select
  const sel=$('#since');
  for(let i=ym2i(END)-1;i>=ym2i('2000-01');i--){ if(i%12!==0&&i%6!==0&&i<ym2i(END)-24) continue;
    const o=document.createElement('option'); o.value=i2ym(i); o.textContent=mlabel(i2ym(i)); sel.appendChild(o) }
  sel.value=[...sel.options].some(o=>o.value===PAGE.since)?PAGE.since:'2021-01';

  function toggle(id){ const k=selected.indexOf(id); if(k>=0){ if(selected.length>1){selected.splice(k,1);delete colorOf[id]} }
    else { if(selected.length>=MAXSEL){delete colorOf[selected.shift()]} selected.push(id) } assignColors(); chips(); render() }
  function chips(){
    $('#chips').innerHTML=selected.map(id=>{const a=BYID[id];return `<button class="chip" style="--c:${colorOf[id]}" data-id="${id}"><i></i>${esc(nm(a))} <span class="muted">${esc(a.t)}</span><span class="x">×</span></button>`}).join('')+`<button class="chip add" id="addBtn">${T.add}</button>`;
    $$('#chips .chip[data-id]').forEach(b=>b.onclick=()=>toggle(b.dataset.id));
    $('#addBtn').onclick=()=>{ $('#picker').classList.toggle('open'); $('#pq').focus(); pool() } }
  function pool(){ const q=$('#pq').value.trim().toLowerCase();
    const list=IDX.filter(a=>!selected.includes(a.i)&&(!q||a.t.toLowerCase().includes(q)||nm(a).toLowerCase().includes(q))).sort((x,y)=>x.o-y.o).slice(0,40);
    $('#pool').innerHTML=list.map(a=>`<button data-id="${a.i}">${esc(nm(a))} <span class="muted">${esc(a.t)}</span></button>`).join('')||`<span class="muted">${T.nothing}</span>`;
    $$('#pool button').forEach(b=>b.onclick=()=>{toggle(b.dataset.id); $('#pq').value=''; pool()}) }
  $('#pq').placeholder=T.filter; $('#pq').oninput=pool;
  $$('#mode button').forEach(b=>b.onclick=()=>{ mode=b.dataset.v; $$('#mode button').forEach(x=>x.classList.toggle('on',x===b));
    const am=$('#amt'); if(mode==='lump'&&+am.value<100) am.value=1000; if(mode==='dca'&&+am.value>=1000) am.value=10;
    $('#freqbox').style.visibility=mode==='lump'?'hidden':''; render() });
  $$('#freq button').forEach(b=>b.onclick=()=>{freq=b.dataset.v;$$('#freq button').forEach(x=>x.classList.toggle('on',x===b));render()});
  $('#amt').oninput=render; sel.onchange=render;
  $('#logBtn').onclick=()=>{logScale=!logScale;$('#logBtn').classList.toggle('on',logScale);render()};
  $('#copyBtn').onclick=async()=>{try{await navigator.clipboard.writeText($('#shareText').textContent);$('#copyBtn').textContent=T.copied;setTimeout(()=>$('#copyBtn').textContent=T.copy,1600)}catch(e){}};
  let rz; addEventListener('resize',()=>{clearTimeout(rz);rz=setTimeout(render,150)});

  let seq=0;
  async function render(){
    const my=++seq, amt=Math.max(1,+$('#amt').value||10), startI=ym2i(sel.value);
    const series=await Promise.all(selected.map(id=>load(id).catch(()=>null))); if(my!==seq) return;
    const res=selected.map((id,k)=>series[k]?{a:BYID[id],c:colorOf[id],...simulate(series[k],startI,amt)}:null).filter(r=>r&&r.inv>0)
      .sort((x,y)=>y.val/y.inv-x.val/x.inv);
    if(!res.length) return;
    const best=res[0], worst=res[res.length-1], full=res.filter(r=>r.from===startI);
    const h=(k,v,s,c='')=>`<div class="card"><div class="k">${k}</div><div class="v ${c}">${v}</div><div class="s">${s}</div></div>`;
    $('#hero').innerHTML=h(T.invested,fmtUsd((full[0]||best).inv),full.length?`${mlabel(i2ym(startI))} → ${mlabel(END)}`:T.diffStart)+
      h(`${T.best}: ${esc(nm(best.a))}`,fmtUsd(best.val),fmtPct(best.val/best.inv-1),cls(best.val-best.inv))+
      (res.length>1?h(`${T.worst}: ${esc(nm(worst.a))}`,fmtUsd(worst.val),fmtPct(worst.val/worst.inv-1),cls(worst.val-worst.inv)):h('&nbsp;','',''));
    $('#rt').innerHTML=`<tr><th>${T.asset}</th><th class="hide-sm">${T.invested}</th><th>${T.value}</th><th>${T.profit}</th><th class="hide-sm">${T.got}</th><th></th></tr>`+
      res.map(r=>{ const p=r.val-r.inv, u=T['u_'+r.a.c]||r.a.t, late=r.from>startI?`<div class="muted" style="font:500 11px var(--fb)">${T.frm} ${mlabel(i2ym(r.from))}</div>`:'';
        return `<tr><td class="a" style="--c:${r.c}"><i></i><a href="${url(r.a.i)}" style="text-decoration:none">${esc(nm(r.a))}</a>${late}</td><td class="hide-sm">${fmtUsd(r.inv)}</td><td>${fmtUsd(r.val)}</td><td class="${cls(p)}">${fmtUsd(p)}<br><span style="font-size:11px">${fmtPct(r.val/r.inv-1)}</span></td><td class="hide-sm">${(+r.units.toPrecision(5)).toLocaleString('en-US')} ${esc(u)}</td><td>${buyBtn(r.a)}</td></tr>` }).join('');
    $('#shareText').textContent=fmt(T.share,{asset:nm(best.a),amt,per:mode==='lump'?'':T['per_'+freq],since:mlabel(i2ym(best.from)),val:fmtUsd(best.val),pct:fmtPct(best.val/best.inv-1)});
    chart(res);
  }
  function niceStep(x){const p=10**Math.floor(Math.log10(x)),n=x/p;return (n<1.5?1:n<3?2:n<7?5:10)*p}
  function shortUsd(v){return v>=1e6?'$'+(+(v/1e6).toFixed(1))+'M':v>=1e3?'$'+(+(v/1e3).toFixed(1))+'k':'$'+Math.round(v)}
  function chart(res){
    const narrow=($('#chart').clientWidth||1000)<600, W=narrow?420:1000,H=narrow?320:400,L=narrow?46:60,R=10,Tp=12,B=28;
    const x0=Math.min(...res.map(r=>r.from)), x1=ym2i(END);
    const all=res.flatMap(r=>r.pts.flatMap(p=>[p.val,p.inv]));
    const maxV=Math.max(...all)*1.05, minV=logScale?Math.max(1,Math.min(...all.filter(v=>v>0))):0;
    const fy=v=>logScale?Tp+(H-Tp-B)*(1-(Math.log10(Math.max(v,minV))-Math.log10(minV))/(Math.log10(maxV)-Math.log10(minV)||1)):Tp+(H-Tp-B)*(1-v/maxV);
    const fx=i=>L+(W-L-R)*(x1===x0?0:(i-x0)/(x1-x0));
    let g=''; const ticks=[];
    if(logScale){for(let e=Math.floor(Math.log10(minV));e<=Math.ceil(Math.log10(maxV));e++)[1,3].forEach(k=>{const v=k*10**e;if(v>=minV&&v<=maxV)ticks.push(v)})}
    else{const st=niceStep(maxV/5);for(let v=0;v<=maxV;v+=st)ticks.push(v)}
    ticks.forEach(v=>{const y=fy(v);g+=`<line x1="${L}" x2="${W-R}" y1="${y}" y2="${y}" stroke="#eef0f3"/><text x="${L-8}" y="${y+4}" fill="#9aa1ad" font-size="11.5" text-anchor="end" font-family="Geologica, sans-serif">${shortUsd(v)}</text>`});
    const yrs=(x1-x0)/12, every=yrs>16?(narrow?4:2):yrs>8&&narrow?2:1;
    for(let i=x0;i<=x1;i++) if(i%12===0&&Math.floor(i/12)%every===0) g+=`<text x="${fx(i)}" y="${H-8}" fill="#9aa1ad" font-size="11.5" text-anchor="middle">${Math.floor(i/12)}</text>`;
    const ref=res.reduce((a,b)=>a.pts.length>=b.pts.length?a:b);
    g+=`<path d="${ref.pts.map((p,k)=>(k?'L':'M')+fx(p.i).toFixed(1)+' '+fy(p.inv).toFixed(1)).join('')}" fill="none" stroke="#9aa1ad" stroke-width="1.4" stroke-dasharray="5 5"/>`;
    res.slice().reverse().forEach(r=>{g+=`<path d="${r.pts.map((p,k)=>(k?'L':'M')+fx(p.i).toFixed(1)+' '+fy(p.val).toFixed(1)).join('')}" fill="none" stroke="${r.c}" stroke-width="2.2" stroke-linejoin="round"/>`});
    g+=`<line id="hl" x1="0" x2="0" y1="${Tp}" y2="${H-B}" stroke="#c4c9d2" style="display:none"/>`;
    $('#chart').innerHTML=`<svg viewBox="0 0 ${W} ${H}" id="svg">${g}<rect x="${L}" y="${Tp}" width="${W-L-R}" height="${H-Tp-B}" fill="transparent" id="hit"/></svg>`;
    const svg=$('#svg'),tip=$('#tip'),hl=$('#hl'),hit=$('#hit');
    const move=ev=>{ const rect=svg.getBoundingClientRect(), px=(ev.touches?ev.touches[0].clientX:ev.clientX)-rect.left;
      let i=Math.round(x0+(px*W/rect.width-L)/(W-L-R)*(x1-x0)); i=Math.max(x0,Math.min(x1,i));
      hl.setAttribute('x1',fx(i));hl.setAttribute('x2',fx(i));hl.style.display='';
      const rows=res.map(r=>{const p=r.pts.find(q=>q.i===i);return p?{c:r.c,n:nm(r.a),v:p.val}:null}).filter(Boolean).sort((a,b)=>b.v-a.v);
      const ip=ref.pts.find(q=>q.i===i);
      tip.innerHTML=`<div class="d">${mlabel(i2ym(i))}</div>`+rows.map(r=>`<div class="row"><span><span style="color:${r.c}">●</span> ${esc(r.n)}</span><b>${fmtUsd(r.v)}</b></div>`).join('')+(ip?`<div class="row muted" style="margin-top:4px"><span>${T.investedLine}</span><span>${fmtUsd(ip.inv)}</span></div>`:'');
      tip.style.display='block'; const cw=$('#chartcard').getBoundingClientRect();
      let left=rect.left-cw.left+px+14; if(left+200>cw.width) left=rect.left-cw.left+px-210;
      tip.style.left=left+'px'; tip.style.top=(rect.top-cw.top+16)+'px' };
    hit.addEventListener('mousemove',move); hit.addEventListener('touchmove',move,{passive:true});
    hit.addEventListener('mouseleave',()=>{tip.style.display='none';hl.style.display='none'});
  }
  assignColors(); chips(); render();
})();

/* ---------- referral CTA buttons on home ---------- */
(function(){ const r=REF_DEFAULT.crypto; if(!r||!r.url) return;
  ['#ctaBuy','#ctaBuy2'].forEach(s=>{const b=$(s); if(b){b.href=goUrl(r.url); b.target='_blank'; b.rel='sponsored noopener'}}) })();

/* ---------- quick DCA calculator (home hero) ---------- */
(function(){
  const box=$('#qcalc'); if(!box) return;
  let years=5;
  const ym2i=s=>{const [y,m]=s.split('-').map(Number);return y*12+m-1};
  const END=WI.u.slice(0,7), END_DAY=+WI.u.slice(8,10), ENDI=ym2i(END);
  const run=async()=>{ const id=$('#qa').value, amt=Math.max(1,+$('#qm').value||10);
    let P; try{P=await fetch(`${BASE}/assets/p/${id}.json?v=${WI.v}`).then(r=>r.json())}catch(e){return}
    const s0=ym2i(P.start), e=ym2i(P.end), from=Math.max(s0,ENDI-years*12);
    let u=0,inv=0; const path=[];
    for(let i=from;i<=e;i++){ let d=new Date(Math.floor(i/12),i%12+1,0).getDate(); if(i===ENDI) d=END_DAY;
      const c=amt*d; u+=c/P.p[i-s0]; inv+=c; path.push(u*P.p[i-s0]) }
    const val=u*P.p[e-s0], roi=val/inv-1;
    $('#qv').textContent=fmtUsd(val); $('#qv').className='v '+cls(roi);
    $('#qs').innerHTML=`<span class="${cls(roi)}">${fmtPct(roi)}</span> · ${esc(T.w_q_inv)} ${fmtUsd(inv)}`;
    $('#qsp').innerHTML=spark(path,300,56); $('#qmore').href=url(id) };
  $$('#qy button').forEach(b=>b.onclick=()=>{years=+b.dataset.y;$$('#qy button').forEach(x=>x.classList.toggle('on',x===b));run()});
  $('#qa').onchange=run; $('#qm').oninput=run; run();
})();

/* ---------- live global widgets (CoinGecko, alternative.me) ---------- */
(function(){
  if(!PAGE.home) return;
  const big=v=>v>=1e12?'$'+(v/1e12).toFixed(2)+'T':'$'+(v/1e9).toFixed(1)+'B';
  fetch('https://api.coingecko.com/api/v3/global').then(r=>r.json()).then(d=>{ const x=d.data; if(!x) return;
    $('#gmcap').textContent=big(x.total_market_cap.usd); $('#gvol').textContent=big(x.total_volume.usd);
    const c=x.market_cap_change_percentage_24h_usd/100; const el=$('#gmchg'); el.textContent=fmtPct(c); el.className=cls(c);
    $('#gdom').textContent=x.market_cap_percentage.btc.toFixed(1)+'%' }).catch(()=>{});
  fetch('https://api.alternative.me/fng/?limit=1').then(r=>r.json()).then(d=>{ const v=+d.data[0].value; if(!isFinite(v)) return;
    $('#fngv').textContent=v; const L=(T.w_fng_l||'').split('|'); $('#fngl').textContent=L[v<25?0:v<45?1:v<56?2:v<76?3:4]||'';
    const a=Math.PI*(1-v/100), dot=$('#fngdot'); if(dot){dot.setAttribute('cx',100+78*Math.cos(a));dot.setAttribute('cy',100-78*Math.sin(a))} }).catch(()=>{});
})();

/* ---------- mobile menu sheet ---------- */
(function(){ const b=$('#mmore'), sh=$('#msheet'); if(!b||!sh) return;
  b.onclick=e=>{ e.stopPropagation(); sh.hidden=!sh.hidden }; document.addEventListener('click',e=>{ if(!sh.hidden&&!sh.contains(e.target)) sh.hidden=true }) })();

/* ---------- theme toggle + PWA ---------- */
(function(){
  const b=$('#thm'); if(b) b.onclick=()=>{ const d=document.documentElement, dark=d.dataset.theme!=='dark';
    if(dark) d.dataset.theme='dark'; else delete d.dataset.theme;
    try{ localStorage.setItem('wi_theme',dark?'dark':'light') }catch(e){}
    const m=$('meta[name=theme-color]'); if(m) m.content=dark?'#0e1014':'#ffffff';
    if($('.tvw[data-done]')) location.reload() };
  if('serviceWorker' in navigator && location.protocol==='https:') addEventListener('load',()=>navigator.serviceWorker.register('/sw.js').catch(()=>{}));
})();

/* ---------- live crypto prices (Binance WebSocket, only symbols shown on the page) ---------- */
(function(){
  if(!('WebSocket' in window)) return;
  const heat=c=>{ c=Math.max(-.1,Math.min(.1,c)); if(c>=0){const k=c/.1;return `rgb(${232-212*k|0},${246-82*k|0},${237-160*k|0})`} const k=-c/.1;return `rgb(${253-24*k|0},${236-164*k|0},${236-159*k|0})` };
  let ws=null, tries=0, want='';
  function symbols(){ const ids=new Set($$('[data-p],[data-c],[data-h]').map(el=>el.dataset.p||el.dataset.c||el.dataset.h));
    if($('#hold')) try{ JSON.parse(localStorage.getItem('wi_hold')||'[]').forEach(x=>ids.add(x.id)) }catch(e){}
    return [...ids].map(id=>BYID[id]).filter(a=>a&&a.c==='crypto'&&a.bn).map(a=>a.t.toLowerCase()+'usdt@miniTicker').slice(0,200) }
  function apply(k){ const a=IDX.find(x=>x.c==='crypto'&&x.t+'USDT'===k.s); if(!a) return; const p=+k.c, o=+k.o; if(!p) return;
    const old=a.pr; a.pr=p; a.ch=o?p/o-1:a.ch;
    $$(`[data-p="${a.i}"]`).forEach(el=>{ el.textContent=fmtPrice(p); if(old&&p!==old){ el.classList.remove('flash-up','flash-dn'); void el.offsetWidth; el.classList.add(p>old?'flash-up':'flash-dn') } });
    $$(`[data-c="${a.i}"]`).forEach(el=>{ el.textContent=fmtPct(a.ch); el.classList.remove('good','bad'); el.classList.add(cls(a.ch)) });
    $$(`[data-h="${a.i}"]`).forEach(el=>{ el.style.background=heat(a.ch); el.classList.toggle('dk',Math.abs(a.ch)>.04) });
    document.dispatchEvent(new CustomEvent('wi:tick',{detail:a})) }
  function connect(){ const s=symbols(); if(!s.length) return; want=s.join('/');
    try{ ws=new WebSocket('wss://data-stream.binance.vision/stream?streams='+want) }catch(e){ return }
    ws.onmessage=ev=>{ let m; try{m=JSON.parse(ev.data).data}catch(e){return} if(m&&m.s) apply(m) };
    ws.onclose=()=>{ ws=null; if(!document.hidden&&tries++<5) setTimeout(connect,3000*tries) } }
  document.addEventListener('visibilitychange',()=>{ if(document.hidden){ if(ws){ tries=99; ws.close() } } else if(!ws){ tries=0; connect() } });
  if(!document.querySelector('.art')) connect();
})();

/* ---------- TradingView widgets (lazy) ---------- */
(function(){
  const els=$$('.tvw'); if(!els.length) return;
  const mount=el=>{ if(el.dataset.done) return; el.dataset.done=1;
    const wrap=document.createElement('div'); wrap.className='tradingview-widget-container'; wrap.style.height='100%';
    wrap.innerHTML='<div class="tradingview-widget-container__widget" style="height:100%"></div>';
    const s=document.createElement('script'); s.src=`https://s3.tradingview.com/external-embedding/embed-widget-${el.dataset.w}.js`; s.async=true;
    let cfg=el.dataset.cfg; if(document.documentElement.dataset.theme==='dark'){ try{ const c=JSON.parse(cfg); if('colorTheme' in c) c.colorTheme='dark'; if('theme' in c) c.theme='dark'; cfg=JSON.stringify(c) }catch(e){} }
    s.textContent=cfg; wrap.appendChild(s); el.appendChild(wrap) };
  if('IntersectionObserver' in window){ const io=new IntersectionObserver(es=>es.forEach(e=>{ if(e.isIntersecting){io.unobserve(e.target);mount(e.target)} }),{rootMargin:'400px'}); els.forEach(el=>io.observe(el)) }
  else els.forEach(mount);
})();

/* ---------- converter (crypto, stocks, metals, 45 fiat currencies) ---------- */
(function(){
  if(!$('#cvres')) return;
  const FX=Object.assign({},WI.fx||{});
  let DN; try{DN=new Intl.DisplayNames([T.intl||'en'],{type:'currency'})}catch(e){}
  const SYM='$ € ₴ zł £ ¥';
  $$('#cvf optgroup,#cvt optgroup').forEach(g=>{ g.label=g.dataset.g==='fiat'?SYM:g.dataset.g==='crypto'?T.crypto:`${T.stock} · ${T.etf} · ${T.metal}` });
  $$('#cvf option,#cvt option').forEach(o=>{ const v=o.value; const c=v==='usd'?'USD':v.startsWith('fx:')?v.slice(3):null;
    if(c&&DN){ try{ const n=DN.of(c); o.textContent=`${n.charAt(0).toUpperCase()+n.slice(1)} (${c})` }catch(e){} } });
  const def=$('#cvt').dataset.def; if(def&&[...$('#cvt').options].some(o=>o.value===def)) $('#cvt').value=def;
  const isFiat=id=>id==='usd'||id.startsWith('fx:');
  const px=id=>id==='usd'?1:id.startsWith('fx:')?(FX[id.slice(3)]?1/FX[id.slice(3)]:null):(BYID[id]&&BYID[id].pr);
  const lab=id=>id==='usd'?'USD':id.startsWith('fx:')?id.slice(3):BYID[id].t;
  const fmtN=(x,fiat)=>fiat?x.toLocaleString(T.intl||'en-US',{minimumFractionDigits:2,maximumFractionDigits:2}):x>=1?x.toLocaleString('en-US',{maximumFractionDigits:4}):x.toLocaleString('en-US',{maximumSignificantDigits:6});
  const run=()=>{ const a=+$('#cva').value||0, f=$('#cvf').value, to=$('#cvt').value, pf=px(f), pt=px(to); if(!pf||!pt) return;
    const v=a*pf/pt, r=pf/pt;
    $('#cvres').innerHTML=`<b>${fmtN(a,false)} ${esc(lab(f))}</b> = <b class="big">${fmtN(v,isFiat(to))} ${esc(lab(to))}</b>`;
    $('#cvrate').textContent=`1 ${lab(f)} = ${fmtN(r,isFiat(to))} ${lab(to)} · 1 ${lab(to)} = ${fmtN(1/r,isFiat(f))} ${lab(f)}${(isFiat(f)&&f!=='usd')||(isFiat(to)&&to!=='usd')?' · FX '+(WI.fxu||''):''}` };
  ['#cva','#cvf','#cvt'].forEach(s=>$(s).addEventListener('input',run));
  $('#cvsw').onclick=()=>{ const f=$('#cvf').value; $('#cvf').value=$('#cvt').value; $('#cvt').value=f; run() };
  run(); document.addEventListener('wi:tick',run);
  fetch('https://open.er-api.com/v6/latest/USD').then(r=>r.json()).then(d=>{ if(d&&d.rates){ Object.keys(FX).forEach(c=>{ if(d.rates[c]) FX[c]=d.rates[c] }); WI.fxu=(d.time_last_update_utc||'').slice(5,16); run() } }).catch(()=>{});
})();

/* ---------- habits -> money calculator ---------- */
(function(){
  const box=$('#hcalc'); if(!box||!PAGE.habit) return; const C=PAGE.habit;
  let asset='spy', years=10; const S={};
  const END=WI.u.slice(0,7), END_DAY=+WI.u.slice(8,10);
  const ym2i=s=>{const [y,m]=s.split('-').map(Number);return y*12+m-1};
  const nf=v=>{ try{ return new Intl.NumberFormat(T.intl||'en',{style:'currency',currency:C.code,maximumFractionDigits:Math.abs(v)>=100?0:2}).format(v) }catch(e){ return Math.round(v)+' '+C.code } };
  function sim(P,st,amt){ const s0=ym2i(P.start), e=ym2i(P.end), from=Math.max(st,s0); let u=0,inv=0;
    for(let i=from;i<=e;i++){ const y=Math.floor(i/12), m=i%12+1, d=i===ym2i(END)?END_DAY:new Date(y,m,0).getDate(), c=amt*d; u+=c/P.p[i-s0]; inv+=c }
    return {inv,val:u*P.p[e-s0]} }
  async function run(){
    const price=+$('#hp').value||0, t=+$('#ht').value||0, per=$('#hper').value, daily=price*t/({d:1,w:7,m:30.4375}[per])/C.rate;
    try{ await Promise.all(C.assets.map(async id=>{ if(!S[id]) S[id]=await fetch(`${BASE}/assets/p/${id}.json?v=${WI.v}`).then(r=>r.json()) })) }catch(e){ return }
    const st=ym2i(END)-years*12, R={};
    C.assets.forEach(id=>{ const r=sim(S[id],st,daily); r.inv*=C.rate; r.val*=C.rate; r.roi=r.inv?r.val/r.inv-1:null; R[id]=r;
      const tr=$(`#htb tr[data-a="${id}"]`); if(tr){ const td=tr.children; td[1].textContent=nf(r.inv); td[2].innerHTML='<b>'+nf(r.val)+'</b>'; td[3].textContent=fmtPct(r.roi); td[3].className='mono '+cls(r.roi) } });
    const r=R[asset]; $('#hval').textContent=nf(r.val); $('#hval').className='v '+cls(r.roi);
    const ph=C.res.startsWith('{habit}')?C.phrase[0].toUpperCase()+C.phrase.slice(1):C.phrase;
    $('#hsent').textContent=fmt(C.res,{y:C.yl[years],habit:ph,spent:nf(r.inv),asset:nm(BYID[asset]),val:nf(r.val),roi:fmtPct(r.roi)}) }
  ['#hp','#ht','#hper'].forEach(q=>$(q).addEventListener('input',run));
  $$('#has button').forEach(b=>b.onclick=()=>{ asset=b.dataset.v; $$('#has button').forEach(x=>x.classList.toggle('on',x===b)); run() });
  $$('#hy button').forEach(b=>b.onclick=()=>{ years=+b.dataset.v; $$('#hy button').forEach(x=>x.classList.toggle('on',x===b)); run() });
  run();
})();
/* ---------- millionaire + compound interest ---------- */
(function(){
  const box=$('#gcalc'); if(!box||!PAGE.calc) return; const C=PAGE.calc;
  const nf=v=>{ try{ return new Intl.NumberFormat(T.intl||'en',{style:'currency',currency:C.code,maximumFractionDigits:Math.abs(v)>=100?0:2}).format(v) }catch(e){ return Math.round(v)+' '+C.code } };
  const pc=v=>(v*100).toFixed(1)+'%';
  let r=+($('#gseg button.on')||{}).dataset?.r||0.1, asset=($('#gseg button.on')||{}).dataset?.a||'spy';
  const num=q=>{ const e=$(q); return e?Math.max(0,+e.value||0):0 };
  function run(){
    const n=Math.max(1,Math.min(60,num('#gy'))), p0=num('#gp'), rate=$('#gcw').hidden?r:(+$('#gr').value||0)/100;
    const rm=Math.pow(1+rate,1/12)-1, N=n*12, g=Math.pow(1+rm,N), an=Math.abs(rm)<1e-12?N:(g-1)/rm;
    const aname=C.names[asset]||''; $('#gsent').hidden=!$('#gcw').hidden;
    let inv,val;
    if(C.kind==='millionaire'){ const goal=num('#gg'); const pmt=Math.max(0,(goal-p0*g)/an); inv=p0+pmt*N; val=Math.max(goal,p0*g);
      $('#gv').textContent=nf(pmt); $('#gsent').textContent=fmt(C.res,{goal:nf(goal),n,yr:C.yr,pmt:nf(pmt),asset:aname,r:pc(rate)}) }
    else { const pmt=num('#gm'); val=p0*g+pmt*an; inv=p0+pmt*N;
      $('#gv').textContent=nf(val); $('#gsent').textContent=fmt(C.res,{n,yr:C.yr,fv:nf(val),inv:nf(inv),gain:nf(val-inv)}) }
    const a=val>0?Math.min(100,inv/val*100):100; $('#gbar .a').style.width=a+'%'; $('#gbar .b').style.width=(100-a)+'%' }
  $$('#gseg button').forEach(b=>b.onclick=()=>{ $$('#gseg button').forEach(x=>x.classList.toggle('on',x===b));
    if(b.dataset.r==='custom'){ $('#gcw').hidden=false } else { $('#gcw').hidden=true; r=+b.dataset.r; asset=b.dataset.a; $('#gr').value=(r*100).toFixed(1) } run() });
  $$('#gcalc input').forEach(e=>e.addEventListener('input',run)); run();
})();

/* ---------- inflation ---------- */
(function(){
  const box=$('#icalc'); if(!box||!PAGE.infl) return; const C=PAGE.infl;
  let DN; try{ DN=new Intl.DisplayNames([T.intl||'en'],{type:'region'}) }catch(e){}
  $$('#ic option').forEach(o=>{ const n=DN&&DN.of(o.dataset.cc); if(n) o.textContent=`${n} (${o.dataset.ccy})` });
  const opts=[...$('#ic').options].sort((a,b)=>a.textContent.localeCompare(b.textContent)); const cur=$('#ic').value; $('#ic').append(...opts); $('#ic').value=cur;
  const pc=v=>(v*100).toFixed(1)+'%';
  function run(){ const c=$('#ic').value, o=$('#ic').selectedOptions[0], ccy=o.dataset.ccy, d=C.c[c]||{}, y0=+$('#iy').value, amt=+$('#ia').value||0;
    const ys=Object.keys(d).map(Number), last=Math.max(...ys); let f=1; for(let y=y0+1;y<=last;y++) f*=1+(d[y]||0)/100;
    const nf=v=>{ try{ return new Intl.NumberFormat(T.intl||'en',{style:'currency',currency:ccy,maximumFractionDigits:Math.abs(v)>=100?0:2}).format(v) }catch(e){ return Math.round(v)+' '+ccy } };
    let sym=ccy; try{ sym=new Intl.NumberFormat(T.intl||'en',{style:'currency',currency:ccy}).formatToParts(1).find(p=>p.type==='currency').value }catch(e){}
    $('#isym').textContent=sym; $('#iv').textContent=nf(amt*f);
    $('#is').textContent=fmt(C.res,{amt:nf(amt),y0,now:nf(amt*f),pct:pc(f-1),lost:pc(1-1/f)}); $('#isrc').textContent=fmt(C.src,{y:last}) }
  ['#ic','#iy','#ia'].forEach(q=>$(q).addEventListener('input',run)); run();
})();

/* ---------- bitcoin halving countdown ---------- */
(function(){
  const box=$('#hv'); if(!box) return;
  const NEXT=+box.dataset.next; let h=+box.dataset.h, at=Date.now();
  let DTF; try{ DTF=new Intl.DateTimeFormat(T.intl||'en',{day:'numeric',month:'long',year:'numeric'}) }catch(e){}
  function draw(){ const left=Math.max(0,NEXT-h), ms=left*600000-(Date.now()-at), s=Math.max(0,ms/1000);
    $('#hd').textContent=Math.floor(s/86400).toLocaleString(T.intl||'en'); $('#hh').textContent=Math.floor(s%86400/3600); $('#hm').textContent=Math.floor(s%3600/60);
    $('#hleft').textContent=left.toLocaleString(T.intl||'en'); if(DTF) $('#hest').textContent='≈ '+DTF.format(new Date(at+left*600000));
    $('#hprog').style.width=Math.min(100,(h-840000)/2100)+'%' }
  fetch('https://mempool.space/api/blocks/tip/height').then(r=>r.text()).then(t=>{ const v=parseInt(t); if(v>840000){ h=v; at=Date.now(); draw() } }).catch(()=>{});
  draw(); setInterval(draw,30000);
})();
/* ---------- Polymarket odds (Gamma API) ---------- */
(function(){
  const box=$('.pm'); if(!box) return;
  const VIA='?via=alek-du', pc=v=>v<.01?'<1%':v>.99?'>99%':Math.round(v*100)+'%';
  const go=()=>fetch(`https://gamma-api.polymarket.com/events?closed=false&tag_slug=${box.dataset.tag||'crypto'}&order=volume24hr&ascending=false&limit=12`).then(r=>r.json()).then(ev=>{
    const out=[];
    for(const e of ev){ if(out.length>=4) break;
      const ms=(e.markets||[]).filter(m=>m.active&&!m.closed&&m.outcomePrices).map(m=>{ let p; try{p=+JSON.parse(m.outcomePrices)[0]}catch(x){} return {t:m.groupItemTitle||m.question,p} })
        .filter(m=>m.p>=.04&&m.p<=.96).slice(0,4);
      if(!ms.length) continue;
      out.push(`<a class="pmi" href="${goUrl('/go/polymarket','&e='+encodeURIComponent(e.slug))}" target="_blank" rel="sponsored nofollow noopener"><b>${esc(e.title)}</b>`+
        ms.map(m=>`<span class="pmr"><em>${esc(m.t)}</em><i><s style="width:${Math.round(m.p*100)}%"></s></i><strong>${pc(m.p)}</strong></span>`).join('')+'</a>') }
    if(out.length){ box.querySelector('.pml').innerHTML=out.join(''); box.hidden=false } }).catch(()=>{});
  setTimeout(go,1200);
})();
/* ---------- news aggregator ---------- */
(function(){
  const box=$('#nlist'); if(!box||!PAGE.news) return; const TG=PAGE.news.tags;
  let items=[], tag='', shown=40;
  let RT; try{ RT=new Intl.RelativeTimeFormat(T.intl||'en',{numeric:'auto'}) }catch(e){}
  const ago=d=>{ if(!d||!RT) return ''; const m=Math.round((d-Date.now())/60000); return Math.abs(m)<60?RT.format(m,'minute'):Math.abs(m)<1440?RT.format(Math.round(m/60),'hour'):RT.format(Math.round(m/1440),'day') };
  function draw(){ const L=items.filter(x=>!tag||(x.g||[]).includes(tag));
    box.innerHTML=L.slice(0,shown).map(x=>`<a class="nrow" href="${esc(x.u)}" target="_blank" rel="noopener"><b>${esc(x.t)}</b><span class="muted">${esc(x.s)} · ${ago(x.d)}${(x.g||[]).map(g=>` <i class="badge">${esc(TG[g]||g)}</i>`).join('')}</span></a>`).join('')||'<p class="muted">—</p>';
    $('#nmore').hidden=L.length<=shown }
  $$('#ntags button').forEach(b=>b.onclick=()=>{ tag=b.dataset.t; shown=40; $$('#ntags button').forEach(x=>x.classList.toggle('on',x===b));
    $$('.nlist.own .nrow').forEach(r=>r.hidden=!!tag&&!(r.dataset.g||'').split(' ').includes(tag)); draw() });
  $('#nmore').onclick=()=>{ shown+=40; draw() };
  const load=()=>fetch('/api/news/').then(r=>r.json()).then(d=>{ items=d.items||[]; draw() }).catch(()=>{ box.innerHTML='<p class="muted">—</p>' });
  load(); setInterval(()=>{ if(!document.hidden) load() },300000);
})();

/* ---------- local time for news timestamps ---------- */
(function(){ let F; try{ F=new Intl.DateTimeFormat(T.intl||'en',{day:'numeric',month:'short',hour:'2-digit',minute:'2-digit'}) }catch(e){ return }
  $$('time[data-t]').forEach(t=>{ const d=Date.parse(t.dataset.t.replace(' ','T')+(/Z|[+-]\d\d:?\d\d$/.test(t.dataset.t)?'':'Z')); if(d) t.textContent=F.format(new Date(d)) }) })();

/* ---------- insights category tabs ---------- */
(function(){ const t=$('#bcats'); if(!t) return;
  $$('#bcats button').forEach(b=>b.onclick=()=>{ $$('#bcats button').forEach(x=>x.classList.toggle('on',x===b)); $$('.posts .post[data-c]').forEach(p=>p.hidden=!!b.dataset.c&&p.dataset.c!==b.dataset.c) }) })();
/* ---------- one-question poll ---------- */
(function(){ const box=$('#poll'); if(!box) return; let done; try{ done=localStorage.getItem('wi_poll1') }catch(e){}
  if(done) return; box.hidden=false;
  $$('#poll button').forEach(b=>b.onclick=()=>{ fetch(`/api/poll/?o=${b.dataset.o}&l=${lang}`).catch(()=>{}); try{ localStorage.setItem('wi_poll1',b.dataset.o) }catch(e){}
    box.querySelector('.pollb').innerHTML=`<span class="good">✓ ${esc(box.dataset.thanks)}</span>` }) })();
/* ---------- watchlist stars (localStorage) ---------- */
const WL={ get(){ try{ return JSON.parse(localStorage.getItem('wi_watch')||'[]') }catch(e){ return [] } },
  set(v){ try{ localStorage.setItem('wi_watch',JSON.stringify(v)) }catch(e){} document.dispatchEvent(new Event('wi:watch')) } };
function paintStars(){ const w=new Set(WL.get()); $$('.star[data-s]').forEach(b=>{ const on=w.has(b.dataset.s); b.textContent=on?'★':'☆'; b.classList.toggle('on',on) });
}
document.addEventListener('click',e=>{ const b=e.target.closest('.star[data-s]'); if(!b) return; e.preventDefault(); e.stopPropagation();
  const w=WL.get(), i=w.indexOf(b.dataset.s); if(i>=0) w.splice(i,1); else w.unshift(b.dataset.s); WL.set(w) },true);
document.addEventListener('wi:watch',paintStars); paintStars();
new MutationObserver(()=>{ clearTimeout(window._wiStar); window._wiStar=setTimeout(paintStars,50) }).observe(document.body,{childList:true,subtree:true});

/* ---------- my account: DCA plans + watchlist ---------- */
(function(){
  const C=PAGE.me; if(!C) return; const t=C.t;
  const PL={ get(){ try{ return JSON.parse(localStorage.getItem('wi_plans')||'[]') }catch(e){ return [] } }, set(v){ try{ localStorage.setItem('wi_plans',JSON.stringify(v)) }catch(e){} } };
  const nf=v=>{ try{ return new Intl.NumberFormat(T.intl||'en',{style:'currency',currency:C.code,maximumFractionDigits:Math.abs(v)>=100?0:2}).format(v) }catch(e){ return Math.round(v)+' '+C.code } };
  const END=WI.u.slice(0,7), END_DAY=+WI.u.slice(8,10), ym2i=s=>{const [y,m]=s.split('-').map(Number);return y*12+m-1};
  const cache={}, load=id=>cache[id]||(cache[id]=fetch(`${BASE}/assets/p/${id}.json?v=${WI.v}`).then(r=>r.json()));
  function sim(P,st,amt,f){ const s0=ym2i(P.start), e=ym2i(P.end), from=Math.max(st,s0); let u=0,inv=0;
    for(let i=from;i<=e;i++){ const y=Math.floor(i/12), m=i%12+1, d=i===ym2i(END)?END_DAY:new Date(y,m,0).getDate(); const c=f==='d'?amt*d:f==='w'?amt*d/7:(i===ym2i(END)&&END_DAY<28&&i!==from?0:amt); u+=c/P.p[i-s0]; inv+=c }
    return {inv,val:u*P.p[e-s0]} }
  // datalist
  $('#palist').innerHTML=IDX.slice(0,1200).map(a=>`<option value="${esc(nm(a))} (${esc(a.t)})" data-i="${a.i}">`).join('');
  const findId=v=>{ const m=/\(([^)]+)\)\s*$/.exec(v||''); const tk=m?m[1]:v; const a=IDX.find(x=>x.t.toLowerCase()===String(tk).toLowerCase()||nm(x).toLowerCase()===String(v).toLowerCase()); return a&&a.i };
  async function drawPlans(){
    const plans=PL.get(), box=$('#plans'); if(!plans.length){ box.innerHTML=''; $('#metot').innerHTML=''; return }
    let tInv=0,tVal=0,tSpy=0; const rows=[];
    for(const [k,p] of plans.entries()){ const a=BYID[p.id]; if(!a) continue;
      const [P,S]=await Promise.all([load(p.id),load('spy')]), usd=p.amt/C.rate, st=ym2i(p.from);
      const r=sim(P,st,usd,p.f), s=sim(S,st,usd,p.f); const inv=r.inv*C.rate, val=r.val*C.rate, sv=s.val*C.rate, roi=inv?val/inv-1:0;
      tInv+=inv; tVal+=val; tSpy+=sv;
      rows.push(`<div class="card plan"><div class="ph"><a class="asset" href="${url(a.i)}">${icon(a)}<span><span class="nm">${esc(nm(a))}</span><span class="tk">${esc(nf(p.amt))} · ${esc(C.per[p.f]||'')} · ${esc(t.start)} ${esc(p.from)}</span></span></a><button class="toggle" data-del="${k}">${esc(t.remove)}</button></div>
        <div class="pg"><div><small>${esc(T.invested||'')}</small><b>${nf(inv)}</b></div><div><small>${esc(T.value||'')}</small><b>${nf(val)}</b></div><div><small>${esc(t.profit)}</small><b class="${cls(roi)}">${fmtPct(roi)}</b></div><div><small>${esc(t.vs)}</small><b>${nf(sv)}</b></div></div></div>`) }
    box.innerHTML=rows.join('');
    const roi=tInv?tVal/tInv-1:0;
    $('#metot').innerHTML=`<div class="card"><div class="k">${esc(t.total)}</div><div class="v">${nf(tVal)}</div><div class="s">${esc(T.invested||'')}: ${nf(tInv)}</div></div>
      <div class="card"><div class="k">${esc(t.profit)}</div><div class="v ${cls(roi)}">${fmtPct(roi)}</div><div class="s">${nf(tVal-tInv)}</div></div>
      <div class="card"><div class="k">${esc(t.vs)}</div><div class="v">${nf(tSpy)}</div><div class="s">${fmtPct(tInv?tSpy/tInv-1:0)}</div></div>`;
    $$('#plans [data-del]').forEach(b=>b.onclick=()=>{ const v=PL.get(); v.splice(+b.dataset.del,1); PL.set(v); drawPlans() }) }
  $('#psave').onclick=()=>{ const id=findId($('#pa').value), amt=+$('#pm').value, from=$('#ps').value||END;
    if(!id){ $('#pa').focus(); $('#pa').classList.add('bad'); return } if(!(amt>0)) return;
    const v=PL.get(); v.push({id,amt,f:$('#pf').value,from:from.slice(0,7)}); PL.set(v); $('#pa').value=''; drawPlans();
    const w=WL.get(); if(!w.includes(id)){ w.unshift(id); WL.set(w) } };
  function drawWatch(){ const w=WL.get().filter(i=>BYID[i]), box=$('#watch'); if(!w.length){ box.innerHTML=`<p class="muted">${esc(t.empty)}</p>`; return }
    box.innerHTML=`<div class="tw"><table class="mt"><thead><tr><th class="l">${esc(T.name||'')}</th><th>${esc(T.price||'')}</th><th>${esc(T.chg||'')}</th><th class="hide-sm">${esc(T.d1||'')}</th><th>${esc(T.d5||'')}</th><th class="hide-sm">${esc(T.spark||'')}</th></tr></thead><tbody>`+
      w.map(i=>{ const a=BYID[i]; return `<tr><td class="l"><button class="star" data-s="${a.i}">★</button><a class="asset" href="${url(a.i)}">${icon(a)}<span><span class="nm">${esc(nm(a))}</span><span class="tk">${esc(a.t)}</span></span></a></td>
        <td class="num" data-p="${a.i}">${fmtPrice(a.pr)}</td><td class="num ${cls(a.ch)}" data-c="${a.i}">${fmtPct(a.ch)}</td><td class="num hide-sm ${cls(a.r1)}">${fmtPct(a.r1)}</td><td><span class="pill ${cls(a.r5)}">${fmtPct(a.r5)}</span></td><td class="hide-sm">${spark(a.sp)}</td></tr>` }).join('')+'</tbody></table></div>' }
  /* simple portfolio (holdings) */
  const HL={ get(){ try{ return JSON.parse(localStorage.getItem('wi_hold')||'[]') }catch(e){ return [] } }, set(v){ try{ localStorage.setItem('wi_hold',JSON.stringify(v)) }catch(e){} } };
  const PAL=['#1a6dff','#f59e0b','#14a44d','#e5484d','#8b5cf6','#0ea5e9','#ec4899','#64748b','#84cc16','#f97316'];
  $('#hmode').onchange=()=>{ $('#hunit').textContent=$('#hmode').value==='qty'?'':(new Intl.NumberFormat(T.intl||'en',{style:'currency',currency:C.code}).formatToParts(1).find(p=>p.type==='currency')||{}).value||C.code };
  $('#hsave').onclick=async()=>{ const id=findId($('#ha').value), v=+$('#hamt').value, d=($('#hdate').value||END).slice(0,7);
    if(!id){ $('#ha').focus(); $('#ha').classList.add('bad'); return } if(!(v>0)) return;
    const a=BYID[id]; let px=a.pr;
    if(d<END){ try{ const P=await load(id), k=ym2i(d)-ym2i(P.start); if(k>=0&&k<P.p.length) px=P.p[k] }catch(e){} }
    const qty=$('#hmode').value==='qty'?v:(v/C.rate)/px, cost=qty*px;
    const h=HL.get(); h.push({id,qty,cost,d}); HL.set(h); $('#ha').value=''; $('#ha').classList.remove('bad'); drawHold() };
  function drawHold(){
    const raw=HL.get(), agg={};
    raw.forEach(x=>{ if(!BYID[x.id]) return; const g=agg[x.id]||(agg[x.id]={id:x.id,qty:0,cost:0}); g.qty+=x.qty; g.cost+=x.cost });
    const L=Object.values(agg).map(g=>{ const a=BYID[g.id]; return Object.assign(g,{a,val:g.qty*a.pr}) }).sort((x,y)=>y.val-x.val);
    if(!L.length){ $('#hold').innerHTML=`<p class="muted">${esc(t.hempty)}</p>`; $('#htot').innerHTML=''; $('#abar').innerHTML=''; return }
    const tv=L.reduce((s,g)=>s+g.val,0), tc=L.reduce((s,g)=>s+g.cost,0), d24=L.reduce((s,g)=>s+g.val*(g.a.ch||0)/(1+(g.a.ch||0)),0), roi=tc?tv/tc-1:0;
    $('#htot').innerHTML=`<div class="card"><div class="k">${esc(t.total)}</div><div class="v">${nf(tv*C.rate)}</div><div class="s">${esc(T.invested||'')}: ${nf(tc*C.rate)}</div></div>
      <div class="card"><div class="k">${esc(t.profit)}</div><div class="v ${cls(roi)}">${fmtPct(roi)}</div><div class="s ${cls(roi)}">${nf((tv-tc)*C.rate)}</div></div>
      <div class="card"><div class="k">${esc(T.chg||'24h')}</div><div class="v ${cls(d24)}">${fmtPct(tv-d24?d24/(tv-d24):0)}</div><div class="s ${cls(d24)}">${nf(d24*C.rate)}</div></div>`;
    $('#abar').innerHTML=L.map((g,i)=>`<i style="width:${(g.val/tv*100).toFixed(2)}%;background:${PAL[i%PAL.length]}" title="${esc(g.a.t)} ${(g.val/tv*100).toFixed(1)}%"></i>`).join('');
    $('#hold').innerHTML=`<div class="tw"><table class="mt"><thead><tr><th class="l">${esc(T.name||'')}</th><th class="hide-sm">${esc(t.qty)}</th><th class="hide-sm">${esc(t.avg)}</th><th>${esc(T.value||'')}</th><th>${esc(t.profit)}</th><th class="hide-sm">${esc(T.chg||'')}</th><th class="hide-sm">${esc(t.share)}</th><th></th></tr></thead><tbody>`+
      L.map((g,i)=>{ const r=g.cost?g.val/g.cost-1:0; return `<tr><td class="l"><i class="dot" style="background:${PAL[i%PAL.length]}"></i><a class="asset" href="${url(g.id)}">${icon(g.a)}<span><span class="nm">${esc(nm(g.a))}</span><span class="tk">${esc(g.a.t)}</span></span></a></td>
        <td class="num hide-sm">${(+g.qty.toPrecision(6)).toLocaleString(T.intl||'en')}</td><td class="num hide-sm">${fmtPrice(g.cost/g.qty)}</td><td class="num"><b>${nf(g.val*C.rate)}</b></td>
        <td class="num ${cls(r)}">${fmtPct(r)}<br><small>${nf((g.val-g.cost)*C.rate)}</small></td><td class="num hide-sm ${cls(g.a.ch)}">${fmtPct(g.a.ch)}</td><td class="num hide-sm">${(g.val/tv*100).toFixed(1)}%</td>
        <td><button class="toggle" data-hdel="${g.id}" aria-label="${esc(t.remove)}">✕</button></td></tr>` }).join('')+'</tbody></table></div>';
    $$('#hold [data-hdel]').forEach(b=>b.onclick=()=>{ HL.set(HL.get().filter(x=>x.id!==b.dataset.hdel)); drawHold() }) }
  let ht; document.addEventListener('wi:tick',()=>{ clearTimeout(ht); ht=setTimeout(drawHold,1500) });
  document.addEventListener('wi:watch',drawWatch); drawWatch(); drawPlans(); drawHold();
})();
/* ---------- memecoins: live DEX trending (GeckoTerminal) ---------- */
(function(){
  const box=$('#dexb'); if(!box||!PAGE.memes) return; const L=PAGE.memes.t; let net='solana';
  const GMGN={solana:'sol',base:'base',bsc:'bsc',eth:'eth'};
  const big=v=>{ v=+v||0; return v>=1e9?'$'+(v/1e9).toFixed(2)+'B':v>=1e6?'$'+(v/1e6).toFixed(2)+'M':v>=1e3?'$'+(v/1e3).toFixed(1)+'K':'$'+v.toFixed(0) };
  let RT; try{ RT=new Intl.RelativeTimeFormat(T.intl||'en',{numeric:'auto',style:'short'}) }catch(e){}
  const age=d=>{ const h=(Date.now()-Date.parse(d))/36e5; if(!isFinite(h)||!RT) return ''; return h<1?RT.format(-Math.round(h*60),'minute'):h<48?RT.format(-Math.round(h),'hour'):RT.format(-Math.round(h/24),'day') };
  function load(){
    fetch(`https://api.geckoterminal.com/api/v2/networks/${net}/trending_pools?page=1&include=base_token`).then(r=>r.json()).then(d=>{
      const toks={}; (d.included||[]).forEach(x=>{ if(x.type==='token') toks[x.id]=x.attributes });
      const rows=(d.data||[]).slice(0,20).map(p=>{ const a=p.attributes, bt=toks[(p.relationships&&p.relationships.base_token&&p.relationships.base_token.data||{}).id]||{};
        const c1=+(a.price_change_percentage||{}).h1/100, c24=+(a.price_change_percentage||{}).h24/100, liq=+a.reserve_in_usd||0, vol=+(a.volume_usd||{}).h24||0;
        const hrs=(Date.now()-Date.parse(a.pool_created_at))/36e5, flags=[];
        if(hrs<72) flags.push(`<i class="rf">${esc(L.new)}</i>`); if(liq<50000) flags.push(`<i class="rf">${esc(L.lowliq)}</i>`); if(liq>0&&vol/liq>20) flags.push(`<i class="rf">${esc(L.hot)}</i>`);
        const sym=bt.symbol||(a.name||'').split(' / ')[0], img=bt.image_url&&bt.image_url!=='missing.png'?bt.image_url:'';
        const go=`/go/gmgn?from=${encodeURIComponent('memes:'+net+':'+(bt.address||''))}&l=${lang}`;
        return `<tr><td class="l"><span class="asset">${img?`<span class="ic"><img src="${esc(img)}" alt="" loading="lazy" width="26" height="26"></span>`:`<span class="ic" style="background:#64748b">${esc(sym.slice(0,2))}</span>`}<span><span class="nm">${esc(bt.name||sym)}</span><span class="tk">${esc(sym)} ${flags.join('')}</span></span></span></td>
          <td class="num">${fmtPrice(+a.base_token_price_usd)}</td><td class="num ${cls(c1)}">${fmtPct(c1)}</td><td class="num ${cls(c24)}">${fmtPct(c24)}</td>
          <td class="num hide-sm">${big(vol)}</td><td class="num hide-sm">${big(liq)}</td><td class="num hide-sm">${age(a.pool_created_at)}</td>
          <td><a class="buy" href="${go}" target="_blank" rel="sponsored nofollow noopener">${esc(L.trade)}</a></td></tr>` });
      box.innerHTML=rows.join('')||'<tr><td colspan="8" class="empty">—</td></tr>' }).catch(()=>{ box.innerHTML='<tr><td colspan="8" class="empty">—</td></tr>' }) }
  $$('#dexn button').forEach(b=>b.onclick=()=>{ net=b.dataset.n; $$('#dexn button').forEach(x=>x.classList.toggle('on',x===b)); box.innerHTML='<tr><td colspan="8" class="empty">…</td></tr>'; load() });
  load(); setInterval(()=>{ if(!document.hidden) load() },60000);
})();
/* ---------- share buttons ---------- */
(function(){
  const bars=$$('.sharebar'); if(!bars.length) return;
  const page=location.origin+location.pathname, title=(document.querySelector('h1')||{}).textContent||document.title;
  const u=src=>encodeURIComponent(page+'?utm_source='+src+'&utm_medium=share'), tt=encodeURIComponent(title.trim());
  const N=[['Telegram','#229ED9',`https://t.me/share/url?url=${u('telegram')}&text=${tt}`,'✈'],['X','#000',`https://x.com/intent/post?url=${u('x')}&text=${tt}`,'𝕏'],
    ['WhatsApp','#25D366',`https://wa.me/?text=${tt}%20${u('whatsapp')}`,'✆'],['Facebook','#1877F2',`https://www.facebook.com/sharer/sharer.php?u=${u('facebook')}`,'f'],
    ['Reddit','#FF4500',`https://www.reddit.com/submit?url=${u('reddit')}&title=${tt}`,'r'],['LinkedIn','#0A66C2',`https://www.linkedin.com/sharing/share-offsite/?url=${u('linkedin')}`,'in']];
  bars.forEach(bar=>{
    bar.innerHTML=`<span>${esc(bar.dataset.l)}:</span>`+(navigator.share?`<button class="sh" data-native style="background:var(--accent)">↗</button>`:'')+
      N.map(([n,c,h,ic])=>`<a class="sh" href="${h}" target="_blank" rel="noopener" title="${n}" aria-label="${n}" style="background:${c}">${ic}</a>`).join('')+
      `<button class="sh" data-copy title="${esc(T.copy||'Copy')}" style="background:#64748b">⧉</button>`;
    const nb=bar.querySelector('[data-native]'); if(nb) nb.onclick=()=>navigator.share({title,url:page+'?utm_source=native&utm_medium=share'}).catch(()=>{});
    bar.querySelector('[data-copy]').onclick=e=>{ navigator.clipboard&&navigator.clipboard.writeText(page+'?utm_source=copy&utm_medium=share'); e.currentTarget.textContent='✓' };
  });
})();

/* ---------- returns heatmap on asset pages (day / month / quarter) ---------- */
(function(){
  const box=$('#seas'); if(!box) return;
  const C=JSON.parse(box.dataset.cfg), t=C.t, loc=lang==='zh'?'zh-CN':lang==='fil'?'fil-PH':lang;
  let dn=null; try{ dn=new Intl.DisplayNames([loc],{type:'dateTimeField'}) }catch(e){}
  const cap=s=>s?s[0].toLocaleUpperCase(loc)+s.slice(1):s, L=(k,f)=>cap(dn?dn.of(k):f);
  const MN=Array.from({length:12},(_,i)=>new Date(2021,i,15).toLocaleString(loc,{month:'short'}));
  const pc=v=>v==null?'':(v>=0?'+':'−')+(Math.abs(v)*100).toFixed(Math.abs(v)>=10?0:Math.abs(v)>=1?1:2)+'%';
  const cell=(v,open)=>v==null?'<td></td>':`<td class="${v>0.001?'up':v<-0.001?'dn':'fl'}${open?' open':''}" style="--a:${Math.min(1,.35+Math.abs(v)*3).toFixed(2)}" ${open?`title="${esc(t.open)}"`:''}>${pc(v)}</td>`;
  const med=a=>{ if(!a.length) return null; const s=[...a].sort((x,y)=>x-y), k=s.length>>1; return s.length%2?s[k]:(s[k-1]+s[k])/2 };
  const modes=[...(C.bn?[['d',L('day','Day')]]:[]),['m',L('month','Month')],['q',L('quarter','Quarter')]];
  let mode='m', P=null, D=null;
  $('#seasm').innerHTML=modes.map(([k,l])=>`<button data-m="${k}" class="${k===mode?'on':''}">${esc(l)}</button>`).join('');
  $$('#seasm button').forEach(b=>b.onclick=async()=>{ mode=b.dataset.m; $$('#seasm button').forEach(x=>x.classList.toggle('on',x===b)); draw() });
  const ym=s=>{ const [y,m]=s.split('-').map(Number); return y*12+m-1 };
  function monthly(){ const s0=ym(P.start), rows={};
    P.p.forEach((v,i)=>{ if(!i) return; const k=s0+i, y=Math.floor(k/12), m=k%12; (rows[y]=rows[y]||{})[m]=v/P.p[i-1]-1 });
    const yr={}; for(const y in rows){ const endI=Math.min(P.p.length-1,(+y)*12+11-s0), stI=(+y)*12-1-s0; if(stI>=0) yr[y]=P.p[endI]/P.p[stI]-1 }
    return {rows,yr,last:s0+P.p.length-1} }
  function qrows(){ const s0=ym(P.start), last=s0+P.p.length-1, rows={}; const px=k=>P.p[k-s0];
    for(let y=Math.floor(s0/12);y<=Math.floor(last/12);y++) for(let q=0;q<4;q++){ const e=Math.min(y*12+q*3+2,last), b=y*12+q*3-1;
      if(b<s0||e<y*12+q*3) continue; (rows[y]=rows[y]||{})[q]=px(e)/px(b)-1 }
    return {rows,last} }
  function cards(M){ const now=M.last, y=Math.floor(now/12), m=now%12, ys=Object.keys(M.rows).map(Number).filter(x=>x<y);
    const mtd=M.rows[y]&&M.rows[y][m], mm=ys.map(x=>M.rows[x][m]).filter(v=>v!=null);
    const Q=qrows(), q=Math.floor(m/3), qtd=Q.rows[y]&&Q.rows[y][q], qq=ys.map(x=>Q.rows[x]&&Q.rows[x][q]).filter(v=>v!=null);
    const ytd=M.yr[y], yy=ys.map(x=>M.yr[x]).filter(v=>v!=null);
    const c=(lab,v,arr)=>`<div class="card stat"><div class="k">${esc(lab)}</div><div class="v ${cls(v)}">${v==null?'—':pc(v)}</div><div class="s muted">${esc(t.med)} ${arr.length?pc(med(arr)):'—'} · ${esc(t.up)}: ${arr.filter(v=>v>0).length}/${arr.length}</div></div>`;
    $('#seasc').innerHTML=`<div class="stats">${c(t.mtd+' · '+MN[m],mtd,mm)}${c(t.qtd+' · Q'+(q+1),qtd,qq)}${c(t.ytd+' · '+y,ytd,yy)}</div>` }
  async function draw(){ const g=$('#seasg');
    if(!P){ try{ P=await fetch(`${BASE}/assets/p/${C.id}.json?v=${WI.v}`).then(r=>r.json()) }catch(e){ g.innerHTML=''; return } }
    const M=monthly(); cards(M);
    if(mode==='m'){ const ys=Object.keys(M.rows).map(Number).sort((a,b)=>b-a);
      g.innerHTML=`<table class="seast"><thead><tr><th></th>${MN.map(x=>`<th>${esc(x)}</th>`).join('')}<th>${esc(L('year','Year'))}</th></tr></thead><tbody>`+
        ys.map(y=>`<tr><th>${y}</th>${MN.map((_,m)=>cell(M.rows[y][m], y*12+m===M.last)).join('')}${cell(M.yr[y], y===Math.floor(M.last/12))}</tr>`).join('')+
        `<tr class="med"><th>${esc(t.med)}</th>${MN.map((_,m)=>{ const a=ys.filter(y=>y*12+m<M.last).map(y=>M.rows[y][m]).filter(v=>v!=null); return cell(a.length?med(a):null) }).join('')}<td></td></tr></tbody></table>`; return }
    if(mode==='q'){ const Q=qrows(), ys=Object.keys(Q.rows).map(Number).sort((a,b)=>b-a);
      g.innerHTML=`<table class="seast q"><thead><tr><th></th>${[1,2,3,4].map(q=>`<th>Q${q}</th>`).join('')}<th>${esc(L('year','Year'))}</th></tr></thead><tbody>`+
        ys.map(y=>`<tr><th>${y}</th>${[0,1,2,3].map(q=>cell(Q.rows[y][q], y*12+q*3+2>Q.last)).join('')}${cell(M.yr[y], y===Math.floor(M.last/12))}</tr>`).join('')+'</tbody></table>'; return }
    if(!D){ g.innerHTML='<div class="bload"><i></i></div>';
      try{ D=await fetch(`https://data-api.binance.vision/api/v3/klines?symbol=${C.bn}&interval=1d&limit=400`).then(r=>r.json()) }catch(e){ D=[] } }
    const by={}; D.forEach((k,i)=>{ if(!i) return; const d=new Date(k[0]), key=d.getUTCFullYear()*12+d.getUTCMonth(); (by[key]=by[key]||{})[d.getUTCDate()]=k[4]/D[i-1][4]-1 });
    const keys=Object.keys(by).map(Number).sort((a,b)=>b-a).slice(0,12), today=new Date();
    g.innerHTML=`<table class="seast d"><thead><tr><th></th>${Array.from({length:31},(_,i)=>`<th>${i+1}</th>`).join('')}</tr></thead><tbody>`+
      keys.map(k=>`<tr><th>${esc(MN[k%12])} ${String(Math.floor(k/12)).slice(2)}</th>${Array.from({length:31},(_,i)=>cell(by[k][i+1], k===today.getUTCFullYear()*12+today.getUTCMonth()&&i+1===today.getUTCDate())).join('')}</tr>`).join('')+
      `</tbody></table><p class="muted" style="font-size:12px;margin:8px 0 0">${esc(t.dnote)}</p>` }
  const io=new IntersectionObserver(es=>{ if(es.some(e=>e.isIntersecting)){ io.disconnect(); draw() } },{rootMargin:'400px'}); io.observe(box);
})();
})();

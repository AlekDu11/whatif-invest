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
function refFor(a){ const r=REF[a.i]||REF_DEFAULT[a.c]; return r&&r.url?r:null }
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
  $('#tabs').innerHTML=TABS.map(t=>`<button data-t="${t}" class="${t===tab?'on':''}">${T[t]}</button>`).join('');
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
    $('#mthead').innerHTML='<tr>'+COLS.map(([c,l,cl])=>{ const s=(c===sortK||(c==='n'&&sortK==='o'));
      const sortable=!['buy','sp','go'].includes(c);
      return `<th class="${cl}${s?' sorted':''}" ${sortable?`data-k="${c}"`:''}>${l}${sortable&&l?`<span class="ar">${s?(sortDir>0?'↑':'↓'):'↕'}</span>`:''}</th>`}).join('')+'</tr>';
    $$('#mthead th[data-k]').forEach(th=>th.onclick=()=>{ let kk=th.dataset.k; if(kk==='n') kk='o';
      if(sortK===kk) sortDir=-sortDir; else {sortK=kk; sortDir=(kk==='name'||kk==='o')?1:-1} draw() });
    tb.innerHTML=rows.length?rows.map((a,i)=>`<tr>
      <td class="l n hide-sm">${i+1}</td>
      <td class="l"><a class="asset" href="${url(a.i)}">${icon(a)}<span><span class="nm">${esc(nm(a))}</span><span class="tk">${esc(a.t)}</span></span></a></td>
      <td>${buyBtn(a)}</td>
      <td class="num">${fmtPrice(a.pr)}</td>
      <td class="num ${cls(a.ch)}">${fmtPct(a.ch)}</td>
      <td class="num hide-sm ${cls(a.r1)}">${fmtPct(a.r1)}</td>
      <td class="num hide-sm ${cls(a.r3)}">${fmtPct(a.r3)}</td>
      <td><span class="pill ${cls(a.r5)}">${fmtPct(a.r5)}</span></td>
      <td class="hide-sm">${spark(a.sp)}</td>
      <td class="hide-sm"><a class="calc" href="${url(a.i)}">${T.calc} →</a></td></tr>`).join('')
      :`<tr><td colspan="10" class="empty">${T.nothing}</td></tr>`;
    $('#mtmore').innerHTML=total>shown?`<button class="more">${T.more} (${fmt(T.shown,{a:shown,b:total})})</button>`:'';
    const mb=$('#mtmore button'); if(mb) mb.onclick=()=>{shown+=100;draw()};
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
      res.map(r=>{ const p=r.val-r.inv, u=T['u_'+r.a.c]||r.a.t, late=r.from>startI?`<div class="muted" style="font:500 11px Inter">${T.frm} ${mlabel(i2ym(r.from))}</div>`:'';
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
    ticks.forEach(v=>{const y=fy(v);g+=`<line x1="${L}" x2="${W-R}" y1="${y}" y2="${y}" stroke="#eef0f3"/><text x="${L-8}" y="${y+4}" fill="#9aa1ad" font-size="11.5" text-anchor="end" font-family="JetBrains Mono">${shortUsd(v)}</text>`});
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
  ['#ctaBuy','#ctaBuy2'].forEach(s=>{const b=$(s); if(b){b.href=r.url; b.target='_blank'; b.rel='sponsored noopener'}}) })();

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

/* ---------- live crypto prices (Binance WebSocket, only symbols shown on the page) ---------- */
(function(){
  if(!('WebSocket' in window)) return;
  const heat=c=>{ c=Math.max(-.1,Math.min(.1,c)); if(c>=0){const k=c/.1;return `rgb(${232-212*k|0},${246-82*k|0},${237-160*k|0})`} const k=-c/.1;return `rgb(${253-24*k|0},${236-164*k|0},${236-159*k|0})` };
  let ws=null, tries=0, want='';
  function symbols(){ const ids=new Set($$('[data-p],[data-c],[data-h]').map(el=>el.dataset.p||el.dataset.c||el.dataset.h));
    return [...ids].map(id=>BYID[id]).filter(a=>a&&a.c==='crypto').map(a=>a.t.toLowerCase()+'usdt@miniTicker').slice(0,200) }
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
    s.textContent=el.dataset.cfg; wrap.appendChild(s); el.appendChild(wrap) };
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

/* ---------- market bubbles (canvas, own physics, live via wi:tick) ---------- */
(function(){
  const box=$('.bub'); if(!box) return;
  const cv=box.querySelector('canvas'), ctx=cv.getContext('2d'), N=+box.dataset.n||100;
  let per='ch', cat='crypto', bs=[], W=0, H=0, hover=null, dpr=Math.min(2,window.devicePixelRatio||1);
  const imgs={};
  const val=a=>per==='ch'?a.ch:per==='y1'?(a.sp&&a.sp.length>1?a.sp[a.sp.length-1]/a.sp[0]-1:null):a.r1;
  function pick(){ return IDX.filter(a=>(cat==='all'||a.c===cat)&&val(a)!=null).sort((x,y)=>x.o-y.o).slice(0,N) }
  function size(){ const r=box.getBoundingClientRect(); W=r.width; H=r.height; cv.width=W*dpr; cv.height=H*dpr; cv.style.width=W+'px'; cv.style.height=H+'px'; ctx.setTransform(dpr,0,0,dpr,0,0) }
  function radii(){ const vs=bs.map(b=>Math.abs(val(b.a))||0); const cap=per==='ch'?.25:3;
    const raw=bs.map((b,k)=>Math.sqrt(Math.min(vs[k],cap)+(per==='ch'?.004:.05)));
    const tot=raw.reduce((s,r)=>s+r*r,0)||1, k=Math.sqrt(W*H*.5/(Math.PI*tot));
    bs.forEach((b,i)=>{ b.tr=Math.max(10,Math.min(Math.min(W,H)/4.2,raw[i]*k)) }) }
  function build(){ const keep=Object.fromEntries(bs.map(b=>[b.a.i,b]));
    bs=pick().map(a=>keep[a.i]||{a,x:Math.random()*W,y:Math.random()*H,vx:0,vy:0,r:4});
    bs.forEach(b=>{ if(b.a.l&&!imgs[b.a.i]){ const im=new Image(); im.src=b.a.l; im.onload=()=>{imgs[b.a.i]=im}; imgs[b.a.i]=null } });
    radii() }
  function step(){
    for(const b of bs){ b.r+=(b.tr-b.r)*.08; b.vx+=(W/2-b.x)*.00025; b.vy+=(H/2-b.y)*.00025; }
    for(let i=0;i<bs.length;i++){ const p=bs[i]; for(let j=i+1;j<bs.length;j++){ const q=bs[j];
      const dx=q.x-p.x, dy=q.y-p.y, d=Math.hypot(dx,dy)||.01, m=p.r+q.r+1.5;
      if(d<m){ const o=(m-d)/d*.5, ox=dx*o, oy=dy*o; p.x-=ox; p.y-=oy; q.x+=ox; q.y+=oy; p.vx-=ox*.02; p.vy-=oy*.02; q.vx+=ox*.02; q.vy+=oy*.02 } } }
    for(const b of bs){ b.vx*=.9; b.vy*=.9; b.x+=b.vx; b.y+=b.vy;
      if(b.x<b.r){b.x=b.r;b.vx*=-.5} if(b.x>W-b.r){b.x=W-b.r;b.vx*=-.5} if(b.y<b.r){b.y=b.r;b.vy*=-.5} if(b.y>H-b.r){b.y=H-b.r;b.vy*=-.5} } }
  function draw(){ ctx.clearRect(0,0,W,H);
    for(const b of bs){ const v=val(b.a)||0, up=v>=0, k=Math.min(1,Math.abs(v)/(per==='ch'?.1:1));
      const c=up?[20,164,77]:[229,72,77];
      const g=ctx.createRadialGradient(b.x,b.y,b.r*.2,b.x,b.y,b.r);
      g.addColorStop(0,`rgba(${c},${.05+.15*k})`); g.addColorStop(1,`rgba(${c},${.35+.5*k})`);
      ctx.beginPath(); ctx.arc(b.x,b.y,b.r,0,7); ctx.fillStyle=g; ctx.fill();
      ctx.lineWidth=b===hover?3:1.5; ctx.strokeStyle=`rgba(${c},${b===hover?1:.85})`; ctx.stroke();
      if(b.r>14){ const im=imgs[b.a.i], fs=Math.max(9,Math.min(20,b.r*.34));
        let y=b.y; if(im&&b.r>26){ const s=b.r*.5; ctx.save(); ctx.beginPath(); ctx.arc(b.x,b.y-b.r*.38,s/2,0,7); ctx.clip(); ctx.drawImage(im,b.x-s/2,b.y-b.r*.38-s/2,s,s); ctx.restore(); y=b.y+b.r*.12 }
        ctx.fillStyle='#161a23'; ctx.textAlign='center'; ctx.font=`700 ${fs}px Inter,system-ui,sans-serif`; ctx.fillText(b.a.t.slice(0,6),b.x,y+fs*.2);
        if(b.r>20){ ctx.font=`600 ${fs*.78}px Inter,system-ui,sans-serif`; ctx.fillStyle=up?'#0b6b30':'#a3262b'; ctx.fillText(fmtPct(v,1),b.x,y+fs*1.15) } } } }
  let raf; function loop(){ step(); draw(); raf=requestAnimationFrame(loop) }
  const at=e=>{ const r=cv.getBoundingClientRect(), x=e.clientX-r.left, y=e.clientY-r.top; return bs.find(b=>Math.hypot(b.x-x,b.y-y)<b.r) };
  cv.addEventListener('mousemove',e=>{ hover=at(e)||null; cv.style.cursor=hover?'pointer':'default'; cv.title=hover?`${nm(hover.a)} · ${fmtPrice(hover.a.pr)} · ${fmtPct(val(hover.a))}`:'' });
  cv.addEventListener('click',e=>{ const b=at(e); if(b) location.href=url(b.a.i) });
  $$('#bper button').forEach(b=>b.onclick=()=>{ per=b.dataset.v; $$('#bper button').forEach(x=>x.classList.toggle('on',x===b)); build() });
  $$('#bcat button').forEach(b=>b.onclick=()=>{ cat=b.dataset.v; $$('#bcat button').forEach(x=>x.classList.toggle('on',x===b)); build() });
  document.addEventListener('wi:tick',()=>{ if(per==='ch') radii() });
  addEventListener('resize',()=>{ size(); radii() });
  document.addEventListener('visibilitychange',()=>{ if(document.hidden) cancelAnimationFrame(raf); else loop() });
  const io=new IntersectionObserver(es=>{ if(es[0].isIntersecting){ io.disconnect(); size(); build(); loop() } }); io.observe(box);
})();
})();

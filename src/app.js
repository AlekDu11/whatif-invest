/* WhatIfStack — front-end. Data: window.WI (index of all assets, from index.js),
   page config: window.PAGE, referral links: window.REF / window.REF_DEFAULT (ref.js).
   Price series are loaded on demand from /assets/p/<id>.json. */
/* owner 2026-11-23 (save Vercel requests): background polling pauses when the tab is hidden or nobody touched the page for 20 min */
(function(){ let t=Date.now(); const up=()=>{ t=Date.now() }; ['pointerdown','keydown','scroll','touchstart','mousemove'].forEach(e=>addEventListener(e,up,{passive:true}));
  document.addEventListener('visibilitychange',()=>{ if(!document.hidden) up() }); window.wiAway=()=>document.hidden||Date.now()-t>1200000 })();
(function(){
const WI = window.WI, PAGE = window.PAGE || {}, BASE = PAGE.base || '';
const lang = PAGE.lang || 'uk';
const $ = (s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const IDX = WI.a, BYID = Object.fromEntries(IDX.map(a=>[a.i,a]));
IDX.forEach(a=>{ if(a.h==null) a.h=9999; if(a.l===1) a.l='/assets/logo/'+a.i+'.webp' });
const REF = window.REF||{}, REF_DEFAULT = window.REF_DEFAULT||{};

const T = window.I18N || {};
const fmt = (s,o)=>String(s).replace(/\{(\w+)\}/g,(m,k)=>o[k]!=null?o[k]:m);

/* ---------- helpers ---------- */
const NAMES=PAGE.names||{};
const nm = a => ((a.c==='metal'||a.c==='cmd')&&NAMES[a.i]) ? NAMES[a.i] : lang==='uk' ? a.n : (a.ne||a.n);
const url = id => { const a=BYID[id]; if(a&&a.st) return `${PAGE.prefix||''}/${a.t.toLowerCase()}/`; return (PAGE.full||(a&&a.o<PAGE.topn)) ? `${PAGE.prefix}/${id}/` : `${BASE}/en/${id}/` };
const esc = s => String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
// Display currency (header switcher): all JS-rendered money and server numbers marked [data-u] are converted from USD
let CCY='USD'; try{ CCY=localStorage.getItem('wi_ccy')||'USD' }catch(e){}
const ccyRate=()=>CCY==='USD'?1:((WI.fx||{})[CCY]||1);
if(CCY!=='USD'&&!(WI.fx||{})[CCY]) CCY='USD';
const _nf={}; const NF=(k,o)=>_nf[k]||(_nf[k]=(()=>{ try{ return new Intl.NumberFormat(T.intl||'en',o) }catch(e){ return new Intl.NumberFormat('en',o) } })());
const _cur=(min,max,compact)=>NF(CCY+min+'|'+max+(compact?'c':''),{style:'currency',currency:CCY,currencyDisplay:'narrowSymbol',minimumFractionDigits:min,maximumFractionDigits:max,...(compact?{notation:'compact'}:{})});
function fmtUsd(v){ if(v==null) return '—'; const x=v*ccyRate(), a=Math.abs(x);
  if(a>=1e6) return _cur(0,2,true).format(x).replace('-','−'); return _cur(0,a>=1000?0:2).format(x).replace('-','−') }
function fmtPrice(v){ if(v==null) return '—'; const x=v*ccyRate(); const d=x>=1?2:x>=0.01?4:8;
  return _cur(x>=1?2:0,d).format(x) }
function fmtPct(p,dec){ if(p==null||!isFinite(p)) return '—'; const a=Math.abs(p*100);
  return (p>=0?'+':'−')+NF('p'+(dec!=null?dec:(a>=100?0:a>=10?1:2)),{maximumFractionDigits:dec!=null?dec:(a>=100?0:a>=10?1:2)}).format(a)+'%' }
const cls = p => p==null?'':p>=0?'good':'bad';
window.WIF={fmtUsd:v=>fmtUsd(v),fmtPct:(p,d)=>fmtPct(p,d),cls,BYID};   // for IIFEs appended outside the main scope
function hue(s){let h=0;for(const c of s)h=(h*31+c.charCodeAt(0))%360;return h}
function icon(a,big){ const c=big?' lg':''; if(a.mi) return `<span class="ic${c} mi" style="background:${a.mi[0]}">${a.mi[1]}</span>`; const k=(WI.sp||{})[a.i];
  if(k!=null){ const [C,R]=WI.spc; return `<span class="ic sp${c}" style="background-position:${(k%C*100/(C-1)).toFixed(3)}% ${(Math.floor(k/C)*100/Math.max(1,R-1)).toFixed(3)}%"></span>` }
  if(a.l) return `<span class="ic${c}"><img src="${esc(a.l)}" alt="" loading="lazy" width="26" height="26"></span>`;
  return `<span class="ic${c}" style="background:hsl(${hue(a.t)} 55% 52%)">${esc(a.t.slice(0,2))}</span>` }
function spark(arr,w=110,h=34){ if(!arr||arr.length<2) return '';
  const mn=Math.min(...arr),mx=Math.max(...arr),r=mx-mn||1, up=arr[arr.length-1]>=arr[0];
  const pts=arr.map((v,i)=>`${(i/(arr.length-1)*w).toFixed(1)},${(h-2-(v-mn)/r*(h-4)).toFixed(1)}`).join(' ');
  return `<svg class="spk ${up?'up':'dn'}" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" aria-hidden="true"><polygon points="0,${h} ${pts} ${w},${h}"/><polyline points="${pts}"/></svg>` }
const goUrl=(u,extra)=>u&&u.startsWith('/go/')?`${u}?from=${encodeURIComponent(location.pathname)}&l=${lang}${extra||''}`:u;
// crypto: send buyers only to an exchange that really lists the coin (index: bn = Binance, x = g Gate / m MEXC / y Bybit / o OKX); none → no button
const XREF={o:{url:'/go/okx',where:'OKX'},g:{url:'/go/gate',where:'Gate'},m:{url:'/go/mexc',where:'MEXC'},y:{url:'/go/bybit',where:'Bybit'},n:{url:'/go/bingx',where:'BingX'}};
function refFor(a){ const RL=(window.REF_LANG||{})[a.c]; let r=REF[a.i];
  if(!r&&a.c==='crypto'){ if(a.bn) r=(RL&&RL.langs.includes(lang)&&a.o<=150)?RL:REF_DEFAULT.crypto; else r=XREF[a.x]||null }
  if(!r) r=(RL&&RL.langs.includes(lang)?RL:null)||(a.c==='crypto'?null:REF_DEFAULT[a.c]);
  return r&&r.url?Object.assign({},r,{url:goUrl(r.url)}):null }
function buyBtn(a){ const r=refFor(a); return r?`<a class="buy" href="${esc(r.url)}" target="_blank" rel="sponsored noopener" title="${esc(r.where)} · ${T.aff}">${T.buy}</a>`:'' }
window.WIX={T,nm,url,esc,fmtUsd,fmtPrice,fmtPct,cls,icon,spark,buyBtn,BYID,IDX,lang};
const bs=$('#buyslot'); if(bs&&BYID[bs.dataset.id]){ const r=refFor(BYID[bs.dataset.id]); if(r) bs.innerHTML=`<a class="btn" href="${esc(r.url)}" target="_blank" rel="sponsored noopener">${T.buy} ${esc(BYID[bs.dataset.id].t)} · ${esc(r.where)}</a>` }

/* ---------- global search (header) ---------- */
(function(){
  const inp=$('#gs'), box=$('#gres'); if(!inp) return;
  inp.placeholder=T.search; let sel=0, items=[];
  const run=()=>{ const q=inp.value.trim().toLowerCase(); if(!q){box.style.display='none';return}
    const sc=a=>{ const t=a.t.toLowerCase(), n=nm(a).toLowerCase(), ne=(a.ne||a.n||'').toLowerCase(), al=(a.al||'').toLowerCase();
      if(t===q) return 0; if(n.startsWith(q)||ne.startsWith(q)||t.startsWith(q)) return 1; if(al.split(' ').some(w=>w.startsWith(q))) return 2;
      if(n.split(/[\s.-]+/).some(w=>w.startsWith(q))||ne.split(/[\s.-]+/).some(w=>w.startsWith(q))) return 3; if(q.length>=3&&(n.includes(q)||ne.includes(q))) return 4; return 9 };
    items=IDX.map(a=>[sc(a),a]).filter(x=>x[0]<9).sort((x,y)=>x[0]-y[0]||x[1].o-y[1].o).slice(0,8).map(x=>x[1]);
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
  let tab=PAGE.tab||'all', q='', sortK=PAGE.sort||'o', sortDir=1, shown=PAGE.home?20:100, pg=0; const STEP=PAGE.home?50:100, PER=PAGE.home?20:50;
  const TABS=['all','crypto','stock','etf','metal','cmd','lead','lag'], ONLY=PAGE.only?new Set(PAGE.only):null;   // category pages: only their assets
  $('#tabs').innerHTML=TABS.map(t=>`<button data-t="${t}" class="${t===tab?'on':''}">${T[t]}</button>`).join('')+(PAGE.wa?`<a class="tablink" href="${PAGE.wau}">🌍 ${esc(PAGE.wa)}</a>`:'');
  $$('#tabs button').forEach(b=>b.onclick=()=>{tab=b.dataset.t; $$('#tabs button').forEach(x=>x.classList.toggle('on',x===b));
    if(tab==='lead'){sortK='r5';sortDir=-1} else if(tab==='lag'){sortK='r5';sortDir=1} else if(sortK==='r5'&&(sortDir)){sortK='o';sortDir=1}
    shown=PAGE.home?20:100; pg=0; draw()});
  const f=$('#flt'); f.placeholder=T.filter; f.setAttribute('aria-label',T.filter); f.oninput=()=>{q=f.value.trim().toLowerCase(); shown=PAGE.home?20:100; pg=0; draw()};
  try{ const sq=new URLSearchParams(location.search).get('q'); if(sq){ f.value=sq; f.oninput() } }catch(e){}
  // two views: market (CoinMarketCap-style: 7d, market cap, volume, 7-day chart) and DCA returns (tabs «DCA leaders/laggards»)
  const COLS_DCA=[['n','#','l n hide-sm'],['name',T.name,'l'],['buy','','hide-sm'],['pr',T.price,''],['ch',T.chg,''],['r1',T.d1,'hide-sm'],['r3',T.d3,'hide-sm'],['r5',T.d5,''],['sp',T.spark,'hide-sm'],['go','','hide-sm']];
  const COLS_MKT=[['n','#','l n hide-sm'],['name',T.name,'l'],['buy','','hide-sm'],['pr',T.price,''],['ch',T.chg,''],['w7',T.mk_d7||'7d','hide-sm'],['mc',T.mk_mcap||'Market cap','hide-sm'],['vo',T.mk_vol||'Volume','hide-md'],['k7',T.mk_k7||'7d','hide-sm'],['go','','hide-sm']];
  let COLS=COLS_MKT, ST=[];
  fetch(`${BASE}/assets/mkt.json?v=${WI.v}`).then(r=>r.json()).then(M=>{
    Object.entries(M.a||{}).forEach(([i,v])=>{ const a=BYID[i]; if(a){ a.mc=v[0]; a.vo=v[1]; a.w7=v[2]; a.k7=v[3]; a.rk=v[4]; if(v[5]) a.sp=v[5]; if(v.length>6){ a.r1=v[6]; a.r3=v[7]; a.r5=v[8] } } });
    const cr=IDX.filter(a=>a.c==='crypto'&&a.rk).sort((x,y)=>x.rk-y.rk);
    ST=(M.st||[]).filter(x=>x.r&&x.pr).map(x=>{ const prev=cr.filter(a=>a.rk<x.r).pop(); return {i:'st-'+x.t.toLowerCase(), st:1, c:'crypto', n:x.n, t:x.t, pr:x.pr, ch:x.ch, l:x.l, mc:x.mc, vo:x.vo, w7:x.w7, k7:x.k7, rk:x.r, o:(prev?prev.o:-1)+0.5-1/(x.r+2)} });
    draw() }).catch(()=>{});
  function draw(){
    COLS=(PAGE.home||PAGE.dca||tab==='lead'||tab==='lag')?COLS_DCA:COLS_MKT;   // home keeps its approved DCA columns
    let rows=(tab==='crypto'&&!ONLY?IDX.concat(ST):IDX).filter(a=>{
      if(ONLY&&!ONLY.has(a.i)) return false;
      if(tab==='crypto'||tab==='stock'||tab==='etf'||tab==='metal'||tab==='cmd'){ if(a.c!==tab) return false }
      if((tab==='lead'||tab==='lag')&&a.r5==null) return false;
      return !q||a.t.toLowerCase().includes(q)||nm(a).toLowerCase().includes(q) });
    // crypto tab: «#» = market-cap rank like CoinMarketCap (stablecoins included); home «All» keeps its own mix
    const k=sortK==='n'?'o':(sortK==='o'&&PAGE.home&&tab==='all'&&!q?'h':(sortK==='o'&&tab==='crypto'&&ST.length?'rk':sortK));
    rows.sort((x,y)=>{ const vx=k==='name'?nm(x):x[k], vy=k==='name'?nm(y):y[k];
      if(vx==null&&vy==null) return x.o-y.o; if(vx==null) return 1; if(vy==null) return -1;
      return (typeof vx==='string'?vx.localeCompare(vy):vx-vy)*sortDir });
    const total=rows.length, paged=true, np=Math.max(1,Math.ceil(total/PER)); if(pg>=np) pg=np-1; const off=paged?pg*PER:0;
    rows=paged?rows.slice(off,off+PER):rows.slice(0,shown);
    const split=!!$('#mt2'), top=split?rows.slice(0,10):rows, rest=split?rows.slice(10):[];
    const head='<tr>'+COLS.map(([c,l,cl])=>{ const s=(c===sortK||(c==='n'&&sortK==='o'));
      const sortable=!['buy','sp','go','k7'].includes(c);
      return `<th class="${cl}${s?' sorted':''}" ${sortable?`data-k="${c}"`:''}>${l}${sortable&&l?`<span class="ar">${s?(sortDir>0?'↑':'↓'):'↕'}</span>`:''}</th>`}).join('')+'</tr>';
    $('#mthead').innerHTML=head; if(split) $('#mthead2').innerHTML=head;
    $$('#mthead th[data-k],#mthead2 th[data-k]').forEach(th=>th.onclick=()=>{ let kk=th.dataset.k; if(kk==='n') kk='o';
      if(sortK===kk) sortDir=-sortDir; else {sortK=kk; sortDir=(kk==='name'||kk==='o')?1:-1} pg=0; draw() });
    const cvu=`${PAGE.prefix}/converter/`;
    const cells=a=>COLS===COLS_DCA?`
      <td class="num hide-sm ${cls(a.r1)}">${fmtPct(a.r1)}</td>
      <td class="num hide-sm ${cls(a.r3)}">${fmtPct(a.r3)}</td>
      <td><span class="pill ${cls(a.r5)}">${fmtPct(a.r5)}</span></td>
      <td class="hide-sm">${spark(a.sp)}</td>`:`
      <td class="num hide-sm ${cls(a.w7)}">${fmtPct(a.w7)}</td>
      <td class="num hide-sm">${a.mc?fmtUsd(a.mc):'—'}</td>
      <td class="num hide-md">${a.vo?fmtUsd(a.vo):'—'}</td>
      <td class="hide-sm">${spark(a.k7||a.sp)}</td>`;
    const tr=(a,i)=>a.st?`<tr class="strow">
      <td class="l n hide-sm">${off+i+1}</td>
      <td class="l"><button class="star" data-s="${a.i}" aria-label="☆">☆</button><a class="asset" href="${PAGE.prefix}/${a.t.toLowerCase()}/">${icon(a)}<span><span class="nm">${esc(a.n)}</span><span class="tk">${esc(a.t)} · ${esc(T.mk_stable||'Stablecoin')}</span></span></a></td>
      <td class="hide-sm"></td><td class="num">${fmtPrice(a.pr)}</td><td class="num ${cls(a.ch)}">${fmtPct(a.ch)}</td>${cells(a)}
      <td class="hide-sm"></td></tr>`:`<tr>
      <td class="l n hide-sm">${off+i+1}</td>
      <td class="l"><button class="star" data-s="${a.i}" aria-label="☆">☆</button><a class="asset" href="${url(a.i)}">${icon(a)}<span><span class="nm">${esc(nm(a))}</span><span class="tk">${esc(a.t)}${lang!=='en'&&url(a.i).startsWith(BASE+'/en/')?'<i class="enb" title="English">EN</i>':''}</span></span></a></td>
      <td class="hide-sm">${buyBtn(a)}</td>
      <td class="num" data-p="${a.i}">${fmtPrice(a.pr)}</td>
      <td class="num ${cls(a.ch)}" data-c="${a.i}">${fmtPct(a.ch)}</td>${cells(a)}
      <td class="hide-sm"><a class="calc" href="${url(a.i)}">${T.calc} →</a></td></tr>`;
    tb.innerHTML=top.length?top.map(tr).join(''):`<tr><td colspan="10" class="empty">${T.nothing}</td></tr>`;
    if(split){ $('#mt2').innerHTML=rest.map((a,i)=>tr(a,i+10)).join(''); $('#rank2').hidden=!rest.length;
      $('#mttop').innerHTML=total>10?`<a class="more" href="#rank2">${T.more} ↓</a>`:''; }
    if(paged){ const pb=(n,l,dis,on)=>`<button type="button" class="pgb${on?' on':''}" data-pg="${n}"${dis?' disabled':''}>${l}</button>`;
      let h=''; if(np>1){ h+=pb(pg-1,'‹',pg===0); const seen=new Set(); [0,1,2,pg-1,pg,pg+1,np-1].filter(n=>n>=0&&n<np).sort((a,b)=>a-b).forEach(n=>{ if(seen.has(n)) return; if(seen.size&&!seen.has(n-1)) h+='<span class="pgd">…</span>'; seen.add(n); h+=pb(n,n+1,false,n===pg) }); h+=pb(pg+1,'›',pg===np-1) }
      $('#mtmore').innerHTML=np>1?`<div class="pager">${h}<span class="muted pgi">${off+1}–${Math.min(off+PER,total)} / ${total}</span></div>`:'';
      $$('#mtmore .pgb').forEach(b=>b.onclick=()=>{ pg=+b.dataset.pg; draw(); $('#mthead').closest('.tw').scrollIntoView({block:'start',behavior:'smooth'}) }) }
    else { $('#mtmore').innerHTML=total>shown?`<button class="more">${T.more} (${fmt(T.shown,{a:shown,b:total})})</button>`:'';
      const mb=$('#mtmore button'); if(mb) mb.onclick=()=>{shown+=STEP;draw()}; }
    try{paintStars()}catch(e){}
    document.dispatchEvent(new Event('wi:rows'));   // live price streams pick up the rows now on screen
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
    const anniv=from===startI&&from<ym2i(END)&&(ym2i(END)-from)%12===0; let u=0,inv=0; const pts=[]; for(let i=from;i<=e;i++){ let c=amt*perMonth(i); if(anniv&&i===from&&freq!=='m') c=c*(1-END_DAY/new Date(Math.floor(i/12),i%12+1,0).getDate()); u+=c/P.p[i-s0]; inv+=c; pts.push({i,inv,val:u*P.p[i-s0]}) }
    return {units:u,inv,val:u*P.p[e-s0],pts,from} }

  // since select
  const sel=$('#since');
  for(let i=ym2i(END)-1;i>=ym2i('2000-01');i--){ if(i%12!==0&&i%6!==0&&i<ym2i(END)-24&&(ym2i(END)-i)%12!==0) continue;
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
      res.map(r=>{ const p=r.val-r.inv, u=(r.a.u?T.u_cmd:T['u_'+r.a.c])||r.a.t, late=r.from>startI?`<div class="muted" style="font:500 11px var(--fb)">${T.frm} ${mlabel(i2ym(r.from))}</div>`:'';
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
/* "Start DCA" buttons lead to the exchanges page (fees + recurring-buy features side by side) */

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
    for(let i=from;i<=e;i++){ let d=new Date(Math.floor(i/12),i%12+1,0).getDate(); if(i===ENDI) d=END_DAY; else if(i===from&&from===ENDI-years*12) d-=END_DAY;
      const c=amt*d; u+=c/P.p[i-s0]; inv+=c; path.push(u*P.p[i-s0]) }
    const val=u*P.p[e-s0], roi=val/inv-1;
    $('#qv').textContent=fmtUsd(val); $('#qv').className='v '+cls(roi);
    $('#qs').innerHTML=`<span class="${cls(roi)}">${fmtPct(roi)}</span> · ${esc(T.w_q_inv)} ${fmtUsd(inv)}`;
    $('#qsp').innerHTML=spark(path,300,56); $('#qmore').href=url(id) };
  $$('#qy button').forEach(b=>b.onclick=()=>{years=+b.dataset.y;$$('#qy button').forEach(x=>x.classList.toggle('on',x===b));run()});
  $('#qa').onchange=run; $('#qm').oninput=run;
  // any asset we have: type to search all of them (the select only lists the top 120)
  (function(){ const sel=$('#qa'), lab=(a)=>`${nm(a)} (${a.t})`, inp=document.createElement('input'), dl=document.createElement('datalist');
    inp.type='search'; inp.id='qas'; inp.setAttribute('list','qal'); inp.autocomplete='off'; inp.setAttribute('aria-label',sel.closest('label')?.firstChild?.textContent||'asset');
    dl.id='qal'; dl.innerHTML=IDX.map(a=>`<option value="${esc(lab(a))}">`).join('');
    const cur=BYID[sel.value]; inp.value=cur?lab(cur):''; sel.hidden=true; sel.after(inp,dl);
    const pick=()=>{ const v=inp.value.trim().toLowerCase(); if(!v) return;
      const a=IDX.find(x=>lab(x).toLowerCase()===v)||IDX.find(x=>x.t.toLowerCase()===v)||IDX.find(x=>x.n.toLowerCase()===v||(x.ne||'').toLowerCase()===v);
      if(!a) return; if(![...sel.options].some(o=>o.value===a.i)) sel.add(new Option(lab(a),a.i)); sel.value=a.i; inp.value=lab(a); inp.blur(); run() };
    inp.addEventListener('change',pick); inp.addEventListener('input',()=>{ if(IDX.some(x=>lab(x)===inp.value)) pick() });
    inp.addEventListener('focus',()=>inp.select()) })();
  run();
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
    const m=$('meta[name=theme-color]'); if(m) m.content=dark?'#080d0f':'#ffffff';
    if($('.tvw[data-done]')) location.reload() };
  if('serviceWorker' in navigator && location.protocol==='https:') addEventListener('load',()=>navigator.serviceWorker.register('/sw.js').catch(()=>{}));
})();

/* ---------- personal home: watchlist + portfolio first (only for visitors who have them) ---------- */
(function(){ const box=$('#myh'); if(!box) return; let C; try{ C=JSON.parse(box.dataset.cfg) }catch(e){ return }
  const rd=k=>{ try{ return JSON.parse(localStorage.getItem(k)||'[]') }catch(e){ return [] } };
  const hold={}; rd('wi_hold').forEach(x=>{ if(!BYID[x.id]) return; const g=hold[x.id]||(hold[x.id]={qty:0,cost:0}); g.qty+=+x.qty||0; g.cost+=+x.cost||0 });
  Object.keys(hold).forEach(k=>{ if(hold[k].qty<=1e-12) delete hold[k] });
  const ids=[...new Set([...Object.keys(hold),...rd('wi_watch').filter(i=>BYID[i])])]; if(!ids.length) return;
  const nfc=(v,c)=>{ try{ return new Intl.NumberFormat(T.intl||'en',{style:'currency',currency:c,maximumFractionDigits:Math.abs(v)>=100?0:2}).format(v) }catch(e){ return Math.round(v)+' '+c } };
  // display currency = the portfolio's choice (USD by default; USDT/USDC count as USD), the visitor's local currency in brackets
  let pc='USD'; try{ pc=localStorage.getItem('wi_pfccy')||'USD' }catch(e){} if(pc==='USDT'||pc==='USDC') pc='USD';
  const fx=(WI.fx||{}), rt=c=>c==='USD'?1:(c===C.code?C.rate:(fx[c]||null)); if(!rt(pc)) pc='USD';
  const main=v=>nfc(v*rt(pc),pc), loc=v=>C.code&&C.code!==pc&&C.rate?` <small class="muted">(≈ ${nfc(v*C.rate,C.code)})</small>`:'';
  let hide=false; try{ hide=localStorage.getItem('wi_pfhide')==='1' }catch(e){}
  const pf=()=>{ let tv=0,tc=0,d=0; const rows=[]; for(const [id,g] of Object.entries(hold)){ const a=BYID[id], v=g.qty*a.pr; tv+=v; tc+=g.cost; d+=v*(a.ch||0)/(1+(a.ch||0)); rows.push([id,v]) }
    if(!tv) return ''; const dp=tv-d?d/(tv-d):0, r=tc?tv/tc-1:0, M='••••';
    const al=rows.sort((x,y)=>y[1]-x[1]).slice(0,3).map(([id,v])=>{ const a=BYID[id], sh=v/tv; return `<a class="mrow" href="${url(id)}">${icon(a)}<span class="mn"><b>${esc(a.t)}</b><span>${esc(nm(a))}</span></span><span class="mp">${hide?M:main(v)}</span><span class="mc muted">${(sh*100).toFixed(sh<.1?1:0)}%</span></a>` }).join('');
    return `<div class="card mypf"><div class="mypfh"><span class="muted">${esc(C.pf)}</span><button class="eye" type="button" title="${esc(C.hide)}" aria-label="${esc(C.hide)}" aria-pressed="${hide}">${hide?'🙈':'👁'}</button></div>
      <b class="v">${hide?M:main(tv)}${hide?'':loc(tv)}</b>
      <span class="${cls(dp)}">${fmtPct(dp)} ${esc(C.today)}${hide?'':` · ${d<0?'−':'+'}${main(Math.abs(d))}`}</span><span class="muted">${esc(T.invested||'')}: ${hide?M:main(tc)} · <span class="${cls(r)}">${fmtPct(r)}</span></span>
      <div class="myal">${al}</div><a class="mymore" href="${C.me}">${esc(C.open)} →</a></div>` };
  const bindEye=()=>{ const e=$('#mypf .eye'); if(e) e.onclick=()=>{ hide=!hide; try{ localStorage.setItem('wi_pfhide',hide?'1':'0') }catch(e){} $('#mypf').innerHTML=pf(); bindEye() } };
  const wl=rd('wi_watch').filter(i=>BYID[i]), wids=wl.length?wl:ids;
  const top=wids.slice(0,3).map(i=>{ const a=BYID[i]; return `<a class="mrow" href="${url(i)}">${icon(a)}<span class="mn"><b>${esc(a.t)}</b><span>${esc(nm(a))}</span></span>
      <span class="mp" data-p="${i}">${fmtPrice(a.pr)}</span><span class="mc ${cls(a.ch)}" data-c="${i}">${fmtPct(a.ch)}</span></a>` }).join('');
  box.innerHTML=`<div class="myhh"><h2>${esc(C.h)}</h2><a class="calc" href="${C.me}">${esc(C.open)} →</a></div>
    <div class="mygrid"><div id="mypf">${pf()}</div><div class="card wd mywl"><div class="wt">★ ${esc(C.watch)}</div>${top}<a class="mymore" href="${C.wlu}">${esc(C.wl_all)}${wids.length>3?` (${wids.length})`:''} →</a></div><div class="card wd" id="mynews" hidden><div class="wt">📰 ${esc(C.news)}</div><div class="nlist own"></div></div></div>`;
  if(!Object.keys(hold).length) box.querySelector('#mypf').remove(); else bindEye();
  box.hidden=false;
  let t; document.addEventListener('wi:tick',()=>{ clearTimeout(t); t=setTimeout(()=>{ const el=$('#mypf'); if(el){ el.innerHTML=pf(); bindEye() } },1200) });
  fetch(C.nf+'?v='+WI.v).then(r=>r.json()).then(L=>{ const w=new Set(ids), f=L.filter(n=>(n.a||[]).some(x=>w.has(x))).slice(0,3); if(!f.length) return;
    const n=$('#mynews'); n.querySelector('.nlist').innerHTML=f.map(x=>`<a class="nrow" href="${x.u}"><b>${esc(x.t)}</b><span class="muted"><time data-t="${esc(x.d)}">${esc(x.d)}</time> · ${esc(x.a.map(i=>BYID[i]?BYID[i].t:i).slice(0,3).join(', '))}</span></a>`).join(''); n.hidden=false }).catch(()=>{});
})();

/* ---------- live quotes for US stocks, ETFs, gold and other futures (/api/quote, Yahoo incl. pre-/after-market, 30 s CDN cache) ---------- */
(function(){
  const ids=()=>[...new Set($$('[data-p],[data-c]').map(el=>el.dataset.p||el.dataset.c))].filter(i=>BYID[i]&&BYID[i].y).slice(0,25);
  let busy=false;
  async function run(){ if(busy||wiAway()) return; const L=ids(); if(!L.length) return; busy=true;
    try{ const r=await fetch('/api/quote?s='+encodeURIComponent(L.map(i=>BYID[i].y).join(','))); if(!r.ok) return; const Q=await r.json();
      L.forEach(i=>{ const a=BYID[i], q=Q[a.y]; if(!q||!(q.p>0)) return; const old=a.pr; a.pr=q.p; if(q.c!=null) a.ch=q.c;
        $$(`[data-p="${i}"]`).forEach(el=>{ el.textContent=fmtPrice(q.p); if(old&&Math.abs(q.p/old-1)>1e-6){ el.classList.remove('flash-up','flash-dn'); void el.offsetWidth; el.classList.add(q.p>old?'flash-up':'flash-dn') } });
        if(q.c!=null) $$(`[data-c="${i}"]`).forEach(el=>{ el.textContent=fmtPct(q.c); el.classList.remove('good','bad'); el.classList.add(cls(q.c)) });
        document.dispatchEvent(new CustomEvent('wi:tick',{detail:a})) });
    }catch(e){} finally{ busy=false } }
  setTimeout(run,600); setInterval(run,30000); document.addEventListener('visibilitychange',()=>{ if(!document.hidden) run() });
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
  let rt; document.addEventListener('wi:rows',()=>{ clearTimeout(rt); rt=setTimeout(()=>{ if(document.hidden) return; const s=symbols().join('/'); if(s&&s!==want){ if(ws){ tries=99; ws.onclose=null; ws.close(); ws=null } tries=0; connect() } },400) });
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
  $$('#cvf optgroup,#cvt optgroup').forEach(g=>{ g.label=g.dataset.g==='fiat'?SYM:g.dataset.g==='crypto'?T.crypto:g.dataset.g==='stable'?'USDT · USDC · DAI':`${T.stock} · ${T.etf} · ${T.metal} · ${T.cmd}` });
  $$('#cvf option,#cvt option').forEach(o=>{ const v=o.value; const c=v==='usd'?'USD':v.startsWith('fx:')?v.slice(3):null;
    if(c&&DN){ try{ const n=DN.of(c); o.textContent=`${n.charAt(0).toUpperCase()+n.slice(1)} (${c})` }catch(e){} } });
  const def=$('#cvt').dataset.def; if(def&&[...$('#cvt').options].some(o=>o.value===def)) $('#cvt').value=def;
  const isFiat=id=>id==='usd'||id.startsWith('fx:')||id.startsWith('st:');
  const SPX={}; $$('#cvf option[data-p]').forEach(o=>SPX[o.value]=+o.dataset.p);
  const px=id=>id==='usd'?1:id.startsWith('fx:')?(FX[id.slice(3)]?1/FX[id.slice(3)]:null):id.startsWith('st:')?SPX[id]:(BYID[id]&&BYID[id].pr);
  const lab=id=>id==='usd'?'USD':(id.startsWith('fx:')||id.startsWith('st:'))?id.slice(3):BYID[id].t;
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
  load(); setInterval(()=>{ if(!wiAway()) load() },300000);
})();

/* ---------- own news list (owner 2026-11-23): tag chips + numbered pager «‹ 1 2 3 ›», 10 a page ---------- */
(function(){ const box=$('.nlist.own[data-per]'); if(!box) return;
  const PER=+box.dataset.per||10; let all=$$('.nrow',box), tag='', pg=0;
  const nav=document.createElement('div'); nav.className='pager'; box.after(nav);
  function draw(scroll){ const L=all.filter(r=>!tag||(r.dataset.g||'').split(' ').includes(tag)), np=Math.max(1,Math.ceil(L.length/PER)); if(pg>=np) pg=np-1;
    all.forEach(r=>r.hidden=true); L.slice(pg*PER,pg*PER+PER).forEach(r=>r.hidden=false);
    const pb=(n,l,dis,on)=>`<button type="button" class="pgb${on?' on':''}" data-pg="${n}"${dis?' disabled':''}>${l}</button>`;
    let h=''; if(np>1){ h+=pb(pg-1,'‹',pg===0); const seen=new Set(); [0,1,2,pg-1,pg,pg+1,np-1].filter(n=>n>=0&&n<np).sort((a,b)=>a-b).forEach(n=>{ if(seen.has(n)) return; if(seen.size&&!seen.has(n-1)) h+='<span class="pgd">…</span>'; seen.add(n); h+=pb(n,n+1,false,n===pg) }); h+=pb(pg+1,'›',pg===np-1)
      h+=`<span class="muted pgi">${pg*PER+1}–${Math.min(pg*PER+PER,L.length)} / ${L.length}</span>` }
    nav.innerHTML=h; nav.hidden=np<2;
    $$('.pgb',nav).forEach(b=>b.onclick=()=>{ pg=+b.dataset.pg; try{ history.replaceState(null,'',pg?'#p'+(pg+1):location.pathname+location.search) }catch(e){} draw(true) });
    if(scroll) ($('#ntags')||box).scrollIntoView({block:'start',behavior:'smooth'}) }
  $$('#ntags button').forEach(b=>b.onclick=()=>{ $$('#ntags button').forEach(x=>x.classList.toggle('on',x===b)); tag=b.dataset.t; pg=0; draw() });
  const m=/^#p(\d+)$/.exec(location.hash); if(m) pg=+m[1]-1;
  document.addEventListener('wi:news',()=>{ all=$$('.nrow',box); draw() });
  draw();
})();

/* ---------- local time for news timestamps ---------- */
(function(){ let F; try{ F=new Intl.DateTimeFormat(T.intl||'en',{day:'numeric',month:'short',hour:'2-digit',minute:'2-digit'}) }catch(e){ return }
  $$('time[data-t]').forEach(t=>{ const d=Date.parse(t.dataset.t.replace(' ','T')+(/Z|[+-]\d\d:?\d\d$/.test(t.dataset.t)?'':'Z')); if(d) t.textContent=F.format(new Date(d)) }) })();

/* ---------- insights category tabs ---------- */
/* ---------- blog list: category chips + numbered pager «‹ 1 2 3 ›», 20 posts a page (same pager as the asset tables) ---------- */
(function(){ const box=$('.posts[data-per]'); if(!box) return;
  const PER=+box.dataset.per||20; let all=$$('.post',box), cat='', pg=0;
  const nav=document.createElement('div'); nav.className='pager'; box.after(nav);
  function draw(scroll){ const L=all.filter(p=>!cat||p.dataset.c===cat), np=Math.max(1,Math.ceil(L.length/PER)); if(pg>=np) pg=np-1;
    all.forEach(p=>p.hidden=true); L.slice(pg*PER,pg*PER+PER).forEach(p=>p.hidden=false);
    const pb=(n,l,dis,on)=>`<button type="button" class="pgb${on?' on':''}" data-pg="${n}"${dis?' disabled':''}>${l}</button>`;
    let h=''; if(np>1){ h+=pb(pg-1,'‹',pg===0); const seen=new Set(); [0,1,2,pg-1,pg,pg+1,np-1].filter(n=>n>=0&&n<np).sort((a,b)=>a-b).forEach(n=>{ if(seen.has(n)) return; if(seen.size&&!seen.has(n-1)) h+='<span class="pgd">…</span>'; seen.add(n); h+=pb(n,n+1,false,n===pg) }); h+=pb(pg+1,'›',pg===np-1)
      h+=`<span class="muted pgi">${pg*PER+1}–${Math.min(pg*PER+PER,L.length)} / ${L.length}</span>` }
    nav.innerHTML=h; nav.hidden=np<2;
    $$('.pgb',nav).forEach(b=>b.onclick=()=>{ pg=+b.dataset.pg; try{ history.replaceState(null,'',pg?'#p'+(pg+1):location.pathname+location.search) }catch(e){} draw(true) });
    if(scroll) ($('#bcats')||box).scrollIntoView({block:'start',behavior:'smooth'}) }
  $$('#bcats button').forEach(b=>b.onclick=()=>{ $$('#bcats button').forEach(x=>x.classList.toggle('on',x===b)); cat=b.dataset.c; pg=0; draw() });
  const m=/^#p(\d+)$/.exec(location.hash); if(m) pg=+m[1]-1;
  document.addEventListener('wi:posts',()=>{ all=$$('.post',box); draw() });
  draw() })();
/* ---------- one-question poll ---------- */
(function(){ const box=$('#poll'); if(!box) return; let done; try{ done=localStorage.getItem('wi_poll1') }catch(e){}
  if(done) return; box.hidden=false;
  $$('#poll button').forEach(b=>b.onclick=()=>{ fetch(`/api/poll/?o=${b.dataset.o}&l=${lang}`).catch(()=>{}); try{ localStorage.setItem('wi_poll1',b.dataset.o) }catch(e){}
    box.querySelector('.pollb').innerHTML=`<span class="good">✓ ${esc(box.dataset.thanks)}</span>` }) })();
/* ---------- watchlist stars (localStorage) ---------- */
/* ---------- stores: several watchlists (wi_wls) and portfolios with transactions (wi_pfs); wi_watch / wi_hold stay as mirrors for older code ---------- */
const WLS={ rd(){ let S=null; try{ S=JSON.parse(localStorage.getItem('wi_wls')||'null') }catch(e){}
    if(!S||!Array.isArray(S.list)||!S.list.length){ let w=[]; try{ w=JSON.parse(localStorage.getItem('wi_watch')||'[]') }catch(e){} S={cur:0,list:[{n:'',ids:Array.isArray(w)?w:[]}]} }
    if(!S.list[S.cur]) S.cur=0; return S },
  wr(S){ try{ localStorage.setItem('wi_wls',JSON.stringify(S)); localStorage.setItem('wi_watch',JSON.stringify(S.list[S.cur].ids)) }catch(e){} document.dispatchEvent(new Event('wi:watch')) } };
const WL={ get(){ const S=WLS.rd(); return S.list[S.cur].ids.slice() }, set(v){ const S=WLS.rd(); S.list[S.cur].ids=v; WLS.wr(S) } };
window.WLS=WLS;
const PFS=(function(){
  const rd=k=>{ try{ return JSON.parse(localStorage.getItem(k)||'null') }catch(e){ return null } };
  function calc(p){ const by={}; let realized=0, invested=0;
    p.tx.map((x,k)=>Object.assign({k},x)).sort((a,b)=>a.t<b.t?-1:a.t>b.t?1:a.k-b.k).forEach(x=>{
      const g=by[x.a]||(by[x.a]={id:x.a,qty:0,cost:0,real:0}), f=+x.f||0;
      if(x.s>0){ g.qty+=x.q; g.cost+=x.q*x.p+f; invested+=x.q*x.p+f }
      else { const qq=Math.min(x.q,g.qty), avg=g.qty?g.cost/g.qty:0, r=qq*x.p-f-avg*qq; g.real+=r; realized+=r; g.cost-=avg*qq; g.qty-=qq } });
    return {pos:Object.values(by), realized, invested} }
  let S=rd('wi_pfs');
  function save(){ try{ localStorage.setItem('wi_pfs',JSON.stringify(S)) }catch(e){}
    const m={}; S.list.forEach(p=>calc(p).pos.forEach(g=>{ if(g.qty<=1e-12) return; const x=m[g.id]||(m[g.id]={id:g.id,qty:0,cost:0}); x.qty+=g.qty; x.cost+=g.cost }));
    try{ localStorage.setItem('wi_hold',JSON.stringify(Object.values(m))) }catch(e){} document.dispatchEvent(new Event('wi:pf')) }
  if(!S||!Array.isArray(S.list)||!S.list.length){ S={cur:0,list:[{n:'',tx:[]}]}; const old=rd('wi_hold')||[];   // migrate the old single portfolio
    old.forEach(x=>{ if(!x||!x.id||!x.qty) return; const d=x.d||WI.u.slice(0,7), t=d.length===7?d+'-15T12:00':String(d).slice(0,16);
      if(x.qty>0) S.list[0].tx.push({a:x.id,s:1,q:x.qty,p:x.cost/x.qty,f:0,t}); else S.list[0].tx.push({a:x.id,s:-1,q:-x.qty,p:x.px||Math.abs(x.cost/x.qty),f:0,t}) });
    if(old.length) save() }
  if(!S.list[S.cur]) S.cur=0;
  return { get S(){ return S }, cur(){ return S.list[S.cur]||S.list[0] }, save, calc, add(tx){ this.cur().tx.push(tx); save() } };
})();
window.WIPF=PFS;
/* stablecoins (mkt.json) as light pseudo-assets so they can be watched and held: ids st-<ticker> */
const STBL=(()=>{ let pr=null; return ()=>pr||(pr=fetch(`${BASE}/assets/mkt.json?v=${WI.v}`).then(r=>r.json()).then(M=>{ (M.st||[]).filter(x=>x.pr&&x.t).forEach(x=>{ const i='st-'+x.t.toLowerCase(); if(!BYID[i]) BYID[i]={i,st:1,c:'crypto',n:x.n,t:x.t,pr:x.pr,ch:x.ch||0,l:x.l,o:0,mc:x.mc,vo:x.vo,w7:x.w7,k7:x.k7} }); return M }).catch(()=>({}))) })();
const STLIST=()=>Object.values(BYID).filter(a=>a.st);
const findAsset=v=>{ const m=/\(([^)]+)\)\s*$/.exec(v||''); const tk=String(m?m[1]:v).toLowerCase(), nv=String(v||'').toLowerCase(); const a=IDX.find(x=>x.t.toLowerCase()===tk||nm(x).toLowerCase()===nv)||STLIST().find(x=>x.t.toLowerCase()===tk||x.n.toLowerCase()===nv); return a&&a.i };
const fillPalist=()=>{ const d=$('#palist'); if(d) d.innerHTML=[...IDX.slice(0,1200),...STLIST()].map(a=>`<option value="${esc(nm(a))} (${esc(a.t)})">`).join('') };
function askDlg(title,val,ok,danger,L){ let d=$('#askm'); if(!d){ d=document.createElement('dialog'); d.id='askm'; d.className='txm askm'; document.body.appendChild(d) }
  d.innerHTML=`<form method="dialog"><div class="txh"><b>${esc(title)}</b></div>${val!=null?`<div class="inp"><input maxlength="40" value="${esc(val)}"></div>`:''}<div class="pfb"><button class="btn${danger?' danger':''}" value="ok">${esc(danger?L.delete:L.save)}</button><button class="btn ghost" value="no" formnovalidate>${esc(L.cancel)}</button></div></form>`;
  d.returnValue=''; d.onclose=()=>{ if(d.returnValue==='ok') ok(val!=null?d.querySelector('input').value.trim():true) }; d.showModal(); const i=d.querySelector('input'); if(i){ i.focus(); i.select() } }
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
  fillPalist(); STBL().then(fillPalist);
  const findId=findAsset;
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
  /* ---------- portfolio v2 (owner 2026-11-20, CryptoRank-style): several portfolios, transactions, balance chart, allocation ---------- */
  const q=C.q, PAL=['#1a6dff','#f59e0b','#14a44d','#e5484d','#8b5cf6','#0ea5e9','#ec4899','#64748b','#84cc16','#f97316'];
  // display currency (owner 2026-11-20): USD by default, also USDT / USDC / EUR / the visitor's local currency
  const CCY=[...new Set(['USD','USDT','USDC','EUR',C.code])];
  let CC='USD'; try{ const v=localStorage.getItem('wi_pfccy'); if(v&&CCY.includes(v)) CC=v }catch(e){}
  const rateOf=c=>c==='USD'?1:(c==='USDT'||c==='USDC')?1/((BYID['st-'+c.toLowerCase()]||{}).pr||1):c===C.code?C.rate:((WI.fx||{})[c]||1);
  const nfc=v=>{ const d=Math.abs(v)>=100?0:2; if(CC==='USDT'||CC==='USDC') return v.toLocaleString(T.intl||'en',{minimumFractionDigits:d,maximumFractionDigits:d})+' '+CC;
    try{ return new Intl.NumberFormat(T.intl||'en',{style:'currency',currency:CC,maximumFractionDigits:d}).format(v) }catch(e){ return Math.round(v)+' '+CC } };
  const usd=v=>nfc(v*rateOf(CC)), sgn=v=>(v<0?'−':'+')+usd(Math.abs(v));
  { const sel=$('#pfccy'); if(sel){ sel.innerHTML=CCY.map(c=>`<option${c===CC?' selected':''}>${c}</option>`).join(''); sel.onchange=()=>{ CC=sel.value; try{ localStorage.setItem('wi_pfccy',CC) }catch(e){} drawHold() } } }
  let hide=false; try{ hide=localStorage.getItem('wi_pfhide')==='1' }catch(e){}
  const H=s=>hide?'•••••':s;
  const nowT=()=>new Date(Date.now()-new Date().getTimezoneOffset()*6e4).toISOString().slice(0,16);
  const pname=(p,i)=>p.n||(i?`${q.main} ${i+1}`:q.main);
  const qf=v=>(+v).toLocaleString(T.intl||'en',{maximumSignificantDigits:8});
  const ask=(title,val,ok,danger)=>askDlg(title,val,ok,danger,q);
  function bar(){ const S=PFS.S; $('#pfsel').innerHTML=S.list.map((p,i)=>`<option value="${i}"${i===S.cur?' selected':''}>${esc(pname(p,i))}</option>`).join(''); $('#pfdel').disabled=S.list.length<2 }
  $('#pfsel').onchange=e=>{ PFS.S.cur=+e.target.value; PFS.save(); drawHold() };
  $('#pfnew').onclick=()=>ask(q.new,`${q.main} ${PFS.S.list.length+1}`,n=>{ PFS.S.list.push({n:n.slice(0,40),tx:[]}); PFS.S.cur=PFS.S.list.length-1; PFS.save(); drawHold() });
  $('#pfren').onclick=()=>ask(q.rename,pname(PFS.cur(),PFS.S.cur),n=>{ if(n){ PFS.cur().n=n.slice(0,40); PFS.save(); drawHold() } });
  $('#pfdel').onclick=()=>{ if(PFS.S.list.length<2) return; ask(`${q.delete} «${pname(PFS.cur(),PFS.S.cur)}»? ${q.confirm}`,null,()=>{ PFS.S.list.splice(PFS.S.cur,1); PFS.S.cur=0; PFS.save(); drawHold() },true) };
  // tabs
  let tab='bal'; $$('.pftabs button').forEach(b=>b.onclick=()=>{ tab=b.dataset.tab; $$('.pftabs button').forEach(x=>x.classList.toggle('on',x===b)); $$('.pfpane').forEach(p=>p.hidden=p.dataset.pane!==tab); paneDraw() });
  let rng='30'; $$('.pfrng button').forEach(b=>b.onclick=()=>{ rng=b.dataset.r; $$('.pfrng button').forEach(x=>x.classList.toggle('on',x===b)); chart() });
  let R=null;
  function model(){ const p=PFS.cur(), r=PFS.calc(p); let tv=0,d24=0,unreal=0;
    r.pos=r.pos.filter(g=>BYID[g.id]); r.pos.forEach(g=>{ const a=BYID[g.id], v=g.qty>1e-12?g.qty*a.pr:0; g.a=a; g.val=v; tv+=v; d24+=v*(a.ch||0)/(1+(a.ch||0)); if(g.qty>1e-12) unreal+=v-g.cost });
    r.live=r.pos.filter(g=>g.qty>1e-12).sort((x,y)=>y.val-x.val); r.tv=tv; r.d24=d24; r.unreal=unreal; r.p=p; return r }
  function drawSum(){ const r=R, dp=r.tv-r.d24?r.d24/(r.tv-r.d24):0, pnl=r.realized+r.unreal, pp=r.invested?pnl/r.invested:0;
    $('#pfsum').innerHTML=`<div class="pfk"><span>${esc(q.bal)}</span><button type="button" class="eye" title="${esc(q.hide)}" aria-label="${esc(q.hide)}">${hide?'🙈':'👁'}</button></div>
      <div class="pfv">${H(usd(r.tv))}</div><div class="pfd ${cls(r.d24)}">${H(sgn(r.d24))} (${fmtPct(dp)}) <small class="muted">${esc(q.chg24)}</small></div>
      <div class="pfg"><div><small>${esc(q.inv)}</small><b>${H(usd(r.invested))}</b></div><div><small>${esc(q.pnl)}</small><b class="${cls(pnl)}">${H(sgn(pnl))}<br><span>${fmtPct(pp)}</span></b></div>
      <div><small>${esc(C.t.realized)}</small><b class="${cls(r.realized)}">${H(sgn(r.realized))}</b></div><div><small>${esc(q.unreal)}</small><b class="${cls(r.unreal)}">${H(sgn(r.unreal))}</b></div></div>`;
    $('#pfsum .eye').onclick=()=>{ hide=!hide; try{ localStorage.setItem('wi_pfhide',hide?'1':'0') }catch(e){} drawHold() } }
  function drawTable(){ const r=R, f=($('#pffilter').value||'').trim().toLowerCase();
    if(!r.live.length){ $('#hold').innerHTML=`<div class="card pfempty"><p>${esc(q.empty)}</p><button class="btn" type="button" data-new>＋ ${esc(q.addtx)}</button></div>`; $('#hold [data-new]').onclick=()=>openTx(1); return }
    const L=r.live.filter(g=>!f||nm(g.a).toLowerCase().includes(f)||g.a.t.toLowerCase().includes(f));
    $('#hold').innerHTML=`<div class="tw"><table class="mt pft"><thead><tr><th class="l">${esc(T.name||'')}</th><th>${esc(T.price||'')}</th><th class="hide-sm">${esc(q.p24)}</th><th>${esc(q.pnl.split('/')[0].trim())}</th><th class="hide-sm">${esc(q.avg)}</th><th>${esc(q.hold)}</th><th>${esc(q.act)}</th></tr></thead><tbody>`+
      L.map(g=>{ const a=g.a, r1=g.cost?g.val/g.cost-1:0, p24=g.val*(a.ch||0)/(1+(a.ch||0));
        return `<tr><td class="l"><a class="asset" href="${url(a.i)}">${icon(a)}<span><span class="nm">${esc(nm(a))}</span><span class="tk">${esc(a.t)}</span></span></a></td>
        <td class="num" data-p="${a.i}">${fmtPrice(a.pr)}</td><td class="num hide-sm ${cls(p24)}">${H(sgn(p24))}<br><small>${fmtPct(a.ch)}</small></td>
        <td class="num ${cls(r1)}">${H(sgn(g.val-g.cost))}<br><small>${fmtPct(r1)}</small></td><td class="num hide-sm">${fmtPrice(g.cost/g.qty)}</td>
        <td class="num"><b>${H(usd(g.val))}</b><br><small class="muted">${H(qf(g.qty))} ${esc(a.t)}</small></td>
        <td class="pfact"><button class="pb" type="button" data-buy="${a.i}" title="${esc(q.buy)}">＋</button><button class="pb" type="button" data-sell="${a.i}" title="${esc(q.sell)}">⇄</button><button class="pb" type="button" data-del="${a.i}" title="${esc(q.delete)}">🗑</button></td></tr>` }).join('')+'</tbody></table></div>';
    $$('#hold [data-buy]').forEach(b=>b.onclick=()=>openTx(1,b.dataset.buy));
    $$('#hold [data-sell]').forEach(b=>b.onclick=()=>openTx(-1,b.dataset.sell));
    $$('#hold [data-del]').forEach(b=>b.onclick=()=>{ const a=BYID[b.dataset.del]; ask(`${q.delete} ${nm(a)}? ${q.confirm}`,null,()=>{ const p=PFS.cur(); p.tx=p.tx.filter(x=>x.a!==a.i); PFS.save(); drawHold() },true) }) }
  $('#pffilter').oninput=()=>drawTable();
  function drawAlloc(){ const r=R, box=$('#pfalloc'); if(!r.live.length){ box.innerHTML=`<p class="muted">${esc(q.nochart)}</p>`; return }
    let L=r.live.map(g=>({n:nm(g.a),t:g.a.t,a:g.a,v:g.val})); if(L.length>9){ const rest=L.slice(8); L=L.slice(0,8).concat([{n:'…',t:'',v:rest.reduce((s,x)=>s+x.v,0)}]) }
    const tv=r.tv||1; let acc=0; const R0=60, cx=80, cy=80, C0=2*Math.PI*R0;
    const arcs=L.map((x,i)=>{ const f=x.v/tv, s=`<circle r="${R0}" cx="${cx}" cy="${cy}" fill="none" stroke="${PAL[i%PAL.length]}" stroke-width="22" stroke-dasharray="${(f*C0).toFixed(2)} ${C0.toFixed(2)}" stroke-dashoffset="${(-acc*C0).toFixed(2)}" transform="rotate(-90 ${cx} ${cy})"><title>${esc(x.t||x.n)} ${(f*100).toFixed(1)}%</title></circle>`; acc+=f; return s }).join('');
    box.innerHTML=`<div class="pfal"><svg viewBox="0 0 160 160" width="190" height="190" role="img" aria-label="${esc(q.t_alloc)}">${arcs}<text x="80" y="76" text-anchor="middle" class="dt">${esc(L[0].t||L[0].n)}</text><text x="80" y="96" text-anchor="middle" class="dv">${(L[0].v/tv*100).toFixed(1)}%</text></svg>
      <table class="mt pfat"><thead><tr><th class="l">${esc(q.asset)}</th><th>${esc(q.hold)}</th><th>%</th></tr></thead><tbody>${L.map((x,i)=>`<tr><td class="l"><i class="dot" style="background:${PAL[i%PAL.length]}"></i>${x.a?icon(x.a):''}<b>${esc(x.t||x.n)}</b> <span class="muted">${esc(x.t?x.n:'')}</span></td><td class="num">${H(usd(x.v))}</td><td class="num">${(x.v/tv*100).toFixed(2)}%</td></tr>`).join('')}</tbody></table></div>` }
  function drawTx(){ const p=PFS.cur(), box=$('#pftx'); if(!p.tx.length){ box.innerHTML=`<p class="muted">${esc(q.nochart)}</p>`; return }
    const L=p.tx.map((x,k)=>Object.assign({k},x)).filter(x=>BYID[x.a]).sort((a,b)=>a.t<b.t?1:a.t>b.t?-1:b.k-a.k); let day='';
    box.innerHTML=`<div class="tw"><table class="mt pftx"><thead><tr><th class="l">${esc(q.type)}</th><th>${esc(q.qty)}</th><th class="hide-sm">${esc(q.price)}</th><th>${esc(C.t.total||'Total')}</th><th class="hide-sm">${esc(q.when)}</th><th></th></tr></thead><tbody>`+
      L.map(x=>{ const a=BYID[x.a], d=(x.t||'').slice(0,10), hd=d!==day?(day=d,`<tr class="pfday"><td colspan="6">${esc(new Date(d+'T12:00').toLocaleDateString(T.intl||'en',{year:'numeric',month:'short',day:'numeric'}))}</td></tr>`):'';
        const tot=x.q*x.p+(x.s>0?1:-1)*(x.f||0);
        return hd+`<tr><td class="l"><span class="txi ${x.s>0?'good':'bad'}">${x.s>0?'↓':'↑'}</span> ${esc(x.s>0?q.buy:q.sell)} <b>${esc(a.t)}</b>${x.m?`<br><small class="muted">${esc(x.m)}</small>`:''}</td>
          <td class="num ${x.s>0?'good':'bad'}">${x.s>0?'+':'−'}${H(qf(x.q))} ${esc(a.t)}</td><td class="num hide-sm">${fmtPrice(x.p)}</td><td class="num">${H(usd(tot))}</td>
          <td class="num hide-sm">${esc((x.t||'').slice(11,16))}</td><td class="pfact"><button class="pb" type="button" data-ed="${x.k}" title="${esc(q.edit)}">✎</button><button class="pb" type="button" data-rm="${x.k}" title="${esc(q.delete)}">🗑</button></td></tr>` }).join('')+'</tbody></table></div>';
    $$('#pftx [data-ed]').forEach(b=>b.onclick=()=>openTx(0,null,+b.dataset.ed));
    $$('#pftx [data-rm]').forEach(b=>b.onclick=()=>ask(`${q.delete}? ${q.confirm}`,null,()=>{ PFS.cur().tx.splice(+b.dataset.rm,1); PFS.save(); drawHold() },true)) }
  $('#pfcsv').onclick=()=>{ const p=PFS.cur(), e=v=>`"${String(v==null?'':v).replace(/"/g,'""')}"`;
    const rows=[['Date','Type','Asset','Ticker','Quantity','Price USD','Fee USD','Total USD','Note']].concat(p.tx.filter(x=>BYID[x.a]).sort((a,b)=>a.t<b.t?-1:1).map(x=>{ const a=BYID[x.a]; return [x.t,x.s>0?'buy':'sell',nm(a),a.t,x.q,x.p,x.f||0,(x.q*x.p+(x.s>0?1:-1)*(x.f||0)).toFixed(2),x.m||''] }));
    const a=document.createElement('a'); a.href=URL.createObjectURL(new Blob(['﻿'+rows.map(r=>r.map(e).join(',')).join('\n')],{type:'text/csv'})); a.download=`whatifstack-${(pname(p,PFS.S.cur)||'portfolio').replace(/[^\w-]+/g,'_')}.csv`; a.click() };
  /* balance chart: daily closes (Binance / Yahoo via /api/chart), monthly closes as a fallback; values in USD shown in the local currency */
  let SYM=null, CH=null, SER=null; const SC={};
  const loadLib=()=>window.LightweightCharts?Promise.resolve():new Promise((ok,no)=>{ const s=document.createElement('script'); s.src=`${BASE}/assets/vendor/lwc-5.3.0.js`; s.onload=ok; s.onerror=no; document.head.appendChild(s) });
  async function series(id,long){ const key=id+(long?'w':'d'); if(SC[key]) return SC[key];
    return SC[key]=(async()=>{ const a=BYID[id]; if(!SYM){ try{ SYM=await fetch(`${BASE}/assets/sym.json?v=${WI.v}`).then(r=>r.json()) }catch(e){ SYM={} } }
      const s=SYM[id]||[]; let out=null;
      if(s[0]){ try{ const k=await fetch(`https://data-api.binance.vision/api/v3/klines?symbol=${s[0]}&interval=${long?'1w':'1d'}&limit=${long?1000:400}`).then(r=>r.ok?r.json():Promise.reject()); if(k.length>1) out=k.map(x=>[x[0]/1e3,+x[4]]) }catch(e){} }
      if(!out&&s[1]){ try{ const j=await fetch(`/api/chart?s=${encodeURIComponent(s[1])}&r=${long?'max':'5y'}`).then(r=>r.ok?r.json():Promise.reject()); if(j.d&&j.d.length>1) out=j.d.map(x=>[x[0],x[4]]) }catch(e){} }
      if(!out&&a.st) out=[[0,a.pr],[Date.now()/1e3,a.pr]];
      if(!out){ try{ const P=await load(id), s0=ym2i(P.start); out=P.p.map((v,i)=>{ const k=s0+i; return [Date.UTC(Math.floor(k/12),k%12,28)/1e3,v] }) }catch(e){ out=[] } }
      if(out.length&&a.pr){ const f=a.pr/out[out.length-1][1]; if(isFinite(f)&&f>0) out=out.map(x=>[x[0],x[1]*f]) }   // currency/units -> today's USD price
      return out })() }
  let chartTok=0;
  async function chart(){ const tok=++chartTok, box=$('#pfchart'), p=PFS.cur(), txs=p.tx.filter(x=>BYID[x.a]&&x.t).map(x=>Object.assign({ts:Date.parse(x.t)/1e3},x)).sort((a,b)=>a.ts-b.ts);
    if(!txs.length){ box.innerHTML=`<p class="muted pfnochart">${esc(q.nochart)}</p>`; CH=null; return }
    const now=Date.now()/1e3, first=txs[0].ts, from=rng==='all'?first:Math.max(first,now-(+rng)*864e2), span=now-from, long=span>400*864e2;
    if(!CH) box.innerHTML='<div class="bload"><i></i></div>';
    const ids=[...new Set(txs.map(x=>x.a))];
    let S; try{ [S]=await Promise.all([Promise.all(ids.map(i=>series(i,long))),loadLib()]) }catch(e){ return } if(tok!==chartTok) return;
    const step=long?7*864e2:864e2, pts=[], ptr=ids.map(()=>0), qty={}; let ti=0;
    for(let t=Math.floor(from/step)*step; t<=now+step; t+=step){ const tt=Math.min(t,now);
      while(ti<txs.length&&txs[ti].ts<=tt){ const x=txs[ti++]; qty[x.a]=Math.max(0,(qty[x.a]||0)+x.s*x.q) }
      let v=0; ids.forEach((id,j)=>{ const d=S[j]; if(!d.length||!qty[id]) return; while(ptr[j]+1<d.length&&d[ptr[j]+1][0]<=tt) ptr[j]++; const px=d[ptr[j]][0]<=tt?d[ptr[j]][1]:d[0][1]; v+=qty[id]*px });
      pts.push({time:Math.floor(tt),value:+(v*rateOf(CC)).toFixed(2)}); if(tt>=now) break }
    // the last point = live value
    if(pts.length){ pts[pts.length-1].value=+(R.tv*rateOf(CC)).toFixed(2) }
    const L=window.LightweightCharts, css=getComputedStyle(document.documentElement), cv=k=>css.getPropertyValue(k).trim();
    const up=pts.length>1&&pts[pts.length-1].value>=pts[0].value, col=up?(cv('--good')||'#16a34a'):(cv('--bad')||'#dc2626');
    if(!CH){ box.innerHTML=''; CH=L.createChart(box,{autoSize:true,height:300,layout:{background:{color:'transparent'},textColor:cv('--muted')||'#666',fontFamily:getComputedStyle(document.body).fontFamily,attributionLogo:true},
        grid:{vertLines:{visible:false},horzLines:{color:cv('--line2')||'#eee'}},rightPriceScale:{borderVisible:false},timeScale:{borderVisible:false},crosshair:{mode:L.CrosshairMode.Normal},localization:{locale:T.intl||'en',priceFormatter:v=>hide?'•••':nfc(v)}});
      SER=CH.addSeries(L.AreaSeries,{lineWidth:2}) }
    SER.applyOptions({lineColor:col,topColor:col+'40',bottomColor:col+'05',priceFormat:{type:'custom',formatter:v=>hide?'•••':nfc(v)}});
    const seen=new Set(); SER.setData(pts.filter(x=>{ if(seen.has(x.time)) return false; seen.add(x.time); return true })); CH.timeScale().fitContent() }
  function paneDraw(){ if(tab==='bal') chart(); else if(tab==='alloc') drawAlloc(); else drawTx() }
  function drawHold(){ bar(); R=model(); drawSum(); drawTable(); paneDraw() }
  /* add / edit transaction (modal) */
  const M=$('#txm'); let side=1, editK=null;
  const setSide=s=>{ side=s; $$('.txside button').forEach(b=>b.classList.toggle('on',+b.dataset.s===s)); $('#txtl').textContent=s>0?q.spent:q.recv; $('#txok').textContent=editK!=null?q.save:(s>0?q.buy:q.sell); recalc('q') };
  $$('.txside button').forEach(b=>b.onclick=()=>setSide(+b.dataset.s));
  const num=id=>+($(id).value||0);
  function recalc(src){ const p=num('#txp'), f=num('#txfee');
    if(src==='t'){ const t=num('#txt'); if(p>0) $('#txq').value=+(Math.max(0,(t-side*f))/p).toPrecision(10) }
    else { const qq=num('#txq'); $('#txt').value=qq&&p?+(qq*p+side*f).toFixed(2):'' }
    const t=num('#txt'); $('#txloc').textContent=CC!=='USD'&&t?`≈ ${usd(t)}`:'' }
  ['#txq','#txp','#txfee'].forEach(s=>$(s).oninput=()=>recalc('q')); $('#txt').oninput=()=>recalc('t');
  async function priceAt(id,t){ const a=BYID[id]; if(!a) return 0; if(!t||Date.parse(t)>Date.now()-864e5) return a.pr;
    try{ const d=await series(id,false); const ts=Date.parse(t)/1e3; if(d.length&&ts>=d[0][0]){ let px=d[0][1]; for(const x of d){ if(x[0]<=ts) px=x[1]; else break } return px } }catch(e){}
    try{ const P=await load(id), k=ym2i(t.slice(0,7))-ym2i(P.start); if(k>=0&&k<P.p.length) return P.p[k] }catch(e){} return a.pr }
  let prTok=0; async function autoPrice(){ const id=findId($('#txa').value); $('#txtk').textContent=id?BYID[id].t:''; if(!id) return; const tok=++prTok; const p=await priceAt(id,$('#txd').value); if(tok!==prTok||!p) return; $('#txp').value=+p.toPrecision(8); recalc('q') }
  $('#txa').onchange=autoPrice; $('#txd').onchange=autoPrice;
  function openTx(s,id,k){ editK=k==null?null:k; const x=k!=null?PFS.cur().tx[k]:null;
    $('#txa').value=x?`${nm(BYID[x.a])} (${BYID[x.a].t})`:id&&BYID[id]?`${nm(BYID[id])} (${BYID[id].t})`:''; $('#txa').classList.remove('bad');
    $('#txq').value=x?x.q:''; $('#txp').value=x?x.p:(id&&BYID[id]?+BYID[id].pr.toPrecision(8):''); $('#txfee').value=x&&x.f?x.f:''; $('#txn').value=x&&x.m||''; $('#txd').value=x?x.t:nowT(); $('#txd').max=nowT();
    $('#txtk').textContent=x?BYID[x.a].t:id&&BYID[id]?BYID[id].t:''; $('.txh b',M).textContent=x?q.edit:q.addtx; setSide(x?x.s:(s||1));
    if(s<0&&id){ const g=R.live.find(g=>g.id===id); if(g){ $('#txq').value=+g.qty.toPrecision(10); recalc('q') } }
    M.showModal(); setTimeout(()=>(x||id?$('#txq'):$('#txa')).focus(),50) }
  $('#pfadd').onclick=()=>openTx(1); $('.txx',M).onclick=()=>M.close();
  M.addEventListener('click',e=>{ if(e.target===M) M.close() });
  $('#txf').onsubmit=e=>{ e.preventDefault(); const id=findId($('#txa').value), qq=num('#txq'), p=num('#txp');
    if(!id){ $('#txa').classList.add('bad'); $('#txa').focus(); return } if(!(qq>0)){ $('#txq').focus(); return } if(!(p>0)){ $('#txp').focus(); return }
    const tx={a:id,s:side,q:qq,p,f:num('#txfee')||0,t:$('#txd').value||nowT()}; const m=$('#txn').value.trim(); if(m) tx.m=m;
    const pf=PFS.cur(); if(editK!=null) pf.tx[editK]=tx; else pf.tx.push(tx); PFS.save(); M.close(); drawHold();
    const w=WL.get(); if(!w.includes(id)){ w.unshift(id); WL.set(w) } };
  { const id=new URLSearchParams(location.search).get('add'); if(id) STBL().then(()=>{ if(BYID[id]){ R=model(); openTx(1,id) } }) }
  // backup / restore (data lives only in this browser)
  $('#pfexp')&&($('#pfexp').onclick=()=>{ const g=k=>{ try{ return JSON.parse(localStorage.getItem(k)||'null') }catch(e){ return null } };
    const data={v:2,pfs:PFS.S,wls:WLS.rd(),plans:PL.get(),bonds:g('wi_bonds')||[],hold:g('wi_hold')||[],watch:WL.get()}; const a=document.createElement('a');
    a.href=URL.createObjectURL(new Blob([JSON.stringify(data,null,1)],{type:'application/json'})); a.download='whatifstack-portfolio.json'; a.click() });
  $('#pfimp')&&($('#pfimp').onchange=e=>{ const f=e.target.files[0]; if(!f) return; f.text().then(s=>{ const d=JSON.parse(s), w=(k,v)=>{ try{ localStorage.setItem(k,JSON.stringify(v)) }catch(e){} };
    if(d.pfs&&Array.isArray(d.pfs.list)) w('wi_pfs',d.pfs); else if(Array.isArray(d.hold)){ try{ localStorage.removeItem('wi_pfs') }catch(e){} w('wi_hold',d.hold) }
    if(d.wls&&Array.isArray(d.wls.list)) w('wi_wls',d.wls); else if(Array.isArray(d.watch)){ try{ localStorage.removeItem('wi_wls') }catch(e){} w('wi_watch',d.watch) }
    if(Array.isArray(d.plans)) w('wi_plans',d.plans); if(Array.isArray(d.bonds)) w('wi_bonds',d.bonds); location.reload() }).catch(()=>{}) });
  let ht; document.addEventListener('wi:tick',()=>{ clearTimeout(ht); ht=setTimeout(()=>{ R=model(); drawSum(); if(!document.activeElement||document.activeElement.id!=='pffilter') drawTable(); if(tab==='alloc') drawAlloc() },1500) });
  drawPlans(); STBL().then(()=>drawHold()); drawHold();
})();
/* ---------- watchlists page (/watchlist/): several lists, summary cards, add asset, market columns ---------- */
(function(){ const W=PAGE.wl; if(!W||!$('#wl')) return; const q=W.q, t={empty:W.empty};
  const ask=(title,val,ok,danger)=>askDlg(title,val,ok,danger,q); fillPalist();
  /* ---------- watchlists v2: several lists, summary cards, add asset, market columns ---------- */
  let MK=null; STBL().then(j=>{ MK=j.a||{}; fillPalist(); drawWatch() });
  const fb=v=>v==null?'—':(v>=1e12?(v/1e12).toFixed(2)+'T':v>=1e9?(v/1e9).toFixed(2)+'B':v>=1e6?(v/1e6).toFixed(2)+'M':Math.round(v).toLocaleString(T.intl||'en'));
  const wname=(l,i)=>l.n||(i?`${q.wl_main} ${i+1}`:q.wl_main);
  function wlbar(){ const S=WLS.rd(); $('#wlsel').innerHTML=S.list.map((l,i)=>`<option value="${i}"${i===S.cur?' selected':''}>${esc(wname(l,i))} (${l.ids.filter(x=>BYID[x]).length})</option>`).join(''); $('#wldel').disabled=S.list.length<2 }
  $('#wlsel').onchange=e=>{ const S=WLS.rd(); S.cur=+e.target.value; WLS.wr(S) };
  $('#wlnew').onclick=()=>ask(q.new,`${q.wl_main} ${WLS.rd().list.length+1}`,n=>{ const S=WLS.rd(); S.list.push({n:n.slice(0,40),ids:[]}); S.cur=S.list.length-1; WLS.wr(S) });
  $('#wlren').onclick=()=>{ const S=WLS.rd(); ask(q.rename,wname(S.list[S.cur],S.cur),n=>{ if(n){ const S2=WLS.rd(); S2.list[S2.cur].n=n.slice(0,40); WLS.wr(S2) } }) };
  $('#wldel').onclick=()=>{ const S=WLS.rd(); if(S.list.length<2) return; ask(`${q.delete} «${wname(S.list[S.cur],S.cur)}»? ${q.confirm}`,null,()=>{ const S2=WLS.rd(); S2.list.splice(S2.cur,1); S2.cur=0; WLS.wr(S2) },true) };
  const wadd=()=>{ const id=findAsset($('#wla').value); if(!id){ $('#wla').classList.add('bad'); $('#wla').focus(); return } const w=WL.get(); if(!w.includes(id)) w.unshift(id); WL.set(w); $('#wla').value=''; $('#wla').classList.remove('bad') };
  $('#wlgo').onclick=wadd; $('#wla').onkeydown=e=>{ if(e.key==='Enter'){ e.preventDefault(); wadd() } };
  function drawWatch(){ wlbar(); const w=WL.get().filter(i=>BYID[i]), box=$('#watch'), sum=$('#wlsum');
    if(!w.length){ box.innerHTML=`<p class="muted">${esc(t.empty)}</p>`; sum.innerHTML=''; return }
    const m=i=>{ const a=BYID[i]; return a&&a.st?[a.mc,a.vo,a.w7,a.k7]:(MK&&MK[i])||[] }; let mc=0, up=0, dn=0, avg=0;
    w.forEach(i=>{ const a=BYID[i]; mc+=m(i)[0]||0; if((a.ch||0)>0) up++; else if((a.ch||0)<0) dn++; avg+=(a.ch||0) }); avg/=w.length;
    sum.innerHTML=`<div class="card"><div class="k">${esc(q.wl_mcap)}</div><div class="v">${mc?'$'+fb(mc):'—'}</div></div>
      <div class="card"><div class="k">${esc(q.wl_gl)}</div><div class="v"><span class="good">${up}</span> / <span class="bad">${dn}</span></div><div class="glbar"><i style="width:${(up/((up+dn)||1)*100).toFixed(1)}%"></i></div></div>
      <div class="card"><div class="k">${esc(q.wl_avg)}</div><div class="v ${cls(avg)}">${fmtPct(avg)}</div></div>`;
    box.innerHTML=`<div class="tw"><table class="mt"><thead><tr><th class="l">${esc(T.name||'')}</th><th>${esc(T.price||'')}</th><th>${esc(T.chg||'')}</th><th class="hide-sm">${esc(T.mk_d7||'7d')}</th><th class="hide-md">${esc(T.mk_mcap||'')}</th><th class="hide-md">${esc(T.mk_vol||'')}</th><th class="hide-sm">${esc(T.mk_k7||'')}</th><th></th></tr></thead><tbody>`+
      w.map(i=>{ const a=BYID[i], k=m(i); return `<tr><td class="l"><button class="star" data-s="${a.i}">★</button><a class="asset" href="${url(a.i)}">${icon(a)}<span><span class="nm">${esc(nm(a))}</span><span class="tk">${esc(a.t)}</span></span></a></td>
        <td class="num" data-p="${a.i}">${fmtPrice(a.pr)}</td><td class="num ${cls(a.ch)}" data-c="${a.i}">${fmtPct(a.ch)}</td><td class="num hide-sm ${cls(k[2])}">${k[2]!=null?fmtPct(k[2]):'—'}</td>
        <td class="num hide-md">${k[0]?'$'+fb(k[0]):'—'}</td><td class="num hide-md">${k[1]?'$'+fb(k[1]):'—'}</td><td class="hide-sm">${spark(k[3]||k[5]||a.sp)}</td><td class="pfact"><button class="pb" type="button" data-pfa="${a.i}" title="${esc(q.addtx)}">＋</button></td></tr>` }).join('')+'</tbody></table></div>';
    $$('#watch [data-pfa]').forEach(b=>b.onclick=()=>{ location.href=`${W.me}?add=${encodeURIComponent(b.dataset.pfa)}` }) }
  document.addEventListener('wi:watch',drawWatch); drawWatch();
})();
/* ---------- long texts (stock analyses): show the first screen, «Show more» opens the rest ---------- */
/* analysis: sticky table of contents on wide screens (owner 2026-11-23); a click opens the clamped text and scrolls to the section */
$$('.anltoc').forEach(as=>{ const body=as.closest('.anl')&&as.closest('.anl').querySelector('.artbody'); if(!body) return;
  const hs=[...body.querySelectorAll('h2')]; if(hs.length<3) return;
  hs.forEach((h,i)=>{ if(!h.id) h.id='s-'+(i+1) });
  as.innerHTML=`<b>${esc(as.dataset.h||'')}</b><ol>${hs.map(h=>`<li><a href="#${h.id}">${esc(h.textContent)}</a></li>`).join('')}</ol>`; as.hidden=false;
  as.addEventListener('click',e=>{ const a=e.target.closest('a'); if(!a) return; e.preventDefault(); const t=document.getElementById(a.getAttribute('href').slice(1));
    if(body.classList.contains('clamped')){ const b=body.parentNode.querySelector('.clampbtn'); if(b) b.click() }
    setTimeout(()=>t&&t.scrollIntoView({block:'start',behavior:'smooth'}),60) }) });
$$('.clamp').forEach(el=>{ if(el.scrollHeight<760) return; el.classList.add('clamped');
  const b=document.createElement('button'); b.type='button'; b.className='btn ghost clampbtn'; b.textContent=(el.dataset.more||'Show more')+' ▾';
  b.onclick=()=>{ const open=el.classList.toggle('clamped')===false; b.textContent=open?'▴':(el.dataset.more||'Show more')+' ▾'; if(!open) el.scrollIntoView({block:'start',behavior:'smooth'}) };
  el.after(b) });
/* ---------- weekly e-mail report signup (api/subscribe.js) ---------- */
$$('form.nlf').forEach(f=>f.onsubmit=async e=>{ e.preventDefault(); const em=$('input[type=email]',f).value.trim(), b=$('button',f), box=f.closest('.nlbox'), note=$('.nln',box);
  b.disabled=true;
  try{ const r=await fetch('/api/forms?k=nl',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({em,l:lang,src:(f.dataset.src||'')+' '+location.pathname,hp:f.hp.value})});
    if(!r.ok) throw 0; f.remove(); note.textContent=f.dataset.ok; note.className='good nln'; try{ localStorage.setItem('wi_nl','1') }catch(x){} }
  catch(x){ note.textContent=f.dataset.err; note.className='bad nln'; b.disabled=false } });
try{ if(localStorage.getItem('wi_nl')) $$('.nlbox').forEach(x=>x.remove()) }catch(e){}
/* ---------- price alert in Telegram (asset page) ---------- */
$$('[data-alert]').forEach(b=>{ let C; try{ C=JSON.parse(b.dataset.alert) }catch(e){ return }
  b.onclick=()=>{ const old=$('.alpop'); if(old){ old.remove(); return }
    const a=BYID[C.aid], cur=a&&a.pr||0, r=v=>v>=1000?Math.round(v):v>=1?+v.toFixed(2):+v.toPrecision(4);
    const pop=document.createElement('div'); pop.className='alpop card';
    pop.innerHTML=`<b>${esc(C.t.h)}</b><div class="alrow"><label><input type="radio" name="ald" value="u" checked> ${esc(C.t.up)}</label><label><input type="radio" name="ald" value="d"> ${esc(C.t.dn)}</label></div>
      <div class="inp"><span class="muted">$</span><input type="number" min="0" step="any" value="${r(cur*1.05)}"></div><a class="btn" target="_blank" rel="noopener">✈️ ${esc(C.t.go)}</a><p class="muted">${esc(C.t.note)}</p>`;
    b.after(pop); const inp=$('input[type=number]',pop), go=$('a',pop);
    const upd=()=>{ const d=$('input[name=ald]:checked',pop).value, v=+inp.value; go.href=`https://t.me/${C.bot}?start=${encodeURIComponent(`a_${C.aid}_${d}_${String(r(v)).replace('.','p')}_${C.lang}`)}` };
    $$('input[name=ald]',pop).forEach(x=>x.onchange=()=>{ inp.value=r(cur*(x.value==='u'?1.05:0.95)); upd() }); inp.oninput=upd; upd(); inp.focus() } });
/* ---------- markets tables: quote tabs + show more ---------- */
$$('section.mkt').forEach(sec=>{ const rows=[...sec.querySelectorAll('tbody tr')], more=sec.querySelector('.mkmore'); let q='', open=false;
  const apply=()=>{ let n=0; rows.forEach(r=>{ const ok=!q||r.dataset.q===q; const show=ok&&(open||q||!r.classList.contains('xh')); r.style.display=show?'':'none'; if(show) n++ }); if(more) more.style.display=(open||q||!rows.some(r=>r.classList.contains('xh')))?'none':'' };
  sec.querySelectorAll('.qtabs button').forEach(b=>b.onclick=()=>{ q=b.dataset.q; sec.querySelectorAll('.qtabs button').forEach(x=>x.classList.toggle('on',x===b)); apply() });
  if(more) more.onclick=()=>{ open=true; apply() }; apply() });
/* ---------- my OVDP (Ukrainian government bonds) in the portfolio ---------- */
(function(){
  const M=PAGE.me; if(!M||!M.ob||!$('#bonds')) return; const t=M.ob.t, BR=M.ob.b;
  const BS={ get(){ try{ return JSON.parse(localStorage.getItem('wi_bonds')||'[]') }catch(e){ return [] } }, set(v){ try{ localStorage.setItem('wi_bonds',JSON.stringify(v)) }catch(e){} } };
  { const sec=$('#bonds'), show=()=>{ sec.hidden=false };
    if(sec.hasAttribute('data-opt')){ if(BS.get().length||location.hash==='#bonds'||new URLSearchParams(location.search).get('bb')) show();
      document.addEventListener('wi:bonds',()=>{ if(BS.get().length) show() }); window.addEventListener('hashchange',()=>{ if(location.hash==='#bonds') show() }) } }
  const SYM={UAH:'₴',USD:'$',EUR:'€'}, DAY=864e5;
  const nf=(v,c)=>{ try{ return new Intl.NumberFormat(T.intl||'uk',{style:'currency',currency:c,maximumFractionDigits:Math.abs(v)>=1000?0:2}).format(v) }catch(e){ return Math.round(v)+' '+c } };
  const toLocal=(v,c)=>{ const fx=WI.fx||{}; const usd=c==='USD'?v:(fx[c]?v/fx[c]:null); return usd==null?null:usd*M.rate };
  const today=()=>{ const d=new Date(); d.setHours(0,0,0,0); return d };
  const pd=s=>{ if(!s) return null; s=String(s).trim(); let m=/^(\d{4})-(\d{1,2})-(\d{1,2})/.exec(s); if(m) return new Date(+m[1],m[2]-1,+m[3]);
    m=/^(\d{1,2})[./](\d{1,2})[./](\d{2,4})$/.exec(s); if(m){ const y=+m[3]<100?2000+(+m[3]):+m[3]; return new Date(y,m[2]-1,+m[1]) } return null };
  const iso=d=>d?`${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`:'';
  const loc=s=>{ const d=pd(s); return d?d.toLocaleDateString(T.intl||'uk',{day:'numeric',month:'short',year:'numeric'}):'' };
  const calc=b=>{ const s=pd(b.s), e=pd(b.e), now=today(); const term=s&&e?Math.max(1,(e-s)/DAY):365;
    const el=s?Math.min(term,Math.max(0,(now-s)/DAY)):0, inc=b.a*b.r/100*term/365;
    return {term,el,acc:b.a*b.r/100*el/365,inc,fin:b.a+inc,left:e?Math.ceil((e-now)/DAY):null,done:e?now>=e:false,p:el/term} };
  const bname=b=>b.b&&BR[b.b]?BR[b.b]:(b.bt||'');
  let edit=-1;
  function draw(){
    const L=BS.get(), box=$('#blist'), tot=$('#btot');
    if(!L.length){ box.innerHTML=`<p class="muted">${esc(t.empty)}</p>`; tot.innerHTML=''; return }
    const rows=L.map((b,k)=>Object.assign({k,b},calc(b))).sort((x,y)=>(x.done-y.done)||((pd(x.b.e)||0)-(pd(y.b.e)||0)));
    const by={}; let loc_=0, locAcc=0, ok=true;
    rows.forEach(r=>{ const c=r.b.c||'UAH', g=by[c]||(by[c]={a:0,acc:0,inc:0}); if(!r.done){ g.a+=r.b.a; g.acc+=r.acc; g.inc+=r.inc }
      if(!r.done){ const v=toLocal(r.b.a+r.acc,c), w=toLocal(r.acc,c); if(v==null) ok=false; else { loc_+=v; locAcc+=w } } });
    const nx=rows.find(r=>!r.done&&r.left!=null);
    tot.innerHTML=`<div class="card"><div class="k">${esc(t.total)}</div><div class="v">${Object.entries(by).filter(([c,g])=>g.a).map(([c,g])=>esc(nf(g.a+g.acc,c))).join('<br>')||'—'}</div>`
      +(ok&&Object.values(by).filter(g=>g.a).length>1?`<div class="s">≈ ${esc(nf(loc_,M.code))} ${esc(t.in_ccy.replace('{c}',M.code))}</div>`:'')+`</div>`
      +`<div class="card"><div class="k">${esc(t.earned)}</div><div class="v good">${Object.entries(by).filter(([c,g])=>g.a).map(([c,g])=>'+'+esc(nf(g.acc,c))).join('<br>')||'—'}</div><div class="s">${esc(t.income)}: ${Object.entries(by).filter(([c,g])=>g.a).map(([c,g])=>'+'+esc(nf(g.inc,c))).join(' · ')}</div></div>`
      +(nx?`<div class="card"><div class="k">${esc(t.next)}</div><div class="v">${esc(loc(nx.b.e))}</div><div class="s">${esc(nx.b.n||bname(nx.b))} · ${esc(nf(nx.fin,nx.b.c))} · ${nx.left} ${esc(t.days)}</div></div>`:'');
    box.innerHTML=`<div class="tw"><table class="mt bdt"><thead><tr><th class="l">${esc(t.name)}</th><th>${esc(t.amt)}</th><th>%</th><th class="hide-sm">${esc(t.start)} → ${esc(t.end)}</th><th>${esc(t.earned)}</th><th class="hide-sm">${esc(t.at_end)}</th><th></th></tr></thead><tbody>`+
      rows.map(r=>{ const b=r.b, c=b.c||'UAH';
        return `<tr class="${r.done?'bdone':''}"><td class="l"><b>${esc(b.n||'ОВДП')}</b><br><small class="muted">${esc(bname(b))}${b.q?' · '+esc(t.qty)+' '+b.q:''}</small></td>
        <td class="num">${esc(nf(b.a,c))}</td><td class="num">${(+b.r).toFixed(2).replace(/\.?0+$/,'')}%</td>
        <td class="hide-sm"><div class="bper"><span>${esc(loc(b.s))}</span><span>${esc(loc(b.e))}</span></div><div class="bbar"><i style="width:${(r.p*100).toFixed(1)}%"></i></div><small class="muted">${r.done?esc(t.matured):r.left!=null?esc(t.left)+' '+r.left+' '+esc(t.days):''}</small></td>
        <td class="num good">+${esc(nf(r.acc,c))}</td><td class="num hide-sm"><b>${esc(nf(r.fin,c))}</b><br><small class="good">+${esc(nf(r.inc,c))}</small></td>
        <td class="pfact"><button class="pb" data-be="${r.k}" title="${esc(t.edit)}">✎</button><button class="pb" data-bd="${r.k}" title="${esc(t.del)}">✕</button></td></tr>` }).join('')+'</tbody></table></div>';
    $$('#blist [data-bd]').forEach(x=>x.onclick=()=>{ const v=BS.get(); v.splice(+x.dataset.bd,1); BS.set(v); if(edit===+x.dataset.bd) reset(); draw() });
    $$('#blist [data-be]').forEach(x=>x.onclick=()=>{ const k=+x.dataset.be, b=BS.get()[k]; if(!b) return; edit=k;
      $('#bn').value=b.n||''; $('#bb').value=b.b&&BR[b.b]?b.b:''; $('#bc').value=b.c||'UAH'; $('#ba').value=b.a; $('#br').value=b.r; $('#bs').value=b.s||''; $('#be').value=b.e||''; sym();
      $('#bsave').textContent=t.save; $('#bform').scrollIntoView({behavior:'smooth',block:'center'}) });
  }
  const sym=()=>{ $('#bcs').textContent=SYM[$('#bc').value]||'' };
  const reset=()=>{ edit=-1; $('#bsave').textContent=t.add; $('#bn').value=''; $('#be').value='' };
  $('#bc').onchange=sym;
  $('#bsave').onclick=()=>{ const a=+$('#ba').value, r=+$('#br').value, s_=$('#bs').value, e_=$('#be').value;
    if(!(a>0)){ $('#ba').focus(); return } if(!(r>=0)){ $('#br').focus(); return } if(!e_||(s_&&e_<=s_)){ $('#be').focus(); $('#be').classList.add('bad'); return } $('#be').classList.remove('bad');
    const b={n:$('#bn').value.trim(),b:$('#bb').value,c:$('#bc').value,a,r,s:s_,e:e_}; const v=BS.get(); if(edit>=0&&v[edit]) v[edit]=Object.assign(v[edit],b); else v.push(b); BS.set(v); reset(); draw() };
  // CSV import: name; broker; currency; amount; rate; bought; matures
  const num=x=>{ x=String(x||'').replace(/[\s %₴$€]/g,''); if(/,\d{1,2}$/.test(x)&&!/\.\d/.test(x)) x=x.replace(/\./g,'').replace(',','.'); else x=x.replace(/,/g,''); return parseFloat(x) };
  const brk=x=>{ x=String(x||'').toLowerCase().trim(); if(!x) return ''; if(BR[x]) return x; const hit=Object.entries(BR).find(([id,n])=>n.toLowerCase().includes(x)||x.includes(id)||x.includes(n.toLowerCase().split(' ')[0])); return hit?hit[0]:'' };
  function parse(txt){
    const lines=String(txt||'').replace(/^﻿/,'').split(/\r?\n/).map(l=>l.trim()).filter(Boolean); if(!lines.length) return [];
    const sep=[';','\t',','].map(c=>[c,lines[0].split(c).length]).sort((a,b)=>b[1]-a[1])[0][0];
    const out=[];
    for(const l of lines){ const f=l.split(sep).map(x=>x.replace(/^"|"$/g,'').trim()); if(f.length<6) continue;
      const a=num(f[3]), r=num(f[4]), s=pd(f[5]), e=pd(f[6]||''); if(!(a>0)||!(r>=0)||!e) continue;
      const c=(String(f[2]).toUpperCase().match(/UAH|USD|EUR/)||[/[$]|ДОЛ/i.test(f[2])?'USD':/€|ЄВРО|ЕВРО/i.test(f[2])?'EUR':'UAH'])[0];
      const id=brk(f[1]); out.push({n:f[0],b:id,bt:id?'':f[1],c,a,r,s:iso(s),e:iso(e)}) }
    return out }
  const doImp=txt=>{ const L=parse(txt), m=$('#bmsg'); if(!L.length){ m.textContent=t.imp_bad; m.className='muted bad'; return } BS.set(BS.get().concat(L)); m.textContent=t.imp_ok.replace('{n}',L.length); m.className='muted good'; draw() };
  $('#bimp').onchange=e=>{ const f=e.target.files[0]; if(f) f.text().then(doImp); e.target.value='' };
  $('#bpgo').onclick=()=>doImp($('#bpt').value);
  $('#btpl').onclick=()=>{ const csv='﻿name;broker;currency;amount;rate;bought;matures\nUA4000227045;privatbank;UAH;50000;15.5;2026-03-01;2027-03-01\nUA4000226211;monobank;USD;2000;4.2;01.05.2026;01.05.2027\n';
    const a=document.createElement('a'); a.href=URL.createObjectURL(new Blob([csv],{type:'text/csv'})); a.download='whatifstack-ovdp.csv'; a.click() };
  const q=new URLSearchParams(location.search).get('bb'); if(q&&BR[q]){ $('#bb').value=q; setTimeout(()=>$('#bonds').scrollIntoView({block:'start'}),300) }
  if(!$('#be').value){ const d=today(); d.setFullYear(d.getFullYear()+1); $('#be').value=iso(d) }
  document.addEventListener('wi:bonds',draw); sym(); draw();
})();
/* ---------- memecoins: DEX hub (/memes/) and token page (/memes/token/) — data from /api/chart?dex=… (cached server fetch of GeckoTerminal) ---------- */
const DEXU=(()=>{
  const NETN={solana:'Solana',base:'Base',bsc:'BNB',eth:'Ethereum',ton:'TON',tron:'TRON',arbitrum:'Arbitrum',polygon_pos:'Polygon',avax:'Avalanche',sui:'Sui','sui-network':'Sui',hyperevm:'HyperEVM',robinhood:'Robinhood',abstract:'Abstract',unichain:'Unichain',monad:'Monad'};
  const big=v=>{ v=+v||0; return v>=1e9?'$'+(v/1e9).toFixed(2)+'B':v>=1e6?'$'+(v/1e6).toFixed(2)+'M':v>=1e3?'$'+(v/1e3).toFixed(1)+'K':'$'+v.toFixed(0) };
  let RT; try{ RT=new Intl.RelativeTimeFormat(T.intl||'en',{numeric:'auto',style:'short'}) }catch(e){}
  const age=d=>{ const h=(Date.now()-Date.parse(d))/36e5; if(!isFinite(h)||!RT) return ''; return h<1?RT.format(-Math.round(h*60),'minute'):h<48?RT.format(-Math.round(h),'hour'):RT.format(-Math.round(h/24),'day') };
  const pc=v=>v==null?null:v/100;
  const GM=new Set(['solana','base','bsc','eth','tron']);
  const go=(r,p,where)=>`/go/${p}?from=${encodeURIComponent('memes-'+where+':'+r.n)}&l=${lang}&c=${encodeURIComponent(r.n)}&a=${encodeURIComponent(r.a)}`;
  const BW=new Set(['solana','bsc','base']);   // Binance Wallet (owner's referral, token deep link via /go/binance-web3)
  const btns=(r,w)=>`<span class="dexgo">${BW.has(r.n)?`<a class="buy bnw" href="${go(r,'binance-web3',w)}" target="_blank" rel="sponsored nofollow noopener">Binance</a>`:''}${GM.has(r.n)?`<a class="buy" href="${go(r,'gmgn',w)}" target="_blank" rel="sponsored nofollow noopener">GMGN</a>`:''}<a class="buy" href="${go(r,'okx-wallet',w)}" target="_blank" rel="sponsored nofollow noopener">OKX</a></span>`;
  const ic=(r,sz=26)=>r.img?`<span class="ic"><img src="${esc(r.img)}" alt="" loading="lazy" referrerpolicy="no-referrer" width="${sz}" height="${sz}" onerror="this.parentNode.textContent='${esc((r.s||'?').slice(0,2)).replace(/'/g,'')}'"></span>`:`<span class="ic" style="background:#64748b">${esc((r.s||'?').slice(0,2))}</span>`;
  const api=q=>fetch('/api/chart?'+q).then(r=>{ if(!r.ok) throw r.status; return r.json() });
  /* traffic light in plain words (owner 2026-11-22): Binance numbers → 🟢🟡🔴 + short reasons; F = strings MEM5 */
  const light=(r,F)=>{ const why=[], d=r.at?(Date.now()-Date.parse(r.at))/864e5:null, nf=v=>Math.round(v).toLocaleString(T.intl||'en'), lv=r.risk&&r.risk.lvl?r.risk.lvl:(r.risk>=4?'HIGH':null);
    let red=0, warn=0;
    if(lv==='HIGH'){ red++; why.push(F.risk_hi) }
    if(r.t10!=null){ if(r.t10>30){ (r.t10>50?red++:warn++); why.push(F.top10.replace('{p}',Math.round(r.t10))) } else if(r.h) why.push(F.spread.replace('{h}',nf(r.h))) }
    if(r.liq!=null){ if(r.liq<10000){ red++; why.push(F.liq_low) } else if(r.liq<50000) warn++; else why.push(F.liq_ok) }
    if(d!=null){ if(d<1){ warn++; why.push(F.new) } else why.push(F.old.replace('{d}',nf(d))) }
    if(lv==='LOW') why.push(F.risk_ok); else if(lv==='MEDIUM') warn++;
    const c=red?'r':(warn||r.t10==null?'y':'g'); return {c,t:F[c],why:why.slice(0,3)} };
  const lightHtml=(r,F)=>{ const l=light(r,F); return `<div class="tl tl-${l.c}"><b>${{g:'🟢',y:'🟡',r:'🔴'}[l.c]} ${esc(l.t)}</b><ul>${l.why.map(w=>`<li>${esc(w)}</li>`).join('')}</ul></div>` };
  const keep=r=>{ try{ sessionStorage.setItem('wi_dexrow',JSON.stringify(r)) }catch(e){} };
  return {NETN,big,age,pc,btns,ic,api,go,BW,light,lightHtml,keep};
})();
const DEXW={ key:'wi_dexw',
  all(){ try{ const v=JSON.parse(localStorage.getItem(this.key)||'[]'); return Array.isArray(v)?v:[] }catch(e){ return [] } },
  has(r){ return this.all().some(x=>x.a===r.a&&x.n===r.n) },
  toggle(r){ let l=this.all(); const on=l.some(x=>x.a===r.a&&x.n===r.n); l=on?l.filter(x=>!(x.a===r.a&&x.n===r.n)):[{n:r.n,a:r.a,s:r.s,nm:r.nm,img:r.img,pr:r.pr,mc:r.mc,c24:r.c24,liq:r.liq,vol:r.vol,h:r.h,at:r.at,t10:r.t10}].concat(l).slice(0,50);
    try{ localStorage.setItem(this.key,JSON.stringify(l)) }catch(e){} return !on } };
(function(){
  const box=$('#dexb'); if(!box||!PAGE.memes) return; const L=PAGE.memes.t, U=DEXU; let net='all', view='trend', last=[], tmr;
  const good=r=>r.liq>=100000&&r.vol>=50000&&(Date.now()-Date.parse(r.at))/36e5>=24&&r.vol/r.liq<=60&&r.c24!=null;
  const goodNew=r=>r.liq>=20000&&r.vol>=10000;
  const RUSH=new Set(['new','soon','done']);   // Binance Meme Rush stages: quality = no heavy insider / top-10 / dev concentration
  const goodRush=r=>(r.t10==null||r.t10<=40)&&(r.ins==null||r.ins<=15)&&(r.dev==null||r.dev<=10)&&(r.liq||0)>=3000;
  const qOn=()=>{ const q=$('#dexq'); return !q||q.checked };
  const uniq=l=>{ const s=new Set(); return l.filter(r=>{ const k=r.n+(r.a||r.p); if(s.has(k)) return false; s.add(k); return true }) };
  const link=r=>`${PAGE.memes.tok}?n=${encodeURIComponent(r.n)}&${r.p?'p='+encodeURIComponent(r.p):'a='+encodeURIComponent(r.a)}`;
  box.addEventListener('click',e=>{ const a=e.target.closest('a[href*="?n="]'); if(!a) return; const k=new URL(a.href,location.href).searchParams; const r=last.find(x=>x.a===k.get('a')||(x.p&&x.p===k.get('p'))); if(r) U.keep(r) });
  function row(r){ const f=[]; if(r.t10!=null&&r.t10>40) f.push(`<i class="rf">${esc(L.top10)} ${Math.round(r.t10)}%</i>`);
    if(!qOn()||RUSH.has(view)){ const hrs=(Date.now()-Date.parse(r.at))/36e5;
    if(hrs<72) f.push(`<i class="rf">${esc(L.new)}</i>`); if(r.liq<50000) f.push(`<i class="rf">${esc(L.lowliq)}</i>`); if(r.liq>0&&r.vol/r.liq>20) f.push(`<i class="rf">${esc(L.hot)}</i>`) }
    return `<tr data-href="${link(r)}"><td class="l"><a class="asset" href="${link(r)}">${U.ic(r)}<span><span class="nm">${esc(r.nm||r.s)}</span><span class="tk">${esc(r.s)} <i class="dexnet">${esc(U.NETN[r.n]||r.n)}</i> ${f.join('')}</span></span></a></td>
      <td class="num">${fmtPrice(r.pr)}</td><td class="num hide-sm">${r.mc?U.big(r.mc):'—'}</td>${RUSH.has(view)&&view!=='done'&&r.prog!=null?`<td class="num hide-sm"><span class="dprog" title="${esc(L.curve)}"><i style="width:${Math.min(100,r.prog)}%"></i></span>${Math.round(r.prog)}%</td>`:`<td class="num hide-sm ${cls(U.pc(r.c1))}">${fmtPct(U.pc(r.c1))}</td>`}<td class="num ${cls(U.pc(r.c24))}">${fmtPct(U.pc(r.c24))}</td>
      <td class="num hide-sm">${U.big(r.vol)}</td><td class="num hide-sm">${U.big(r.liq)}</td><td class="num hide-sm">${U.age(r.at)}</td><td>${U.btns(r,'table')}</td></tr>` }
  function movers(list){ const ok=uniq(list.filter(good));
    const put=(id,arr)=>{ const el=$('#dex_'+id); if(el) el.innerHTML=arr.length?arr.map(r=>`<a class="mrow" href="${link(r)}">${U.ic(r)}<span class="mn"><b>${esc(r.s)}</b><span>${esc(U.NETN[r.n]||r.n)} · ${U.big(r.mc||r.liq)}</span></span>
      <span class="mp">${fmtPrice(r.pr)}</span><span class="mc ${cls(U.pc(r.c24))}">${fmtPct(U.pc(r.c24))}</span></a>`).join(''):'<div class="empty">—</div>' };
    put('gain',[...ok].filter(r=>r.c24>0).sort((a,b)=>b.c24-a.c24).slice(0,5)); put('lose',[...ok].filter(r=>r.c24<0).sort((a,b)=>a.c24-b.c24).slice(0,5)) }
  function draw(){ let l=uniq(last); if(qOn()) l=l.filter(RUSH.has(view)?(l[0]&&l[0].src==='bn'?goodRush:goodNew):good);
    if(view==='gain') l=l.filter(r=>r.c24!=null).sort((a,b)=>b.c24-a.c24); else if(view==='vol') l=l.sort((a,b)=>b.vol-a.vol);
    else if(view==='soon') l=l.sort((a,b)=>(b.prog||0)-(a.prog||0)); else if(RUSH.has(view)) l=l.sort((a,b)=>Date.parse(b.at)-Date.parse(a.at));
    box.innerHTML=l.slice(0,30).map(row).join('')||'<tr><td colspan="9" class="empty">—</td></tr>' }
  let seq=0;
  function load(){ const my=++seq; clearTimeout(tmr); const v=view==='gain'?'trend':view;
    U.api(`dex=${v}&n=${net}`).then(j=>{ if(my!==seq) return; $('#dexerr').hidden=true; last=j.d||[]; if(v==='trend'&&net==='all') movers(last); draw(); const again=()=>{ if(wiAway()) tmr=setTimeout(again,30000); else load() }; tmr=setTimeout(again,90000) })
      .catch(()=>{ if(my!==seq) return; if(!last.length) $('#dexerr').hidden=false; tmr=setTimeout(load,15000) }) }
  if(view!=='trend'||net!=='all') U.api('dex=trend&n=all').then(j=>movers(j.d||[])).catch(()=>{});
  $$('#dexn button').forEach(b=>b.onclick=()=>{ net=b.dataset.n; $$('#dexn button').forEach(x=>x.classList.toggle('on',x===b)); last=[]; box.innerHTML='<tr><td colspan="9" class="empty">…</td></tr>'; load() });
  $$('#dexv button').forEach(b=>b.onclick=()=>{ const nv=b.dataset.v, same=(nv==='gain'?'trend':nv)===(view==='gain'?'trend':view); view=nv; $$('#dexv button').forEach(x=>x.classList.toggle('on',x===b)); if(same) draw(); else { last=[]; box.innerHTML='<tr><td colspan="9" class="empty">…</td></tr>'; load() } });
  const q=$('#dexq'); if(q) q.onchange=draw;
  box.addEventListener('click',e=>{ if(e.target.closest('a')) return; const tr=e.target.closest('tr[data-href]'); if(tr) location.href=tr.dataset.href });
  document.addEventListener('visibilitychange',()=>{ if(!document.hidden&&!last.length) load() });
  load();
})();
(function(){
  const box=$('#dexpool'); if(!box||!PAGE.dexpool) return; const L=PAGE.dexpool.t, U=DEXU; const M6=L.m6||{}, F5=L.l5||{};
  const q=new URLSearchParams(location.search), n=q.get('n')||'', p=q.get('p')||'', a0=q.get('a')||'', AD=/^[A-Za-z0-9_:\-]{20,80}$/;
  if(!/^[a-z0-9_-]{2,30}$/.test(n)||!(AD.test(p)||AD.test(a0))){ location.replace(PAGE.dexpool.list); return }
  const stat=(k,v)=>`<div class="dps"><small class="muted">${esc(k)}</small><b>${v}</b></div>`;
  const chg=(k,v)=>`<div class="dpc"><small class="muted">${k}</small><b class="${cls(U.pc(v))}">${fmtPct(U.pc(v))}</b></div>`;
  function infoHtml(inf){ inf=inf||{};
    const links=[...(inf.web||[]).map(w=>[w.replace(/^https?:\/\/(www\.)?/,'').replace(/\/$/,''),w]), inf.x?['X @'+inf.x,'https://x.com/'+inf.x]:null, inf.tg?['Telegram','https://t.me/'+inf.tg]:null].filter(Boolean);
    const desc=(inf.d||'').trim(), short=desc.length>320?desc.slice(0,320).replace(/\s+\S*$/,'')+'…':desc;
    return (short?`<p class="dpdesc">${esc(short)}</p>`:'')+(links.length?`<div class="dplinks">${links.map(([t,h])=>`<a class="bchip" href="${esc(h)}" target="_blank" rel="nofollow noopener">${esc(t)}</a>`).join('')}</div>`:'') }
  let shown=false, trDone=false;
  function trending(r){ if(trDone||!M6.trend_h) return; trDone=true;   // keep people browsing: 6 other trending tokens on the same network
    U.api(`dex=trend&n=${U.BW.has(r.n)?r.n:'all'}`).then(j=>{ const l=(j.d||[]).filter(x=>x.a&&x.a!==r.a&&(x.liq||0)>=10000).slice(0,6); if(!l.length) return;
      const el=document.createElement('section'); el.className='card dptrend';
      el.innerHTML=`<h2>🔥 ${esc(M6.trend_h)}</h2>`+l.map(x=>`<a class="mrow" href="?n=${encodeURIComponent(x.n)}&a=${encodeURIComponent(x.a)}" data-a="${esc(x.a)}">${U.ic(x,28)}<span class="mn"><b>${esc(x.s)}</b><span>${esc(x.nm||'')}</span></span><span class="mp">${fmtPrice(x.pr)}</span><span class="mc ${cls(U.pc(x.c24))}">${fmtPct(U.pc(x.c24))}</span></a>`).join('');
      el.addEventListener('click',e=>{ const a=e.target.closest('a[data-a]'); if(!a) return; const x=l.find(y=>y.a===a.dataset.a); if(x) U.keep(x) });
      const ca=$('.dpca'); (ca&&ca.parentNode?ca.parentNode:box).insertBefore(el, ca?ca.nextSibling:null) }).catch(()=>{}) }
  function show(r){ shown=true; const inf=r.info||{}; if(inf.img&&!r.img) r.img=inf.img;
    try{ const k=JSON.parse(sessionStorage.getItem('wi_dexrow')||'null'); if(k&&k.a===r.a){ ['h','t10','dev','ins','hb'].forEach(f=>{ if(r[f]==null&&k[f]!=null) r[f]=k[f] }); if(!r.at&&k.at) r.at=k.at } }catch(e){}
    document.title=`${r.nm||r.s} (${r.s}) — ${fmtPrice(r.pr)} | WhatIfStack`;
    box.innerHTML=`<div class="dph">${U.ic(r,48)}<div><h1>${esc(r.nm||r.s)} <span class="muted">${esc(r.s)}</span></h1><span class="dexnet">${esc(U.NETN[r.n]||r.n)}</span>${r.q?` <span class="muted" style="font-size:13px">${esc(r.s)}/${esc(r.q)}</span>`:''}</div><span class="dpact">${M6.watch?`<button type="button" class="btn ghost dpw${DEXW.has(r)?' on':''}" id="dpw">${esc(DEXW.has(r)?M6.watching:M6.watch)}</button>`:''}${L.al&&{solana:1,bsc:1,base:1,eth:1}[r.n]?`<button type="button" class="btn ghost" id="dpal">${esc(L.al.t.btn)}</button>`:''}</span></div>
      <div class="dpp"><b class="dpprice">${fmtPrice(r.pr)}</b><span class="${cls(U.pc(r.c24))}">${fmtPct(U.pc(r.c24))} · 24h</span></div>
      ${[['5m',r.c5],['1h',r.c1],['6h',r.c6],['24h',r.c24]].some(x=>x[1]!=null)?`<div class="dpchg" aria-label="${esc(M6.chg||'')}">${[['5m',r.c5],['1h',r.c1],['6h',r.c6],['24h',r.c24]].filter(x=>x[1]!=null).map(([k,v])=>chg(k,v)).join('')}</div>`:''}
      <div class="dpgrid"><div class="dpl">
      ${U.BW.has(r.n)&&r.a?`<div class="card dpch"><div class="dpchh"><b>${esc(L.chart)}</b><span class="dpiv">${['1m','5m','15m','1h','4h','1d'].map(i=>`<button type="button" data-i="${i}"${i==='15m'?' class=on':''}>${i}</button>`).join('')}</span></div><div id="dpchart" style="height:320px"><div class="bload"><i></i></div></div><small class="muted">Binance Web3</small></div>`:''}
      </div><div class="dpr"><div class="dpbtn">${U.BW.has(r.n)?`<a class="btn bnw" href="${U.go(r,'binance-web3','token')}" target="_blank" rel="sponsored nofollow noopener">${esc(L.trade)} · Binance Wallet</a>`:''}${['solana','base','bsc','eth','tron'].includes(r.n)?`<a class="btn" href="/go/gmgn?from=memes-token:${encodeURIComponent(r.n)}&l=${lang}&c=${encodeURIComponent(r.n)}&a=${encodeURIComponent(r.a)}" target="_blank" rel="sponsored nofollow noopener">${esc(L.trade)} · GMGN</a>`:''}<a class="btn ghost" href="/go/okx-wallet?from=memes-token:${encodeURIComponent(r.n)}&l=${lang}" target="_blank" rel="sponsored nofollow noopener">${esc(L.trade)} · OKX Wallet</a></div>
      <div class="dpstats">${stat(L.mc,r.mc?U.big(r.mc):'—')}${stat(L.liq,U.big(r.liq))}${stat(L.vol,U.big(r.vol))}${r.h?stat(L.hold,Math.round(r.h).toLocaleString(T.intl||'en')):stat(L.tx,(r.tx||0).toLocaleString(T.intl||'en'))}${stat(L.age,U.age(r.at))}</div>
      ${F5.g?`<div class="card dpsafe"><b class="dpsafeh">🛡 ${esc(M6.safe_h||'')}</b>${U.lightHtml(r,F5)}</div>`:''}</div></div>
      <div id="dpinfo">${infoHtml(inf)}</div>
      <div class="dpca"><small class="muted">${esc(L.ca)}</small><code>${esc(r.a)}</code><button class="btn ghost" type="button" id="dpcopy">${esc(L.copy)}</button></div>
      ${L.learn&&L.learn.ls&&L.learn.ls.length?`<section class="card dplearn"><h2>🎓 ${esc(L.learn.h)}</h2><p class="muted">${esc(L.learn.d)}</p><ol class="lsteps">${L.learn.ls.map(([h,t])=>`<li><a href="${esc(h)}">${esc(t)}</a></li>`).join('')}</ol><a class="chip" href="${esc(L.learn.url)}">${esc(L.learn.all)} →</a></section>`:''}`;
    const c=$('#dpcopy'); if(c) c.onclick=()=>{ try{ navigator.clipboard.writeText(r.a); c.textContent=L.copied }catch(e){} }
    const w=$('#dpw'); if(w) w.onclick=()=>{ const on=DEXW.toggle(r); w.classList.toggle('on',on); w.textContent=on?M6.watching:M6.watch };
    const ab=$('#dpal'); if(ab) ab.onclick=()=>{ const old=$('.alpop'); if(old){ old.remove(); return } const C=L.al, cur=+r.pr||0;
      const NC={solana:'s',bsc:'b',base:'a',eth:'e'}, addr=r.n==='solana'?r.a:String(r.a).replace(/^0x/i,'').toLowerCase();
      const enc=v=>{ const [m,e]=(+v).toExponential(3).split('e'); let d=m.replace('.','').replace(/0+$/,''); const ex=+e-(m.replace('.','').length-1)+(m.replace('.','').length-d.length); return d+'e'+ex };
      const pop=document.createElement('div'); pop.className='alpop card';
      pop.innerHTML=`<b>${esc(C.t.h.replace('{tk}',r.s))}</b><div class="alrow"><label><input type="radio" name="ald" value="u" checked> ${esc(C.t.up)}</label><label><input type="radio" name="ald" value="d"> ${esc(C.t.dn)}</label></div>
        <div class="inp"><span class="muted">$</span><input type="number" min="0" step="any" value="${+(cur*1.5).toPrecision(4)}"></div><a class="btn" target="_blank" rel="noopener">✈️ ${esc(C.t.go)}</a><p class="muted">${esc(C.t.note)}</p>`;
      ab.closest('.dph').after(pop); const inp=$('input[type=number]',pop), go=$('a',pop);
      const upd=()=>{ const d=$('input[name=ald]:checked',pop).value, v=+inp.value; go.href=v>0?`https://t.me/${C.bot}?start=${`x_${NC[r.n]}${addr}_${d}_${enc(v)}_${lang}`}`:'#' };
      $$('input[name=ald]',pop).forEach(x=>x.onchange=()=>{ inp.value=+(cur*(x.value==='u'?1.5:0.7)).toPrecision(4); upd() }); inp.oninput=upd; upd(); inp.focus() };
    trending(r);
    if($('#dpchart')) candles(r) }
  /* candle chart from Binance Web3 klines, our colours; the last candle and the price refresh every 15 s */
  let CHT=null, CS=null, iv='15m', ktok=0, kt=null;
  const lib=()=>window.LightweightCharts?Promise.resolve():new Promise((ok,no)=>{ const s=document.createElement('script'); s.src=`${BASE}/assets/vendor/lwc-5.3.0.js`; s.onload=ok; s.onerror=no; document.head.appendChild(s) });
  async function candles(r){
    $$('.dpiv button').forEach(b=>b.onclick=()=>{ iv=b.dataset.i; $$('.dpiv button').forEach(x=>x.classList.toggle('on',x===b)); draw(true) });
    const box=$('#dpchart'), pe=$('.dpprice');
    async function draw(fit){ const tok=++ktok; let d;
      try{ [d]=await Promise.all([U.api(`dex=kline&n=${encodeURIComponent(r.n)}&a=${encodeURIComponent(r.a)}&i=${iv}`),lib()]) }catch(e){ if(!CHT) box.innerHTML=`<p class="muted">${esc(L.nodata)}</p>`; return }
      if(tok!==ktok) return; const k=(d.d||[]); if(k.length<2){ if(!CHT) box.innerHTML=`<p class="muted">${esc(L.nodata)}</p>`; return }
      const LW=window.LightweightCharts, css=getComputedStyle(document.documentElement), cv=x=>css.getPropertyValue(x).trim(), up=cv('--good')||'#16a34a', dn=cv('--bad')||'#dc2626';
      if(!CHT){ box.innerHTML=''; CHT=LW.createChart(box,{autoSize:true,layout:{background:{color:'transparent'},textColor:cv('--muted')||'#666',fontFamily:getComputedStyle(document.body).fontFamily,attributionLogo:true},
          grid:{vertLines:{visible:false},horzLines:{color:cv('--line2')||'#eee'}},rightPriceScale:{borderVisible:false},timeScale:{borderVisible:false,timeVisible:true},crosshair:{mode:LW.CrosshairMode.Normal},localization:{locale:T.intl||'en',priceFormatter:v=>fmtPrice(v)}});
        CS=CHT.addSeries(LW.CandlestickSeries,{upColor:up,downColor:dn,borderVisible:false,wickUpColor:up,wickDownColor:dn,priceFormat:{type:'custom',formatter:v=>fmtPrice(v),minMove:1e-12}}) }
      const seen=new Set(); CS.setData(k.filter(c=>!seen.has(c[0])&&seen.add(c[0])).sort((a,b)=>a[0]-b[0]).map(c=>({time:c[0],open:c[1],high:c[2],low:c[3],close:c[4]})));
      if(fit) CHT.timeScale().fitContent();
      const last=k[k.length-1][4]; if(pe&&last>0){ pe.textContent=fmtPrice(last); document.title=document.title.replace(/— [^|]+\|/,`— ${fmtPrice(last)} |`) }
      clearTimeout(kt); const tick=()=>{ if(wiAway()) kt=setTimeout(tick,30000); else draw(false) }; kt=setTimeout(tick,30000) }
    draw(true) }
  let row=null; try{ const k=JSON.parse(sessionStorage.getItem('wi_dexrow')||'null'); if(k&&k.n===n&&(k.a===a0||(p&&k.p===p))) row=k }catch(e){}
  if(row) show(row);
  const load=()=>U.api(`dex=pool&n=${encodeURIComponent(n)}&${AD.test(p)?'p='+encodeURIComponent(p):'a='+encodeURIComponent(a0)}`)
    .then(r=>{ if(!shown) show(r); else { const el=$('#dpinfo'); if(el) el.innerHTML=infoHtml(r.info) } })
    .catch(()=>{ if(!shown){ box.innerHTML=`<p class="muted">${esc(L.nodata)}</p>`; setTimeout(load,15000) } });
  load();
})();
/* ---------- memes v6 (owner 2026-11-22/23): one simple list like Fomo — tabs, networks, search, ★ watchlist, sortable columns, safety dot ---------- */
(function(){
  const box=$('#mrows'); if(!box||!PAGE.memes5) return; const U=DEXU, P=PAGE.memes, M6=P.m6||{}, F=P.l5||{}, NM=new Set(P.nm||[]); let view='trend', net='all', rows=[], tok=0, q='';
  const RUSH={done:'done',soon:'soon',new:'new'};
  // owner 2026-11-23: «fewer but better» — only tokens with real money and real holders; obvious junk is hidden silently
  const okRush=r=>(r.t10==null||r.t10<=35)&&(r.ins==null||r.ins<=15)&&(r.dev==null||r.dev<=10)&&(r.liq||0)>=5000&&(r.h==null||r.h>=50);
  const riskHi=r=>{ const v=r.risk; return v&&(v.lvl==='HIGH'||v==='HIGH'||+v>=4) };
  const old24=r=>!r.at||Date.now()-Date.parse(r.at)>=864e5;   // owner 2026-11-23: only tokens older than 24 h
  const okTop=r=>!NM.has(String(r.s||'').toUpperCase())&&old24(r)&&!riskHi(r)&&(r.liq||0)>=50000&&(r.mc==null||r.mc>=100000)&&(r.h==null||r.h>=300)&&(r.t10==null||r.t10<=60)&&(r.vol==null||r.vol>=20000)&&(!F.g||U.light(r,F).c!=='r');
  const link=r=>`${P.tok}?n=${encodeURIComponent(r.n)}&a=${encodeURIComponent(r.a)}`;
  const H=P.h||{}, num=v=>v==null?'—':Math.round(v).toLocaleString(T.intl||'en');
  let sk=null, sd=-1;   // sort by any column (click the header; click again = reverse); phones: the «Sort by» select
  const SK={p:r=>r.pr,c:r=>U.pc(r.c24),m:r=>r.mc,v:r=>r.vol,l:r=>r.liq,h:r=>r.h,a:r=>r.at?-Date.parse(r.at):null};
  const hc=(k,cl,t)=>`<span class="${cl} dxs${sk===k?' on':''}" data-k="${k}" role="button" tabindex="0">${esc(t)}${sk===k?(sd<0?' ↓':' ↑'):''}</span>`;
  const head=()=>`<div class="dxr dxh"><span class="mrk">#</span><span class="mrn">${esc(H.name||'')}</span>${hc('p','mc-p',H.price||'')}${hc('c','mc-c','24h')}${hc('m','mc-m',H.mc||'')}${hc('v','mc-v',H.vol||'')}${hc('l','mc-l',H.liq||'')}${hc('h','mc-h',H.hold||'')}${hc('a','mc-a',H.age||'')}</div>`;
  const dot=r=>{ if(!F.g) return ''; const l=U.light(r,F); return `<i class="rd rd-${l.c}" title="${esc(l.t+(l.why.length?' — '+l.why.join('; '):''))}"></i>` };
  const star=r=>{ const on=DEXW.has(r); return `<button type="button" class="dxw${on?' on':''}" data-w="${esc(r.n)}|${esc(r.a)}" aria-pressed="${on}" title="${esc(on?M6.watching:M6.watch)}">${on?'★':'☆'}</button>` };
  const row=(r,i)=>`<a class="dxr" href="${link(r)}" data-a="${esc(r.a)}"><span class="mrk">${star(r)}<em>${i+1}</em></span>
    <span class="mrn">${U.ic(r,36)}<span class="mrt"><b>${esc(r.s)} ${dot(r)}</b><small class="muted">${esc((r.nm&&r.nm!==r.s?r.nm+' · ':'')+(U.NETN[r.n]||r.n))}</small></span></span>
    <span class="mc-p"><b>${fmtPrice(r.pr)}</b><small class="mob muted">${U.big(r.mc)} MC</small></span>
    <span class="mc-c ${cls(U.pc(r.c24))}">${fmtPct(U.pc(r.c24))}</span>
    <span class="mc-m">${U.big(r.mc)}</span><span class="mc-v">${U.big(r.vol)}</span><span class="mc-l">${U.big(r.liq)}</span>
    <span class="mc-h">${num(r.h)}</span><span class="mc-a">${esc(U.age(r.at))}</span></a>`;
  const isAddr=s=>/^(0x[0-9a-fA-F]{40}|[1-9A-HJ-NP-Za-km-z]{32,44})$/.test(s);
  function draw(){ let l=rows.slice(); const seen=new Set(); l=l.filter(r=>r.a&&!seen.has(r.n+r.a)&&seen.add(r.n+r.a));
    if(view==='fav'){} else if(RUSH[view]) l=l.filter(okRush); else l=l.filter(okTop);
    if(view==='gain') l.sort((a,b)=>(b.c24||0)-(a.c24||0)); else if(view==='most') l.sort((a,b)=>(b.h||0)-(a.h||0));
    else if(view==='soon') l.sort((a,b)=>(b.prog||0)-(a.prog||0)); else if(RUSH[view]) l.sort((a,b)=>Date.parse(b.at)-Date.parse(a.at));
    if(q){ const s=q.toLowerCase(); l=l.filter(r=>(r.s||'').toLowerCase().includes(s)||(r.nm||'').toLowerCase().includes(s)||(r.a||'').toLowerCase()===s) }
    if(sk){ const f=SK[sk]; l.sort((a,b)=>{ const x=f(a), y=f(b); if(x==null&&y==null) return 0; if(x==null) return 1; if(y==null) return -1; return sd*(x-y) }) }
    if(l.length){ box.innerHTML=head()+l.slice(0,view==='fav'?50:30).map(row).join(''); return }
    if(q&&isAddr(q)){ const nets=q.startsWith('0x')?['bsc','base','eth']:['solana'];
      box.innerHTML=`<div class="empty">${esc(M6.nf||'')}<div class="mnf">${nets.map(n=>`<a class="btn ghost" href="${P.tok}?n=${n}&a=${encodeURIComponent(q)}">${esc(U.NETN[n]||n)}</a>`).join('')}</div></div>`; return }
    box.innerHTML=`<div class="empty">${view==='fav'&&!q?esc(M6.fav0||'—'):'—'}</div>` }
  async function load(){ const t=++tok;
    if(view==='fav'){ rows=DEXW.all().filter(r=>net==='all'||r.n===net); draw();
      for(const r of rows.slice(0,20)){ U.api(`dex=pool&n=${encodeURIComponent(r.n)}&a=${encodeURIComponent(r.a)}`).then(x=>{ if(t!==tok||!x) return; Object.assign(r,{pr:x.pr??r.pr,mc:x.mc??r.mc,c24:x.c24??r.c24,liq:x.liq??r.liq,vol:x.vol??r.vol,h:x.h??r.h}); draw() }).catch(()=>{}) }
      return }
    try{ const j=await U.api(`dex=${RUSH[view]||'trend'}&n=${net}`); if(t!==tok) return; rows=j.d||[]; draw() }catch(e){ if(t===tok&&!rows.length) box.innerHTML='<div class="empty">—</div>' } }
  $$('#mtab button').forEach(b=>b.onclick=()=>{ $$('#mtab button').forEach(x=>x.classList.toggle('on',x===b)); const was=view==='fav'?'fav':(RUSH[view]||'trend'); view=b.dataset.v; const now=view==='fav'?'fav':(RUSH[view]||'trend'); if(now===was) draw(); else { box.innerHTML='<div class="empty">…</div>'; load() } });
  $$('#mnet button').forEach(b=>b.onclick=()=>{ $$('#mnet button').forEach(x=>x.classList.toggle('on',x===b)); net=b.dataset.n; box.innerHTML='<div class="empty">…</div>'; load() });
  const mq=$('#mq'); if(mq){ let qt; mq.addEventListener('input',()=>{ clearTimeout(qt); qt=setTimeout(()=>{ q=mq.value.trim(); draw() },150) }) }
  const ms=$('#msort'); if(ms) ms.onchange=()=>{ sk=ms.value||null; sd=-1; draw() };
  const sortBy=k=>{ if(sk===k) sd=-sd; else { sk=k; sd=-1 } if(ms) ms.value=sk||''; draw() };
  box.addEventListener('keydown',e=>{ const h=e.target.closest('.dxs'); if(h&&(e.key==='Enter'||e.key===' ')){ e.preventDefault(); sortBy(h.dataset.k) } });
  box.addEventListener('click',e=>{ const h=e.target.closest('.dxs'); if(h){ e.preventDefault(); sortBy(h.dataset.k); return }
    const w=e.target.closest('.dxw'); if(w){ e.preventDefault(); e.stopPropagation(); const [n,a]=w.dataset.w.split('|'); const r=rows.find(x=>x.a===a&&x.n===n)||DEXW.all().find(x=>x.a===a&&x.n===n); if(r){ DEXW.toggle(r); if(view==='fav') rows=DEXW.all(); draw() } return }
    const a=e.target.closest('.dxr'); if(!a) return; const r=rows.find(x=>x.a===a.dataset.a); if(r) U.keep(r) });
  load(); setInterval(()=>{ if(!wiAway()&&view!=='fav') load() },60000);
})();
/* ---------- memes extras (owner 2026-11-23): launch pulse, fresh exchange listings, meme narratives ---------- */
(function(){
  if(!PAGE.memes5||!PAGE.memes) return; const U=DEXU, M7=PAGE.memes.m7||{}, P=PAGE.memes;
  const nf=v=>Math.round(v).toLocaleString(T.intl||'en');
  const pu=$('#mpulse'); if(pu) U.api('dex=pulse').then(j=>{ const d=j.d||{}; if(!d.n) return;
    $$('b[data-k]',pu).forEach(b=>{ const k=b.dataset.k; b.textContent=k==='rate'?'~'+nf(d.rate):k==='climb'?nf(d.climb):nf(d[k]||0) });
    const c=$('b[data-k=climb]',pu); if(c&&c.nextSibling) c.nextSibling.textContent=' '+(M7.p_climb||'').replace('{n}',nf(d.n));
    pu.hidden=false }).catch(()=>{});
  const ago=ms=>{ const m=(Date.now()-ms)/6e4; const s=m<60?Math.round(m)+'m':m<1440?Math.round(m/60)+'h':Math.round(m/1440)+'d'; return M7.ago?`${s} ${M7.ago}`.trim():s };
  const X=window.WIX||{}, IDXT={}; try{ (X.IDX||[]).forEach(a=>{ if(a&&a.t&&a.c==='crypto'&&!IDXT[a.t.toUpperCase()]) IDXT[a.t.toUpperCase()]=a }) }catch(e){}
  const li=$('#mlistings'); if(li) U.api('dex=listings').then(j=>{ const l=j.d||[]; if(!l.length){ li.innerHTML=`<p class="muted">${esc(M7.none||'—')}</p>`; return }
    li.innerHTML=l.slice(0,10).map(x=>{ const tk=(x.tk||[])[0]||'', our=IDXT[tk.toUpperCase()];
      const href=x.n&&x.a?`${P.tok}?n=${encodeURIComponent(x.n)}&a=${encodeURIComponent(x.a)}`:our&&X.url?X.url(our.i):x.url;
      const ext=!(x.n&&x.a)&&!our;
      return `<a class="mrow" href="${esc(href)}"${ext?' target="_blank" rel="nofollow noopener"':''}>${x.img?U.ic({s:tk,img:x.img},28):`<span class="ic">${esc(tk.slice(0,3))}</span>`}<span class="mn"><b>${esc(tk||x.t)}</b><span>${esc(x.ex)} · ${esc(ago(x.at))}</span></span>${x.pr?`<span class="mp">${fmtPrice(x.pr)}</span><span class="mc ${cls(U.pc(x.c24))}">${fmtPct(U.pc(x.c24))}</span>`:''}</a>` }).join('') }).catch(()=>{ li.innerHTML=`<p class="muted">${esc(M7.none||'—')}</p>` });
  const na=$('#mnarr'); if(na) U.api('dex=narr').then(j=>{ const l=j.d||[]; if(!l.length){ na.innerHTML='<p class="muted">—</p>'; return }
    const mx=Math.max(...l.map(x=>x.mc||0));
    na.innerHTML=l.slice(0,10).map(x=>`<div class="nrw"><span class="nimg">${(x.img||[]).map(u=>`<img src="${esc(u)}" alt="" width="20" height="20" loading="lazy" referrerpolicy="no-referrer">`).join('')}</span><span class="nn"><b>${esc(x.n)}</b><i style="width:${Math.max(3,(x.mc/mx)*100).toFixed(1)}%"></i></span><span class="mp">${U.big(x.mc)}</span><span class="mc ${cls(U.pc(x.c24))}">${fmtPct(U.pc(x.c24))}</span></div>`).join('') }).catch(()=>{ na.innerHTML='<p class="muted">—</p>' });
})();
/* token page: «why people are talking about it» from Binance's social hype board (English) */
(function(){
  if(!PAGE.dexpool) return; const L=PAGE.dexpool.t, M7=L.m7||{}, U=DEXU; if(!M7.hype_h) return;
  const q=new URLSearchParams(location.search), n=q.get('n')||'', a=(q.get('a')||'').toLowerCase(); if(!U.BW.has(n)||!a) return;
  U.api(`dex=hype&n=${encodeURIComponent(n)}`).then(j=>{ const h=(j.d||{})[a]; if(!h||!h.b) return;
    const put=()=>{ const ref=$('.dpgrid'); if(!ref){ setTimeout(put,400); return } if($('.dphype')) return;
      const el=document.createElement('div'); el.className='card dphype';
      el.innerHTML=`<b>🗣 ${esc(M7.hype_h)}</b>${h.s?` <span class="badge">${esc(h.s)}</span>`:''}<p>${esc(h.b)}</p><small class="muted">${esc(M7.hype_en||'')}</small>`;
      ref.parentNode.insertBefore(el,ref) }; put() }).catch(()=>{});
})();
/* ---------- memes «Pick of the day»: strict filter + Binance social buzz, traffic light in plain words ---------- */
(function(){
  const box=$('#mpick'); if(!box||!PAGE.memes) return; const U=DEXU, F=PAGE.memes.l5;
  const link=r=>`${PAGE.memes.tok}?n=${encodeURIComponent(r.n)}&a=${encodeURIComponent(r.a)}`;
  const card=r=>`<a class="card mpc" href="${link(r)}" data-a="${esc(r.a)}"><div class="mph">${U.ic(r,36)}<div><b>${esc(r.s)}</b> <span class="dexnet">${esc(U.NETN[r.n]||r.n)}</span><small class="muted">${esc(r.nm||'')}</small></div>
      <div class="mpp"><b>${fmtPrice(r.pr)}</b><span class="${cls(U.pc(r.c24))}">${fmtPct(U.pc(r.c24))}</span></div></div>
      ${U.lightHtml(r,F)}${r.hb?`<p class="mphype"><b>🗣 ${esc(F.why)}${lang!=='en'?' (EN)':''}:</b> ${esc(r.hb.length>170?r.hb.slice(0,170).replace(/\s+\S*$/,'')+'…':r.hb)}</p>`:''}
      <small class="muted">${esc(PAGE.memes.t.mcs||'MC')} ${U.big(r.mc)} · ${esc(PAGE.memes.t.vols||'Vol')} ${U.big(r.vol)}</small></a>`;
  let rows=[];
  box.addEventListener('click',e=>{ const a=e.target.closest('.mpc'); if(!a) return; const r=rows.find(x=>x.a===a.dataset.a); if(r) U.keep(r) });
  const load=()=>U.api('dex=picks').then(j=>{ rows=j.d||[]; box.innerHTML=rows.length?rows.map(card).join(''):`<p class="muted">${esc(F.none)}</p>` }).catch(()=>{ box.innerHTML=`<p class="muted">${esc(F.none)}</p>` });
  load(); setInterval(()=>{ if(!wiAway()) load() },300000);
})();
/* ---------- share: one button -> phone share sheet, or a menu (networks + copy link) ---------- */
(function(){
  const bars=$$('.sharebar'); if(!bars.length) return;
  const page=location.origin+location.pathname, title=((document.querySelector('h1')||{}).textContent||document.title).trim();
  const u=src=>encodeURIComponent(page+'?utm_source='+src+'&utm_medium=share'), tt=encodeURIComponent(title);
  const N=[['Telegram','#229ED9',`https://t.me/share/url?url=${u('telegram')}&text=${tt}`,'✈'],['X','#000',`https://x.com/intent/post?url=${u('x')}&text=${tt}`,'𝕏'],
    ['WhatsApp','#25D366',`https://wa.me/?text=${tt}%20${u('whatsapp')}`,'✆'],['Facebook','#1877F2',`https://www.facebook.com/sharer/sharer.php?u=${u('facebook')}`,'f'],
    ['Viber','#7360F2',`viber://forward?text=${tt}%20${u('viber')}`,'V'],['Reddit','#FF4500',`https://www.reddit.com/submit?url=${u('reddit')}&title=${tt}`,'r'],
    ['LinkedIn','#0A66C2',`https://www.linkedin.com/sharing/share-offsite/?url=${u('linkedin')}`,'in'],['E-mail','#64748b',`mailto:?subject=${tt}&body=${u('email')}`,'@']];
  const label=bars[0].dataset.l||'Share', copyL=T.copy||'Copy link';
  const touch=matchMedia('(pointer:coarse)').matches;
  let menu=null;
  const close=()=>{ if(menu){ menu.remove(); menu=null } };
  function open(btn){
    if(navigator.share&&touch){ navigator.share({title,url:page+'?utm_source=native&utm_medium=share'}).catch(()=>{}); return }
    if(menu){ close(); return }
    menu=document.createElement('div'); menu.className='shmenu'; menu.setAttribute('role','menu');
    menu.innerHTML=N.map(([n,c,h,ic])=>`<a role="menuitem" href="${h}" target="_blank" rel="noopener"><i style="background:${c}">${ic}</i>${n}</a>`).join('')+
      `<button type="button" role="menuitem" data-copy><i style="background:var(--accent)">⧉</i>${esc(copyL)}</button>`;
    document.body.appendChild(menu);
    const r=btn.getBoundingClientRect(), w=menu.offsetWidth, h=menu.offsetHeight;
    let x=Math.min(r.left, innerWidth-w-12), y=r.bottom+8; if(y+h>innerHeight-8) y=r.top-h-8;
    menu.style.left=Math.max(12,x)+scrollX+'px'; menu.style.top=y+scrollY+'px';
    menu.querySelector('[data-copy]').onclick=e=>{ const v=page+'?utm_source=copy&utm_medium=share';
      (navigator.clipboard?navigator.clipboard.writeText(v):Promise.reject()).catch(()=>{ const t=document.createElement('textarea'); t.value=v; document.body.appendChild(t); t.select(); try{document.execCommand('copy')}catch(_){} t.remove() });
      e.currentTarget.lastChild.textContent=' ✓'; setTimeout(close,700) };
    menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>setTimeout(close,100)));
  }
  const mk=cls=>{ const b=document.createElement('button'); b.type='button'; b.className='shbtn'+(cls?' '+cls:''); b.setAttribute('aria-haspopup','menu');
    b.innerHTML=`<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" d="M4 12v7a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-7M16 6l-4-4-4 4M12 2v14"/></svg><span>${esc(label)}</span>`;
    b.onclick=e=>{ e.stopPropagation(); open(b) }; return b };
  bars.forEach(bar=>{ bar.innerHTML=''; bar.appendChild(mk()) });
  document.addEventListener('click',e=>{ if(menu&&!menu.contains(e.target)) close() });
  document.addEventListener('keydown',e=>{ if(e.key==='Escape') close() });
  addEventListener('scroll',()=>{ if(menu) close() },{passive:true});
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
  let mode='m', P=null, D=null, all=false;
  const SHOW=6;   // recent years shown; older ones behind a language-neutral "▾ 2004–2019" toggle
  const more=ys=>ys.length>SHOW?`<button type="button" class="seasmore" id="seasmore">${all?'▴':'▾ '+ys[ys.length-1]+'–'+ys[SHOW]}</button>`:'';
  const bindMore=()=>{ const b=$('#seasmore'); if(b) b.onclick=()=>{ all=!all; draw() } };
  $('#seasm').innerHTML=modes.map(([k,l])=>`<button data-m="${k}" class="${k===mode?'on':''}">${esc(l)}</button>`).join('');
  $$('#seasm button').forEach(b=>b.onclick=async()=>{ mode=b.dataset.m; $$('#seasm button').forEach(x=>x.classList.toggle('on',x===b)); draw() });
  const ym=s=>{ const [y,m]=s.split('-').map(Number); return y*12+m-1 };
  function monthly(){ const s0=ym(P.start), rows={};
    P.p.forEach((v,i)=>{ if(!i||v===P.p[i-1]) return; const k=s0+i, y=Math.floor(k/12), m=k%12; (rows[y]=rows[y]||{})[m]=v/P.p[i-1]-1 });   // an identical close = a gap in the source series, not a 0% month
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
    const c=(lab,v,arr)=>`<div class="card stat"><div class="k">${esc(lab)}</div><div class="v ${cls(v)}">${v==null?'—':pc(v)}</div>${arr.length?`<div class="s muted">${esc(t.med)} ${pc(med(arr))} · ${esc(t.up)}: ${arr.filter(v=>v>0).length}/${arr.length}</div>`:''}</div>`;
    $('#seasc').innerHTML=`<div class="stats sfit">${c(t.mtd+' · '+MN[m],mtd,mm)}${c(t.qtd+' · Q'+(q+1),qtd,qq)}${c(t.ytd+' · '+y,ytd,yy)}</div>` }
  async function draw(){ const g=$('#seasg');
    if(!P){ try{ P=await fetch(`${BASE}/assets/p/${C.id}.json?v=${WI.v}`).then(r=>r.json()) }catch(e){ g.innerHTML=''; return } }
    const M=monthly(); cards(M);
    if(mode==='m'){ const ys=Object.keys(M.rows).map(Number).sort((a,b)=>b-a);
      g.innerHTML=`<table class="seast"><thead><tr><th></th>${MN.map(x=>`<th>${esc(x)}</th>`).join('')}<th>${esc(L('year','Year'))}</th></tr></thead><tbody>`+
        `<tr class="med"><th>${esc(t.med)}</th>${MN.map((_,m)=>{ const a=ys.filter(y=>y*12+m<M.last).map(y=>M.rows[y][m]).filter(v=>v!=null); return cell(a.length?med(a):null) }).join('')}<td></td></tr>`+
        (all?ys:ys.slice(0,SHOW)).map(y=>`<tr><th>${y}</th>${MN.map((_,m)=>cell(M.rows[y][m], y*12+m===M.last)).join('')}${cell(M.yr[y], y===Math.floor(M.last/12))}</tr>`).join('')+'</tbody></table>'+more(ys); bindMore(); return }
    if(mode==='q'){ const Q=qrows(), ys=Object.keys(Q.rows).map(Number).sort((a,b)=>b-a);
      g.innerHTML=`<table class="seast q"><thead><tr><th></th>${[1,2,3,4].map(q=>`<th>Q${q}</th>`).join('')}<th>${esc(L('year','Year'))}</th></tr></thead><tbody>`+
        (all?ys:ys.slice(0,SHOW)).map(y=>`<tr><th>${y}</th>${[0,1,2,3].map(q=>cell(Q.rows[y][q], y*12+q*3+2>Q.last)).join('')}${cell(M.yr[y], y===Math.floor(M.last/12))}</tr>`).join('')+'</tbody></table>'+more(ys); bindMore(); return }
    if(!D){ g.innerHTML='<div class="bload"><i></i></div>';
      try{ D=await fetch(`https://data-api.binance.vision/api/v3/klines?symbol=${C.bn}&interval=1d&limit=400`).then(r=>r.json()) }catch(e){ D=[] } }
    const by={}; D.forEach((k,i)=>{ if(!i) return; const d=new Date(k[0]), key=d.getUTCFullYear()*12+d.getUTCMonth(); (by[key]=by[key]||{})[d.getUTCDate()]=k[4]/D[i-1][4]-1 });
    const keys=Object.keys(by).map(Number).sort((a,b)=>b-a).slice(0,12), today=new Date();
    g.innerHTML=`<table class="seast d"><thead><tr><th></th>${Array.from({length:31},(_,i)=>`<th>${i+1}</th>`).join('')}</tr></thead><tbody>`+
      keys.map(k=>`<tr><th>${esc(MN[k%12])} ${String(Math.floor(k/12)).slice(2)}</th>${Array.from({length:31},(_,i)=>cell(by[k][i+1], k===today.getUTCFullYear()*12+today.getUTCMonth()&&i+1===today.getUTCDate())).join('')}</tr>`).join('')+
      `</tbody></table><p class="muted" style="font-size:12px;margin:8px 0 0">${esc(t.dnote)}</p>` }
  const io=new IntersectionObserver(es=>{ if(es.some(e=>e.isIntersecting)){ io.disconnect(); draw() } },{rootMargin:'400px'}); io.observe(box);
})();
// About card next to the chart: clip long descriptions with a "show more" toggle
document.querySelectorAll('.side').forEach(sd => {
  const c = sd.querySelector('.sclip'), b = sd.querySelector('.smore');
  if (!c || !b || c.scrollHeight <= c.clientHeight + 4) return;
  c.classList.add('clip'); b.hidden = false; const more = b.textContent;
  b.addEventListener('click', () => { const o = sd.classList.toggle('open'); b.textContent = o ? b.dataset.less : more; });
});

/* ---------- "Add to portfolio" button on asset pages ---------- */
document.addEventListener('click',async e=>{
  const b=e.target.closest('.addpf'); if(!b) return; const C=JSON.parse(b.dataset.cfg), id=b.dataset.add, old=document.querySelector('.pfpop');
  // owner 2026-11-20: the same «Add transaction» window as in the portfolio (quantity, price, date, fee, USD by default)
  if(C.me){ e.preventDefault(); location.href=`${C.me}?add=${encodeURIComponent(id)}`; return }
  if(old){ old.remove(); if(old.dataset.id===id) return }
  const END=WI.u.slice(0,7), pop=document.createElement('div'); pop.className='pfpop card'; pop.dataset.id=id;
  pop.innerHTML=`<label>${esc(C.t.qty_or_sum)}<div class="inp"><input type="number" min="0" step="any" value="100" class="pa"><span class="muted">${esc(C.code)}</span></div></label>
    <label>${esc(C.d)}<div class="inp"><input type="month" class="pd" value="${END}" max="${END}"></div></label>
    <div class="pfb"><button class="btn pok">＋ ${esc(C.t.addpf)}</button><button class="btn ghost pno">${esc(C.t.cancel)}</button></div><p class="pmsg"></p>`;
  b.parentNode.after(pop); const pa=pop.querySelector('.pa'); pa.focus(); pa.select(); pop.querySelector('.pno').onclick=()=>pop.remove();
  pop.addEventListener('keydown',ev=>{ if(ev.key==='Enter'){ ev.preventDefault(); const k=pop.querySelector('.pok'); k&&k.click() } if(ev.key==='Escape') pop.remove() });
  pop.querySelector('.pok').onclick=async()=>{ const v=+pop.querySelector('.pa').value, d=(pop.querySelector('.pd').value||END).slice(0,7); if(!(v>0)) return;
    let px=(BYID[id]||{}).pr;
    try{ const P=await fetch(`${BASE}/assets/p/${id}.json?v=${WI.v}`).then(r=>r.json()); const ym=s=>{const [y,m]=s.split('-').map(Number);return y*12+m-1}, k=ym(d)-ym(P.start);
      if(!px) px=P.p[P.p.length-1]; if(d<END&&k>=0&&k<P.p.length) px=P.p[k] }catch(e){}
    if(!px) return; const qty=(v/C.rate)/px, nowT=new Date(Date.now()-new Date().getTimezoneOffset()*6e4).toISOString().slice(0,16);
    PFS.add({a:id,s:1,q:qty,p:px,f:0,t:d<END?d+'-15T12:00':nowT});
    pop.querySelector('.pmsg').innerHTML=`✓ ${esc(C.t.added)} · <a href="${C.me}">${esc(C.t.open)} →</a>`; pop.querySelector('.pfb').remove() };
});

/* ---------- AI assistant (api/ask.js, Groq) ---------- */
(function(){
  const host=$('#aiw'); if(!host) return; let C; try{ C=JSON.parse(host.dataset.cfg) }catch(e){ return }
  const KEY='wi_ai_'+lang; let H=[]; try{ H=JSON.parse(sessionStorage.getItem(KEY)||'[]') }catch(e){}
  const save=()=>{ try{ sessionStorage.setItem(KEY,JSON.stringify(H.slice(-20))) }catch(e){} };
  const md=t=>{ let h=esc(t).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>')
      .replace(/(https:\/\/(?:www\.)?whatifstack\.com[^\s<)"]*)/g,'<a href="$1">$1</a>');
    return h.split(/\n{2,}/).map(p=>{ const ls=p.split('\n');
      if(ls.every(l=>/^\s*([-*•]|\d+[.)])\s+/.test(l))) return '<ul>'+ls.map(l=>'<li>'+l.replace(/^\s*([-*•]|\d+[.)])\s+/,'')+'</li>').join('')+'</ul>';
      return '<p>'+ls.join('<br>')+'</p>' }).join('') };
  const btn=document.createElement('button'); btn.type='button'; btn.className='aibtn'; btn.setAttribute('aria-haspopup','dialog'); btn.setAttribute('aria-label',C.btn);
  btn.innerHTML='<svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path fill="currentColor" d="M12 2l1.9 5.6L19.5 9.5l-5.6 1.9L12 17l-1.9-5.6L4.5 9.5l5.6-1.9zM19 14l.9 2.6 2.6.9-2.6.9L19 21l-.9-2.6-2.6-.9 2.6-.9z"/></svg><span>'+esc(C.btn)+'</span>';
  const P=document.createElement('section'); P.className='aip'; P.hidden=true; P.setAttribute('role','dialog'); P.setAttribute('aria-label',C.title);
  P.innerHTML=`<header><b>${esc(C.title)}</b><button type="button" class="ainew">${esc(C.new)}</button><button type="button" class="aix" aria-label="×">×</button></header>
    <div class="aimsgs" aria-live="polite"></div>
    <form class="aiform"><textarea rows="1" maxlength="600" placeholder="${esc(C.ph)}" aria-label="${esc(C.ph)}"></textarea><button type="submit" aria-label="${esc(C.send)}">➤</button></form>
    <p class="ainote">${esc(C.note)}${C.fb?` · <button type="button" class="aifbl">${esc(C.fb.btn)}</button>`:''}</p>
    ${C.fb?`<form class="aifb" hidden><b>${esc(C.fb.h)}</b><p>${esc(C.fb.d)}</p><textarea rows="4" maxlength="2000" required placeholder="${esc(C.fb.ph)}"></textarea><input type="email" maxlength="120" placeholder="${esc(C.fb.em)}"><div><button type="button" class="aifbx">${esc(C.fb.back)}</button><button type="submit" class="btn">${esc(C.fb.send)}</button></div><p class="aifbm" aria-live="polite"></p></form>`:''}`;
  document.body.append(btn,P);
  const box=$('.aimsgs',P), ta=$('textarea',P), form=$('form',P);
  const chips=()=>{ const qs=C.n?[C.a1,C.a2,C.a3].map(x=>fmt(x,{n:C.n})):[C.g1,C.g2,C.g3];
    return '<div class="aichips">'+qs.map(q=>`<button type="button">${esc(q)}</button>`).join('')+'</div>' };
  const render=()=>{ box.innerHTML=H.length?H.map(m=>`<div class="aim ${m.r}">${m.r==='a'?md(m.t):esc(m.t)}</div>`).join(''):chips(); box.scrollTop=box.scrollHeight };
  const ctx=()=>{ const g=s=>{ const e=$(s); return e?e.innerText.replace(/\s+\n/g,'\n').replace(/[ \t]+/g,' ').trim():'' };
    return [location.pathname, document.title, g('h1'), g('.price'), g('.lead'), g('.side'), g('.stats')].filter(Boolean).join('\n').slice(0,2500) };
  let busy=false;
  const ask=async q=>{ q=q.trim(); if(!q||busy) return; busy=true; H.push({r:'u',t:q}); render(); ta.value='';
    box.insertAdjacentHTML('beforeend','<div class="aim a typing"><i></i><i></i><i></i></div>'); box.scrollTop=box.scrollHeight;
    let a, err;
    try{ const r=await fetch('/api/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({q,lang,ctx:ctx(),hist:H.slice(-7,-1)})});
      const j=await r.json().catch(()=>({})); if(r.ok&&j.a) a=j.a; else err=r.status===429?C.limit:C.err }catch(e){ err=C.err }
    if(a){ H.push({r:'a',t:a}); save(); render() } else { H.pop(); render(); box.insertAdjacentHTML('beforeend',`<div class="aim err">${esc(err)}</div>`); ta.value=q }
    busy=false; ta.focus() };
  const open=v=>{ P.hidden=!v; btn.classList.toggle('on',v); if(v){ render(); ta.focus() } };
  const FBF=$('.aifb',P);
  if(FBF){ let fbT=0; const fbMode=v=>{ FBF.hidden=!v; box.hidden=v; form.hidden=v; if(v){ fbT=Date.now(); $('textarea',FBF).focus() } else ta.focus() };
    $('.aifbl',P).onclick=()=>fbMode(true); $('.aifbx',FBF).onclick=()=>fbMode(false);
    FBF.onsubmit=async e=>{ e.preventDefault(); const t=$('textarea',FBF).value.trim(), em=$('input',FBF).value.trim(), m=$('.aifbm',FBF); if(t.length<3) return;
      const sb=$('[type=submit]',FBF); sb.disabled=true;
      try{ const r=await fetch('/api/forms?k=fb',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({t,em,l:lang,p:location.pathname,w:Date.now()-fbT})});
        if(!r.ok) throw 0; m.textContent=C.fb.ok; m.className='aifbm good'; $('textarea',FBF).value=''; setTimeout(()=>{ fbMode(false); m.textContent='' },2200) }
      catch(x){ m.textContent=C.fb.err; m.className='aifbm bad' } sb.disabled=false } }
  btn.onclick=()=>open(P.hidden); $('.aix',P).onclick=()=>{ open(false); btn.focus() };
  $('.ainew',P).onclick=()=>{ H=[]; save(); render(); ta.focus() };
  box.addEventListener('click',e=>{ const b=e.target.closest('.aichips button'); if(b) ask(b.textContent) });
  form.onsubmit=e=>{ e.preventDefault(); ask(ta.value) };
  ta.addEventListener('keydown',e=>{ if(e.key==='Enter'&&!e.shiftKey){ e.preventDefault(); ask(ta.value) } });
  ta.addEventListener('input',()=>{ ta.style.height='auto'; ta.style.height=Math.min(ta.scrollHeight,120)+'px' });
  document.addEventListener('keydown',e=>{ if(e.key==='Escape'&&!P.hidden){ open(false); btn.focus() } });
})();

/* ---------- own daily chart: Lightweight Charts (Apache-2.0, TradingView) where the TradingView embed is not allowed ---------- */
(function(){
  const sec=$('.ownchart[data-lw]'); if(!sec) return; let C; try{ C=JSON.parse(sec.dataset.lw) }catch(e){ return } if(!C.y) return;
  const loadLib=()=>window.LightweightCharts?Promise.resolve():new Promise((ok,no)=>{ const s=document.createElement('script'); s.src=`${BASE}/assets/vendor/lwc-5.3.0.js`; s.onload=ok; s.onerror=no; document.head.appendChild(s) });
  const get=r=>fetch(`/api/chart?s=${encodeURIComponent(C.y)}&r=${r}`).then(x=>x.ok?x.json():Promise.reject()).then(j=>{ if(!j.d||j.d.length<2) throw 0; return j });
  const start=async()=>{
    let D5; try{ [D5]=await Promise.all([get('5y'),loadLib()]) }catch(e){ return }   // keep the monthly SVG chart
    const L=window.LightweightCharts, css=getComputedStyle(document.documentElement), v=k=>css.getPropertyValue(k).trim();
    const up=v('--good')||'#16a34a', dn=v('--bad')||'#dc2626';
    sec.classList.add('lw');
    const ranges=[[C.yrs[0],365],[C.yrs[1],365*3],[C.yrs[2],365*5],[C.all,0]];
    sec.innerHTML=`<div class="charthead"><h2>${esc(C.t)} · ${esc($('.ahead .badge')?.textContent||'')}${D5.cur&&D5.cur!=='USD'?` <span class="lwcur">${esc(D5.cur)}</span>`:''}</h2><span class="lwchg"></span></div>
      <div class="lwbar"><div class="lwr">${ranges.map((r,i)=>`<button type="button" data-i="${i}"${i===0?' class="on"':''}>${esc(r[0])}</button>`).join('')}</div>
      <div class="lwr lwt"><button type="button" data-t="c" class="on" aria-label="candles"><svg viewBox="0 0 16 16" width="14" height="14"><path fill="currentColor" d="M4 1h1v3h1v7H5v4H4v-4H3V4h1zm7 2h1v2h1v6h-1v4h-1v-4h-1V5h1z"/></svg></button><button type="button" data-t="l" aria-label="line"><svg viewBox="0 0 16 16" width="14" height="14"><path fill="none" stroke="currentColor" stroke-width="1.6" d="M1 12l4-5 3 3 4-6 3 3"/></svg></button></div></div>
      <div class="lwbox"></div><p class="lwnote"><span class="lwavg"></span></p>`;
    const box=$('.lwbox',sec);
    const ch=L.createChart(box,{autoSize:true,layout:{background:{color:'transparent'},textColor:v('--muted')||'#666',fontFamily:getComputedStyle(document.body).fontFamily,attributionLogo:true},
      grid:{vertLines:{visible:false},horzLines:{color:v('--line2')||'#eee'}},rightPriceScale:{borderVisible:false},timeScale:{borderVisible:false},
      crosshair:{mode:L.CrosshairMode.Normal},localization:{locale:C.intl}});
    const cs=ch.addSeries(L.CandlestickSeries,{upColor:up,downColor:dn,borderVisible:false,wickUpColor:up,wickDownColor:dn});
    const ls=ch.addSeries(L.AreaSeries,{lineColor:v('--accent')||up,topColor:'rgba(63,209,155,.25)',bottomColor:'rgba(63,209,155,0)',lineWidth:2,visible:false});
    let all=null, type='c', ri=0, pl=null;
    const show=async()=>{
      let d=D5.d;
      if(ranges[ri][1]===0){ try{ all=all||await get('max'); d=all.d }catch(e){ d=D5.d } }
      else { const from=d[d.length-1][0]-ranges[ri][1]*864e2; d=d.filter(x=>x[0]>=from) }
      cs.setData(d.map(x=>({time:x[0],open:x[1],high:x[2],low:x[3],close:x[4]})));
      ls.setData(d.map(x=>({time:x[0],value:x[4]})));
      cs.applyOptions({visible:type==='c'}); ls.applyOptions({visible:type==='l'});
      const s=type==='c'?cs:ls; if(pl){ try{cs.removePriceLine(pl)}catch(e){} try{ls.removePriceLine(pl)}catch(e){} }
      const avg=d.length/d.reduce((a,x)=>a+1/x[4],0);   // equal money each period -> harmonic mean of closes
      pl=s.createPriceLine({price:avg,color:v('--gold')||'#f0b53a',lineWidth:1,lineStyle:L.LineStyle.Dashed,axisLabelVisible:true,title:C.avg});
      const chg=d[d.length-1][4]/d[0][4]-1, e=$('.lwchg',sec); e.textContent=fmtPct(chg); e.className='lwchg '+(chg>=0?'up':'dn');
      const last=d[d.length-1][4]; $('.lwavg',sec).textContent=`${C.avg}: ${avg.toLocaleString(C.intl,{maximumSignificantDigits:5})}${D5.cur&&D5.cur!=='USD'?' '+D5.cur:''} · ${fmtPct(last/avg-1)}`;
      ch.timeScale().fitContent() };
    $('.lwbar',sec).addEventListener('click',e=>{ const b=e.target.closest('button'); if(!b) return;
      if(b.dataset.i!=null){ ri=+b.dataset.i; $$('.lwr:not(.lwt) button',sec).forEach(x=>x.classList.toggle('on',x===b)) }
      else { type=b.dataset.t; $$('.lwt button',sec).forEach(x=>x.classList.toggle('on',x===b)) }
      show() });
    show() };
  if('IntersectionObserver' in window){ const io=new IntersectionObserver(es=>{ if(es.some(e=>e.isIntersecting)){ io.disconnect(); start() } },{rootMargin:'300px'}); io.observe(sec) } else start();
})();

/* ---------- widget builder: embed code for other sites ---------- */
(function(){
  $$('.embuild').forEach(box=>{ let C; try{ C=JSON.parse(box.dataset.cfg) }catch(e){ return } const t=C.t;
    const det=box.closest('details'); let done=false;
    const init=()=>{ if(done) return; done=true;
      const yr=new Date().getFullYear(); let a=C.a||'btc', amt=10, f='d', since=(yr-5)+'-01', th='light';
      const A=id=>(WI.a||[]).find(x=>x.i===id);
      const seg=(k,opts,v)=>`<div class="seg" data-k="${k}">${opts.map(([val,lab])=>`<button type="button" data-v="${val}"${val===v?' class="on"':''}>${esc(lab)}</button>`).join('')}</div>`;
      const years=[]; for(let y=yr-1;y>=2015;y--) years.push(y);
      box.innerHTML=`<div class="embf">${C.pickable?`<label class="f">${esc(t.pick)}<div class="inp"><input class="ea" list="emblist" value="${esc(nm(A(a)||{n:a}))}"></div><datalist id="emblist">${(WI.a||[]).slice(0,600).map(x=>`<option value="${esc(nm(x))}">${esc(x.t)}</option>`).join('')}</datalist></label>`:''}
        <label class="f">${esc(t.amount)}<div class="inp"><input class="em" type="number" min="1" max="100000" value="10"><span class="muted">$</span></div></label>
        <div class="f">${esc(t.freq)}${seg('f',[['d',t.daily],['w',t.weekly],['m',t.monthly]],f)}</div>
        <label class="f">${esc(t.since)}<div class="inp"><select class="es">${years.map(y=>`<option value="${y}-01"${y+'-01'===since?' selected':''}>${y}</option>`).join('')}</select></div></label>
        <div class="f">${esc(t.theme)}${seg('th',[['light',t.light],['dark',t.dark],['auto',t.auto]],th)}</div></div>
        <div class="embprev"><iframe title="preview" loading="lazy"></iframe></div>
        <p class="muted embhelp">${esc(t.help)}</p><div class="embcode"><textarea readonly rows="4"></textarea><button type="button" class="btn">${esc(t.copy)}</button></div>`;
      const ifr=$('iframe',box), ta=$('textarea',box);
      const upd=()=>{ const x=A(a); if(!x) return; const n=nm(x), base='https://whatifstack.com';
        const q=`a=${a}&amt=${amt}&f=${f}&s=${since}&l=${C.l}&th=${th}&n=${encodeURIComponent(n)}`;
        ifr.src=`/embed/?${q}`;
        const page=base+(C.l==='uk'?'':'/'+C.l)+'/'+a+'/';
        ta.value=`<iframe src="${base}/embed/?${q}" width="100%" height="250" style="border:0;max-width:520px" loading="lazy" title="${esc(fmt(t.anchor,{n}))}"></iframe>\n<p style="margin:4px 0;font-size:13px"><a href="${page}">${esc(fmt(t.anchor,{n}))}</a></p>` };
      box.addEventListener('click',e=>{ const b=e.target.closest('.seg button'); if(b){ const k=b.parentNode.dataset.k; $$('button',b.parentNode).forEach(x=>x.classList.toggle('on',x===b)); if(k==='f') f=b.dataset.v; else th=b.dataset.v; upd() }
        if(e.target.closest('.embcode .btn')){ ta.select(); (navigator.clipboard?navigator.clipboard.writeText(ta.value):Promise.reject()).catch(()=>document.execCommand('copy')); const bt=e.target.closest('.btn'); bt.textContent=t.copied; setTimeout(()=>bt.textContent=t.copy,1600) } });
      $('.em',box).addEventListener('input',e=>{ amt=Math.max(1,Math.min(100000,Math.round(+e.target.value)||10)); clearTimeout(box._t); box._t=setTimeout(upd,400) });
      $('.es',box).addEventListener('change',e=>{ since=e.target.value; upd() });
      const ea=$('.ea',box); if(ea) ea.addEventListener('change',()=>{ const v=ea.value.trim().toLowerCase(); const x=(WI.a||[]).find(y=>nm(y).toLowerCase()===v||y.t.toLowerCase()===v||y.i===v); if(x){ a=x.i; upd() } });
      upd() };
    if(det&&!det.open) det.addEventListener('toggle',()=>{ if(det.open) init() },{once:false}); else init() });
})();

/* ---------- investment calculator (/compound-interest/) ---------- */
(function(){
  const box=$('.icpage'); if(!box||!PAGE.ic) return; const C=PAGE.ic, t=C.t;
  const nf=v=>{ try{ return new Intl.NumberFormat(T.intl||'en',{style:'currency',currency:C.code,maximumFractionDigits:Math.abs(v)>=100?0:2}).format(v) }catch(e){ return Math.round(v)+' '+C.code } };
  const short=v=>{ try{ return new Intl.NumberFormat(T.intl||'en',{style:'currency',currency:C.code,notation:'compact',maximumFractionDigits:1}).format(v) }catch(e){ return nf(v) } };
  const num=id=>{ const e=$('#'+id); return e?Math.max(0,+e.value||0):0 };
  const segv=id=>($('#'+id+' button.on')||{}).dataset?.v;
  const PER={m:1,q:3,h:6,y:12}, SC={o:1.25,r:1,p:0.6};
  function sim(p0,pmt,years,rate,per,reinv,tax){ let bal=p0,acc=0,paid=0,contrib=p0,taxT=0; const yrs=[{y:0,contrib:p0,total:p0}]; const N=Math.round(years*12);
    for(let m=1;m<=N;m++){ if(m>1){ bal+=pmt; contrib+=pmt } acc+=bal*rate/12;
      if(m%per===0||m===N){ const tx=acc*tax; taxT+=tx; const net=acc-tx; if(reinv) bal+=net; else paid+=net; acc=0 }
      if(m%12===0||m===N) yrs.push({y:+(m/12).toFixed(1),contrib,total:bal+paid}) }
    return {final:bal+paid,contrib,taxT,yrs} }
  const opt=()=>$('#ici').selectedOptions[0];
  function inputs(){ const o=opt(); return { p0:num('icp'), pmt:num('icm'), y:Math.min(60,Math.max(1,Math.round(num('icy'))||1)),
      rate:(+$('#icr').value||0)/100*SC[segv('ics')||'r'], per:PER[segv('icc')||'m'], reinv:$('#icre').checked,
      tax:$('#ictx').checked&&o.dataset.tf!=='1'?num('ictr')/100:0, inf:$('#icin').checked?num('icir')/100:0, inst:o.value, col:o.dataset.c } }
  function run(){
    const I=inputs(), R=sim(I.p0,I.pmt,I.y,I.rate,I.per,I.reinv,I.tax), defl=Math.pow(1+I.inf,I.y);
    const interest=R.final-R.contrib+R.taxT, real=R.final/defl;
    $('#icyl').textContent=I.y; $('#icys').value=Math.min(40,I.y);
    $('#ic_p0').textContent=nf(I.p0); $('#ic_contrib').textContent=nf(R.contrib); $('#ic_interest').textContent='+'+nf(interest); $('#ic_taxes').textContent=R.taxT?'−'+nf(R.taxT):nf(0);
    $('#icv').textContent=nf(R.final);
    const re=$('#ic_realv'); re.textContent=nf(real); re.className=real>=R.contrib?'good':'bad';
    const cashReal=R.contrib/defl; $('#ic_cash').textContent=nf(cashReal); $('#ic_cashs').textContent=I.inf?fmt(t.cash_t,{v:nf(R.contrib-cashReal),inv:nf(R.contrib)}):'';
    // comparison bars
    $('#iccmph').textContent=fmt(t.cmp_h,{n:I.y,yr:C.yr});
    const rows=[...$('#ici').options].filter(o=>o.value!=='custom').map(o=>{ const rr=(+o.dataset.r)/100*SC[segv('ics')||'r'], tx=$('#ictx').checked&&o.dataset.tf!=='1'?num('ictr')/100:0;
      return {n:o.textContent,r:o.dataset.r,c:o.dataset.c,f:sim(I.p0,I.pmt,I.y,rr,I.per,I.reinv,tx).final,on:o.value===I.inst} });
    const top=Math.max(...rows.map(r=>r.f),1);
    $('#iccmp').innerHTML=rows.map(r=>`<div class="icrow${r.on?' on':''}"><div class="h"><span>${esc(r.n)} · ${r.r}%</span><b>${esc(nf(r.f))}</b></div><div class="bar"><i style="width:${(r.f/top*100).toFixed(1)}%;background:${r.c}"></i></div></div>`).join('');
    // growth line chart: total vs contributions
    const W=640,H=230,L=6,Rr=70,TP=10,B=24, ys=R.yrs, mx=Math.max(...ys.map(r=>r.total),1), X=k=>L+(W-L-Rr)*k/Math.max(1,ys.length-1), Y=v=>TP+(H-TP-B)*(1-v/mx);
    let g=''; for(let k=0;k<=4;k++){ const v=mx*k/4; g+=`<line x1="${L}" x2="${W-Rr}" y1="${Y(v)}" y2="${Y(v)}" class="g"/><text x="${W-Rr+6}" y="${Y(v)+4}">${esc(short(v))}</text>` }
    const pt=f=>ys.map((r,k)=>`${X(k).toFixed(1)},${Y(f(r)).toFixed(1)}`).join(' ');
    const step=Math.max(1,Math.ceil(ys.length/8)); ys.forEach((r,k)=>{ if(k%step===0||k===ys.length-1) g+=`<text x="${X(k)}" y="${H-6}" text-anchor="middle">${Math.round(r.y)}</text>` });
    $('#icchart').innerHTML=`<svg viewBox="0 0 ${W} ${H}" role="img"><defs><linearGradient id="icgr" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="${I.col}" stop-opacity=".28"/><stop offset="1" stop-color="${I.col}" stop-opacity="0"/></linearGradient></defs>${g}
      <polygon points="${X(0)},${H-B} ${pt(r=>r.total)} ${X(ys.length-1)},${H-B}" fill="url(#icgr)"/><polyline points="${pt(r=>r.total)}" fill="none" stroke="${I.col}" stroke-width="3" stroke-linejoin="round"/>
      <polyline points="${pt(r=>r.contrib)}" fill="none" stroke="var(--muted)" stroke-width="2" stroke-dasharray="6 5"/></svg>`;
    $$('.glg i.tl',box).forEach(i=>i.style.background=I.col);
    // donut
    const gain=Math.max(0,R.final-R.contrib), tot=gain+R.contrib||1, fr=gain/tot, rr=54, cc=2*Math.PI*rr;
    $('#icdonut').innerHTML=`<svg viewBox="0 0 140 140" width="140" height="140"><circle cx="70" cy="70" r="${rr}" fill="none" stroke="var(--line2)" stroke-width="18"/><circle cx="70" cy="70" r="${rr}" fill="none" stroke="${I.col}" stroke-width="18" stroke-dasharray="${(cc*fr).toFixed(1)} ${cc}" transform="rotate(-90 70 70)"/><text x="70" y="76" text-anchor="middle" class="dn">${Math.round(fr*100)}%</text></svg>`;
    $('#icdi').textContent=Math.round(fr*100)+'%'; $('#icdc').textContent=Math.round((1-fr)*100)+'%';
    $$('.glg i.b',box).forEach(i=>i.style.background=I.col);
    // table
    $('#ictable').innerHTML=`<thead><tr><th>${esc(t.year)}</th><th>${esc(t.contrib)}</th><th>${esc(t.interest)}</th><th>${esc(t.total)}</th></tr></thead><tbody>`+
      ys.slice(1).map(r=>`<tr><td>${Math.round(r.y)}</td><td>${nf(r.contrib)}</td><td class="good">+${nf(r.total-r.contrib)}</td><td><b>${nf(r.total)}</b></td></tr>`).join('')+'</tbody>';
    // reverse
    const base=sim(I.p0,0,I.y,I.rate,I.per,I.reinv,I.tax).final, unit=sim(0,1,I.y,I.rate,I.per,I.reinv,I.tax).final, G=num('icg');
    $('#icgv').textContent=nf(Math.max(0,(G-base)/(unit||1)));
    // FIRE (today's money) + income from the final capital
    const need=num('icx')*12/0.04; $('#icfn').textContent=short(need);
    let bal=I.p0, mm=0; const rm=I.rate*(1-I.tax)/12; while(mm<720){ mm++; if(mm>1) bal+=I.pmt; bal*=1+rm; if(bal/Math.pow(1+I.inf,mm/12)>=need) break }
    $('#icfy').textContent=mm>=720?'—':`${Math.ceil(mm/12)} ${C.yr}`; $('#icfy').title=mm>=720?t.fire_never:'';
    const yInc=R.final*I.rate*(1-I.tax); $('#icid').textContent=nf(yInc/365); $('#iciw').textContent=nf(yInc/52); $('#icfi').textContent=nf(yInc/12);
    try{ const q=new URLSearchParams({p:I.p0,m:I.pmt,y:I.y,i:I.inst,r:$('#icr').value,s:segv('ics'),c:segv('icc')}); new URLSearchParams(location.search).forEach((v,k)=>{ if(k.startsWith('utm_')) q.set(k,v) }); history.replaceState(null,'','?'+q) }catch(e){}
  }
  const pick=(v,keepRate)=>{ $('#ici').value=v; const o=opt(); if(!keepRate) $('#icr').value=o.dataset.r; $$('.icard',box).forEach(c=>c.classList.toggle('on',c.dataset.v===v)) };
  try{ const q=new URLSearchParams(location.search); if(q.has('p')){ $('#icp').value=q.get('p'); $('#icm').value=q.get('m')||0; $('#icy').value=q.get('y')||10;
    if(q.get('i')&&[...$('#ici').options].some(o=>o.value===q.get('i'))) pick(q.get('i'),true); if(q.get('r')) $('#icr').value=q.get('r');
    ['s','c'].forEach(k=>{ const v=q.get(k), sg=$(k==='s'?'#ics':'#icc'); if(v&&sg) $$('button',sg).forEach(b=>b.classList.toggle('on',b.dataset.v===v)) }) } }catch(e){}
  box.addEventListener('click',e=>{ const c=e.target.closest('.icard'); if(c){ pick(c.dataset.v); run(); return }
    const b=e.target.closest('.seg button'); if(b){ $$('button',b.parentNode).forEach(x=>x.classList.toggle('on',x===b)); run() } });
  $('#icys').addEventListener('input',e=>{ $('#icy').value=e.target.value; run() });
  $$('input',box).forEach(e=>{ if(e.id!=='icys') e.addEventListener('input',run) });
  $('#icsh').onclick=()=>{ const u=location.href; (navigator.share?navigator.share({url:u,title:document.title}):navigator.clipboard.writeText(u)).catch(()=>{}); $('#icsh').textContent='✓' };
  run();
})();

/* header dropdowns: one open at a time, close on outside click */
document.addEventListener('click',e=>{ $$('details.dd[open]').forEach(d=>{ if(!d.contains(e.target)) d.removeAttribute('open') }) });
$$('details.dd').forEach(d=>d.addEventListener('toggle',()=>{ if(d.open) $$('details.dd[open]').forEach(o=>{ if(o!==d) o.removeAttribute('open') }) }));

/* ---------- currency switcher in the header ---------- */
(function(){
  const conv=()=>{ $$('[data-u]').forEach(el=>{ el.textContent=fmtUsd(+el.dataset.u) }); if(CCY!=='USD') $$('[data-p]').forEach(el=>{ const a=BYID[el.dataset.p]; if(a&&a.pr!=null) el.textContent=fmtPrice(a.pr) }) };
  const sel=$('#ccysel'); if(sel){ const list=['USD','EUR','UAH','PLN','GBP','CHF','TRY','RUB','KZT','BRL','MXN','INR','IDR','VND','THB','PHP','JPY','KRW','CNY','SAR','AED','CAD','AUD'].filter(c=>c==='USD'||(WI.fx||{})[c]);
    sel.innerHTML=list.map(c=>`<option value="${c}"${c===CCY?' selected':''}>${c}</option>`).join('');
    sel.onchange=()=>{ try{ localStorage.setItem('wi_ccy',sel.value) }catch(e){} location.reload() } }
  if(CCY!=='USD') conv();
})();
/* ---------- dividend calculator (/dividends/) ---------- */
(function(){
  const box=$('.icpage'); if(!box||!PAGE.dv) return; const C=PAGE.dv, t=C.t;
  const nf=v=>{ try{ return new Intl.NumberFormat(T.intl||'en',{style:'currency',currency:C.code,maximumFractionDigits:Math.abs(v)>=100?0:2}).format(v) }catch(e){ return Math.round(v)+' '+C.code } };
  const short=v=>{ try{ return new Intl.NumberFormat(T.intl||'en',{style:'currency',currency:C.code,notation:'compact',maximumFractionDigits:1}).format(v) }catch(e){ return nf(v) } };
  const num=id=>Math.max(0,+$('#'+id).value||0);
  function run(){
    const p0=num('dvp'), pm=num('dvm'), Y=Math.min(60,Math.max(1,Math.round(num('dvy'))||1)), y=num('dvr')/100, dg=num('dvg')/100, pg=num('dvq')/100, tax=Math.min(1,num('dvt')/100), re=$('#dvre').checked;
    $('#dvyl').textContent=Y; $('#dvys').value=Math.min(40,Y);
    let P=1, units=p0, dpu=y, cash=0, contrib=p0, tot=0, yd=0; const rows=[], gm=Math.pow(1+pg,1/12);
    for(let m=1;m<=Y*12;m++){ P*=gm; units+=pm/P; contrib+=pm;
      if(m%3===0){ const d=units*dpu/4*(1-tax); tot+=d; yd+=d; if(re) units+=d/P; else cash+=d }
      if(m%12===0){ rows.push({y:m/12,v:units*P+cash,c:contrib,d:yd}); yd=0; dpu*=1+dg } }
    const last=rows[rows.length-1]||{v:p0,c:p0,d:0};
    $('#dv_c').textContent=nf(contrib); $('#dv_d').textContent='+'+nf(tot); $('#dv_v').textContent=nf(last.v);
    $('#dv_m').textContent=nf(last.d/12); $('#dv_y').textContent=nf(last.d); $('#dv_o').textContent=contrib?(last.d/contrib*100).toFixed(1)+'%':'—';
    const W=640,H=220,L=6,R=70,TP=10,B=24, mx=Math.max(...rows.map(r=>r.d),1), bw=(W-L-R)/rows.length;
    let g=''; for(let k=0;k<=4;k++){ const v=mx*k/4, yy=TP+(H-TP-B)*(1-k/4); g+=`<line x1="${L}" x2="${W-R}" y1="${yy}" y2="${yy}" class="g"/><text x="${W-R+6}" y="${yy+4}">${esc(short(v))}</text>` }
    const step=Math.max(1,Math.ceil(rows.length/10));
    rows.forEach((r,k)=>{ const h=(H-TP-B)*r.d/mx, x=L+k*bw; g+=`<rect x="${(x+bw*.15).toFixed(1)}" y="${(H-B-h).toFixed(1)}" width="${(bw*.7).toFixed(1)}" height="${h.toFixed(1)}" rx="2" fill="var(--good)"/>`;
      if(k%step===0||k===rows.length-1) g+=`<text x="${(x+bw/2).toFixed(1)}" y="${H-6}" text-anchor="middle">${r.y}</text>` });
    $('#dvchart').innerHTML=`<svg viewBox="0 0 ${W} ${H}" role="img">${g}</svg>`;
    $('#dvtable').innerHTML=`<thead><tr><th>${esc(t.year)}</th><th>${esc(t.contrib)}</th><th>${esc(t.val)}</th><th>${esc(t.divy)}</th></tr></thead><tbody>`+
      rows.map(r=>`<tr><td>${r.y}</td><td>${nf(r.c)}</td><td>${nf(r.v)}</td><td class="good">+${nf(r.d)}</td></tr>`).join('')+'</tbody>';
  }
  $$('.icard',box).forEach(b=>b.onclick=()=>{ $$('.icard',box).forEach(x=>x.classList.toggle('on',x===b)); $('#dvr').value=b.dataset.y; $('#dvg').value=b.dataset.dg; $('#dvq').value=b.dataset.pg; run() });
  $('#dvys').oninput=()=>{ $('#dvy').value=$('#dvys').value; run() };
  $$('input',box).forEach(i=>{ if(i.id!=='dvys') i.addEventListener('input',run) }); run();
})();

/* ---------- average buy price (/average-price/) ---------- */
(function(){
  const box=$('.icpage'); if(!box||!PAGE.av) return; const t=PAGE.av.t;
  const n=v=>{ const a=Math.abs(v); return NF('av'+(a>=1000?0:a>=1?2:6),{maximumFractionDigits:a>=1000?2:a>=1?4:8}).format(v) };
  let mode='s', rows=[{p:100,v:500},{p:80,v:500},{p:60,v:500}];
  try{ const s=JSON.parse(localStorage.getItem('wi_avg')||'null'); if(s&&Array.isArray(s.rows)){ rows=s.rows; mode=s.mode||'s' } }catch(e){}
  const save=()=>{ try{ localStorage.setItem('wi_avg',JSON.stringify({rows,mode})) }catch(e){} };
  function draw(){
    $$('#avmode button').forEach(b=>b.classList.toggle('on',b.dataset.v===mode)); $('#avh2').textContent=mode==='s'?t.sum:t.qty;
    $('#avrows').innerHTML=rows.map((r,i)=>`<tr><td>${i+1}</td><td><input type="number" min="0" step="any" data-i="${i}" data-k="p" value="${r.p||''}" aria-label="${esc(t.price)} ${i+1}"></td>`+
      `<td><input type="number" min="0" step="any" data-i="${i}" data-k="v" value="${r.v||''}" aria-label="${esc(mode==='s'?t.sum:t.qty)} ${i+1}"></td><td><button type="button" class="avdel" data-i="${i}" aria-label="${esc(t.del)}">✕</button></td></tr>`).join('');
    $$('#avrows input').forEach(e=>e.oninput=()=>{ rows[+e.dataset.i][e.dataset.k]=+e.value||0; save(); run() });
    $$('#avrows .avdel').forEach(b=>b.onclick=()=>{ rows.splice(+b.dataset.i,1); if(!rows.length) rows.push({p:0,v:0}); save(); draw() });
    run() }
  function run(){
    let q=0,c=0; rows.forEach(r=>{ if(!(r.p>0)||!(r.v>0)) return; const qq=mode==='s'?r.v/r.p:r.v; q+=qq; c+=qq*r.p });
    const avg=q?c/q:0, cur=+$('#avcur').value||0;
    $('#av_a').textContent=avg?n(avg):'—'; $('#av_q').textContent=q?n(q):'—'; $('#av_c').textContent=c?n(c):'—';
    const pl=$('#av_p'); if(cur&&q){ const v=q*cur-c; pl.textContent=(v>=0?'+':'−')+n(Math.abs(v))+' ('+fmtPct(v/c)+')'; pl.className=v>=0?'good':'bad' } else { pl.textContent='—'; pl.className='' }
    const tg=+$('#avtg').value||0, bp=+$('#avbp').value||0, out=$('#av_n'), nq=$('#av_nq');
    if(!(tg>0&&bp>0&&q)){ out.textContent='—'; nq.textContent=''; return }
    // (c + x) / (q + x/bp) = tg  →  x = (tg*q - c) / (1 - tg/bp)
    const den=1-tg/bp, x=den?(tg*q-c)/den:NaN;
    if(!isFinite(x)||x<0){ out.textContent='—'; nq.textContent=t.imp; return }
    out.textContent=n(x); nq.textContent=t.need_qty+': '+n(x/bp) }
  $('#avadd').onclick=()=>{ rows.push({p:0,v:0}); save(); draw(); const ins=$$('#avrows input'); ins[ins.length-2]&&ins[ins.length-2].focus() };
  $('#avclr').onclick=()=>{ rows=[{p:0,v:0}]; save(); draw() };
  $$('#avmode button').forEach(b=>b.onclick=()=>{ mode=b.dataset.v; save(); draw() });
  ['avcur','avtg','avbp'].forEach(id=>$('#'+id).addEventListener('input',run));
  $('#avasset').onchange=async e=>{ const id=e.target.value; if(!id) return;
    try{ const P=await fetch(`${BASE}/assets/p/${id}.json?v=${WI.v}`).then(r=>r.json()); const p=P.p[P.p.length-1]; $('#avcur').value=+p.toPrecision(6); run() }catch(err){} };
  draw();
})();

/* ---------- Ukrainian bonds (/ovdp/) ---------- */
(function(){
  const box=$('.icpage'); if(!box||!PAGE.ov) return; const C=PAGE.ov;
  let ccy='UAH', sym='₴';
  const nf=v=>{ try{ return new Intl.NumberFormat(T.intl||'uk',{style:'currency',currency:ccy,maximumFractionDigits:0}).format(v) }catch(e){ return Math.round(v)+' '+ccy } };
  const num=id=>Math.max(0,+$('#'+id).value||0);
  function run(){
    const a=num('ova'), m=+(($('#ovt button.on')||{}).dataset||{}).v||12, b=num('ovb')/100, d=num('ovd')/100, dev=num('ovv')/100;
    const ib=a*b*m/12, id=a*d*m/12*(1-0.23);
    $('#ov_b').textContent='+'+nf(ib); $('#ov_d').textContent='+'+nf(id); $('#ov_m').textContent='+'+nf(ib/m);
    const x=$('#ov_x'); x.textContent=(ib>=id?'+':'−')+nf(Math.abs(ib-id)); x.className=ib>=id?'good':'bad';
    const top=Math.max(ib,id,1);
    $('#ovbars').innerHTML=[[C.b,ib,'#f0b53a'],[C.dp,id,'#4f8cff']].map(r=>`<div class="icrow"><div class="h"><span>${esc(r[0])}</span><b>+${esc(nf(r[1]))}</b></div><div class="bar"><i style="width:${(r[1]/top*100).toFixed(1)}%;background:${r[2]}"></i></div></div>`).join('');
    const u=$('#ovusd'), w=$('#ovdevw'); u.hidden=w.hidden=ccy!=='UAH';
    if(ccy==='UAH'){ const r=(1+b*m/12)/Math.pow(1+dev,m/12)-1; const e=$('#ov_u'); e.textContent=fmtPct(r); e.className=r>=0?'good':'bad' } }
  $$('.icard',box).forEach(c=>c.onclick=()=>{ $$('.icard',box).forEach(x=>x.classList.toggle('on',x===c)); ccy=c.dataset.c; sym=c.dataset.s;
    $('#ovb').value=c.dataset.b; $('#ovd').value=c.dataset.d; $('#ova').value=ccy==='UAH'?100000:3000; $('#ova').nextElementSibling.textContent=sym; run() });
  $$('#ovt button').forEach(bt=>bt.onclick=()=>{ $$('#ovt button').forEach(x=>x.classList.toggle('on',x===bt)); run() });
  $$('input',box).forEach(i=>i.addEventListener('input',run)); run();
})();
/* footer columns collapse on phones */
if(innerWidth<640) $$('.fcols details').forEach(d=>d.open=false);
})();

/* ---------- click-to-sort for static tables (largest companies, «where it trades», exchanges, stablecoins) ---------- */
(function(){
  const MULT=[[/трлн|trn|tn\b|bio\.?|bln\b|T\b|兆/i,1e12],[/млрд|mrd|bn\b|B\b|tỷ|miliar|億/i,1e9],[/млн|mio|mln|M\b|triệu|juta|百万/i,1e6],[/тис|tys|K\b|k\b|nghìn|ribu|千/i,1e3]];
  const val=td=>{ const u=td.querySelector('[data-u]'); if(u) return +u.dataset.u;
    let t=(td.innerText||'').trim(); if(!t||t==='—') return null;
    let m=1; for(const [re,v] of MULT) if(re.test(t)){ m=v; break }
    t=t.replace(/[−–]/g,'-').replace(/[^\d,.\-]/g,'');
    if(/,\d{1,2}$/.test(t)&&!/\.\d{1,2}$/.test(t)) t=t.replace(/\./g,'').replace(',','.'); else t=t.replace(/,/g,'');
    const n=parseFloat(t); return isNaN(n)?(td.innerText||'').trim().toLowerCase():n*m };
  document.querySelectorAll('table.mt').forEach(tb=>{ if(tb.querySelector('#mthead')||!tb.tHead||!tb.tBodies[0]) return;
    const ths=[...tb.tHead.rows[0].cells]; let last=-1, dir=-1;
    ths.forEach((th,ci)=>{ if(!th.innerText.trim()) return; th.classList.add('sortable'); th.style.cursor='pointer'; th.title='↕';
      th.addEventListener('click',()=>{ dir=(last===ci)?-dir:(ci<=1?1:-1); last=ci;
        const body=tb.tBodies[0], rows=[...body.rows];
        rows.sort((a,b)=>{ const x=val(a.cells[ci]||a), y=val(b.cells[ci]||b); if(x==null) return 1; if(y==null) return -1;
          return (typeof x==='number'&&typeof y==='number'? x-y : String(x).localeCompare(String(y)))*dir });
        rows.forEach(r=>{ r.classList.remove('xh'); body.appendChild(r) });
        ths.forEach(h=>h.classList.remove('asc','desc')); th.classList.add(dir>0?'asc':'desc');
        const more=tb.closest('section')&&tb.closest('section').querySelector('.mkmore'); if(more) more.remove() }) }) });
})();

/* ---------- fresh posts between deploys: data/feed/<lang>.json (GitHub raw, made by scripts/feed.py) ---------- */
(function(){
  const RAW='https://raw.githubusercontent.com/AlekDu11/whatif-invest/main/data/feed/', L=PAGE.lang||'en', P=PAGE.prefix||'';
  const nl=/\/news\/$/.test(location.pathname)?document.querySelector('.nlist.own'):null, posts=document.querySelector('.posts[data-per]'), rd=document.getElementById('reader');
  if(!nl&&!posts&&!rd) return;
  const esc2=s=>String(s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const rurl=r=>`${P}/read/?k=${r.k}&s=${encodeURIComponent(r.s)}`;
  fetch(RAW+L+'.json',{cache:'no-cache'}).then(r=>r.ok?r.json():null).then(F=>{ if(!F) return; const items=F.items||[];
    if(nl){ const have=new Set([...nl.querySelectorAll('a.nrow')].map(a=>a.getAttribute('href')));
      const tags=(PAGE.news&&PAGE.news.tags)||{};
      const add=items.filter(r=>r.k==='news'&&!have.has(`${P}/news/${r.s}/`)).map(r=>`<a class="nrow fresh${r.cv?' nth':''}" data-g="${esc2((r.g||[]).join(' '))}" href="${rurl(r)}">${r.cv?`<img class="nthumb" src="${esc2(r.cv)}" alt="" width="160" height="84" loading="lazy">`:''}<span class="ntx"><b>${esc2(r.t)}</b><span class="muted">WhatIfStack · <time data-t="${esc2(r.d)}">${esc2(r.d)}</time> ${(r.g||[]).filter(g=>tags[g]).map(g=>`<i class="badge">${esc2(tags[g])}</i>`).join(' ')}</span></span></a>`).join('');
      if(add){ nl.insertAdjacentHTML('afterbegin',add); document.dispatchEvent(new Event('wi:news')) } }
    if(posts){ const have=new Set([...posts.querySelectorAll('a.post')].map(a=>a.getAttribute('href')));
      const cats={}; document.querySelectorAll('#bcats button[data-c]').forEach(b=>cats[b.dataset.c]=b.textContent.trim());
      const add=items.filter(r=>r.k==='blog'&&!have.has(`${P}/blog/${r.s}/`)).map(r=>`<a class="card post fresh" data-c="${esc2(r.c)}" href="${rurl(r)}">${r.cv?`<img class="thumb" src="${esc2(r.cv)}" alt="" width="600" height="315" loading="lazy">`:''}<div class="muted">${cats[r.c]?`<span class="badge">${esc2(cats[r.c])}</span> `:''}${esc2(r.d)}</div><h2>${esc2(r.t)}</h2><p>${esc2(r.x)}</p></a>`).join('');
      if(add){ posts.insertAdjacentHTML('afterbegin',add); document.dispatchEvent(new Event('wi:posts')) } }
    if(rd){ const q=new URLSearchParams(location.search), k=q.get('k'), s=q.get('s'), r=items.find(x=>x.k===k&&x.s===s);
      // once the daily deploy has built the real page, go there
      fetch(`${P}/${k}/${s}/`,{method:'HEAD'}).then(x=>{ if(x.ok&&!x.redirected) location.replace(`${P}/${k}/${s}/`) }).catch(()=>{});
      if(!r){ rd.innerHTML='<p class="muted">—</p>'; return }
      document.title=r.t+' | WhatIfStack';
      fetch(`${RAW}${L}/${k}-${encodeURIComponent(s)}.html`,{cache:'no-cache'}).then(x=>x.ok?x.text():'').then(h=>{
        const [body,tail]=h.split('<!--wi-tail-->');
        rd.innerHTML=`<h1>${esc2(r.t)}</h1>${r.cv?`<img class="cover" src="${esc2(r.cv)}" alt="" width="1200" height="630">`:''}<div class="muted byline">WhatIfStack Research · ${esc2(r.d)}</div><div class="artbody">${body}</div>${tail||''}`;
        if(typeof paintStars==='function') paintStars() }) }
  }).catch(()=>{});
})();

/* ---------- deposits calculator (/deposits-ukraine/): rate from the bank table, 23% tax, vs OVDP (tax-free) and inflation, 12-month history of other assets ---------- */
(function(){ const {T,nm,esc,fmtPct,cls,icon,BYID}=window.WIX||{}; const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
  const C=(window.PAGE||{}).dep; if(!C||!$('#dpa')||!T) return;
  let ccy='uah', term=12; const TI={12:0,9:1,6:2,3:3};
  const sym=()=>ccy==='uah'?'₴':'$';
  const f=v=>(Math.round(v)).toLocaleString(T.intl||'uk')+' '+sym(), pc=v=>(v*100).toFixed(2).replace('.',',')+'%';
  const bankRate=()=>{ const b=C.banks[$('#dpb').value]; if(!b) return null; const L=b[ccy==='uah'?0:1]; let r=L[TI[term]]; if(r==null){ for(const k of [12,9,6,3]){ if(L[TI[k]]!=null){ r=L[TI[k]]; break } } } return r };
  const setRate=()=>{ const r=bankRate(); if(r!=null) $('#dpr').value=r; calc() };
  function calc(){ const A=+$('#dpa').value||0, r=(+$('#dpr').value||0)/100, inf=(+$('#dpi').value||0)/100, y=term/12;
    const g=A*r*y, tx=g*C.tax/100, n=g-tx, ov=A*((ccy==='uah'?C.ovdp.uah:C.ovdp.usd)/100)*y, real=(A+n)/Math.pow(1+inf,y)-A;
    $('#dp_g').textContent=f(g); $('#dp_t').textContent='−'+f(tx); $('#dp_n').textContent='+'+f(n); $('#dp_e').textContent=f(A+n); $('#dp_r').textContent=pc(r*(1-C.tax/100));
    $('#dp_o').textContent='+'+f(ov)+(ov>n?` (+${f(ov-n)})`:''); const x=$('#dp_x'); x.textContent=(real>=0?'+':'−')+f(Math.abs(real)); x.className=real>=0?'good':'bad' }
  $$('#dpc button').forEach(b=>b.onclick=()=>{ ccy=b.dataset.v; $$('#dpc button').forEach(x=>x.classList.toggle('on',x===b)); if(ccy==='usd'&&+$('#dpa').value===100000) $('#dpa').value=2500; if(ccy==='uah'&&+$('#dpa').value===2500) $('#dpa').value=100000; $('#dpi').closest('.f').style.display=ccy==='uah'?'':'none'; setRate() });
  $$('#dpt button').forEach(b=>b.onclick=()=>{ term=+b.dataset.v; $$('#dpt button').forEach(x=>x.classList.toggle('on',x===b)); setRate() });
  $('#dpb').onchange=setRate; ['#dpa','#dpr','#dpi'].forEach(s=>$(s).oninput=calc); setRate();
  // history: lump sum a year ago in other assets (USD price change)
  const H=[['spy','S&P 500'],['gold',null],['btc',null]];
  Promise.all(H.map(([id])=>fetch(`/assets/p/${id}.json?v=${window.WI.v}`).then(r=>r.json()).catch(()=>null))).then(R=>{
    $('#dp_h').innerHTML=R.map((P,i)=>{ if(!P||P.p.length<13) return ''; const a=BYID[H[i][0]], ch=P.p[P.p.length-1]/P.p[P.p.length-13]-1;
      return `<div class="kv"><span>${a?icon(a):''} ${esc(H[i][1]||(a?nm(a):H[i][0]))}</span><b class="${cls(ch)}">${fmtPct(ch)}</b></div>` }).join('') });
})();

/* ---------- accounts: sign in by e-mail link / Telegram and sync portfolios, watchlists and bonds (api/_auth.js via /api/forms) ---------- */
(function(){
  const KEYS=['wi_pfs','wi_wls','wi_bonds','wi_pfccy','wi_hold','wi_watch'];
  const ls={ get:k=>{ try{ return localStorage.getItem(k) }catch(e){ return null } }, set:(k,v)=>{ try{ v==null?localStorage.removeItem(k):_set.call(localStorage,k,v) }catch(e){} } };
  let _set; try{ _set=Storage.prototype.setItem }catch(e){ return }
  const sid=()=>ls.get('wi_sid');
  const api=(k,opt={})=>fetch('/api/forms?k='+k,{method:opt.body?'POST':'GET',headers:Object.assign({'Content-Type':'application/json'},sid()?{'x-sid':sid()}:{}),body:opt.body?JSON.stringify(opt.body):undefined})
    .then(async r=>{ const j=await r.json().catch(()=>({})); if(!r.ok){ const e=new Error(j.e||r.status); e.status=r.status; throw e } return j });
  const J=s=>{ try{ return JSON.parse(s) }catch(e){ return null } };
  const snap=()=>{ const d={}; KEYS.forEach(k=>{ const v=ls.get(k); if(v!=null) d[k]=v }); return d };
  function merge(loc,srv){   // union: portfolios/watchlists by name, transactions and ids without duplicates; local wins on simple values
    const out=Object.assign({},srv,loc);
    const pl=J(loc.wi_pfs), ps=J(srv.wi_pfs);
    if(pl&&ps&&pl.list&&ps.list){ const by={}; [...ps.list,...pl.list].forEach(p=>{ const k=p.n||''; const g=by[k]||(by[k]={n:p.n,tx:[]}); const seen=new Set(g.tx.map(t=>JSON.stringify([t.a,t.s,t.q,t.p,t.t]))); (p.tx||[]).forEach(t=>{ const id=JSON.stringify([t.a,t.s,t.q,t.p,t.t]); if(!seen.has(id)){ seen.add(id); g.tx.push(t) } }) });
      out.wi_pfs=JSON.stringify({cur:pl.cur||0,list:Object.values(by)}) }
    const wl=J(loc.wi_wls), ws=J(srv.wi_wls);
    if(wl&&ws&&wl.list&&ws.list){ const by={}; [...ws.list,...wl.list].forEach(w=>{ const g=by[w.n]||(by[w.n]={n:w.n,ids:[]}); (w.ids||[]).forEach(i=>{ if(!g.ids.includes(i)) g.ids.push(i) }) }); out.wi_wls=JSON.stringify({cur:wl.cur||0,list:Object.values(by)}) }
    const bl=J(loc.wi_bonds), bs=J(srv.wi_bonds);
    if(Array.isArray(bl)&&Array.isArray(bs)){ const seen=new Set(bl.map(x=>JSON.stringify(x))); out.wi_bonds=JSON.stringify([...bl,...bs.filter(x=>!seen.has(JSON.stringify(x)))]) }
    return out }
  let t, busy=false;
  const push=()=>{ if(!sid()) return; clearTimeout(t); t=setTimeout(()=>{ if(busy) return push(); busy=true;
    api('data',{body:{d:snap()}}).then(j=>{ ls.set('wi_syncv',String(j.v)); ls.set('wi_dirty',null); document.dispatchEvent(new CustomEvent('wi:synced')) }).catch(e=>{ if(e.status===401) ls.set('wi_sid',null) }).finally(()=>{ busy=false }) },1500) };
  Storage.prototype.setItem=function(k,v){ _set.call(this,k,v); if(this===localStorage&&KEYS.includes(k)&&sid()){ _set.call(this,'wi_dirty','1'); push() } };
  async function pull(){ if(!sid()) return;
    try{ const s=await api('data'); const sv=+ls.get('wi_syncv')||0, dirty=!!ls.get('wi_dirty');
      if(s.d&&s.v>sv){ const loc=snap(); const has=Object.keys(loc).length;
        const nd=(dirty||!sv)&&has?merge(loc,s.d):s.d; const changed=KEYS.some(k=>(nd[k]||null)!==(loc[k]||null));
        KEYS.forEach(k=>ls.set(k,nd[k]==null?null:nd[k])); ls.set('wi_syncv',String(s.v));
        if(nd!==s.d) { ls.set('wi_dirty','1'); push() } else ls.set('wi_dirty',null);
        if(changed&&!sessionStorage.getItem('wi_reloaded')){ sessionStorage.setItem('wi_reloaded','1'); location.reload(); return } }
      else if(!s.d||dirty) push();
      document.dispatchEvent(new CustomEvent('wi:synced')) }catch(e){ if(e.status===401) ls.set('wi_sid',null) } }
  window.WIACC={api,pull,sid,set:ls.set,get:ls.get};
  pull();
})();
(function(){ const {T,esc,lang}=window.WIX||{}; const $=s=>document.querySelector(s);
  const box=$('#acct'); if(!box) return; let C; try{ C=JSON.parse(box.dataset.cfg) }catch(e){ return }
  const A=window.WIACC, inn=box.querySelector('.acct-in'), out=box.querySelector('.acct-out'), msg=$('#acctmsg');
  const say=(t,bad)=>{ if(!msg) return; msg.hidden=false; msg.textContent=t; msg.classList.toggle('bad',!!bad) };
  function show(){ const u=JSON.parse(A.get('wi_user')||'null');
    box.hidden=(A.sid()&&u)||(!C.mail&&!C.tg);   // owner 2026-11-22: no «Signed in as … Synced … Sign out» bar — account + sign-out live in the header 👤 popup
    if(A.sid()&&u){ out.hidden=true; inn.hidden=false;
      const v=+A.get('wi_syncv'); inn.innerHTML=`<span>✅ ${esc(C.in)} <b>${esc(u.name||'')}</b></span><span class="muted">${v?esc(C.sync)+' '+new Date(v).toLocaleTimeString(T.intl||'en',{hour:'2-digit',minute:'2-digit'}):''}</span><button class="btn ghost sm" type="button" id="acctout">${esc(C.out)}</button>`;
      $('#acctout').onclick=()=>{ A.api('logout',{body:{}}).catch(()=>{}).finally(()=>{ A.set('wi_sid',null); A.set('wi_user',null); A.set('wi_syncv',null); show() }) } }
    else { out.hidden=false; inn.hidden=true } }
  async function start(j){ A.set('wi_sid',j.sid); A.set('wi_user',JSON.stringify({name:j.name})); A.set('wi_syncv',null); A.set('wi_dirty','1'); show(); await A.pull(); show() }
  const q=new URLSearchParams(location.search), tok=q.get('login');
  if(tok){ history.replaceState(null,'',location.pathname+location.hash);
    A.api('verify',{body:{t:tok}}).then(start).catch(e=>say(e.status===410?C.exp:C.err,true)) }
  const f=$('#acctf'); if(f) f.onsubmit=e=>{ e.preventDefault(); const b=f.querySelector('button'); b.disabled=true;
    A.api('login',{body:{em:f.em.value,l:lang,hp:f.hp.value}}).then(()=>{ say(C.sent); f.hidden=true }).catch(()=>say(C.err,true)).finally(()=>{ b.disabled=false }) };
  if(C.tg&&!A.sid()){ window.wiTgAuth=u=>A.api('tg',{body:u}).then(start).catch(()=>say(C.err,true));
    const s=document.createElement('script'); s.async=true; s.src='https://telegram.org/js/telegram-widget.js?22';
    s.setAttribute('data-telegram-login',C.tg); s.setAttribute('data-size','large'); s.setAttribute('data-radius','10'); s.setAttribute('data-onauth','wiTgAuth(user)'); s.setAttribute('data-request-access','write');
    $('#tglogin').appendChild(s) }
  if(C.g&&!A.sid()){ const s=document.createElement('script'); s.src='https://accounts.google.com/gsi/client'; s.async=true; s.onload=()=>{ try{
      google.accounts.id.initialize({client_id:C.g, callback:r=>A.api('google',{body:{c:r.credential}}).then(start).catch(()=>say(C.err,true))});
      google.accounts.id.renderButton($('#glogin'),{theme:document.documentElement.dataset.theme==='dark'?'filled_black':'outline',size:'large',shape:'pill',locale:(C.loc||'').split('-')[0]}) }catch(e){} }; document.head.appendChild(s) }
  if(/[?&]tgapp=1/.test(location.search)){   // opened from the bot's «Portfolio» button: sign in silently with Telegram's signed data
    const s=document.createElement('script'); s.src='https://telegram.org/js/telegram-web-app.js'; s.onload=()=>{ const W=window.Telegram&&Telegram.WebApp; if(!W) return; try{ W.ready(); W.expand() }catch(e){}
      if(W.initData&&!A.sid()) A.api('tgapp',{body:{d:W.initData}}).then(start).catch(()=>{}) }; document.head.appendChild(s) }
  document.addEventListener('wi:synced',show); show();
})();

/* ---------- home «Today in the markets»: live movers, trending and fresh news between deploys (owner 2026-11-21) ---------- */
(function(){ const W=window.WIX||{}, PG0=window.PAGE||{}; if(!(PG0.home||PG0.stx)||!W.T||!document.querySelector('[data-mv]')) return;   // home + /stocks/ «Stocks today»
  const {IDX,BYID,esc,fmtPrice,fmtPct,icon,url,nm}=W;
  const row=(a,p,c)=>`<a class="mrow" href="${url(a.i)}">${icon(a)}<span class="mn"><b>${esc(a.t)}</b><span>${esc(nm(a))}</span></span><span class="mp" data-p="${a.i}">${fmtPrice(p)}</span><span class="mc ${c>=0?'good':'bad'}">${fmtPct(c)}</span></a>`;
  const fill=(k,rows)=>{ const el=document.querySelector(`[data-mv="${k}"]`); if(!el||!rows.length) return; const h=el.querySelector('.wt').outerHTML; el.innerHTML=h+rows.map(r=>row(...r)).join('') };
  // crypto: CoinGecko symbol → our coin (biggest one with that ticker)
  const bySym={}; IDX.filter(a=>a.c==='crypto'&&!a.st).sort((x,y)=>x.o-y.o).forEach(a=>{ const t=a.t.toUpperCase(); if(!bySym[t]) bySym[t]=a });
  const stocks=IDX.filter(a=>a.c==='stock'&&a.y).sort((x,y)=>x.o-y.o).slice(0,150);
  fetch(`${(window.PAGE||{}).base||''}/api/quote?mv=1&s=${stocks.map(a=>a.y).join(',')}`).then(r=>r.ok?r.json():null).then(D=>{ if(!D) return;
    const cr=(D.c||[]).filter(x=>x[4]>=1e9&&bySym[x[0]]).map(x=>[bySym[x[0]],x[2],x[3]]);
    cr.forEach(([a,p,c])=>{ a.pr=p; a.ch=c });
    const up=cr.filter(x=>x[2]>0).sort((x,y)=>y[2]-x[2]).slice(0,5), dn=cr.filter(x=>x[2]<0).sort((x,y)=>x[2]-y[2]).slice(0,5);
    fill('crypto+',up); fill('crypto-',dn);
    const st=stocks.filter(a=>D.s&&D.s[a.y]).map(a=>[a,D.s[a.y][0],D.s[a.y][1]]);
    if(st.length>=20){ fill('stock+',st.filter(x=>x[2]>0).sort((x,y)=>y[2]-x[2]).slice(0,5)); fill('stock-',st.filter(x=>x[2]<0).sort((x,y)=>x[2]-y[2]).slice(0,5)) }
    const cgp={}; (D.c||[]).forEach(x=>cgp[x[1]]=x);
    const tr=(D.t||[]).map(x=>{ const a=bySym[x[0]], m=cgp[x[1]]; return a&&m?[a,m[2],m[3]]:null }).filter(Boolean).slice(0,5);
    if(tr.length>=3) fill('trend',tr);
    document.dispatchEvent(new Event('wi:rows'));   // new coins in the cards → live streams resubscribe
  }).catch(()=>{});
  // news: newest briefs from data/feed (GitHub raw), so the card is never a day old
  const nl=document.getElementById('hnews'); if(!nl) return;
  const PG=window.PAGE||{}, P=PG.prefix||'', L=PG.lang||'en'; let tags={}; try{ tags=JSON.parse(nl.dataset.tags||'{}') }catch(e){}
  fetch(`https://raw.githubusercontent.com/AlekDu11/whatif-invest/main/data/feed/${L}.json`,{cache:'no-cache'}).then(r=>r.ok?r.json():null).then(F=>{ if(!F) return;
    const have=new Set([...nl.querySelectorAll('a.nrow')].map(a=>a.getAttribute('href')));
    const fresh=(F.items||[]).filter(r=>r.k==='news'&&!have.has(`${P}/news/${r.s}/`)).sort((x,y)=>(y.d||'').localeCompare(x.d||'')).slice(0,4);
    if(!fresh.length) return;
    nl.insertAdjacentHTML('afterbegin',fresh.map(r=>`<a class="nrow fresh" href="${P}/read/?k=news&s=${encodeURIComponent(r.s)}"><span class="ntx"><b>${esc(r.t)}</b><span class="muted">WhatIfStack · <time data-t="${esc(r.d)}">${esc(r.d)}</time> ${(r.g||[]).filter(g=>tags[g]).map(g=>`<i class="badge">${esc(tags[g])}</i>`).join(' ')}</span></span></a>`).join(''));
    [...nl.querySelectorAll('a.nrow')].slice(4).forEach(a=>a.remove());
  }).catch(()=>{});
})();

/* ---------- live prices for coins outside Binance (owner 2026-11-21): OKX, Bybit and Gate WebSockets, MEXC every 15 s via /api/quote?mx= ----------
   Only coins shown on the page (and the portfolio's holdings); connections close when the tab is hidden. Index field x: g=Gate, o=OKX, y=Bybit, m=MEXC. */
(function(){ const W=window.WIX||{}; if(!('WebSocket' in window)||!W.IDX||document.querySelector('.art')) return;
  const {BYID,fmtPrice,fmtPct,cls}=W, $$=s=>[...document.querySelectorAll(s)];
  const coins=()=>{ const ids=new Set($$('[data-p],[data-c],[data-h]').map(el=>el.dataset.p||el.dataset.c||el.dataset.h));
    if(document.getElementById('hold')) try{ JSON.parse(localStorage.getItem('wi_hold')||'[]').forEach(x=>ids.add(x.id)) }catch(e){}
    return [...ids].map(i=>BYID[i]).filter(a=>a&&a.c==='crypto'&&!a.bn&&a.x).slice(0,120) };
  const byTk={}; const put=(a,p,ch)=>{ if(!(p>0)) return; const old=a.pr; a.pr=p; if(ch!=null&&isFinite(ch)) a.ch=ch;
    $$(`[data-p="${a.i}"]`).forEach(el=>{ el.textContent=fmtPrice(p); if(old&&p!==old){ el.classList.remove('flash-up','flash-dn'); void el.offsetWidth; el.classList.add(p>old?'flash-up':'flash-dn') } });
    if(ch!=null) $$(`[data-c="${a.i}"]`).forEach(el=>{ el.textContent=fmtPct(a.ch); el.classList.remove('good','bad'); el.classList.add(cls(a.ch)) });
    document.dispatchEvent(new CustomEvent('wi:tick',{detail:a})) };
  const EX={
    o:{url:'wss://ws.okx.com:8443/ws/v5/public', sub:t=>[{op:'subscribe',args:t.map(x=>({channel:'tickers',instId:x+'-USDT'}))}], ping:'ping',
       msg:m=>(m.data||[]).forEach(d=>{ const a=byTk['o'+(d.instId||'').replace('-USDT','')]; if(a) put(a,+d.last,+d.open24h>0?d.last/d.open24h-1:null) })},
    y:{url:'wss://stream.bybit.com/v5/public/spot', sub:t=>{ const r=[]; for(let i=0;i<t.length;i+=10) r.push({op:'subscribe',args:t.slice(i,i+10).map(x=>'tickers.'+x+'USDT')}); return r }, ping:'{"op":"ping"}',
       msg:m=>{ const d=m.data; if(!d||!d.symbol) return; const a=byTk['y'+d.symbol.replace(/USDT$/,'')]; if(a) put(a,+d.lastPrice,d.price24hPcnt!=null?+d.price24hPcnt:null) }},
    g:{url:'wss://api.gateio.ws/ws/v4/', sub:t=>[{time:Math.floor(Date.now()/1000),channel:'spot.tickers',event:'subscribe',payload:t.map(x=>x+'_USDT')}], ping:()=>JSON.stringify({time:Math.floor(Date.now()/1000),channel:'spot.ping'}),
       msg:m=>{ const d=m.result; if(m.event!=='update'||!d||!d.currency_pair) return; const a=byTk['g'+d.currency_pair.replace(/_USDT$/,'')]; if(a) put(a,+d.last,d.change_percentage!=null?d.change_percentage/100:null) }}};
  const open={}; let want='', mxT=null;
  function stop(){ Object.values(open).forEach(o=>{ o.dead=1; clearInterval(o.pi); try{o.ws.close()}catch(e){} }); for(const k in open) delete open[k]; clearInterval(mxT); mxT=null; clearInterval(window.__xtT) }
  function start(){ const L=coins(); want=L.map(a=>a.i).join(','); if(!L.length) return;
    for(const k in byTk) delete byTk[k]; L.forEach(a=>byTk[a.x+a.t.toUpperCase()]=a);
    Object.keys(EX).forEach(k=>{ const t=L.filter(a=>a.x===k).map(a=>a.t.toUpperCase()); if(!t.length) return; const E=EX[k];
      const go=(n)=>{ let ws; try{ ws=new WebSocket(E.url) }catch(e){ return } const o=open[k]={ws};
        ws.onopen=()=>{ E.sub(t).forEach(m=>ws.send(JSON.stringify(m))); o.pi=setInterval(()=>{ try{ ws.send(typeof E.ping==='function'?E.ping():E.ping) }catch(e){} },20000) };
        ws.onmessage=ev=>{ if(ev.data==='pong') return; let m; try{ m=JSON.parse(ev.data) }catch(e){ return } E.msg(m) };
        ws.onclose=()=>{ clearInterval(o.pi); if(!o.dead&&!document.hidden&&n<5) setTimeout(()=>go(n+1),3000*(n+1)) } };
      go(0) });
    const xt=L.filter(a=>'kbhn'.includes(a.x)&&a.xs), dx=L.filter(a=>a.x==='d'&&a.xs);
    if(xt.length||dx.length){ const poll2=()=>{ if(wiAway()) return;
      if(xt.length) fetch(`${(window.PAGE||{}).base||''}/api/quote?xt=${xt.map(a=>a.x+':'+a.xs).join(',')}`).then(r=>r.ok?r.json():null).then(Q=>{ if(Q) xt.forEach(a=>{ const q=Q[a.xs]; if(q) put(a,q[0],q[1]) }) }).catch(()=>{});
      dx.forEach(a=>{ const [n,p]=a.xs.split('/'); fetch(`${(window.PAGE||{}).base||''}/api/chart?dex=pool&n=${n}&p=${p}`).then(r=>r.ok?r.json():null).then(q=>{ if(q&&q.pr) put(a,+q.pr,q.c24!=null?q.c24/100:null) }).catch(()=>{}) }) };
      poll2(); clearInterval(window.__xtT); window.__xtT=setInterval(poll2,30000) }
    const mx=L.filter(a=>a.x==='m'); if(mx.length){ const poll=()=>{ if(wiAway()) return;
      fetch(`${(window.PAGE||{}).base||''}/api/quote?mx=${mx.map(a=>a.t.toUpperCase()).join(',')}`).then(r=>r.ok?r.json():null).then(Q=>{ if(Q) mx.forEach(a=>{ const q=Q[a.t.toUpperCase()]; if(q) put(a,q[0],q[1]) }) }).catch(()=>{}) };
      poll(); mxT=setInterval(poll,15000) } }
  document.addEventListener('visibilitychange',()=>{ if(document.hidden) stop(); else start() });
  let rt; document.addEventListener('wi:rows',()=>{ clearTimeout(rt); rt=setTimeout(()=>{ if(document.hidden) return; const L=coins().map(a=>a.i).join(','); if(L!==want){ stop(); start() } },500) });
  setTimeout(start,800);
})();

/* ---------- account button in the header + «sign in so you don't lose it» nudges (owner 2026-11-21) ----------
   Signed in → the header button shows the user's initial and opens the cabinet. Not signed in → after starring an asset or adding
   to the portfolio, or on a return visit with a watchlist/portfolio, a small card invites to sign in with Google (once per 3 days). */
(function(){ const P=window.PAGE||{}, N=P.nudge; const $=s=>document.querySelector(s);
  const g=k=>{ try{ return localStorage.getItem(k) }catch(e){ return null } }, s=(k,v)=>{ try{ localStorage.setItem(k,v) }catch(e){} };
  const esc=x=>String(x||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const signed=()=>!!g('wi_sid')&&!!g('wi_user');
  const btn=$('#acctb');
  // header popup: sign in with Google right here (like every site does), or — when signed in — cabinet / watchlist / sign out
  if(btn&&N){ btn.addEventListener('click',e=>{ if(e.metaKey||e.ctrlKey) return; e.preventDefault(); let pop=$('#acpop'); if(pop){ pop.remove(); return }
    pop=document.createElement('div'); pop.id='acpop'; pop.className='card acpop';
    const r=btn.getBoundingClientRect(), vw=document.documentElement.clientWidth;
    if(vw<640){ pop.style.position='fixed'; pop.style.top=Math.max(8,r.bottom+8)+'px'; pop.style.left='12px'; pop.style.right='12px'; pop.style.width='auto' }   // phone: full width under the header, never off-screen
    else{ pop.style.top=(r.bottom+window.scrollY+8)+'px'; pop.style.right=Math.max(8,Math.min(vw-r.right,vw-308))+'px' }
    if(signed()){ let n=''; try{ n=(JSON.parse(g('wi_user'))||{}).name||'' }catch(e){}
      pop.innerHTML=`<b>👤 ${esc(n)}</b><a href="${esc(N.me)}">💼 ${esc(N.cab)}</a><a href="${esc(N.wlu)}">★ ${esc(N.wl)}</a><button type="button" class="btn ghost sm" id="acpout">${esc(N.out)}</button>`;
      document.body.appendChild(pop);
      $('#acpout').onclick=()=>{ const A=window.WIACC; (A?A.api('logout',{body:{}}):Promise.resolve()).catch(()=>{}).finally(()=>{ ['wi_sid','wi_user','wi_syncv'].forEach(k=>{ try{ localStorage.removeItem(k) }catch(e){} }); location.reload() }) } }
    else{ pop.innerHTML=`<b>${esc(N.login)}</b><p class="muted">${esc(N.d1)}</p><div id="gpop"></div><p class="acperr bad" hidden></p>`; document.body.appendChild(pop);
      const go=()=>{ try{ google.accounts.id.initialize({client_id:N.g, callback:res=>{ const A=window.WIACC; if(!A) return;
          A.api('google',{body:{c:res.credential}}).then(async j=>{ A.set('wi_sid',j.sid); A.set('wi_user',JSON.stringify({name:j.name})); A.set('wi_syncv',null); A.set('wi_dirty','1'); await A.pull(); location.reload() })
            .catch(()=>{ const m=pop.querySelector('.acperr'); m.hidden=false; m.textContent=N.err }) }});
        google.accounts.id.renderButton($('#gpop'),{theme:'outline',size:'large',shape:'pill',width:260,locale:(N.loc||'').split('-')[0]}) }catch(e){} };
      if(window.google&&google.accounts) go(); else { const sc=document.createElement('script'); sc.src='https://accounts.google.com/gsi/client'; sc.async=true; sc.onload=go; document.head.appendChild(sc) } }
    setTimeout(()=>document.addEventListener('click',function off(ev){ if(!pop.contains(ev.target)&&ev.target!==btn&&!btn.contains(ev.target)){ pop.remove(); document.removeEventListener('click',off) } }),0) }) }
  function paint(){ if(!btn) return; if(signed()){ let n=''; try{ n=(JSON.parse(g('wi_user'))||{}).name||'' }catch(e){}
      btn.classList.add('on'); btn.title=btn.dataset.in; btn.setAttribute('aria-label',btn.dataset.in); btn.href=btn.href.split('#')[0];
      btn.innerHTML=`<span class="acin">${esc((n.trim()[0]||'✓').toUpperCase())}</span>` } }
  paint(); document.addEventListener('wi:synced',paint);
  if(!N||signed()||/\/me\/?$/.test(location.pathname)) return;
  const has=()=>{ try{ return (JSON.parse(g('wi_watch')||'[]').length+JSON.parse(g('wi_hold')||'[]').length)>0 }catch(e){ return false } };
  function show(){ if(signed()||$('#acnudge')) return; const last=+g('wi_nudge')||0; if(Date.now()-last<3*864e5) return; s('wi_nudge',String(Date.now()));
    const d=document.createElement('div'); d.id='acnudge'; d.className='card acnudge'; d.setAttribute('role','dialog');
    d.innerHTML=`<button class="x" type="button" aria-label="×">×</button><b>💾 ${esc(N.h)}</b><p>${esc(N.d)}</p><a class="btn" href="${esc(N.u)}"><svg width="16" height="16" viewBox="0 0 48 48" aria-hidden="true"><path fill="#FFC107" d="M43.6 20.5H42V20H24v8h11.3C33.7 32.7 29.2 36 24 36c-6.6 0-12-5.4-12-12s5.4-12 12-12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 12.9 4 4 12.9 4 24s8.9 20 20 20 20-8.9 20-20c0-1.3-.1-2.4-.4-3.5z"/><path fill="#FF3D00" d="M6.3 14.7l6.6 4.8C14.7 15.1 19 12 24 12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 16.3 4 9.7 8.3 6.3 14.7z"/><path fill="#4CAF50" d="M24 44c5.2 0 9.9-2 13.4-5.2l-6.2-5.2C29.2 35.1 26.7 36 24 36c-5.2 0-9.6-3.3-11.3-8l-6.5 5C9.5 39.6 16.2 44 24 44z"/><path fill="#1976D2" d="M43.6 20.5H42V20H24v8h11.3c-.8 2.2-2.2 4.2-4.1 5.6l6.2 5.2C37 39.2 44 34 44 24c0-1.3-.1-2.4-.4-3.5z"/></svg> ${esc(N.b)}</a>`;
    document.body.appendChild(d); d.querySelector('.x').onclick=()=>d.remove();
    if(btn) d.querySelector('a.btn').onclick=e=>{ e.preventDefault(); d.remove(); window.scrollTo({top:0,behavior:'smooth'}); setTimeout(()=>btn.click(),250) } }
  document.addEventListener('click',e=>{ if(e.target.closest('.star[data-s],.addpf,[data-add],a[href*="?add="]')) setTimeout(show,1200) },true);
  if(has()) setTimeout(show,25000);   // a returning visitor who already tracks something
})();

/* ---------- live price widget builder (/widgets/): tickers → iframe /embed/price/ + a real backlink under it ---------- */
(function(){ const box=document.querySelector('.embprice'); if(!box) return; let C; try{ C=JSON.parse(box.dataset.cfg) }catch(e){ return }
  const W=window.WIX||{}, esc=W.esc||(s=>s), $$=s=>[...box.querySelectorAll(s)];
  let list='BTC, ETH, SOL, XRP, GOLD', th='light';
  box.innerHTML=`<div class="embf"><label class="f">${esc(C.pick)}<div class="inp"><input class="ep" value="${esc(list)}"></div></label>
    <div class="f">${esc(C.theme)}<div class="seg">${[['light',C.light],['dark',C.dark],['auto',C.auto]].map(([v,l])=>`<button type="button" data-v="${v}"${v===th?' class="on"':''}>${esc(l)}</button>`).join('')}</div></div></div>
    <div class="embprev"><iframe title="preview" loading="lazy" style="height:290px"></iframe></div><p class="muted embhelp">${esc(C.help)}</p>
    <div class="embcode"><textarea readonly rows="4"></textarea><button type="button" class="btn">${esc(C.copy)}</button></div>`;
  const ifr=box.querySelector('iframe'), ta=box.querySelector('textarea');
  const ids=()=>{ const out=[]; list.split(/[,\s]+/).map(x=>x.trim().toLowerCase()).filter(Boolean).forEach(t=>{ const a=(W.IDX||[]).find(y=>y.i===t)||(W.IDX||[]).find(y=>y.t.toLowerCase()===t); if(a&&!out.includes(a.i)) out.push(a.i) }); return out.slice(0,8) };
  const upd=()=>{ const a=ids(); if(!a.length) return; const q=`a=${a.join(',')}&l=${C.l}&th=${th}`, base='https://whatifstack.com', h=60+a.length*39;
    ifr.src=`/embed/price/?${q}`; ifr.style.height=h+'px';
    ta.value=`<iframe src="${base}/embed/price/?${q}" width="100%" height="${h}" style="border:0;max-width:520px" loading="lazy" title="${esc(C.anchor)}"></iframe>\n<p style="margin:4px 0;font-size:13px"><a href="${base}${C.l==='uk'?'':'/'+C.l}/crypto/">${esc(C.anchor)}</a></p>` };
  box.querySelector('.ep').addEventListener('input',e=>{ list=e.target.value; clearTimeout(box._t); box._t=setTimeout(upd,500) });
  box.addEventListener('click',e=>{ const b=e.target.closest('.seg button'); if(b){ th=b.dataset.v; $$('.seg button').forEach(x=>x.classList.toggle('on',x===b)); upd() }
    if(e.target.closest('.embcode .btn')){ ta.select(); (navigator.clipboard?navigator.clipboard.writeText(ta.value):Promise.reject()).catch(()=>document.execCommand('copy')); const bt=e.target.closest('.btn'); bt.textContent=C.copied; setTimeout(()=>bt.textContent=C.copy,1600) } });
  upd();
})();

/* ---------- /crypto/gainers-losers/: live top-1000 movers (api/quote?gl=1, CoinGecko, CDN 5 min), 24h / 7d, market-cap filter ---------- */
(function(){ const bar=document.getElementById('glbar'); if(!bar) return; const W=window.WIX||{}; const {IDX,esc,fmtPrice,fmtPct,icon,url,nm,fmtUsd}=W;
  let C={}; try{ C=JSON.parse(bar.dataset.cfg) }catch(e){} let per='d', min=0, D=null;
  const bySym={}; (IDX||[]).filter(a=>a.c==='crypto'&&!a.st).sort((x,y)=>x.o-y.o).forEach(a=>{ const t=a.t.toUpperCase(); if(!bySym[t]) bySym[t]=a });
  const mc=v=>v>=1e12?'$'+(v/1e12).toFixed(2)+'T':v>=1e9?'$'+(v/1e9).toFixed(2)+'B':v>=1e6?'$'+(v/1e6).toFixed(1)+'M':'$'+Math.round(v/1e3)+'K';
  function draw(){ if(!D) return; const k=per==='d'?3:4;
    const L=D.c.filter(x=>x[k]!=null&&x[5]>=min&&bySym[x[0]]);
    const row=(x,n)=>{ const a=bySym[x[0]]; return `<tr><td class="l n hide-sm">${n}</td><td class="l"><a class="asset" href="${url(a.i)}">${icon(a)}<span><span class="nm">${esc(nm(a))}</span><span class="tk">${esc(a.t)}</span></span></a></td><td data-p="${a.i}">${fmtPrice(x[2])}</td><td class="${x[k]>=0?'good':'bad'}">${fmtPct(x[k])}</td><td class="hide-sm">${mc(x[5])}</td></tr>` };
    document.getElementById('glup').innerHTML=L.filter(x=>x[k]>0).sort((a,b)=>b[k]-a[k]).slice(0,30).map((x,i)=>row(x,i+1)).join('');
    document.getElementById('gldn').innerHTML=L.filter(x=>x[k]<0).sort((a,b)=>a[k]-b[k]).slice(0,30).map((x,i)=>row(x,i+1)).join('');
    document.querySelectorAll('th#glk').forEach(th=>th.textContent=per==='d'?C.t24:C.t7);
    const u=document.getElementById('glupd'); if(u&&(window.PAGE||{}).glupd) u.textContent='· '+PAGE.glupd;
    document.dispatchEvent(new Event('wi:rows')) }
  bar.addEventListener('click',e=>{ const b=e.target.closest('button'); if(!b) return; const s=b.parentNode; s.querySelectorAll('button').forEach(x=>x.classList.toggle('on',x===b));
    if(s.id==='glper') per=b.dataset.k; else min=+b.dataset.m; if(D) draw(); else load() });
  function load(){ fetch(`${(window.PAGE||{}).base||''}/api/quote?gl=1`).then(r=>r.ok?r.json():null).then(j=>{ if(j&&j.c){ D=j; draw() } }).catch(()=>{}) }
  load(); setInterval(()=>{ if(!wiAway()) load() },300000);
})();

/* ---------- /investors/<id>/: «Follow this portfolio» → its stocks become a watchlist named after the investor ---------- */
(function(){ const b=document.getElementById('invfollow'), WLS=window.WLS, esc=(window.WIX||{}).esc||(x=>x); if(!b||!WLS) return; let C={}; try{ C=JSON.parse(b.dataset.cfg) }catch(e){}
  b.onclick=()=>{ const ids=(b.dataset.ids||'').split(',').filter(Boolean), n=b.dataset.n; const S=WLS.rd();
    let k=S.list.findIndex(w=>w.n===n); if(k<0){ S.list.push({n,ids:[]}); k=S.list.length-1 }
    ids.forEach(i=>{ if(!S.list[k].ids.includes(i)) S.list[k].ids.push(i) }); S.cur=k; WLS.wr(S);
    b.outerHTML=`<span class="pill up">✓ ${esc((C.done||'').replace('{n}',n))}</span> <a class="btn ghost sm" href="${C.u}">${esc(C.open||'')} →</a>` };
})();

/* ---------- live «$10 a day» results inside articles and analyses (owner 2026-11-22): units bought × live price ---------- */
(function(){
  const F=window.WIF; if(!F) return; const {fmtUsd,fmtPct,cls,BYID}=F, $$=s=>[...document.querySelectorAll(s)];
  const els=$$('[data-di],[data-dr],[data-yi]'); if(!els.length) return;
  function upd(a){ if(!a||!(a.pr>0)) return;
    $$(`[data-di="${a.i}"]`).forEach(el=>{ const u=+el.dataset.du; if(!u) return; const v=u*a.pr; el.dataset.u=v; el.textContent=fmtUsd(v) });
    $$(`[data-dr="${a.i}"]`).forEach(el=>{ const u=+el.dataset.du, inv=+el.dataset.dv; if(!u||!inv) return; const r=u*a.pr/inv-1;
      el.textContent=fmtPct(r); el.classList.remove('good','bad'); el.classList.add(cls(r)) });
    $$(`[data-yi="${a.i}"]`).forEach(el=>{ const y0=+el.dataset.y0; if(!y0) return; const r=a.pr/y0-1;
      el.textContent=fmtPct(r); el.classList.remove('good','bad'); el.classList.add(cls(r)) }) }
  new Set(els.map(el=>el.dataset.di||el.dataset.dr||el.dataset.yi)).forEach(i=>upd(BYID[i]));
  document.addEventListener('wi:tick',e=>upd(e.detail));
})();

/* ---------- earnings calendar: hide days that are already over (pages are rebuilt once a day) ---------- */
(function(){ const els=document.querySelectorAll('[data-ed]'); if(!els.length) return; const today=new Date().toISOString().slice(0,10);
  els.forEach(el=>{ if(el.dataset.ed<today) el.remove() }) })();

/* ---------- onboarding tour (owner 2026-11-23): first visit → short walk-through of what the site can do; skip any time; replay from Tools («✨») ---------- */
(function(){
  const P=window.PAGE||{}; if(!P.lang) return;
  const ua=navigator.userAgent||''; if(navigator.webdriver||/bot|crawl|spider|slurp|lighthouse|headless|preview/i.test(ua)) return;
  if(window.top!==window||/[?&]tgapp=1/.test(location.search)||/\/(embed|read)\//.test(location.pathname)) return;
  const get=k=>{ try{ return localStorage.getItem(k) }catch(e){ return '1' } }, put=(k,v)=>{ try{ localStorage.setItem(k,v) }catch(e){} };
  const ev=(a,s)=>{ try{ window.gtag&&window.gtag('event','tour',{tour_action:a,tour_step:s||''}) }catch(e){} };
  const E=x=>String(x==null?'':x).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const STEPS=[['stk','.herox .cchips'],['stk','.nav a[href$="/stocks/"]'],['stk','.mnav a[href$="/stocks/"]'],['cry','.nav a[href$="/crypto/"]'],['cry','.strip'],['search','.gsearch'],['calc','.herox .qcalc'],['calc','.herox'],['acalc','#calc'],['watch','.top a.me[href$="/watchlist/"]'],['pf','.top a.me[href$="/me/"]'],['tools','.nav .ddt>summary'],['tools','#mmore'],['ai','.aibtn']];
  const vis=el=>{ if(!el) return false; const r=el.getBoundingClientRect(); return r.width>0&&r.height>0&&getComputedStyle(el).visibility!=='hidden' };
  let S=null, steps=[], i=-1, ov=null, onMove=null;
  const load=()=>S?Promise.resolve(S):fetch(`${P.base||''}/assets/tour/${P.lang}.json`).then(r=>r.json()).then(j=>S=j);
  function close(how){ if(!ov) return; ov.remove(); ov=null; window.removeEventListener('resize',onMove); window.removeEventListener('scroll',onMove,true); put('wi_tour',how||'done'); ev(how||'done',steps[i]&&steps[i][0]) }
  function btns(first,last){ return `<div class="trb"><button type="button" class="trs" data-a="skip">${E(S.skip)}</button><span class="trd">${steps.map((_,k)=>`<i${k===i?' class=on':''}></i>`).join('')}</span>`+
    (first?'':`<button type="button" class="btn ghost" data-a="back">${E(S.back)}</button>`)+`<button type="button" class="btn" data-a="${last?'end':'next'}">${E(last?S.done:S.next)}</button></div>` }
  function place(){ if(!ov||i<0) return; const el=steps[i][2], r=el.getBoundingClientRect(), sp=ov.querySelector('.trsp'), bx=ov.querySelector('.trbox'), pad=6;
    sp.style.cssText=`top:${r.top-pad}px;left:${r.left-pad}px;width:${r.width+pad*2}px;height:${r.height+pad*2}px`;
    const W=innerWidth, H=innerHeight, bw=Math.min(400,W-24); bx.style.width=bw+'px'; const bh=bx.offsetHeight;
    let top=r.bottom+14; if(top+bh>H-10) top=Math.max(10,r.top-bh-14); if(top+bh>H-10) top=Math.max(10,H-bh-10);
    let left=Math.min(Math.max(12,r.left+r.width/2-bw/2),W-bw-12); bx.style.top=top+'px'; bx.style.left=left+'px' }
  function show(n){ i=n; const [k,,el]=steps[i]; ov.className='tour'; ov.innerHTML=`<div class="trsp"></div><div class="trbox card" role="dialog" aria-label="WhatIfStack" aria-live="polite"><p>${E(S[k])}</p>${btns(i===0,i===steps.length-1)}</div>`;
    const r=el.getBoundingClientRect(); if(r.top<70||r.bottom>innerHeight-40){ el.scrollIntoView({block:'center',behavior:'smooth'}); setTimeout(place,420) } place() }
  function center(h,p,b){ ov.className='tour trc'; ov.innerHTML=`<div class="trbox card trmid" role="dialog" aria-label="${E(h)}"><h3>${E(h)}</h3><p>${p}</p>${b}</div>` }
  function welcome(){ center(S.wh,E(S.wp),`<div class="trb"><button type="button" class="trs" data-a="skip">${E(S.skip)}</button><button type="button" class="btn" data-a="go">${E(S.go)}</button></div>`) }
  function end(){ i=-1; center(S.eh,`${E(S.ep)} <a href="${E(S.gu)}">${E(S.guide)} →</a>`,`<div class="trb"><span></span><button type="button" class="btn" data-a="close">${E(S.done)}</button></div>`) }
  function start(auto){ load().then(()=>{ if(ov) return; const seen=new Set();
    steps=STEPS.map(([k,s])=>[k,s,document.querySelector(s)]).filter(([k,,el])=>vis(el)&&!seen.has(k)&&seen.add(k));
    ov=document.createElement('div'); document.body.appendChild(ov);
    ov.addEventListener('click',e=>{ const b=e.target.closest('[data-a]'); if(!b){ if(e.target===ov&&ov.classList.contains('trc')) close('skip'); return } const a=b.dataset.a;
      if(a==='skip') close('skip'); else if(a==='close') close('done'); else if(a==='go'){ ev('start'); steps.length?show(0):end() } else if(a==='next') show(i+1); else if(a==='back') show(i-1); else if(a==='end') end() });
    onMove=()=>place(); window.addEventListener('resize',onMove); window.addEventListener('scroll',onMove,true);
    document.addEventListener('keydown',function kd(e){ if(!ov){ document.removeEventListener('keydown',kd); return } if(e.key==='Escape') close('skip') });
    welcome(); ev(auto?'shown':'replay') }).catch(()=>{}) }
  document.addEventListener('click',e=>{ const a=e.target.closest('[data-tour]'); if(!a) return; e.preventDefault(); const d=a.closest('details'); if(d) d.open=false; const sh=document.getElementById('msheet'); if(sh) sh.hidden=true; start(false) });
  if(location.hash==='#tour') setTimeout(()=>start(false),800);
  else if(!get('wi_tour')) setTimeout(()=>{ (window.requestIdleCallback||setTimeout)(()=>{ if(!get('wi_tour')&&!document.querySelector('.aip:not([hidden]),.nudge')) start(true) }) },2500);
})();

/* ---------- quick converter under every asset chart (owner 2026-11-23): amount ⇄ value, live price, reader's currencies ---------- */
(function(){ const box=document.querySelector('.qconv[data-a]'); if(!box) return; const W=window.WI||{}, FX=W.fx||{};
  const ia=box.querySelector('[data-q=a]'), ic=box.querySelector('[data-q=c]'), sel=box.querySelector('select'), h2=box.querySelector('h2'), aid=box.dataset.a;
  const BY=(window.WIX&&window.WIX.BYID)||{};
  const px=()=>{ const a=BY[aid]; return (a&&a.pr)||+box.dataset.p };
  const rate=()=>sel.value==='USD'?1:(FX[sel.value]||0);
  const fmt=v=>{ if(!isFinite(v)) return ''; const d=v>=1000?2:v>=1?4:Math.min(10,3-Math.floor(Math.log10(Math.max(v,1e-12)))+2); return String(+v.toFixed(d)) };
  let last='a';
  const fromA=()=>{ last='a'; const r=rate(); if(!r) return; ic.value=fmt((+ia.value||0)*px()*r) };
  const fromC=()=>{ last='c'; const r=rate(); if(!r) return; ia.value=fmt((+ic.value||0)/(px()*r)) };
  ia.addEventListener('input',fromA); ic.addEventListener('input',fromC);
  sel.addEventListener('change',()=>{ h2.textContent=(box.dataset.h||'').replace('{c}',sel.value); fromA(); ic.setAttribute('aria-label',sel.value) });
  document.addEventListener('wi:tick',()=>{ if(document.activeElement!==ic&&document.activeElement!==ia) (last==='a'?fromA:fromC)() });
  fromA();
})();

/* ---------- big crypto holders (/investors/): value = coins held × live price ---------- */
(function(){ const els=[...document.querySelectorAll('[data-hq]')]; if(!els.length) return; const BY=(window.WIX&&window.WIX.BYID)||{};
  const big=v=>v>=1e12?'$'+(v/1e12).toFixed(2)+'T':v>=1e9?'$'+(v/1e9).toFixed(2)+'B':v>=1e6?'$'+(v/1e6).toFixed(1)+'M':'$'+Math.round(v).toLocaleString('en-US');
  const run=()=>els.forEach(el=>{ const a=BY[el.dataset.hc]; if(a&&a.pr) el.textContent=big(+el.dataset.hq*a.pr) });
  run(); document.addEventListener('wi:tick',run);
})();

// country offer: swap the Telegram Wallet card for the visitor's country bonus (time zone → country, no request; owner 2026-11-26)
(function(){ let tz=''; try{ tz=Intl.DateTimeFormat().resolvedOptions().timeZone||'' }catch(e){}
  if(!tz) return; const today=new Date().toISOString().slice(0,10);
  document.querySelectorAll('a.offer[data-alt]').forEach(a=>{ let m; try{ m=Object.values(JSON.parse(a.dataset.alt)).find(x=>x.z.includes(tz)) }catch(e){ return }
    if(!m||(m.u&&today>m.u)) return; a.href=m.h; const b=a.querySelector('.oft b'), d=a.querySelector('.oft span'), n=a.querySelector('.oft small'), c=a.querySelector('.btn');
    if(b) b.textContent=m.t; if(d) d.textContent=m.d; if(n) n.textContent=m.note; if(c) c.textContent=m.cta; a.dataset.cc='1' }) })();
// 🎁 «Exclusive offers» popup + rotating partner strip (owner 2026-11-26). Data: /assets/bonus-<lang>.json (bonuses.json); country by time zone.
(function(){ const btn=document.getElementById('bonbtn'), st=document.getElementById('pstrip'), xo=document.querySelector('.xoffer'); if(!btn&&!st&&!xo) return;
  const l=(btn||st||xo).dataset.l; let D=null, P=null; let tz=''; try{ tz=Intl.DateTimeFormat().resolvedOptions().timeZone||'' }catch(e){}
  const E=s=>String(s==null?'':s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const num=n=>Number(n).toLocaleString(l==='en'?'en-US':l).replace(/,/g,' ');
  const load=()=>D?Promise.resolve(D):fetch('/assets/bonus-'+l+'.json').then(r=>r.json()).then(j=>(D=j));
  const mine=()=>D.c.find(c=>c.z.includes(tz));
  const AV=x=>x.g?`<span class="bav"><img src="${E(x.g)}" alt="" loading="lazy"></span>`:`<span class="bav" style="background:${E(x.c||'#3a4150')}">${E(x.a||(x.n||'?')[0])}</span>`;
  function open(){ load().then(d=>{ const s=d.s, my=mine(), hot=d.x.find(x=>x.hot)||d.x[0];
    if(!P){ P=document.createElement('div'); P.className='bpop'; P.hidden=true; P.setAttribute('role','dialog'); P.setAttribute('aria-label',s.title); document.body.appendChild(P);
      P.addEventListener('click',e=>{ if(e.target===P||e.target.closest('.x')) P.hidden=true }); document.addEventListener('keydown',e=>{ if(e.key==='Escape'&&P) P.hidden=true }) }
    const row=(n,t,h,m,av)=>`<div class="brow2">${av}<div class="bn"><b>${E(n)}</b><small>${m?`${E(s.upto)} <em class="big">${num(m)} USDT</em> · `:''}${E(t)}</small></div><a href="${E(h)}" target="_blank" rel="sponsored noopener">${E(s.open)} ›</a></div>`;
    P.innerHTML=`<div class="bpw"><div class="bph"><span style="font-size:26px">🎁</span><div><h2>${E(s.title)}</h2><p>${E(s.sub)}</p></div><button class="x" type="button" aria-label="×">×</button></div>
      <div class="bhot"><span class="gift" aria-hidden="true">🎁</span><div class="bhl">${AV(hot)}<b>${E(hot.n)}</b> <span class="bxrec">${E(s.rec)}</span></div><div class="big">${hot.m?E(s.upto)+' '+num(hot.m)+' USDT':E(hot.l)}</div><a class="btn" href="${E(hot.h)}" target="_blank" rel="sponsored noopener">${E(s.open)} ›</a></div>
      <div class="bsteps">${s.steps.map((x,i)=>`<span>${i+1}. ${E(x)}</span>`).join('')}</div>
      <h3>🪙 ${E(s.ex)}</h3>${d.x.filter(x=>x!==hot).map(x=>row(x.n,x.l,x.h,x.m,AV(x))).join('')}
      ${my&&my.i.length?`<h3>${my.f} ${E(s.local)}: ${E(my.n)}</h3>`+my.i.map(i=>row(i.n,i.t,i.h,0,AV(i))).join(''):''}
      <p class="bnote">${E(s.note)}</p><a class="ball" href="${E(d.u)}">${E(s.all)} →</a></div>`;
    P.hidden=false; const c=P.querySelector('.x'); c&&c.focus() }).catch(()=>{ location.href='/'+(l==='uk'?'':l+'/')+'bonuses/' }) }
  if(btn) btn.addEventListener('click',open);
  // «Exclusive offers» strip under posts and on asset pages: top 3 exchanges by «up to» + button that opens the popup
  document.querySelectorAll('.xoffer').forEach(el=>{ setTimeout(()=>{
    load().then(d=>{ const s=d.s; const top=d.x.filter(x=>x.m).slice(0,3);
      el.innerHTML=`<span class="xt">🎁 ${E(s.title)}</span>`+top.map(x=>`<a class="xi" href="${E(x.h.replace('from=pop','from=xoffer'))}" target="_blank" rel="sponsored noopener">${AV(x)}<span>${E(x.n)}<small>${E(s.upto)} ${num(x.m)} USDT</small></span></a>`).join('')+`<button class="btn" type="button">${E(s.all)} ›</button>`;
      el.querySelector('button').addEventListener('click',open); el.hidden=false }).catch(()=>{}) },1200) });
  if(st){ const go=()=>load().then(d=>{ const s=d.s, my=mine(); let list=d.x.map(x=>({h:x.h,t:s.strip.replace('{n}',x.n).replace('{l}',x.l)}));
      if(my) list=my.i.slice(0,2).map(i=>({h:i.h,t:i.n+': '+i.t})).concat(list);
      if(!list.length) return; let k=0; st.innerHTML=`<span class="pl">${E(s.partner)}</span><button class="pg" type="button" aria-label="${E(s.title)}">🎁</button><a target="_blank" rel="sponsored noopener"></a>`; st.querySelector('.pg').addEventListener('click',open); const a=st.querySelector('a');
      const show=()=>{ const it=list[k%list.length]; a.href=it.h; a.innerHTML=`${E(it.t)} <i>→</i>`; k++ }; show(); st.hidden=false;
      setInterval(()=>{ if(document.hidden) return; a.classList.add('fade'); setTimeout(()=>{ show(); a.classList.remove('fade') },400) },6000) }).catch(()=>{});
    ('requestIdleCallback' in window)?requestIdleCallback(go,{timeout:2500}):setTimeout(go,1200) }
})();

// «{{offer}}» box: honest countdown to the promo's end date (owner 2026-11-26)
document.querySelectorAll('.obcnt[data-until]').forEach(el=>{ const t=new Date(el.dataset.until+'T23:59:59+02:00')-Date.now(); if(t<0){ el.closest('.offerbig').hidden=true; return }
  const d=Math.ceil(t/864e5); el.querySelector('b').textContent=d+' '+el.dataset.w });

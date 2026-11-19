/* WhatIfStack — front-end. Data: window.WI (index of all assets, from index.js),
   page config: window.PAGE, referral links: window.REF / window.REF_DEFAULT (ref.js).
   Price series are loaded on demand from /assets/p/<id>.json. */
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
const url = id => { const a=BYID[id]; return (PAGE.full||(a&&a.o<PAGE.topn)) ? `${PAGE.prefix}/${id}/` : `${BASE}/en/${id}/` };
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
function refFor(a){ const RL=(window.REF_LANG||{})[a.c]; const r=REF[a.i]||(RL&&RL.langs.includes(lang)?RL:null)||REF_DEFAULT[a.c]; return r&&r.url?Object.assign({},r,{url:goUrl(r.url)}):null }
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
  const TABS=['all','crypto','stock','etf','metal','cmd','lead','lag'];
  $('#tabs').innerHTML=TABS.map(t=>`<button data-t="${t}" class="${t===tab?'on':''}">${T[t]}</button>`).join('')+(PAGE.wa?`<a class="tablink" href="${PAGE.wau}">🌍 ${esc(PAGE.wa)}</a>`:'');
  $$('#tabs button').forEach(b=>b.onclick=()=>{tab=b.dataset.t; $$('#tabs button').forEach(x=>x.classList.toggle('on',x===b));
    if(tab==='lead'){sortK='r5';sortDir=-1} else if(tab==='lag'){sortK='r5';sortDir=1} else if(sortK==='r5'&&(sortDir)){sortK='o';sortDir=1}
    shown=PAGE.home?20:100; pg=0; draw()});
  const f=$('#flt'); f.placeholder=T.filter; f.setAttribute('aria-label',T.filter); f.oninput=()=>{q=f.value.trim().toLowerCase(); shown=PAGE.home?20:100; pg=0; draw()};
  try{ const sq=new URLSearchParams(location.search).get('q'); if(sq){ f.value=sq; f.oninput() } }catch(e){}
  const COLS=[['n','#','l n hide-sm'],['name',T.name,'l'],['buy','','hide-sm'],['pr',T.price,''],['ch',T.chg,''],['r1',T.d1,'hide-sm'],['r3',T.d3,'hide-sm'],['r5',T.d5,''],['sp',T.spark,'hide-sm'],['go','','hide-sm']];
  function draw(){
    let rows=IDX.filter(a=>{
      if(tab==='crypto'||tab==='stock'||tab==='etf'||tab==='metal'||tab==='cmd'){ if(a.c!==tab) return false }
      if((tab==='lead'||tab==='lag')&&a.r5==null) return false;
      return !q||a.t.toLowerCase().includes(q)||nm(a).toLowerCase().includes(q) });
    const k=sortK==='n'?'o':(sortK==='o'&&PAGE.home&&tab==='all'&&!q?'h':sortK);
    rows.sort((x,y)=>{ const vx=k==='name'?nm(x):x[k], vy=k==='name'?nm(y):y[k];
      if(vx==null&&vy==null) return x.o-y.o; if(vx==null) return 1; if(vy==null) return -1;
      return (typeof vx==='string'?vx.localeCompare(vy):vx-vy)*sortDir });
    const total=rows.length, paged=true, np=Math.max(1,Math.ceil(total/PER)); if(pg>=np) pg=np-1; const off=paged?pg*PER:0;
    rows=paged?rows.slice(off,off+PER):rows.slice(0,shown);
    const split=!!$('#mt2'), top=split?rows.slice(0,10):rows, rest=split?rows.slice(10):[];
    const head='<tr>'+COLS.map(([c,l,cl])=>{ const s=(c===sortK||(c==='n'&&sortK==='o'));
      const sortable=!['buy','sp','go'].includes(c);
      return `<th class="${cl}${s?' sorted':''}" ${sortable?`data-k="${c}"`:''}>${l}${sortable&&l?`<span class="ar">${s?(sortDir>0?'↑':'↓'):'↕'}</span>`:''}</th>`}).join('')+'</tr>';
    $('#mthead').innerHTML=head; if(split) $('#mthead2').innerHTML=head;
    $$('#mthead th[data-k],#mthead2 th[data-k]').forEach(th=>th.onclick=()=>{ let kk=th.dataset.k; if(kk==='n') kk='o';
      if(sortK===kk) sortDir=-sortDir; else {sortK=kk; sortDir=(kk==='name'||kk==='o')?1:-1} pg=0; draw() });
    const tr=(a,i)=>`<tr>
      <td class="l n hide-sm">${off+i+1}</td>
      <td class="l"><button class="star" data-s="${a.i}" aria-label="☆">☆</button><a class="asset" href="${url(a.i)}">${icon(a)}<span><span class="nm">${esc(nm(a))}</span><span class="tk">${esc(a.t)}${lang!=='en'&&url(a.i).startsWith(BASE+'/en/')?'<i class="enb" title="English">EN</i>':''}</span></span></a></td>
      <td class="hide-sm">${buyBtn(a)}</td>
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
    if(paged){ const pb=(n,l,dis,on)=>`<button type="button" class="pgb${on?' on':''}" data-pg="${n}"${dis?' disabled':''}>${l}</button>`;
      let h=''; if(np>1){ h+=pb(pg-1,'‹',pg===0); const seen=new Set(); [0,1,2,pg-1,pg,pg+1,np-1].filter(n=>n>=0&&n<np).sort((a,b)=>a-b).forEach(n=>{ if(seen.has(n)) return; if(seen.size&&!seen.has(n-1)) h+='<span class="pgd">…</span>'; seen.add(n); h+=pb(n,n+1,false,n===pg) }); h+=pb(pg+1,'›',pg===np-1) }
      $('#mtmore').innerHTML=np>1?`<div class="pager">${h}<span class="muted pgi">${off+1}–${Math.min(off+PER,total)} / ${total}</span></div>`:'';
      $$('#mtmore .pgb').forEach(b=>b.onclick=()=>{ pg=+b.dataset.pg; draw(); $('#mthead').closest('.tw').scrollIntoView({block:'start',behavior:'smooth'}) }) }
    else { $('#mtmore').innerHTML=total>shown?`<button class="more">${T.more} (${fmt(T.shown,{a:shown,b:total})})</button>`:'';
      const mb=$('#mtmore button'); if(mb) mb.onclick=()=>{shown+=STEP;draw()}; }
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
  const nf=v=>{ try{ return new Intl.NumberFormat(T.intl||'en',{style:'currency',currency:C.code,maximumFractionDigits:Math.abs(v)>=100?0:2}).format(v) }catch(e){ return Math.round(v)+' '+C.code } };
  const pf=()=>{ let tv=0,tc=0,d=0; for(const [id,g] of Object.entries(hold)){ const a=BYID[id], v=g.qty*a.pr; tv+=v; tc+=g.cost; d+=v*(a.ch||0)/(1+(a.ch||0)) }
    if(!tv) return ''; const dp=tv-d?d/(tv-d):0, r=tc?tv/tc-1:0;
    return `<a class="card mypf" href="${C.me}"><span class="muted">${esc(C.pf)}</span><b class="v">${nf(tv*C.rate)}</b>
      <span class="${cls(dp)}">${fmtPct(dp)} ${esc(C.today)} · ${d<0?'−':'+'}${nf(Math.abs(d)*C.rate)}</span><span class="muted">${esc(T.invested||'')}: ${nf(tc*C.rate)} · <span class="${cls(r)}">${fmtPct(r)}</span></span></a>` };
  const top=ids.slice(0,8).map(i=>{ const a=BYID[i]; return `<a class="mrow" href="${url(i)}">${icon(a)}<span class="mn"><b>${esc(a.t)}</b><span>${esc(nm(a))}</span></span>
      <span class="mp" data-p="${i}">${fmtPrice(a.pr)}</span><span class="mc ${cls(a.ch)}" data-c="${i}">${fmtPct(a.ch)}</span></a>` }).join('');
  box.innerHTML=`<div class="myhh"><h2>${esc(C.h)}</h2><a class="calc" href="${C.me}">${esc(C.open)} →</a></div>
    <div class="mygrid"><div class="mycol"><div id="mypf">${pf()}</div></div><div class="card wd"><div class="wt">★ ${esc(C.watch)}</div>${top}</div><div class="card wd" id="mynews" hidden><div class="wt">📰 ${esc(C.news)}</div><div class="nlist own"></div></div></div>`;
  if(!Object.keys(hold).length) box.querySelector('#mypf').remove();
  const br=$('#brief'); if(br) box.querySelector('.mycol').appendChild(br);   // «Market in 60 seconds» sits under the portfolio balance
  box.hidden=false;
  let t; document.addEventListener('wi:tick',()=>{ clearTimeout(t); t=setTimeout(()=>{ const el=$('#mypf'); if(el) el.innerHTML=pf() },1200) });
  fetch(C.nf+'?v='+WI.v).then(r=>r.json()).then(L=>{ const w=new Set(ids), f=L.filter(n=>(n.a||[]).some(x=>w.has(x))).slice(0,4); if(!f.length) return;
    const n=$('#mynews'); n.querySelector('.nlist').innerHTML=f.map(x=>`<a class="nrow" href="${x.u}"><b>${esc(x.t)}</b><span class="muted"><time data-t="${esc(x.d)}">${esc(x.d)}</time> · ${esc(x.a.map(i=>BYID[i]?BYID[i].t:i).slice(0,3).join(', '))}</span></a>`).join(''); n.hidden=false }).catch(()=>{});
})();

/* ---------- live quotes for US stocks, ETFs, gold and other futures (/api/quote, Yahoo, 60 s CDN cache) ---------- */
(function(){
  const ids=()=>[...new Set($$('[data-p],[data-c]').map(el=>el.dataset.p||el.dataset.c))].filter(i=>BYID[i]&&BYID[i].y).slice(0,25);
  let busy=false;
  async function run(){ if(busy||document.hidden) return; const L=ids(); if(!L.length) return; busy=true;
    try{ const r=await fetch('/api/quote?s='+encodeURIComponent(L.map(i=>BYID[i].y).join(','))); if(!r.ok) return; const Q=await r.json();
      L.forEach(i=>{ const a=BYID[i], q=Q[a.y]; if(!q||!(q.p>0)) return; const old=a.pr; a.pr=q.p; if(q.c!=null) a.ch=q.c;
        $$(`[data-p="${i}"]`).forEach(el=>{ el.textContent=fmtPrice(q.p); if(old&&Math.abs(q.p/old-1)>1e-6){ el.classList.remove('flash-up','flash-dn'); void el.offsetWidth; el.classList.add(q.p>old?'flash-up':'flash-dn') } });
        if(q.c!=null) $$(`[data-c="${i}"]`).forEach(el=>{ el.textContent=fmtPct(q.c); el.classList.remove('good','bad'); el.classList.add(cls(q.c)) });
        document.dispatchEvent(new CustomEvent('wi:tick',{detail:a})) });
    }catch(e){} finally{ busy=false } }
  setTimeout(run,600); setInterval(run,60000); document.addEventListener('visibilitychange',()=>{ if(!document.hidden) run() });
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
  /* portfolio (holdings): buy, buy more, sell part, history, backup */
  const HL={ get(){ try{ return JSON.parse(localStorage.getItem('wi_hold')||'[]') }catch(e){ return [] } }, set(v){ try{ localStorage.setItem('wi_hold',JSON.stringify(v)) }catch(e){} } };
  const PAL=['#1a6dff','#f59e0b','#14a44d','#e5484d','#8b5cf6','#0ea5e9','#ec4899','#64748b','#84cc16','#f97316'];
  $('#hmode').onchange=()=>{ $('#hunit').textContent=$('#hmode').value==='qty'?'':(new Intl.NumberFormat(T.intl||'en',{style:'currency',currency:C.code}).formatToParts(1).find(p=>p.type==='currency')||{}).value||C.code };
  $('#hsave').onclick=async()=>{ const id=findId($('#ha').value), v=+$('#hamt').value, d=($('#hdate').value||END).slice(0,7);
    if(!id){ $('#ha').focus(); $('#ha').classList.add('bad'); return } if(!(v>0)) return;
    const a=BYID[id]; let px=a.pr;
    if(d<END){ try{ const P=await load(id), k=ym2i(d)-ym2i(P.start); if(k>=0&&k<P.p.length) px=P.p[k] }catch(e){} }
    const qty=$('#hmode').value==='qty'?v:(v/C.rate)/px, cost=qty*px;
    const h=HL.get(); h.push({id,qty,cost,d,px}); HL.set(h); $('#ha').value=''; $('#ha').classList.remove('bad'); drawHold() };
  const open=new Set();
  function drawHold(){
    const raw=HL.get(), agg={}; let realized=0;
    raw.forEach((x,k)=>{ if(!BYID[x.id]) return; const g=agg[x.id]||(agg[x.id]={id:x.id,qty:0,cost:0,tx:[]}); g.qty+=x.qty; g.cost+=x.cost; g.tx.push(Object.assign({k},x)); realized+=x.r||0 });
    const L=Object.values(agg).filter(g=>g.qty>1e-12).map(g=>{ const a=BYID[g.id]; return Object.assign(g,{a,val:g.qty*a.pr}) }).sort((x,y)=>y.val-x.val);
    if(!L.length){ $('#hold').innerHTML=`<p class="muted">${esc(t.hempty)}</p>`; $('#htot').innerHTML=''; $('#abar').innerHTML=''; return }
    const tv=L.reduce((s,g)=>s+g.val,0), tc=L.reduce((s,g)=>s+g.cost,0), d24=L.reduce((s,g)=>s+g.val*(g.a.ch||0)/(1+(g.a.ch||0)),0), roi=tc?tv/tc-1:0;
    $('#htot').innerHTML=`<div class="card"><div class="k">${esc(t.total)}</div><div class="v">${nf(tv*C.rate)}</div><div class="s">${esc(T.invested||'')}: ${nf(tc*C.rate)}</div></div>
      <div class="card"><div class="k">${esc(t.profit)}</div><div class="v ${cls(roi)}">${fmtPct(roi)}</div><div class="s ${cls(roi)}">${nf((tv-tc)*C.rate)}</div></div>
      <div class="card"><div class="k">${esc(T.chg||'24h')}</div><div class="v ${cls(d24)}">${fmtPct(tv-d24?d24/(tv-d24):0)}</div><div class="s ${cls(d24)}">${nf(d24*C.rate)}</div></div>`
      +(realized?`<div class="card"><div class="k">${esc(t.realized)}</div><div class="v ${cls(realized)}">${nf(realized*C.rate)}</div></div>`:'');
    $('#abar').innerHTML=L.map((g,i)=>`<i style="width:${(g.val/tv*100).toFixed(2)}%;background:${PAL[i%PAL.length]}" title="${esc(g.a.t)} ${(g.val/tv*100).toFixed(1)}%"></i>`).join('');
    const q=v=>v.toLocaleString(T.intl||'en',{maximumSignificantDigits:6});
    $('#hold').innerHTML=`<div class="tw"><table class="mt pft"><thead><tr><th class="l">${esc(T.name||'')}</th><th class="hide-sm">${esc(t.qty)}</th><th class="hide-sm">${esc(t.avg)}</th><th>${esc(T.value||'')}</th><th>${esc(t.profit)}</th><th class="hide-sm">${esc(T.chg||'')}</th><th class="hide-sm">${esc(t.share)}</th><th></th></tr></thead><tbody>`+
      L.map((g,i)=>{ const r=g.cost?g.val/g.cost-1:0, op=open.has(g.id);
        return `<tr><td class="l"><i class="dot" style="background:${PAL[i%PAL.length]}"></i><a class="asset" href="${url(g.id)}">${icon(g.a)}<span><span class="nm">${esc(nm(g.a))}</span><span class="tk">${esc(g.a.t)}</span></span></a></td>
        <td class="num hide-sm">${q(g.qty)}</td><td class="num hide-sm">${fmtPrice(g.cost/g.qty)}</td><td class="num"><b>${nf(g.val*C.rate)}</b></td>
        <td class="num ${cls(r)}">${fmtPct(r)}<br><small>${nf((g.val-g.cost)*C.rate)}</small></td><td class="num hide-sm ${cls(g.a.ch)}">${fmtPct(g.a.ch)}</td><td class="num hide-sm">${(g.val/tv*100).toFixed(1)}%</td>
        <td class="pfact"><button class="pb" data-buy="${g.id}" title="${esc(t.buy)}">＋</button><button class="pb" data-sell="${g.id}" title="${esc(t.sell)}">−</button><button class="pb" data-hist="${g.id}" title="${esc(t.txs)}">${op?'▴':'▾'}</button></td></tr>`
        +`<tr class="pfx" data-x="${g.id}" hidden><td colspan="8"><div class="pfsell"><input type="number" min="0" step="any" placeholder="${esc(t.amount)} (${esc(C.code)})"><button class="btn" data-go="${g.id}">${esc(t.sell)}</button><button class="btn ghost" data-all="${g.id}">${esc(t.sell_all)}</button></div></td></tr>`
        +(op?`<tr class="pfh"><td colspan="8">`+g.tx.map(x=>`<div class="tx"><span class="${x.qty<0?'bad':'good'}">${esc(x.qty<0?t.sold:t.bought)}</span><span>${esc(x.d||'')}</span><span>${q(Math.abs(x.qty))} ${esc(g.a.t)}</span><span>${nf(Math.abs(x.qty)*(x.px||Math.abs(x.cost/x.qty))*C.rate)}</span>${x.r?`<span class="${cls(x.r)}">${nf(x.r*C.rate)}</span>`:'<span></span>'}<button class="toggle" data-tx="${x.k}" aria-label="${esc(t.remove)}">✕</button></div>`).join('')+`<div class="tx"><span></span><span></span><span></span><span></span><span></span><button class="toggle" data-hdel="${g.id}" title="${esc(t.remove)}">🗑</button></div></td></tr>`:'') }).join('')+'</tbody></table></div>';
    const sell=(id,usd,all)=>{ const g=agg[id], a=BYID[id], avg=g.cost/g.qty; let qq=all?g.qty:Math.min(g.qty,usd/a.pr); if(!(qq>0)) return;
      const h=HL.get(); h.push({id,qty:-qq,cost:-avg*qq,d:END,px:a.pr,r:(a.pr-avg)*qq}); HL.set(h); drawHold() };
    $$('#hold [data-buy]').forEach(b=>b.onclick=()=>{ const a=BYID[b.dataset.buy]; $('#ha').value=`${nm(a)} (${a.t})`; $('#hmode').value='sum'; $('#hdate').value=END; $('#holdform').scrollIntoView({behavior:'smooth',block:'center'}); setTimeout(()=>$('#hamt').focus(),400) });
    $$('#hold [data-sell]').forEach(b=>b.onclick=()=>{ const r=$(`#hold tr.pfx[data-x="${b.dataset.sell}"]`); r.hidden=!r.hidden; if(!r.hidden) r.querySelector('input').focus() });
    $$('#hold [data-go]').forEach(b=>b.onclick=()=>{ const v=+b.parentNode.querySelector('input').value; if(v>0) sell(b.dataset.go,v/C.rate,false) });
    $$('#hold [data-all]').forEach(b=>b.onclick=()=>sell(b.dataset.all,0,true));
    $$('#hold [data-hist]').forEach(b=>b.onclick=()=>{ const id=b.dataset.hist; open.has(id)?open.delete(id):open.add(id); drawHold() });
    $$('#hold [data-tx]').forEach(b=>b.onclick=()=>{ const h=HL.get(); h.splice(+b.dataset.tx,1); HL.set(h); drawHold() });
    $$('#hold [data-hdel]').forEach(b=>b.onclick=()=>{ HL.set(HL.get().filter(x=>x.id!==b.dataset.hdel)); drawHold() }) }
  // backup / restore (data lives only in this browser)
  $('#pfexp')&&($('#pfexp').onclick=()=>{ const data={v:1,hold:HL.get(),plans:PL.get(),watch:WL.get(),bonds:(()=>{ try{ return JSON.parse(localStorage.getItem('wi_bonds')||'[]') }catch(e){ return [] } })()}; const a=document.createElement('a');
    a.href=URL.createObjectURL(new Blob([JSON.stringify(data,null,1)],{type:'application/json'})); a.download='whatifstack-portfolio.json'; a.click() });
  $('#pfimp')&&($('#pfimp').onchange=e=>{ const f=e.target.files[0]; if(!f) return; f.text().then(s=>{ const d=JSON.parse(s);
    if(Array.isArray(d.hold)) HL.set(d.hold); if(Array.isArray(d.plans)) PL.set(d.plans); if(Array.isArray(d.watch)) WL.set(d.watch); if(Array.isArray(d.bonds)){ try{ localStorage.setItem('wi_bonds',JSON.stringify(d.bonds)) }catch(e){} document.dispatchEvent(new Event('wi:bonds')) } drawHold(); drawPlans(); drawWatch() }).catch(()=>{}) });
  let ht; document.addEventListener('wi:tick',()=>{ clearTimeout(ht); ht=setTimeout(drawHold,1500) });
  document.addEventListener('wi:watch',drawWatch); drawWatch(); drawPlans(); drawHold();
})();
/* ---------- long texts (stock analyses): show the first screen, «Show more» opens the rest ---------- */
$$('.clamp').forEach(el=>{ if(el.scrollHeight<760) return; el.classList.add('clamped');
  const b=document.createElement('button'); b.type='button'; b.className='btn ghost clampbtn'; b.textContent=(el.dataset.more||'Show more')+' ▾';
  b.onclick=()=>{ const open=el.classList.toggle('clamped')===false; b.textContent=open?'▴':(el.dataset.more||'Show more')+' ▾'; if(!open) el.scrollIntoView({block:'start',behavior:'smooth'}) };
  el.after(b) });
/* ---------- weekly e-mail report signup (api/subscribe.js) ---------- */
$$('form.nlf').forEach(f=>f.onsubmit=async e=>{ e.preventDefault(); const em=$('input[type=email]',f).value.trim(), b=$('button',f), box=f.closest('.nlbox'), note=$('.nln',box);
  b.disabled=true;
  try{ const r=await fetch('/api/subscribe',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({em,l:lang,src:(f.dataset.src||'')+' '+location.pathname,hp:f.hp.value})});
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
    if(!px) return; const qty=(v/C.rate)/px; let h=[]; try{ h=JSON.parse(localStorage.getItem('wi_hold')||'[]') }catch(e){}
    h.push({id,qty,cost:qty*px,d,px}); try{ localStorage.setItem('wi_hold',JSON.stringify(h)) }catch(e){}
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
  const btn=document.createElement('button'); btn.type='button'; btn.className='aibtn'; btn.setAttribute('aria-haspopup','dialog');
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
      try{ const r=await fetch('/api/feedback',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({t,em,l:lang,p:location.pathname,w:Date.now()-fbT})});
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

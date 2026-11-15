// whatif.invest calculator. Data comes from data.js (window.WHATIF_DATA), page config from window.PAGE.
const DATA = window.WHATIF_DATA, PRICES = DATA.prices, PAGE = window.PAGE || {};

// Partner links live in ref.js (window.REF, window.REF_DEFAULT).
const REF = window.REF || {};
const PALETTE=['#f7931a','#76b900','#e6c15a','#b8c2cc','#8f7bff','#ff5a5f','#3fa9f5','#22d3c5','#ff8fd1','#a3e635'];
const UNIT={stock:{uk:'акцій',en:'shares'},etf:{uk:'паїв',en:'shares'},metal:{uk:'унцій',en:'oz'}};
const ASSETS = DATA.assets.filter(a=>PRICES[a.id]).map(a=>({...a,unit:UNIT[a.cat]||{uk:a.tk,en:a.tk}}));
const AMAP=Object.fromEntries(ASSETS.map(a=>[a.id,a]));
const REF_DEFAULT = window.REF_DEFAULT || {};

const T = {
  uk:{
    h1:'Що якби я щодня вкладав <em>$10</em>?',
    sub:'Обери активи й дату старту — і подивись, скільки б у тебе було зараз. Реальні історичні ціни: 48 активів — крипта, акції, ETF, золото і срібло.',
    amount:'Сума', freq:'Як часто', daily:'Щодня', weekly:'Щотижня', monthly:'Щомісяця',
    since:'Починаючи з', assets:'Активи на графіку (до 10)', chartTitle:'Вартість портфеля в часі',
    log:'Лог. шкала', invested:'Вкладено', best:'Найкращий результат', worst:'Найгірший результат',
    asset:'Актив', value:'Зараз', profit:'Прибуток', got:'Накопичив', buy:'Купити', aff:'партнерське посилання',
    investedLine:'Вкладено', copy:'Копіювати', copied:'Скопійовано ✓',
    per:{d:'щодня',w:'щотижня',m:'щомісяця'},
    share:(a,amt,per,since,val,pct)=>`Якби я вкладав $${amt} ${per} у ${a} з ${since}, зараз у мене було б ${val} (${pct}).`,
    note:`<b>Як рахуємо:</b> для кожного місяця беремо ціну закриття і купуємо на суму всіх внесків за цей місяць (щоденні внески = сума × кількість днів). Без комісій, податків і дивідендів. Ціни: Yahoo Finance та відкриті датасети, з урахуванням сплітів; золото і срібло — ф'ючерси. Дані оновлено: ${DATA.updated}. <b>Це не інвестиційна порада.</b> Минулі результати не гарантують майбутніх.`,
    cats:{all:'Усі',crypto:'Крипта',stock:'Акції',etf:'ETF',metal:'Метали'}, nothing:'Нічого не знайдено',
    lbTitle:s=>`Рейтинг: найкращі активи для DCA з ${s}`, lbSub:n=>`${n} активів · натисни, щоб додати на графік`,
    months:['січ','лют','бер','кві','тра','чер','лип','сер','вер','жов','лис','гру']
  },
  en:{
    h1:'What if I invested <em>$10</em> every day?',
    sub:'Pick assets and a start date to see what you would have today. Real historical prices for 48 assets: crypto, stocks, ETFs, gold and silver.',
    amount:'Amount', freq:'How often', daily:'Daily', weekly:'Weekly', monthly:'Monthly',
    since:'Starting from', assets:'Assets on the chart (up to 10)', chartTitle:'Portfolio value over time',
    log:'Log scale', invested:'Invested', best:'Best result', worst:'Worst result',
    asset:'Asset', value:'Now', profit:'Profit', got:'Accumulated', buy:'Buy', aff:'affiliate link',
    investedLine:'Invested', copy:'Copy', copied:'Copied ✓',
    per:{d:'every day',w:'every week',m:'every month'},
    share:(a,amt,per,since,val,pct)=>`If I had invested $${amt} ${per} in ${a} since ${since}, I would have ${val} today (${pct}).`,
    note:`<b>Method:</b> for each month we take the closing price and buy with all contributions for that month (daily = amount × days in month). No fees, taxes or dividends. Prices: Yahoo Finance and open datasets, split-adjusted; gold and silver are futures prices. Data updated: ${DATA.updated}. <b>Not investment advice.</b> Past performance does not guarantee future results.`,
    cats:{all:'All',crypto:'Crypto',stock:'Stocks',etf:'ETFs',metal:'Metals'}, nothing:'Nothing found',
    lbTitle:s=>`Leaderboard: best assets to DCA since ${s}`, lbSub:n=>`${n} assets · tap to add to the chart`,
    months:['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
  }
};

let lang=PAGE.lang||'uk', freq='d', logScale=false;
let selected=(PAGE.sel||['btc','nvda','gold','silver','atom']).filter(id=>PRICES[id]); const colorOf={}; let cat='all';
const MAXSEL=10;
function assignColors(){const used=new Set(selected.map(id=>colorOf[id]).filter(Boolean));selected.forEach(id=>{if(!colorOf[id]){colorOf[id]=PALETTE.find(c=>!used.has(c))||'#999';used.add(colorOf[id])}});Object.keys(colorOf).forEach(id=>{if(!selected.includes(id))delete colorOf[id]})}
function toggleAsset(id){const k=selected.indexOf(id);if(k>=0){if(selected.length>1)selected.splice(k,1)}else{if(selected.length>=MAXSEL)selected.shift();selected.push(id)}assignColors();buildChips();render()}
const END=DATA.updated.slice(0,7), END_DAY=+DATA.updated.slice(8,10);

const $=s=>document.querySelector(s);
const ym2i=s=>{const [y,m]=s.split('-').map(Number);return y*12+m-1};
const i2ym=i=>`${Math.floor(i/12)}-${String(i%12+1).padStart(2,'0')}`;
const nm=a=>typeof a.name==='string'?a.name:a.name[lang];
const fmt$=v=>{const a=Math.abs(v);const s=a>=1e6?(a/1e6).toFixed(2)+'M':a>=1e4?Math.round(a).toLocaleString('en-US'):a.toLocaleString('en-US',{maximumFractionDigits:2});return (v<0?'−$':'$')+s};
const fmtPct=p=>(p>=0?'+':'−')+Math.abs(p*100).toLocaleString('en-US',{maximumFractionDigits:p>9.99?0:1})+'%';
const monthLabel=s=>{const [y,m]=s.split('-').map(Number);return `${T[lang].months[m-1]} ${y}`};
const daysIn=(y,m)=>new Date(y,m,0).getDate();

function perMonth(i){
  const y=Math.floor(i/12), m=i%12+1;
  let days=daysIn(y,m); if(i2ym(i)===END) days=END_DAY;
  return freq==='d'?days:freq==='w'?days/7:(i2ym(i)===END?0:1);
}

function simulate(id,startI,amt){
  const P=PRICES[id], s0=ym2i(P.start), e=ym2i(P.end);
  const from=Math.max(startI,s0);
  let units=0,inv=0; const pts=[];
  for(let i=from;i<=e;i++){
    const price=P.p[i-s0], c=amt*perMonth(i);
    units+=c/price; inv+=c;
    pts.push({i,inv,val:units*price});
  }
  return {id,units,inv,val:units*P.p[e-s0],pts,from};
}

function buildSince(){
  const sel=$('#since'), prev=sel.value||PAGE.since||'2018-01';
  sel.innerHTML='';
  for(let i=ym2i(END)-1;i>=ym2i('2000-01');i--){
    if(i%12!==0 && i%6!==0 && i<ym2i(END)-24) continue;
    const o=document.createElement('option');o.value=i2ym(i);o.textContent=monthLabel(i2ym(i));sel.appendChild(o);
  }
  sel.value=[...sel.options].some(o=>o.value===prev)?prev:sel.options[sel.options.length-1].value;
}

function buildChips(){
  const box=$('#assets');box.innerHTML='';
  selected.forEach(id=>{const a=AMAP[id];
    const b=document.createElement('button');b.className='chip on';b.style.setProperty('--c',colorOf[id]);
    b.innerHTML=`<i></i>${nm(a)} <span style="opacity:.55">${a.tk}</span><span class="x">×</span>`;
    b.onclick=()=>toggleAsset(id);box.appendChild(b)});
  buildPool();
}
function buildPool(){
  const q=($('#q').value||'').trim().toLowerCase(), t=T[lang];
  $('#cats').innerHTML=['all','crypto','stock','etf','metal'].map(c=>`<button data-c="${c}" class="${c===cat?'on':''}">${t.cats[c]}</button>`).join('');
  $('#cats').querySelectorAll('button').forEach(b=>b.onclick=()=>{cat=b.dataset.c;buildPool()});
  const list=ASSETS.filter(a=>!selected.includes(a.id)&&(cat==='all'||a.cat===cat)&&(!q||(nm(a)+' '+a.tk+' '+(a.name.en||'')).toLowerCase().includes(q)));
  $('#pool').innerHTML=list.length?list.map(a=>`<button data-id="${a.id}"><b>+</b>${nm(a)} <span style="opacity:.6">${a.tk}</span></button>`).join(''):`<div class="empty">${t.nothing}</div>`;
  $('#pool').querySelectorAll('button').forEach(b=>b.onclick=()=>toggleAsset(b.dataset.id));
}

function applyText(){
  document.documentElement.lang=lang;
  $('#q').placeholder=lang==='uk'?'Пошук: Apple, ETH, золото…':'Search: Apple, ETH, gold…';
  document.querySelectorAll('[data-t]').forEach(el=>{el.innerHTML=T[lang][el.dataset.t]});
  const amt=$('#amt').value||10;
  if(PAGE.staticH1) return;
  $('h1').innerHTML=T[lang].h1.replace('$10','$'+amt);
  if(freq!=='d') $('h1').innerHTML=lang==='uk'
    ? `Що якби я ${T.uk.per[freq]} вкладав <em>$${amt}</em>?`
    : `What if I invested <em>$${amt}</em> ${T.en.per[freq]}?`;
}

function render(){
  applyText();
  const amt=Math.max(1,+$('#amt').value||10);
  const startI=ym2i($('#since').value);
  const res=selected.map(id=>({a:{...AMAP[id],c:colorOf[id]},...simulate(id,startI,amt)}))
    .sort((x,y)=>(y.val/y.inv)-(x.val/x.inv));
  const t=T[lang];

  // hero
  const best=res[0], worst=res[res.length-1];
  const full=res.filter(r=>r.from===startI);
  const sameStart=full.length>0;
  const invShown=sameStart?fmt$(full[0].inv):fmt$(Math.max(...res.map(r=>r.inv)));
  const h=(k,v,s,cls='')=>`<div class="card stat"><div class="k">${k}</div><div class="v ${cls}">${v}</div><div class="s">${s}</div></div>`;
  $('#hero').innerHTML=
    h(t.invested,invShown,sameStart?`${monthLabel(i2ym(startI))} → ${monthLabel(END)}`:(lang==='uk'?'різні дати старту':'different start dates'))+
    h(t.best+': '+nm(best.a),fmt$(best.val),fmtPct(best.val/best.inv-1),best.val>=best.inv?'good':'bad')+
    (res.length>1?h(t.worst+': '+nm(worst.a),fmt$(worst.val),fmtPct(worst.val/worst.inv-1),worst.val>=worst.inv?'good':'bad'):h('—','',''));

  // table
  $('#tbl').innerHTML=`<tr><th>${t.asset}</th><th class="hide-sm">${t.invested}</th><th>${t.value}</th><th>${t.profit}</th><th class="hide-sm">${t.got}</th><th class="hide-sm"></th></tr>`+
    res.map(r=>{
      const p=r.val-r.inv, cls=p>=0?'good':'bad', ref=REF[r.id]||REF_DEFAULT[r.a.cat];
      const cta=ref&&ref.url?`<a class="cta" href="${ref.url}" rel="sponsored noopener" target="_blank">${t.buy} ${r.a.tk}</a><span class="aff">${ref.where} · ${t.aff}</span>`:'';
      const late=r.from>startI?`<div style="font:500 11px Inter;color:var(--muted)">${lang==='uk'?'з':'from'} ${monthLabel(i2ym(r.from))}</div>`:'';
      return `<tr><td class="a" style="--c:${r.a.c}"><i></i>${nm(r.a)}${late}${cta?`<div class="show-sm">${cta}</div>`:''}</td><td class="hide-sm">${fmt$(r.inv)}</td><td>${fmt$(r.val)}</td><td class="${cls}">${fmt$(p)}<br><span style="font-size:11px">${fmtPct(r.val/r.inv-1)}</span></td><td class="hide-sm">${r.units.toLocaleString('en-US',{maximumFractionDigits:r.a.dp})} ${r.a.unit[lang]}</td><td class="hide-sm">${cta}</td></tr>`;
    }).join('');

  $('#shareText').textContent=t.share(nm(best.a),amt,t.per[freq],monthLabel(i2ym(best.from)),fmt$(best.val),fmtPct(best.val/best.inv-1));
  drawChart(res,startI);
  // leaderboard: every asset that has data from the chosen start
  const lb=ASSETS.filter(a=>ym2i(PRICES[a.id].start)<=startI).map(a=>{const s=simulate(a.id,startI,amt);return {a,roi:s.val/s.inv-1}}).sort((x,y)=>y.roi-x.roi);
  $('#lbTitle').textContent=t.lbTitle(monthLabel(i2ym(startI)));
  $('#lbSub').textContent=t.lbSub(lb.length);
  $('#lb').innerHTML=lb.map((x,k)=>{const sel=selected.includes(x.a.id);return `<button class="lbi${sel?' sel':''}" style="--c:${colorOf[x.a.id]||'transparent'}" data-id="${x.a.id}"><span class="k">${k+1}</span><span class="n">${nm(x.a)}<small>${x.a.tk}</small></span><span class="r ${x.roi>=0?'good':'bad'}">${fmtPct(x.roi)}</span></button>`}).join('');
  $('#lb').querySelectorAll('button').forEach(b=>b.onclick=()=>{toggleAsset(b.dataset.id);window.scrollTo({top:0,behavior:'smooth'})});
}

function drawChart(res,startI){
  const narrow=($('#chart').clientWidth||1000)<600; const W=narrow?420:1000,H=narrow?320:420,L=narrow?46:62,R=narrow?8:14,Tp=14,B=30;
  const x0=Math.min(...res.map(r=>r.from)), x1=ym2i(END);
  const all=res.flatMap(r=>r.pts.map(p=>p.val)).concat(res.flatMap(r=>r.pts.map(p=>p.inv)));
  let maxV=Math.max(...all)*1.05, minV=logScale?Math.max(1,Math.min(...all.filter(v=>v>0))):0;
  const fy=v=>logScale?Tp+(H-Tp-B)*(1-(Math.log10(Math.max(v,minV))-Math.log10(minV))/(Math.log10(maxV)-Math.log10(minV))):Tp+(H-Tp-B)*(1-v/maxV);
  const fx=i=>L+(W-L-R)*(x1===x0?0:(i-x0)/(x1-x0));
  let g='';
  // grid
  const ticks=[];
  if(logScale){for(let e=Math.floor(Math.log10(minV));e<=Math.ceil(Math.log10(maxV));e++){[1,3].forEach(k=>{const v=k*10**e;if(v>=minV&&v<=maxV)ticks.push(v)})}}
  else{const step=niceStep(maxV/5);for(let v=0;v<=maxV;v+=step)ticks.push(v)}
  ticks.forEach(v=>{const y=fy(v);g+=`<line x1="${L}" x2="${W-R}" y1="${y}" y2="${y}" stroke="#252a36"/><text x="${L-8}" y="${y+4}" fill="#8a91a3" font-size="12" text-anchor="end" font-family="JetBrains Mono">${shortUsd(v)}</text>`});
  for(let i=x0;i<=x1;i++){ if(i%12===0 && (!narrow||(x1-x0)<=72||Math.floor(i/12)%2===0)){const x=fx(i);g+=`<text x="${x}" y="${H-10}" fill="#8a91a3" font-size="12" text-anchor="middle">${Math.floor(i/12)}</text><line x1="${x}" x2="${x}" y1="${H-B}" y2="${H-B+5}" stroke="#3a4050"/>`}}
  // invested line (from earliest start)
  const ref=res.reduce((a,b)=>a.pts.length>=b.pts.length?a:b);
  g+=`<path d="${ref.pts.map((p,k)=>(k?'L':'M')+fx(p.i).toFixed(1)+' '+fy(p.inv).toFixed(1)).join('')}" fill="none" stroke="#e8ebf2" stroke-width="1.5" stroke-dasharray="5 5" opacity=".6"/>`;
  res.slice().reverse().forEach(r=>{
    g+=`<path d="${r.pts.map((p,k)=>(k?'L':'M')+fx(p.i).toFixed(1)+' '+fy(p.val).toFixed(1)).join('')}" fill="none" stroke="${r.a.c}" stroke-width="2.4" stroke-linejoin="round"/>`;
  });
  g+=`<line id="hl" x1="0" x2="0" y1="${Tp}" y2="${H-B}" stroke="#8a91a3" stroke-width="1" style="display:none"/>`;
  $('#chart').innerHTML=`<svg viewBox="0 0 ${W} ${H}" id="svg">${g}<rect x="${L}" y="${Tp}" width="${W-L-R}" height="${H-Tp-B}" fill="transparent" id="hit"/></svg>`;

  const svg=$('#svg'),tip=$('#tip'),hl=$('#hl');
  const move=ev=>{
    const rect=svg.getBoundingClientRect(), px=(ev.touches?ev.touches[0].clientX:ev.clientX)-rect.left;
    const vx=px*W/rect.width; let i=Math.round(x0+(vx-L)/(W-L-R)*(x1-x0)); i=Math.max(x0,Math.min(x1,i));
    hl.setAttribute('x1',fx(i));hl.setAttribute('x2',fx(i));hl.style.display='';
    const rows=res.map(r=>{const p=r.pts.find(q=>q.i===i);return p?{c:r.a.c,n:nm(r.a),v:p.val}:null}).filter(Boolean).sort((a,b)=>b.v-a.v);
    const ip=ref.pts.find(q=>q.i===i);
    tip.innerHTML=`<div class="d">${monthLabel(i2ym(i))}</div>`+rows.map(r=>`<div class="row"><span><span style="color:${r.c}">●</span> ${r.n}</span><b>${fmt$(r.v)}</b></div>`).join('')+(ip?`<div class="row" style="color:var(--muted);margin-top:4px"><span>${T[lang].investedLine}</span><span>${fmt$(ip.inv)}</span></div>`:'');
    tip.style.display='block';
    const cw=svg.parentElement.parentElement.getBoundingClientRect();
    let left=rect.left-cw.left+px+14; if(left+190>cw.width) left=rect.left-cw.left+px-200;
    tip.style.left=left+'px'; tip.style.top=(rect.top-cw.top+20)+'px';
  };
  const hit=$('#hit');
  hit.addEventListener('mousemove',move);hit.addEventListener('touchmove',move,{passive:true});
  hit.addEventListener('mouseleave',()=>{tip.style.display='none';hl.style.display='none'});
}
function niceStep(x){const p=10**Math.floor(Math.log10(x)),n=x/p;return (n<1.5?1:n<3?2:n<7?5:10)*p}
function shortUsd(v){return v>=1e6?'$'+(v/1e6).toFixed(v%1e6?1:0)+'M':v>=1e3?'$'+(v/1e3).toFixed(v%1e3?1:0)+'k':'$'+Math.round(v)}

document.querySelectorAll('#freq button').forEach(b=>b.onclick=()=>{freq=b.dataset.v;document.querySelectorAll('#freq button').forEach(x=>x.classList.toggle('on',x===b));render()});
$('#amt').oninput=render; $('#q').oninput=buildPool; $('#since').onchange=render;
$('#logBtn').onclick=()=>{logScale=!logScale;$('#logBtn').classList.toggle('on',logScale);render()};
$('#copyBtn').onclick=async()=>{try{await navigator.clipboard.writeText($('#shareText').textContent);$('#copyBtn').textContent=T[lang].copied;setTimeout(()=>$('#copyBtn').textContent=T[lang].copy,1600)}catch(e){}};

let rz;window.addEventListener('resize',()=>{clearTimeout(rz);rz=setTimeout(render,150)});
assignColors();buildSince();buildChips();render();

// WhatIfStack 4:5 card (1080x1350) for Instagram / Facebook / Threads, drawn on the page itself (their CSP blocks outside images).
// Usage in the built-in browser (javascript_tool): paste this file, then
//   await wisSquare({title:'What if you had invested $10 a day?', stat:'+49%', statLabel:'Bitcoin, 5 years', sub:'$18,420 in → $27,512 today',
//                    label:'DCA', series:[...monthly closes...], date:'2026-11-16'})
// It stores the JPEG as window.__wisFile and attaches it to the first <input type=file> (or the selector passed as o.input).
async function wisSquare(o) {
  const W = 1080, H = 1350, c = document.createElement('canvas'); c.width = W; c.height = H;
  const d = c.getContext('2d'), F = '"Segoe UI", "Helvetica Neue", Arial, sans-serif';
  const BG = '#0c1613', GOLD = '#f2b632', TEXT = '#eef5f1', MUTED = '#8fa59b', GREEN = '#3fd19b', RED = '#f06e6e';
  d.fillStyle = BG; d.fillRect(0, 0, W, H);
  d.strokeStyle = '#101c18'; d.lineWidth = 1;
  for (let x = 0; x < W; x += 60) { d.beginPath(); d.moveTo(x + .5, 0); d.lineTo(x + .5, H); d.stroke(); }
  d.fillStyle = GOLD; d.fillRect(0, 0, W, 10);
  d.textBaseline = 'top';
  [['#3fd19b', 10, 0, 32], ['#eef5f1', 0, 15, 52], ['#f2b632', 0, 30, 52]].forEach(([col, x, y, w]) => {
    d.fillStyle = col; d.beginPath(); d.roundRect(72 + x, 72 + y, w, 12, 6); d.fill(); });
  d.fillStyle = TEXT; d.font = `700 40px ${F}`; d.fillText('whatifstack', 144, 70);
  if (o.label) {
    d.font = `600 28px ${F}`; const lw = d.measureText(o.label).width;
    d.fillStyle = '#132520'; d.strokeStyle = '#1f3a32'; d.lineWidth = 2;
    d.beginPath(); d.roundRect(W - 72 - lw - 40, 66, lw + 40, 54, 27); d.fill(); d.stroke();
    d.fillStyle = GREEN; d.fillText(o.label, W - 72 - lw - 20, 78);
  }
  const tw = W - 144; let size = 84, lines = [];
  const wrap = t => { const out = []; let cur = ''; for (const w of t.split(/\s+/)) { const n = cur ? cur + ' ' + w : w;
    if (d.measureText(n).width <= tw || !cur) cur = n; else { out.push(cur); cur = w; } } if (cur) out.push(cur); return out; };
  for (size of [84, 76, 68, 60, 54]) { d.font = `700 ${size}px ${F}`; lines = wrap(o.title || ''); if (lines.length <= 4) break; }
  let y = 210; d.fillStyle = TEXT; lines.slice(0, 4).forEach(l => { d.fillText(l, 72, y); y += size * 1.14; });
  y += 40;
  if (o.stat) {
    let ss = 200; for (ss of [200, 180, 160, 140, 120, 100]) { d.font = `800 ${ss}px ${F}`; if (d.measureText(o.stat).width <= tw) break; }
    d.fillStyle = /^[-−]/.test(o.stat) ? RED : GOLD; d.fillText(o.stat, 72, y); y += ss + 10;
  }
  if (o.statLabel) { d.font = `600 40px ${F}`; d.fillStyle = TEXT; d.fillText(o.statLabel, 72, y); y += 56; }
  if (o.sub) { d.font = `400 36px ${F}`; d.fillStyle = MUTED; wrap(o.sub).slice(0, 2).forEach(l => { d.fillText(l, 72, y); y += 48; }); }
  const s = (o.series || []).filter(v => typeof v === 'number');
  if (s.length > 2) {
    const top = Math.max(y + 40, 900), bot = 1180, lo = Math.min(...s), hi = Math.max(...s), col = s[s.length - 1] >= s[0] ? GREEN : RED;
    const pts = s.map((v, k) => [72 + k * (W - 144) / (s.length - 1), bot - (v - lo) / ((hi - lo) || 1) * (bot - top)]);
    d.beginPath(); pts.forEach(([px, py], k) => k ? d.lineTo(px, py) : d.moveTo(px, py));
    d.strokeStyle = col; d.lineWidth = 6; d.lineJoin = 'round'; d.stroke();
    d.lineTo(W - 72, bot); d.lineTo(72, bot); d.closePath(); d.fillStyle = col + '22'; d.fill();
  }
  d.font = `400 30px ${F}`; d.fillStyle = MUTED; d.fillText((o.date || new Date().toISOString().slice(0, 10)) + ' · not investment advice', 72, 1250);
  d.textAlign = 'right'; d.fillStyle = TEXT; d.font = `700 30px ${F}`; d.fillText('whatifstack.com', W - 72, 1250); d.textAlign = 'left';
  const blob = await new Promise(r => c.toBlob(r, 'image/jpeg', 0.92));
  const file = new File([blob], 'whatifstack.jpg', { type: 'image/jpeg' }); window.__wisFile = file;
  const inp = document.querySelector(o.input || 'input[type=file]');
  if (inp) { const dt = new DataTransfer(); dt.items.add(file); inp.files = dt.files; inp.dispatchEvent(new Event('change', { bubbles: true })); }
  return { ok: true, size: blob.size, attached: !!inp };
}

// Square logo (profile picture): same three bars on the brand background. Attaches like wisSquare.
async function wisLogo(o = {}) {
  const S = 640, c = document.createElement('canvas'); c.width = S; c.height = S; const d = c.getContext('2d');
  d.fillStyle = '#0c1613'; d.fillRect(0, 0, S, S);
  [['#3fd19b', 60, 0, 220], ['#eef5f1', 0, 110, 340], ['#f2b632', 0, 220, 340]].forEach(([col, x, y, w]) => {
    d.fillStyle = col; d.beginPath(); d.roundRect(150 + x, 180 + y, w, 64, 32); d.fill(); });
  const blob = await new Promise(r => c.toBlob(r, 'image/jpeg', 0.95));
  const file = new File([blob], 'whatifstack-logo.jpg', { type: 'image/jpeg' }); window.__wisLogo = file;
  const inp = document.querySelector(o.input || 'input[type=file]');
  if (inp) { const dt = new DataTransfer(); dt.items.add(file); inp.files = dt.files; inp.dispatchEvent(new Event('change', { bubbles: true })); }
  return { ok: true, size: blob.size, attached: !!inp };
}

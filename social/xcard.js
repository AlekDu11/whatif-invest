// WhatIfStack card for X posts, drawn on the x.com page itself (X's CSP blocks loading images from other sites).
// Usage in the built-in browser on https://x.com/compose/post (javascript_tool): paste this file, then call
//   await wisCard({title:'Crypto Fear & Greed drops to 10', stat:'10', statLabel:'Extreme fear', label:'Market',
//                  series:[...last 30-60 closes from data/market.json or the asset JSON...], date:'2026-11-16'})
// It renders 1200x675 JPEG and attaches it to the composer's file input. Returns {ok, size} or {err}.
async function wisCard(o) {
  const W = 1200, H = 675, c = document.createElement('canvas'); c.width = W; c.height = H;
  const d = c.getContext('2d'), F = '"Segoe UI", "Helvetica Neue", Arial, sans-serif';
  const BG = '#0c1613', GOLD = '#f2b632', TEXT = '#eef5f1', MUTED = '#8fa59b', GREEN = '#3fd19b', RED = '#f06e6e';
  d.fillStyle = BG; d.fillRect(0, 0, W, H);
  d.strokeStyle = '#101c18'; d.lineWidth = 1;
  for (let x = 0; x < W; x += 60) { d.beginPath(); d.moveTo(x + .5, 0); d.lineTo(x + .5, H); d.stroke(); }
  d.fillStyle = GOLD; d.fillRect(0, 0, 10, H);
  const s = (o.series || []).filter(v => typeof v === 'number');
  if (s.length > 2) {   // faint price band
    const lo = Math.min(...s), hi = Math.max(...s), up = s[s.length - 1] >= s[0], col = up ? GREEN : RED;
    const pts = s.map((v, k) => [40 + k * (W - 80) / (s.length - 1), 640 - (v - lo) / ((hi - lo) || 1) * 250]);
    d.beginPath(); pts.forEach(([x, y], k) => k ? d.lineTo(x, y) : d.moveTo(x, y)); d.lineTo(W - 40, H); d.lineTo(40, H); d.closePath();
    d.fillStyle = col + '1a'; d.fill();
    d.beginPath(); pts.forEach(([x, y], k) => k ? d.lineTo(x, y) : d.moveTo(x, y)); d.strokeStyle = col + '70'; d.lineWidth = 4; d.stroke();
  }
  // brand: three stacked bars + wordmark
  [['#3fd19b', 8, 0, 26], ['#eef5f1', 0, 12, 42], ['#f2b632', 0, 24, 42]].forEach(([col, x, y, w]) => {
    d.fillStyle = col; d.beginPath(); d.roundRect(64 + x, 50 + y, w, 10, 5); d.fill(); });
  d.fillStyle = TEXT; d.font = `700 32px ${F}`; d.textBaseline = 'top'; d.fillText('whatifstack', 122, 50);
  if (o.label) {
    d.font = `600 24px ${F}`; const lw = d.measureText(o.label).width;
    d.fillStyle = '#132520'; d.strokeStyle = '#1f3a32'; d.lineWidth = 2;
    d.beginPath(); d.roundRect(W - 64 - lw - 36, 46, lw + 36, 46, 23); d.fill(); d.stroke();
    d.fillStyle = GREEN; d.fillText(o.label, W - 64 - lw - 18, 56);
  }
  // title (wrap, shrink to fit 4 lines)
  const tw = W - 128 - (o.stat ? 400 : 0);
  let size = 72, lines = [];
  const wrap = t => { const out = []; let cur = ''; for (const w of t.split(/\s+/)) { const n = cur ? cur + ' ' + w : w;
    if (d.measureText(n).width <= tw || !cur) cur = n; else { out.push(cur); cur = w; } } if (cur) out.push(cur); return out; };
  for (size of [72, 66, 60, 54, 48, 44]) { d.font = `700 ${size}px ${F}`; lines = wrap(o.title || ''); if (lines.length <= 4) break; }
  let y = 160 + (4 - Math.min(lines.length, 4)) * size * 0.28;
  d.fillStyle = TEXT; lines.slice(0, 4).forEach(l => { d.fillText(l, 64, y); y += size * 1.14; });
  if (o.stat) {
    let ss = 110; for (ss of [110, 96, 84, 72, 62, 54]) { d.font = `800 ${ss}px ${F}`; if (d.measureText(o.stat).width <= 380) break; }
    d.textAlign = 'right'; d.fillStyle = /^[-−]/.test(o.stat) ? RED : GOLD; d.fillText(o.stat, W - 64, 250);
    if (o.statLabel) { d.font = `400 26px ${F}`; d.fillStyle = MUTED;
      const words = o.statLabel.split(' '); let cur = '', row = 0;
      for (const w of words) { const n = cur ? cur + ' ' + w : w;
        if (d.measureText(n).width > 360 && cur) { d.fillText(cur, W - 64, 250 + ss + 14 + row * 34); row++; cur = w; } else cur = n; }
      if (cur && row < 2) d.fillText(cur, W - 64, 250 + ss + 14 + row * 34); }
    d.textAlign = 'left';
  }
  d.font = `400 26px ${F}`; d.fillStyle = MUTED; d.fillText(o.date || new Date().toISOString().slice(0, 10), 64, 600);
  d.textAlign = 'right'; d.fillText('whatifstack.com', W - 64, 600); d.textAlign = 'left';
  const blob = await new Promise(r => c.toBlob(r, 'image/jpeg', 0.9));
  for (let i = 0; i < 20 && !document.querySelector('[role=dialog] input[type=file]'); i++) await new Promise(r => setTimeout(r, 500));
  const inp = document.querySelector('[role=dialog] input[type=file]') || document.querySelector('input[type=file][data-testid="fileInput"]') || document.querySelector('input[type=file]');
  if (!inp) return { err: 'no file input: open https://x.com/compose/post first' };
  const dt = new DataTransfer(); dt.items.add(new File([blob], 'whatifstack.jpg', { type: 'image/jpeg' }));
  inp.files = dt.files; inp.dispatchEvent(new Event('change', { bubbles: true }));
  return { ok: true, size: blob.size };
}

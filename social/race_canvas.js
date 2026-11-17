// In-page race video for composers whose CSP blocks downloading our MP4 (X). Renders the same animation as
// scripts/race_video.py on a canvas, encodes H.264 with WebCodecs (deterministic, works in a background tab) and muxes a
// minimal MP4. scripts/race_snippet.py prepends `const RACE = {...}` (data, colours, logos as data: URIs) and this file.
// Result: window.__wisRaceFile (File video/mp4). Returns a short status string.
(async () => {
  const R = RACE, W = 1080, H = 1350, FPS = 30;
  const BG = '#0c1612', CARD = '#14221c', TEXT = '#ecf4f0', MUTED = '#8ca097', LINE = '#283a32', ACC = '#3fd19b', RED = '#ff7a6e';
  const FB = '700 {s}px Geologica, "Segoe UI", system-ui, sans-serif', FS = '600 {s}px Geologica, "Segoe UI", system-ui, sans-serif', FT = '400 {s}px Onest, "Segoe UI", system-ui, sans-serif';
  const f = (t, s) => t.replace('{s}', s);
  const cv = document.createElement('canvas'); cv.width = W; cv.height = H; const c = cv.getContext('2d');
  const logos = {};
  await Promise.all(R.ids.map(i => new Promise(ok => { if (!R.logo[i]) return ok(); const im = new Image(); im.onload = () => { logos[i] = im; ok() }; im.onerror = ok; im.src = R.logo[i] })));
  const money = v => v >= 1e6 ? '$' + (v / 1e6).toFixed(2) + 'M' : v >= 1e4 ? '$' + (v / 1e3).toFixed(1) + 'K' : '$' + Math.round(v).toLocaleString('en-US');
  const n = R.inv.length, anim = Math.round(R.secs * FPS), hold = Math.round(3.5 * FPS);
  const logo = (i, x, y, s, ring) => { if (ring) { c.fillStyle = ring; c.beginPath(); c.arc(x + s / 2, y + s / 2, s / 2 + 4, 0, 7); c.fill() }
    if (logos[i]) { c.save(); c.beginPath(); c.arc(x + s / 2, y + s / 2, s / 2, 0, 7); c.clip(); c.drawImage(logos[i], x, y, s, s); c.restore() }
    else { c.fillStyle = R.col[i]; c.beginPath(); c.arc(x + s / 2, y + s / 2, s / 2, 0, 7); c.fill(); c.fillStyle = BG; c.font = f(FB, s * .38); c.textAlign = 'center'; c.fillText(R.tk[i].slice(0, 3), x + s / 2, y + s * .64); c.textAlign = 'left' } };
  const txt = (s, x, y, font, col) => { c.font = font; c.fillStyle = col; c.fillText(s, x, y) };
  const CX0 = 90, CX1 = W - 230, CY0 = 430, CY1 = 1170;
  let ymaxS = null;
  function frame(fr) {
    const t = Math.min(1, fr / anim), e = t * t * (3 - 2 * t) * .15 + t * .85, pos = e * (n - 1), j = Math.floor(pos), fj = pos - j, j1 = Math.min(j + 1, n - 1);
    c.fillStyle = BG; c.fillRect(0, 0, W, H); c.textBaseline = 'alphabetic';
    txt('whatifstack', 60, 80, f(FS, 32), ACC); txt(R.title, 60, 145, f(FB, 52), TEXT);
    let x = 60;
    R.ids.forEach((i, k) => { logo(i, x, 180, 64); c.font = f(FB, 40); txt(R.tk[i], x + 76, 228, f(FB, 40), R.col[i]); x += 76 + c.measureText(R.tk[i]).width + 26;
      if (k < R.ids.length - 1) { txt('vs', x, 225, f(FS, 26), MUTED); c.font = f(FS, 26); x += c.measureText('vs').width + 26 } });
    const cur = R.months[Math.min(j + (fj > .5 ? 1 : 0), n - 1)], invd = R.inv[j] + (R.inv[j1] - R.inv[j]) * fj;
    txt(cur, 60, 340, f(FB, 52), TEXT); txt(R.invLabel + ': ' + money(invd), 60, 385, f(FS, 26), MUTED);
    const cv_ = {}; R.ids.forEach(i => cv_[i] = R.S[i][j] + (R.S[i][j1] - R.S[i][j]) * fj);
    let ymaxT = Math.max(invd, ...R.ids.map(i => Math.max(...R.S[i].slice(0, j + 2)))) * 1.12;
    ymaxS = ymaxS == null ? ymaxT : ymaxS + (ymaxT - ymaxS) * .12;
    const ymax = Math.max(ymaxS, invd * 1.05, ...R.ids.map(i => cv_[i] * 1.05));
    const X = q => CX0 + (CX1 - CX0) * q / Math.max(1, n - 1), Y = v => CY1 - (CY1 - CY0) * v / ymax;
    for (let g = 0; g < 5; g++) { const gv = ymax * g / 4, gy = Y(gv); c.strokeStyle = LINE; c.lineWidth = 2; c.beginPath(); c.moveTo(CX0, gy); c.lineTo(CX1, gy); c.stroke(); txt(money(gv), CX1 + 14, gy + 8, f(FT, 22), MUTED) }
    c.setLineDash([12, 10]); c.strokeStyle = MUTED; c.lineWidth = 3; c.beginPath(); for (let q = 0; q <= j; q++) c.lineTo(X(q), Y(R.inv[q])); c.lineTo(X(pos), Y(invd)); c.stroke(); c.setLineDash([]);
    [...R.ids].sort((a, b) => cv_[a] - cv_[b]).forEach(i => { c.strokeStyle = R.col[i]; c.lineWidth = 6; c.lineJoin = 'round'; c.beginPath(); for (let q = 0; q <= j; q++) c.lineTo(X(q), Y(R.S[i][q])); c.lineTo(X(pos), Y(cv_[i])); c.stroke() });
    const heads = R.ids.map(i => [Y(cv_[i]), i]).sort((a, b) => a[0] - b[0]), placed = [];
    heads.forEach(([yy, i]) => { let ly = yy; placed.forEach(py => { if (Math.abs(ly - py) < 70) ly = py + 70 }); placed.push(ly);
      const hx = X(pos); logo(i, hx - 23, yy - 23, 46, R.col[i]);
      const roi = invd ? cv_[i] / invd - 1 : 0, tx = Math.min(hx + 38, W - 200);
      if (Math.abs(ly - yy) > 4) { c.strokeStyle = R.col[i]; c.lineWidth = 2; c.beginPath(); c.moveTo(hx + 27, yy); c.lineTo(tx - 4, ly - 6); c.stroke() }
      txt(money(cv_[i]), tx, ly - 6, f(FS, 32), R.col[i]); txt((roi >= 0 ? '+' : '') + Math.round(roi * 100) + '%', tx, ly + 24, f(FT, 22), roi >= 0 ? ACC : RED) });
    txt('whatifstack.com', 60, H - 78, f(FS, 32), ACC); txt(R.foot, 60, H - 40, f(FT, 22), MUTED);
    if (fr >= anim) {
      const k = Math.min(1, (fr - anim) / (.6 * FPS)); c.globalAlpha = k; c.fillStyle = BG; c.fillRect(0, 270, W, H - 400); c.globalAlpha = 1;
      if (k >= 1) {
        const rank = [...R.ids].sort((a, b) => R.S[b][n - 1] - R.S[a][n - 1]); let y = 430;
        txt(R.invLabel + ': ' + money(R.inv[n - 1]), 80, y - 70, f(FS, 32), MUTED);
        rank.forEach((i, r) => { c.fillStyle = CARD; c.beginPath(); c.roundRect(70, y, W - 140, 150, 28); c.fill(); if (r === 0) { c.strokeStyle = R.col[i]; c.lineWidth = 4; c.stroke() }
          logo(i, 100, y + 27, 96); txt((r + 1) + '. ' + R.tk[i], 220, y + 68, f(FB, 40), TEXT);
          const roi = R.S[i][n - 1] / R.inv[n - 1] - 1; txt((roi >= 0 ? '+' : '') + Math.round(roi * 100) + '%', 220, y + 116, f(FS, 32), roi >= 0 ? ACC : RED);
          c.font = f(FB, 52); const vt = money(R.S[i][n - 1]); txt(vt, W - 110 - c.measureText(vt).width, y + 95, f(FB, 52), R.col[i]); y += 175 });
        txt(R.winLabel + ': ' + R.tk[rank[0]], 80, y + 60, f(FB, 40), R.col[rank[0]]);
      }
    }
  }
  // --- encode (WebCodecs, H.264) ---
  const chunks = []; let desc = null;
  const enc = new VideoEncoder({ output: (ch, meta) => { const b = new Uint8Array(ch.byteLength); ch.copyTo(b); chunks.push({ b, key: ch.type === 'key' }); if (meta && meta.decoderConfig && meta.decoderConfig.description) desc = new Uint8Array(meta.decoderConfig.description) }, error: e => { throw e } });
  enc.configure({ codec: 'avc1.4d0032', width: W, height: H, bitrate: 3e6, framerate: FPS, avc: { format: 'avc' } });
  const total = anim + hold;
  for (let fr = 0; fr < total; fr++) {
    frame(fr);
    const vf = new VideoFrame(cv, { timestamp: Math.round(fr * 1e6 / FPS), duration: Math.round(1e6 / FPS) });
    enc.encode(vf, { keyFrame: fr % 60 === 0 }); vf.close();
    if (enc.encodeQueueSize > 8) await new Promise(r => setTimeout(r, 0));
  }
  await enc.flush(); enc.close();
  // --- minimal MP4 mux ---
  const u32 = v => [v >>> 24 & 255, v >>> 16 & 255, v >>> 8 & 255, v & 255], u16 = v => [v >> 8 & 255, v & 255], str = s => [...s].map(ch => ch.charCodeAt(0));
  const box = (type, ...parts) => { const body = parts.flatMap(p => p instanceof Uint8Array ? Array.from(p) : p); return [...u32(8 + body.length), ...str(type), ...body] };
  const full = (type, v, fl, ...parts) => box(type, [v, ...u32(fl).slice(1)], ...parts);
  const TS = FPS * 1000, dur = total * 1000, mat = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 64, 0, 0, 0].map((v, k) => v);
  const M = [0x00010000, 0, 0, 0, 0x00010000, 0, 0, 0, 0x40000000].flatMap(u32);
  const ftyp = box('ftyp', str('isom'), u32(512), str('isomiso2avc1mp41'));
  const sizes = chunks.map(ch => ch.b.length), mdatLen = 8 + sizes.reduce((a, b) => a + b, 0);
  const build = off => {
    const avc1 = box('avc1', new Array(6).fill(0), u16(1), new Array(16).fill(0), u16(W), u16(H), u32(0x00480000), u32(0x00480000), u32(0), u16(1), new Array(32).fill(0), u16(24), u16(0xffff), box('avcC', desc));
    const stbl = box('stbl', full('stsd', 0, 0, u32(1), avc1), full('stts', 0, 0, u32(1), u32(total), u32(1000)),
      full('stss', 0, 0, u32(chunks.filter(ch => ch.key).length), chunks.flatMap((ch, k) => ch.key ? u32(k + 1) : [])),
      full('stsc', 0, 0, u32(1), u32(1), u32(total), u32(1)), full('stsz', 0, 0, u32(0), u32(total), sizes.flatMap(u32)), full('stco', 0, 0, u32(1), u32(off)));
    const minf = box('minf', full('vmhd', 0, 1, u16(0), u16(0), u16(0), u16(0)), box('dinf', full('dref', 0, 0, u32(1), full('url ', 0, 1))), stbl);
    const mdia = box('mdia', full('mdhd', 0, 0, u32(0), u32(0), u32(TS), u32(dur), u16(0x55c4), u16(0)), full('hdlr', 0, 0, u32(0), str('vide'), new Array(12).fill(0), str('VideoHandler'), [0]), minf);
    const tkhd = full('tkhd', 0, 3, u32(0), u32(0), u32(1), u32(0), u32(Math.round(dur / TS * 1000)), new Array(8).fill(0), u16(0), u16(0), u16(0), u16(0), M, u32(W << 16), u32(H << 16));
    const mvhd = full('mvhd', 0, 0, u32(0), u32(0), u32(1000), u32(Math.round(dur / TS * 1000)), u32(0x00010000), u16(0x0100), new Array(10).fill(0), M, new Array(24).fill(0), u32(2));
    return box('moov', mvhd, box('trak', tkhd, mdia));
  };
  let moov = build(0); moov = build(ftyp.length + moov.length + 8);
  const out = new Uint8Array(ftyp.length + moov.length + mdatLen); let p = 0;
  out.set(ftyp, p); p += ftyp.length; out.set(moov, p); p += moov.length; out.set(u32(mdatLen), p); out.set(str('mdat'), p + 4); p += 8;
  chunks.forEach(ch => { out.set(ch.b, p); p += ch.b.length });
  window.__wisRaceFile = new File([out], R.slug + '.mp4', { type: 'video/mp4' });
  return 'ok ' + Math.round(out.length / 1024) + ' KB, ' + total + ' frames';
})();

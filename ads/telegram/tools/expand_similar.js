// Run in the built-in browser on https://ads.telegram.org/account/ad/new (javascript_tool).
// Expands the base through Telegram Ads' own "similar channels" (no Telegram account API calls,
// so no FLOOD_WAIT on the owner's account).
// Usage: set SEEDS to the best-performing channel usernames, run, copy the returned JSON
// into ads/telegram/data/similar_YYYY-MM-DD.json.
const SEEDS = window.SEEDS || [];               // e.g. ["CryptoZInsights", "Cryptos_Insights"]
const KNOWN = new Set((window.KNOWN || []).map(s => s.toLowerCase())); // already in channels.csv
const req = (m, p) => new Promise(res => Aj.apiRequest(m, p, r => res(r)));
const sleep = ms => new Promise(r => setTimeout(r, ms));
const out = {};
for (const u of SEEDS) {
  const s = await req('searchChannel', { owner_id: Aj.state.ownerId, query: 'https://t.me/' + u, field: 'channels' });
  if (!s.channel) { out[u] = { error: s.error || 'not found' }; continue; }
  const r = await req('getSimilarChannels', { channels: s.channel.val, for: 'channels' });
  out[u] = (r.channels || []).map(c => {
    const subs = ((c.cb_item || '').match(/([\d,]+) subscribers/) || [])[1];
    return { u: c.username, name: c.name, subs: subs ? +subs.replace(/,/g, '') : null };
  }).filter(c => c.u && !KNOWN.has(c.u.toLowerCase()));
  await sleep(300);
}
JSON.stringify(out);

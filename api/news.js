// Crypto news aggregator: headlines + links from public RSS feeds of major outlets.
// We only show title, source, time and a link to the original article (no article text, no images).
// Cached at the edge for 10 minutes.
const FEEDS = [
  ['CoinDesk', 'https://www.coindesk.com/arc/outboundfeeds/rss/'],
  ['Cointelegraph', 'https://cointelegraph.com/rss'],
  ['Decrypt', 'https://decrypt.co/feed'],
  ['The Block', 'https://www.theblock.co/rss.xml'],
  ['Bitcoin Magazine', 'https://bitcoinmagazine.com/.rss/full/'],
  ['CryptoSlate', 'https://cryptoslate.com/feed/'],
  ['BeInCrypto', 'https://beincrypto.com/feed/'],
  ['U.Today', 'https://u.today/rss'],
  ['CryptoPotato', 'https://cryptopotato.com/feed/'],
];
const TAGS = [
  ['bitcoin', /\b(bitcoin|btc)\b/i], ['ethereum', /\b(ethereum|ether|eth)\b/i], ['etf', /\betfs?\b/i],
  ['regulation', /\b(sec|regulat\w*|law|bill|senate|congress|cftc|mica|ban|court|lawsuit)\b/i],
  ['defi', /\b(defi|dex|lending|liquidity|staking|restaking)\b/i], ['stablecoins', /\b(stablecoins?|usdt|usdc|tether|circle)\b/i],
  ['solana', /\b(solana|sol)\b/i], ['xrp', /\b(xrp|ripple)\b/i], ['markets', /\b(price|rally|crash|market|liquidat\w*|fed|rates?|stocks?|nasdaq|s&p)\b/i],
  ['hacks', /\b(hack\w*|exploit\w*|scam|stolen|drain\w*)\b/i],
  ['ai', /\b(ai|a\.i\.|artificial intelligence|openai|nvidia|llm|chatgpt|agents?|bittensor|tao)\b/i],
];
const dec = s => s.replace(/<!\[CDATA\[([\s\S]*?)\]\]>/g, '$1').replace(/<[^>]+>/g, '').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>')
  .replace(/&quot;/g, '"').replace(/&#0?39;|&#8217;|&rsquo;/g, '’').replace(/&#8216;|&lsquo;/g, '‘').replace(/&#822[01];|&[lr]dquo;/g, '"')
  .replace(/&#8211;|&ndash;/g, '–').replace(/&#8212;|&mdash;/g, '—').replace(/&#\d+;/g, '').replace(/\s+/g, ' ').trim();
const tag = (x, n) => { const m = x.match(new RegExp(`<${n}[^>]*>([\\s\\S]*?)</${n}>`, 'i')); return m ? dec(m[1]) : '' };

async function feed([src, url]) {
  try {
    const ctl = new AbortController(); const t = setTimeout(() => ctl.abort(), 6000);
    const r = await fetch(url, { signal: ctl.signal, headers: { 'User-Agent': 'WhatIfStack/1.0 (+https://whatifstack.com/)' } });
    clearTimeout(t);
    if (!r.ok) return [];
    const xml = await r.text();
    return (xml.match(/<item[\s>][\s\S]*?<\/item>/gi) || []).slice(0, 25).map(it => {
      const title = tag(it, 'title');
      let link = tag(it, 'link') || (it.match(/<guid[^>]*>(https?:[^<]+)<\/guid>/i) || [])[1] || '';
      const d = Date.parse(tag(it, 'pubDate') || tag(it, 'dc:date')) || 0;
      const cats = (it.match(/<category[^>]*>([\s\S]*?)<\/category>/gi) || []).map(c => dec(c.replace(/<\/?category[^>]*>/gi, ''))).join(' ');
      const tags = TAGS.filter(([, re]) => re.test(title + ' ' + cats)).map(([k]) => k).slice(0, 3);
      return title && /^https?:/.test(link) ? { t: title.slice(0, 220), u: link.trim(), s: src, d, g: tags } : null;
    }).filter(Boolean);
  } catch (e) { return [] }
}

const G = require('./_guard');
module.exports = async (req, res) => {
  if (G.over(req, 30, 'news')) { res.statusCode = 429; res.setHeader('Retry-After', '60'); return res.end('[]') }
  const all = (await Promise.all(FEEDS.map(feed))).flat();
  const seen = new Set();
  const items = all.filter(x => { const k = x.t.toLowerCase().slice(0, 60); if (seen.has(k)) return false; seen.add(k); return true })
    .sort((a, b) => b.d - a.d).slice(0, 150);
  res.setHeader('Cache-Control', 'public, s-maxage=600, stale-while-revalidate=1800');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  res.status(200).send(JSON.stringify({ updated: Date.now(), sources: FEEDS.map(f => f[0]), items }));
};

// Probe the data sources for the memes section from a US datacenter (like Vercel iad1). Run by probe.yml.
const UA = { 'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json' };
const T = async (name, url, opt = {}, pick = j => j) => {
  try { const r = await fetch(url, { ...opt, headers: { ...UA, ...(opt.headers || {}) }, signal: AbortSignal.timeout(15000) });
    const t = await r.text(); let j = null; try { j = JSON.parse(t) } catch (e) {}
    console.log(`\n## ${name}: HTTP ${r.status}`); console.log(JSON.stringify(j ? pick(j) : t.slice(0, 300)).slice(0, 900));
  } catch (e) { console.log(`\n## ${name}: FAIL ${e.message}`) } };
(async () => {
  await T('binance listings', 'https://www.binance.com/bapi/composite/v1/public/cms/article/list/query?type=1&pageNo=1&pageSize=10&catalogId=48', {},
    j => ((j.data || {}).catalogs || []).map(c => (c.articles || []).slice(0, 6).map(a => [a.title, a.releaseDate, a.code])));
  await T('okx listings', 'https://www.okx.com/api/v5/support/announcements?annType=announcements-new-listings', {},
    j => (((j.data || [])[0] || {}).details || []).slice(0, 6).map(a => [a.title, a.pTime, a.url]));
  await T('bybit listings', 'https://api.bybit.com/v5/announcements/index?locale=en-US&type=new_crypto&limit=6', {},
    j => ((j.result || {}).list || []).map(a => [a.title, a.dateTimestamp, a.url]));
  await T('coingecko categories', 'https://api.coingecko.com/api/v3/coins/categories', {},
    j => j.filter(c => /meme/i.test(c.id + c.name)).map(c => [c.id, c.name, Math.round(c.market_cap / 1e6), c.market_cap_change_24h]));
  await T('binance hype sol', 'https://web3.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/market/token/pulse/social/hype/rank/leaderboard/ai?chainId=CT_501&targetLanguage=en&timeRange=1', {},
    j => (((j.data || {}).leaderBoardList) || []).slice(0, 3).map(x => [(x.metaInfo || {}).symbol, ((x.socialHypeInfo || {}).socialSummaryBrief || '').slice(0, 80)]));
  for (const rt of [10, 20, 30]) await T('rush ' + rt, 'https://web3.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/market/token/pulse/rank/list/ai',
    { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ chainId: 'CT_501', rankType: rt, limit: 5 }) },
    j => ({ keys: Object.keys(j.data || {}), n: Array.isArray(j.data) ? j.data.length : null, first: JSON.stringify(Array.isArray(j.data) ? j.data[0] : j.data).slice(0, 400) }));
})();

const UA = { 'User-Agent': 'Mozilla/5.0', 'Accept': 'application/json' };
const T = async (name, url, pick = j => j) => { try { const r = await fetch(url, { headers: UA, signal: AbortSignal.timeout(15000) }); const t = await r.text(); let j = null; try { j = JSON.parse(t) } catch (e) {}
  console.log(`\n## ${name}: HTTP ${r.status}`); console.log(JSON.stringify(j ? pick(j) : t.slice(0, 300)).slice(0, 1500)) } catch (e) { console.log(`\n## ${name}: FAIL ${e.message}`) } };
(async () => {
  await T('alpha list', 'https://www.binance.com/bapi/defi/v1/public/wallet-direct/buw/wallet/cex/alpha/all/token/list', j => { const d = j.data || []; const k = Object.keys(d[0] || {}); const s = [...d].sort((a, b) => (+b.listingTime || 0) - (+a.listingTime || 0)).slice(0, 5).map(x => [x.symbol, x.name, x.listingTime, x.chainName, x.marketCap, x.contractAddress]); return { n: d.length, k, s } });
  await T('mexc new', 'https://www.mexc.com/api/operation/new_coin_calendar?timestamp=' + Date.now(), j => JSON.stringify(j).slice(0, 800));
  await T('gate new', 'https://www.gate.io/api/web/v1/announcement/list?type=listing&page=1&limit=5', j => JSON.stringify(j).slice(0, 600));
})();

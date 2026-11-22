// one-off probe (GitHub Actions): Binance social hype (translated), dynamic info, meta info field names
const H = { 'Content-Type': 'application/json', 'Accept-Encoding': 'identity', 'User-Agent': 'binance-web3/1.1 (Skill)' };
const B = 'https://web3.binance.com/bapi/defi';
const get = u => fetch(B + u, { headers: H }).then(r => r.json());
(async () => {
  for (const l of ['uk', 'ja', 'tr', 'ru', 'es']) {
    const j = await get(`/v1/public/wallet-direct/buw/wallet/market/token/pulse/social/hype/rank/leaderboard/ai?chainId=CT_501&targetLanguage=${l}&timeRange=1`);
    const L = ((j.data || {}).leaderBoardList || []);
    console.log('HYPE', l, j.code, L.length, JSON.stringify(L[0] && { s: L[0].metaInfo.symbol, a: L[0].metaInfo.contractAddress, mi: L[0].marketInfo, sh: L[0].socialHypeInfo }).slice(0, 900));
  }
  const j = await get(`/v1/public/wallet-direct/buw/wallet/market/token/pulse/social/hype/rank/leaderboard/ai?chainId=56&targetLanguage=en&timeRange=1`);
  console.log('HYPE bsc', ((j.data || {}).leaderBoardList || []).length);
  const a = 'DChXQ4qFPpNPEDfZLNiwvPhrVuuFGfqEDLAAZbiZHUWf';
  const d = await get(`/v4/public/wallet-direct/buw/wallet/market/token/dynamic/info/ai?chainId=CT_501&contractAddress=${a}`);
  console.log('DYN', d.code, JSON.stringify(d.data).slice(0, 2500));
  const m = await get(`/v1/public/wallet-direct/buw/wallet/dex/market/token/meta/info/ai?chainId=CT_501&contractAddress=${a}`);
  console.log('META', m.code, JSON.stringify(m.data).slice(0, 1500));
})();

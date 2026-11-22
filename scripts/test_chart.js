// Smoke test for exchange candle URLs (GitHub Actions). node scripts/test_chart.js
const U = [
  'https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=BTC_USDT&interval=1d&limit=1000',
  'https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=BTC_USDT&interval=1d&limit=999',
  'https://api.gateio.ws/api/v4/spot/candlesticks?currency_pair=DIGI_USDT&interval=1d&limit=900',
  'https://api.mexc.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=1000',
  'https://api.mexc.com/api/v3/klines?symbol=CHOPUSDT&interval=1d&limit=500',
  'https://api.bybit.com/v5/market/kline?category=spot&symbol=MNTUSDT&interval=D&limit=1000',
];
(async () => { for (const u of U) { try { const r = await fetch(u, { headers: { 'User-Agent': 'Mozilla/5.0', Accept: 'application/json' } }); const t = await r.text(); console.log('URL', r.status, u.slice(8, 70), t.slice(0, 160)) } catch (e) { console.log('URL ERR', u, e.message) } } })();

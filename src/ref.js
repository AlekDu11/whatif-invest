// Partner (referral) links. URLs are /go/<id> (click tracker, api/go.js); the real referral URLs live in api/_partners.js.
// REF overrides one asset; REF_DEFAULT is used for every other asset in that category.
// An empty url ('') hides the button.
window.REF = {
  hype: { url: '/go/hyperliquid', where: 'Hyperliquid' },
};
window.REF_DEFAULT = {
  crypto: { url: '/go/binance', where: 'Binance' },
  metal:  { url: '/go/bybit', where: 'Bybit' },
  stock:  { url: '/go/bybit', where: 'Bybit' },   // Bybit xStocks (tokenized US stocks) / TradFi — where Freedom24 is not offered
  etf:    { url: '/go/bybit', where: 'Bybit' },
  cmd:    { url: '/go/bybit', where: 'Bybit' },   // commodities via Bybit TradFi
};
// Per-language overrides: Freedom24 (EU broker, CySEC; recurring investment plan) for stocks/ETFs where its audience lives.
// Not available to US or UK residents, so English and Asian-language pages keep Bybit.
window.REF_LANG = {
  // Binance does not serve the US and restricts the UK; Kraken does — so English pages send crypto buyers to Kraken.
  crypto: { langs: ['en'], url: '/go/kraken', where: 'Kraken' },
  stock: { langs: ['uk', 'de', 'fr', 'it', 'es', 'pt', 'pl', 'nl'], url: '/go/freedom24', where: 'Freedom24' },
  etf:   { langs: ['uk', 'de', 'fr', 'it', 'es', 'pt', 'pl', 'nl'], url: '/go/freedom24', where: 'Freedom24' },
};

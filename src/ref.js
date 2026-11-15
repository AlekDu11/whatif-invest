// Partner (referral) links. URLs are /go/<id> (click tracker, api/go.js); the real referral URLs live in api/_partners.js.
// REF overrides one asset; REF_DEFAULT is used for every other asset in that category.
// An empty url ('') hides the button.
window.REF = {
  hype: { url: '/go/hyperliquid', where: 'Hyperliquid' },
};
window.REF_DEFAULT = {
  crypto: { url: '/go/binance', where: 'Binance' },
  metal:  { url: '/go/bybit', where: 'Bybit' },
  stock:  { url: '', where: 'broker' },
  etf:    { url: '', where: 'broker' },
};

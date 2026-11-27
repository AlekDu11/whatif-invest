# Money pages — «how to buy X in <country>»

Owner 2026-11-25: one page per country, in the country's language + English, with local banks, payment methods, regulator, taxes and our partner exchanges where they legally serve that country. Sample: content/blog/uk/how-to-buy-bitcoin-in-ukraine.md (+ en).
Written by the scheduled task «Money pages» (2–3 countries per run). Slug: how-to-buy-bitcoin-in-<country> (same slug in every language of that country).

Phase 1 — Bitcoin, queue (top to bottom; country: languages):
- [x] Ukraine: uk, en — 2026-11-25 (sample)
- [x] Poland: pl, en — 2026-11-26
- [x] Turkey: tr, en — 2026-11-26
- [x] India: hi, en — 2026-11-27
- [x] Japan: ja, en — 2026-11-27
- [ ] Germany: de, en
- [ ] Spain: es, en
- [ ] Mexico: es, en
- [ ] Brazil: pt, en
- [ ] Indonesia: id, en
- [ ] Vietnam: vi, en
- [ ] Philippines: fil, en
- [ ] Nigeria: en
- [ ] United States: en, es
- [ ] United Kingdom: en
- [ ] France: fr, en
- [ ] Italy: it, en
- [ ] Netherlands: nl, en
- [ ] South Korea: ko, en
- [ ] Thailand: th, en
- [ ] United Arab Emirates: ar, en
- [ ] Kazakhstan: ru, en
- [ ] Argentina: es, en
- [ ] Canada: en, fr
- [ ] Australia: en

Phase 2 (after phase 1): «how to buy USDT in <country>» → «best crypto exchange in <country>» → «how to buy Apple/Tesla stock from <country>» → «best broker in <country>».

## Offer guides (owner 2026-11-27: «articles on our partner offers that rank in Google — that is where the first money comes from»)
Written by the same task on EVEN days of the month (odd days = country pages above). One guide per run, in the languages listed. Honest how-to that answers the search query first; the partner is one clear option, never the only one; {{offer:<bonus item id>}} box where the offer is in data/bonuses.json; real fees/limits from official pages with the date checked.
- [ ] TransferGo — how to send money from Poland to Ukraine (uk, ru): slug send-money-from-poland-to-ukraine — compare TransferGo, Wise, bank transfer, Western Union (fees + rate on a checked date), {{offer:transfergo}}, promo WhatIfStack1
- [ ] TransferGo — how to send money from Germany to Ukraine (uk, ru): send-money-from-germany-to-ukraine
- [ ] Crypto exchange sign-up bonuses explained honestly (uk, ru, en): crypto-exchange-sign-up-bonuses — what «up to 10,000 USDT» really means, tasks, risks; links /bonuses/ and our partner exchanges
- [ ] Polymarket explained: how prediction markets work (en first, then es, pt, de… ONLY languages/countries where Polymarket is legally available — check its restricted-countries list and local regulators; where blocked, no partner link and say so): what-is-polymarket — 18+, risk of loss, not betting advice
- [ ] Telegram Wallet: how to buy crypto inside Telegram (uk, ru, en): buy-crypto-in-telegram-wallet — {{offer:tgwallet}}
- [ ] TransferGo — Czechia/Italy/Spain → Ukraine (uk, ru), one per run
- [ ] Freedom24 — how to buy US stocks from Europe (uk, ru, en)

## Log
| date | country | languages | slugs | notes |
|---|---|---|---|---|
| 2026-11-25 | Ukraine | uk, en | how-to-buy-bitcoin-in-ukraine | sample; law 10225-d passed 25 Nov — update tax section when signed |
| 2026-11-26 | Poland | pl, en | how-to-buy-bitcoin-in-poland | partners: OKX (OKX Europe, MiCA MFSA) + Kraken (MiCA CBI), both list PL, BLIK; Binance NOT linked (no new PL users since 1.07.2026, closes PL accounts 31.12.2026); Bybit EU named without link (partner link goes to global bybit.com); 3 presidential vetoes, no PL MiCA act — update when a crypto act passes |
| 2026-11-26 | Turkey | tr, en | how-to-buy-bitcoin-in-turkey | NO partner links: our /go/ links go to global entities and Law 7518 bars foreign platforms targeting TR residents; SPK-listed TR entities (BtcTurk, Paribu, Binance TR, OKX TR, Bybit TR…) named without links, «SPK listesinde» not «lisanslı»; tax: 0.03% + 10% stopaj withdrawn 27.03.2026 — update if reintroduced |
| 2026-11-27 | India | hi, en | how-to-buy-bitcoin-in-india | partners: Binance + Bybit (both FIU-IND registered, India not on their restricted lists; INR mostly via P2P); OKX NOT linked (left India 2024), MEXC left 28.02.2026, BingX/Gate/Kraken blocked or unregistered; tax 30%+cess, 1% TDS, unchanged by Budget 2026 / Income-tax Act 2025. Bonuses «in» added: Binance Referral Lite (feat, go binance, «up to» vouchers), Angel One, ZebPay (official pages); Bybit (conflicting «up to» figures), CoinDCX/CoinSwitch/Mudrex skipped (terms not confirmed officially) |
| 2026-11-27 | Japan | ja, en | how-to-buy-bitcoin-in-japan | NO partner links: Binance global left JP 1.12.2023 (→ Binance Japan), Bybit phasing out JP, OKX = separate OKJ, Kraken left 2023; FSA register 27 firms (31.10.2026); FIEA amendment passed 15.07.2026, promulgated 23.07.2026 — 20% separate tax expected 1.01.2028 (update when confirmed). Bonuses «jp» added (no feat, no partner): bitFlyer invite ¥1,500 BTC each, bitbank first deposit ¥1,000; Coincheck referral not confirmed on its own site — skipped |

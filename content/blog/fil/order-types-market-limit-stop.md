---
title: "Mga uri ng order: market, limit at stop order, hakbang-hakbang"
description: Ano ang ginagawa ng Market, Limit at Stop na button sa exchange o broker app, may halimbawang kuwenta at 3 pagkakamaling nagpapatalo sa baguhan.
date: 2026-11-28T09:05:00Z
category: learn
track: trading
step: 2
assets: btc, aapl
stat: 3
stat_label: pangunahing uri ng order — market (mabilis, hindi tiyak ang presyo), limit (tiyak ang presyo, hindi tiyak ang fill), stop (gumagana sa isang presyo)
---
**Anong mga uri ng order ang mayroon?** Ang **market order** ay bumibili o nagbebenta agad sa pinakamagandang presyong available ngayon. Ang **limit order** ay bumibili o nagbebenta lang sa presyo mo o mas maganda pa, kaya puwedeng hindi ito ma-fill kailanman. Ang **stop order** ay naghihintay hanggang umabot ang presyo sa antas na pinili mo, saka magpapadala ng market order — madalas gamitin para limitahan ang lugi.

> **Mahahalagang punto**
> - Market = bilis, pero hindi mo kontrolado ang eksaktong presyo. Limit = kontrolado mo ang presyo, pero walang garantiyang ma-fill.
> - Nagiging market order ang stop order kapag na-trigger. Sa mabilis na bagsak, puwede itong ma-fill nang malayo sa ilalim ng stop price mo.
> - Bago pindutin ang "Buy", laging tingnan ang tatlong bagay: uri ng order, dami at presyo.

## Ang tatlong button, sa simpleng salita

Kapag binuksan mo ang trade screen sa exchange o broker app, kadalasan may mga tab: **Market**, **Limit** at **Stop** (minsan "Stop-limit").

- **Market order.** "Bumili ngayon, kahit ano pa ang presyo." Halos agad itong na-fi-fill sa pinakamagandang alok (ang **ask**, ang pinakamababang presyong hinihingi ng nagbebenta). Sa malalaking coin at malalaking stock, kadalasan napakalapit ng presyo sa nakikita mo. Sa maliliit at matumal na market, puwedeng mas masama nang malaki.
- **Limit order.** "Bumili lang sa $X o mas mura" (o "magbenta lang sa $X o mas mataas"). Naghihintay ang order mo sa **order book** (ang listahan ng lahat ng naghihintay na buy at sell order) hanggang may tumanggap sa presyo mo. Kung hindi umabot doon ang presyo, walang mangyayari.
- **Stop order (stop-loss).** "Kapag bumagsak ang presyo sa $X, ibenta." Hanggang doon, hindi ito nakikita at walang ginagawa. Kapag tumama ang presyo sa $X, nagiging market order ito at nagbebenta sa susunod na available na presyo.
- **Stop-limit order.** Parang stop, pero nagiging *limit* order ito. Hindi ka magbebenta sa ilalim ng limit mo — pero sa mabilis na bagsak, baka hindi ito makabenta kahit kaunti.

## Halimbawa gamit ang simpleng numero

Sabihin nating **$100.00** ang presyo ng isang share. Ang pinakamagandang buyer ay nag-aalok ng $99.95 (ang **bid**) at ang pinakamagandang seller ay humihingi ng $100.05 (ang ask). Ang agwat na $0.10 ay ang **spread**.

1. Pinindot mo ang **Market buy, 10 shares** → magbabayad ka ng mga $100.05 bawat isa = **$1,000.50** dagdag ang anumang fee.
2. Naglagay ka ng **Limit buy, 10 shares sa $98** → walang mangyayari hanggang may seller na tumanggap ng $98. Kung umakyat na lang ang presyo sa $105, maghihintay lang ang order mo at wala kang mabibili.
3. Hawak mo ang shares at naglagay ka ng **Stop sa $90** → kapag bumagsak ang presyo sa $90, magpapadala ng market sell. Sa kalmadong market, baka makakuha ka ng $89.95. Pero kung may masamang balita bago magbukas ang market at nagbukas ang share sa $80, ma-trigger ang stop mo at magbebenta ka nang malapit sa **$80**, hindi $90.

Totoong nangyari ang ikatlong kaso. Noong 6 Mayo 2010 (ang "flash crash"), bumagsak ang mga presyo sa US sa loob ng ilang minuto. May mga stop order na na-fill nang malayo sa ilalim ng kanilang stop level, at may ilang share pa ngang na-trade sa isang sentimo, ayon sa ulat ng SEC at CFTC.

## Hakbang-hakbang: ilagay nang ligtas ang una mong limit order

Mag-practice muna gamit ang napakaliit na halaga.

1. **Hakbang 1 — Buksan ang trade screen** ng coin o stock at piliin ang **Buy**.
2. **Hakbang 2 — Pindutin ang tab na "Limit"**, hindi "Market".
3. **Hakbang 3 — I-type ang presyo mo.** Tingnan muna ang kasalukuyang presyo (halimbawa, {{price:btc}} ang Bitcoin ngayon). Ang limit na malayo sa ilalim nito ay baka hindi kailanman ma-fill.
4. **Hakbang 4 — I-type ang dami.** Tingnan kung ang kahon ay para sa bilang ng coin/share o para sa pera (USD, EUR). Ito ang pinakakaraniwang typo.
5. **Hakbang 5 — Suriin ang summary**: uri, presyo, dami, kabuuan, fee. Saka mag-confirm.
6. **Hakbang 6 — Hanapin ang order mo** sa "Open orders". Puwede mo itong i-cancel doon anumang oras hangga't hindi pa na-fi-fill. Kapag na-fill, lilipat ito sa "Order history".

> **⚠️ Mag-ingat**
> - **Market order sa matumal na market.** Sa maliliit na coin o labas sa normal na oras ng trading, puwedeng ma-fill ang market order nang mas masama kaysa sa presyo sa screen (tinatawag itong **slippage**). Gumamit ng limit order doon.
> - **Pag-aakalang garantisado ng stop-loss ang presyo mo.** Hindi: garantisado nito ang pagbenta, hindi ang presyo. Puwedeng itulak ng gap at crash ang fill nang mas mababa. Pinoprotektahan ng stop-limit ang presyo pero baka hindi ito makabenta.
> - **Pagkalito sa mga field.** Maling side (Sell imbes na Buy), sobrang isang zero sa dami, o presyong na-type sa maling kahon. Basahin ang summary bago mag-confirm.

## Ano ang ibig sabihin nito kung regular kang bumibili

Kung bumibili ka lang nang kaunti bawat linggo o buwan, hindi mo kailangan ng komplikadong order. Kadalasan ayos na ang market order sa malaki at liquid na asset, o limit order na bahagyang mas mataas sa kasalukuyang presyo kung gusto mo ng cap. Ang totoong resulta ay galing sa tagal sa market: ang $10 kada araw sa Bitcoin sa loob ng 3 taon ay nagkakahalaga na ngayon ng {{dca:btc:3}} (naglagay ka ng {{dcainv:3}}) — nakaraang resulta, hindi hula.

Susunod sa WhatIfStack: tingnan kung paano ginagalaw ng order book at ng malalaking trader ang market sa [trading hub]({lang}/trading/) at sa [Hyperliquid whale tracker]({lang}/trading/hyperliquid/), ikumpara ang fee sa mga [exchange]({lang}/exchanges/), at hanapin ang lahat ng aralin sa [Learn page]({lang}/learn/).

## Mga pinagmulan

- [Investor.gov (SEC): Mga uri ng order](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders)
- [Investor.gov (SEC): Investor bulletin — Stop, stop-limit at trailing stop order](https://www.investor.gov/additional-resources/news-alerts/alerts-bulletins/investor-bulletin-stop-stop-limit-trailing-stop)
- [FINRA: Mga uri ng order](https://www.finra.org/investors/investing/investment-products/stocks/order-types)
- [CFTC at SEC: Staff report tungkol sa mga pangyayari sa market noong 6 Mayo 2010](https://www.cftc.gov/MarketReports/StaffReportonMay6MarketEvents/staffreport050610marketevents.html)

*Hindi ito payo sa pamumuhunan.*

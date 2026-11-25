---
title: Paano mag-withdraw ng crypto mula sa exchange papunta sa sarili mong wallet: hakbang-hakbang
description: Ilipat nang ligtas ang coins sa sarili mong wallet: kopyahin ang tamang address, piliin ang parehong network, lagyan ng memo kung kailangan at mag-test muna.
date: 2026-11-25T09:40:00Z
category: learn
track: crypto
step: 6
assets: btc, eth, sol, bnb
stat: 1 network
stat_label: dapat iisa ang network ng exchange at ng wallet, kung hindi ay puwedeng mawala ang coins
---
**Paano mag-withdraw ng crypto papunta sa sarili mong wallet?** Sa wallet mo, kopyahin ang **receive address** ng coin. Pagkatapos, sa exchange, buksan ang **Withdraw**, i-paste ang address, piliin ang **parehong network** na gamit ng wallet mo, maglagay ng maliit na test amount at i-confirm gamit ang 2FA. Kapag dumating na ang test, saka ipadala ang natitira.

> **Mahahalagang punto**
> - Tatlong bagay ang dapat magtugma: ang **coin**, ang **address** at ang **network** (ang blockchain na dinadaanan ng coins, halimbawa Ethereum, BNB Smart Chain, TRON o Solana). Nagbababala ang Binance na ang coins na naipadala sa maling network ay puwedeng mawala nang tuluyan.
> - May mga coin (gaya ng XRP, XLM o ATOM) na kailangan din ng **memo** o **tag** (isang maikling numero na nagsasabi sa tatanggap kung kanino ang coins). Kung wala ito, puwedeng maipit ang transfer o mapunta sa ibang tao.
> - **Laging mag-test muna ng maliit na halaga.** Hindi na puwedeng i-cancel ang withdrawal kapag nakaalis na ang coins sa exchange.

Karugtong ang araling ito ng [Paano mag-set up ng recurring buy]({lang}/blog/how-to-set-up-a-recurring-buy/). Kung bakit baka gusto mo ng sariling wallet, ipinaliwanag sa [hot vs cold wallets]({lang}/blog/crypto-wallets-hot-vs-cold/).

## Bago ka magsimula

Dalawang bagay ang kailangan mo. Una, exchange account na may coins (protektado ng 2FA — tingnan ang [Paano mag-register sa crypto exchange]({lang}/blog/how-to-register-on-a-crypto-exchange/)). Ikalawa, sarili mong wallet app na naka-set up na, at ang **seed phrase** nito (ang 12 o 24 na lihim na salita na pang-restore ng wallet) ay nakasulat sa papel at nakatago offline. Huwag kailanman i-type ang seed phrase kahit saan pa — walang exchange, website o "support" na tao na mangangailangan nito.

## Hakbang 1 — Kopyahin ang receive address ng wallet mo

1. Buksan ang wallet app at i-tap ang **Receive** (minsan **Deposit**).
2. Piliin ang coin, halimbawa Bitcoin o USDT.
3. Kung itanong ng wallet, piliin ang network. Isulat kung alin ito — halimbawa "USDT sa TRON (TRC20)" o "USDT sa Ethereum (ERC20)".
4. I-tap ang **Copy** sa tabi ng address. Huwag itong i-type nang mano-mano.

Ang address ay mahabang linya ng mga letra at numero. Ang mga Bitcoin address ay kadalasang nagsisimula sa **bc1**, ang mga Ethereum at BNB Smart Chain address sa **0x**, ang mga TRON address sa **T**.

## Hakbang 2 — Buksan ang Withdraw sa exchange

Sa Binance app, ito ay **Assets → Spot → Send → Withdraw Crypto**; sa website ay **Wallet → Overview → Withdraw**. Ang ibang exchange ay may **Withdraw** button sa tabi ng bawat coin sa wallet o portfolio screen. Piliin ang parehong coin na pinili mo sa Hakbang 1.

## Hakbang 3 — I-paste ang address at piliin ang network

1. I-paste ang address sa **Address** field.
2. Ikumpara ang **unang 4 at huling 4 na character** sa wallet mo. May malware na pinapalitan ang kinopyang address ng address ng magnanakaw.
3. Piliin ang **network**. Dapat ito ang ipinakita ng wallet mo sa Hakbang 1. Puwedeng kusang magmungkahi ng network ang Binance — tingnan pa rin. Huwag pumili ng network dahil lang pinakamababa ang fee nito.
4. Kung may lumabas na **Memo** o **Tag** field at may ibinigay na memo ang wallet mo, punan ito. Kung walang memo na ipinapakita ang wallet mo, kadalasan ay hindi ito kailangan — pero i-double-check sa help pages ng wallet.

Tip: kung hindi ka sigurado, i-save ang address sa **Address Management** (address book) ng exchange. May **whitelist** din ang Binance: kapag in-on mo ito, sa mga naka-save na address lang puwedeng mapunta ang withdrawals — nakakatulong kung may magnakaw ng password mo.

## Hakbang 4 — Magpadala ng maliit na test

1. Maglagay ng maliit na halaga — bahagyang mas mataas sa minimum withdrawal na ipinapakita sa screen.
2. Tingnan ang mga linya ng **network fee** at **you will receive** (matatanggap mo). Pare-pareho ang fee kada withdrawal, kaya sa napakaliit na halaga ay puwede itong maging malaking bahagi.
3. Pindutin ang **Withdraw** at i-confirm gamit ang 2FA code o passkey. May mga exchange na nagpapadala rin ng confirmation e-mail — buksan ito at pindutin ang **Confirm**.

## Hakbang 5 — Tingnan kung dumating, saka ipadala ang natitira

1. Maghintay. Puwedeng tumagal ang transfer mula ilang segundo hanggang mga isang oras, depende sa network at sa dami ng transaksyon.
2. Sa exchange, buksan ang withdrawal history para makita ang status at ang **TxID** (ang ID ng transaksyon, na puwede mong hanapin sa isang block explorer site).
3. Kapag lumabas na ang coins sa wallet mo, ulitin ang Hakbang 2–4 para sa natitira. Nasa history o address book na ang address, kaya mas mabilis sa ikalawang beses.

Idagdag ang coins sa [portfolio mo]({lang}/me/) para masubaybayan ang halaga nila sa iisang lugar, saan man sila nakatago.

> **⚠️ Mag-ingat**
> - **Maling network.** Nasa maraming network ang USDT. Ang pagpapadala ng "TRC20" USDT sa address na "ERC20" lang ang tinatanggap ay puwedeng mangahulugang mawawala ang coins. Dalawang beses tingnan ang network.
> - **Nakalimutang memo o tag.** Ang mga exchange at wallet na nangangailangan ng memo ay hindi malalaman kung kanino ang dumating na coins kung wala ito. Ang pagbawi, kung posible man, ay mabagal at may bayad.
> - **Pekeng support at mga site na "address verification".** Walang lehitimong tao na hihingi ng seed phrase mo o magsasabing "i-verify" ang wallet sa pagpapadala ng coins. Mag-withdraw lang sa loob ng opisyal na app o website.

## Ano ang ibig sabihin kung regular kang bumibili

Kung bumibili ka nang paunti-unti bawat linggo o buwan, hindi mo kailangang mag-withdraw pagkatapos ng bawat bili — may fee ang bawat withdrawal. Maraming tao ang hinahayaang maipon ang coins sa exchange at paminsan-minsan lang inililipat sa sariling wallet, halimbawa isang beses kada quarter, sa isang mas malaking transfer. Halimbawa mula sa calculator namin: ang $10 kada araw sa Bitcoin sa loob ng 3 taon ({{dcainv:3}} lahat-lahat) ay naging {{dca:btc:3}} ({{dcaroi:btc:3}}). Nakaraang resulta ito, hindi hula. Nasa {{price:btc}} ang Bitcoin ngayon; tingnan ang [Bitcoin page]({lang}/btc/).

Nakaraang aralin: [Paano mag-set up ng recurring buy]({lang}/blog/how-to-set-up-a-recurring-buy/). Susunod na aralin: paano magbenta ng crypto at ilipat ang pera sa bank account mo. Ikumpara ang mga exchange sa aming [exchanges page]({lang}/exchanges/); lahat ng aralin ay nasa [Learn page]({lang}/learn/).

## Mga pinagkunan

- [Binance Support: How to deposit/withdraw cryptocurrency on Binance (na-update Marso 2026)](https://www.binance.com/en/support/faq/85a1c394ac1d489fb0bfac0ef2fceafd)
- [Binance Support: How to retrieve a crypto deposit with a wrong or missing tag/memo](https://www.binance.com/en/support/faq/40b87335db904481888ef406b105442b)
- [Binance.US Help Center: How to withdraw crypto from your Binance.US account (Hunyo 2026)](https://support.binance.us/en/articles/9842854-how-to-withdraw-crypto-from-your-binance-us-account)

*Hindi ito payo sa pamumuhunan.*

---
title: Paano magbasa ng price chart sa loob ng 2 minuto: 5 bagay na dapat silipin
description: Piliin ang time range, basahin ang linya o candles, silipin ang volume, gamitin ang log scale sa mahabang range, hanapin ang record high. Gabay sa baguhan.
date: 2026-11-23T19:00:00Z
category: learn
track: start
step: 5
assets: btc, spy, gold
stat: 5
stat_label: bagay na dapat silipin sa kahit anong price chart
---
**Paano magbasa ng price chart?** Una, piliin ang time range. Tapos tingnan kung saan nagsimula ang presyo at nasaan ito ngayon. Pagkatapos, silipin kung gaano kalaki ang pagtaas at pagbaba, at gaano karami ang na-trade. Sapat na iyan para maintindihan ang 90% ng sinasabi ng chart — walang formula na kailangan.

> **Mahahalagang punto**
> - **Nakaraan** lang ang ipinapakita ng chart. Sinasabi nito kung gaano kalayo gumalaw ang asset at gaano kagulo ang biyahe, hindi kung ano ang mangyayari bukas.
> - Ang iisang asset ay puwedeng mukhang bumagsak sa 1-week chart pero tuloy-tuloy na umaakyat sa 5-year chart. Laging silipin muna ang time range.
> - May live chart ang bawat asset page sa WhatIfStack. Ang Bitcoin ay nasa {{price:btc}} ngayon, {{chg1y:btc}} sa loob ng 12 buwan; ang record high nito ay {{ath:btc}} ({{athd:btc}}).

Karugtong ang araling ito ng [Diversification: huwag ilagay lahat sa iisang coin]({lang}/blog/diversification-dont-put-everything-in-one-coin/). Buksan ang [Bitcoin page]({lang}/btc/) sa ibang tab at sumabay.

## Step 1 — Piliin ang time range

Sa ilalim ng chart may mga button na gaya ng **1D, 5D, 1M, 3M, 6M, YTD, 1Y, 5Y, All**. Ibig sabihin nito ay 1 araw, 5 araw, 1 buwan, at iba pa (YTD = "year to date", mula 1 Enero; All = lahat ng data).

- Kung bumibili ka nang paunti-unti bawat buwan sa loob ng maraming taon, tingnan muna ang **1Y** at **5Y**.
- Ang maiikling range (1D, 5D) ay kadalasang "ingay" lang — maliliit na taas-baba na hindi mahalaga sa pangmatagalang bumibili.

Tip: pindutin ang **1M**, tapos ang **5Y**. Kita mo kung gaano kaiba ang itsura ng iisang asset? Iyan ang pinakamahalagang aral tungkol sa charts.

## Step 2 — Ikumpara ang simula at ang dulo

Tingnan ang kaliwang gilid (presyo sa simula ng range) at ang kanang gilid (presyo ngayon). Mas mataas ba o mas mababa ang kanan? Iyan ang pagbabago sa panahong iyon. Sa mga asset page namin, hindi mo kailangang manghula: ipinapakita ng mga card sa ilalim ng chart ang pagbabago sa porsiyento, at ipinapakita ng calculator na "Magkano sana ang meron ako" ang resulta sa pera.

## Step 3 — Basahin ang candles

Bilang default, **candles** (maliliit na bar) ang ipinapakita ng chart namin. Bawat candle ay isang yugto — sa daily setting, isang araw.

- **Berdeng** candle: nagsara ang presyo nang **mas mataas** kaysa sa pagbukas nito noong araw na iyon.
- **Pulang** candle: nagsara ang presyo nang **mas mababa** kaysa sa pagbukas.
- Ang makapal na bahagi (ang "body") ay mula sa opening price hanggang closing price.
- Ang manipis na linya sa itaas at ibaba (ang "wicks") ay ang pinakamataas at pinakamababang presyo noong araw na iyon.

Kapag mahaba ang wicks, ibig sabihin ay maraming talon-talon ang presyo sa loob ng araw. Hindi mo na kailangan ng higit pa rito — ang mga pattern na may magagarang pangalan ay para sa mga trader, at tatalakayin namin iyon mamaya sa trading folder.

## Step 4 — Silipin ang volume

Ang maliliit na bar sa ibaba ng chart ay ang **volume** — kung gaano karami ng asset ang na-trade sa bawat yugto. Kapag malaki ang galaw at mataas ang volume, maraming tao ang kasali. Kapag malaki ang galaw pero maliit na maliit ang volume, hindi ito gaanong maaasahan: ilang trade lang ay kayang itulak pataas o pababa ang presyo ng maliit na coin.

## Step 5 — Sa mahahabang range, lumipat sa log scale

Sa kanang ibabang sulok ng chart may button na **log**. Sa normal ("linear") na scale, ang galaw mula $1 papuntang $2 ay mukhang maliit kumpara sa galaw mula $100 papuntang $200, kahit pareho silang +100%. Sa **log scale**, pareho ang laki ng itsura ng parehong porsiyentong galaw. Para sa 5-year o "All" na chart ng mabilis lumagong asset gaya ng Bitcoin, mas tapat na larawan ng nakaraan ang ipinapakita ng log scale.

Panghuli, hanapin ang **record high** — ang pinakamataas na punto sa "All" chart. Ipinapakita rin ito sa mga card ng pages namin. Ang Bitcoin ay {{fromath:btc}} ang layo rito ngayon. Hindi mali ang bumili mismo sa record, pero paalala ito kung gaano kalalim puwedeng bumagsak ang presyo pagkatapos.

> **⚠️ Mag-ingat**
> - **Pagbasa ng hinaharap sa isang linya.** "Tumaas na nang 3 buwan, kaya tataas pa" ang pinakakaraniwang pagkakamali ng baguhan. Kasaysayan ang chart, hindi hula.
> - **Paghusga batay sa 1-day chart.** Halos walang sinasabi ang isang pulang araw tungkol sa asset na balak mong hawakan nang ilang taon. Mag-zoom out muna.
> - **Pagtitiwala sa screenshot ng mga estranghero.** Ang mga chart na pino-post sa group chat ay puwedeng putulin sa kahit anong range para patunayan ang kahit ano. Buksan mo mismo ang chart sa isang mapagkakatiwalaang site.

## Ano ang ibig sabihin kung regular kang bumibili

Kung pare-parehong halaga ang binibili mo bawat buwan, pabor pa sa iyo ang taas-baba sa chart: sa mga pulang bahagi, mas maraming unit ang nabibili ng parehong pera. Halimbawa, $10 kada araw sa Bitcoin sa loob ng 5 taon ({{dcainv:5}} lahat-lahat) ay naging {{dca:btc:5}} ({{dcaroi:btc:5}}); sa S&P 500 ay {{dca:spy:5}} at sa ginto ay {{dca:gold:5}}. Nakaraang resulta ito, hindi hula. Ikumpara sila nang magkatabi sa [compare tool]({lang}/compare/) at itala ang sarili mong mga bili sa [iyong portfolio]({lang}/me/).

Susunod na aralin: ano ang Bitcoin, sa simpleng salita. Nasa [Learn page]({lang}/learn/) ang lahat ng aralin.

## Mga pinagmulan

- [TradingView: Introduction to candlestick charts and patterns](https://www.tradingview.com/support/solutions/43000745269-introduction-to-candlestick-charts-and-patterns/)
- [TradingView education: logarithmic scale](https://www.tradingview.com/education/logarithmic/)
- [Investor.gov (US SEC): Dollar-cost averaging](https://www.investor.gov/introduction-investing/investing-basics/glossary/dollar-cost-averaging)

*Hindi ito investment advice. Ipinapaliwanag ng araling ito kung paano magbasa ng chart at hindi nagrerekomendang bumili ng anumang asset.*

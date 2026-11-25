---
title: The Graph (GRT) sa simpleng paliwanag: indexing protocol para sa blockchain data, live mula 2020, sa Ethereum at Arbitrum
description: The Graph sa simpleng salita: paano ginagawang mabilis na query ng indexer ang blockchain data, ano ang gamit ng GRT, staking, kuwento, karibal at panganib.
date: 2026-11-25
kind: analysis
---
Ang **The Graph** ay madalas tawaging "Google ng mga blockchain": inaayos nito ang hilaw na data ng blockchain para mahanap ng mga app ang kailangan nila sa loob ng ilang millisecond. Ginagamit ito ng mga wallet, exchange at DeFi app para ipakita ang mga balanse, trade at presyo nang hindi nagpapatakbo ng sarili nilang data server. Ang token nitong **GRT** ang pambayad sa trabahong iyon at nagbibigay-seguridad sa network, at nagkakahalaga ito ngayon ng {{mcap:grt}} ({{rank:grt}} sa mga cryptocurrency).

> **Mahahalagang punto**
> - Naging live ang network noong Disyembre 2020 na may 10 bilyong GRT; may bagong token na inilalabas taon-taon bilang gantimpala, kaya walang nakapirming limit ang supply.
> - Ang pinakamataas nitong presyo ay {{ath:grt}} ({{athd:grt}}); ngayon ang presyo ay {{fromath:grt}} mula roon.
> - Ang GRT ay isang work token: kailangan itong i-stake ng mga indexer para makapagbigay ng data, at dito binabayaran ng mga app ang query fees.
> - Taya ito sa demand para sa blockchain data, hindi isang pera — madalas na magkahiwalay ang galaw ng paggamit at ng presyo.

## Paano ito gumagana

Mabagal at mahirap ang direktang pagbasa ng data mula sa blockchain. Sa The Graph, inilalarawan ng mga developer ang data na kailangan nila sa isang bukas na "subgraph", halimbawa ang bawat trade sa isang decentralised exchange. Ang mga **indexer** — mga independiyenteng operator na nagpapatakbo ng server — ang nagpoproseso ng mga subgraph na ito at sumasagot sa mga query ng app, kapalit ng fees at bagong labas na GRT. Ang mga **curator** ang nagsasabi kung aling mga subgraph ang sulit i-index, at ang mga **delegator** ay nagpapahiram ng kanilang GRT sa mga indexer na pinagkakatiwalaan nila kapalit ng bahagi ng gantimpala. Puwedeng mawalan ng bahagi ng stake ang indexer na nagbibigay ng maling data ("slashing"). Sinusuportahan na ngayon ng The Graph ang dose-dosenang blockchain, at mula 2024 tumatakbo ang mga gantimpala at bayad nito sa Arbitrum, isang layer 2 ng Ethereum, para manatiling mababa ang gastos. Noong 2025, sinimulang ilunsad ng proyekto ang **Horizon**, isang upgrade na nagpapahintulot sa parehong staking system na magbigay-seguridad sa mga bagong uri ng data service.

## Para saan ginagamit ang token

May tatlong trabaho ang GRT. Kailangan itong i-stake ng mga indexer bago sila makapagtrabaho, kaya malaking bahagi ng supply ang naka-lock. Sa GRT nagbabayad ang mga app para sa mga query (madalas na awtomatikong kino-convert mula sa stablecoin o bayad gamit ang card). At puwede itong i-delegate ng mga may hawak para kumita ng bahagi ng gantimpala nang hindi nagpapatakbo ng server. Isang maliit na bahagi ng query fees at staking tax ang sinusunog (burn), habang ang bagong labas na mga 3% kada taon ay napupunta sa mga indexer at delegator. Kung tataas ang halaga ng GRT ay nakasalalay sa kung mas mabilis lalago ang bayad na demand para sa data kaysa sa bagong supply.

## Ang mga numero ngayon

- Presyo ngayon: {{price:grt}}
- Pinakamataas na presyo: {{ath:grt}} ({{athd:grt}}), {{fromath:grt}} mula roon
- Halaga sa merkado: {{mcap:grt}} ({{rank:grt}} sa mga cryptocurrency)
- Pagbabago ng presyo sa loob ng 12 buwan: {{chg1y:grt}}
- $10 kada araw sa loob ng 5 taon: {{dca:grt:5}} mula sa {{dcainv:5}} na inilagay ({{dcaroi:grt:5}})

## Ang kuwento nito hanggang ngayon

Sinimulan ang The Graph noong 2018 nina Yaniv Tal, Brandon Ramirez at Jannis Pohlmann, na ang kompanya ay naging Edge & Node kalaunan. Sa loob ng maraming taon, nagpatakbo ito ng libreng "hosted service" na inaasahan ng maraming Ethereum app. Naging live ang decentralised network at ang GRT token noong 17 Disyembre 2020, at sa crypto boom ay umakyat ang GRT sa mga $2.84 noong Pebrero 2021. Pagkatapos ay bumagsak ito nang higit 90% sa buong 2021 at 2022. Noong 2023 at 2024, inilipat ng proyekto ang mga gantimpala nito sa Arbitrum at isinara ang hosted service noong Hunyo 2024, kaya napilitang lumipat ang lahat ng user sa bayad na network. Panandaliang itinaas ng rally ng mga AI token noong unang bahagi ng 2024 ang GRT, pero bumagsak ito kalaunan sa mga bagong pinakamababang presyo.

## Mga alternatibo

Nakikipagkumpitensya ang The Graph sa mga indexing company at protocol gaya ng Goldsky, SubQuery at Covalent, at sa mga blockchain data API ng Alchemy at QuickNode, na mas simple para sa maraming developer. May ilang malalaking app na nagpapatakbo na lang ng sarili nilang indexer. Sa mga token na may kinalaman sa blockchain data, madalas ikumpara sa GRT ang [Chainlink]({lang}/link/) at [Pyth Network]({lang}/pyth/), kahit na naghahatid sila ng price feeds sa mga smart contract sa halip na paghahanap sa lumang data.

## Pangunahing panganib

- **Bagong supply:** nagdaragdag ng bagong GRT ang taunang paglalabas ng token, at madalas ibenta ng mga indexer ang kanilang gantimpala para matustusan ang gastos sa server.
- **Mahinang ugnayan sa paggamit:** matagal nang maliit ang query fees kumpara sa mga gantimpala, kaya hindi kusang tumataas ang presyo dahil lang marami ang gumagamit.
- **Kompetisyon:** mabilis at mura ang mga sentralisadong data provider, at madaling lumipat sa kanila ang mga app.
- **Pagdepende sa iisang kompanya:** ang Edge & Node at ang The Graph Foundation pa rin ang gumagabay sa malaking bahagi ng development.
- **Regulasyon:** iba-iba sa bawat bansa ang mga patakaran sa staking token at sa mga gantimpala nito, at puwedeng magbago ang mga ito.

## Ano ang ibig sabihin nito kung regular kang bumibili

Sa halos buong buhay nito, malayo sa ibaba ng peak nito noong 2021 ang GRT, kaya ang regular na bumibili ay patuloy na nakakuha ng mas maraming token sa mas mababang presyo — na magbubunga lang kung babawi ang presyo. Ang regular na pagbili ng nakapirming halaga ay nagkakalat ng panganib sa maling timing pero hindi nito inaalis ang panganib na malugi. Maraming tao ang nagtatabi lang ng ganitong token bilang maliit na bahagi ng kanilang ipon. Hindi garantiya ng nakaraang resulta ang kita sa hinaharap.

*Hindi ito payo sa pamumuhunan.*

## Mga pinagmulan

- [Tungkol sa The Graph (dokumentasyon ng The Graph)](https://thegraph.com/docs/en/about/)
- [Gabay sa pagpapatupad ng Horizon: ano ang nagbago para sa mga kalahok sa network (blog ng The Graph)](https://thegraph.com/blog/horizon-implementation-guide/)
- [Presyo, market cap at pinakamataas na presyo ng The Graph (CoinGecko)](https://www.coingecko.com/en/coins/the-graph)

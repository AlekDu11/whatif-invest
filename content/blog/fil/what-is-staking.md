---
title: Ano ang crypto staking at ligtas ba ito?
description: Ano ang crypto staking? Simpleng paliwanag kung paano ito gumagana, lock-up periods, staking sa exchange vs on-chain, at ang totoong panganib bago mag-stake.
date: 2026-11-16
category: guides
assets: eth, sol, ada, dot, atom
---
**Ano ang staking?** Ang staking ay ang pag-lock ng crypto coins para tumulong na patakbuhin ang isang blockchain — at makatanggap ng bagong coins bilang reward. Madalas itong ikinukumpara sa savings account, pero ibang-iba ang takbo nito at may sarili itong mga panganib.

Ipinapaliwanag ng guide na ito kung paano gumagana ang staking, ano ang ibig sabihin ng "lock-up", paano naiiba ang staking sa exchange sa staking on-chain, at ano ang puwedeng magkamali.

## Paano gumagana ang staking

Maraming modernong blockchain — Ethereum, Solana, Cardano, Polkadot, Cosmos at iba pa — ang gumagamit ng sistemang tinatawag na **proof of stake**. Imbes na gumamit ng kuryente para i-secure ang network (tulad ng mining ng Bitcoin), umaasa sila sa **validators**: mga computer na nagche-check ng transactions at nagdadagdag ng bagong blocks.

Para maging validator, kailangan mong maglagay ng coins bilang garantiya na magiging tapat ka. Sa simpleng hakbang:

1. Ini-lock (sine-stake) mo ang coins sa network — ikaw mismo ang magpapatakbo ng validator o ide-delegate mo sa isa.
2. Kinukumpirma ng validators ang transactions at gumagawa ng blocks.
3. Nagbabayad ang network ng rewards sa bagong coins, kasama ang bahagi ng transaction fees.
4. Kapag nandaya ang validator o madalas na offline, puwedeng bawasan ang bahagi ng stake. Tinatawag itong **slashing**.

Ang Bitcoin mismo ay hindi puwedeng i-stake sa ganitong paraan — proof of work ang gamit nito. Ang mga produktong nag-aalok ng "Bitcoin yield" ay kadalasang lending o ibang scheme, hindi staking.

## Saan galing ang staking rewards

Hindi libreng pera ang rewards. Kadalasang galing ito sa:

- **Bagong coins** na ginagawa ng network (inflation ng coin supply),
- **Transaction fees** na binabayaran ng users.

Mahalaga ito: kung gumagawa ang network ng bagong coins nang, halimbawa, 5% kada taon at kumikita ka ng 5%, kadalasang napapanatili mo lang ang bahagi mo sa network — hindi ka talaga yumayaman. At sa coin mismo binabayaran ang rewards — kapag bumagsak ang presyo nito, puwede pa ring lumiit nang husto ang kabuuang halaga mo.

Palaging nagbabago ang reward rates depende sa dami ng nag-i-stake at sa patakaran ng network. Ituring ang anumang ina-advertise na porsiyento bilang snapshot, hindi pangako.

## Lock-ups at unbonding: kailan mo makukuha ulit ang coins mo

Kadalasan, kapag nag-stake ka, hindi agad magagamit ang coins mo. Iba-iba ang patakaran ng bawat network:

- **Ethereum** — posible na ang withdrawals mula sa "Shapella" upgrade noong 2023, pero dumadaan sa pila ang pag-exit, na puwedeng tumagal ng ilang araw hanggang ilang linggo kapag maraming sabay-sabay na umaalis.
- **Solana** — epektibo ang unstaking sa dulo ng isang "epoch", kadalasan mga dalawang araw.
- **Cosmos at Polkadot** — may "unbonding" period na ilang linggo, kung saan walang kinikita ang coins at hindi mo ito maibebenta.
- **Cardano** — nananatili ang coins sa wallet mo at hindi naka-lock.

Bakit mahalaga: kapag bumagsak ang market habang nasa unbonding period ka, hindi ka makakabenta. Laging i-check ang eksaktong kasalukuyang patakaran ng coin bago mag-stake.

## Staking sa exchange vs on-chain staking

May dalawang pangunahing paraan ng pag-stake para sa ordinaryong tao.

### Staking sa exchange (custodial)

Pipindutin mo ang "Stake" o "Earn" sa app ng exchange at sila na ang bahala sa technical na trabaho.

- ✅ Napakadali, okay kahit maliit na halaga, walang wallet setup.
- ❌ Hawak ng exchange ang coins mo. Kapag bumagsak ito, na-hack o nag-freeze ng withdrawals, nanganganib ang coins mo.
- ❌ Kumukuha ang exchange ng bahagi ng rewards bilang fee.
- ❌ Ang ilang "earn" products ay lending pala, hindi staking — ibang-iba ang panganib.

Masusing binabantayan ng mga regulator ang mga serbisyong ito. Noong 2023, kinasuhan ng US SEC ang Kraken dahil sa staking program nito; nagbayad ang Kraken ng $30 million at isinara ang serbisyo para sa US customers. Noong 2025, sinabi ng SEC staff na ang ilang anyo ng direktang "protocol staking" ay hindi securities transactions. Iba-iba ang patakaran sa bawat bansa at patuloy na nagbabago.

### Staking on-chain (non-custodial)

Itinatabi mo ang coins sa sarili mong wallet at ide-delegate sa isang validator, o ikaw mismo ang magpapatakbo ng validator.

- ✅ Hawak mo ang keys mo; walang makakapag-freeze ng account mo.
- ✅ Kadalasang mas mababa ang fees.
- ❌ Mas technical: maling address, phishing at masamang validators ay problema mo.
- ❌ Para magpatakbo ng sariling Ethereum validator, kailangan ng 32 ETH at maaasahang hardware.

### Liquid staking

Gitnang opsyon: nag-i-stake ka sa pamamagitan ng isang protocol at makakatanggap ka ng token na kumakatawan sa naka-stake mong coins (halimbawa, isang "staked ETH" token). Puwede mo itong i-trade habang kumikita ng rewards ang coins mo. Ang kapalit ay dagdag na **smart-contract risk** at ang posibilidad na mas mababa ang trading price ng token kaysa sa halaga ng coins sa likod nito.

## Ang mga pangunahing panganib ng staking

Ligtas ba ang staking? Mas mababa ang panganib nito kaysa sa maraming "high yield" na crypto product, pero hindi ito kailanman risk-free:

1. **Price risk.** Ito ang pinakamalaki. Halos walang saysay ang reward na ilang porsiyento kung bumagsak ang coin nang 50%. Tingnan kung gaano kagalaw ang mga coin sa [Ethereum page]({lang}/eth/) o [Solana page]({lang}/sol/).
2. **Lock-up risk.** Baka hindi ka makabenta habang may crash.
3. **Platform risk.** Puwedeng bumagsak ang exchanges at lending platforms. Nang bumagsak ang Celsius noong 2022, nawalan ng access sa kanilang coins ang users ng "earn" program nito.
4. **Slashing.** Puwedeng mawalan ng bahagi ng stake ang validator na nagkamali — kasama ang delegated coins sa ilang network.
5. **Smart-contract risk** sa liquid staking at DeFi.
6. **Buwis.** Sa maraming bansa, taxable income ang staking rewards pagkatanggap. Alamin ang lokal na patakaran.
7. **Scams.** Karaniwan ang pekeng staking sites at mga alok na "guaranteed 20% kada buwan". Basahin ang guide namin kung [paano iwasan ang crypto scams]({lang}/blog/how-to-avoid-crypto-scams/).

## Maingat na checklist bago mag-stake

- I-stake lang ang coins na plano mo na talagang hawakan nang matagal.
- I-check ang unbonding period at kung baka kailanganin mo ang pera nang mas maaga.
- Alamin kung sino ang may hawak ng coins mo — ikaw o isang platform.
- Ikumpara ang fees: gaano kalaking bahagi ng rewards ang kinukuha ng platform?
- Iwasan ang mga alok na napakataas na fixed return — gumagalaw ang totoong staking rewards.
- Magsimula nang maliit at subukan munang mag-withdraw.

Hindi binabago ng staking ang pangunahing tanong: bagay ba ang coin mismo sa pangmatagalang plano mo? Ang regular na pagbili, tulad ng DCA, ay tungkol sa presyo ng asset sa loob ng maraming taon — subukan ito sa aming [DCA calculator]({lang}/compare/). Ganito sana ang naging resulta ng $10 kada araw sa Ethereum sa loob ng 5 taon — nang walang staking rewards: {{dca:eth:5}} mula sa {{dcainv:5}} na na-invest ({{dcaroi:eth:5}}).

{{card:eth}}
{{card:sol}}

## FAQ

### Pareho ba ang staking sa pagkita ng interes?

Hindi. Galing sa nangungutang ang interes; ang staking rewards ay galing sa network mismo dahil tumutulong kang i-secure ito. Sa coin binabayaran ang rewards, kaya gumagalaw ang halaga nito kasabay ng presyo.

### Puwede ba akong malugi sa staking?

Oo. Puwedeng bumagsak ang presyo ng coin, puwedeng bumagsak ang platform, at sa bihirang kaso, puwedeng bawasan ng slashing ang stake mo. Hindi ka pinoprotektahan ng rewards sa pagbaba ng presyo.

### Puwede bang i-stake ang Bitcoin?

Hindi natively — proof of work ang gamit ng Bitcoin. Ang mga alok na "Bitcoin yield" ay kadalasang lending o ibang produkto na may ibang panganib.

### Alin ang mas mabuti, staking sa exchange o sa wallet?

Mas simple ang staking sa exchange; sa wallet staking, ikaw ang may kontrol sa keys mo. Depende ang tamang pagpili sa kung gaano ka komportable mag-manage ng wallet — tingnan ang guide namin sa [hot at cold wallets]({lang}/blog/crypto-wallets-hot-vs-cold/).

## Sources

- [ethereum.org — Ethereum staking](https://ethereum.org/en/staking/)
- [ethereum.org — Staking withdrawals](https://ethereum.org/en/staking/withdrawals/)
- [Solana — Staking](https://solana.com/staking)
- [US SEC — Ititigil ng Kraken ang staking program, magbabayad ng $30 million (2023)](https://www.sec.gov/news/press-release/2023-25)
- [Skadden — SEC: ang ilang protocol staking activities ay hindi securities transactions (2025)](https://www.skadden.com/insights/publications/2025/06/sec-certain-protocol-staking-activities-are-not-securities-transactions)

*Hindi ito investment advice. Ipinapaliwanag ng guide na ito kung paano gumagana ang staking at hindi nagrerekomenda ng anumang coin, platform o validator.*

---
title: Ano ang DEX at ano ang pinagkaiba nito sa crypto exchange?
description: Ano ang DEX? Simpleng gabay sa decentralised exchanges: AMM, liquidity pools, wallets, gas fees, at ang pros at cons kumpara sa centralised exchange (CEX).
date: 2026-11-16
category: guides
assets: eth, sol, uni
---
**Ano ang DEX?** Ang DEX (decentralised exchange) ay isang set ng smart contracts sa blockchain na nagpapahintulot sa iyong ipagpalit ang isang token sa iba nang direkta mula sa sarili mong wallet. Walang kumpanyang humahawak ng pera mo, walang account at kadalasan walang ID check. Kilalang halimbawa ang Uniswap sa Ethereum, at ang Raydium, Orca at Meteora sa Solana.

Ang karaniwang crypto exchange gaya ng Binance, Coinbase o Kraken ay isang **CEX** (centralised exchange): kumpanyang humahawak ng pondo mo, nagtutugma ng buyers at sellers sa sarili nitong sistema at kailangang sumunod sa mga financial rule.

## Paano gumagana ang DEX

### Automated market makers (AMMs)

Karamihan sa mga DEX ay walang order book na may buyers at sellers. Sa halip, gumagamit sila ng **automated market maker**, isang formula na nagtatakda ng presyo.

Ang classic na bersyon, na gamit ng Uniswap v2, ay ang "constant product" rule: may dalawang token ang pool, at ang dami ng token A na pinarami sa dami ng token B ay kailangang manatiling pareho matapos ang bawat trade. Kapag bumili ka ng token A, nagdadagdag ka ng token B sa pool at nag-aalis ng token A, kaya nagiging mas kaunti ang A sa pool at tumataas ang presyo nito.

Hindi mo kailangang mag-math. Ang pangunahing ideya: **habang lumalaki ang pool, lumiliit ang galaw ng presyo dahil sa trade mo.**

### Liquidity pools

Ang mga token sa pool ay galing sa **liquidity providers**, mga taong nagdedeposito ng pares ng token at kumikita ng bahagi ng trading fees (madalas 0.05–1% bawat swap). Ang panganib nila ay ang paglayo ng presyo ng dalawang token, na puwedeng magpalugi sa kanila kumpara kung hinawakan lang nila ang mga ito ("impermanent loss").

Para sa mga bagong inilunsad na token, kadalasang ang creator ang gumagawa ng unang pool. Kaya mahalaga ang liquidity lock: kung sino ang may kontrol sa pool ay kayang i-withdraw ito.

### Ang wallet mo ang account mo

Para gumamit ng DEX, kino-connect mo ang isang self-custody wallet gaya ng MetaMask (Ethereum at mga katulad na chain) o Phantom (Solana). Ang bawat trade ay transaction na ikaw mismo ang pumipirma. Ang **seed phrase** mo ang master key: mawala ito at mawawala ang pera; ibahagi ito at kukunin ng iba ang pera.

### Gas at fees

Bawat DEX trade ay nagbabayad ng network fee, na tinatawag na **gas** sa Ethereum. Sa Ethereum, tumataas ito kapag abala ang network; ang Layer-2 networks at Solana ay kadalasang mas mura nang husto, at ang base fee ng Solana ay 0.000005 SOL bawat signature. Bukod sa gas, nagbabayad ka ng pool fee, at puwede kang tamaan ng **slippage** at **price impact** sa maliliit o mabilis gumalaw na token.

## DEX vs CEX: ang mga pangunahing pagkakaiba

- **Sino ang humahawak ng pondo mo:** sa DEX, ikaw (ang wallet mo); sa CEX, ang exchange.
- **Account at ID check:** kadalasan walang kailangan sa DEX; sa CEX, kailangan ang identity check (KYC).
- **Pagpipiliang token:** halos kahit anong token ay nasa DEX, pati ang mga bagong-bago; sa CEX, piling token lang ang naka-list.
- **Pagbili gamit ang card o bangko:** kadalasan hindi direktang posible sa DEX; standard sa CEX.
- **Fees:** DEX, gas, pool fee at slippage; CEX, trading fee, spread at withdrawal fee.
- **Tulong kapag may problema:** walang support line ang DEX; may customer support ang CEX at minsan may protection schemes.
- **Pangunahing panganib:** DEX, scam tokens, maling approvals at sarili mong pagkakamali; CEX, hacks, account freeze at pagkalugi ng exchange.

## Pros ng DEX

- **Self-custody.** Walang makakapag-freeze ng account mo o makakawala ng pera mo sa isang bankruptcy.
- **Bukas sa lahat.** Kahit sino na may wallet ay puwedeng mag-trade, mula halos kahit saan.
- **Nauuna ang bagong tokens.** Lumalabas ang mga token sa DEX bago pa (o kahit walang) listing sa exchange.
- **Transparency.** Kita sa blockchain ang pools, trades at holders.

## Cons ng DEX

- **Ikaw ang bangko.** Isang pagkakamali lang, gaya ng maling address, pekeng site o mapanganib na approval, at mawawala nang tuluyan ang pondo.
- **Scam tokens.** Kahit sino ay kayang gumawa ng token at pool sa loob ng ilang minuto. Karamihan sa mga bagong token ay nawawalan ng halos lahat ng halaga; tingnan ang aming [rug pull checklist]({lang}/blog/how-to-spot-a-rug-pull/).
- **Nakatagong gastos.** Puwedeng mas mahal ang slippage at price impact kaysa sa nakikitang fee.
- **Walang madaling on-ramp.** Kadalasan kailangan mo munang bumili ng crypto sa CEX at ipadala ito sa wallet mo.
- **Smart-contract risk.** Nagdulot na ng malalaking lugi ang mga bug o hack sa DEX code.

## Alin ang dapat gamitin ng baguhan?

Marami ang gumagamit ng pareho: isang lisensyadong CEX para gawing crypto ang lokal na pera, at isang DEX para sa mga token na on-chain lang available. Para sa regular at pangmatagalang pagbili ng malalaking asset gaya ng Bitcoin o Ethereum, kadalasang mas simple ang CEX na mababa ang fees; ikumpara ang mga opsyon sa aming [exchanges page]({lang}/exchanges/).

Kung gusto mong subukan ang memecoins at iba pang on-chain token, magsimula sa napakaliit na halaga, sa hiwalay na wallet, at sa mga pinakamatatag na coin sa aming [memecoins page]({lang}/memes/). Ipinapakita ng aming step-by-step na gabay na [paano bumili ng memecoin sa Solana]({lang}/blog/how-to-buy-memecoins-on-solana/) ang buong proseso, kasama ang mga tool gaya ng [GMGN](/go/gmgn?from=blog&l=fil).

## Mga karaniwang termino sa DEX

- **Swap**: pagpapalit ng isang token sa iba.
- **Pair**: ang dalawang token sa isang pool, gaya ng SOL/USDC.
- **Slippage tolerance**: ang pinakamalaking pagbabago sa presyo na tatanggapin mo.
- **Approve**: pahintulot sa isang contract na ilipat ang isang token mula sa wallet mo (pangunahin sa mga Ethereum-style chain). I-revoke ang mga lumang approval na hindi mo na kailangan.
- **Aggregator**: serbisyong hinahati ang trade mo sa ilang DEX para sa mas magandang presyo, gaya ng Jupiter sa Solana o 1inch sa Ethereum.

## FAQ

### Mas ligtas ba ang DEX kaysa CEX?

Inaalis nito ang panganib na mawala o ma-freeze ng exchange ang pondo mo, pero dinadagdag nito ang panganib ng sarili mong pagkakamali at ng scam tokens. Walang isa sa kanila ang walang panganib.

### Kailangan ko ba ng ID para gumamit ng DEX?

Kadalasan hindi, dahil nagte-trade ka mula sa sarili mong wallet. Pero sakop ka pa rin ng mga lokal na batas at buwis.

### Bakit pumalya ang DEX trade ko?

Mga karaniwang dahilan: kulang ang native coin pambayad ng gas, masyadong mababa ang slippage para sa mabilis gumalaw na presyo, o token na humaharang sa pagbebenta.

### May buwis ba ang DEX trades?

Sa maraming bansa, oo; ang pag-swap ng isang token sa iba ay puwedeng ituring na pagbebenta. Magtabi ng record ng mga trade mo.

## Sources

- [Paano gumagana ang Uniswap (Uniswap docs)](https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works)
- [Gas at fees (ethereum.org)](https://ethereum.org/en/developers/docs/gas/)
- [Solana docs: fee structure](https://solana.com/docs/core/fees/fee-structure)

*Hindi ito investment advice. Ipinapaliwanag ng gabay na ito kung paano gumagana ang DEX at hindi ito nagrerekomenda ng kahit anong platform o token.*

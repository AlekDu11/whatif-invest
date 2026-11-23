---
title: Paano gumawa ng Binance Wallet at bumili ng memecoin: step by step
description: Gumawa ng Binance Wallet sa Binance app, i-back up ito, maglipat ng coins, hanapin ang token gamit ang contract at mag-swap, kasama ang safety checks.
date: 2026-11-23T12:30:00Z
category: learn
track: memes
step: 5
assets: bnb, sol, doge
stat: 3
stat_label: piraso ng key ang nagpoprotekta sa Binance Wallet; 2 ang kailangan para makapasok
---
**Paano gumawa ng Binance Wallet?** Buksan ang Binance app, lumipat sa **Wallet** tab sa itaas, i-tap ang **Create Keyless Wallet** (gumawa ng wallet na walang key) at i-back up ito gamit ang recovery password. Ilang minuto lang ito, hindi kailangan ng seed phrase, at magkakaroon ka ng self-custody wallet (wallet kung saan ikaw, hindi ang exchange, ang may kontrol sa coins) para bumili ng on-chain tokens gaya ng memecoins.

> **Mahahalagang punto**
> - Nasa loob ng Binance app ang Binance Wallet. Kailangan mo ng verified na Binance account, pero self-custody ang coins sa wallet: ikaw ang responsable sa backup.
> - Isa itong "keyless" (MPC) wallet: hinati ang key sa 3 piraso, nasa phone mo, nasa cloud backup mo at nasa Binance. Kahit alin sa 2 ay kayang buksan ang wallet.
> - Huwag kailanman laktawan ang backup. Kung mawala ang phone mo **at** makalimutan mo ang recovery password, hindi na maibabalik ng Binance ang wallet.

Bago ka magsimula: karamihan sa mga bagong memecoin ay nawawalan ng halos lahat ng halaga. Gamitin lang ang perang kaya mong mawala nang buo. Basahin muna kung [ano ang memecoins]({lang}/blog/what-are-memecoins/).

## Ang mga kailangan mo

- Phone na may opisyal na Binance app (i-download lang sa App Store, Google Play o binance.com; maraming pekeng app).
- Binance account na tapos na ang identity verification (KYC, ang pagpapakita ng ID). Kung wala ka pa nito, pwede kang mag-sign up gamit ang aming link: [Binance Wallet](/go/binance-web3?from=learn&l=fil).
- Kaunting BNB o SOL sa Binance account mo, pambili at pambayad ng network fees.

## Step 1 — Buksan ang wallet

1. Mag-log in sa Binance app.
2. Sa itaas ng screen, lumipat mula **Exchange** papuntang **Wallet**.
3. I-tap ang **Create Keyless Wallet**. (Kung may iba ka nang wallet, ang isa pang option ay **Import Wallet** (i-import ang wallet); hindi ito kailangan ng mga baguhan.)

Ilang segundo lang ang paggawa. Hindi ka pakikitaan ng app ng 12 o 24 na seed words: sa halip, gumagamit ito ng MPC (multi-party computation: hinahati ang key sa mga piraso na hindi kailanman magkakasama sa iisang lugar).

## Step 2 — I-back up ito (huwag itong laktawan)

May tatlong paraan ang app para i-save ang backup na piraso mo. Pumili ng isa:

- **iCloud o Google Drive.** Magse-set ka ng **recovery password** na ikaw lang ang nakakaalam. Ine-encrypt dito ang piraso at sine-save sa cloud mo.
- **QR code.** Magse-set ka ng recovery password at magse-save ng QR code; nakatago ang piraso sa isang decentralised na cloud.
- **Quick Backup** (mabilis na backup). Kukumpirmahin mo gamit ang Face ID o fingerprint; walang password, pero third-party provider ang may hawak ng piraso.

Isulat ang recovery password sa papel at itago sa ligtas na lugar. Pagkatapos, i-check: i-tap ang **Settings** (kaliwang itaas sa Home o Assets) → **Wallet Management**. Dapat makita mo ang tag na **Backed Up**.

## Step 3 — Ilipat ang coins mula Binance papunta sa wallet

1. Sa wallet, i-tap ang **Receive** (tumanggap) → **Withdraw from Binance Exchange** (mag-withdraw mula sa Binance Exchange).
2. Piliin ang coin (halimbawa BNB) **at ang network** (BNB Smart Chain para sa BNB, Solana para sa SOL). Dapat magtugma ang network.
3. Ilagay ang halaga. Ipapakita ng app ang fee at ang final na halaga bago ka mag-confirm.
4. Piliin kung sa Spot o Funding account manggagaling ang pera, i-tap ang **Withdraw**, i-check ang address at network, at i-tap ang **Confirm**.

Magsimula sa maliit na test amount. Hindi na makakansela ang na-confirm na transfer. Laging mag-iwan ng kaunting BNB o SOL sa wallet: may network fee (gas) ang bawat galaw sa blockchain, kahit pumalya pa ito.

## Step 4 — Hanapin ang tamang token gamit ang contract address nito

Maraming memecoin ang may kopya na pareho ang pangalan at logo. Ang tanging maaasahang ID ay ang **contract address** (mahabang hanay ng mga letra at numero na natatangi sa bawat token).

1. Kunin ang address sa mapagkakatiwalaang source: ang verified account ng project, isang malaking data site o ang token page sa aming [memecoins page]({lang}/memes/).
2. Sa **Markets** o **Trade** screen ng wallet, i-paste ang address sa search sa halip na i-type ang pangalan.
3. Ikumpara ang unang at huling 4–6 na character sa source mo.

## Step 5 — I-check ang token bago bumili

Sa aming [memecoins page]({lang}/memes/), ipinapakita ng bawat token page ang security check ng Binance at ang mahahalagang numero. Tingnan ang:

- **Liquidity**: gaano kalaking pera ang nasa trading pool. Maliit na liquidity = baka hindi ka makabenta.
- **Holders at bahagi ng top 10**: kung iilang wallet ang may hawak ng karamihan ng supply, kaya nilang pabagsakin ang presyo.
- **Edad**: ang token na ginawa isang oras pa lang ang nakalipas ay parang lotto ticket.
- **Mga babala**: kung may lumabas na kahit anong risk o security warning, tumigil.

Sinasabi mismo ng Binance na hindi nito chine-check ang mga token na nakalista sa Meme Rush (ang feed nito ng mga bagong-bagong memecoin), kaya ikaw ang dapat mag-check. Nakalista ang mga babalang senyales sa aming [lesson tungkol sa scams at rug pulls]({lang}/blog/memecoin-scams-rug-pull/).

## Step 6 — Mag-swap

1. Buksan ang **Trade** → **Swap**. Piliin kung ano ang ipambabayad mo (BNB) at ang token na gusto mo, sa parehong network.
2. Maglagay ng maliit na halaga. Basahin ang rate, ang **slippage** (ang pinakamalaking pagbabago ng presyo na tatanggapin mo bago pumalya ang trade) at ang network fee.
3. May mga token na kailangan munang dumaan sa **Approve** step; may maliit itong fee.
4. I-tap ang **Swap** at kumpirmahin gamit ang passkey o 2FA mo.

Para magbenta, gawin lang ang pabaligtad. Kung gusto mong makita ang pinakabagong mga token, may **Meme Rush** sa Markets tab: doon tine-trade ang mga bagong-bagong token sa isang "bonding curve" at hindi sila mailalabas sa wallet hangga't hindi sila "nagmi-migrate" sa isang normal na DEX (decentralised exchange). Ito ang pinakadelikadong sulok ng market.

> **⚠️ Mag-ingat**
> - **Walang backup, o password na naka-save sa screenshots.** Kapag nawala ang phone at ang password, wala na ang coins habambuhay.
> - **Maling network o maling address.** Ayon sa FAQ ng Binance, hindi na mare-refund ang tokens na naipadala sa maling address. Laging magpadala muna ng test amount.
> - **Pekeng tokens at mga mensahe mula sa "support".** Maghanap lang gamit ang contract address. Hindi kailanman hihingin ng Binance staff ang recovery password mo o ipapa-"verify" ang wallet mo sa isang website.

Susunod na lesson: paano i-connect ang Binance Wallet sa isang DEX site at ibalik ang coins sa Binance. Tingnan ang lahat ng lesson sa [Learn page]({lang}/learn/).

## Sources

- [Binance: Frequently Asked Questions on Binance Wallet](https://www.binance.com/en/support/faq/5a3fc86a702b43e1a4a398ebd8853b77)
- [Binance: What Is a Keyless Wallet and Why Do I Need to Back It Up?](https://www.binance.com/en/support/faq/4efebcb9a937417ca31baa2f7754c50f)
- [Binance: How to Back Up My Binance Wallet?](https://www.binance.com/en/support/faq/53521dedad474c908ec3761a935cb8d6)
- [Binance: How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance: What Is Binance Wallet Swap?](https://www.binance.com/en/support/faq/7ebe19e8ff884cc09a9dbb064aff131f)
- [Binance: Introducing Meme Rush — Fair Mode (9 Oct 2025)](https://www.binance.com/en/support/announcement/detail/c21eac66543c4a62b8b6868cb01ba4f3)

*Hindi ito investment advice. Napakadelikado ng memecoins; ipinapaliwanag lang ng gabay na ito kung paano gumagana ang app at hindi nito inirerekomenda ang pagbili ng kahit anong token. Maaaring hindi available ang Binance Wallet sa bawat bansa.*

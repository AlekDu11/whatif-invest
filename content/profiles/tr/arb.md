---
title: Arbitrum (ARB) sade dille: Ethereum katman 2, optimistic rollup ve 10 milyar ARB tavanı
description: Arbitrum sade dille: bu Ethereum katman 2 ağı nasıl çalışır, ARB DAO'da ne işe yarar, token kilit açılışları, hikâyesi ve başlıca riskler.
date: 2026-11-23
kind: analysis
---
**Arbitrum**, Ethereum'un üzerine kurulmuş, işlemleri daha hızlı ve çok daha ucuz hâle getiren ama güvenlik için yine Ethereum'a dayanan bir ağdır; buna "katman 2" (layer 2) denir. ABD'li Offchain Labs şirketi tarafından geliştirildi; **ARB** tokeni ise sahiplerine ağın ve hazinesinin nasıl yönetileceği konusunda oy hakkı verir. ARB'nin bugünkü değeri {{mcap:arb}} (kripto paralar arasında {{rank:arb}}).

> **Öne çıkanlar**
> - Hiçbir zaman 10 milyardan fazla ARB olmayacak; Mart 2023'teki çıkışta yaklaşık %42'si DAO hazinesine, yaklaşık %27'si ekibe ve %17,5'i yatırımcılara ayrıldı.
> - Rekoru {{ath:arb}} ({{athd:arb}}); bugünkü fiyat ondan {{fromath:arb}}.
> - ARB bir yönetişim tokenidir: Arbitrum'daki ücretler ARB ile değil, ETH ile ödenir.
> - Ekip ve yatırımcı tokenlerinin kilidi Mart 2024'ten beri her ay açılıyor; bu da piyasaya yeni arz ekliyor.

## Nasıl çalışır

Arbitrum bir **optimistic rollup**'tır. Her Ethereum düğümünün her işlemi tek tek işlemesi yerine Arbitrum işlemleri kendi zincirinde yürütür ve sıkıştırılmış veri paketlerini Ethereum'a gönderir. Tek bir operatör, yani **sıralayıcı** (sequencer, Offchain Labs tarafından işletiliyor), işlemleri sıraya koyar ve saniyenin çok küçük bir bölümünde onaylar. Sonuçlar, biri itiraz etmedikçe doğru kabul edilir ("iyimser" yaklaşım): herhangi bir doğrulayıcı **dolandırıcılık kanıtı** (fraud proof) sunabilir ve anlaşmazlık Ethereum üzerinde çözülür. Şubat 2025'ten beri **BoLD** protokolü herkesin doğrulamaya katılmasına izin veriyor ve zinciri korumak için tek bir dürüst doğrulayıcı yeterli. Yazılım altyapısı **Nitro** Ethereum uygulamalarıyla uyumludur; **Orbit** programı ise başka projelerin Arbitrum teknolojisiyle kendi zincirlerini kurmasını sağlar.

## Token ne işe yarıyor

ARB her şeyden önce bir oy tokenidir. Sahipleri veya seçtikleri delegeler, **Arbitrum DAO**'da ağın güncellemeleri ve milyarlarca ARB ile sıralayıcı ücretlerinden gelen geliri tutan DAO hazinesinin nasıl harcanacağı üzerine oy kullanır. Arbitrum'u kullanmak için ARB gerekmez: gas ücreti ETH ile ödenir. Bu yüzden tokenin değeri, ağın ne kadar kullanıldığına doğrudan değil, oy haklarına ve DAO'nun parasıyla ne yapmaya karar verdiğine bağlıdır.

## Şu anki rakamlar

- Bugünkü fiyat: {{price:arb}}
- Rekor: {{ath:arb}} ({{athd:arb}}), ondan {{fromath:arb}}
- Piyasa değeri: {{mcap:arb}} (kripto paralar arasında {{rank:arb}})
- 12 aylık fiyat değişimi: {{chg1y:arb}}
- 3 yıl boyunca günde 10 $: {{dca:arb:3}}, yatırılan {{dcainv:3}} ({{dcaroi:arb:3}})

## Hikâyesi

Offchain Labs, Princeton Üniversitesi'ndeki araştırmalardan doğdu. Arbitrum One Ağustos 2021'in sonunda herkese açıldı; Ağustos 2022'deki Nitro güncellemesi ücretleri düşürüp kapasiteyi artırdı. 23 Mart 2023'te ARB tokeni, kullanıcılara yapılan büyük bir airdrop ile piyasaya çıktı. Birkaç gün sonra ilk teklif olan AIP-1 büyük tepki çekti, çünkü Vakıf 750 milyon ARB'lik bir payı oylamadan önce kullanmaya başlamıştı; ardından teklifi bölerek DAO'ya daha fazla kontrol verdi. ARB zirvesine, yaklaşık 2,39 $'a, Ocak 2024'te ulaştı. 16 Mart 2024'te ekip ve yatırımcılara ait yaklaşık 1,1 milyar tokenin kilidi açıldı, ardından aylık kilit açılışları başladı. 2025'te BoLD devreye girdi; fiyat ise 2025 ve 2026 boyunca sert düştü.

## Alternatifler

Arbitrum diğer Ethereum katman 2 ağlarıyla rekabet ediyor: [Optimism]({lang}/op/) ve onun OP Stack'i üzerine kurulan zincirler, bunlar arasında kendi tokeni olmayan Coinbase'in Base ağı; [ZKsync]({lang}/zk/) ve [Starknet]({lang}/strk/) gibi sıfır bilgi (zero-knowledge) rollup'ları; ayrıca [Mantle]({lang}/mnt/) ve [POL (ex-MATIC)]({lang}/pol/). Kendi güncellemeleriyle kullanımı giderek ucuzlayan [Ethereum]({lang}/eth/) da bir alternatiftir.

## Başlıca riskler

- **Yeni arz:** ekip ve yatırımcılar için kilit açılışları sürüyor; DAO hazinesi de tüm ARB'nin büyük bir kısmını tutuyor.
- **Merkezî sıralayıcı:** işlemleri tek bir operatör sıralıyor; durursa ya da kötü davranırsa kullanıcılar daha yavaş yedek yollara muhtaç kalır.
- **Rekabet:** Base ve diğer katman 2 ağları aynı kullanıcılar, uygulamalar ve ücretler için yarışıyor.
- **Kullanımla zayıf bağ:** ücretler ETH ile ödendiği için Arbitrum'un yoğun kullanımı ARB talebini otomatik olarak artırmıyor.
- **Düzenleme:** tokenler, DAO'lar ve arkalarındaki şirketlerle ilgili kurallar ülkeden ülkeye değişebilir.

## Düzenli alım yapıyorsanız bu ne anlama geliyor

ARB hayatının büyük bölümünü ilk zirvesinden düşerek geçirdi; yani düzenli alım yapan biri giderek daha düşük fiyatlardan daha fazla token biriktirdi — bu yalnızca fiyat toparlanırsa işe yarar. Belirli bir tutarı düzenli olarak almak, yanlış zamanlama riskini dağıtır ama zarar riskini ortadan kaldırmaz. Pek çok kişi bu tür tokenleri birikimlerinin yalnızca küçük bir kısmı olarak tutar. Geçmiş sonuçlar gelecekteki getirilerin garantisi değildir.

*Yatırım tavsiyesi değildir.*

## Kaynaklar

- [A gentle introduction to Arbitrum (Arbitrum belgeleri)](https://docs.arbitrum.io/intro/)
- [A gentle introduction to the Arbitrum DAO (Arbitrum Foundation)](https://docs.arbitrum.foundation/gentle-intro-dao-governance)
- [Offchain Labs releases Arbitrum BoLD on mainnet (The Block, 12 Şubat 2025)](https://www.theblock.co/post/340278/offchain-labs-releases-arbitrum-bold-on-mainnet-for-permissionless-validation)
- [Arbitrum price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/arbitrum)

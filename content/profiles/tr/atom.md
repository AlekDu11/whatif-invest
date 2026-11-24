---
title: Cosmos (ATOM) sade dille: 2019'dan beri "blokzincirlerin interneti", IBC ve Cosmos Hub
description: Cosmos sade dille: Cosmos SDK ve IBC blokzincirleri nasıl bağlar, ATOM ne işe yarar, enflasyonu, tokenomi tartışması, uzun düşüşü ve başlıca riskler.
date: 2026-11-24
kind: analysis
---
**Cosmos**, insanların kendi blokzincirlerini kurmasını ve bunları birbirine token ve mesaj gönderebilecek şekilde bağlamasını sağlayan bir araçlar ailesi ve bir ağdır — proje buna "blokzincirlerin interneti" diyor. ATOM, ağın ilk zinciri olan ve Mart 2019'da devreye giren Cosmos Hub'ın token'ıdır. Bugünkü piyasa değeri {{mcap:atom}} (kripto paralar arasında {{rank:atom}}).

> **Öne çıkanlar**
> - Osmosis, dYdX, Injective, Celestia ve Cronos dahil yüzlerce blokzincir ücretsiz Cosmos SDK ile kuruldu, ancak bunların çoğunun ATOM'a ihtiyacı yok.
> - Rekor fiyatı {{ath:atom}} ({{athd:atom}}); bugün fiyat ondan {{fromath:atom}} uzakta.
> - ATOM'un azami arzı yok: stake edenler için her yıl yeni token yaratılıyor; 2023'teki bir oylamadan beri yılda %7–10 oranında.
> - Cosmos Labs, 2025–2026'da ATOM'un ekonomisini yeniden tasarlamak için herkese açık bir araştırma süreci yürüttü; Kasım 2026'ya kadar yeni bir model kabul edilmedi.

## Nasıl çalışır

Cosmos'un üç yapı taşı var. **Cosmos SDK**, kendi kuralları ve token'ı olan bir blokzincir kurmak için ücretsiz bir araç setidir. **CometBFT** (eski adıyla Tendermint), bir grup doğrulayıcının yeni bloklar üzerinde saniyeler içinde uzlaşmasını sağlayan motordur. **IBC** ise, yani 2021'de devreye alınan Inter-Blockchain Communication protokolü, ayrı zincirlerin merkezi bir köprü operatörü olmadan birbirine token ve veri göndermesine izin verir; ikinci sürümü IBC Eureka, Ethereum gibi Cosmos dışındaki ağlara ulaşmak için 2025'te çıktı. Her zincir kendi doğrulayıcılarını ve güvenliğini korur — zincirlerin tek bir güvenliği paylaştığı [Polkadot]({lang}/dot/)'tan farklı olarak. Cosmos Hub'ın kendisini ATOM stake eden 180 doğrulayıcı işletiyor.

## Token ne işe yarar

ATOM, Cosmos Hub'ı güvence altına alır: sahipleri onu doğrulayıcılara stake eder ve ödül olarak yeni yaratılan ATOM ile ücretleri alır. Stake'ten çıkış 21 gün sürer ve kurallara aykırı davranan doğrulayıcılar stake'lerinin bir kısmını kaybeder. ATOM aynı zamanda oy demek: güncellemeler ve topluluk havuzu zincir üstü tekliflerle kararlaştırılır. Zayıf noktası, diğer Cosmos zincirlerinin kendi token'larını kullanmasıdır; bu yüzden ekosistemin başarısı ATOM'a otomatik olarak talep yaratmaz. Ona daha büyük bir rol verme planları başarısız oldu: sahipleri Kasım 2022'de "ATOM 2.0" planını reddetti ve Hub'ın 2023'ten itibaren daha küçük zincirleri korumasını sağlayan Interchain Security, bu zincirlerin sonuncusu da ayrıldıktan sonra 2026'da kaldırıldı.

## Şu anki rakamlar

- Bugünkü fiyat: {{price:atom}}
- Rekor: {{ath:atom}} ({{athd:atom}}), ondan {{fromath:atom}}
- Piyasa değeri: {{mcap:atom}} (kripto paralar arasında {{rank:atom}})
- 12 aylık fiyat değişimi: {{chg1y:atom}}
- 5 yıl boyunca günde 10 $: {{dca:atom:5}}, yatırılan {{dcainv:5}} ({{dcaroi:atom:5}})

## Hikâyesi

Tendermint'in yaratıcısı Jae Kwon ile Ethan Buchman, Cosmos'un teknik belgesini (whitepaper) 2016'da yayımladı; Nisan 2017'deki token satışı yaklaşık 17 milyon dolar topladı. Cosmos Hub 13 Mart 2019'da başladı ve IBC 2021'de devreye girdi. O yıl ATOM, Eylül 2021'de yaklaşık 44 $'a ulaştı. Mayıs 2022'de Cosmos SDK ile kurulan en büyük zincirlerden biri olan Terra çöktü ve tüm ekosisteme zarar verdi. Kasım 2023'te sahipleri azami enflasyonu %20'den %10'a indirmek için oy verdi. 2025'te geliştirici şirket Interchain Labs'in adı Cosmos Labs olarak değişti ve Interchain Foundation dışarıdan araştırmacılarla yeni bir token modeli üzerinde çalışmaya başladı. ATOM düşmeye devam etti ve Kasım 2026'da 2021 zirvesinin %95'ten fazla altında yeni dipler gördü.

## Alternatifler

Birçok zinciri birbirine bağlamada Cosmos'un en yakın rakibi [Polkadot]({lang}/dot/). Uygulama geliştirmede ikisi de [Ethereum]({lang}/eth/) ve onun katman 2 ağlarıyla, ayrıca [Solana]({lang}/sol/), [Avalanche]({lang}/avax/) ve [Sui]({lang}/sui/) gibi hızlı tekil zincirlerle yarışıyor. Cosmos teknolojisini beğenen yatırımcılar, onunla kurulan zincirlerin token'larına da bakabilir: [Osmosis]({lang}/osmo/), [Injective]({lang}/inj/), [Celestia]({lang}/tia/) veya [Cronos]({lang}/cro/) gibi.

## Başlıca riskler

- **Büyük dalgalanmalar:** ATOM 2021 zirvesinden %95'ten fazla değer kaybetti; teknoloji kullanılırken bile uzun düşüşler sürebilir.
- **Zayıf değer yakalama:** Cosmos zincirleri ATOM kullanmak veya ATOM ile ödeme yapmak zorunda değil, bu yüzden token ekosistemin büyümesinden yararlanamayabilir.
- **Enflasyon:** her yıl yeni ATOM yaratılıyor; bu, stake etmeyen sahiplerin payını sulandırıyor.
- **Yönetişim ve uygulama:** token modeli yeniden tasarlanıyor ve geçmişteki büyük planlar reddedildi ya da bırakıldı; sonuç belirsiz.
- **Rekabet ve düzenleme:** kullanıcıların çoğunu Ethereum'un katman 2'leri ve hızlı tekil zincirler çekiyor; token ve staking kuralları ülkeden ülkeye değişiyor.

## Düzenli alım yapıyorsanız bu ne anlama geliyor

ATOM, yaygın kullanılan bir teknolojinin token fiyatının yükselmesini garanti etmediğini gösteriyor. Düzenli olarak sabit tutarda almak, dibi tahmin etmeye çalışmadan fiyat düşükken daha çok, yüksekken daha az almanız demek — ama kayıp riskini ortadan kaldırmaz. Birçok kişi kriptoyu, sert düştüğünü görmeyi göze alabileceği birikiminin küçük bir kısmıyla sınırlı tutar. Geçmiş sonuçlar gelecekteki getirileri garanti etmez.

*Yatırım tavsiyesi değildir.*

## Kaynaklar

- [Cosmos resmî sitesi](https://cosmos.network/)
- [Cosmos (ATOM) review: tokenomics, staking and risks (Coin Bureau, Eylül 2026)](https://coinbureau.com/review/cosmos-atom)
- [Cosmos powers the internet of blockchains. Can ATOM capture the value? (TipRanks, Nisan 2026)](https://www.tipranks.com/news/cosmos-powers-the-internet-of-blockchains-can-atom-capture-the-value)

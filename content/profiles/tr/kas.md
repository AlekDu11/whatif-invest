---
title: Kaspa (KAS) sade dille: 2021'den beri iş kanıtlı blockDAG, saniyede 10 blok ve 28,7 milyar üst sınır
description: Kaspa sade dille: blockDAG ve GHOSTDAG nasıl çalışır, ön madencilik olmadan adil başlangıç, Crescendo ve Toccata güncellemeleri, hikâyesi ve riskleri.
date: 2026-11-24
kind: analysis
---
**Kaspa**, bitcoin gibi madencilikle üretilen ama çok daha hızlı olacak şekilde tasarlanmış bir iş kanıtı (proof of work) kripto parası. Tek bir blok zinciri yerine aynı anda birçok bloğun eklenebildiği bir "blockDAG" kullanır. Kasım 2021'de ön madencilik ve token satışı olmadan başladı; coini **KAS**'ın bugünkü piyasa değeri {{mcap:kas}} (kripto paralar arasında {{rank:kas}}).

> **Öne çıkanlar**
> - Hiçbir zaman yaklaşık 28,7 milyardan fazla KAS olmayacak; 2026 sonuna kadar bunların yaklaşık %97'si zaten çıkarılmıştı.
> - Rekoru {{ath:kas}} ({{athd:kas}}); bugünkü fiyat ondan {{fromath:kas}}.
> - Mayıs 2025'teki Crescendo güncellemesinden beri ağ saniyede bir yerine 10 blok üretiyor.
> - Kaspa'da ön madencilik, ön satış veya kuruculara ayrılmış coin yoktu; her KAS madencilikten geldi.

## Nasıl çalışır

Bitcoin'de iki madenci aynı anda blok bulursa bloklardan biri atılır; bu yüzden bloklar yavaş olmalıdır (yaklaşık 10 dakikada bir). Kaspa bu paralel blokların hepsini tutar ve onları bir grafikte, yani bir **blockDAG**'da (yönlü döngüsüz grafik) birbirine bağlar. Yonatan Sompolinsky ve Aviv Zohar'ın akademik araştırmalarına dayanan **GHOSTDAG** protokolü de tüm blokları ve işlemleri tek bir ortak sıraya koyar. Böylece Kaspa çok sık blok üretir ve ödemeleri saniyeler içinde onaylar; bunu yaparken kendi kHeavyHash algoritmasıyla bitcoin tarzı madenciliği korur. Arz yavaş yavaş azalır: madenci ödülü her ay biraz düşer ve yaklaşık yılda bir yarıya iner.

## İnsanlar neden değeri olduğunu düşünüyor

Destekçileri Kaspa'yı "hızlı dijital gümüş" olarak görüyor: bitcoin'de sevilen şeyleri —iş kanıtı, sabit arz, şirket olmaması ve önceden dağıtılmış coin olmaması— korur, ama ödemeler dakikalar yerine saniyeler içinde kesinleşir. Adil başlangıç birçok yatırımcı için önemli, çünkü hiçbir ekip veya fon sonradan satmak üzere ucuz coin almadı. 2026'da ağ programlanabilirlik de kazanmaya başladı: Toccata güncellemesi covenant'ları (coinlerin nasıl harcanabileceğine dair kurallar), sıfır bilgi kanıtı doğrulamasını ve yerel tokenleri getirdi; bu da geliştiricilerin Kaspa üzerinde uygulama kurmasını sağlayabilir.

## Şu anki rakamlar

- Bugünkü fiyat: {{price:kas}}
- Rekor: {{ath:kas}} ({{athd:kas}}), ondan {{fromath:kas}}
- Piyasa değeri: {{mcap:kas}} (kripto paralar arasında {{rank:kas}})
- 12 aylık fiyat değişimi: {{chg1y:kas}}
- 3 yıl boyunca günde 10 $: {{dca:kas:3}}, yatırılan {{dcainv:3}} ({{dcaroi:kas:3}})

## Hikâyesi

Kaspa, araştırmalardan ve DAGlabs şirketinden doğdu; ana ağ 7 Kasım 2021'de başladı. İlk yıl yalnızca küçük borsalarda, bir sentin kesirleri fiyatına işlem gördü. 2023'te büyük borsalar listeledi, fiyat kat kat yükseldi ve 2024 ortasında yaklaşık 0,21 $ ile rekor kırdı. Geliştiriciler düğüm yazılımını Rust ile yeniden yazdı ("Rusty Kaspa"); hız sıçramasını bu mümkün kıldı: 5 Mayıs 2025'te Crescendo hard fork'u ağı saniyede bir bloktan on bloğa çıkardı. Fiyat 2025 ve 2026 boyunca sert düştü; 2026'da Toccata hard fork'u Kaspa'yı programlanabilir bir katman 1 ağına dönüştürdü.

## Alternatifler

Kaspa en doğrudan [Bitcoin]({lang}/btc/), [Litecoin]({lang}/ltc/) ve [Bitcoin Cash]({lang}/bch/) gibi diğer iş kanıtlı ödeme coinleriyle rekabet eder. Hızlı ve ucuz transferler ile uygulamalar için insanlar [Solana]({lang}/sol/) gibi hisse kanıtı ağlarını da kullanıyor; günlük ödemelerde ise birçok kişi doğrudan dolar stablecoinlerini tercih ediyor.

## Başlıca riskler

- **Büyük dalgalanmalar:** KAS 2024 rekorundan şimdiden %80'den fazla düştü; bu tür düşüşler tekrarlanabilir.
- **Madencilik yoğunlaşması:** birkaç büyük madencilik havuzu ve ASIC üreticisi hash gücünün büyük kısmını kontrol ediyor.
- **Küçük ekip:** geliştirme, büyük bir şirket yerine çoğunlukla topluluk bağışlarıyla finanse edilen bir grup çekirdek geliştiriciye dayanıyor.
- **Benimsenme:** hız tek başına talep yaratmaz; Toccata uygulamaları ve gerçek ödemeler henüz yaygınlaşmalı.
- **Piyasaya erişim:** işlemlerin büyük kısmı orta ölçekli borsalarda yapılıyor ve kripto kuralları ülkeden ülkeye değişebiliyor.

## Düzenli alım yapıyorsanız bu ne anlama geliyor

Kaspa, çok sert yükseliş ve düşüşleri olan genç bir coin. Düzenli olarak sabit tutarda almak giriş fiyatınızı iyi ve kötü aylara yayar, ama uzun bir düşüşten korumaz. KAS'ın büyük kısmı zaten çıkarıldı; bu yüzden gelecekteki fiyat hareketleri esas olarak talebe bağlı. Birçok kişi bu tür coinleri kripto varlıklarının küçük bir parçası olarak tutar. Geçmiş sonuçlar geleceği garanti etmez.

*Yatırım tavsiyesi değildir.*

## Kaynaklar

- [Kaspa — official website (kaspa.org)](https://kaspa.org/)
- [PHANTOM and GHOSTDAG: A Scalable Generalization of Nakamoto Consensus — Sompolinsky, Wyborski, Zohar (IACR ePrint 2018/104)](https://eprint.iacr.org/2018/104.pdf)
- [Kaspa Covenants++ «Toccata» hard-fork outlook — Michael Sutton, Kaspa core developer (Medium)](https://medium.com/@michaelsuttonil/kaspa-covenants-toccata-hard-fork-outlook-a4d81a40900c)
- [Kaspa price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/kaspa)

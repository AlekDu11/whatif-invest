---
title: Akash Network (AKT) sade dille: bulut ve yapay zekâ hesaplaması için açık pazar yeri, 2020'den beri
description: Akash sade dille: GPU bulut pazar yeri nasıl çalışır, AKT ne işe yarar, Burn-Mint Equilibrium, Solana'ya geçiş, hikâyesi, rakipleri ve başlıca riskler.
date: 2026-11-26
kind: analysis
---
**Akash Network**, bilgi işlem gücü için bir pazar yeridir: web siteleri, uygulamalar ya da yapay zekâ için sunucuya veya ekran kartına (GPU) ihtiyaç duyanlar, bunları Amazon, Google ya da Microsoft yerine dünyanın dört bir yanındaki bağımsız sağlayıcılardan kiralar. Ağı, kurucusu Greg Osuri'nin yönettiği ABD'li Overclock Labs şirketi geliştiriyor; AKT tokeninin toplam değeri bugün {{mcap:akt}} (kripto paralar arasında {{rank:akt}}). İnsanlar onu yapay zekâ hesaplamasına olan talepten güç alan en eski "DePIN" — merkeziyetsiz fiziksel altyapı — projelerinden biri olarak takip ediyor.

> **Öne çıkanlar**
> - Akash, bilgi işlem alıcılarını açık bir açık artırmada sağlayıcılarla buluşturuyor; GPU'lar pazar yerine Ağustos 2023'te katıldı.
> - Mart 2026'dan beri her kiralama "Burn-Mint Equilibrium" modeliyle AKT üzerinden ödeniyor; kullanım arttıkça daha fazla AKT yakılıyor.
> - Kasım 2026'da topluluk, Akash'ın kendi Cosmos zincirinden yaklaşık 24 ay içinde Solana'ya taşınmasını ve AKT'nin 1:1 takas edilmesini onayladı.
> - Rekor fiyatı {{ath:akt}} ({{athd:akt}}); bugün fiyat ondan {{fromath:akt}} uzakta.

## Nasıl çalışır

Bir geliştirici neye ihtiyacı olduğunu tarif eder — örneğin bir yapay zekâ modelini çalıştırmak için bir GPU ve biraz bellek — ve sağlayıcılar bunu barındırmak için teklif verir. Uygun olan en ucuz teklif kazanır ve uygulama o sağlayıcının donanımında konteynerler içinde çalışır. Sağlayıcılar veri merkezlerinden, 2026'da açılan Homenode betasıyla birlikte RTX 4090 gibi güçlü bir ev ekran kartına sahip bireylere kadar uzanıyor. Ağın kendisi şimdiye kadar Cosmos SDK ile kurulmuş, AKT stake eden doğrulayıcıların güvence altına aldığı ayrı bir blokzincirdi. Akash ayrıca açık yapay zekâ modellerini çalıştırmaya yarayan ve OpenRouter platformu üzerinden sunulan AkashML hizmetini işletiyor.

## Token ne işe yarar

AKT, staking yoluyla ağı güvence altına alır, sahiplerine güncellemelerde oy hakkı verir ve 23 Mart 2026'daki Mainnet 17 güncellemesinden beri tüm ödemelerin aracıdır. Burn-Mint Equilibrium (BME) modelinde müşteri AKT yakarak ACT alır; ACT yaklaşık bir dolar değerinde, alınıp satılamayan bir kredidir. İş ödendiğinde sağlayıcılar, o anki fiyattan yeni basılmış AKT alır. Arada AKT değer kazandıysa yakılandan daha az basılır ve arz küçülür; değer kaybettiyse daha fazla basılır. Müşteriler kartla da ödeyebilir; bu durumda önce piyasadan AKT satın alınır. BME'den önce ödemeler USDC stablecoin'iyle yapılabiliyordu ve ücretlerin bir kısmı stake edenlere gidiyordu.

## Şu anki rakamlar

- Bugünkü fiyat: {{price:akt}}
- Rekor: {{ath:akt}} ({{athd:akt}}), ondan {{fromath:akt}}
- Piyasa değeri: {{mcap:akt}} (kripto paralar arasında {{rank:akt}})
- 12 aylık fiyat değişimi: {{chg1y:akt}}
- 5 yıl boyunca günde 10 $: {{dca:akt:5}}, yatırılan {{dcainv:5}} ({{dcaroi:akt:5}})

## Hikâyesi

Akash'ın ana ağı Eylül 2020'de yayına girdi, Mart 2021'de de bilgi işlem kiralama pazar yeri açıldı. AKT, Nisan 2021'de yaklaşık 8 $ ile rekorunu kırdı, ardından 2022 kripto çöküşünde neredeyse tüm değerini kaybederek Kasım 2022'de 0,20 $'ın altına indi. 31 Ağustos 2023'te Mainnet 6 güncellemesi Nvidia GPU'larını ve USDC ödemelerini ekledi; yapay zekâ patlaması AKT'yi 2024 başında yeniden 5 $ civarına taşıdı. Fiyatlar 2025'te yine geriledi ve yıl sonunda yaklaşık 0,35 $'a indi. Ekim 2025'te Osuri, Akash'ın kendi zincirinden vazgeçeceğini açıkladı; BME Mart 2026'da devreye girdi ve 2 Kasım 2026'da Akash, 346 numaralı yönetişim önerisinin %97 destekle kabul edilmesinin ardından Solana'ya geçişi doğruladı.

## Alternatifler

Asıl rekabet büyük bulutlardan — Amazon Web Services, Microsoft Azure ve Google Cloud — ve GPU'ya özel bulutlardan geliyor. Kripto projeleri arasında [Render]({lang}/render/) ve [io.net]({lang}/io/) de GPU kiralıyor, [Bittensor]({lang}/tao/) yapay zekâ modellerinin kendisini ödüllendiriyor, [Internet Computer]({lang}/icp/) zincir üstü barındırma sunuyor; [Filecoin]({lang}/fil-crypto/) ve [Arweave]({lang}/ar-crypto/) ise aynısını hesaplama yerine depolama için yapıyor.

## Başlıca riskler

- **Büyük dalgalanmalar:** AKT bir kez rekorundan %95'ten fazla düştü; bu tür düşüşler yeniden yaşanabilir.
- **Taşınma:** iki yıl sürecek Solana geçişi büyük bir teknik proje; gecikmeler, hatalar ya da karmaşık bir token takası sahiplerine zarar verebilir.
- **Yeni token modeli:** BME ancak 2026'da devreye girdi; kullanım küçük kalırsa yeni basılan AKT yakılanı geçebilir.
- **Rekabet:** büyük bulutların çok daha fazla parası var, diğer kripto GPU ağları da aynı müşterilerin peşinde.
- **Yoğunlaşma ve düzenleme:** ana şirket, büyük sahipler ve birkaç sağlayıcı büyük ağırlık taşıyor; tokenlara ilişkin kurallar ülkeden ülkeye değişiyor.

## Düzenli alım yapıyorsanız bu ne anlama geliyor

AKT'nin fiyatı, ağın gerçek kullanımından çok yapay zekâ ve kripto heyecan dalgalarını izledi. Düzenli olarak sabit bir tutarla almak giriş fiyatınızı bu dalgalara yayar, ancak büyük kayıp riskini ortadan kaldırmaz. Pek çok kişi bu tür tokenları, sert düşüşünü kaldırabileceği küçük bir birikim payıyla sınırlar. Geçmiş getiriler gelecekteki kazancı garanti etmez.

*Yatırım tavsiyesi değildir.*

## Kaynaklar

- [AEP-76: Akash'ta Burn Mint Equilibrium (akash.network)](https://akash.network/roadmap/aep-76/)
- [Yapay zekâ için süper bulut yayında — Akash'ta GPU'lar (akash.network, Ağustos 2023)](https://akash.network/blog/the-supercloud-for-ai-is-live/)
- [Akash, Solana'ya geçişini duyurdu (basın bülteni, 2 Kasım 2026)](https://www.webull.com/news/15855281864205312)
- [Akash Network, Cosmos zincirini kullanımdan kaldıracak (The Block, Ekim 2025)](https://www.theblock.co/news/ecosystems/2025-10-13-akash-network-to-deprecate-its-cosmos-chain-begin-search-for-new-network-374318)

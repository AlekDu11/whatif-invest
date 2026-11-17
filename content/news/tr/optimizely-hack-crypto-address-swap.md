---
title: Optimizely saldırısı 178 büyük siteye kripto adresi değiştiren kod yerleştirdi
description: Optimizely'nin test aracındaki bir açık, 16 Kasım'da CNN, BBC ve Zoom gibi sitelerde kripto cüzdan adreslerinin değiştirilmesine yol açtı. Nasıl korunursunuz?
date: 2026-11-17 10:40
tags: hacks, bitcoin
assets: btc, eth, sol
---
16 Kasım Pazartesi günü bir saldırgan, büyük şirketlerin kullandığı A/B test aracı Optimizely Web Experimentation'daki bir açığı kullanarak en az 178 kuruluşun sitesine zararlı JavaScript yerleştirdi. Bunlar arasında CNN, BBC, Zoom, HSBC ve donanım cüzdanı üreticisi Ledger da var. Kod, kripto cüzdan adreslerini sessizce saldırganın adresleriyle değiştiriyordu.

## Ne oldu

- **Tedarik zinciri saldırısı.** Kod, Optimizely'nin kendi CDN'inden geçerli bir sertifikayla sunulduğu için siteler normal görünüyordu. Report URI, incelediği 1,611 kod parçasının 188'inde zararlı kodu buldu ve gerçek sayının daha yüksek olduğunu düşünüyor.
- **Her yerde adres değişimi.** Bitcoin, ether ve diğer EVM ağları, Tron, Solana, TON, Litecoin, Bitcoin Cash ve Dogecoin adresleri hedefteydi — sayfa metninde, formlarda, bağlantılarda, hatta panoda.
- **Kartlar ve iPhone'lar da.** 13:43 UTC'de bir kart kopyalayıcı eklendi; gizli bir çerçeve eski iOS sürümleri için istismar kiti yüklemeye çalıştı. Ele geçirilmiş bir iPhone henüz doğrulanmadı.
- **Şimdilik küçük bir ganimet.** Saldırganın cüzdanlarına yaklaşık dokuz saatte $7,040 civarında para girdi, çoğu BTC olarak. Optimizely kodu kaldırdığını ve etkilenen hesapları güvenceye aldığını söylüyor.

## Sizin için anlamı

Pazartesi günü bir siteden adres kopyalayarak kripto gönderdiyseniz, paranın doğru cüzdana gidip gitmediğini kontrol edin. Her transferde iyi bir alışkanlık: adresin ilk ve son karakterlerini karşılaştırın ve donanım cüzdanınızın ekranında onaylayın. iPhone'unuzu iOS 18.7.3 / 26.3 veya daha yeni bir sürüme güncelleyin. Bitcoin {{price:btc}} seviyesinde, $126,080'lik rekorunun çok altında; her coinin durumunu [zirveden uzaklık sayfamızda]({lang}/ath/) görün, platformu da [borsa karşılaştırmamızla]({lang}/exchanges/) dikkatle seçin.

## Kaynaklar

- [Report URI — World's largest brands infected with malware via Optimizely](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)
- [The Hacker News — Hijacked Optimizely scripts served card skimmer and iOS exploit kits](https://thehackernews.com/2026/11/hijacked-optimizely-scripts-served-card.html)
- [U.Today — Crypto-stealing exploit in JavaScript emerges](https://u.today/major-crypto-stealing-exploit-in-javascript-emerges-zoom-cnn-hsbc-affected)

*Yatırım tavsiyesi değildir. WhatIfStack makaleleri, Anthropic'in Claude'u dahil yapay zekâ araçlarının yardımıyla hazırlanır.*

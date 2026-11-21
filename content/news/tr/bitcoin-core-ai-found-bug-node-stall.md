---
title: Bitcoin Core, yapay zekânın bulduğu düğüm donduran hatayı kapattı: 30.5 ve 31.3 sürümleri
description: Bitcoin Core 30.5 ve 31.3, Block'un Spiral ekibinin yapay zekâ tarayıcısının bulduğu, bir eşin düğümü 10 saniyeden fazla dondurabildiği hatayı kapatıyor.
date: 2026-11-21 14:30
tags: bitcoin, hacks, ai
assets: btc
---
Bitcoin'in ana yazılımı, ilk olarak bir yapay zekâ aracının bulduğu bir güvenlik açığı için düzeltme aldı. 20 Kasım cuma günü yayımlanan Bitcoin Core 30.5 ve 31.3 sürümleri, tek bir eşin her mesajla bir düğümü on saniyeden fazla durdurmasına yol açan hatayı kapatıyor.

## Ne oldu

- **Hata.** CVE-2026-117348 numarasıyla izleniyor ve orta düzey olarak sınıflandırıldı. Bir eş, tek bir duyuruda aynı işlem kimliğini 50.000 kez tekrarlayabiliyordu; düğüm her kopyayı kontrol edip donuyor, yeni blokları bile işlemiyordu.
- **Kim buldu.** Block'un Spiral ekibinin yapay zekâ ajanları kullanan açık kaynaklı tarayıcısı Loupe tespit etti; bülten, Elias Rohrer'in Project Loupe'u kapsamındaki otomatik yapay zekâ taramasına teşekkür ediyor.
- **Düzeltme.** Güncellenen düğümler artık duyurulan her işlemi yalnızca bir kez işliyor. The Defiant'a göre emekliye ayrılan 29.x dalı düzeltme almayacak.
- **Risk.** Hiçbir fon ya da coin tehlikede değildi. CoinDesk'e göre gerçekçi zarar gecikmeydi: borsanın mevduatları daha geç yansıtması ya da bir madencinin kısa süre eski zincir üzerinde çalışması.

## Bizim bakışımız

Bu, cumartesi günkü satışın nedeni değil; bitcoin hisselerle ve kaldıraçlı pozisyonların tasfiyesiyle düştü. Ama yapay zekânın artık temel kripto kodundaki hataları hem saldırganlar hem savunanlar için bulduğunu gösteriyor. Düğüm çalıştırıyorsanız 30.5 ya da 31.3'e güncelleyin. Yalnızca bitcoin tutuyorsanız hiçbir şey değişmiyor. Bitcoin {{price:btc}} seviyesinde, rekorunun yüzde 50'den fazla altında — [zirveden uzaklık sayfasına]({lang}/ath/) ve [yapay zekâ ve piyasalar sayfamıza]({lang}/ai/) bakın. 5 yıl boyunca günde 10 dolar ({{dcainv:5}}) bugün {{dca:btc:5}} ediyor ({{dcaroi:btc:5}}). Bu geçmiş, tahmin değil.

## Kaynaklar

- [CoinDesk — Bitcoin düğümleri tek bir kimliğin 50.000 kez tekrarıyla durdurulabiliyordu](https://www.coindesk.com/markets/2026/11/21/bitcoin-nodes-could-be-stalled-by-repeating-one-id-50-000-times-ai-found-the-bug)
- [The Defiant — Bitcoin Core yapay zekânın bulduğu hatayı düzeltti](https://thedefiant.io/news/security/bitcoin-core-fixes-ai-found-bug-that-could-stall-nodes)
- [Coinotag — Bitcoin Core 30.5 ve 31.3'te hatayı kapattı](https://en.coinotag.com/bitcoin-core-fixes-node-stall-cve-2026-117348)

*Yatırım tavsiyesi değildir.*

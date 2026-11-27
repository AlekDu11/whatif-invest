---
title: Fluid (FLUID) sade dille: Instadapp'in borç verme ve alım satım protokolü, 100 milyon token sınırı
description: Fluid sade dille: borç verme ve alım satım için ortak likidite katmanı nasıl çalışır, smart collateral ve smart debt, INST'ten geçiş, rakipler ve riskler.
date: 2026-11-27
kind: analysis
---
**Fluid**, insanların tek bir ortak para havuzundan kripto borç verdiği, borç aldığı ve takas yaptığı bir merkeziyetsiz finans (DeFi) protokolüdür. Ethereum'daki en eski DeFi uygulamalarından biri olan Instadapp'in ekibi tarafından geliştirildi ve 2025 başında eski INST tokenının adı FLUID olarak değiştirildi. Bugünkü piyasa değeri {{mcap:fluid}} (kripto paralar arasında {{rank:fluid}}).

> **Öne çıkanlar**
> - Toplam 100 milyon FLUID token var; INST'ten FLUID'e geçişte arz ve token adresi aynı kaldı.
> - Henüz INST iken ulaşılan rekor fiyatı {{ath:fluid}} ({{athd:fluid}}); bugün fiyat ondan {{fromath:fluid}} uzakta.
> - Fluid aynı mevduatın iki kez çalışmasını sağlar — hem kredi teminatı hem de alım satım likiditesi olarak — böylece kullanıcılar borç verme ve işlem ücretlerinden aynı anda kazanabilir.
> - Aralık 2024'te, lansmandan üç hafta sonra, borsasındaki işlem hacmi 1 milyar doları aşmıştı.

## Nasıl çalışır

Çoğu DeFi uygulaması borç verme ve alım satımı ayrı havuzlarda tutar. Fluid ise tüm mevduatları tek bir "likidite katmanına" koyar; para piyasası, kasalar (vaults) ve merkeziyetsiz borsa (DEX) gibi farklı uygulamalar buradan yararlanır. "Akıllı teminat" (smart collateral) sayesinde bir kredi için yatırdığınız coinler DEX'te alım satım likiditesi olarak da kullanılır ve takas ücreti kazanır. "Akıllı borç" (smart debt) sayesinde borç aldığınız tutar da likidite olarak çalıştırılır, böylece işlem ücretleri faizinizin bir kısmını karşılayabilir. Her şey akıllı sözleşmelerle, yani blokzincir üzerindeki programlarla çalışır; başta Ethereum olmak üzere Arbitrum ve Base gibi katman 2 ağlarında da. 2025'te Solana borsası Jupiter, Fluid'in teknolojisiyle geliştirilen borç verme uygulaması Jupiter Lend'i başlattı.

## Token ne işe yarar

FLUID bir yönetişim tokenıdır: sahipleri ücretler, yeni piyasalar ve hazinenin nasıl harcanacağı konusunda oy verir. Aralık 2024'teki yeniden markalaşma önerisi, protokol yıllık yaklaşık 10 milyon dolar gelire ulaştığında token geri alımlarını da öngörüyordu; böylece Fluid'in kazandığı ücretlerin bir kısmı tokena geri dönecekti. FLUID temettü ödemez; değeri, protokolün ne kadar kazandığına ve bunun ne kadarının sahiplere ulaştığına bağlıdır.

## Şu anki rakamlar

- Bugünkü fiyat: {{price:fluid}}
- Rekor: {{ath:fluid}} ({{athd:fluid}}), ondan {{fromath:fluid}}
- Piyasa değeri: {{mcap:fluid}} (kripto paralar arasında {{rank:fluid}})
- 12 aylık fiyat değişimi: {{chg1y:fluid}}
- 1 yıl boyunca günde 10 $: {{dca:fluid:1}}, yatırılan {{dcainv:1}} ({{dcaroi:fluid:1}})

## Hikâyesi

Instadapp, 2018'de Sowmay ve Samyak Jain kardeşler tarafından birkaç DeFi uygulamasını aynı anda kullanmaya yarayan basit bir panel olarak kuruldu. INST yönetişim tokenı Haziran 2021'de, DeFi patlamasının zirvesinde piyasaya çıktı, aynı ay yaklaşık 24 dolara ulaştı ve 2022 sonuna kadar değerinin %95'inden fazlasını kaybetti. Yaklaşık iki yıllık geliştirmenin ardından ekip, Fluid'in borç verme protokolünü 2024'te, DEX'ini ise Kasım 2024'te başlattı; DEX hacim bakımından kısa sürede Ethereum'un en büyük borsalarından biri oldu. Ardından sahipler INST'in FLUID'e bire bir dönüştürülmesini onayladı ve token 2025'ten itibaren FLUID olarak, çoğunlukla yaklaşık 1,50 ile 6 dolar arasında işlem gördü.

## Alternatifler

[Aave]({lang}/aave/) en büyük DeFi borç verme protokolüdür, [Morpho]({lang}/morpho/) ise hızla büyüyen bir rakip. Alım satımda Fluid'in DEX'i [Uniswap]({lang}/uni/) ve [Curve DAO]({lang}/crv/) ile rekabet eder. Solana'da [Jupiter]({lang}/jup/) hem iş ortağı hem de rakiptir.

## Başlıca riskler

- **Büyük dalgalanmalar:** token daha önce bir kez değerinin %95'inden fazlasını kaybetti; DeFi tokenları ayı piyasalarında hızla düşebilir.
- **Akıllı sözleşme riski:** tek bir ortak likidite katmanındaki bir hata ya da saldırı, borç verme ve alım satımı aynı anda vurabilir.
- **Likidasyonlar:** oynak coinlerle teminatlandırılan krediler fiyatlar düştüğünde otomatik olarak satılır; bu da bir çöküşte zincirleme tepkilere yol açabilir.
- **Sahiplere değer:** geri alımlar gelir hedeflerine ve yönetişim oylamalarına bağlıdır; ücretler tokena beklendiği gibi ulaşmayabilir.
- **Yoğunlaşma ve düzenleme:** ekip ve ilk yatırımcılar büyük bir pay tutuyor; DeFi kuralları birçok ülkede hâlâ yazılıyor.

## Düzenli alım yapıyorsanız bu ne anlama geliyor

FLUID olarak tokenın geçmişi kısa ve 2025'ten beri yapılan düzenli alımlar çoğunlukla düşen fiyatlardan gerçekleşti. Düzenli olarak sabit bir tutarla almak zamanlama riskini yayar, ancak sonuç yine de protokolün ücret gelirlerini büyütmeye devam edip etmeyeceğine bağlıdır. Pek çok kişi DeFi tokenlarını, sert düşüşünü kaldırabileceği küçük bir birikim payıyla sınırlar. Geçmiş getiriler gelecekteki kazancı garanti etmez.

*Yatırım tavsiyesi değildir.*

## Kaynaklar

- [Fluid resmî sitesi ve dokümantasyonu (fluid.io)](https://fluid.io/)
- [Instadapp proposes rebrand and new tokenomics following Fluid launch (The Defiant, 4 Aralık 2024)](https://thedefiant.io/news/defi/instadapp-proposes-rebrand-and-new-tokenomics-following-fluid-launch)
- [DeFi superapp Fluid is coming for Aave and Uniswap's lunch (Blockworks)](https://blockworks.co/news/defi-superapp-competitor-to-aave-uniswap)
- [Fluid fiyatı, piyasa değeri ve rekor fiyatı (CoinGecko)](https://www.coingecko.com/en/coins/instadapp)

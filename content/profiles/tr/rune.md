---
title: THORChain (RUNE) sade dille: gerçek bitcoin ve diğer coinlerin blokzincirler arasında takası, wrapped token olmadan
description: THORChain sade dille: zincirler arası takaslar ve RUNE havuzları, node teminatları, 2021 hackleri, 2025 borç verme dondurması, riskler ve düzenli alım.
date: 2026-11-26
kind: analysis
---
**THORChain (RUNE)**, farklı ağlar arasında coin takası yapmayı — örneğin gerçek bitcoini gerçek ether ile değiştirmeyi — merkezi bir borsa olmadan ve coinlerin "sarılmış" (wrapped) kopyalarına gerek kalmadan mümkün kılan bir blokzincirdir. RUNE bu sistemin merkezindeki token'dır: her işlem havuzu RUNE ile eşleşir ve ağı çalıştıran bilgisayarlar güvence depozitosu olarak RUNE kilitlemek zorundadır. Dolaşımdaki tüm RUNE'un bugünkü değeri {{mcap:rune}} (kripto paralar arasında {{rank:rune}}).

> **Öne çıkanlar**
> - THORChain; Bitcoin, Ethereum, BNB Chain, Dogecoin ve diğer zincirler arasında yerel varlıkları tek adımda takas eder.
> - Her likidite havuzu RUNE ile eşleşir ve node operatörleri, kurallara aykırı davranırlarsa ellerinden alınabilecek RUNE teminatı yatırır.
> - Rekor fiyatı {{ath:rune}} ({{athd:rune}}); bugün fiyat ondan {{fromath:rune}} uzakta.
> - Ağ 2021'de iki kez hacklendi ve Ocak 2025'te borç verme ve birikim ürünlerini dondurdu.

## Nasıl çalışır

THORChain, Cosmos SDK ile inşa edilmiştir. Bağımsız node'lardan oluşan bir grup, eşik imzalar sayesinde "kasaları" (vaults) — Bitcoin, Ethereum ve bağlı diğer zincirlerdeki adresleri — ortaklaşa kontrol eder; böylece hiçbir node fonları tek başına hareket ettiremez. BTC'yi ETH ile takas ettiğinizde bitcoini bir kasaya gönderirsiniz; ağ onu BTC havuzunda RUNE karşılığında satar, ardından bu RUNE'u ETH havuzunda ETH karşılığında satar ve bir kasa size gerçek ether gönderir. Fiyatlar, [Uniswap]({lang}/uni/)'te olduğu gibi havuz bakiyelerinden belirlenir. Likidite sağlayıcıları havuzlara coin yatırır ve takas ücretlerinden pay alır. Node'lar, korumaya yardım ettikleri fonlardan daha değerli RUNE'u teminat olarak yatırmak zorundadır; bunun amacı hırsızlığı kârsız hâle getirmektir.

## İnsanlar neden değeri olduğunu düşünüyor

Değeri blokzincirler arasında taşımak genellikle yavaş, riskli ya da hesap doğrulaması isteyen merkezi bir borsa gerektiren bir iştir. THORChain yerel coinler arasında doğrudan bir yol sunuyor; bu yüzden pek çok kripto cüzdan ve takas uygulaması işlemleri onun üzerinden yönlendiriyor. RUNE talebi üç kaynaktan geliyor: her havuzun yarısını oluşturuyor, node'ların yatırması gereken teminat o ve takas ücretlerinin bir kısmı onu tutan ve stake edenlere gidiyor. Dolayısıyla daha yüksek işlem hacmi, RUNE sahipleri için daha fazla ücret demek.

## Şu anki rakamlar

- Bugünkü fiyat: {{price:rune}}
- Rekor: {{ath:rune}} ({{athd:rune}}), ondan {{fromath:rune}}
- Piyasa değeri: {{mcap:rune}} (kripto paralar arasında {{rank:rune}})
- 12 aylık fiyat değişimi: {{chg1y:rune}}
- 5 yıl boyunca günde 10 $: {{dca:rune:5}}, yatırılan {{dcainv:5}} ({{dcaroi:rune:5}})

## Hikâyesi

RUNE ilk kez Temmuz 2019'da Binance Launchpad üzerinden satışa çıktı. 2020'de gerçek parayla çalışan ve bilerek sınırlandırılmış bir "chaosnet" devreye girdi, Nisan 2021'de ise çoklu zincir işlemleri başladı. 2021 yükselişinde RUNE Mayıs 2021'de yaklaşık 20 dolara ulaştı, ancak Temmuz 2021'de ağ milyonlarca dolarlık iki saldırıya uğradı. Tam mainnet Haziran 2022'de ilan edildi. Ocak 2025'te THORChain, yaklaşık 200 milyon dolarlık yükümlülük biriktiren borç verme ve "savers" ürünlerini durdurdu; borç daha sonra ayrı bir token olan TCY'ye dönüştürüldü. Şubat 2025'te Bybit borsasından 1,4 milyar dolarlık hırsızlığı gerçekleştiren hackerlar, çalınan etheri bitcoine çevirmek için THORChain'i kullandı; bu da rekor hacimler ve sert eleştiriler getirdi.

## Alternatifler

Merkezi borsalar, zincirler arasında takas yapmanın hâlâ en kolay yolu. Zincir üstü rakipler arasında köprü ve toplayıcı (aggregator) hizmetleri ile THORChain'in bir fork'u olan Maya Protocol bulunuyor. Tek bir ağ içindeki takaslar için insanlar [Uniswap]({lang}/uni/) veya [PancakeSwap]({lang}/cake/) gibi merkeziyetsiz borsaları kullanıyor. Blokzincirleri genel olarak birbirine bağlamak için [Cosmos]({lang}/atom/) ve [Chainlink]({lang}/link/) farklı yaklaşımlar sunuyor.

## Başlıca riskler

- **Büyük dalgalanmalar:** RUNE zirvesinden birden fazla kez yüzde 80'den fazla düştü.
- **Hackler:** zincirler arası kasalar büyük meblağlar tutuyor ve daha önce saldırıya uğradı; yeni bir hata kullanıcılara para kaybettirebilir.
- **Başarısız ürünler:** 2025'teki borç verme dondurması, yeni özelliklerin kullanıcılar için kayıplara ve RUNE üzerinde baskıya yol açabileceğini gösterdi.
- **Düzenleme:** hackerların fon aklamak için ağı kullanması düzenleyicilerin dikkatini çekiyor ve kısıtlamalara yol açabilir.
- **RUNE'a bağımlılık:** her havuz RUNE ile eşleştiği için RUNE'daki sert bir düşüş tüm sistemi vurur.

## Düzenli alım yapıyorsanız bu ne anlama geliyor

RUNE, insanların zincirler arası takaslar için THORChain'i kullanmaya devam edeceğine yönelik bir bahis; geçmişinde hızlı yükselişlerin yanı sıra hackler ve dondurulmuş bir ürün de var. Düzenli olarak sabit bir tutarla alım yapmak giriş fiyatınızı dengeler, ancak projeye özgü şoklardan sizi korumaz. Pek çok kişi RUNE gibi niş bir token'ı birikimlerinin küçük bir kısmıyla sınırlı tutuyor. Geçmiş sonuçlar gelecekteki getirileri garanti etmez.

*Yatırım tavsiyesi değildir.*

## Kaynaklar

- [THORChain dokümantasyonu — giriş (docs.thorchain.org)](https://docs.thorchain.org/)
- [THORChain kesintinin ardından takasların çoğunu yeniden başlatınca RUNE %15 yükseldi (Cointelegraph)](https://cointelegraph.com/markets/rune-rallies-15-as-thorchain-restarts-most-swaps-after-outage)
- [THORChain fiyatı, piyasa değeri ve tüm zamanların en yükseği (CoinGecko)](https://www.coingecko.com/en/coins/thorchain)

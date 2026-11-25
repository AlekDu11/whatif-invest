---
title: The Graph (GRT) sade dille: blokzincir verileri için indeksleme protokolü, 2020'den beri Ethereum ve Arbitrum'da
description: The Graph sade dille: indeksleyiciler blokzincir verisini nasıl hızlı sorgulara dönüştürür, GRT ne işe yarar, staking, delegasyon, hikâyesi ve riskler.
date: 2026-11-25
kind: analysis
---
**The Graph** sık sık "blokzincirlerin Google'ı" diye anılır: ham blokzincir verilerini, uygulamaların ihtiyaç duyduğunu milisaniyeler içinde bulabileceği şekilde düzenler. Cüzdanlar, borsalar ve DeFi uygulamaları kendi veri sunucularını çalıştırmadan bakiyeleri, işlemleri ve fiyatları göstermek için onu kullanır. **GRT** tokeni bu işin karşılığını öder ve ağı güvence altına alır; bugünkü değeri {{mcap:grt}} (kripto paralar arasında {{rank:grt}}).

> **Öne çıkanlar**
> - Ağ, Aralık 2020'de 10 milyar GRT ile yayına girdi; her yıl ödül olarak yeni tokenler basılıyor, yani sabit bir üst sınır yok.
> - Rekoru {{ath:grt}} ({{athd:grt}}); bugünkü fiyat ondan {{fromath:grt}}.
> - GRT bir iş tokenidir (work token): indeksleyiciler veri sunabilmek için onu stake etmek zorundadır, uygulamalar da sorgu ücretlerini onunla öder.
> - Bu bir para birimi değil, blokzincir verisine olan talep üzerine bir bahistir — kullanım ve fiyat çoğu zaman farklı yönlere gitti.

## Nasıl çalışır

Verileri doğrudan bir blokzincirden okumak yavaş ve zahmetlidir. The Graph'taki geliştiriciler ihtiyaç duydukları veriyi açık bir "subgraph" içinde tanımlar; örneğin merkeziyetsiz bir borsadaki her işlem. **İndeksleyiciler** — kendi sunucularını çalıştıran bağımsız operatörler — bu subgraph'ları işler ve uygulamalardan gelen sorguları yanıtlar; karşılığında ücret ve yeni basılan GRT kazanır. **Küratörler** hangi subgraph'ların indekslenmeye değer olduğuna dair sinyal verir; **delegatörler** ise GRT'lerini güvendikleri indeksleyicilere emanet ederek ödüllerden pay alır. Yanlış veri sunan indeksleyiciler stake ettikleri tokenlerin bir kısmını kaybedebilir ("slashing"). The Graph bugün onlarca blokzinciri destekliyor ve maliyetleri düşük tutmak için 2024'ten beri ödülleri ve ödemeleri bir Ethereum katman 2 ağı olan Arbitrum üzerinde çalışıyor. 2025'te proje, aynı staking sisteminin yeni veri hizmeti türlerini de güvence altına almasını sağlayan **Horizon** güncellemesini devreye almaya başladı.

## Token ne işe yarıyor

GRT'nin üç görevi var. İndeksleyiciler çalışmaya başlamadan önce onu stake etmek zorunda; bu da arzın büyük bir kısmını kilitliyor. Uygulamalar sorgular için GRT ile ödeme yapıyor (çoğu zaman stablecoin'lerden veya kart ödemelerinden otomatik olarak dönüştürülüyor). Sahipleri de sunucu çalıştırmadan ödüllerden pay almak için onu delege edebiliyor. Sorgu ücretlerinin ve staking vergilerinin küçük bir kısmı yakılırken yılda yaklaşık %3'lük yeni ihraç indeksleyicilere ve delegatörlere gidiyor. GRT'nin değer kazanıp kazanmayacağı, veriye yönelik ücretli talebin yeni arzdan daha hızlı büyüyüp büyümeyeceğine bağlı.

## Şu anki rakamlar

- Bugünkü fiyat: {{price:grt}}
- Rekor: {{ath:grt}} ({{athd:grt}}), ondan {{fromath:grt}}
- Piyasa değeri: {{mcap:grt}} (kripto paralar arasında {{rank:grt}})
- 12 aylık fiyat değişimi: {{chg1y:grt}}
- 5 yıl boyunca günde 10 $: {{dca:grt:5}}, yatırılan {{dcainv:5}} ({{dcaroi:grt:5}})

## Hikâyesi

The Graph, 2018'de Yaniv Tal, Brandon Ramirez ve Jannis Pohlmann tarafından kuruldu; şirketlerinin adı daha sonra Edge & Node oldu. Yıllarca pek çok Ethereum uygulamasının dayandığı ücretsiz bir "barındırılan hizmet" (hosted service) çalıştırdı. Merkeziyetsiz ağ ve GRT tokeni 17 Aralık 2020'de yayına girdi; kripto yükselişinde GRT, Şubat 2021'de yaklaşık 2,84 $'a çıktı. Ardından 2021 ve 2022 boyunca %90'dan fazla değer kaybetti. 2023 ve 2024'te proje ödüllerini Arbitrum'a taşıdı ve Haziran 2024'te barındırılan hizmeti kapatarak tüm kullanıcıları ücretli ağa geçirdi. 2024 başındaki yapay zekâ tokenleri rallisi GRT'yi bir süre yukarı taşıdı, ancak fiyat daha sonra yeni diplere geriledi.

## Alternatifler

The Graph; Goldsky, SubQuery ve Covalent gibi indeksleme şirketleri ve protokolleriyle, ayrıca birçok geliştiricinin daha basit bulduğu Alchemy ve QuickNode'un blokzincir veri API'leriyle rekabet ediyor. Bazı büyük uygulamalar ise kendi indeksleyicilerini çalıştırıyor. Blokzincir verisiyle ilişkili tokenler arasında [Chainlink]({lang}/link/) ve [Pyth Network]({lang}/pyth/) sık sık GRT ile karşılaştırılır; ancak bunlar geçmiş veriler üzerinde arama yerine akıllı sözleşmelere fiyat akışları sağlar.

## Başlıca riskler

- **Yeni arz:** yıllık ihraç yeni GRT ekliyor ve indeksleyiciler sunucu maliyetlerini karşılamak için ödüllerini sık sık satıyor.
- **Kullanımla zayıf bağ:** sorgu ücretleri uzun süredir ödüllere kıyasla küçük; bu yüzden yoğun kullanım tek başına fiyatı yükseltmiyor.
- **Rekabet:** merkezî veri sağlayıcıları hızlı ve ucuz; uygulamalar onlara kolayca geçebiliyor.
- **Tek bir şirkete bağımlılık:** geliştirmenin büyük kısmını hâlâ Edge & Node ve The Graph Foundation yönlendiriyor.
- **Düzenleme:** staking tokenleri ve ödülleriyle ilgili kurallar ülkeden ülkeye farklıdır ve değişebilir.

## Düzenli alım yapıyorsanız bu ne anlama geliyor

GRT ömrünün büyük bölümünü 2021 zirvesinin çok altında geçirdi; yani düzenli alım yapan biri giderek daha düşük fiyatlardan daha fazla token biriktirdi — bu ancak fiyat toparlanırsa karşılığını verir. Belirli bir tutarı düzenli olarak almak, yanlış zamanlama riskini dağıtır ama zarar riskini ortadan kaldırmaz. Pek çok kişi bu tür tokenleri birikimlerinin yalnızca küçük bir kısmı olarak tutar. Geçmiş sonuçlar gelecekteki getirilerin garantisi değildir.

*Yatırım tavsiyesi değildir.*

## Kaynaklar

- [The Graph hakkında (The Graph belgeleri)](https://thegraph.com/docs/en/about/)
- [Horizon uygulama rehberi: ağ katılımcıları için neler değişti (The Graph blogu)](https://thegraph.com/blog/horizon-implementation-guide/)
- [The Graph fiyatı, piyasa değeri ve tüm zamanların en yükseği (CoinGecko)](https://www.coingecko.com/en/coins/the-graph)

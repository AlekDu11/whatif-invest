---
title: Binance Wallet nasıl oluşturulur ve memecoin nasıl alınır? Adım adım
description: Binance uygulamasında Binance Wallet oluşturun, yedekleyin, hesabınızdan coin aktarın, token'ı kontrat adresiyle bulun ve takas yapın; güvenlik kontrolleriyle.
date: 2026-11-23T12:30:00Z
category: learn
track: memes
step: 5
assets: bnb, sol, doge
stat: 3
stat_label: anahtar parçası Binance Wallet'ı korur; girmek için 2'si gerekir
---
**Binance Wallet nasıl oluşturulur?** Binance uygulamasını açın, üstteki **Wallet** (cüzdan) sekmesine geçin, **Create Keyless Wallet** (anahtarsız cüzdan oluştur) düğmesine dokunun ve bir kurtarma şifresiyle yedekleyin. Birkaç dakika sürer, kurtarma ifadesi (seed phrase) gerekmez ve size memecoin gibi zincir üstü token'ları almak için kendi kontrolünüzde bir cüzdan (coin'leri borsanın değil, sizin kontrol ettiğiniz bir cüzdan) verir.

> **Öne çıkanlar**
> - Binance Wallet, Binance uygulamasının içindedir. Doğrulanmış bir Binance hesabı gerekir, ama cüzdandaki coin'ler sizin kontrolünüzdedir; yedekten siz sorumlusunuz.
> - "Anahtarsız" (MPC) bir cüzdandır: anahtar 3 parçaya bölünür; telefonunuzda, bulut yedeğinizde ve Binance'te. Herhangi 2'si cüzdanı açar.
> - Yedeklemeyi asla atlamayın. Telefonunuzu kaybeder **ve** kurtarma şifresini unutursanız, Binance cüzdanı geri getiremez.

Başlamadan önce: yeni memecoin'lerin çoğu değerinin neredeyse tamamını kaybeder. Yalnızca tamamen kaybetmeyi göze alabileceğiniz parayı kullanın. Bkz. [memecoin nedir]({lang}/blog/what-are-memecoins/).

## Neye ihtiyacınız var

- Resmî Binance uygulaması yüklü bir telefon (yalnızca App Store, Google Play ya da binance.com'dan indirin; sahte uygulamalar yaygın).
- Kimlik doğrulaması (KYC, yani kimliğinizi göstermek) tamamlanmış bir Binance hesabı. Henüz yoksa bağlantımızla kaydolabilirsiniz: [Binance Wallet](/go/binance-web3?from=learn&l=tr).
- Alım yapmak ve ağ ücretlerini ödemek için Binance hesabınızda biraz BNB ya da SOL.

## Adım 1 — Cüzdanı açın

1. Binance uygulamasına giriş yapın.
2. Ekranın üstünde **Exchange** (borsa) sekmesinden **Wallet** sekmesine geçin.
3. **Create Keyless Wallet** düğmesine dokunun. (Zaten başka bir cüzdanınız varsa diğer seçenek **Import Wallet**'tır (cüzdanı içe aktar); yeni başlayanların buna ihtiyacı yok.)

Oluşturma birkaç saniye sürer. Uygulama size 12 ya da 24 kelimelik kurtarma ifadesi göstermez; bunun yerine MPC kullanır (multi-party computation, çok taraflı hesaplama: anahtar, hiçbir zaman tek bir yerde durmayan parçalara bölünür).

## Adım 2 — Yedekleyin (bunu atlamayın)

Uygulama yedek parçanızı kaydetmek için üç yol sunar. Birini seçin:

- **iCloud ya da Google Drive.** Yalnızca sizin bildiğiniz bir **kurtarma şifresi** belirlersiniz. Parça bu şifreyle şifrelenip bulutunuza kaydedilir.
- **QR kod.** Bir kurtarma şifresi belirler ve bir QR kod kaydedersiniz; parça merkeziyetsiz bir bulutta saklanır.
- **Quick Backup** (hızlı yedek). Face ID ya da parmak iziyle onaylarsınız; şifre yoktur ama parçayı üçüncü taraf bir sağlayıcı tutar.

Kurtarma şifresini kâğıda yazın ve güvenli bir yerde saklayın. Sonra kontrol edin: **Settings** (ayarlar; Home ya da Assets ekranında sol üstte) → **Wallet Management** (cüzdan yönetimi). **Backed Up** (yedeklendi) etiketini görmelisiniz.

## Adım 3 — Coin'leri Binance'ten cüzdana aktarın

1. Cüzdanda **Receive** (al) → **Withdraw from Binance Exchange** (Binance borsasından çek) düğmesine dokunun.
2. Coin'i (örneğin BNB) **ve ağı** seçin (BNB için BNB Smart Chain, SOL için Solana). Ağ eşleşmelidir.
3. Tutarı girin. Uygulama onaylamadan önce ücreti ve net tutarı gösterir.
4. Paranın Spot mu yoksa Funding hesabından mı geleceğini seçin, **Withdraw** (çek) düğmesine dokunun, adresi ve ağı kontrol edin ve **Confirm** (onayla) deyin.

Küçük bir deneme tutarıyla başlayın. Onaylanmış bir transfer iptal edilemez. Cüzdanda her zaman biraz BNB ya da SOL bırakın: blokzincirdeki her işlem, başarısız olsa bile, bir ağ ücreti (gas) tutar.

## Adım 4 — Doğru token'ı kontrat adresiyle bulun

Birçok memecoin'in aynı ad ve logoya sahip kopyaları vardır. Tek güvenilir kimlik **kontrat adresidir** (her token'a özgü uzun bir harf ve rakam dizisi).

1. Adresi güvenilir bir kaynaktan alın: projenin doğrulanmış hesabı, büyük bir veri sitesi ya da [memecoin sayfamızdaki]({lang}/memes/) token sayfası.
2. Cüzdanın **Markets** (piyasalar) ya da **Trade** (işlem) ekranında, adı yazmak yerine adresi aramaya yapıştırın.
3. İlk ve son 4–6 karakteri kaynağınızla karşılaştırın.

## Adım 5 — Almadan önce token'ı kontrol edin

[Memecoin sayfamızda]({lang}/memes/) her token sayfası Binance'in güvenlik kontrolünü ve temel rakamları gösterir. Şunlara bakın:

- **Likidite**: işlem havuzunda ne kadar para olduğu. Düşük likidite = satamayabilirsiniz.
- **Sahipler ve ilk 10'un payı**: arzın çoğunu birkaç cüzdan tutuyorsa fiyatı çökertebilirler.
- **Yaş**: bir saat önce oluşturulmuş bir token piyango biletidir.
- **Uyarılar**: herhangi bir risk ya da güvenlik uyarısı çıkarsa durun.

Binance'in kendisi, Meme Rush'ta (yepyeni memecoin akışı) listelenen token'ları kontrol etmediğini söylüyor; yani kontrol size kalıyor. [Dolandırıcılık ve rug pull dersimiz]({lang}/blog/memecoin-scams-rug-pull/) uyarı işaretlerini sıralıyor.

## Adım 6 — Takas yapın

1. **Trade** → **Swap** (takas) ekranını açın. Ne ile ödeyeceğinizi (BNB) ve istediğiniz token'ı aynı ağda seçin.
2. Küçük bir tutar girin. Kuru, **slippage**'ı (işlem başarısız olmadan önce kabul ettiğiniz en büyük fiyat değişimi) ve ağ ücretini okuyun.
3. Bazı token'lar önce bir **Approve** (onay) adımı ister; küçük bir ücreti vardır.
4. **Swap**'a dokunun ve geçiş anahtarınız (passkey) ya da 2FA ile onaylayın.

Satmak için aynısını tersine yapın. En yeni token'ları görmek isterseniz Markets sekmesinde **Meme Rush** var: yepyeni token'lar orada bir "bonding curve" üzerinde işlem görür ve normal bir DEX'e (merkeziyetsiz borsa) "taşınana" kadar cüzdandan çıkarılamaz. Bu, piyasanın en riskli köşesidir.

> **⚠️ Dikkat**
> - **Yedek yok ya da şifre ekran görüntüsünde.** Telefonu ve şifreyi kaybederseniz coin'ler sonsuza dek gider.
> - **Yanlış ağ ya da yanlış adres.** Binance'in SSS sayfası, yanlış adrese gönderilen token'ların iade edilemeyeceğini söylüyor. Her zaman deneme tutarı gönderin.
> - **Sahte token'lar ve "destek" mesajları.** Yalnızca kontrat adresiyle arayın. Binance çalışanları kurtarma şifrenizi ya da cüzdanınızı bir sitede "doğrulamanızı" asla istemez.

Sonraki ders: Binance Wallet bir DEX sitesine nasıl bağlanır ve coin'ler Binance'e nasıl geri taşınır. Tüm dersleri [Öğren sayfasında]({lang}/learn/) görün.

## Kaynaklar

- [Binance: Frequently Asked Questions on Binance Wallet](https://www.binance.com/en/support/faq/5a3fc86a702b43e1a4a398ebd8853b77)
- [Binance: What Is a Keyless Wallet and Why Do I Need to Back It Up?](https://www.binance.com/en/support/faq/4efebcb9a937417ca31baa2f7754c50f)
- [Binance: How to Back Up My Binance Wallet?](https://www.binance.com/en/support/faq/53521dedad474c908ec3761a935cb8d6)
- [Binance: How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance: What Is Binance Wallet Swap?](https://www.binance.com/en/support/faq/7ebe19e8ff884cc09a9dbb064aff131f)
- [Binance: Introducing Meme Rush — Fair Mode (9 Oct 2025)](https://www.binance.com/en/support/announcement/detail/c21eac66543c4a62b8b6868cb01ba4f3)

*Yatırım tavsiyesi değildir. Memecoin'ler son derece risklidir; bu rehber uygulamanın nasıl çalıştığını anlatır ve herhangi bir token'ın alınmasını önermez. Binance Wallet her ülkede kullanılamayabilir.*

---
title: "İki faktörlü doğrulama (2FA): adım adım nasıl açılır"
description: 2FA, borsa hesabınıza ikinci bir kilit ekler. Doğrulama uygulaması veya passkey adım adım nasıl açılır ve SMS kodları neden en zayıf seçenektir.
date: 2026-11-27T12:30:00Z
category: learn
track: safety
step: 10
assets: btc, eth
stat: 68 milyon $
stat_label: 2021'de SIM swap dolandırıcılığına kaybedildi; FBI'a 1.611 şikâyet (IC3, Şubat 2022)
---
**2FA nedir ve nasıl açılır?** İki faktörlü doğrulama (2FA), giriş yapmak ya da para çekmek için iki şey gerektiği anlamına gelir: şifreniz *ve* ikinci bir kanıt — örneğin telefonunuzdaki bir uygulamanın ürettiği 6 haneli kod ya da bir passkey (parmak iziniz veya yüzünüz). Borsanızın **Security** (Güvenlik) ayarlarından açın ve SMS yerine bir doğrulama uygulaması ya da passkey kullanın.

> **Öne çıkanlar**
> - 2FA açıkken, çalınan şifre tek başına hesabınızı boşaltmaya yetmez.
> - **SMS kodları en zayıf seçenektir:** "SIM swap" (SIM kart değiştirme) dolandırıcılığında suçlu, telefon numaranızı kendi SIM kartına taşır ve kodlarınızı o alır. FBI 2021'de bu türden 1.611 şikâyet ve **68 milyon doların** üzerinde kayıp kaydetti; 2018–2020 döneminde ise 320 şikâyet ve yaklaşık 12 milyon dolar vardı.
> - FBI daha güçlü seçenekler öneriyor: doğrulama uygulaması, biyometri ya da fiziksel güvenlik anahtarı.

## En zayıftan en güçlüye seçenekler

- **SMS kodu** — kod içeren bir kısa mesaj. Hiç yoktan iyidir ama telefon numaranız çalınabilir.
- **E-posta kodu** — ancak e-posta hesabınız kadar güvenlidir (onu da 2FA ile koruyun).
- **Doğrulama uygulaması** (Google Authenticator, Microsoft Authenticator ve benzerleri) — uygulama her 30 saniyede bir, çevrimdışıyken bile yeni bir 6 haneli kod üretir. Kimse onu telefon operatörünüz üzerinden ele geçiremez.
- **Passkey** (geçiş anahtarı, biyometri) — parmak iziniz, yüzünüz veya telefon PIN'inizle onaylarsınız. Yalnızca gerçek sitede çalışır, bu yüzden sahte bir site onu çalamaz.
- **Fiziksel güvenlik anahtarı** (küçük bir USB/NFC cihazı) — en güçlüsü, büyük tutarlar için iyi bir seçim.

## Adım adım: doğrulama uygulaması (örnek olarak Binance uygulaması)

Diğer borsalarda da adımlar hemen hemen aynıdır; profilinizde **Security** (Güvenlik) bölümünü arayın.

1. **Adım 1 — Uygulamayı kurun.** Google Authenticator'ı (veya başka bir doğrulama uygulamasını) resmi App Store ya da Google Play'den indirin.
2. **Adım 2 — Güvenlik ayarlarını açın.** Binance uygulamasında **Account** simgesine, ardından en üstteki profilinize, sonra **Security**'ye dokunun.
3. **Adım 3 — Kurulumu başlatın.** **Authenticator App**'e, ardından **Enable**'a dokunun. Bir QR kod ve bir **setup key** (kurulum anahtarı, uzun bir kod) göreceksiniz.
4. **Adım 4 — Kurulum anahtarını kâğıda yazın.** Telefonunuzu kaybederseniz yedeğiniz budur. Bir seed phrase gibi çevrimdışı saklayın. Henüz **Next**'e dokunmayın.
5. **Adım 5 — Hesabı doğrulama uygulamasına ekleyin.** Google Authenticator'da **+**'ya dokunun, **Enter a setup key** (Kurulum anahtarı girin) seçeneğini seçin (ya da QR kodu tarayın), anahtarı yapıştırın, "Binance" gibi bir ad yazın ve **Add**'e dokunun.
6. **Adım 6 — Onaylayın.** Binance'e dönüp **Next**'e dokunun ve uygulamadaki 6 haneli kodu yazın. Başarılı olduğunu gösteren bir mesaj göreceksiniz.
7. **Adım 7 — Deneyin.** Çıkış yapıp yeniden giriş yapın. Sizden kod isteniyorsa çalışıyor demektir.

## Adım adım: passkey (daha da basit)

Binance'in yardım sayfasına göre uygulamanın 2.60 veya üstü sürümü, iOS 16+ ya da Android 9+ gerekir.

1. **Account → profil → Security → Passkeys (Biometrics) → Add Passkey.**
2. İstenirse mevcut 2FA'nızla onaylayın ve **Continue**'ya dokunun.
3. Nereye kaydedileceğini seçin: iCloud Anahtar Zinciri (iPhone), Google Şifre Yöneticisi (Android) ya da bir güvenlik anahtarı; ardından parmak iziniz, yüzünüz veya PIN'inizle onaylayın.

## 2FA açıldıktan sonra

- Borsa izin veriyorsa SMS'i giriş yöntemi olarak kapatın ya da en azından operatörünüzden SIM kilidi / numara taşıma şifresi isteyin.
- Borsaya bağlı e-posta adresinizi de 2FA ile koruyun.
- Borsanızda varsa **çekim beyaz listesini** (yalnızca kayıtlı adresler para alabilir) açın.

> **⚠️ Dikkat**
> - **Gerçek hiç kimse 2FA kodunuzu istemez.** Telegram'daki "destek", "borsadan" ya da "bankadan" arayıp 6 haneli kodu isteyen kişi her zaman dolandırıcıdır.
> - **Yedek anahtar olmadan telefonu kaybetmek.** Bu durumda hesabı kurtarmak günlerce kimlik kontrolü gerektirir. Kurulum anahtarını kâğıda yazın ve güvenli bir yerde saklayın.
> - **Sahte doğrulama uygulamaları ve taklit giriş sayfaları.** Uygulamaları yalnızca resmi mağazadan kurun ve borsanın adresini kendiniz yazın ya da yer imi kullanın.

## Düzenli alım yapıyorsanız bu ne anlama geliyor

Her ay biraz alıyorsanız borsa hesabınız yavaş yavaş gerçek bir tutara dönüşür — örneğin bitcoin şu anda {{price:btc}} ({{chg1y:btc}} 12 ayda); geçmiş sonuçlardır, tahmin değildir. On dakikalık 2FA kurulumu yılların alımlarını korur. Elinizdekileri [portföy sayfanızda]({lang}/me/) takip edin.

Önceki ders: [seed phrase: güvende tutmak için 5 kural]({lang}/blog/seed-phrase-safety-rules/). Daha fazlası: [kripto borsasına nasıl kayıt olunur]({lang}/blog/how-to-register-on-a-crypto-exchange/), [ülkenizde çalışan borsalar]({lang}/exchanges/). Tüm dersler [Öğren sayfasında]({lang}/learn/).

## Kaynaklar

- [FBI IC3: Criminals increasing SIM swap schemes to steal millions (8 Şubat 2022)](https://www.ic3.gov/PSA/2022/PSA220208)
- [Binance Support: How to enable Google Authenticator for 2FA on the Binance app (güncelleme: 10 Aralık 2025)](https://www.binance.com/en/support/faq/f3b1adaed1c846bbbba0f3650ad23e45)
- [Binance Support: How to create a passkey for my Binance account (güncelleme: 10 Aralık 2025)](https://www.binance.com/en/support/faq/2aec8fe0437242f2a5fbef9cdb71d4c2)

*Yatırım tavsiyesi değildir.*

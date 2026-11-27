---
title: "Two-factor authentication (2FA): paano ito i-on, step by step"
description: Dagdag na pangalawang lock sa exchange account mo ang 2FA. Paano i-on ang authenticator app o passkey step by step, at bakit pinakamahina ang SMS codes.
date: 2026-11-27T12:30:00Z
category: learn
track: safety
step: 10
assets: btc, eth
stat: $68M
stat_label: nawala sa SIM-swap fraud noong 2021 sa 1,611 reklamo sa FBI (IC3, Pebrero 2022)
---
**Ano ang 2FA at paano ito i-on?** Ang two-factor authentication (2FA) ay nangangahulugang kailangan ng dalawang bagay para mag-log in o mag-withdraw: ang password mo *at* isang pangalawang patunay, gaya ng 6-digit code mula sa app sa phone mo o passkey (fingerprint o mukha mo). I-on ito sa **Security** settings ng exchange mo at gumamit ng authenticator app o passkey sa halip na SMS.

> **Mahahalagang punto**
> - Kapag may 2FA, hindi sapat ang ninakaw na password lang para maubos ang laman ng account mo.
> - **Pinakamahina ang SMS codes:** sa "SIM swap", inililipat ng kriminal ang phone number mo sa sarili niyang SIM card at siya na ang tumatanggap ng codes mo. Nagtala ang FBI ng 1,611 ganitong reklamo at mahigit **$68 milyon** na nawala noong 2021, mula sa 320 reklamo at mga $12 milyon noong 2018–2020.
> - Inirerekomenda ng FBI ang mas matitibay na opsyon: authenticator app, biometrics o physical security key.

## Ang mga opsyon, mula pinakamahina hanggang pinakamatibay

- **SMS code** — text message na may code. Mas mabuti kaysa wala, pero puwedeng manakaw ang phone number mo.
- **E-mail code** — kasing-ligtas lang ng e-mail account mo (protektahan din ito ng 2FA).
- **Authenticator app** (Google Authenticator, Microsoft Authenticator at mga katulad) — gumagawa ang app sa phone ng bagong 6-digit code kada 30 segundo, kahit offline. Walang makakaharang nito sa pamamagitan ng telco mo.
- **Passkey** (biometrics) — kinukumpirma mo gamit ang fingerprint, mukha o PIN ng phone. Gumagana lang ito sa tunay na site, kaya hindi ito kayang nakawin ng pekeng site.
- **Physical security key** (maliit na USB/NFC device) — ang pinakamatibay, mainam para sa malalaking halaga.

## Step-by-step: authenticator app (Binance app bilang halimbawa)

Halos pareho ang steps sa ibang exchanges; hanapin ang **Security** sa profile mo.

1. **Hakbang 1 — I-install ang app.** I-download ang Google Authenticator (o ibang authenticator app) mula sa official na App Store o Google Play.
2. **Hakbang 2 — Buksan ang security settings.** Sa Binance app, i-tap ang **Account** icon, i-tap ang profile mo sa itaas, tapos **Security**.
3. **Hakbang 3 — Simulan ang setup.** I-tap ang **Authenticator App**, tapos **Enable**. Makakakita ka ng QR code at **setup key** (isang mahabang code).
4. **Hakbang 4 — Isulat sa papel ang setup key.** Ito ang backup mo kapag nawala ang phone mo. Itago ito offline, gaya ng seed phrase. Huwag munang i-tap ang **Next**.
5. **Hakbang 5 — Idagdag ang account sa authenticator.** Sa Google Authenticator, i-tap ang **+**, piliin ang **Enter a setup key** (o i-scan ang QR code), i-paste ang key, mag-type ng pangalan gaya ng "Binance", at i-tap ang **Add**.
6. **Hakbang 6 — Kumpirmahin.** Bumalik sa Binance, i-tap ang **Next** at i-type ang 6-digit code mula sa app. Makakakita ka ng success message.
7. **Hakbang 7 — Subukan.** Mag-log out at mag-log in ulit. Kung hihingan ka ng code, gumagana na ito.

## Step-by-step: passkey (mas simple pa)

Ayon sa help page ng Binance, kailangan mo ng app version 2.60+, iOS 16+ o Android 9+.

1. **Account → profile → Security → Passkeys (Biometrics) → Add Passkey.**
2. Kumpirmahin gamit ang kasalukuyan mong 2FA kung hihingin, tapos i-tap ang **Continue**.
3. Piliin kung saan ito ise-save: iCloud Keychain (iPhone), Google Password Manager (Android) o security key, at kumpirmahin gamit ang fingerprint, mukha o PIN.

## Pagkatapos i-on ang 2FA

- I-off ang SMS bilang login method kung pinapayagan ng exchange, o kahit man lang humingi sa telco mo ng SIM lock / port-out PIN.
- Protektahan din ng 2FA ang e-mail na naka-link sa exchange.
- I-on ang **withdrawal whitelist** (mga naka-save na address lang ang puwedeng tumanggap) kung mayroon nito ang exchange mo.

> **⚠️ Mag-ingat**
> - **Walang totoong tao na hihingi ng 2FA code mo.** Ang "support" sa Telegram, o tumatawag mula sa "exchange" o "bangko" na humihingi ng 6-digit code ay laging scammer.
> - **Nawalan ng phone nang walang backup key.** Ilang araw ng ID checks ang aabutin bago mabawi ang account. Isulat ang setup key sa papel at itago nang maayos.
> - **Pekeng authenticator apps at kamukhang login pages.** Mag-install lang ng apps mula sa official store at ikaw mismo ang mag-type ng address ng exchange, o gumamit ng bookmark.

## Ano ang ibig sabihin nito kung regular kang bumibili

Kung bumibili ka nang kaunti bawat buwan, unti-unting nagiging tunay na halaga ang exchange account mo — halimbawa, ang bitcoin ay nasa {{price:btc}} ngayon ({{chg1y:btc}} sa loob ng 12 buwan), nakaraang resulta, hindi hula. Sampung minuto ng 2FA setup ang nagpoprotekta sa maraming taon ng pagbili. I-track ang hawak mo sa iyong [portfolio page]({lang}/me/).

Nakaraang aralin: [seed phrase: 5 patakaran para manatili itong ligtas]({lang}/blog/seed-phrase-safety-rules/). Dagdag pa: [paano mag-register sa crypto exchange]({lang}/blog/how-to-register-on-a-crypto-exchange/), [mga exchange na gumagana sa bansa mo]({lang}/exchanges/). Lahat ng aralin ay nasa [Learn page]({lang}/learn/).

## Mga pinagkunan

- [FBI IC3: Criminals increasing SIM swap schemes to steal millions (Pebrero 8, 2022)](https://www.ic3.gov/PSA/2022/PSA220208)
- [Binance Support: How to enable Google Authenticator for 2FA on the Binance app (in-update Disyembre 10, 2025)](https://www.binance.com/en/support/faq/f3b1adaed1c846bbbba0f3650ad23e45)
- [Binance Support: How to create a passkey for my Binance account (in-update Disyembre 10, 2025)](https://www.binance.com/en/support/faq/2aec8fe0437242f2a5fbef9cdb71d4c2)

*Hindi ito payo sa pamumuhunan.*

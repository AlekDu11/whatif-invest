---
title: "Tweestapsverificatie (2FA): zo zet je het stap voor stap aan"
description: 2FA zet een tweede slot op je exchange-account. Zo zet je stap voor stap een authenticator-app of passkey aan, en daarom zijn sms-codes de zwakste optie.
date: 2026-11-27T12:30:00Z
category: learn
track: safety
step: 10
assets: btc, eth
stat: $68 mln
stat_label: verloren aan SIM-swapfraude in 2021, in 1.611 klachten bij de FBI (IC3, februari 2022)
---
**Wat is 2FA en hoe zet je het aan?** Tweestapsverificatie (2FA) betekent dat je voor inloggen of opnemen twee dingen nodig hebt: je wachtwoord *en* een tweede bewijs, zoals een 6-cijferige code uit een app op je telefoon of een passkey (je vingerafdruk of gezicht). Zet het aan in de **Security**-instellingen (Beveiliging) van je exchange en kies een authenticator-app of passkey in plaats van sms.

> **Belangrijkste punten**
> - Met 2FA is een gestolen wachtwoord alleen niet genoeg om je account leeg te halen.
> - **Sms-codes zijn de zwakste optie:** bij een "SIM swap" zet een crimineel jouw telefoonnummer over naar zijn eigen simkaart en ontvangt hij jouw codes. De FBI registreerde in 2021 1.611 van zulke klachten en meer dan **$68 miljoen** aan verliezen, tegenover 320 klachten en zo'n $12 miljoen in 2018–2020.
> - De FBI raadt sterkere opties aan: een authenticator-app, biometrie of een fysieke beveiligingssleutel.

## De opties, van zwak naar sterk

- **Sms-code** — een sms met een code. Beter dan niets, maar je telefoonnummer kan gestolen worden.
- **Code per e-mail** — net zo veilig als je e-mailaccount (bescherm dat ook met 2FA).
- **Authenticator-app** (Google Authenticator, Microsoft Authenticator en vergelijkbare apps) — de app maakt elke 30 seconden een nieuwe 6-cijferige code, ook offline. Niemand kan die onderscheppen via je telecomprovider.
- **Passkey** (biometrie) — je bevestigt met je vingerafdruk, gezicht of de pincode van je telefoon. Een passkey werkt alleen op de echte site, dus een nepsite kan hem niet stelen.
- **Fysieke beveiligingssleutel** (een klein USB/NFC-apparaatje) — de sterkste optie, goed voor grote bedragen.

## Stap voor stap: authenticator-app (met de Binance-app als voorbeeld)

Andere exchanges werken bijna hetzelfde; zoek naar **Security** (Beveiliging) in je profiel.

1. **Stap 1 — Installeer de app.** Download Google Authenticator (of een andere authenticator-app) uit de officiële App Store of Google Play.
2. **Stap 2 — Open de beveiligingsinstellingen.** Tik in de Binance-app op het icoon **Account**, tik bovenaan op je profiel en daarna op **Security**.
3. **Stap 3 — Start de installatie.** Tik op **Authenticator App** en dan op **Enable**. Je ziet een QR-code en een **setup key** (instelsleutel, een lange code).
4. **Stap 4 — Schrijf de instelsleutel op papier.** Dit is je reserve als je je telefoon kwijtraakt. Bewaar hem offline, net als een seed phrase. Tik nog niet op **Next**.
5. **Stap 5 — Voeg het account toe in de authenticator.** Tik in Google Authenticator op **+**, kies **Enter a setup key** (of scan de QR-code), plak de sleutel, typ een naam zoals "Binance" en tik op **Add**.
6. **Stap 6 — Bevestig.** Ga terug naar Binance, tik op **Next** en typ de 6-cijferige code uit de app. Je ziet een melding dat het gelukt is.
7. **Stap 7 — Test het.** Log uit en log opnieuw in. Wordt er om de code gevraagd, dan werkt het.

## Stap voor stap: passkey (nog eenvoudiger)

Volgens de helppagina van Binance heb je app-versie 2.60 of hoger nodig, iOS 16+ of Android 9+.

1. **Account → profiel → Security → Passkeys (Biometrics) → Add Passkey.**
2. Bevestig met je huidige 2FA als daarom gevraagd wordt en tik op **Continue**.
3. Kies waar je hem opslaat: iCloud-sleutelhanger (iPhone), Google Wachtwoordmanager (Android) of een beveiligingssleutel, en bevestig met je vingerafdruk, gezicht of pincode.

## Als 2FA aanstaat

- Zet sms als inlogmethode uit als de exchange dat toestaat, of vraag je provider in elk geval om een simslot / extra pincode tegen het overzetten van je nummer.
- Bescherm ook het e-mailadres dat aan de exchange gekoppeld is met 2FA.
- Zet een **whitelist voor opnames** aan (alleen opgeslagen adressen kunnen ontvangen) als je exchange die heeft.

> **⚠️ Let op**
> - **Niemand die echt is, vraagt om je 2FA-code.** Een "support" op Telegram, iemand die belt namens "de exchange" of "de bank" en om de 6-cijferige code vraagt, is altijd een oplichter.
> - **Je telefoon kwijtraken zonder de reservesleutel.** Herstel kost dan dagen aan identiteitscontroles. Schrijf de instelsleutel op papier en bewaar hem veilig.
> - **Nep-authenticator-apps en nagemaakte inlogpagina's.** Installeer apps alleen uit de officiële store en typ het adres van de exchange zelf in, of gebruik een bladwijzer.

## Wat het betekent als je regelmatig koopt

Koop je elke maand een beetje, dan wordt je exchange-account langzaam een echt bedrag — bitcoin staat bijvoorbeeld nu op {{price:btc}} ({{chg1y:btc}} in 12 maanden), resultaten uit het verleden, geen voorspelling. Tien minuten 2FA instellen beschermt jaren aan aankopen. Volg wat je bezit op je [portfoliopagina]({lang}/me/).

Vorige les: [seed phrase: 5 regels om hem veilig te bewaren]({lang}/blog/seed-phrase-safety-rules/). Meer: [zo registreer je je bij een crypto-exchange]({lang}/blog/how-to-register-on-a-crypto-exchange/), [exchanges die in jouw land werken]({lang}/exchanges/). Alle lessen staan op de [pagina Leren]({lang}/learn/).

## Bronnen

- [FBI IC3: Criminals increasing SIM swap schemes to steal millions (8 februari 2022)](https://www.ic3.gov/PSA/2022/PSA220208)
- [Binance Support: How to enable Google Authenticator for 2FA on the Binance app (bijgewerkt op 10 december 2025)](https://www.binance.com/en/support/faq/f3b1adaed1c846bbbba0f3650ad23e45)
- [Binance Support: How to create a passkey for my Binance account (bijgewerkt op 10 december 2025)](https://www.binance.com/en/support/faq/2aec8fe0437242f2a5fbef9cdb71d4c2)

*Geen beleggingsadvies.*

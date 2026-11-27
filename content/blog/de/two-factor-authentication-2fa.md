---
title: "Zwei-Faktor-Authentifizierung (2FA): so aktivieren Sie sie Schritt für Schritt"
description: 2FA ist ein zweites Schloss für Ihr Börsenkonto. So aktivieren Sie eine Authenticator-App oder einen Passkey — und warum SMS-Codes am schwächsten sind.
date: 2026-11-27T12:30:00Z
category: learn
track: safety
step: 10
assets: btc, eth
stat: 68 Mio. $
stat_label: Verluste durch SIM-Swap-Betrug im Jahr 2021 laut 1.611 Beschwerden beim FBI (IC3, Februar 2022)
---
**Was ist 2FA, und wie aktivieren Sie sie?** Zwei-Faktor-Authentifizierung (2FA) bedeutet, dass Sie für Login oder Auszahlung zwei Dinge brauchen: Ihr Passwort *und* einen zweiten Nachweis, etwa einen 6-stelligen Code aus einer App auf dem Handy oder einen Passkey (Fingerabdruck oder Gesicht). Aktivieren Sie sie in den **Security**-Einstellungen (Sicherheit) Ihrer Börse und nutzen Sie lieber eine Authenticator-App oder einen Passkey statt SMS.

> **Das Wichtigste**
> - Mit 2FA reicht ein gestohlenes Passwort allein nicht aus, um Ihr Konto leerzuräumen.
> - **SMS-Codes sind die schwächste Option:** Beim „SIM-Swap“ lässt ein Betrüger Ihre Telefonnummer auf seine SIM-Karte übertragen und empfängt Ihre Codes. Das FBI verzeichnete 2021 1.611 solcher Beschwerden und über **68 Millionen Dollar** Verluste — nach 320 Beschwerden und rund 12 Millionen Dollar in 2018–2020.
> - Das FBI empfiehlt stärkere Optionen: eine Authenticator-App, Biometrie oder einen physischen Sicherheitsschlüssel.

## Die Optionen, von der schwächsten zur stärksten

- **SMS-Code** — eine Textnachricht mit einem Code. Besser als nichts, aber Ihre Telefonnummer kann gestohlen werden.
- **E-Mail-Code** — nur so sicher wie Ihr E-Mail-Konto (schützen Sie es ebenfalls mit 2FA).
- **Authenticator-App** (Google Authenticator, Microsoft Authenticator und ähnliche) — die App auf dem Handy erzeugt alle 30 Sekunden einen neuen 6-stelligen Code, sogar offline. Über Ihren Mobilfunkanbieter kann ihn niemand abfangen.
- **Passkey** (Biometrie) — Sie bestätigen mit Fingerabdruck, Gesicht oder Handy-PIN. Er funktioniert nur auf der echten Website, daher kann eine gefälschte Seite ihn nicht stehlen.
- **Physischer Sicherheitsschlüssel** (ein kleines USB-/NFC-Gerät) — die stärkste Option, gut für größere Beträge.

## Schritt für Schritt: Authenticator-App (am Beispiel der Binance-App)

Andere Börsen nutzen fast dieselben Schritte; suchen Sie in Ihrem Profil nach **Security** (Sicherheit).

1. **Schritt 1 — App installieren.** Laden Sie Google Authenticator (oder eine andere Authenticator-App) aus dem offiziellen App Store oder Google Play herunter.
2. **Schritt 2 — Sicherheitseinstellungen öffnen.** Tippen Sie in der Binance-App auf das Symbol **Account** (Konto), oben auf Ihr Profil und dann auf **Security** (Sicherheit).
3. **Schritt 3 — Einrichtung starten.** Tippen Sie auf **Authenticator App** und dann auf **Enable** (Aktivieren). Sie sehen einen QR-Code und einen **Einrichtungsschlüssel** (setup key, ein langer Code).
4. **Schritt 4 — Einrichtungsschlüssel auf Papier notieren.** Das ist Ihr Backup, falls Sie das Handy verlieren. Bewahren Sie ihn offline auf, wie eine Seed-Phrase. Tippen Sie noch nicht auf **Next** (Weiter).
5. **Schritt 5 — Konto im Authenticator hinzufügen.** Tippen Sie in Google Authenticator auf **+**, wählen Sie **Enter a setup key** (Einrichtungsschlüssel eingeben) oder scannen Sie den QR-Code, fügen Sie den Schlüssel ein, geben Sie einen Namen wie „Binance“ ein und tippen Sie auf **Add** (Hinzufügen).
6. **Schritt 6 — Bestätigen.** Zurück in Binance tippen Sie auf **Next** (Weiter) und geben den 6-stelligen Code aus der App ein. Sie sehen eine Erfolgsmeldung.
7. **Schritt 7 — Testen.** Melden Sie sich ab und wieder an. Werden Sie nach dem Code gefragt, funktioniert es.

## Schritt für Schritt: Passkey (noch einfacher)

Laut Binance-Hilfeseite brauchen Sie App-Version 2.60+, iOS 16+ oder Android 9+.

1. **Account → Profil → Security → Passkeys (Biometrics) → Add Passkey** (Konto → Profil → Sicherheit → Passkeys (Biometrie) → Passkey hinzufügen).
2. Bestätigen Sie, falls verlangt, mit Ihrer bisherigen 2FA und tippen Sie auf **Continue** (Fortfahren).
3. Wählen Sie, wo er gespeichert wird: iCloud-Schlüsselbund (iPhone), Google Passwortmanager (Android) oder ein Sicherheitsschlüssel — und bestätigen Sie mit Fingerabdruck, Gesicht oder PIN.

## Wenn 2FA aktiv ist

- Schalten Sie SMS als Login-Methode ab, wenn die Börse das erlaubt, oder bitten Sie zumindest Ihren Mobilfunkanbieter um eine Sperre gegen SIM-Tausch und Rufnummernmitnahme ohne Ihre Zustimmung (SIM-Sperre / Portierungs-PIN).
- Schützen Sie auch die mit der Börse verknüpfte E-Mail-Adresse mit 2FA.
- Aktivieren Sie eine **Auszahlungs-Whitelist** (withdrawal whitelist: nur gespeicherte Adressen können Geld empfangen), wenn Ihre Börse eine anbietet.

> **⚠️ Vorsicht**
> - **Niemand Seriöses fragt nach Ihrem 2FA-Code.** Ein „Support“ in Telegram oder ein Anruf „von der Börse“ oder „von der Bank“, der den 6-stelligen Code will, ist immer ein Betrüger.
> - **Handy verloren ohne Backup-Schlüssel.** Die Wiederherstellung dauert dann Tage mit Identitätsprüfungen. Schreiben Sie den Einrichtungsschlüssel auf Papier und bewahren Sie ihn sicher auf.
> - **Gefälschte Authenticator-Apps und nachgemachte Login-Seiten.** Installieren Sie Apps nur aus dem offiziellen Store und tippen Sie die Adresse der Börse selbst ein oder nutzen Sie ein Lesezeichen.

## Was das bedeutet, wenn Sie regelmäßig kaufen

Wenn Sie jeden Monat ein wenig kaufen, wird Ihr Börsenkonto nach und nach zu einer echten Summe — Bitcoin steht zum Beispiel gerade bei {{price:btc}} ({{chg1y:btc}} in 12 Monaten); vergangene Ergebnisse, keine Prognose. Zehn Minuten für die 2FA-Einrichtung schützen Jahre an Käufen. Verfolgen Sie Ihre Bestände auf Ihrer [Portfolio-Seite]({lang}/me/).

Vorherige Lektion: [Seed-Phrase: 5 Regeln, um sie sicher aufzubewahren]({lang}/blog/seed-phrase-safety-rules/). Mehr: [bei einer Krypto-Börse registrieren]({lang}/blog/how-to-register-on-a-crypto-exchange/), [Börsen, die in Ihrem Land funktionieren]({lang}/exchanges/). Alle Lektionen finden Sie auf der [Lernen-Seite]({lang}/learn/).

## Quellen

- [FBI IC3: Criminals increasing SIM swap schemes to steal millions (8. Februar 2022)](https://www.ic3.gov/PSA/2022/PSA220208)
- [Binance-Support: How to enable Google Authenticator for 2FA on the Binance app (aktualisiert am 10. Dezember 2025)](https://www.binance.com/en/support/faq/f3b1adaed1c846bbbba0f3650ad23e45)
- [Binance-Support: How to create a passkey for my Binance account (aktualisiert am 10. Dezember 2025)](https://www.binance.com/en/support/faq/2aec8fe0437242f2a5fbef9cdb71d4c2)

*Keine Anlageberatung.*

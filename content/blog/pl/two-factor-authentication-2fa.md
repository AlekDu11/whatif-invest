---
title: "Uwierzytelnianie dwuskładnikowe (2FA): jak je włączyć krok po kroku"
description: 2FA to drugi zamek na koncie na giełdzie. Jak krok po kroku włączyć aplikację uwierzytelniającą lub passkey i dlaczego kody SMS to najsłabsza opcja.
date: 2026-11-27T12:30:00Z
category: learn
track: safety
step: 10
assets: btc, eth
stat: 68 mln $
stat_label: stracono w 2021 r. przez oszustwa typu SIM swap, w 1611 zgłoszeniach do FBI (IC3, luty 2022)
---
**Czym jest 2FA i jak ją włączyć?** Uwierzytelnianie dwuskładnikowe (2FA) oznacza, że do logowania albo wypłaty potrzebujesz dwóch rzeczy: hasła *i* drugiego dowodu, np. 6-cyfrowego kodu z aplikacji na telefonie albo passkey (klucza dostępu — Twojego odcisku palca lub twarzy). Włącz ją w ustawieniach **Security** (Bezpieczeństwo) swojej giełdy i wybierz aplikację uwierzytelniającą lub passkey zamiast SMS-a.

> **Najważniejsze**
> - Z 2FA samo skradzione hasło nie wystarczy, żeby opróżnić Twoje konto.
> - **Kody SMS to najsłabsza opcja:** przy „SIM swap” (podmianie karty SIM) przestępca przenosi Twój numer telefonu na swoją kartę SIM i odbiera Twoje kody. FBI odnotowało 1611 takich zgłoszeń i ponad **68 mln dolarów** strat w 2021 r., wobec 320 zgłoszeń i ok. 12 mln dolarów w latach 2018–2020.
> - FBI zaleca mocniejsze opcje: aplikację uwierzytelniającą, biometrię albo fizyczny klucz bezpieczeństwa.

## Opcje od najsłabszej do najmocniejszej

- **Kod SMS** — wiadomość z kodem. Lepsze niż nic, ale Twój numer telefonu można ukraść.
- **Kod e-mailem** — jest tak bezpieczny jak Twoja skrzynka (ją też zabezpiecz 2FA).
- **Aplikacja uwierzytelniająca** (Google Authenticator, Microsoft Authenticator i podobne) — aplikacja co 30 sekund tworzy nowy 6-cyfrowy kod, nawet offline. Nikt nie przechwyci go przez Twojego operatora komórkowego.
- **Passkey** (biometria) — potwierdzasz odciskiem palca, twarzą albo PIN-em telefonu. Działa tylko na prawdziwej stronie, więc fałszywa strona nie może go ukraść.
- **Fizyczny klucz bezpieczeństwa** (małe urządzenie USB/NFC) — najmocniejsza opcja, dobra przy dużych kwotach.

## Krok po kroku: aplikacja uwierzytelniająca (na przykładzie aplikacji Binance)

Inne giełdy mają prawie te same kroki; szukaj **Security** (Bezpieczeństwo) w swoim profilu.

1. **Krok 1 — Zainstaluj aplikację.** Pobierz Google Authenticator (albo inną aplikację uwierzytelniającą) z oficjalnego App Store lub Google Play.
2. **Krok 2 — Otwórz ustawienia bezpieczeństwa.** W aplikacji Binance dotknij ikony **Account**, dotknij swojego profilu na górze, a potem **Security**.
3. **Krok 3 — Rozpocznij konfigurację.** Dotknij **Authenticator App**, a potem **Enable**. Zobaczysz kod QR i **setup key** (klucz konfiguracji — długi kod).
4. **Krok 4 — Zapisz klucz konfiguracji na papierze.** To Twoje koło ratunkowe, jeśli zgubisz telefon. Trzymaj go offline, tak jak seed phrase. Nie dotykaj jeszcze **Next**.
5. **Krok 5 — Dodaj konto w aplikacji uwierzytelniającej.** W Google Authenticator dotknij **+**, wybierz **Enter a setup key** (Wpisz klucz konfiguracji) albo zeskanuj kod QR, wklej klucz, wpisz nazwę, np. „Binance”, i dotknij **Add**.
6. **Krok 6 — Potwierdź.** Wróć do Binance, dotknij **Next** i wpisz 6-cyfrowy kod z aplikacji. Zobaczysz komunikat o powodzeniu.
7. **Krok 7 — Przetestuj.** Wyloguj się i zaloguj ponownie. Jeśli pojawi się prośba o kod, wszystko działa.

## Krok po kroku: passkey (jeszcze prościej)

Według strony pomocy Binance potrzebujesz aplikacji w wersji 2.60 lub nowszej, iOS 16+ albo Androida 9+.

1. **Account → profil → Security → Passkeys (Biometrics) → Add Passkey.**
2. Jeśli trzeba, potwierdź obecną 2FA i dotknij **Continue**.
3. Wybierz, gdzie go zapisać: pęk kluczy iCloud (iPhone), Menedżer haseł Google (Android) albo klucz bezpieczeństwa, i potwierdź odciskiem palca, twarzą lub PIN-em.

## Po włączeniu 2FA

- Wyłącz SMS jako metodę logowania, jeśli giełda na to pozwala, albo przynajmniej poproś operatora o blokadę karty SIM / PIN chroniący przed przeniesieniem numeru.
- Zabezpiecz 2FA także e-mail powiązany z giełdą.
- Włącz **białą listę adresów do wypłat** (tylko zapisane adresy mogą otrzymać środki), jeśli Twoja giełda ją oferuje.

> **⚠️ Uwaga**
> - **Nikt prawdziwy nie prosi o Twój kod 2FA.** „Wsparcie” na Telegramie, telefon „z giełdy” albo „z banku” z prośbą o 6-cyfrowy kod to zawsze oszust.
> - **Utrata telefonu bez klucza zapasowego.** Odzyskanie konta zajmuje wtedy dni weryfikacji tożsamości. Zapisz klucz konfiguracji na papierze i schowaj go w bezpiecznym miejscu.
> - **Fałszywe aplikacje uwierzytelniające i podrobione strony logowania.** Instaluj aplikacje tylko z oficjalnego sklepu, a adres giełdy wpisuj sam albo korzystaj z zakładki.

## Co to oznacza, jeśli kupujesz regularnie

Jeśli co miesiąc kupujesz trochę, Twoje konto na giełdzie powoli zamienia się w prawdziwą kwotę — np. bitcoin kosztuje teraz {{price:btc}} ({{chg1y:btc}} w ciągu 12 miesięcy); to wyniki z przeszłości, nie prognoza. Dziesięć minut konfiguracji 2FA chroni lata zakupów. Śledź to, co masz, na swojej [stronie portfela]({lang}/me/).

Poprzednia lekcja: [seed phrase: 5 zasad, jak ją chronić]({lang}/blog/seed-phrase-safety-rules/). Więcej: [jak zarejestrować się na giełdzie kryptowalut]({lang}/blog/how-to-register-on-a-crypto-exchange/), [giełdy działające w Twoim kraju]({lang}/exchanges/). Wszystkie lekcje są na [stronie Nauka]({lang}/learn/).

## Źródła

- [FBI IC3: Criminals increasing SIM swap schemes to steal millions (8 lutego 2022)](https://www.ic3.gov/PSA/2022/PSA220208)
- [Binance Support: How to enable Google Authenticator for 2FA on the Binance app (aktualizacja 10 grudnia 2025)](https://www.binance.com/en/support/faq/f3b1adaed1c846bbbba0f3650ad23e45)
- [Binance Support: How to create a passkey for my Binance account (aktualizacja 10 grudnia 2025)](https://www.binance.com/en/support/faq/2aec8fe0437242f2a5fbef9cdb71d4c2)

*To nie jest porada inwestycyjna.*

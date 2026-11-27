---
title: "Two-factor authentication (2FA): how to turn it on, step by step"
description: 2FA adds a second lock to your exchange account. How to turn on an authenticator app or passkey step by step, and why SMS codes are the weakest option.
date: 2026-11-27T12:30:00Z
category: learn
track: safety
step: 10
assets: btc, eth
stat: $68M
stat_label: lost to SIM-swap fraud in 2021 in 1,611 complaints to the FBI (IC3, February 2022)
---
**What is 2FA and how do you turn it on?** Two-factor authentication (2FA) means that logging in or withdrawing needs two things: your password *and* a second proof, such as a 6-digit code from an app on your phone or a passkey (your fingerprint or face). Turn it on in your exchange's **Security** settings and use an authenticator app or passkey rather than SMS.

> **Key takeaways**
> - With 2FA, a stolen password alone is not enough to empty your account.
> - **SMS codes are the weakest option:** in a "SIM swap" a criminal moves your phone number to their SIM card and receives your codes. The FBI recorded 1,611 such complaints and over **$68 million** in losses in 2021, up from 320 complaints and about $12 million in 2018–2020.
> - The FBI recommends stronger options: an authenticator app, biometrics or a physical security key.

## The options, from weakest to strongest

- **SMS code** — a text message with a code. Better than nothing, but your phone number can be stolen.
- **E-mail code** — only as safe as your e-mail account (protect it with 2FA too).
- **Authenticator app** (Google Authenticator, Microsoft Authenticator and similar) — the phone app makes a new 6-digit code every 30 seconds, even offline. Nobody can intercept it through your phone company.
- **Passkey** (biometrics) — you confirm with your fingerprint, face or phone PIN. It works only on the real site, so a fake site cannot steal it.
- **Physical security key** (a small USB/NFC device) — the strongest, good for large amounts.

## Step-by-step: authenticator app (Binance app as the example)

Other exchanges use almost the same steps; look for **Security** in your profile.

1. **Step 1 — Install the app.** Download Google Authenticator (or another authenticator app) from the official App Store or Google Play.
2. **Step 2 — Open security settings.** In the Binance app tap the **Account** icon, tap your profile at the top, then **Security**.
3. **Step 3 — Start setup.** Tap **Authenticator App**, then **Enable**. You will see a QR code and a **setup key** (a long code).
4. **Step 4 — Save the setup key on paper.** This is your backup if you lose your phone. Keep it offline, like a seed phrase. Do not tap **Next** yet.
5. **Step 5 — Add the account in the authenticator.** In Google Authenticator tap **+**, choose **Enter a setup key** (or scan the QR code), paste the key, type a name such as "Binance", tap **Add**.
6. **Step 6 — Confirm.** Back in Binance tap **Next** and type the 6-digit code from the app. You will see a success message.
7. **Step 7 — Test it.** Log out and log in again. If you are asked for the code, it works.

## Step-by-step: passkey (even simpler)

Binance's help page says you need app version 2.60+, iOS 16+ or Android 9+.

1. **Account → profile → Security → Passkeys (Biometrics) → Add Passkey.**
2. Confirm with your current 2FA if asked, tap **Continue**.
3. Choose where to save it: iCloud Keychain (iPhone), Google Password Manager (Android) or a security key, and confirm with your fingerprint, face or PIN.

## After 2FA is on

- Turn off SMS as a login method if the exchange allows it, or at least ask your phone company for a SIM lock / port-out PIN.
- Protect the e-mail linked to the exchange with 2FA as well.
- Turn on a **withdrawal whitelist** (only saved addresses can receive) if your exchange has one.

> **⚠️ Watch out**
> - **Nobody real asks for your 2FA code.** "Support" on Telegram, a caller from "the exchange" or a "bank" asking for the 6-digit code is always a scammer.
> - **Losing the phone without the backup key.** Recovery then takes days of ID checks. Write the setup key on paper and keep it safe.
> - **Fake authenticator apps and look-alike login pages.** Install apps only from the official store and type the exchange address yourself, or use a bookmark.

## What it means if you buy regularly

If you buy a little every month, your exchange account slowly becomes a real sum — for example bitcoin is at {{price:btc}} right now ({{chg1y:btc}} over 12 months), past results, not a forecast. Ten minutes of 2FA setup protects years of buys. Track what you hold on your [portfolio page]({lang}/me/).

Previous lesson: [seed phrase: 5 rules to keep it safe]({lang}/blog/seed-phrase-safety-rules/). More: [how to register on a crypto exchange]({lang}/blog/how-to-register-on-a-crypto-exchange/), [exchanges that work in your country]({lang}/exchanges/). All lessons are on the [Learn page]({lang}/learn/).

## Sources

- [FBI IC3: Criminals increasing SIM swap schemes to steal millions (February 8, 2022)](https://www.ic3.gov/PSA/2022/PSA220208)
- [Binance Support: How to enable Google Authenticator for 2FA on the Binance app (updated December 10, 2025)](https://www.binance.com/en/support/faq/f3b1adaed1c846bbbba0f3650ad23e45)
- [Binance Support: How to create a passkey for my Binance account (updated December 10, 2025)](https://www.binance.com/en/support/faq/2aec8fe0437242f2a5fbef9cdb71d4c2)

*Not investment advice.*

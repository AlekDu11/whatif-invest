---
title: How to connect Binance Wallet to a DEX and move coins back: step by step
description: Connect Binance Wallet to a DEX site safely, send coins back to your Binance account on the right network and remove old approvals — in plain steps.
date: 2026-11-23T14:30:00Z
category: learn
track: memes
step: 6
assets: bnb, sol, cake
stat: 1
stat_label: small test transfer before every new address or network
---
**How do you connect Binance Wallet to a DEX?** Open the DEX's official website, press **Connect Wallet**, choose Binance Wallet (or WalletConnect and scan the QR code with the Binance app) and confirm in the app. To move coins back, copy your Binance **deposit address** for the same coin and network, then send to it from the wallet — a small test amount first.

> **Key takeaways**
> - A DEX (decentralised exchange — a website where you swap tokens straight from your own wallet) never needs your recovery password or seed phrase. Connecting only lets the site *ask* you to sign; nothing moves until you confirm.
> - The network must match on both sides (BNB Smart Chain to BNB Smart Chain, Solana to Solana). A wrong network or address can mean the coins are lost.
> - Every "Approve" lets a site spend a token for you. Give small approvals and remove the ones you no longer use.

This lesson continues [How to create a Binance Wallet]({lang}/blog/how-to-create-binance-wallet/). Memecoins are extremely risky — only use money you can afford to lose.

## Step 1 — Open the real website

Fake DEX sites with the same logo are one of the most common traps.

1. Type the address yourself or use a bookmark. Do not click ads in search results or links in chats.
2. Check the address bar letter by letter.
3. Check that the DEX works on the network your coins are on.

## Step 2 — Connect the wallet

There are three ways, depending on your device:

- **On a computer with the Binance Wallet browser extension** (Chrome or Brave). Log in to the extension by scanning its QR code with the Binance app. Then on the DEX press **Connect** or **Connect Wallet**, pick Binance Wallet and confirm the pop-up.
- **On a computer without the extension.** On the DEX press **Connect Wallet → WalletConnect**. A QR code appears. Scan it with the scanner in the Binance app and tap **Connect**.
- **On your phone.** Open the DEX in the phone browser, press **Connect Wallet**, choose Binance Wallet from the list and confirm in the app.

Before you confirm, read the pop-up: the site name, the address and the network. If any of these look wrong, press Cancel.

## Step 3 — Swap and read every signature

1. Choose the coin you pay with and the token you want (find the token by its **contract address**, not by its name).
2. Enter a small amount and check the rate, the slippage (the biggest price change you accept) and the network fee.
3. The first time you sell a token, the site asks for **Approve** (permission to spend that token). If the app lets you, set the amount instead of "unlimited".
4. Confirm the swap in the app. If a signature request is a page of unreadable code or makes no sense — **do not sign it**.

## Step 4 — Send coins back to your Binance account

1. In the Binance app, switch to **Exchange** → **Assets** → **Deposit**. Choose the coin (for example BNB).
2. Choose the **network** (for example BNB Smart Chain). Copy the deposit address. Some coins also need a **memo/tag** — copy it too.
3. Switch to **Wallet** → **Send**. Choose the same coin and the same network. Paste the address (and the memo if there is one).
4. Send a small test amount first. When it arrives in your Binance account, send the rest.

Keep a little BNB or SOL in the wallet: every on-chain action, even a failed one, costs a network fee. Some memecoins cannot be deposited to the exchange at all (the exchange does not list them) — to cash out, swap them back to BNB, SOL or USDT in the wallet first.

## Step 5 — Disconnect and clean up

1. When you finish, disconnect the site (in the wallet's connected-sites or WalletConnect settings, or the **Disconnect** button on the DEX).
2. From time to time check your token approvals and revoke (cancel) the ones you do not need. A revoke costs a small fee.
3. On a shared computer, log out of the extension.

You can follow the tokens you bought in [your portfolio]({lang}/me/) and see live memecoin data on our [memecoins page]({lang}/memes/).

> **⚠️ Watch out**
> - **A site or "support" asks for your recovery password, seed phrase or a "wallet sync".** No real DEX or Binance employee ever does. Close the page.
> - **Unlimited approvals and blind signing.** A malicious approval or signature can let a scammer empty that token later, without another confirmation from you.
> - **Wrong network, missing memo or a pasted address that changed.** Malware can swap a copied address. Compare the first and last characters every time, and test with a small amount.

Next lesson: how to check a memecoin before buying. All lessons are on the [Learn page]({lang}/learn/).

## Sources

- [Binance: What Is Binance Wallet Extension and How Does It Work?](https://www.binance.com/en/support/faq/ebfa9f504ec548968bf0c1ed591a3eaa)
- [Binance Academy: How to Use WalletConnect](https://www.binance.com/en/academy/articles/how-to-use-walletconnect)
- [Binance: How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance.US: How to stay safe when using dApps on your Web3 Wallet](https://support.binance.us/en/articles/15090007-how-to-stay-safe-when-using-dapps-on-your-binance-us-wallet)

*Not investment advice. This guide explains how the tools work and does not recommend buying any token. Binance Wallet may not be available in every country.*

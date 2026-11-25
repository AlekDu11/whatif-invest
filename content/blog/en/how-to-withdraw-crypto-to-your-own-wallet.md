---
title: How to withdraw crypto from an exchange to your own wallet: step by step
description: Move coins from an exchange to your own wallet safely: copy the right address, pick the same network, add a memo if needed and send a small test first.
date: 2026-11-25T09:40:00Z
category: learn
track: crypto
step: 6
assets: btc, eth, sol, bnb
stat: 1 network
stat_label: the exchange and the wallet must use the same one, or the coins can be lost
---
**How do you withdraw crypto to your own wallet?** In your wallet you copy your **receive address** for the coin, then on the exchange you open **Withdraw**, paste that address, choose **the same network** your wallet uses, enter a small test amount and confirm with 2FA. When the test arrives, you send the rest.

> **Key takeaways**
> - Three things must match: the **coin**, the **address** and the **network** (the blockchain the coins travel on, for example Ethereum, BNB Smart Chain, TRON or Solana). Binance warns that coins sent on the wrong network may be lost for good.
> - Some coins (such as XRP, XLM or ATOM) also need a **memo** or **tag** (a short number that tells the receiver whose coins they are). Without it the transfer can get stuck or go to the wrong person.
> - **Always send a small test first.** A withdrawal cannot be cancelled once the coins have left the exchange.

This lesson continues [How to set up a recurring buy]({lang}/blog/how-to-set-up-a-recurring-buy/). Why you might want your own wallet at all is explained in [hot vs cold wallets]({lang}/blog/crypto-wallets-hot-vs-cold/).

## Before you start

You need two things: an exchange account with coins on it (protected with 2FA — see [How to register on a crypto exchange]({lang}/blog/how-to-register-on-a-crypto-exchange/)) and your own wallet app that is already set up, with its **seed phrase** (the 12 or 24 secret words that restore the wallet) written on paper and kept offline. Never type the seed phrase anywhere else — no exchange, website or "support" person will ever need it.

## Step 1 — Copy your wallet's receive address

1. Open your wallet app and tap **Receive** (sometimes **Deposit**).
2. Choose the coin, for example Bitcoin or USDT.
3. If the wallet asks, choose the network. Write down which one it is — for example "USDT on TRON (TRC20)" or "USDT on Ethereum (ERC20)".
4. Tap **Copy** next to the address. Do not type it by hand.

An address is a long line of letters and numbers. Bitcoin addresses often start with **bc1**, Ethereum and BNB Smart Chain addresses with **0x**, TRON addresses with **T**.

## Step 2 — Open Withdraw on the exchange

On Binance in the app this is **Assets → Spot → Send → Withdraw Crypto**; on the website it is **Wallet → Overview → Withdraw**. Other exchanges have a **Withdraw** button next to each coin in the wallet or portfolio screen. Pick the same coin you chose in Step 1.

## Step 3 — Paste the address and pick the network

1. Paste the address into the **Address** field.
2. Compare the **first 4 and last 4 characters** with your wallet. Some malware swaps a copied address for the thief's one.
3. Choose the **network**. It must be the one your wallet showed in Step 1. Binance may suggest a network automatically — still check it. Do not pick a network only because its fee is the lowest.
4. If a **Memo** or **Tag** field appears and your wallet gave you one, fill it in. If your own wallet shows no memo, it usually does not need one — but double-check in the wallet's help pages.

Tip: if you are not sure, save the address in the exchange's **Address Management** (address book). Binance also has a **whitelist**: once you turn it on, withdrawals can only go to saved addresses, which helps if someone steals your password.

## Step 4 — Send a small test

1. Enter a small amount — just above the minimum withdrawal the screen shows.
2. Look at the **network fee** and **you will receive** lines. The fee is fixed per withdrawal, so on a tiny amount it can be a large share.
3. Press **Withdraw** and confirm with your 2FA code or passkey. Some exchanges also send a confirmation e-mail — open it and press **Confirm**.

## Step 5 — Check that it arrived, then send the rest

1. Wait. A transfer can take from a few seconds to about an hour, depending on the network and traffic.
2. On the exchange, open the withdrawal history to see the status and the **TxID** (the transaction's ID, which you can look up on a block explorer site).
3. When the coins appear in your wallet, repeat Steps 2–4 with the rest. The address is already in the history or address book, so it is quicker the second time.

Add the coins to [your portfolio]({lang}/me/) so you can follow their value in one place, wherever they are kept.

> **⚠️ Watch out**
> - **Wrong network.** USDT exists on many networks. Sending "TRC20" USDT to an address that only expects "ERC20" can mean the coins are lost. Check the network twice.
> - **Missing memo or tag.** Exchanges and wallets that need a memo cannot tell whose coins arrived without it. Recovery, if possible at all, is slow and costs a fee.
> - **Fake support and "address verification" sites.** Nobody legitimate asks for your seed phrase or asks you to "verify" a wallet by sending coins. Withdraw only inside the official app or website.

## What it means if you buy regularly

If you buy a little every week or month, you do not need to withdraw after every buy — each withdrawal has a fee. Many people let the coins collect on the exchange and move them to their own wallet now and then, for example once a quarter, in one larger transfer. Example from our calculator: $10 a day in Bitcoin for 3 years ({{dcainv:3}} in total) became {{dca:btc:3}} ({{dcaroi:btc:3}}). Past results, not a forecast. Bitcoin is at {{price:btc}} right now; see the [Bitcoin page]({lang}/btc/).

Previous lesson: [How to set up a recurring buy]({lang}/blog/how-to-set-up-a-recurring-buy/). Next lesson: how to sell crypto and get money to your bank account. Compare exchanges on our [exchanges page]({lang}/exchanges/); all lessons are on the [Learn page]({lang}/learn/).

## Sources

- [Binance Support: How to deposit/withdraw cryptocurrency on Binance (updated March 2026)](https://www.binance.com/en/support/faq/85a1c394ac1d489fb0bfac0ef2fceafd)
- [Binance Support: How to retrieve a crypto deposit with a wrong or missing tag/memo](https://www.binance.com/en/support/faq/40b87335db904481888ef406b105442b)
- [Binance.US Help Center: How to withdraw crypto from your Binance.US account (June 2026)](https://support.binance.us/en/articles/9842854-how-to-withdraw-crypto-from-your-binance-us-account)

*Not investment advice.*

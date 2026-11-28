---
title: "Order types: market, limit and stop orders explained step by step"
description: What the Market, Limit and Stop buttons do on an exchange or broker app, with a worked example and the 3 mistakes that cost beginners money.
date: 2026-11-28T09:05:00Z
category: learn
track: trading
step: 2
assets: btc, aapl
stat: 3
stat_label: basic order types — market (fast, price not fixed), limit (price fixed, fill not sure), stop (triggers at a price)
---
**What order types are there?** A **market order** buys or sells right now at the best price available. A **limit order** buys or sells only at your price or better, so it may never fill. A **stop order** waits until the price reaches a level you choose, then sends a market order — often used to limit a loss.

> **Key takeaways**
> - Market = speed, but you do not control the exact price. Limit = control of the price, but no guarantee it fills.
> - A stop order becomes a market order when it triggers. In a fast fall it can fill far below your stop price.
> - Before pressing "Buy", always check three things: order type, amount and price.

## The three buttons, in plain words

When you open the trade screen on an exchange or broker app, you usually see tabs: **Market**, **Limit** and **Stop** (sometimes "Stop-limit").

- **Market order.** "Buy now, whatever the price." It fills almost instantly at the best offer (the **ask**, the lowest price a seller wants). For big coins and big stocks the price is usually very close to what you see. For small, thin markets it can be much worse.
- **Limit order.** "Buy only at $X or cheaper" (or "sell only at $X or higher"). Your order waits in the **order book** (the list of all waiting buy and sell orders) until someone accepts your price. If the price never gets there, nothing happens.
- **Stop order (stop-loss).** "If the price falls to $X, sell." Until then it is invisible and does nothing. When the price touches $X, it turns into a market order and sells at the next available price.
- **Stop-limit order.** Like a stop, but it turns into a *limit* order instead. You will not sell below your limit — but in a fast fall it may not sell at all.

## A worked example with simple numbers

Say a share shows **$100.00**. The best buyer offers $99.95 (the **bid**) and the best seller asks $100.05 (the ask). The gap of $0.10 is the **spread**.

1. You press **Market buy, 10 shares** → you pay about $100.05 each = **$1,000.50** plus any fee.
2. You place **Limit buy, 10 shares at $98** → nothing happens until a seller accepts $98. If the price goes to $105 instead, your order just waits and you buy nothing.
3. You own the shares and set a **Stop at $90** → if the price drops to $90, a market sell is sent. In a calm market you might get $89.95. If bad news hits before the market opens and the share opens at $80, your stop triggers and you sell near **$80**, not $90.

That third case is real. On 6 May 2010 (the "flash crash"), US prices collapsed within minutes and some stop orders filled far below their stop levels, a few shares even trading for a penny, according to the SEC and CFTC report.

## Step-by-step: place your first limit order safely

Practise with a very small amount first.

1. **Step 1 — Open the trade screen** of the coin or stock and choose **Buy**.
2. **Step 2 — Press the "Limit" tab**, not "Market".
3. **Step 3 — Type your price.** Look at the current price first (for example Bitcoin is {{price:btc}} right now). A limit far below it may never fill.
4. **Step 4 — Type the amount.** Check whether the box means coins/shares or money (USD, EUR). This is the most common typo.
5. **Step 5 — Check the summary**: type, price, amount, total, fee. Then confirm.
6. **Step 6 — Find your order** under "Open orders". You can cancel it there at any time until it fills. When it fills, it moves to "Order history".

> **⚠️ Watch out**
> - **Market orders in thin markets.** On small coins or outside normal trading hours, a market order can fill much worse than the price on the screen (this is called **slippage**). Use a limit order there.
> - **Thinking a stop-loss guarantees your price.** It does not: it guarantees a sale, not the price. Gaps and crashes can push the fill far lower. A stop-limit protects the price but may not sell.
> - **Mixing up the fields.** Wrong side (Sell instead of Buy), an extra zero in the amount, or a price typed in the wrong box. Read the summary before you confirm.

## What it means if you buy regularly

If you simply buy a little every week or month, you do not need complex orders. A market order on a big, liquid asset is usually fine, or a limit order slightly above the current price if you want a cap. The real result comes from time in the market: $10 a day into Bitcoin over 3 years would now be worth {{dca:btc:3}} (you put in {{dcainv:3}}) — past results, not a forecast.

Next on WhatIfStack: see how order books and big traders move the market on the [trading hub]({lang}/trading/) and the [Hyperliquid whale tracker]({lang}/trading/hyperliquid/), compare fees on [exchanges]({lang}/exchanges/), and find all lessons on the [Learn page]({lang}/learn/).

## Sources

- [Investor.gov (SEC): Types of orders](https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders)
- [Investor.gov (SEC): Investor bulletin — Stop, stop-limit and trailing stop orders](https://www.investor.gov/additional-resources/news-alerts/alerts-bulletins/investor-bulletin-stop-stop-limit-trailing-stop)
- [FINRA: Order types](https://www.finra.org/investors/investing/investment-products/stocks/order-types)
- [CFTC and SEC: Staff report on the market events of May 6, 2010](https://www.cftc.gov/MarketReports/StaffReportonMay6MarketEvents/staffreport050610marketevents.html)

*Not investment advice.*

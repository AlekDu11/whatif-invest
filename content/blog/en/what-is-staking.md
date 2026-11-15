---
title: What is crypto staking and is it safe?
description: Crypto staking in plain words: how it works, lock-up periods, exchange vs on-chain staking, and the real risks to check before you stake any coins.
date: 2026-11-16
category: guides
assets: eth, sol, ada, dot, atom
---
**Staking** means locking up crypto coins to help a blockchain run — and receiving new coins as a reward for it. It is often compared to a savings account, but it works very differently and carries its own risks.

This guide explains how staking works, what "lock-up" means, how staking on an exchange differs from staking on-chain, and what can go wrong.

## How staking works

Many modern blockchains — Ethereum, Solana, Cardano, Polkadot, Cosmos and others — use a system called **proof of stake**. Instead of using electricity to secure the network (like Bitcoin's mining), they rely on **validators**: computers that check transactions and add new blocks.

To become a validator, you must put coins at stake as a guarantee of honest behaviour. In simple steps:

1. You lock (stake) coins in the network, either running a validator yourself or delegating to one.
2. Validators confirm transactions and produce blocks.
3. The network pays rewards in new coins, plus a share of transaction fees.
4. If a validator cheats or goes offline badly, part of the stake can be cut. This is called **slashing**.

Bitcoin itself cannot be staked in this way — it uses proof of work. Products that offer "Bitcoin yield" are usually lending or other schemes, not staking.

## Where staking rewards come from

Rewards are not free money. They mostly come from:

- **New coins** created by the network (inflation of the coin supply),
- **Transaction fees** paid by users.

This matters: if a network creates new coins at, say, 5% a year and you earn 5%, you are mostly keeping your share of the network rather than getting richer. And rewards are paid in the coin itself — if its price falls, your total value can still go down sharply.

Reward rates change all the time with the number of stakers and network rules. Treat any advertised percentage as a snapshot, not a promise.

## Lock-ups and unbonding: when you can get your coins back

Staking usually means your coins are not instantly available. Each network has its own rules:

- **Ethereum** — withdrawals have been possible since the 2023 "Shapella" upgrade, but exiting goes through a queue that can take from days to weeks when many people leave at once.
- **Solana** — unstaking takes effect at the end of an "epoch", usually a couple of days.
- **Cosmos and Polkadot** — "unbonding" periods of several weeks, during which coins earn nothing and cannot be sold.
- **Cardano** — coins stay in your wallet and are not locked at all.

Why it matters: if the market drops during the unbonding period, you cannot sell. Always check the exact current rules for the coin before staking.

## Exchange staking vs on-chain staking

There are two main ways ordinary people stake.

### Staking on an exchange (custodial)

You press "Stake" or "Earn" in an exchange app and it does the technical work.

- ✅ Very easy, small amounts are fine, no wallet setup.
- ❌ The exchange holds your coins. If it fails, is hacked or freezes withdrawals, your coins are at risk.
- ❌ The exchange keeps part of the rewards as a fee.
- ❌ Some "earn" products are actually lending, not staking — a very different risk.

Regulators have looked closely at these services. In 2023 the US SEC charged Kraken over its staking program; Kraken paid $30 million and shut the service for US customers. In 2025 SEC staff said that some forms of direct "protocol staking" are not securities transactions. Rules differ by country and keep changing.

### Staking on-chain (non-custodial)

You keep coins in your own wallet and delegate them to a validator, or run a validator yourself.

- ✅ You hold your keys; nobody can freeze your account.
- ✅ Usually lower fees.
- ❌ More technical: wrong addresses, phishing and bad validators are your problem.
- ❌ Running your own Ethereum validator needs 32 ETH and reliable hardware.

### Liquid staking

A middle option: you stake through a protocol and receive a token that represents your staked coins (for example, a "staked ETH" token). You can trade it while your coins earn rewards. The trade-off is extra **smart-contract risk** and the chance that the token trades below the value of the coins behind it.

## The main risks of staking

Is staking safe? It is less risky than many "high yield" crypto products, but it is never risk-free:

1. **Price risk.** The biggest one. A reward of a few percent means little if the coin falls 50%. See how volatile coins are on the [Ethereum page]({lang}/eth/) or [Solana page]({lang}/sol/).
2. **Lock-up risk.** You may not be able to sell during a crash.
3. **Platform risk.** Exchanges and lending platforms can fail. When Celsius collapsed in 2022, users of its "earn" program lost access to their coins.
4. **Slashing.** A misbehaving validator can lose part of the stake — including delegated coins on some networks.
5. **Smart-contract risk** in liquid staking and DeFi.
6. **Taxes.** In many countries staking rewards are taxable income when received. Check local rules.
7. **Scams.** Fake staking sites and "guaranteed 20% a month" offers are common. Read our guide on [avoiding crypto scams]({lang}/blog/how-to-avoid-crypto-scams/).

## A careful checklist before staking

- Only stake coins you already planned to hold for a long time.
- Check the unbonding period and whether you might need the money sooner.
- Understand who holds your coins — you or a platform.
- Compare fees: what share of the rewards does the platform keep?
- Avoid offers with very high fixed returns — real staking rewards float.
- Start small and test a withdrawal.

Staking does not change the main question: does the coin itself fit your long-term plan? A regular buying plan, like [DCA]({lang}/blog/what-is-dca/), is about the asset's price over years. Here is how $10 a day in Ethereum would have done over 5 years — without any staking rewards: {{dca:eth:5}} from {{dcainv:5}} invested ({{dcaroi:eth:5}}).

{{card:eth}}
{{card:sol}}

## FAQ

### Is staking the same as earning interest?

No. Interest comes from a borrower; staking rewards come from the network itself for helping secure it. Rewards are paid in the coin, so their value moves with its price.

### Can I lose money staking?

Yes. The coin's price can fall, a platform can fail, and in rare cases slashing can cut your stake. Rewards do not protect you from a price drop.

### Can I stake Bitcoin?

Not natively — Bitcoin uses proof of work. "Bitcoin yield" offers are usually lending or other products with different risks.

### Is exchange staking or wallet staking better?

Exchange staking is simpler; wallet staking gives you control of your keys. The right choice depends on how comfortable you are managing a wallet — see our guide to [hot and cold wallets]({lang}/blog/crypto-wallets-hot-vs-cold/).

## Sources

- [ethereum.org — Ethereum staking](https://ethereum.org/en/staking/)
- [ethereum.org — Staking withdrawals](https://ethereum.org/en/staking/withdrawals/)
- [Solana — Staking](https://solana.com/staking)
- [US SEC — Kraken to discontinue staking program, pay $30 million (2023)](https://www.sec.gov/news/press-release/2023-25)
- [Skadden — SEC: certain protocol staking activities are not securities transactions (2025)](https://www.skadden.com/insights/publications/2025/06/sec-certain-protocol-staking-activities-are-not-securities-transactions)

*Not investment advice. This guide explains how staking works and does not recommend any coin, platform or validator.*

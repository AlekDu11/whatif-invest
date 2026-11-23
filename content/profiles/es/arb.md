---
title: Arbitrum (ARB) explicado fácil: capa 2 de Ethereum, optimistic rollup y un límite de 10.000 millones de ARB
description: Arbitrum en lenguaje sencillo: cómo funciona esta capa 2 de Ethereum, para qué sirve ARB en la DAO, los desbloqueos, su historia y los riesgos.
date: 2026-11-23
kind: analysis
---
**Arbitrum** es una red construida sobre Ethereum que hace las transacciones más rápidas y mucho más baratas, pero sigue apoyándose en Ethereum para su seguridad: es lo que se llama una «capa 2». La creó la empresa estadounidense Offchain Labs, y su token **ARB** permite a sus poseedores votar cómo se gestionan la red y su tesorería. Hoy ARB vale {{mcap:arb}} ({{rank:arb}} entre las criptomonedas).

> **Claves**
> - Nunca habrá más de 10.000 millones de ARB; en el lanzamiento, en marzo de 2023, cerca del 42% fue a la tesorería de la DAO, alrededor del 27% al equipo y el 17,5% a los inversores.
> - Su máximo histórico es {{ath:arb}} ({{athd:arb}}); hoy el precio está {{fromath:arb}} desde él.
> - ARB es un token de gobernanza: las comisiones en Arbitrum se pagan en ETH, no en ARB.
> - Los tokens del equipo y de los inversores se desbloquean cada mes desde marzo de 2024, lo que añade nueva oferta al mercado.

## Cómo funciona

Arbitrum es un **optimistic rollup**. En lugar de que cada nodo de Ethereum procese cada transacción, Arbitrum las ejecuta en su propia cadena y publica en Ethereum lotes comprimidos de datos. Un único operador, el **secuenciador** (gestionado por Offchain Labs), ordena las transacciones y las confirma en una fracción de segundo. Los resultados se dan por buenos («de forma optimista») salvo que alguien los impugne: cualquier validador puede presentar una **prueba de fraude** y la disputa se resuelve en Ethereum. Desde febrero de 2025 el protocolo **BoLD** permite que cualquiera participe en la validación, y basta un validador honesto para defender la red. Su software, **Nitro**, es compatible con las aplicaciones de Ethereum, y el programa **Orbit** permite a otros proyectos lanzar sus propias cadenas con tecnología de Arbitrum.

## Para qué sirve el token

ARB es sobre todo un token de voto. Los poseedores, o los delegados que eligen, votan en la **DAO de Arbitrum** sobre las mejoras de la red y sobre cómo gastar la tesorería, que guarda miles de millones de ARB además de los ingresos por comisiones del secuenciador. No hace falta ARB para usar Arbitrum: el gas se paga en ETH. Por eso el valor del token depende de los derechos de voto y de lo que la DAO decida hacer con su dinero, no directamente del uso de la red.

## Las cifras actuales

- Precio hoy: {{price:arb}}
- Máximo histórico: {{ath:arb}} ({{athd:arb}}), {{fromath:arb}} desde él
- Valor de mercado: {{mcap:arb}} ({{rank:arb}} entre las criptomonedas)
- Variación del precio en 12 meses: {{chg1y:arb}}
- 10 $ al día durante 3 años: {{dca:arb:3}} con {{dcainv:3}} invertidos ({{dcaroi:arb:3}})

## Su historia

Offchain Labs nació de una investigación en la Universidad de Princeton. Arbitrum One se abrió al público a finales de agosto de 2021, y la actualización Nitro de agosto de 2022 redujo las comisiones y aumentó la capacidad. El 23 de marzo de 2023 se lanzó el token ARB con un gran airdrop para los usuarios. Pocos días después, la primera propuesta, AIP-1, provocó un escándalo porque la Fundación ya había empezado a usar una asignación de 750 millones de ARB antes de la votación; después dividió la propuesta y dio más control a la DAO. ARB alcanzó su pico, unos 2,39 $, en enero de 2024. El 16 de marzo de 2024 se desbloquearon unos 1.100 millones de tokens del equipo y de los inversores, y después llegaron desbloqueos mensuales. En 2025 se activó BoLD, y el precio cayó con fuerza a lo largo de 2025 y 2026.

## Alternativas

Arbitrum compite con otras redes de capa 2 de Ethereum: [Optimism]({lang}/op/) y las cadenas basadas en su OP Stack, como Base de Coinbase, que no tiene token propio; los rollups de conocimiento cero como [ZKsync]({lang}/zk/) y [Starknet]({lang}/strk/); y [Mantle]({lang}/mnt/) y [POL (ex-MATIC)]({lang}/pol/). El propio [Ethereum]({lang}/eth/) también es una alternativa, porque sus mejoras lo hacen cada vez más barato de usar.

## Principales riesgos

- **Nueva oferta:** siguen los desbloqueos para el equipo y los inversores, y la tesorería de la DAO tiene una gran parte de todos los ARB.
- **Secuenciador centralizado:** un solo operador ordena las transacciones; si falla o actúa mal, los usuarios dependen de vías alternativas más lentas.
- **Competencia:** Base y otras redes de capa 2 se disputan los mismos usuarios, aplicaciones y comisiones.
- **Poca relación con el uso:** las comisiones se pagan en ETH, así que un uso intenso de Arbitrum no aumenta automáticamente la demanda de ARB.
- **Regulación:** las normas sobre tokens, DAO y las empresas detrás de ellos pueden cambiar según el país.

## Qué significa si compras con regularidad

ARB ha pasado la mayor parte de su vida cayendo desde su primer pico, así que quien compraba con regularidad fue acumulando cada vez más tokens a precios más bajos, algo que solo ayuda si el precio se recupera. Comprar una cantidad fija cada cierto tiempo reparte el riesgo de elegir mal el momento, pero no elimina el riesgo de pérdidas. Mucha gente mantiene este tipo de tokens como una parte pequeña de sus ahorros. Los resultados pasados no garantizan rentabilidades futuras.

*No es asesoramiento de inversión.*

## Fuentes

- [A gentle introduction to Arbitrum (documentación de Arbitrum)](https://docs.arbitrum.io/intro/)
- [A gentle introduction to the Arbitrum DAO (Arbitrum Foundation)](https://docs.arbitrum.foundation/gentle-intro-dao-governance)
- [Offchain Labs releases Arbitrum BoLD on mainnet (The Block, 12 de febrero de 2025)](https://www.theblock.co/post/340278/offchain-labs-releases-arbitrum-bold-on-mainnet-for-permissionless-validation)
- [Arbitrum price, market cap and all-time high (CoinGecko)](https://www.coingecko.com/en/coins/arbitrum)

---
title: Qué es un DEX y en qué se diferencia de un exchange de criptomonedas
description: ¿Qué es un DEX? Guía sencilla sobre los exchanges descentralizados: AMM, pools de liquidez, wallets, comisiones de gas y ventajas y desventajas frente a un CEX.
date: 2026-11-16
category: guides
assets: eth, sol, uni
---
**¿Qué es un DEX?** Un DEX (exchange descentralizado) es un conjunto de contratos inteligentes en una blockchain que te permite cambiar un token por otro directamente desde tu propia wallet. No hay ninguna empresa que guarde tu dinero, no hay cuenta y normalmente no hay verificación de identidad. Uniswap en Ethereum, y Raydium, Orca y Meteora en Solana, son ejemplos conocidos.

Un exchange de criptomonedas normal como Binance, Coinbase o Kraken es un **CEX** (exchange centralizado): una empresa que guarda tus fondos, cruza compradores y vendedores en su propio sistema y tiene que cumplir las normas financieras.

## Cómo funciona un DEX

### Creadores de mercado automatizados (AMM)

La mayoría de los DEX no tienen un libro de órdenes con compradores y vendedores. En su lugar usan un **creador de mercado automatizado** (AMM): una fórmula que fija el precio.

La versión clásica, la que usa Uniswap v2, es la regla del "producto constante": un pool tiene dos tokens, y la cantidad del token A multiplicada por la cantidad del token B debe mantenerse igual después de cada operación. Cuando compras el token A, añades token B al pool y retiras token A, así que A se vuelve más escaso en el pool y su precio sube.

No necesitas hacer las cuentas. La idea clave: **cuanto más grande es el pool, menos mueve el precio tu operación.**

### Pools de liquidez

Los tokens del pool los aportan los **proveedores de liquidez**: personas que depositan pares de tokens y se llevan una parte de las comisiones de trading (a menudo un 0,05–1% por swap). Su riesgo es que los precios de los dos tokens se separen, lo que puede dejarles peor que si simplemente los hubieran mantenido ("pérdida impermanente").

En los tokens recién lanzados, normalmente es el creador quien monta el primer pool. Por eso importan los bloqueos de liquidez: quien controla el pool puede retirarlo.

### Tu wallet es tu cuenta

Para usar un DEX conectas una wallet de autocustodia como MetaMask (Ethereum y redes similares) o Phantom (Solana). Cada operación es una transacción que firmas tú. Tu **frase semilla** es la llave maestra: si la pierdes, el dinero desaparece; si la compartes, otro se lo lleva.

### Gas y comisiones

Cada operación en un DEX paga una comisión de red, que en Ethereum se llama **gas**. En Ethereum sube cuando la red está saturada; las redes de capa 2 y Solana suelen ser mucho más baratas: la comisión base de Solana es de 0,000005 SOL por firma. Además del gas pagas la comisión del pool, y puedes sufrir **slippage** e **impacto en el precio** en tokens pequeños o que se mueven rápido.

## DEX vs CEX: las principales diferencias

- **Quién guarda tus fondos:** en un DEX, tú (tu wallet); en un CEX, el exchange.
- **Cuenta y verificación de identidad:** un DEX normalmente no pide nada; un CEX exige verificación de identidad (KYC).
- **Oferta de tokens:** un DEX ofrece casi cualquier token, incluidos los recién creados; un CEX solo lista tokens seleccionados.
- **Comprar con tarjeta o banco:** normalmente no es posible directamente en un DEX; es lo habitual en un CEX.
- **Comisiones:** DEX, gas, comisión del pool y slippage; CEX, comisión de trading, spread y comisión de retirada.
- **Ayuda si algo sale mal:** un DEX no tiene línea de soporte; un CEX tiene atención al cliente y a veces sistemas de protección.
- **Riesgos principales:** DEX, tokens estafa, aprobaciones peligrosas y tus propios errores; CEX, hackeos, bloqueos de cuenta e insolvencia.

## Ventajas de un DEX

- **Autocustodia.** Nadie puede congelar tu cuenta ni perder tu dinero en una quiebra.
- **Acceso abierto.** Cualquiera con una wallet puede operar, desde casi cualquier lugar.
- **Tokens nuevos primero.** Los tokens aparecen en los DEX mucho antes de cualquier listado en un exchange (o en lugar de él).
- **Transparencia.** Los pools, las operaciones y los holders se ven en la blockchain.

## Desventajas de un DEX

- **Tú eres el banco.** Un error (una dirección equivocada, una web falsa, una aprobación maliciosa) y los fondos se pierden para siempre.
- **Tokens estafa.** Cualquiera puede crear un token y un pool en minutos. La mayoría de los tokens nuevos pierden casi todo su valor; consulta nuestra [lista para detectar un rug pull]({lang}/blog/how-to-spot-a-rug-pull/).
- **Costes ocultos.** El slippage y el impacto en el precio pueden costar más que la comisión visible.
- **Sin una entrada fácil.** Normalmente primero tienes que comprar cripto en un CEX y enviarla a tu wallet.
- **Riesgo de los contratos inteligentes.** Errores o hackeos en el código de los DEX han causado grandes pérdidas.

## ¿Cuál debería usar un principiante?

Mucha gente usa los dos: un CEX regulado para pasar de moneda local a cripto, y un DEX para tokens que solo existen on-chain. Para comprar de forma periódica y a largo plazo activos grandes como Bitcoin o Ethereum, un CEX con comisiones bajas suele ser más sencillo; compara opciones en nuestra [página de exchanges]({lang}/exchanges/).

Si quieres explorar memecoins y otros tokens on-chain, empieza con cantidades muy pequeñas, una wallet aparte y las monedas más consolidadas de nuestra [página de memecoins]({lang}/memes/). Nuestra guía paso a paso [cómo comprar una memecoin en Solana]({lang}/blog/how-to-buy-memecoins-on-solana/) muestra el proceso completo, incluidas herramientas como [GMGN](/go/gmgn?from=blog&l=es).

## Términos habituales de un DEX

- **Swap**: cambiar un token por otro.
- **Par**: los dos tokens de un pool, como SOL/USDC.
- **Tolerancia de slippage**: el cambio máximo de precio que aceptas.
- **Approve**: permiso para que un contrato mueva un token desde tu wallet (sobre todo en redes tipo Ethereum). Revoca las aprobaciones antiguas que ya no necesites.
- **Agregador**: un servicio que reparte tu operación entre varios DEX para conseguir mejor precio, como Jupiter en Solana o 1inch en Ethereum.

## Preguntas frecuentes

### ¿Un DEX es más seguro que un CEX?

Elimina el riesgo de que el exchange pierda o congele tus fondos, pero añade el riesgo de tus propios errores y de los tokens estafa. Ninguno está libre de riesgo.

### ¿Necesito identificarme para usar un DEX?

Normalmente no, porque operas desde tu propia wallet. Las leyes y los impuestos de tu país te siguen aplicando.

### ¿Por qué ha fallado mi operación en un DEX?

Motivos habituales: no tener suficiente moneda nativa para el gas, un slippage demasiado bajo para un precio que se mueve rápido o un token que bloquea las ventas.

### ¿Las operaciones en un DEX tributan?

En muchos países, sí: cambiar un token por otro puede contar como una venta. Guarda un registro de tus operaciones.

## Fuentes

- [Cómo funciona Uniswap (documentación de Uniswap)](https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works)
- [Gas y comisiones (ethereum.org)](https://ethereum.org/en/developers/docs/gas/)
- [Documentación de Solana: estructura de comisiones](https://solana.com/docs/core/fees/fee-structure)

*No es asesoramiento de inversión. Esta guía explica cómo funcionan los DEX y no recomienda ninguna plataforma ni ningún token.*

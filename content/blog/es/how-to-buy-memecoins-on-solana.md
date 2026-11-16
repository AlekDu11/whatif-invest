---
title: Cómo comprar memecoins en Solana: paso a paso con GMGN
description: Cómo comprar una memecoin en Solana con seguridad: crea tu wallet, cárgala con SOL, revisa contrato, liquidez y holders, ajusta el slippage y vende.
date: 2026-11-16
category: guides
assets: sol, bonk, wif
---
**¿Cómo se compra una memecoin en Solana?** En resumen: creas una wallet de autocustodia, le cargas algo de SOL, buscas la dirección del contrato del token, compruebas que no sea una trampa y cambias SOL por el token en un exchange descentralizado (DEX) o en una herramienta de trading como [GMGN](/go/gmgn?from=blog&l=es). Esta guía te explica cada paso en lenguaje sencillo.

Antes de empezar, un dato honesto: la mayoría de las memecoins nuevas pierden casi todo su valor, a menudo en cuestión de horas. Un informe de 2025 de Solidus Labs clasificó el 98,6% de los tokens lanzados en la plataforma Pump.fun como rug pulls o esquemas de pump-and-dump. Usa solo dinero que puedas permitirte perder por completo.

## Qué necesitas

- Un móvil o un ordenador con un navegador actualizado.
- Una wallet de Solana que controles tú mismo (autocustodia), por ejemplo Phantom, Solflare o Backpack.
- Algo de SOL, la moneda propia de la red Solana. Con SOL pagas la memecoin y las comisiones de la red.
- 30 minutos, y papel y bolígrafo para tu frase semilla.

## Paso 1. Crea una wallet de autocustodia

Una wallet de autocustodia significa que las claves las tienes **tú**, no un exchange. Eso te da control total, y también toda la responsabilidad.

1. Descarga la wallet solo desde su web oficial o desde la tienda oficial de aplicaciones de tu móvil. Las apps de wallet falsas son una trampa habitual.
2. Crea una wallet nueva. La app te mostrará una **frase semilla** de 12 o 24 palabras.
3. Escribe las palabras en papel, en orden, y guarda el papel en un lugar seguro. No hagas captura de pantalla, no la guardes en notas ni en el correo y no la pegues en ninguna web.
4. Pon una contraseña o un PIN fuerte en la app.

**Regla de la frase semilla:** quien tenga estas palabras puede llevarse todo lo que hay en la wallet. Ningún soporte real, exchange ni "airdrop" te la pedirá nunca. Si alguien lo hace, es una estafa.

Un buen hábito: crea una wallet aparte "de trading" para memecoins y guarda tus ahorros a largo plazo en otro sitio, idealmente en una wallet física (hardware wallet).

## Paso 2. Carga la wallet con SOL

La forma más sencilla es comprar SOL en un exchange centralizado y retirarlo a tu wallet.

1. Elige un exchange regulado en nuestra [página de exchanges]({lang}/exchanges/) y compra SOL con tarjeta o transferencia bancaria.
2. Copia la dirección de Solana de tu wallet (empieza por letras y números y tiene unos 32–44 caracteres).
3. En el exchange, elige "Retirar", selecciona SOL y la red **Solana**, y pega la dirección.
4. Envía primero una cantidad pequeña de prueba. Cuando llegue, envía el resto.

Deja siempre un poco de SOL sin gastar (por ejemplo 0,01–0,02 SOL). Lo necesitas para pagar comisiones, incluida la de vender más adelante.

## Paso 3. Encuentra el token y el contrato correcto

Las memecoins se copian mucho. Diez tokens pueden tener el mismo nombre y logo; solo uno es el que buscas.

- Consigue la **dirección del contrato** (también llamada dirección de mint) de una fuente fiable: la cuenta verificada del proyecto, una web de datos conocida o nuestra [página de memecoins]({lang}/memes/) para monedas consolidadas.
- Pega la dirección del contrato en GMGN o en tu DEX en lugar de buscar por nombre.
- Compara los primeros y últimos caracteres de la dirección con la fuente. Los estafadores crean direcciones que se parecen.

## Paso 4. Revisa el token antes de comprar

Este es el paso que más dinero te ahorra. Herramientas como GMGN muestran la mayoría de estas comprobaciones en la página del token.

1. **Liquidez.** ¿Cuánto dinero hay en el pool de trading? Con muy poca liquidez, hasta una venta pequeña mueve mucho el precio, y puede que no consigas vender a un precio justo.
2. **Liquidez bloqueada o quemada.** Si el creador puede retirar el pool, puede "tirar de la alfombra" y dejarte con un token que nadie puede comprar.
3. **Autoridad de mint.** Si no está revocada, el creador puede emitir tokens nuevos y diluirte.
4. **Autoridad de congelación (freeze).** Si no está revocada, el creador puede congelar tus tokens para que no puedas vender.
5. **Top holders.** Si las 10 mayores wallets (sin contar el pool) tienen una parte grande, pueden hundir el precio vendiendo.
6. **Antigüedad e historial.** Un token creado hace unos minutos con un gráfico vertical es un boleto de lotería, no una inversión.

Nuestra [lista para detectar un rug pull]({lang}/blog/how-to-spot-a-rug-pull/) explica en detalle las diez señales de alerta.

## Paso 5. Ajusta el slippage y haz el swap

El **slippage** (deslizamiento) es el cambio máximo de precio que aceptas entre que pulsas "comprar" y se confirma la operación. Los precios de las memecoins se mueven rápido, así que la app te deja elegirlo.

- Un slippage bajo (alrededor del 1%) te protege de un mal precio, pero la operación puede fallar.
- Un slippage alto (10% o más) casi siempre se ejecuta, pero puedes pagar mucho más de lo esperado y los bots pueden aprovecharse de ti.
- Empieza bajo y súbelo solo si entiendes lo que pierdes a cambio.

Después conecta tu wallet a [GMGN](/go/gmgn?from=blog&l=es) o a un DEX, introduce la cantidad de SOL, revisa el número estimado de tokens y el impacto en el precio, y confirma en tu wallet. Tu wallet muestra lo que estás firmando: léelo. Si una web te pide aprobar algo inesperado, cancela.

## Paso 6. Entiende las comisiones

En Solana, la comisión base de la red es mínima: 5.000 lamports (0,000005 SOL) por firma. En momentos de mucho tráfico también puedes pagar una **comisión de prioridad** opcional para que tu operación se procese antes. Además:

- La plataforma de trading o el bot puede cobrar su propia comisión (a menudo alrededor del 1% por operación); revísala antes de operar.
- El pool cobra una comisión de swap que va a los proveedores de liquidez.
- El **impacto en el precio** y el slippage son costes ocultos, a menudo mayores que las comisiones.

Una operación de ida y vuelta (comprar y vender) puede costarte fácilmente varios puntos porcentuales en un token pequeño y con poca liquidez.

## Paso 7. Vender

Vender funciona igual pero al revés: eliges el token, introduces la cantidad, revisas el slippage y confirmas. Algunos consejos prácticos:

- Asegúrate de que todavía tienes SOL para la comisión.
- Si la venta falla una y otra vez con "insufficient liquidity" o un error raro, el token puede ser un honeypot: un token diseñado para que puedas comprar pero no vender.
- Decide de antemano cuánta pérdida puedes aceptar. Las memecoins pueden caer un 50–90% en minutos.
- En muchos países, cada swap puede tributar. Guarda un registro de tus operaciones.

## Los riesgos, claros

- **Perderlo todo es habitual.** CoinGecko consideró muertos a finales de 2025 más de la mitad de todos los tokens que sigue desde 2021, con unos 11,6 millones de fracasos solo en 2025.
- **Los de dentro se mueven primero.** Los creadores y los bots suelen comprar en los primeros segundos y vender a la primera ola de compradores.
- **Estafas y phishing.** Webs falsas, falso soporte y solicitudes de "approve" maliciosas pueden vaciar tu wallet.
- **Sin protección.** Las operaciones on-chain no se pueden revertir y normalmente no hay regulador ni línea de soporte que te ayude.
- **No es DCA.** La inversión periódica funciona mejor con activos con un largo historial. Puedes comparar cómo les ha ido a las memecoins consolidadas con el tiempo en nuestra [página de memecoins]({lang}/memes/).

## Preguntas frecuentes

### ¿Cuál es la forma más barata de comprar una memecoin en Solana?

Las comisiones de red en Solana son muy bajas, así que el coste real suele ser la comisión de la plataforma, la del pool y el impacto en el precio. Operar con cantidades pequeñas en tokens con una liquidez decente reduce los costes ocultos.

### ¿Puedo comprar memecoins de Solana en un exchange normal?

Las memecoins más grandes y antiguas, como Bonk o dogwifhat, cotizan en muchos exchanges centralizados. Los tokens recién lanzados normalmente solo existen en los DEX.

### ¿GMGN es una wallet?

GMGN es una herramienta de trading y análisis de tokens on-chain. Comprueba siempre qué wallet estás conectando o creando, y nunca compartas tu frase semilla con ninguna web.

### ¿Cuánto debería meter en memecoins?

Solo una cantidad que estés totalmente dispuesto a perder. Mucha gente lo trata como un boleto de lotería, separado de sus ahorros a largo plazo.

## Fuentes

- [El 98% de los tokens de Pump.fun han sido rug pulls o fraudes, según un nuevo informe (CoinDesk)](https://hotfix.coindesk.com/business/2025/05/07/98-of-tokens-on-pump-fun-have-been-rug-pulls-or-an-act-of-fraud-new-report-says)
- [Solidus Labs: informe de rug pulls 2025](https://www.soliduslabs.com/reports/solana-rug-pulls-pump-dumps-crypto-compliance)
- [Documentación de Solana: estructura de comisiones](https://solana.com/docs/core/fees/fee-structure)
- [Monedas muertas: más del 50% de las criptomonedas han fracasado, informe de CoinGecko (Crowdfund Insider)](https://www.crowdfundinsider.com/2026/01/257221-dead-coins-over-50-of-cryptocurrencies-have-failed-report-reveals/)

*No es asesoramiento de inversión. Las memecoins son extremadamente arriesgadas; esta guía explica cómo funciona el proceso y no recomienda comprar ni vender ningún token.*

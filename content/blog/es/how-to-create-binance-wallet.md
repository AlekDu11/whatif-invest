---
title: Cómo crear una Binance Wallet y comprar una memecoin: paso a paso
description: Crea Binance Wallet en la app de Binance, haz la copia, pasa monedas desde tu cuenta de Binance, busca el token por contrato y haz el swap con seguridad.
date: 2026-11-23T12:30:00Z
category: learn
track: memes
step: 5
assets: bnb, sol, doge
stat: 3
stat_label: partes de la clave protegen una Binance Wallet; necesitas 2 para entrar
---
**¿Cómo se crea una Binance Wallet?** Abre la app de Binance, cambia arriba a la pestaña **Wallet** (billetera), toca **Create Keyless Wallet** (crear wallet sin clave) y haz la copia de seguridad con una contraseña de recuperación. Se tarda unos minutos, no necesita frase semilla y te da una wallet de autocustodia (una wallet en la que controlas tú las monedas, no el exchange) para comprar tokens on-chain como las memecoins.

> **Claves**
> - Binance Wallet está dentro de la app de Binance. Necesitas una cuenta de Binance verificada, pero las monedas de la wallet son de autocustodia: la copia de seguridad es cosa tuya.
> - Es una wallet "sin clave" (MPC): la clave se divide en 3 partes, una en tu móvil, otra en tu copia en la nube y otra en Binance. Con 2 cualesquiera se abre la wallet.
> - No te saltes nunca la copia de seguridad. Si pierdes el móvil **y** olvidas la contraseña de recuperación, Binance no puede restaurar la wallet.

Antes de empezar: la mayoría de las memecoins nuevas pierden casi todo su valor. Usa solo dinero que puedas permitirte perder por completo; mira [qué son las memecoins]({lang}/blog/what-are-memecoins/).

## Qué necesitas

- Un móvil con la app oficial de Binance (descárgala solo de App Store, Google Play o binance.com: abundan las apps falsas).
- Una cuenta de Binance con la verificación de identidad hecha (KYC, mostrar tu documento). Si aún no tienes una, puedes registrarte con nuestro enlace: [Binance Wallet](/go/binance-web3?from=learn&l=es).
- Un poco de BNB o SOL en tu cuenta de Binance para comprar y pagar las comisiones de red.

## Paso 1. Abre la wallet

1. Inicia sesión en la app de Binance.
2. Arriba en la pantalla, cambia de **Exchange** a **Wallet**.
3. Toca **Create Keyless Wallet**. (Si ya tienes otra wallet, la otra opción es **Import Wallet** (importar wallet); los principiantes no la necesitan.)

Crearla lleva segundos. La app no te muestra 12 o 24 palabras semilla: en su lugar usa MPC (computación multiparte: la clave se divide en piezas que nunca están en un mismo sitio).

## Paso 2. Haz la copia de seguridad (no te la saltes)

La app ofrece tres formas de guardar tu parte de respaldo. Elige una:

- **iCloud** o **Google Drive**. Pones una **contraseña de recuperación** que solo conoces tú. La parte se cifra con ella y se guarda en tu nube.
- **Código QR.** Pones una contraseña de recuperación y guardas un código QR; la parte se almacena en una nube descentralizada.
- **Quick Backup** (copia rápida). Confirmas con Face ID o huella; sin contraseña, pero la parte la guarda un proveedor externo.

Escribe la contraseña de recuperación en papel y guárdala en un lugar seguro. Después compruébalo: toca **Settings** (ajustes; arriba a la izquierda en Home o Assets) → **Wallet Management** (gestión de wallets). Deberías ver la etiqueta **Backed Up** (copia guardada).

## Paso 3. Pasa monedas de Binance a la wallet

1. En la wallet, toca **Receive** (recibir) → **Withdraw from Binance Exchange** (retirar desde el exchange de Binance).
2. Elige la moneda (por ejemplo BNB) **y la red** (BNB Smart Chain para BNB, Solana para SOL). La red tiene que coincidir.
3. Escribe la cantidad. La app muestra la comisión y la cantidad final antes de confirmar.
4. Elige si el dinero sale de tu cuenta Spot o Funding, toca **Withdraw** (retirar), revisa la dirección y la red, y pulsa **Confirm** (confirmar).

Empieza con una pequeña cantidad de prueba. Una transferencia confirmada no se puede cancelar. Deja siempre un poco de BNB o SOL en la wallet: cada acción en la blockchain cuesta una comisión de red (gas), incluso si falla.

## Paso 4. Encuentra el token correcto por su dirección de contrato

Muchas memecoins tienen copias con el mismo nombre y logo. La única identificación fiable es la **dirección del contrato** (una cadena larga de letras y números, única para cada token).

1. Saca la dirección de una fuente fiable: la cuenta verificada del proyecto, una gran web de datos o la página del token en nuestra [página de memecoins]({lang}/memes/).
2. En la pantalla **Markets** (mercados) o **Trade** (operar) de la wallet, pega la dirección en el buscador en lugar de escribir el nombre.
3. Compara los primeros y los últimos 4–6 caracteres con tu fuente.

## Paso 5. Revisa el token antes de comprar

En nuestra [página de memecoins]({lang}/memes/), cada página de token muestra la revisión de seguridad de Binance y las cifras clave. Fíjate en:

- **Liquidez**: cuánto dinero hay en el pool de trading. Poca liquidez = puede que no consigas vender.
- **Holders y porcentaje del top 10**: si unas pocas wallets tienen la mayor parte del suministro, pueden hundir el precio.
- **Antigüedad**: un token creado hace una hora es un boleto de lotería.
- **Avisos**: si aparece cualquier aviso de riesgo o de seguridad, para.

La propia Binance dice que no revisa los tokens listados en Meme Rush (su feed de memecoins recién creadas), así que la revisión te toca a ti. Nuestra [lección sobre estafas y rug pulls]({lang}/blog/memecoin-scams-rug-pull/) recoge las señales de alarma.

## Paso 6. Haz el swap

1. Abre **Trade** → **Swap** (intercambio). Elige con qué pagas (BNB) y el token que quieres, en la misma red.
2. Escribe una cantidad pequeña. Lee el tipo de cambio, el **slippage** (deslizamiento: el mayor cambio de precio que aceptas antes de que la operación falle) y la comisión de red.
3. Algunos tokens necesitan antes un paso de **Approve** (aprobar); cuesta una pequeña comisión.
4. Toca **Swap** y confirma con tu passkey o 2FA.

Para vender, haz lo mismo al revés. Si quieres ver los tokens más nuevos, la pestaña Markets tiene **Meme Rush**: los tokens recién creados cotizan ahí en una "curva de vinculación" (bonding curve) y no se pueden sacar de la wallet hasta que "migran" a un DEX normal (exchange descentralizado). Es el rincón más arriesgado del mercado.

> **⚠️ Cuidado**
> - **Sin copia de seguridad, o con la contraseña guardada en capturas de pantalla.** Si pierdes el móvil y la contraseña, las monedas desaparecen para siempre.
> - **Red equivocada o dirección equivocada.** Las preguntas frecuentes de Binance dicen que los tokens enviados a una dirección equivocada no se pueden devolver. Envía siempre una cantidad de prueba.
> - **Tokens falsos y mensajes de "soporte".** Busca solo por dirección de contrato. El personal de Binance nunca te pedirá tu contraseña de recuperación ni que "verifiques" tu wallet en una web.

Siguiente lección: cómo conectar Binance Wallet a una web DEX y devolver monedas a Binance. Todas las lecciones en la sección [Aprender]({lang}/learn/).

## Fuentes

- [Binance: Frequently Asked Questions on Binance Wallet](https://www.binance.com/en/support/faq/5a3fc86a702b43e1a4a398ebd8853b77)
- [Binance: What Is a Keyless Wallet and Why Do I Need to Back It Up?](https://www.binance.com/en/support/faq/4efebcb9a937417ca31baa2f7754c50f)
- [Binance: How to Back Up My Binance Wallet?](https://www.binance.com/en/support/faq/53521dedad474c908ec3761a935cb8d6)
- [Binance: How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance: What Is Binance Wallet Swap?](https://www.binance.com/en/support/faq/7ebe19e8ff884cc09a9dbb064aff131f)
- [Binance: Introducing Meme Rush — Fair Mode (9 Oct 2025)](https://www.binance.com/en/support/announcement/detail/c21eac66543c4a62b8b6868cb01ba4f3)

*No es asesoramiento de inversión. Las memecoins son extremadamente arriesgadas; esta guía explica cómo funciona la app y no recomienda comprar ningún token. Binance Wallet puede no estar disponible en todos los países.*

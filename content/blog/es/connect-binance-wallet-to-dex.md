---
title: Cómo conectar Binance Wallet a un DEX y devolver monedas: paso a paso
description: Conecta Binance Wallet a un DEX de forma segura, devuelve monedas a tu cuenta de Binance en la red correcta y quita permisos viejos, en pasos sencillos.
date: 2026-11-23T14:30:00Z
category: learn
track: memes
step: 6
assets: bnb, sol, cake
stat: 1
stat_label: pequeña transferencia de prueba antes de cada dirección o red nueva
---
**¿Cómo se conecta Binance Wallet a un DEX?** Abre la web oficial del DEX, pulsa **Connect Wallet** (conectar wallet), elige Binance Wallet (o WalletConnect y escanea el código QR con la app de Binance) y confirma en la app. Para devolver monedas, copia tu **dirección de depósito** de Binance para la misma moneda y red, y envía a ella desde la wallet: primero una cantidad pequeña de prueba.

> **Claves**
> - Un DEX (exchange descentralizado: una web donde cambias tokens directamente desde tu propia wallet) nunca necesita tu contraseña de recuperación ni tu frase semilla. Conectar solo permite a la web *pedirte* firmas; nada se mueve hasta que confirmas.
> - La red tiene que coincidir en ambos lados (BNB Smart Chain con BNB Smart Chain, Solana con Solana). Una red o dirección equivocada puede hacer que pierdas las monedas.
> - Cada «Approve» permite a una web gastar un token por ti. Da permisos pequeños y quita los que ya no uses.

Esta lección continúa [Cómo crear una Binance Wallet]({lang}/blog/how-to-create-binance-wallet/). Las memecoins son extremadamente arriesgadas: usa solo dinero que puedas permitirte perder.

## Paso 1. Abre la web auténtica

Las webs falsas de DEX con el mismo logo son una de las trampas más comunes.

1. Escribe tú la dirección o usa un marcador. No pulses anuncios en el buscador ni enlaces de chats.
2. Revisa la barra de direcciones letra por letra.
3. Comprueba que el DEX funciona en la red donde están tus monedas.

## Paso 2. Conecta la wallet

Hay tres formas, según tu dispositivo:

- **En un ordenador con la extensión Binance Wallet** (Chrome o Brave). Inicia sesión en la extensión escaneando su código QR con la app de Binance. Luego, en el DEX pulsa **Connect** o **Connect Wallet**, elige Binance Wallet y confirma la ventana emergente.
- **En un ordenador sin la extensión.** En el DEX pulsa **Connect Wallet → WalletConnect**. Aparece un código QR. Escanéalo con el lector de la app de Binance y toca **Connect**.
- **En el móvil.** Abre el DEX en el navegador del móvil, pulsa **Connect Wallet**, elige Binance Wallet en la lista y confirma en la app.

Antes de confirmar, lee la ventana: el nombre de la web, la dirección y la red. Si algo no cuadra, pulsa Cancel (cancelar).

## Paso 3. Haz el swap y lee cada firma

1. Elige la moneda con la que pagas y el token que quieres (busca el token por su **dirección de contrato**, no por el nombre).
2. Pon una cantidad pequeña y revisa el tipo de cambio, el slippage (deslizamiento: el mayor cambio de precio que aceptas) y la comisión de red.
3. La primera vez que vendes un token, la web pide **Approve** (permiso para gastar ese token). Si la app te deja, pon una cantidad en lugar de «unlimited» (ilimitado).
4. Confirma el swap en la app. Si una solicitud de firma es una página de código ilegible o no tiene sentido, **no la firmes**.

## Paso 4. Devuelve monedas a tu cuenta de Binance

1. En la app de Binance, cambia a **Exchange** → **Assets** → **Deposit** (exchange → activos → depositar). Elige la moneda (por ejemplo BNB).
2. Elige la **red** (por ejemplo BNB Smart Chain). Copia la dirección de depósito. Algunas monedas necesitan además un **memo/tag** (etiqueta): cópialo también.
3. Cambia a **Wallet** → **Send** (wallet → enviar). Elige la misma moneda y la misma red. Pega la dirección (y el memo, si lo hay).
4. Envía primero una cantidad pequeña de prueba. Cuando llegue a tu cuenta de Binance, envía el resto.

Deja un poco de BNB o SOL en la wallet: cada acción en la blockchain, incluso una fallida, cuesta una comisión de red. Algunas memecoins no se pueden depositar en el exchange (no las admite); para pasarlas a dinero, primero cámbialas en la wallet por BNB, SOL o USDT.

## Paso 5. Desconecta y limpia

1. Al terminar, desconecta la web (en los ajustes de webs conectadas o de WalletConnect de la wallet, o con el botón **Disconnect** del DEX).
2. De vez en cuando revisa tus permisos de tokens y revoca (cancela) los que no necesites. Revocar cuesta una pequeña comisión.
3. En un ordenador compartido, cierra la sesión de la extensión.

Sigue los tokens que compraste en [tu cartera]({lang}/me/) y mira datos en vivo de memecoins en nuestra [página de memecoins]({lang}/memes/).

> **⚠️ Cuidado**
> - **Una web o un «soporte» te pide la contraseña de recuperación, la frase semilla o «sincronizar la wallet».** Ningún DEX real ni empleado de Binance lo hace nunca. Cierra la página.
> - **Permisos ilimitados y firmar a ciegas.** Un permiso o una firma maliciosos pueden dejar que un estafador vacíe ese token más tarde, sin que vuelvas a confirmar.
> - **Red equivocada, memo olvidado o una dirección pegada que ha cambiado.** Un malware puede cambiar una dirección copiada. Compara siempre los primeros y últimos caracteres y prueba con poco.

Próxima lección: cómo revisar una memecoin antes de comprar. Todas las lecciones están en la sección [Aprender]({lang}/learn/).

## Fuentes

- [Binance: What Is Binance Wallet Extension and How Does It Work?](https://www.binance.com/en/support/faq/ebfa9f504ec548968bf0c1ed591a3eaa)
- [Binance Academy: How to Use WalletConnect](https://www.binance.com/en/academy/articles/how-to-use-walletconnect)
- [Binance: How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance.US: How to stay safe when using dApps on your Web3 Wallet](https://support.binance.us/en/articles/15090007-how-to-stay-safe-when-using-dapps-on-your-binance-us-wallet)

*No es asesoramiento de inversión. Esta guía explica cómo funcionan las herramientas y no recomienda comprar ningún token. Binance Wallet puede no estar disponible en todos los países.*

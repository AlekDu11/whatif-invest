---
title: Cara menarik kripto dari exchange ke dompet sendiri: langkah demi langkah
description: Pindahkan koin dari exchange ke dompet sendiri dengan aman: salin alamat yang benar, pilih jaringan yang sama, isi memo bila perlu, dan kirim tes kecil dulu.
date: 2026-11-25T09:40:00Z
category: learn
track: crypto
step: 6
assets: btc, eth, sol, bnb
stat: 1 jaringan
stat_label: exchange dan dompet harus memakai jaringan yang sama, kalau tidak koin bisa hilang
---
**Bagaimana cara menarik kripto ke dompet sendiri?** Di dompet Anda, salin **alamat penerima** (receive address) untuk koin itu. Lalu di exchange buka **Withdraw** (Tarik), tempel alamat tersebut, pilih **jaringan yang sama** dengan dompet Anda, masukkan jumlah tes yang kecil, dan konfirmasi dengan 2FA. Setelah tes sampai, kirim sisanya.

> **Poin penting**
> - Tiga hal harus cocok: **koin**, **alamat**, dan **jaringan** (blockchain yang dilalui koin, misalnya Ethereum, BNB Smart Chain, TRON, atau Solana). Binance memperingatkan bahwa koin yang dikirim lewat jaringan yang salah bisa hilang selamanya.
> - Beberapa koin (seperti XRP, XLM, atau ATOM) juga butuh **memo** atau **tag** (angka pendek yang memberi tahu penerima milik siapa koin itu). Tanpa itu, transfer bisa tertahan atau masuk ke orang lain.
> - **Selalu kirim tes kecil dulu.** Penarikan tidak bisa dibatalkan begitu koin sudah keluar dari exchange.

Pelajaran ini melanjutkan [Cara mengatur pembelian rutin]({lang}/blog/how-to-set-up-a-recurring-buy/). Kenapa Anda mungkin ingin punya dompet sendiri dijelaskan di [dompet hot vs cold]({lang}/blog/crypto-wallets-hot-vs-cold/).

## Sebelum mulai

Anda butuh dua hal. Pertama, akun exchange yang berisi koin (dilindungi 2FA — lihat [Cara mendaftar di exchange kripto]({lang}/blog/how-to-register-on-a-crypto-exchange/)). Kedua, aplikasi dompet sendiri yang sudah diatur, dengan **seed phrase** (12 atau 24 kata rahasia untuk memulihkan dompet) yang ditulis di kertas dan disimpan secara offline. Jangan pernah mengetik seed phrase di tempat lain — tidak ada exchange, situs, atau petugas "support" yang membutuhkannya.

## Langkah 1 — Salin alamat penerima dompet Anda

1. Buka aplikasi dompet dan ketuk **Receive** (kadang **Deposit**).
2. Pilih koinnya, misalnya Bitcoin atau USDT.
3. Kalau dompet bertanya, pilih jaringannya. Catat jaringan yang mana — misalnya "USDT di TRON (TRC20)" atau "USDT di Ethereum (ERC20)".
4. Ketuk **Copy** di sebelah alamat. Jangan mengetiknya manual.

Alamat adalah deretan panjang huruf dan angka. Alamat Bitcoin sering diawali **bc1**, alamat Ethereum dan BNB Smart Chain diawali **0x**, alamat TRON diawali **T**.

## Langkah 2 — Buka Withdraw di exchange

Di aplikasi Binance menunya **Assets → Spot → Send → Withdraw Crypto**; di situs web **Wallet → Overview → Withdraw**. Exchange lain punya tombol **Withdraw** di sebelah tiap koin pada layar dompet atau portofolio. Pilih koin yang sama dengan Langkah 1.

## Langkah 3 — Tempel alamat dan pilih jaringan

1. Tempel alamat di kolom **Address**.
2. Bandingkan **4 karakter pertama dan 4 karakter terakhir** dengan dompet Anda. Ada malware yang mengganti alamat yang disalin dengan alamat pencuri.
3. Pilih **jaringan** (network). Harus sama dengan yang ditunjukkan dompet di Langkah 1. Binance bisa menyarankan jaringan secara otomatis — tetap periksa. Jangan memilih jaringan hanya karena biayanya paling murah.
4. Kalau muncul kolom **Memo** atau **Tag** dan dompet Anda memberinya, isi kolom itu. Kalau dompet Anda tidak menunjukkan memo, biasanya memang tidak perlu — tapi cek lagi di halaman bantuan dompet.

Tips: kalau ragu, simpan alamat di **Address Management** (buku alamat) exchange. Binance juga punya **whitelist**: setelah diaktifkan, penarikan hanya bisa ke alamat yang disimpan. Ini membantu kalau ada yang mencuri kata sandi Anda.

## Langkah 4 — Kirim tes kecil

1. Masukkan jumlah kecil — sedikit di atas penarikan minimum yang tertera di layar.
2. Lihat baris **biaya jaringan** (network fee) dan **yang akan Anda terima** (you will receive). Biayanya tetap per penarikan, jadi pada jumlah sangat kecil biaya bisa jadi bagian yang besar.
3. Tekan **Withdraw** dan konfirmasi dengan kode 2FA atau passkey. Beberapa exchange juga mengirim e-mail konfirmasi — buka dan tekan **Confirm**.

## Langkah 5 — Cek apakah sudah sampai, lalu kirim sisanya

1. Tunggu. Transfer bisa makan waktu dari beberapa detik sampai sekitar satu jam, tergantung jaringan dan kepadatannya.
2. Di exchange, buka riwayat penarikan untuk melihat status dan **TxID** (ID transaksi, yang bisa Anda cari di situs block explorer).
3. Setelah koin muncul di dompet, ulangi Langkah 2–4 untuk sisanya. Alamatnya sudah ada di riwayat atau buku alamat, jadi kali kedua lebih cepat.

Tambahkan koin ke [portofolio Anda]({lang}/me/) agar nilainya bisa dipantau di satu tempat, di mana pun koin itu disimpan.

> **⚠️ Hati-hati**
> - **Jaringan salah.** USDT ada di banyak jaringan. Mengirim USDT "TRC20" ke alamat yang hanya menerima "ERC20" bisa berarti koin hilang. Periksa jaringan dua kali.
> - **Memo atau tag lupa diisi.** Exchange dan dompet yang butuh memo tidak bisa tahu milik siapa koin yang masuk tanpa memo itu. Pemulihan, kalau memang bisa, lambat dan dikenai biaya.
> - **"Support" palsu dan situs "verifikasi alamat".** Pihak resmi tidak pernah meminta seed phrase atau menyuruh Anda "memverifikasi" dompet dengan mengirim koin. Tarik koin hanya lewat aplikasi atau situs resmi.

## Artinya jika Anda membeli secara rutin

Kalau Anda membeli sedikit setiap minggu atau bulan, Anda tidak perlu menarik setelah setiap pembelian — tiap penarikan ada biayanya. Banyak orang membiarkan koin terkumpul di exchange, lalu sesekali memindahkannya ke dompet sendiri, misalnya sekali per kuartal, dalam satu transfer yang lebih besar. Contoh dari kalkulator kami: $10 per hari di Bitcoin selama 3 tahun (total {{dcainv:3}}) menjadi {{dca:btc:3}} ({{dcaroi:btc:3}}). Ini hasil masa lalu, bukan ramalan. Bitcoin saat ini di {{price:btc}}; lihat [halaman Bitcoin]({lang}/btc/).

Pelajaran sebelumnya: [Cara mengatur pembelian rutin]({lang}/blog/how-to-set-up-a-recurring-buy/). Pelajaran berikutnya: cara menjual kripto dan mencairkan uang ke rekening bank. Bandingkan exchange di [halaman exchange]({lang}/exchanges/) kami; semua pelajaran ada di [halaman Belajar]({lang}/learn/).

## Sumber

- [Binance Support: How to deposit/withdraw cryptocurrency on Binance (diperbarui Maret 2026)](https://www.binance.com/en/support/faq/85a1c394ac1d489fb0bfac0ef2fceafd)
- [Binance Support: How to retrieve a crypto deposit with a wrong or missing tag/memo](https://www.binance.com/en/support/faq/40b87335db904481888ef406b105442b)
- [Binance.US Help Center: How to withdraw crypto from your Binance.US account (Juni 2026)](https://support.binance.us/en/articles/9842854-how-to-withdraw-crypto-from-your-binance-us-account)

*Bukan nasihat investasi.*

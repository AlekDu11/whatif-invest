---
title: Cara menghubungkan Binance Wallet ke DEX dan memindahkan koin kembali: langkah demi langkah
description: Hubungkan Binance Wallet ke situs DEX dengan aman, kirim koin kembali ke akun Binance lewat jaringan yang benar dan hapus approval lama — langkah sederhana.
date: 2026-11-23T14:30:00Z
category: learn
track: memes
step: 6
assets: bnb, sol, cake
stat: 1
stat_label: transfer uji kecil sebelum setiap alamat atau jaringan baru
---
**Bagaimana cara menghubungkan Binance Wallet ke DEX?** Buka situs resmi DEX, tekan **Connect Wallet**, pilih Binance Wallet (atau WalletConnect lalu pindai kode QR dengan aplikasi Binance) dan konfirmasi di aplikasi. Untuk memindahkan koin kembali, salin **alamat deposit** Binance untuk koin dan jaringan yang sama, lalu kirim ke sana dari wallet — jumlah uji kecil dulu.

> **Poin penting**
> - DEX (bursa terdesentralisasi — situs tempat Anda menukar token langsung dari wallet sendiri) tidak pernah butuh kata sandi pemulihan atau seed phrase Anda. Menghubungkan hanya membuat situs bisa *meminta* tanda tangan; tidak ada yang berpindah sebelum Anda konfirmasi.
> - Jaringan harus sama di kedua sisi (BNB Smart Chain ke BNB Smart Chain, Solana ke Solana). Jaringan atau alamat yang salah bisa membuat koin hilang.
> - Setiap "Approve" mengizinkan situs membelanjakan token untuk Anda. Beri izin kecil dan hapus yang tidak dipakai lagi.

Pelajaran ini lanjutan dari [Cara membuat Binance Wallet]({lang}/blog/how-to-create-binance-wallet/). Memecoin sangat berisiko — gunakan hanya uang yang siap Anda relakan.

## Langkah 1 — Buka situs yang asli

Situs DEX palsu dengan logo yang sama adalah salah satu jebakan paling umum.

1. Ketik alamatnya sendiri atau pakai bookmark. Jangan klik iklan di hasil pencarian atau tautan di chat.
2. Periksa address bar huruf demi huruf.
3. Pastikan DEX bekerja di jaringan tempat koin Anda berada.

## Langkah 2 — Hubungkan wallet

Ada tiga cara, tergantung perangkat:

- **Di komputer dengan ekstensi browser Binance Wallet** (Chrome atau Brave). Masuk ke ekstensi dengan memindai kode QR-nya memakai aplikasi Binance. Lalu di DEX tekan **Connect** atau **Connect Wallet**, pilih Binance Wallet dan konfirmasi pop-up.
- **Di komputer tanpa ekstensi.** Di DEX tekan **Connect Wallet → WalletConnect**. Kode QR muncul. Pindai dengan pemindai di aplikasi Binance dan ketuk **Connect**.
- **Di ponsel.** Buka DEX di browser ponsel, tekan **Connect Wallet**, pilih Binance Wallet dari daftar dan konfirmasi di aplikasi.

Sebelum konfirmasi, baca pop-up: nama situs, alamat, dan jaringan. Kalau ada yang terlihat salah, tekan Cancel.

## Langkah 3 — Swap dan baca setiap tanda tangan

1. Pilih koin untuk membayar dan token yang diinginkan (cari token lewat **alamat kontrak**, bukan namanya).
2. Masukkan jumlah kecil dan periksa kurs, slippage (perubahan harga terbesar yang Anda terima) dan biaya jaringan.
3. Pertama kali menjual sebuah token, situs meminta **Approve** (izin membelanjakan token itu). Kalau aplikasi memungkinkan, isi jumlahnya alih-alih "unlimited".
4. Konfirmasi swap di aplikasi. Kalau permintaan tanda tangan berupa kode yang tak terbaca atau tidak masuk akal — **jangan tanda tangani**.

## Langkah 4 — Kirim koin kembali ke akun Binance

1. Di aplikasi Binance, pindah ke **Exchange** → **Assets** → **Deposit**. Pilih koin (misalnya BNB).
2. Pilih **jaringan** (misalnya BNB Smart Chain). Salin alamat deposit. Beberapa koin juga butuh **memo/tag** — salin juga.
3. Pindah ke **Wallet** → **Send**. Pilih koin yang sama dan jaringan yang sama. Tempel alamat (dan memo kalau ada).
4. Kirim jumlah uji kecil dulu. Setelah masuk ke akun Binance, kirim sisanya.

Sisakan sedikit BNB atau SOL di wallet: setiap aksi on-chain, bahkan yang gagal, memakan biaya jaringan. Beberapa memecoin sama sekali tidak bisa didepositkan ke exchange (exchange tidak mencantumkannya) — untuk mencairkan, tukar dulu kembali ke BNB, SOL atau USDT di wallet.

## Langkah 5 — Putuskan koneksi dan bersih-bersih

1. Setelah selesai, putuskan koneksi situs (di pengaturan situs terhubung atau WalletConnect di wallet, atau tombol **Disconnect** di DEX).
2. Sesekali periksa approval token Anda dan revoke (batalkan) yang tidak diperlukan. Revoke memakan biaya kecil.
3. Di komputer bersama, keluar (log out) dari ekstensi.

Anda bisa memantau token yang dibeli di [portofolio Anda]({lang}/me/) dan melihat data memecoin langsung di [halaman memecoin]({lang}/memes/).

> **⚠️ Hati-hati**
> - **Situs atau "support" meminta kata sandi pemulihan, seed phrase atau "sinkronisasi wallet".** DEX asli atau karyawan Binance tidak pernah melakukannya. Tutup halamannya.
> - **Approval tanpa batas dan tanda tangan buta.** Approval atau tanda tangan berbahaya bisa membuat penipu menguras token itu nanti, tanpa konfirmasi lagi dari Anda.
> - **Jaringan salah, memo terlupa, atau alamat tempelan yang berubah.** Malware bisa mengganti alamat yang disalin. Bandingkan karakter pertama dan terakhir setiap kali, dan uji dengan jumlah kecil.

Pelajaran berikutnya: cara memeriksa memecoin sebelum membeli. Semua pelajaran ada di [halaman Belajar]({lang}/learn/).

## Sumber

- [Binance: What Is Binance Wallet Extension and How Does It Work?](https://www.binance.com/en/support/faq/ebfa9f504ec548968bf0c1ed591a3eaa)
- [Binance Academy: How to Use WalletConnect](https://www.binance.com/en/academy/articles/how-to-use-walletconnect)
- [Binance: How to Send and Receive Tokens on Binance Wallet](https://www.binance.com/en/support/faq/02f7eb872eca4a1ea44c775767170d13)
- [Binance.US: How to stay safe when using dApps on your Web3 Wallet](https://support.binance.us/en/articles/15090007-how-to-stay-safe-when-using-dapps-on-your-binance-us-wallet)

*Bukan nasihat investasi. Panduan ini menjelaskan cara kerja alat dan tidak merekomendasikan membeli token apa pun. Binance Wallet mungkin tidak tersedia di semua negara.*

---
title: Apa itu DEX dan apa bedanya dengan exchange kripto biasa?
description: Apa itu DEX? Panduan sederhana soal bursa terdesentralisasi: AMM, pool likuiditas, wallet, gas fee, serta kelebihan dan kekurangannya dibanding CEX.
date: 2026-11-16
category: guides
assets: eth, sol, uni
---
**Apa itu DEX?** DEX (decentralised exchange atau bursa terdesentralisasi) adalah kumpulan smart contract di blockchain yang memungkinkan Anda menukar satu token dengan token lain langsung dari wallet Anda sendiri. Tidak ada perusahaan yang memegang uang Anda, tidak ada akun, dan biasanya tidak ada verifikasi identitas. Uniswap di Ethereum, serta Raydium, Orca, dan Meteora di Solana, adalah contoh yang terkenal.

Exchange kripto biasa seperti Binance, Coinbase, atau Kraken adalah **CEX** (centralised exchange atau bursa terpusat): perusahaan yang menyimpan dana Anda, mempertemukan pembeli dan penjual di sistemnya sendiri, dan wajib mengikuti aturan keuangan.

## Cara kerja DEX

### Automated market maker (AMM)

Sebagian besar DEX tidak memakai order book berisi pembeli dan penjual. Sebagai gantinya, mereka memakai **automated market maker**, yaitu rumus yang menentukan harga.

Versi klasiknya, yang dipakai Uniswap v2, adalah aturan "constant product": sebuah pool berisi dua token, dan jumlah token A dikalikan jumlah token B harus tetap sama setelah setiap transaksi. Saat Anda membeli token A, Anda menambahkan token B ke pool dan mengambil token A, sehingga A makin langka di pool dan harganya naik.

Anda tidak perlu menghitungnya. Intinya: **makin besar pool, makin kecil transaksi Anda menggerakkan harga.**

### Pool likuiditas

Token di dalam pool berasal dari **penyedia likuiditas**, yaitu orang-orang yang menyetor pasangan token dan mendapat bagian dari biaya trading (sering 0,05–1% per swap). Risikonya, harga kedua token bisa bergerak menjauh satu sama lain, sehingga mereka bisa lebih rugi dibanding sekadar menyimpan tokennya ("impermanent loss").

Untuk token yang baru diluncurkan, biasanya pembuatnya yang menyiapkan pool pertama. Itulah kenapa kunci likuiditas penting: siapa pun yang mengendalikan pool bisa menariknya.

### Wallet Anda adalah akun Anda

Untuk memakai DEX, Anda menghubungkan wallet self-custody seperti MetaMask (Ethereum dan jaringan sejenis) atau Phantom (Solana). Setiap transaksi Anda tanda tangani sendiri. **Seed phrase** Anda adalah kunci utama: hilang, uangnya ikut hilang; dibagikan, orang lain yang mengambil uangnya.

### Gas dan biaya

Setiap transaksi di DEX membayar biaya jaringan, yang di Ethereum disebut **gas**. Di Ethereum, biayanya naik saat jaringan ramai; jaringan Layer-2 dan Solana biasanya jauh lebih murah. Biaya dasar Solana adalah 0,000005 SOL per tanda tangan. Selain gas, Anda membayar biaya pool, dan bisa terkena **slippage** serta **price impact** pada token kecil atau yang harganya bergerak cepat.

## DEX vs CEX: perbedaan utama

- **Siapa yang memegang dana:** di DEX, Anda sendiri (wallet Anda); di CEX, exchange-nya.
- **Akun dan verifikasi identitas:** DEX biasanya tidak perlu; CEX mewajibkan verifikasi identitas (KYC).
- **Pilihan token:** DEX menyediakan hampir semua token, termasuk yang baru lahir; CEX hanya mencatatkan token pilihan.
- **Beli pakai kartu atau transfer bank:** biasanya tidak bisa langsung di DEX; standar di CEX.
- **Biaya:** DEX: gas, biaya pool, dan slippage; CEX: biaya trading, spread, dan biaya penarikan.
- **Bantuan kalau ada masalah:** DEX tidak punya layanan bantuan; CEX punya customer service dan kadang skema perlindungan.
- **Risiko utama:** DEX: token penipuan, approval yang salah, dan kesalahan sendiri; CEX: peretasan, pembekuan akun, dan kebangkrutan.

## Kelebihan DEX

- **Self-custody.** Tidak ada yang bisa membekukan akun Anda atau menghilangkan uang Anda saat bangkrut.
- **Akses terbuka.** Siapa pun yang punya wallet bisa trading, dari hampir mana saja.
- **Token baru lebih dulu.** Token muncul di DEX jauh sebelum (atau tanpa pernah) listing di exchange.
- **Transparan.** Pool, transaksi, dan holder terlihat di blockchain.

## Kekurangan DEX

- **Anda adalah banknya.** Satu kesalahan (alamat salah, situs palsu, approval berbahaya) dan dana hilang selamanya.
- **Token penipuan.** Siapa saja bisa membuat token dan pool dalam hitungan menit. Sebagian besar token baru kehilangan hampir seluruh nilainya; lihat [checklist rug pull]({lang}/blog/how-to-spot-a-rug-pull/) kami.
- **Biaya tersembunyi.** Slippage dan price impact bisa lebih mahal daripada biaya yang terlihat.
- **Tidak ada jalur masuk yang mudah.** Biasanya Anda harus beli kripto dulu di CEX lalu mengirimnya ke wallet.
- **Risiko smart contract.** Bug atau peretasan pada kode DEX pernah menyebabkan kerugian besar.

## Mana yang sebaiknya dipakai pemula?

Banyak orang memakai keduanya: CEX berizin untuk menukar rupiah atau mata uang lokal ke kripto, dan DEX untuk token yang hanya tersedia on-chain. Untuk membeli aset besar seperti Bitcoin atau Ethereum secara rutin dan jangka panjang, CEX dengan biaya rendah biasanya lebih praktis; bandingkan pilihannya di [halaman exchange]({lang}/exchanges/) kami.

Kalau Anda ingin menjelajahi memecoin dan token on-chain lainnya, mulailah dengan jumlah sangat kecil, wallet terpisah, dan koin yang paling mapan di [halaman memecoin]({lang}/memes/) kami. Panduan langkah demi langkah kami, [cara beli memecoin di Solana]({lang}/blog/how-to-buy-memecoins-on-solana/), menunjukkan seluruh prosesnya, termasuk alat seperti [GMGN](/go/gmgn?from=blog&l=id).

## Istilah DEX yang sering dipakai

- **Swap**: menukar satu token dengan token lain.
- **Pair**: dua token dalam satu pool, misalnya SOL/USDC.
- **Slippage tolerance**: perubahan harga maksimum yang Anda terima.
- **Approve**: izin bagi kontrak untuk memindahkan token dari wallet Anda (terutama di jaringan bergaya Ethereum). Cabut approval lama yang sudah tidak Anda butuhkan.
- **Aggregator**: layanan yang membagi transaksi Anda ke beberapa DEX untuk harga lebih baik, seperti Jupiter di Solana atau 1inch di Ethereum.

## FAQ

### Apakah DEX lebih aman daripada CEX?

DEX menghilangkan risiko exchange menghilangkan atau membekukan dana Anda, tetapi menambah risiko kesalahan sendiri dan token penipuan. Keduanya tidak bebas risiko.

### Apakah perlu KTP atau identitas untuk memakai DEX?

Biasanya tidak, karena Anda bertransaksi dari wallet sendiri. Namun hukum dan pajak setempat tetap berlaku untuk Anda.

### Kenapa transaksi saya di DEX gagal?

Penyebab umumnya: koin asli jaringan tidak cukup untuk gas, slippage diatur terlalu rendah untuk harga yang bergerak cepat, atau token yang memblokir penjualan.

### Apakah transaksi di DEX kena pajak?

Di banyak negara, ya: swap dari satu token ke token lain bisa dihitung sebagai penjualan. Catat semua transaksi Anda.

## Sumber

- [Cara kerja Uniswap (dokumentasi Uniswap)](https://docs.uniswap.org/contracts/v2/concepts/protocol-overview/how-uniswap-works)
- [Gas dan biaya (ethereum.org)](https://ethereum.org/en/developers/docs/gas/)
- [Dokumentasi Solana: struktur biaya](https://solana.com/docs/core/fees/fee-structure)

*Bukan nasihat investasi. Panduan ini menjelaskan cara kerja DEX dan tidak merekomendasikan platform atau token apa pun.*

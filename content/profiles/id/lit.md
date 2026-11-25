---
title: Lighter (LIT) dijelaskan sederhana: futures perpetual tanpa biaya di zk-rollup Ethereum dan apa yang menggerakkan tokennya
description: Lighter dengan bahasa sederhana: bursa futures perpetual di zk-rollup Ethereum miliknya sendiri, tanpa biaya untuk trader ritel, token LIT dan risikonya.
date: 2026-11-25
kind: analysis
---
**Lighter** adalah bursa terdesentralisasi untuk futures perpetual — kontrak yang memungkinkan Anda bertaruh pada harga bitcoin, ether, dan aset lain dengan leverage. Bursa ini berjalan di zk-rollup miliknya sendiri di atas Ethereum, trader biasa tidak membayar biaya trading, dan setiap pencocokan order diperiksa dengan bukti zero-knowledge. Tokennya, **LIT**, diluncurkan pada 30 Desember 2025 dan hari ini bernilai {{mcap:lit}} ({{rank:lit}} di antara mata uang kripto).

> **Poin penting**
> - Ada 1 miliar LIT; 50% diberikan ke ekosistem, termasuk airdrop 25% untuk pengguna awal pada Desember 2025.
> - Rekor harganya {{ath:lit}} ({{athd:lit}}); hari ini harganya {{fromath:lit}} dari rekor itu.
> - Token tim (26%) dan investor (24%) dikunci selama satu tahun setelah peluncuran, lalu dibuka bertahap selama tiga tahun.
> - Bagi trader ritel, trading lewat situs dan aplikasi gratis; biaya dibayar trader profesional lewat API dan frekuensi tinggi.

## Cara kerjanya

Lighter adalah layer 2 di Ethereum. Transaksi terjadi di order book cepat milik Lighter sendiri, dan sirkuit zero-knowledge khusus membuktikan bahwa order dicocokkan secara adil berdasarkan harga dan waktu, serta likuidasi, pembayaran funding, dan pemeriksaan risiko mengikuti aturan. Dana pengguna disimpan di smart contract Ethereum, dan status jaringan baru bergerak maju setelah sebuah bukti diverifikasi di Ethereum. Jika operator macet atau menyensor pengguna, mereka bisa mengirim permintaan langsung ke Ethereum atau keluar lewat jalur darurat bernama "Desert Mode".

## Cara menghasilkan uang dan fungsi LIT

Model bisnis Lighter tidak biasa: yang trading lewat antarmuka tidak membayar apa pun, sementara arus lewat API dan trading frekuensi tinggi — market maker dan perusahaan trading — membayar biaya "premium". Tim mengatakan pendapatan bursa dan produk masa depan terlihat on-chain dan dipakai untuk pertumbuhan serta pembelian kembali (buyback) LIT, tergantung kondisi pasar; biaya dan buyback bisa dilacak di akun treasury pada block explorer Lighter.

LIT diterbitkan oleh perusahaan Lighter di AS. Pada Januari 2026 staking menjadi kegunaan besar pertamanya: untuk menyetor ke Lighter Liquidity Pool (LLP), yang memberi imbal hasil dan berfungsi sebagai dana asuransi saat likuidasi, Anda harus melakukan staking 1 LIT untuk setiap 10 USDC. Pemegang staking minimal 100 LIT tidak membayar biaya penarikan atau transfer, dan staking memberi diskon biaya premium. Tim juga berencana mengaitkan infrastruktur transaksi dan verifikasi keadilannya dengan staking LIT.

## Angka saat ini

- Harga hari ini: {{price:lit}}
- Rekor: {{ath:lit}} ({{athd:lit}}), {{fromath:lit}} dari rekor
- Nilai pasar: {{mcap:lit}} ({{rank:lit}} di antara mata uang kripto)
- Total pasokan: 1 miliar LIT (50% ekosistem, 26% tim, 24% investor)

## Kisahnya sejauh ini

Lighter didirikan pada 2022 oleh Vladimir Novakovski, yang masuk Harvard di usia 16 tahun dan mulai bekerja di Citadel di usia 18. Proyek ini lahir dari Lunchclub, aplikasi networking berbasis AI yang ia dirikan bersama pada 2017; sebagian besar tim itu pindah ke Lighter. Pada 2024 proyek ini mengumpulkan 21 juta dolar dalam putaran yang dipimpin Haun Ventures dan Craft Ventures. Setelah sekitar delapan bulan uji tertutup dengan sekitar 188.000 akun, mainnet publik dibuka pada Oktober 2025.

Pertumbuhannya cepat: pada pertengahan November 2025 volume mingguan mencapai puncak 74,9 miliar dolar, dan untuk November 2025 Lighter melaporkan 292,5 miliar dolar, di atas Aster dan Hyperliquid. Bulan itu juga Lighter mengumpulkan 68 juta dolar dalam putaran yang dipimpin Founders Fund dan Ribbit Capital, bersama Haun Ventures dan Robinhood, menurut laporan dengan valuasi sekitar 1,5 miliar dolar. Awal Desember 2025 trading spot ditambahkan.

LIT mulai diperdagangkan pada 30 Desember 2025; airdrop untuk pemegang poin dari dua musim pertama 2025 saat itu bernilai sekitar 675 juta dolar. Awal Januari 2026 akun treasury mulai mengumpulkan LIT, yang dibaca pasar sebagai buyback, dan pada 14 Januari 2026 diumumkan kewajiban staking untuk LLP. Setelah airdrop, banyak pemburu poin pergi: pada pertengahan Januari 2026 volume mingguan turun ke sekitar 25,3 miliar dolar, kira-kira sepertiga dari puncaknya, dan Hyperliquid kembali ke posisi pertama.

## Alternatif

Pesaing utamanya adalah [Hyperliquid]({lang}/hype/), yang berjalan di blockchain layer 1 miliknya sendiri, bukan di Ethereum, dan punya token HYPE. [Aster]({lang}/aster/) bersaing dengan Lighter memperebutkan posisi pertama berdasarkan volume pada akhir 2025, dan [dYdX]({lang}/dydx/) adalah salah satu bursa perpetual terdesentralisasi tertua. Bursa terpusat besar seperti Binance dan OKX masih menangani sebagian besar trading futures kripto.

## Risiko utama

- **Volume karena hadiah:** sebagian besar aktivitas 2025 berasal dari berburu poin sebelum airdrop; setelahnya, volume turun sekitar tiga kali lipat dalam beberapa minggu.
- **Pembukaan token:** separuh pasokan milik tim dan investor; setelah dikunci setahun, token itu dibuka selama tiga tahun, yang bisa menambah tekanan jual.
- **Persaingan:** Hyperliquid, Aster, dan bursa terpusat memperebutkan trader yang sama, dan trading tanpa biaya mudah ditiru.
- **Teknologi:** zk-rollup muda dengan order book dan sistem bukti sendiri bisa mengalami bug atau gangguan, meski ada jalur keluar lewat Ethereum.
- **Regulasi:** derivatif dengan leverage diatur ketat di banyak negara, dan aturan untuk bursa terdesentralisasi bisa berubah.
- **Fluktuasi besar:** LIT adalah token muda; penurunan tajam setelah peluncuran adalah bagian dari sejarahnya.

## Artinya jika Anda membeli secara rutin

LIT baru diperdagangkan kurang dari setahun, jadi belum ada riwayat panjang "10 dolar sehari" — hasil apa pun hanya mencakup periode singkat yang sangat bergejolak. Membeli jumlah tetap secara rutin menyebar harga masuk Anda dari waktu ke waktu alih-alih bertaruh pada satu momen, tetapi tidak menghilangkan risiko rugi, terutama untuk token muda dengan jadwal pembukaan token di depan. Jika membeli, banyak orang membatasi token seperti ini pada sebagian kecil tabungan yang sanggup mereka lihat turun tajam. Hasil masa lalu tidak menjamin hasil di masa depan.

*Bukan nasihat investasi.*

## Sumber

- [Lighter launches native token LIT, allocates half to ecosystem growth (The Block, 30 Desember 2025)](https://www.theblock.co/post/383940/lighter-native-token-lit)
- [Lighter introduces mandatory LIT staking for liquidity pool access (The Block, 14 Januari 2026)](https://www.theblock.co/post/385696/lighter-lit-staking)
- [Lighter opens public mainnet with Ethereum-settled zk perps (Blockworks)](https://blockworks.co/news/lighter-opens-public-mainnet)
- [DeFi founder who graduated Harvard at 18 raises $68 million for crypto trading protocol Lighter (Fortune, 11 November 2025)](https://fortune.com/2025/11/11/lighter-fundraise-founders-fund-ribbit-capital-haun-ventures-robinhood-vladimir-novakovski/)
- [Trading volume on Lighter plummets threefold after airdrop (ForkLog, 19 Januari 2026)](https://forklog.com/en/news/trading-volume-on-lighter-exchange-plummets-threefold-after-airdrop)
- [Lighter: harga, kapitalisasi pasar, dan rekor tertinggi (CoinGecko)](https://www.coingecko.com/en/coins/lighter)

---
title: Apa itu staking kripto dan apakah aman?
description: Apa itu staking kripto? Penjelasan sederhana: cara kerjanya, masa kunci, staking di exchange vs on-chain, dan risiko nyata yang perlu dicek sebelum staking.
date: 2026-11-16
category: guides
assets: eth, sol, ada, dot, atom
---
**Staking** berarti mengunci koin kripto untuk membantu sebuah blockchain berjalan — dan mendapat koin baru sebagai imbalannya. Staking sering disamakan dengan tabungan berbunga, tetapi cara kerjanya sangat berbeda dan punya risikonya sendiri.

Panduan ini menjelaskan cara kerja staking, apa arti "masa kunci" (lock-up), bedanya staking di exchange dan staking on-chain, serta apa saja yang bisa salah.

## Cara kerja staking

Banyak blockchain modern — Ethereum, Solana, Cardano, Polkadot, Cosmos dan lainnya — memakai sistem bernama **proof of stake**. Alih-alih memakai listrik untuk mengamankan jaringan (seperti mining Bitcoin), mereka mengandalkan **validator**: komputer yang memeriksa transaksi dan menambahkan blok baru.

Untuk menjadi validator, Anda harus mempertaruhkan koin sebagai jaminan bahwa Anda akan berlaku jujur. Langkah sederhananya:

1. Anda mengunci (stake) koin di jaringan, entah dengan menjalankan validator sendiri atau mendelegasikannya ke validator lain.
2. Validator mengonfirmasi transaksi dan membuat blok.
3. Jaringan membayar imbalan berupa koin baru, ditambah bagian dari biaya transaksi.
4. Jika validator curang atau sering offline, sebagian stake bisa dipotong. Ini disebut **slashing**.

Bitcoin sendiri tidak bisa di-stake dengan cara ini — Bitcoin memakai proof of work. Produk yang menawarkan "bunga Bitcoin" biasanya berupa pinjam-meminjam atau skema lain, bukan staking.

## Dari mana imbalan staking berasal

Imbalan staking bukan uang gratis. Sumber utamanya:

- **Koin baru** yang dicetak jaringan (inflasi suplai koin),
- **Biaya transaksi** yang dibayar pengguna.

Ini penting: jika jaringan mencetak koin baru, misalnya 5% per tahun, dan Anda mendapat 5%, sebagian besar Anda hanya mempertahankan porsi Anda di jaringan, bukan menjadi lebih kaya. Imbalan juga dibayar dalam koin itu sendiri — jika harganya turun, total nilai aset Anda tetap bisa anjlok.

Tingkat imbalan terus berubah mengikuti jumlah peserta staking dan aturan jaringan. Anggap persentase yang diiklankan sebagai potret sesaat, bukan janji.

## Masa kunci dan unbonding: kapan koin bisa ditarik kembali

Staking biasanya berarti koin Anda tidak bisa langsung dipakai. Tiap jaringan punya aturannya sendiri:

- **Ethereum** — penarikan bisa dilakukan sejak upgrade "Shapella" tahun 2023, tetapi keluar dari staking harus melalui antrean yang bisa memakan waktu berhari-hari hingga berminggu-minggu saat banyak orang keluar bersamaan.
- **Solana** — unstaking berlaku di akhir sebuah "epoch", biasanya sekitar dua hari.
- **Cosmos dan Polkadot** — masa "unbonding" beberapa minggu; selama itu koin tidak menghasilkan apa pun dan tidak bisa dijual.
- **Cardano** — koin tetap di wallet Anda dan sama sekali tidak dikunci.

Kenapa ini penting: jika pasar jatuh selama masa unbonding, Anda tidak bisa menjual. Selalu cek aturan terbaru untuk koin tersebut sebelum staking.

## Staking di exchange vs staking on-chain

Ada dua cara utama orang biasa melakukan staking.

### Staking di exchange (custodial)

Anda cukup menekan tombol "Stake" atau "Earn" di aplikasi exchange, dan exchange mengurus bagian teknisnya.

- ✅ Sangat mudah, jumlah kecil pun bisa, tanpa perlu menyiapkan wallet.
- ❌ Exchange memegang koin Anda. Jika exchange bangkrut, diretas atau membekukan penarikan, koin Anda ikut berisiko.
- ❌ Exchange mengambil sebagian imbalan sebagai biaya.
- ❌ Sebagian produk "earn" sebenarnya pinjam-meminjam, bukan staking — risikonya sangat berbeda.

Regulator mengawasi layanan seperti ini dengan ketat. Pada 2023 SEC AS menggugat Kraken terkait program staking-nya; Kraken membayar $30 juta dan menghentikan layanan itu untuk nasabah AS. Pada 2025 staf SEC menyatakan bahwa sebagian bentuk "protocol staking" langsung bukan transaksi efek. Di Indonesia, aset kripto diawasi OJK. Aturan berbeda di tiap negara dan terus berubah.

### Staking on-chain (non-custodial)

Anda menyimpan koin di wallet sendiri dan mendelegasikannya ke validator, atau menjalankan validator sendiri.

- ✅ Anda memegang kunci sendiri; tidak ada yang bisa membekukan akun Anda.
- ✅ Biasanya biayanya lebih rendah.
- ❌ Lebih teknis: salah alamat, phishing dan validator yang buruk menjadi tanggung jawab Anda.
- ❌ Menjalankan validator Ethereum sendiri butuh 32 ETH dan perangkat yang andal.

### Liquid staking

Pilihan di tengah: Anda melakukan staking lewat sebuah protokol dan menerima token yang mewakili koin yang di-stake (misalnya token "staked ETH"). Token itu bisa diperdagangkan sementara koin Anda tetap menghasilkan imbalan. Konsekuensinya ada tambahan **risiko smart contract** dan kemungkinan token diperdagangkan di bawah nilai koin yang menjaminnya.

## Risiko utama staking

Apakah staking aman? Risikonya lebih kecil dibanding banyak produk kripto "imbal hasil tinggi", tetapi tidak pernah bebas risiko:

1. **Risiko harga.** Ini yang terbesar. Imbalan beberapa persen tidak banyak artinya jika harga koin turun 50%. Lihat seberapa fluktuatif harganya di [halaman Ethereum]({lang}/eth/) atau [halaman Solana]({lang}/sol/).
2. **Risiko masa kunci.** Anda mungkin tidak bisa menjual saat harga anjlok.
3. **Risiko platform.** Exchange dan platform pinjaman bisa bangkrut. Saat Celsius runtuh pada 2022, pengguna program "earn"-nya kehilangan akses ke koin mereka.
4. **Slashing.** Validator yang berulah bisa kehilangan sebagian stake — di beberapa jaringan termasuk koin yang didelegasikan.
5. **Risiko smart contract** pada liquid staking dan DeFi.
6. **Pajak.** Di banyak negara imbalan staking dikenai pajak sebagai penghasilan saat diterima. Cek aturan setempat.
7. **Penipuan.** Situs staking palsu dan tawaran "dijamin 20% sebulan" sangat banyak. Baca panduan kami tentang [cara menghindari penipuan kripto]({lang}/blog/how-to-avoid-crypto-scams/).

## Daftar cek sebelum staking

- Hanya stake koin yang memang sudah Anda rencanakan untuk disimpan lama.
- Cek masa unbonding dan apakah Anda mungkin butuh uangnya lebih cepat.
- Pahami siapa yang memegang koin Anda — Anda sendiri atau platform.
- Bandingkan biaya: berapa bagian imbalan yang diambil platform?
- Hindari tawaran dengan imbal hasil tetap yang sangat tinggi — imbalan staking yang asli selalu berubah-ubah.
- Mulai dari jumlah kecil dan coba lakukan penarikan.

Staking tidak mengubah pertanyaan utamanya: apakah koin itu sendiri cocok dengan rencana jangka panjang Anda? Rencana beli rutin seperti DCA berfokus pada harga aset selama bertahun-tahun — coba hitung sendiri dengan [kalkulator DCA]({lang}/compare/). Berikut hasil $10 per hari di Ethereum selama 5 tahun — tanpa imbalan staking sama sekali: {{dca:eth:5}} dari {{dcainv:5}} yang diinvestasikan ({{dcaroi:eth:5}}).

{{card:eth}}
{{card:sol}}

## FAQ

### Apakah staking sama dengan mendapat bunga?

Tidak. Bunga berasal dari peminjam; imbalan staking berasal dari jaringan itu sendiri karena Anda membantu mengamankannya. Imbalan dibayar dalam koin, jadi nilainya ikut naik-turun bersama harganya.

### Bisakah rugi karena staking?

Bisa. Harga koin bisa turun, platform bisa bangkrut, dan dalam kasus langka slashing bisa memotong stake Anda. Imbalan tidak melindungi Anda dari penurunan harga.

### Bisakah Bitcoin di-stake?

Tidak secara bawaan — Bitcoin memakai proof of work. Tawaran "bunga Bitcoin" biasanya berupa pinjam-meminjam atau produk lain dengan risiko berbeda.

### Mana yang lebih baik, staking di exchange atau di wallet?

Staking di exchange lebih sederhana; staking di wallet memberi Anda kendali atas kunci sendiri. Pilihan yang tepat tergantung seberapa nyaman Anda mengelola wallet — lihat panduan kami tentang [hot wallet dan cold wallet]({lang}/blog/crypto-wallets-hot-vs-cold/).

## Sumber

- [ethereum.org — Staking Ethereum](https://ethereum.org/en/staking/)
- [ethereum.org — Penarikan staking](https://ethereum.org/en/staking/withdrawals/)
- [Solana — Staking](https://solana.com/staking)
- [SEC AS — Kraken menghentikan program staking dan membayar $30 juta (2023)](https://www.sec.gov/news/press-release/2023-25)
- [Skadden — SEC: sebagian aktivitas protocol staking bukan transaksi efek (2025)](https://www.skadden.com/insights/publications/2025/06/sec-certain-protocol-staking-activities-are-not-securities-transactions)

*Bukan saran investasi. Panduan ini menjelaskan cara kerja staking dan tidak merekomendasikan koin, platform atau validator apa pun.*

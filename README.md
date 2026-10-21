# Materi 6 — Deforestasi, Citra Satelit dan AI
## Studi kasus: Perbandingan tutupan lahan 2021 dan 2024

### Latar belakang
Citra satelit dapat digunakan untuk memantau perubahan tutupan lahan dari waktu ke waktu. Dalam proyek latihan ini, data tabel simulasi dipakai untuk menunjukkan alur membandingkan kelas lahan dan menghitung luas area yang berubah.

### Kaitan dengan materi
Materi sumber membahas citra Sentinel-1 dan Sentinel-2 serta deep learning/CNN untuk mengelompokkan penyebab langsung kehilangan tutupan hutan. Proyek ini hanya mengambil langkah awal yang bisa dikerjakan di tingkat semester 5: menganalisis tabel hasil klasifikasi yang sudah tersedia. Program ini tidak mengunduh citra satelit dan tidak melatih CNN.

### Fitur
- Membaca kelas tutupan lahan dua tahun.
- Menandai area dengan kelas yang berbeda.
- Menghitung total luas area berubah.
- Merangkum transisi Hutan ke Lahan Terbuka.
- Menyimpan rincian perubahan ke CSV.

### Struktur folder
```text
Materi_6_Deforestasi_dan_Citra_Satelit/
├── README.md
├── requirements.txt
├── src/
│   └── analisis_perubahan_lahan.py
├── data/
│   └── perubahan_tutupan_lahan.csv
└── outputs/
    └── (rincian_perubahan.csv dibuat saat program dijalankan)
```

### Cara menjalankan
```bash
python src/analisis_perubahan_lahan.py
```
Menggunakan pustaka bawaan Python.

### Batasan
Dataset merupakan data simulasi, bukan hasil klasifikasi Sentinel atau keluaran CNN. Perubahan tutupan lahan saja tidak cukup untuk memastikan penyebab deforestasi; hasil perlu diperiksa dengan data citra dan validasi lapangan.

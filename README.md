# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input

Nama: Anastasya Putri Kirana
NIM: 2225250041
Kelas: 3A

## Tujuan

Membangun program validasi dan klasifikasi dengan rantai if-elif-else.

## Cara Menjalankan

### Latihan 1
python latihan/01_predikat_nilai.py

### Latihan 2
python latihan/02_kategori_bilangan.py

### Latihan 3
python latihan/03_validasi_rentang.py

### Latihan 4
python latihan/04_validasi_tipe.py

### Latihan 5
python latihan/05_klasifikasi_sudut.py

### Praktik 1
python praktik/validasi_klasifikasi_nilai.py

## Tabel Keputusan

| Kategori | Syarat | Contoh Masukan |
|---|---|---|
| A | Nilai akhir >= 85 | 86 |
| B | Nilai akhir >= 70 | 73 |
| C | Nilai akhir >= 60 | 60 |
| D | Nilai akhir >= 50 | 53 |
| E | Selain kondisi di atas | 36 |

## Hasil Pengujian Praktik 1

| Ujian | Tugas | Kehadiran | Keluaran Diharapkan | Keluaran Aktual | Status |
|---:|---:|---:|---|---|---|
| 90 | 80 | 95 | Nilai akhir 86.00, Predikat A, Lulus | Nilai akhir 86.00, Predikat A, Lulus | Sesuai |
| 75 | 70 | 85 | Nilai akhir 73.00, Predikat B, Lulus | Nilai akhir 73.00, Predikat B, Lulus | Sesuai |
| 60 | 60 | 80 | Nilai akhir 60.00, Predikat C, Lulus | Nilai akhir 60.00, Predikat C, Lulus | Sesuai |
| 55 | 50 | 90 | Nilai akhir 53.00, Predikat D, Belum lulus | Nilai akhir 53.00, Predikat D, Belum lulus | Sesuai |
| 40 | 30 | 100 | Nilai akhir 36.00, Predikat E, Belum lulus | Nilai akhir 36.00, Predikat E, Belum lulus | Sesuai |
| 90 | 90 | 75 | Nilai akhir 90.00, Tidak memenuhi syarat kehadiran | Nilai akhir 90.00, Tidak memenuhi syarat kehadiran | Sesuai |
| 105 | 80 | 90 | Penolakan rentang nilai ujian | Penolakan rentang nilai ujian | Sesuai |
| 80 | -5 | 90 | Penolakan rentang nilai tugas | Penolakan rentang nilai tugas | Sesuai |
| 80 | 80 | abc | Penolakan tipe | Penolakan tipe | Sesuai |

## Refleksi

Salah satu hal yang perlu diperhatikan adalah Salah satu hal yang perlu diperhatikan adalah urutan validasi sebelum klasifikasi. Input harus diperiksa terlebih dahulu dari sisi tipe dan rentang agar data yang tidak valid tidak diproses. Penggunaan try-except ValueError membantu menangani input yang bukan angka, sedangkan if-elif-else digunakan untuk menentukan predikat sesuai rentang nilai.
# SIFT Image Matching Project

Tugas Akhir Pengolahan Citra Digital - Implementasi Algoritma SIFT.

## Deskripsi
Proyek ini melakukan pencocokan fitur (feature matching) antar dua citra menggunakan algoritma SIFT (Scale-Invariant Feature Transform).
Tujuannya adalah mendeteksi objek yang sama meskipun mengalami perubahan rotasi, skala, atau sudut pandang.

## Fitur
- Deteksi Keypoint & Descriptor SIFT.
- Pencocokan fitur dengan Brute-Force Matcher.
- Filter hasil matching menggunakan Lowe's Ratio Test.
- Visualisasi hasil matching.

## Cara Menjalankan
1. Install library: `pip install -r requirements.txt`
2. Jalankan: `python main.py`

## Teknologi
- Python 3.x
- OpenCV
- Matplotlib

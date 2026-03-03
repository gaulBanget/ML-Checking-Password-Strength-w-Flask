# Checking Password Strength using Machine Learning (Flask App)

Aplikasi Flask yang memanfaatkan model Machine Learning untuk menilai kekuatan kata sandi berdasarkan fitur karakter-level. Model menggunakan TF-IDF pada karakter dan Gradient Boosting Classifier.

## Dataset
- Sumber: Password Strength.csv
- Label kekuatan: 0 (Weak), 1 (Medium), 2 (Strong)
- Pembersihan: drop nilai kosong dan analisis distribusi label

## Feature Engineering
- TF-IDF vectorization pada level karakter untuk mengubah string password menjadi fitur numerik.

## Pelatihan & Evaluasi
- Bagi data menjadi train/test.
- Latih Gradient Boosting dan evaluasi dengan accuracy, precision, recall, F1.
- Artefak disimpan ke folder `models/`: `gb_model.pkl`, `tfidf_vectorizer.pkl`.

## Cara Pakai
1. `pip install -r requirements.txt`
2. `python train_model.py` (opsional untuk latih ulang)
3. `python app.py`
4. Buka `http://localhost:5000`

## Dependensi
- Flask, scikit-learn, pandas, numpy, matplotlib, seaborn, Werkzeug

## Catatan
- Analisis dilakukan lokal; kata sandi tidak disimpan atau dikirim keluar.

## Lisensi
Lihat berkas LICENSE.

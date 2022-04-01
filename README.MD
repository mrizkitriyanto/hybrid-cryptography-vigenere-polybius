# Hybrid Kriptografi
Referensi: https://ieeexplore.ieee.org/document/9199997

Konsep utama dari kriptografi ini adalah penggabungan antara dua algoritma yang berbeda yaitu Vigenere dan Polybius

## Vigenere
Vigenere Cipher adalah strategi untuk mengacak huruf [A sampai Z]. Ini menggunakan tipe dasar penggantian polialfabetik. Sebuah sandi polialfabetik dikenal sebagai sandi yang bergantung pada penggantian plainteks.

### Enkripsi
Enkripsi yang diproses akan menghasilkan pesan yang dikodekan. Teks biasa (P) dan kunci (K) ditambahkan ke modulus 26

>Ei = (Pi + Ki) mod 26

Contoh:
```
Plainteks: SECURITY
Kunci: LION
Cipherteks: DMQHCQHL
```

<br>

### Dekripsi

>Di = (Ei - Ki + 26) mod 26

Contoh:
```
Cipherteks: DMQHCQHL
Kunci: LION
Plainteks: SECURITY
```
<br>

## Polybius Square Cipher
Polybius Square Cipher ditampilkan sebagai gambar kotak 5x5 ditempati dengan huruf di dalam untuk enkripsi. Polybius Square adalah tabel yang memungkinkan seseorang untuk mengubah huruf menjadi angka.

### Enkripsi
Enkripsi, sebagai contoh, D ditempatkan pada baris 1 dan kolom 4, jadi menghasilkan keluaran yang dikodekan sebagai 14; O ditempatkan pada baris 3, kolom 3, ini adalah hasil keluaran yang dikodekan sebagai 34. Jadi, hasil pesan terenkripsi DOG adalah 14, 34, 23.

### Dekripsi
Dekripsi Polybius membutuhkan pengetahuan grid dan terdiri dari substitusi beberapa koordinat oleh huruf yang sesuai di grid. Contoh: 12 visualisasi untuk baris 1 dan kolom 2, sebagai hasilnya huruf B, 45 visualisasikan untuk baris ke-4 dan kolom ke-5 yang dihasilkan U dan lalu sama. Hasil pesan yang didekripsi adalah BUS.

## Penggabungan Algoritma
Hybrid Algorithm merupakan kombinasi dari Vigenere Cipher dan Polybius Square Cipher dalam proses enkripsinya. Awalnya cipherteks  akan dikerjakan dengan menggunakan cipher Vigenere. Kunci yang dipilih akan diproses sampai selesai, lalu selanjutnya cipherteks kemudian dirubah menjadi kunci untuk proses Polybius Square Cipher. Kuncinya digunakan untuk mengerjakan pesan yang merupakan plainteks untuk dibuat menjadi cipherteks terakhir. Proses ini akan berakhir menjadi yang cipherteks yang semakin sulit dipecahkan.

Dekripsi akan dilakukan oleh penerima dalam urutan terbalik untuk pengambilan pesan dari pengirim. Program akan disusun menggunakan perhitungan python coding dan teknik kriptanalisis yang berbeda akan dilakukan pada ciphertext.
### Contoh
```
Plaintext: SECURITY
KEY: LION
```

#### Enkripsi
```
Phase 1 (Vigenere Cipher)
STEP1: PLAINTEXT - SECURITY
STEP2: KEY - LION
STEP3: OUTPUT - DMQHCQHL

Phase 2 (Polybius Chiper)
STEP4: TEXT - DMQHCQHL
STEP5: OUTPUT - 4123143231143213
```
#### Dekripsi
```
FOR LOOP len(CIPHERTEXT):
    # Phase 1 (Polybius Cipher)
    STEP1: CIPHERTEXT - 41
    STEP2: OUTPUT - D

    # Phase 2 (Vigenere Chiper)
    STEP4: TEXT - D
    STEP5: KEY - LION
    STEP6: OUTPUT - S
```

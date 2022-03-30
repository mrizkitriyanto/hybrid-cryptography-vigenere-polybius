from application import *

if __name__ == "__main__":

    print("""
 _   _       _          _     _
| | | |_   _| |__  _ __(_) __| |
| |_| | | | | '_ \| '__| |/ _` |
|  _  | |_| | |_) | |  | | (_| |
|_| |_|\__, |_.__/|_|  |_|\__,_|
       |___/                  by Merry & Rizki
  ____                  _                              _
 / ___|_ __ _   _ _ __ | |_ ___   __ _ _ __ __ _ _ __ | |__  _   _
| |   | '__| | | | '_ \| __/ _ \ / _` | '__/ _` | '_ \| '_ \| | | |
| |___| |  | |_| | |_) | || (_) | (_| | | | (_| | |_) | | | | |_| |
 \____|_|   \__, | .__/ \__\___/ \__, |_|  \__,_| .__/|_| |_|\__, |
            |___/|_|             |___/          |_|          |___/

Referensi: https://ieeexplore.ieee.org/document/9199997
    """)

    print("""Pilih proses yang diinginkan \n
                1. Enkripsi
                2. Dekripsi
                3. Keluar
    """)
    choose = input("Ketikkan pilihan: ")

    if (choose=="1"):
        message = input("Masukkan pesan (KAPITAL dan TANPA SPASI): ")
        keyword = input("Masukkan kunci (KAPITAL dan TANPA SPASI): ")

        print("\n======== Pesan Terenkripsi ========")
        hybrid_encryption(message, keyword)
        print("\n")

    elif(choose=="2"):
        ciphertext = input("Masukkan ciphertext (TANPA SPASI): ")
        keyword = input("Masukkan kunci (KAPITAL dan TANPA SPASI): ")

        plaintext = hybrid_decryption(ciphertext, keyword)

        print("\n======== Pesan Terdekripsi ========")
        print(plaintext)
        print("\n")
    elif(choose=='3'):
        sys.exit("Terima Kasih \n")
    else:
        sys.exit("Ulangi Kembali, Masukkan Pilihan Dengan Benar!!\n")


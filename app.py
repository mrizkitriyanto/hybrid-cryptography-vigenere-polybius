import pyfiglet
import sys

from vigenere import *

if __name__ == "__main__":

    ascii_banner = pyfiglet.figlet_format("Hybrid Cryptography")
    print(ascii_banner)

    print("""Pilih proses yang diinginkan \n
                1. Enkripsi
                2. Dekripsi
                3. Keluar
    """)
    choose = input("Ketikkan pilihan: ")

    if (choose=="1"):
        message = input("Masukkan pesan (KAPITAL dan TANPA SPASI): ")
        keyword = input("Masukkan kunci (KAPITAL dan TANPA SPASI): ")
        key = vigenere_generate_key(keyword, len(message))
        e_vigenere = vigenere_encryption(message, key)
        print(e_vigenere)
    elif(choose=="2"):
        print("dekripsi")
    elif(choose=='3'):
        sys.exit("Terima Kasih \n")
    else:
        sys.exit("Ulangi Kembali, Masukkan Pilihan Dengan Benar!!\n")


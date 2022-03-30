import sys

from application.vigenere import *
from application.polybius import *

def hybrid_encryption(plain, keyword):
    key = vigenere_generate_key(keyword, len(plain))

    # Step 1 - Vigenere Encryption
    e_vigenere = vigenere_encryption(plain, key)
    print(key)
    print(e_vigenere)
    # Step 2 - Polybius Encryption
    e_polybius= polybius_encryption(e_vigenere)
    printer(e_polybius)

def hybrid_decryption(cipher, keyword):
    cipher = list(cipher)
    ciphertext_list = list()
    for i in range(0,len(cipher),2):
        ciphertext_list.append(cipher[i]+cipher[i+1])

    key = vigenere_generate_key(keyword, len(cipher))

    # Step 1 - Polybius Decryption
    d_polybius, index= polybius_decryption(ciphertext_list)
    print(ciphertext_list)
    print(index)
    print(d_polybius)
    printer_decryption(index)

    # Step 2 - Vigenere Decryption
    d_vigenere = vigenere_decryption(d_polybius, key)
    return d_vigenere
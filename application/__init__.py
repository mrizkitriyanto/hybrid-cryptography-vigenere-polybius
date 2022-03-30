import pyfiglet
import sys

from application.vigenere import *
from application.polybius import *

def hybrid_encryption(plain, keyword):
    key = vigenere_generate_key(keyword, len(plain))

    # Step 1 - Vigenere Encryption
    e_vigenere = vigenere_encryption(plain, key)
    print(e_vigenere)

    # Step 2 - Polybius Encryption
    e_polybius= polybius_encryption(e_vigenere, plain_table)
    printer(e_polybius)

def hybrid_decryption(cipher, keyword):
    key = vigenere_generate_key(keyword, len(cipher))
    d_vigenere = vigenere_decryption(cipher, key)
    return d_vigenere
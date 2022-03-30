import pyfiglet
import sys

from application.vigenere import *

def hybrid_encryption(plain, keyword):
    key = vigenere_generate_key(keyword, len(plain))
    e_vigenere = vigenere_encryption(plain, key)
    return e_vigenere

def hybrid_decryption(cipher, keyword):
    key = vigenere_generate_key(keyword, len(cipher))
    d_vigenere = vigenere_decryption(cipher, key)
    return d_vigenere
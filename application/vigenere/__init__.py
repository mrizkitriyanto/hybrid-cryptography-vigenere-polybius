def vigenere_generate_key(key, length):
    key = list(key)
    for i in range(length):
        key.append(key[i % len(key)])
    return("".join(key))

#Ei = (Pi + Ki) mod 26
def vigenere_encryption(string, key):
    encrypt_text = list()
    for i in range(len(string)):
        x = chr(((ord(string[i]) - ord('A')) + (ord(key[i]) - ord('A'))) % 26 + ord('A'))
        #ord(c) - ord('A') digunakan untuk mengconvert ke urutan alfabet
        #chr(integer + ord('A')) digunakan untuk mengembalikan nilainya ke unicode
        encrypt_text.append(x)
    return("".join(encrypt_text))

# Di = (Ei - Ki + 26) mod 26
def vigenere_decryption(cipher_text, key):
    plain_text = list()
    for i in range(len(cipher_text)):
        x = chr((((ord(cipher_text[i]) - ord('A')) - ord(key[i]) - ord('A'))+ 26 ) % 26 + ord('A'))
        plain_text.append(x)
    return("".join(plain_text))
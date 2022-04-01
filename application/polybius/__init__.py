from application.polybius.table import plain_table, cipher_table

def polybius_encryption(plaintext):
    cipher_table_index = list()
    cipher_text= list()
    for i in range(len(plaintext)):
        for j in range(len(plain_table)):
            if (plaintext[i] == " "):
                cipher_table_index.append(26)
                break
            # if (plaintext[i] == "J"):
            #     cipher_table_index.append(9)
            #     break
            if plain_table[j] == plaintext[i]:
                cipher_table_index.append(j)
    for k in range(len(cipher_table_index)):
        c = cipher_table[cipher_table_index[k]]
        cipher_text.append(c)
    return cipher_text

def polybius_decryption(cipher):
    plain_table_index = list()
    plain_text= list()
    for i in range(len(cipher)):
        for j in range(len(cipher_table)):
            if (cipher[i] == " "):
                plain_table_index.append(26)
                break
            if cipher_table[j] == cipher[i]:
                plain_table_index.append(j)
    for k in range(len(plain_table_index)):
        p = plain_table[plain_table_index[k]]
        plain_text.append(p)
    return plain_text,plain_table_index

def printer(l):
    return print("".join(l))

def printer_decryption(l):
    for k in range(len(l)):
        print(plain_table[l[k]], end="")
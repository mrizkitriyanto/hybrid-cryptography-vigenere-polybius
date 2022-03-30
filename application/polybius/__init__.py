from application.polybius.table import plain_table, cipher_table

def polybius_encryption(plaintext, plain_table):
    cipher_table_index = list()
    cipher_text= list()
    for i in range(len(plaintext)):
        for j in range(len(plain_table)):
            if (plaintext[i] == " "):
                cipher_table_index.append(26)
                break
            if plain_table[j] == plaintext[i]:
                cipher_table_index.append(j)
    for k in range(len(cipher_table_index)):
        c = cipher_table[cipher_table_index[k]]
        cipher_text.append(c)
    return cipher_text


def printer(l):
    return print("".join(l))
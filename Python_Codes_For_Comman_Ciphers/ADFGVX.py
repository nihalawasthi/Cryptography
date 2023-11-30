#Mannat
 
#3/17 German's ADFGVX Cipher
def generate_key_square(keywords):
    keyword = keywords.lower()                                            #creating the grid of adfgvx cipher
    letters = "abcdefghijklmnopqrstuvwxyz0123456789"
    words = sorted(set(keyword), key=keyword.index)
    remaining_words = [c for c in letters if c not in words]
    words += remaining_words
    key_square = [words[i:i+6] for i in range(0, len(words), 6)]
    return key_square


def adfgvx_encrypt(plaintext, keywords1, keywords2):                                    #encryption of the plaintext accoding to their position in adfgvx grid
    key_square = generate_key_square(keywords1)
    adfgvx = "ADFGVX"

    substitute= {}
    for i, row in enumerate(key_square):
        for j, char in enumerate(row):
            substitute[char] = adfgvx[i] + adfgvx[j]

    encrypted_mssg = ''
    for char in plaintext.lower():
        encrypted_mssg += substitute.get(char, '')

    return encrypted_mssg

def adfgvx_decrypt(cipher, keywords1, keywords2):                                         #decryption using the adfgvx cipher
    key_square = generate_key_square(keywords1)
    adfgvx = "ADFGVX"
    reverse_substitute = {}

    for i, row in enumerate(key_square):
        for j, char in enumerate(row):
            reverse_substitute[adfgvx[i] + adfgvx[j]] = char

    decrypted_mssg = ''
    for i in range(0, len(cipher), 2):
        pair = cipher[i:i+2]
        decrypted_mssg += reverse_substitute.get(pair, '')

    return decrypted_mssg

keywords1 = "CUTIE"                                                                         #ex of the current code with keywords cutie and biscuit
keywords2 = "BISCUIT"
mssg = input("Enter the Plaintext: ")

encrypted = adfgvx_encrypt(mssg, keywords1, keywords2)
print("Encrypted:", encrypted)
encrypted_text = input("enter encrypted text")
decrypted = adfgvx_decrypt(encrypted_text, keywords1, keywords2)
print("Decrypted:", decrypted)

def print_key_square(key_square):                                                                        #for printing the grid
    for row in key_square:
        print(" ".join(row))
        print("-" * 11)


#matrix ADFGVX

import numpy as np

def create_adfgvx_matrix(key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    key = "".join(sorted(set(key), key=key.index))
    key += alphabet
    key = "".join(sorted(set(key), key=key.index))
    matrix = np.array(list(key)).reshape(6, 6)
    return matrix

def adfgvx_encrypt(plaintext, key):
    adfgvx = "ADFGVX"
    matrix = create_adfgvx_matrix(key)
    encrypted = ""
    for char in plaintext:
        if char.upper() in matrix:
            position = np.argwhere(matrix == char.upper())[0]
            encrypted += adfgvx[position[0]] + adfgvx[position[1]]
    print(matrix)
    return encrypted

def adfgvx_decrypt(ciphertext, key):
    adfgvx = "ADFGVX"
    matrix = create_adfgvx_matrix(key)
    decrypted = ""
    for i in range(0, len(ciphertext), 2):
        row, col = adfgvx.index(ciphertext[i]), adfgvx.index(ciphertext[i + 1])
        decrypted += matrix[row, col]
    print(matrix)
    return decrypted

key = "KEYWORD"
plaintext = "HELLO"
ciphertext = adfgvx_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_text = adfgvx_decrypt(ciphertext, key)
print("Decrypted Text:", decrypted_text)

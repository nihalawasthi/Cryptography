#5 One Time Pad Cipher
import random

def gen_random(txt_length):
    key = ""
    for _ in range(txt_length):
        key += chr(random.randint(65, 90)) 
    return key

def encrypt(txt, key):
    etext = ""
    for i in range(len(txt)):
        txt_char = txt[i]
        key_char = key[i]
        echar = chr((ord(txt_char) + ord(key_char)) % 26 + 65)
        etext += echar
    return etext

def decrypt(etext, key):
    decrypted_text = ""
    for i in range(len(etext)):
        echar = etext[i]
        key_char = key[i]
        decrypted_char = chr((ord(echar) - ord(key_char)) % 26 + 65)
        decrypted_text += decrypted_char
    return decrypted_text

txt = input("enter text")
key = gen_random(len(txt))

etext = encrypt(txt, key)
print("Encrypted:", etext)

entext = input("enter encrpted text")
decrypted_text = decrypt(entext, key)
print("Decrypted:", decrypted_text)

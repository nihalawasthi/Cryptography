from base import *

def ecb_encrypt(key, text, padding):

    # Adding padding if required
    if padding == True:
        text = addPadding(text)

    # Encryption
    ciphertext = DES(text, key, padding, True)

    # Returning ciphertext
    return ciphertext

def ecb_decrypt(key, text, padding):
    plaintext = DES(text, key, padding, isEncrypt=False)

    if padding == True:
        return removePadding(plaintext)

    return plaintext

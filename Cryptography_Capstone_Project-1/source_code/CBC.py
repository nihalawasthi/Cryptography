from base import *
from ECB import *

def cbc_encrypt(key, text, iv, padding=True):
    ciphertext = ""
    previous_block = iv
    
    if padding:
        text = addPadding(text)

    plaintext_blocks = nSplit(text, 8)
    for block in plaintext_blocks:
        xored_block = xor(stringToBitArray(block), stringToBitArray(previous_block))
        encrypted_block = ecb_encrypt(key, bitArrayToString(xored_block), padding=False)
        ciphertext += encrypted_block
        previous_block = encrypted_block

    return ciphertext

def cbc_decrypt(key, text, iv, padding=True):
    plaintext = ""
    previous_block = iv
    ciphertext_blocks = nSplit(text, 8)
    
    for block in ciphertext_blocks:
        decrypted_block = DES(block, key, padding=False, isEncrypt=False)
        xored_block = xor(stringToBitArray(decrypted_block), stringToBitArray(previous_block))
        plaintext += bitArrayToString(xored_block)
        previous_block = block
        
    if padding:
        plaintext = removePadding(plaintext)
        
    return plaintext

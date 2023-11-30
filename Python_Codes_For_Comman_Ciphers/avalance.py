#27
import hashlib

num = 16
bsize = 64  

def fround(left, right, key):
    rh = hashlib.sha256(left + key).digest()
    nr = bytes(a ^ b for a, b in zip(right, rh))
    return right, nr

def fcipher(plain_text, key):
    blocksize = len(plain_text) // 2
    left, right = plain_text[:blocksize], plain_text[blocksize:]

    for _ in range(num):
        left, right = fround(left, right, key)

    ctext = right + left
    return ctext

def aveffect():
    plaintext = b'Hello1234' * 4  
    key = b'SecretKey' 

    print("Original Plaintext:", plaintext.hex())

    ciphertext = fcipher(plaintext, key)
    print("Ciphertext:", ciphertext.hex())

    modifiedplaintext = bytearray(plaintext)
    modifiedplaintext[15] ^= 1
    modifiedciphertext = fcipher(modifiedplaintext, key)
    print("Modified Ciphertext:", modifiedciphertext.hex())

aveffect()
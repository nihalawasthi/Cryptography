#26
from crypto.Cipher import AES
from crypto.Random import get_random_bytes

def pad(text):

    plength = 16 - (len(text) % 16)
    return text + bytes([plength] * plength)

def unpad(text):
    plength = text[-1]
    return text[:-plength]

def encrypt_aes(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext))
    return ciphertext

def mangle(input_data):
    
    random_byte = get_random_bytes(1)
    mangled_data = bytes([a ^ b for a, b in zip(input_data, random_byte)])
    return mangled_data


key = get_random_bytes(16)


plaintext = b'This is a secret message'


original_ciphertext = encrypt_aes(plaintext, key)


mangled_plaintext = mangle(plaintext)


mangled_ciphertext = encrypt_aes(mangled_plaintext, key)

print("Original Ciphertext:", original_ciphertext.hex())
print("Mangled Ciphertext:", mangled_ciphertext.hex())
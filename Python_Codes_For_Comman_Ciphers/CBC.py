#Mannat

#21.Cipher block chaining mode with avalanche effect
import random

def zero_pad_binary_string(binary_str, length):
    if len(binary_str) < length:
        return '0' * (length - len(binary_str)) + binary_str
    return binary_str

def xor_binary_strings(str1, str2):
    return ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(str1, str2))

def cbc_encrypt_with_avalanche(data, key, iv):
    data_bin = ''.join(format(ord(char), '08b') for char in data)
    key_bin = ''.join(format(ord(char), '08b') for char in key)
    iv_bin = ''.join(format(ord(char), '08b') for char in iv)

    data_bin = zero_pad_binary_string(data_bin, len(key_bin))
    iv_bin = zero_pad_binary_string(iv_bin, len(key_bin))

    ciphertext = ""

    previous_block = xor_binary_strings(data_bin[:len(key_bin)], iv_bin)

    for i in range(0, len(data_bin), len(key_bin)):
        
        current_block = data_bin[i:i+len(key_bin)]

        mixed_block = xor_binary_strings(current_block, previous_block)

        encrypted_block = xor_binary_strings(mixed_block, key_bin)

        ciphertext += encrypted_block
        previous_block = encrypted_block

    return ciphertext

data = input("Enter the mssg : ")
key = "SecretKey12345"
iv = "Initialization"
encrypted_data = cbc_encrypt_with_avalanche(data, key, iv)
print("Original Data:", data)
print("Encrypted Data with Avalanche Effect (CBC):", encrypted_data)




#19.DES with Avalanche Effect
def des_encrypt(data, key):
    
    max_len = max(len(data), len(key))
    data = data.ljust(max_len, '\x00')
    key = key.ljust(max_len, '\x00')

    data_bin = ''.join(format(ord(char), '08b') for char in data)
    key_bin = ''.join(format(ord(char), '08b') for char in key)

    encrypted_data_bin = ''.join(str(int(data_bit) ^ int(key_bit)) for data_bit, key_bit in zip(data_bin, key_bin))

    encrypted_data = ''.join(chr(int(encrypted_data_bin[i:i+8], 2)) for i in range(0, len(encrypted_data_bin), 8))

    return encrypted_data

data = input("Enter the mssg: ")
key = "BISCUIT6677"
encrypted_data = des_encrypt(data, key)
print("Original Data:", data)
print("Encrypted Data:", encrypted_data)

#20.Electronic codebook mode with Avalanche Effect

import random

def ecb_encrypt_with_avalanche(data, key):
    
    max_len = max(len(data), len(key))
    data = data.ljust(max_len, '\x00')
    key = key.ljust(max_len, '\x00')

    data_bin = ''.join(format(ord(char), '08b') for char in data)
    key_bin = ''.join(format(ord(char), '08b') for char in key)

    encrypted_data_bin = ""

    block_size = 64
    for i in range(0, len(data_bin), block_size):
        
        block = data_bin[i:i + block_size]

        random_bits = ''.join(str(random.randint(0, 1)) for _ in range(block_size))

        mixed_block = ''.join(str(int(data_bit) ^ int(random_bit)) for data_bit, random_bit in zip(block, random_bits))

        encrypted_block = ''.join(str(int(mixed_bit) ^ int(key_bit)) for mixed_bit, key_bit in zip(mixed_block, key_bin))

        encrypted_data_bin += encrypted_block

    encrypted_data = ''.join(chr(int(encrypted_data_bin[i:i + 8], 2)) for i in range(0, len(encrypted_data_bin), 8))

    return encrypted_data

data = input("Enter the mssg: ")
key = "CUTIE4567"
encrypted_data = ecb_encrypt_with_avalanche(data, key)
print("Original Data:", data)
print("Encrypted Data with Avalanche Effect (ECB):", encrypted_data)

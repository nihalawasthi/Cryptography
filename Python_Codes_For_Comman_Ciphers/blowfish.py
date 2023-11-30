def F(s, key):
    if isinstance(s, int):
        s0 = s
        s1 = 0
    else:
        s0, s1 = s
    return ((s0 + s1) % 0xFFFF) ^ key

def generate_subkeys(key):
    def round_function(p, sbox, i):
        return F(p, sbox[i % 4]) ^ sbox[(i + 1) % 4]

    key_schedule = [0] * 18
    p_box = [
        0x3F6A, 0x5A30, 0x982E, 0x0743,
        0xA382, 0x9F31, 0x2EFA, 0xC46C,
        0x2821, 0xD013, 0x466C, 0x0C6C,
        0xAC29, 0x7C50, 0x84D5, 0x4709,
        0x16D5, 0x79FB
    ]
    for i in range(18):
        key_schedule[i] = round_function(key, p_box, i)

    return key_schedule

def encrypt_block(block, subkeys):
    left = block[0]
    right = block[1]

    for i in range(16):
        left = left ^ subkeys[i]
        right = F([left, right], subkeys[i]) ^ right
        left, right = right, left

    left, right = right, left
    left = left ^ subkeys[16]
    right = right ^ subkeys[17]

    return [left, right]

def decrypt_block(block, subkeys):
    left = block[0]
    right = block[1]

    for i in range(17, 1, -1):
        left = left ^ subkeys[i]
        right = F([left, right], subkeys[i]) ^ right
        left, right = right, left

    left, right = right, left
    left = left ^ subkeys[1]
    right = right ^ subkeys[0]

    return [left, right]

def encrypt(data, key):
    subkeys = generate_subkeys(key)
    encrypted_data = []
    for i in range(0, len(data), 2):
        if i + 1 < len(data):
            block = [data[i], data[i + 1]]
            encrypted_block = encrypt_block(block, subkeys)
            encrypted_data.extend(encrypted_block)
    return encrypted_data

def decrypt(data, key):
    subkeys = generate_subkeys(key)
    decrypted_data = []
    for i in range(0, len(data), 2):
        if i + 1 < len(data):
            block = [data[i], data[i + 1]]
            decrypted_block = decrypt_block(block, subkeys)
            decrypted_data.extend(decrypted_block)
    return decrypted_data

def call(plaintext):
    hex_string = hex(plaintext)[2:]
    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string
    data = [int(hex_string[i:i + 2], 16) for i in range(0, len(hex_string), 2)]
    key = 0xAABB
    ciphertext = encrypt(data, key)
    c_data = int(''.join(hex(i)[2:].zfill(4) for i in ciphertext), 16)
    # Reduce output size to 16 bits
    c_data = c_data % 65536  # 65536 is 2^16
    return c_data

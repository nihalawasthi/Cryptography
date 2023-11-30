# S-boxes
S0 = [
    0x1, 0x0, 0xf, 0xe, 0xd, 0xc, 0xb, 0xa,
    0x9, 0x8, 0x7, 0x6, 0x5, 0x4, 0x3, 0x2
]

S1 = [
    0x4, 0x5, 0x6, 0x7, 0x0, 0x1, 0x2, 0x3,
    0xc, 0xd, 0xe, 0xf, 0x8, 0x9, 0xa, 0xb
]

# P-box
P = [
    1, 5, 9, 13,
    2, 6, 10, 14,
    3, 7, 11, 15,
    4, 8, 12, 16
]

# Hight cipher implementation
def hight(key, plaintext):
    # Initial setup
    k = [0] * 8
    for i in range(8):
        k[i] = (key >> (16 * (7 - i))) & 0xFFFF

    x = [(plaintext >> 32) & 0xFFFFFFFF, plaintext & 0xFFFFFFFF]

    # 32 rounds of Feistel network
    for i in range(32):
        t = x[1] ^ k[i % 8]
        t = (S0[(t >> 12) % 16] << 12) | S1[(t & 0xF) % 16]
        t = ((t << 17) | (t >> 15)) & 0xFFFFFFFF
        t ^= x[0] ^ P[i % 16]
        x[0], x[1] = x[1], t

    # Final swap
    ciphertext = (x[1] << 32) | x[0]
    return ciphertext


def call(plaintext):
    key = 0x1A2B3C4D5E6F7A8B
    plaintext_hex = int(plaintext, 16)
    ciphertext = hight(key, plaintext_hex)
    return ciphertext

# PRESENT S-Box
SBox = [
    0xC, 0x5, 0x6, 0xB, 0x9, 0x0, 0xA, 0xD,
    0x3, 0xE, 0xF, 0x8, 0x4, 0x7, 0x1, 0x2
]

# PRESENT round keys
RoundKeys = [
    0x0011, 0x3221, 0x5432, 0x7654, 0x9876,
    0xBA98, 0xDCBA, 0xFEDC, 0x1357, 0x2468
]

Permutation = [
    0, 16, 32, 48, 1, 17, 33, 49,
    2, 18, 34, 50, 3, 19, 35, 51,
    4, 20, 36, 52, 5, 21, 37, 53,
    6, 22, 38, 54, 7, 23, 39, 55,
    8, 24, 40, 56, 9, 25, 41, 57,
    10, 26, 42, 58, 11, 27, 43, 59,
    12, 28, 44, 64, 13, 29, 45, 61,
    14, 30, 46, 62, 15, 31, 47, 63
]

def generateRoundKeys(key):
    for i in range(10):
        RoundKeys[i] = key >> 16
        key = ((key & 0xFFFFFFF) << 61) | (key >> 3)
        key = (SBox[key >> 64] << 64) | (key & 0xFFFFFFFFFFFFFFF)

# Encryption
def encrypt(plainText, key):
    generateRoundKeys(key)
    state = plainText
    for i in range(31):
        state = (SBox[state >> 64] << 64) | (state & 0xFFFFFFFFFFFFFFF)
        state = state ^ RoundKeys[i % 10]
        state = (state >> 4) | (state << 64)
        state = sum(((state >> j) & 0x1) << Permutation[j] for j in range(64))
    state = (SBox[state >> 64] << 64) | (state & 0xFFFFFFFFFFFFFFF)
    state = state ^ RoundKeys[9]
    return state

# Decryption
def decrypt(cipherText, key):
    generateRoundKeys(key)
    state = cipherText
    for i in range(9, 0, -1):
        state = state ^ RoundKeys[i]
        state = sum(((state >> Permutation[j]) & 0x1) << j for j in range(64))
        state = (state << 4) | (state >> 64)
        state = (SBox[state >> 64] << 64) | (state & 0xFFFFFFFFFFFFFFF)
    state = state ^ RoundKeys[0]
    state = sum(((state >> Permutation[j]) & 0x1) << j for j in range(64))
    return state

def call(plaintext):
    key = 0x00000000000000000000
    ciphertext = encrypt(plaintext, key)
    return ciphertext

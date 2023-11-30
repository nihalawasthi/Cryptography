def rotate_left(val, r_bits, max_bits):
    return ((val << r_bits) & (2 ** max_bits - 1)) | ((val & (2 ** max_bits - 1)) >> (max_bits - r_bits))

def S(a, key):
    return (a ^ key) % (1 << 8)

def twine_decrypt(ciphertext, key):
    ciphertext_binary = ''.join(format(x, '08b') for x in ciphertext)

    while len(key) < 80:
        key += '0'  # Padding with zeros if the length is less than 80

    if len(key) != 80:
        raise ValueError("Key must be 80 bits long.")

    X = list(ciphertext_binary)
    for i in range(35, -1, -1):
        X = X[-1:] + X[:-1]
        key = key[:36 - i] + chr(S(ord(key[36 - i]), int(X[7], 2))) + key[37 - i:]

    P = bytearray(8)
    for j in range(8):
        for i in range(8):
            X = X[1:] + X[:1]
            P[i] = S(P[i], int(X[j], 2))

    return bytes(P)

def twine_encrypt(plaintext, key):
    if len(key) < 80:
        key = key.ljust(80, '0')  # Pad with zeros if the length is less than 80
    elif len(key) > 80:
        key = key[:80]  # Truncate to 80 bits if the length is greater than 80

    while len(plaintext) < 64:
        plaintext += '0'  # Padding with zeros if the length is less than 64

    X = list(plaintext)
    for i in range(36):
        X = X[1:] + X[:1]
        key = key[:i] + chr(S(ord(key[i]), ord(X[0]))) + key[i + 1:]

    C = bytearray(8)
    for j in range(8):
        for i in range(8):
            X = X[::-1]
            C[i] = S(C[i], ord(X[j]))

    return bytes(C)

def call(plaintext):
    key = "hellothisisasecretokaydontpeek"
    encrypted = twine_encrypt(plaintext, key)
    return encrypted

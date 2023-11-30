def pad_key(key):
    if len(key) < 16:
        key = key + 'A' * (16 - len(key))
    elif len(key) > 16:
        key = key[:16]
    return key

def Lblock_cipher(input_text, key):
    output_text = []
    if len(key) != 16:
        raise ValueError("Key must be 16 characters long.")
    else:
        Lblock_key = [[ord(key[4*i+j]) % 256 for j in range(4)] for i in range(4)]

    for i in range(0, len(input_text), 4):
        if i + 4 > len(input_text):
            pad_len = 4 - (len(input_text) - i)
            padded_input = input_text[i:] + 'A' * pad_len
        else:
            padded_input = input_text[i:i + 4]

        for j in range(4):
            xor_val = sum(ord(c) % 256 for c in padded_input[j::4]) % 256
            output_text.append(chr((ord(padded_input[j]) + Lblock_key[j % 4][j] + xor_val) % 256))

    return ''.join(output_text)

def call(plaintext, key):
    key = pad_key(key)
    encrypted = Lblock_cipher(plaintext, key)
    return encrypted


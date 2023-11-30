def rotate_left(val, r_bits, max_bits=16):
    return ((val << r_bits) & (2 ** max_bits - 1)) | ((val & (2 ** max_bits - 1)) >> (max_bits - r_bits))

def add_padding(data, block_size):
    padding_len = block_size - len(data) % block_size
    padded_data = data + '0' * padding_len
    return padded_data


def encrypt(plain_text, key):
    if len(key) != 16:
        raise ValueError("Key must be 16 bits long")

    if len(plain_text) > 64:
        raise ValueError("Input must be 64 bits long")

    # Padding the plain text to 64 bits
    plain_text_padded = plain_text.zfill(64)

    # Dividing the plain text into 4 chunks of 16 bits each
    plain_text_chunks = [plain_text_padded[i:i + 16] for i in range(0, len(plain_text_padded), 16)]

    round_keys = [int(key[i*2:(i+1)*2], 2) for i in range(8)]

    encrypted_chunks = []
    for chunk in plain_text_chunks:
        plain_text_int = int(chunk, 2)
        for i in range(32):
            plain_text_int = (plain_text_int + round_keys[i % 8]) & 0xFFFF
            plain_text_int = rotate_left(plain_text_int, 1, 16)
        encrypted_chunks.append(format(plain_text_int, '016b'))

    return ''.join(encrypted_chunks)
# Example Usage
def call(plaintext):
    block_size = 64  # Set the block size as required
    padded_plaintext = add_padding(plaintext, block_size)
    key = "1100110011001100"
    cipher_text = encrypt(padded_plaintext, key)  # Passing the binary plaintext
    return cipher_text
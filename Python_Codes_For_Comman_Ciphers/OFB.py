#22

from crypto.Cipher import AES
from crypto.Random import get_random_bytes

# Function for encrypting the Plain Text by using OFB Mode of AES.
def outputFeedBackModeOfAESEncrypt(plain_text, key, initial_vector=None):
    if initial_vector is None:
        initial_vector = get_random_bytes(16)

    position = 0
    finalCipherText = []
    originalInitialVector = initial_vector
    cipherT = AES.new(key, AES.MODE_ECB)

    if len(plain_text) % 16 != 0:
        plain_text += b"1"

    while len(plain_text) % 16 != 0:
        plain_text += b"0"

    while position + 16 <= len(plain_text):
        forXor = cipherT.encrypt(initial_vector)
        nextPosition = position + 16
        toEnc = plain_text[position:nextPosition]
        cipher_text = bytes([forXor[i] ^ toEnc[i] for i in range(16)])
        finalCipherText.append(cipher_text)
        position += 16
        initial_vector = forXor

    return originalInitialVector, finalCipherText


# Function for Decrypting the cipher text.
def outputFeedBackModeOfAESDecrypt(finalCipherText, key, initial_vector):
    plain_text = b""
    cipherT = AES.new(key, AES.MODE_ECB)
    for chunk in finalCipherText:
        forXor = cipherT.encrypt(initial_vector)
        plain_text += bytes([forXor[i] ^ chunk[i] for i in range(15)])
        initial_vector = forXor

    while plain_text[-1] == 48:
        plain_text = plain_text[0:-1]

    if plain_text[-1] == 49:
        plain_text = plain_text[0:-1]

    return plain_text


plain_text_input = input("Enter the plain text: ")
key_input = input("Enter the encryption key: ")

plain_text = plain_text_input.encode('utf-8')
key = key_input.encode('utf-8')

    # Pass Plaintext and get the ciphertext
initial_vector, result = outputFeedBackModeOfAESEncrypt(plain_text, key)
print("Initial Vector:", initial_vector)
print("Cipher Text:", result)

    # Pass the Cipher Text and get the Plain Text
plain = outputFeedBackModeOfAESDecrypt(result, key, initial_vector)
print("Decrypted Plain Text:", plain.decode('utf-8'))
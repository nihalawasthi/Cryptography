#29. Affine Cipher with encryption and decryption

def mod_inverse(a, m):
    
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt(plaintext, key):
   
    a, b = key
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
            elif char.isupper():
                encrypted_char = chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

def decrypt(ciphertext, key):
   
    a, b = key
    decrypted_text = ""
    a_inv = mod_inverse(a, 26)
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr(((a_inv * (ord(char) - ord('a') - b)) % 26) + ord('a'))
            elif char.isupper():
                decrypted_char = chr(((a_inv * (ord(char) - ord('A') - b)) % 26) + ord('A'))
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text

key = (5, 7)
plaintext = input('enter Plain text')
encrypted_text = encrypt(plaintext, key)

print("Plaintext: ", plaintext)
print("Encrypted: ", encrypted_text)

Encrypted_Text = input('enter encrypted text')
decrypted_text = decrypt(encrypted_text, key)

print("Decrypted: ", decrypted_text)
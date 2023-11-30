#7 Row Transposition cipher
def encrypt(mssg, key):
    mssg = mssg.replace(" ", "").lower()
    num_columns = len(key)
    num_rows = -(-len(mssg) // num_columns)

    mssg += "X" * (num_rows * num_columns - len(mssg))

                                                                                 # Create the matrix
    matrix = [[0] * num_columns for _ in range(num_rows)]
    for i in range(num_rows):
        for j in range(num_columns):
            matrix[i][j] = mssg[i * num_columns + j]

                                                                                                 # Sorting the matrix rows based on the key
    sorted_matrix = [list(row) for _, row in sorted(zip(key, matrix))]

                                                                                                                # Constructionof  the ciphertext
    cipher = ""
    for j in range(num_columns):
        for i in range(num_rows):
            cipher += sorted_matrix[i][j]

    return cipher

def decrypt(cipher, key):
    num_columns = len(key)
    num_rows = -(-len(cipher) // num_columns)

    matrix = [[0] * num_columns for _ in range(num_rows)]
    index = 0
    for j in range(num_columns):
        for i in range(num_rows):
            matrix[i][j] = cipher[index]
            index += 1

    sorted_matrix = [list(row) for _, row in sorted(zip(key, matrix))]

                                                                                                                     # Construction of the plaintext
    plaintext = ""
    for i in range(num_rows):
        for j in range(num_columns):
            plaintext += sorted_matrix[i][j]

    return plaintext

key = "2025"
mssg = input("Enter the mssg: ")
cipher = encrypt(mssg, key)
print("Cipher:", cipher)

decrypted_mssg = decrypt(cipher, key)
print("Decrypted mssg:", decrypted_mssg)


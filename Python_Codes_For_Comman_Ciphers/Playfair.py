#6 Playfair Cipher Encryption

def generate_key_square(keyword):
    
    keyword = keyword.replace("J", "I")
    keyword = "".join(dict.fromkeys(keyword))
    
  
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_square = list(keyword.upper())
    for letter in alphabet:
        if letter not in key_square:
            key_square.append(letter)
    
    return key_square

def find_position(key_square, char):
    pos = key_square.index(char)
    row = pos // 5
    col = pos % 5
    return row, col

def encrypt(text, key_square):
    text = text.replace("J", "I") 
    text = text.upper().replace(" ", "")
    
    ciphertext = ""
    i = 0
    while i < len(text):
        char1 = text[i]
        char2 = text[i + 1] if i + 1 < len(text) else "X"  # Add 'X' for odd-length pairs
        
        row1, col1 = find_position(key_square, char1)
        row2, col2 = find_position(key_square, char2)
        
        if row1 == row2:
            ciphertext += key_square[row1 * 5 + (col1 + 1) % 5] + key_square[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_square[((row1 + 1) % 5) * 5 + col1] + key_square[((row2 + 1) % 5) * 5 + col2]
        else:
            ciphertext += key_square[row1 * 5 + col2] + key_square[row2 * 5 + col1]
        
        i += 2
    
    return ciphertext


keyword = "KEYWORD"
text = print("enter plain text")
key_square = generate_key_square(keyword)

etext = encrypt(text, key_square)
print("Encrypted:", etext)
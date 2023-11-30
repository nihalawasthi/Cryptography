#8 Vigenère Cipher Encryption

def generate_key(txt, keyword):
    key = keyword
    key_length = len(keyword)
    txt_length = len(txt)
    
  
    while len(key) < txt_length:
        key += keyword
    
    return key[:txt_length]

def encrypt(txt, keyword):
    txt = txt.upper().replace(" ", "")
    keyword = keyword.upper().replace(" ", "")
    
    key = generate_key(txt, keyword)
    etext = ""
    
    for i in range(len(txt)):
        char = txt[i]
        shift = ord(key[i]) - ord('A')
        echar = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        etext +=echar
    
    return etext


keyword = "KEY"
text = input("enter plain text")
etext = encrypt(text, keyword)
print("Encrypted:", etext)


#9 Vigenère Cipher Decryption

def decrypt(etext, keyword):
    etext = etext.upper().replace(" ", "")
    keyword = keyword.upper().replace(" ", "")
    
    key = generate_key(etext, keyword)
    decrypted_text = ""
    
    for i in range(len(etext)):
        char = etext[i]
        shift = ord(key[i]) - ord('A')
        decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        decrypted_text += decrypted_char
    
    return decrypted_text


keyword = "KEY"
etext = "RIJVSUYVJN"
decrypted_text = decrypt(etext, keyword)
print("Decrypted:", decrypted_text)
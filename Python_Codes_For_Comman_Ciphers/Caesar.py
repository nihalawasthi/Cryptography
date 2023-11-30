#2 Caesar Cipher

def cc_encrypt(text, shift):
    etext = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                etext += chr((ord(char) - ord('A' ) + shift) % 26 + ord('A'))
            else:
                etext += chr((ord(char) - ord('a' ) + shift) % 26 + ord('a'))
        else:
            etext += char
    return etext

def cc_decrypt(etext, shift):
    decrypted_text = ""
    for char in etext:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A' ) - shift) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - ord('a' ) - shift) % 26 + ord('a'))
        else:
            decrypted_text += char
    return decrypted_text


text = input("enter text")
shift = 3
etext = cc_encrypt(text, shift)
print("Encrypted:", etext)

entext = input("enter encrypted text")
decrypted_text = cc_decrypt(entext, shift)
print("Decrypted:", decrypted_text)

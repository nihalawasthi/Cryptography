# Implement various modes of operation for DES. Conduct a comprehensive benchmark analysis in terms of security, speed, and resource utilization in both software and hardware environments
from base import *
from ECB import *
from CBC import *

def main():
    mode = input("Enter the mode of operation (ECB, CBC): ")
    action = input("Enter 'E' for encryption or 'D' for decryption: ")
    key = input("Enter a key of 8 length (64-bits) (characters or numbers only) : ")
    if len(key) != 8:
        print("Invalid Key. Key should be of 8 length (8 bytes).")
        return
    
    if action == 'E':
        plaintext = input("Enter the message to be encrypted : ")
        isPaddingRequired = (len(plaintext) % 8 != 0)
        if mode == 'ECB':
            print(ecb_encrypt(key, plaintext, isPaddingRequired))
        elif mode == 'CBC':
            iv = input("enter IV: ") 
            print(cbc_encrypt(key, plaintext, iv, padding=True))
        else:
            print("Invalid mode!")
    elif action == 'D':
        ciphertext = input("Enter the ciphertext: ")
        isPaddingRequired = (len(ciphertext) % 8 != 0)
        if mode == 'ECB':
            print(ecb_decrypt(key, ciphertext, isPaddingRequired))
        elif mode == 'CBC':
            iv = input("enter IV: ")
            print(cbc_decrypt(key, ciphertext, iv, padding=True))
        else:
            print("Invalid mode!")
    else:
        print("Invalid action!")

if __name__ == "__main__":
    main()

#23

from Crypto.Cipher import DES3
from hashlib import md5

#to select the opeation for encryption/decryption
while True:
    print('Chose opearation to be done:\n\t1-Encryption\n\t2-Decryption')
    operation = input("Your Choice: ")
    if operation not in ['1' , '2']:
        break

    #takes the file/image path for opration
    file_path = input('File Path: ')

    #the desired key from the user is taken as input for performing Triple DES algorithm
    key = input('TDES Key: ')


    #encode given key to 16 byte ascii key with md5 operation
    key_hash = md5(key.encode('ascii')).digest()

    #adjust key parity of generated Hash key for Final Triple DES key
    tdes_key = DES3.adjust_key_parity(key_hash)

    #Cipher with integration of Triple DES key, MODE_EAX for confidentiality and Aunthentication
    #nonce for generating random/pseudo random number which is used for authentication protocol
    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce = b'0')

    #opens and reads file from given input
    with open(file_path, 'rb') as input_file:
        file_bytes = input_file.read()


        if operation == '1':
            #performs encryption operation
            new_file_bytes = cipher.encrypt(file_bytes)
        
        else:
            #performs decryption operation
            new_file_bytes = cipher.decrypt(file_bytes)

    
    #write updated values in file from given path
    with open(file_path, 'wb') as output_file:
        output_file.write(new_file_bytes)
        print('Operation Done!')
        break
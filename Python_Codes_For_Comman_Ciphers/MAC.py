def plaintocipher(plain, key):
    cipher=''
    key=int(key)
    for i in plain:
        j=ord(i)
        if i.islower():
            k=(j+key-97)%26+97
        else:
            k=(j+key-65)%26+65
        l=chr(k)
        cipher+=l
    return cipher

def sender(mess, k):
    cipher_t=plaintocipher(mess, k)
    message=mess+'xx'+cipher_t
    return message

def receiver(mess, k):
    for i in range(len(mess)-2):
        if mess[i] == 'x' and mess[i+1] == 'x':
            original_cipher=mess[(i+2):]
            original_message=mess[:i]
            calculated_cipher=plaintocipher(original_message, k)
            print('\nOriginal_cipher: ',original_cipher )
            print('\ncalculated_cipher: ',calculated_cipher )
            print('\n')
            if calculated_cipher==original_cipher:
                return True
            else:
                return False
            

plain_text=input('Enter the plain text: ')
key=input('Enter the key: ')
key=int(key)

to_reciever=sender(plain_text, key)
print(f'\nText received from sender side: ', to_reciever)

print(receiver(to_reciever, key))

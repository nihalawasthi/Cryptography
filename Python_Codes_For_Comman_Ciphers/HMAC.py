from Crypto.Hash import HMAC,SHA1

def make_digest(message, key):
  key = bytes(key, 'UTF-8')
  message = bytes(message, 'UTF-8')
  h=HMAC.new(key,digestmod=SHA1)
  # to create the digest
  h.update(message)
  # create signature using digest
  print(h.hexdigest()) 

# main function
message=input("Enter the message(used in SHA1): ")
key=input("Enter the key(used in MAC): ")   
make_digest(message,key)

print()

# This is code for SHA-1 Algorithm:
import hashlib
s=input("Enter the message to encrypt: ")
result=hashlib.sha1(s.encode())
print("The output from SHA1: ",result)
print("The hexa decimal output from SHA1: ",result.hexdigest()) 

import hashlib
from cryptography.fernet import Fernet

# Define a secret key for the Fernet encryption
key = Fernet.generate_key()

# Define plaintext message
message = b'Hello, this is a secret message.'

# Create a combined hash using SHA-256
sha256_hash = hashlib.sha256()
sha256_hash.update(message)
hash_value = sha256_hash.digest()

# Encrypt the hash value using Fernet
cipher_suite = Fernet(key)
encrypted_hash = cipher_suite.encrypt(hash_value)

# Print the results
print(f"Original message: {message.decode('utf-8')}")
print(f"Combined Hash: {hash_value}")
print(f"Encrypted Hash: {encrypted_hash}")

# Decrypt the hash value using Fernet
decrypted_hash = cipher_suite.decrypt(encrypted_hash)

# Verify the integrity of the message
if hash_value == decrypted_hash:
    print("Integrity verified: The message is authentic.")
else:
    print("Integrity verification failed: The message might have been tampered with.")

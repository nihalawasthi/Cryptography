#Omika

import hashlib

def repeated_hash(input_string, num_iterations, hash_algorithm='sha256'):
    hashed_value = input_string.encode()
    
    for _ in range(num_iterations):
        hasher = hashlib.new(hash_algorithm)
        hasher.update(hashed_value)
        hashed_value = hasher.digest()

    return hashed_value.hex()

input_string = "Hello, World!"
num_iterations = 5
hash_algorithm = 'sha256'

result = repeated_hash(input_string, num_iterations, hash_algorithm)
print(f"Repeated Hash ({num_iterations} iterations): {result}")
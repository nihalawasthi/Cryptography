import hashlib

data_sequence = ["Step 1", "Step 2", "Step 3"]

# Initialize the hash object
sha256_hash = hashlib.sha256()

# Hash each step in sequence
for step in data_sequence:
    sha256_hash.update(step.encode())

# Get the final hash
final_hash = sha256_hash.hexdigest()
print("Sequential Hash:", final_hash)
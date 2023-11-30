import hashlib

data_piece1 = "Data 1"
data_piece2 = "Data 2"
data_piece3 = "Data 3"

# Hash each data piece independently
hash1 = hashlib.sha256(data_piece1.encode()).hexdigest()
hash2 = hashlib.sha256(data_piece2.encode()).hexdigest()
hash3 = hashlib.sha256(data_piece3.encode()).hexdigest()

# Print the independent hashes
print("Hash of Data 1:", hash1)
print("Hash of Data 2:", hash2)
print("Hash of Data 3:", hash3)
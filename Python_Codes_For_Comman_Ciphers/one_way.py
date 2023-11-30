#Nihal

#34 one way hashing

def custom_hash(input_string):
    # Starting with an initial hash value
    hash_value = 0

    # Adding the ASCII values of each character in the string to the hash value
    for char in input_string:
        hash_value += ord(char)

    # Returning the final hash value
    return hash_value

# Example usage
input_string = input('input string')
hashed_value = custom_hash(input_string)
print(f"The hash of '{input_string}' is: {hashed_value}")

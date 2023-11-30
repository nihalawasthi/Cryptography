#30 Diffie-Hellman Key Exchange implementation

def power(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

# Compute public keys for Alice and Bob

p = int(input("enter p: "))
g = int(input("enter g: "))

# Alice's private key
Alice = int(input("enter Alice's private key: "))
# Bob's private key
Bob = int(input("enter Bob's private key: "))
A = power(g, Alice, p)
B = power(g, Bob, p)

# Compute the shared secret key
s_A = power(B, Alice, p)
s_B = power(A, Bob, p)

# Print the results
print("Publicly Shared Variables:")
print("Prime Modulus, p:", p)
print("Primitive Root, g:", g)
print("\nPrivate Keys:")
print("Alice's private key:", Alice)
print("Bob's private key, b:", Bob)
print("\nComputed Public Keys:")
print("Alice's public key, A:", A)
print("Bob's public key, B:", B)
print("\nComputed Shared Secret Keys:")
print("Shared secret key for Alice, s_A:", s_A)
print("Shared secret key for Bob, s_B:", s_B)
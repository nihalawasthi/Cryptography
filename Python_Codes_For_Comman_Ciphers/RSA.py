import random
import math

# A set will be the collection of prime numbers,
# where we can select random primes p and q
prime = set()

public_key = None
private_key = None
n = None

# We will run the function only once to fill the set of
# prime numbers
def primefiller():
	# Method used to fill the primes set is Sieve of
	# Eratosthenes (a method to collect prime numbers)
	seive = [True] * 250
	seive[0] = False
	seive[1] = False
	for i in range(2, 250):
		for j in range(i * 2, 250, i):
			seive[j] = False

	# Filling the prime numbers
	for i in range(len(seive)):
		if seive[i]:
			prime.add(i)


# Picking a random prime number and erasing that prime
# number from list because p!=q
def pickrandomprime():
	global prime
	k = random.randint(0, len(prime) - 1)
	it = iter(prime)
	for _ in range(k):
		next(it)

	ret = next(it)
	prime.remove(ret)
	return ret


def setkeys():
	global public_key, private_key, n
	prime1 = pickrandomprime() # First prime number
	prime2 = pickrandomprime() # Second prime number

	n = prime1 * prime2
	fi = (prime1 - 1) * (prime2 - 1)

	e = 2
	while True:
		if math.gcd(e, fi) == 1:
			break
		e += 1

	# d = (k*Φ(n) + 1) / e for some integer k
	public_key = e

	d = 2
	while True:
		if (d * e) % fi == 1:
			break
		d += 1

	private_key = d


# To encrypt the given number
def encrypt(message,public_key, n):
    e = public_key
    encrypted_text = 1
    encoded = []

    for letter in message:
        encrypted_text = 1
        encrypted_text = pow(ord(letter), e, n)
        encoded.append(encrypted_text)
        
    encoded = ''.join(str(p) for p in encoded)
    
    return encoded


# To decrypt the given number
def decrypt(encoded):
    global private_key, n
    d = private_key
    decrypted_text = ''
    
    # Convert the string back to a list of numbers
    encoded_list = [int(encoded[i:i+4]) for i in range(0, len(encoded), 4)]

    # Decrypting and decoding each number
    for num in encoded_list:
        decrypted_text += chr(pow(num, d, n))  # RSA decryption
    
    return decrypted_text

primefiller()
setkeys()
message ='0011011000110100001101110011001000110000'
coded = encrypt(message,public_key, n)

print("Initial message:")
print(message)
print("\n\nThe encoded message(encrypted by public key)\n")
print(coded)
print("\n\nThe decoded message(decrypted by public key)\n")
print(decrypt(coded))
	

#p = int(input("Enter prime p: "))
#q = int(input("Enter prime q (!=p): "))



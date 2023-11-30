from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

def generate_ecc_key_pair():
    private_key = ec.generate_private_key(
        ec.SECP256R1(),  # Elliptic Curve choice (SECP256R1 is also known as NIST P-256)
        default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key, message):
    signature = private_key.sign(
        message.encode('utf-8'),
        ec.ECDSA(hashes.SHA256())
    )
    return signature

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message.encode('utf-8'),
            ec.ECDSA(hashes.SHA256())
        )
        return True
    except Exception as e:
        print(f"Signature verification failed: {e}")
        return False


private_key, public_key = generate_ecc_key_pair()


message = input("Enter the message to sign: ")


signature = sign_message(private_key, message)

print(f"Digital Signature: {signature.hex()}")


verification_result = verify_signature(public_key, message, signature)
if verification_result:
    print("Signature is valid.")
else:
    print("Signature is invalid.")
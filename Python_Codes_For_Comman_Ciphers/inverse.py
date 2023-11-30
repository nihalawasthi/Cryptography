#16 Inverse Modular Function

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = extended_gcd(b % a, a)

    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y

def modular_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist.")
    return x%m
a = int(input("enter a"))
m = int(input("enter m"))
print("Modular Inverse:", modular_inverse(a, m))
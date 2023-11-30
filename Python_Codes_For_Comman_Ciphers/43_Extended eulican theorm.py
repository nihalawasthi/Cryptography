def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclidean(b % a, a)
        return gcd, y - (b // a) * x, x

try:
    a = int(input("Enter the first number (a): "))
    b = int(input("Enter the second number (b): "))

    gcd, x, y = extended_euclidean(a, b)
    print(f"GCD({a}, {b}) = {gcd}")
    print(f"x = {x}, y = {y}")
except Exception as e:
    print(f"An error occurred: {e}")

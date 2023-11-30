#15 Modular arithmetic function

def modulo(a, b):
    return a % b

def modular_add(a, b, m):
    return (a + b) % m

def modular_subtract(a, b, m):
    return (a - b) % m

def modular_multiply(a, b, m):
    return (a * b) % m


a = 7
b = 3
m = 5

print("Modulo:", modulo(a, b))
print("Modular Add:", modular_add(a, b, m))
print("Modular Subtract:", modular_subtract(a, b, m))
print("Modular Multiply:", modular_multiply(a, b, m))
#18 Finite Field Implementation with Irreducible Polynomial

class FiniteField:
    def __init__(self, value, characteristic, irreducible_poly):
        self.value = value % characteristic
        self.characteristic = characteristic
        self.irreducible_poly = irreducible_poly

    def __add__(self, other):
        result = (self.value + other.value) % self.characteristic
        return FiniteField(result, self.characteristic, self.irreducible_poly)

    def __mul__(self, other):
        product = (self.value * other.value) % self.characteristic
        return FiniteField(product, self.characteristic, self.irreducible_poly)

    def __pow__(self, exponent):
        if exponent == 0:
            return FiniteField(1, self.characteristic, self.irreducible_poly)
        result = self
        for _ in range(exponent - 1):
            result *= self
        return result

    def __str__(self):
        return str(self.value)

p = 11
irreducible_poly = [1, 1, 0, 1]
x = FiniteField(3, p, irreducible_poly)
y = FiniteField(7, p, irreducible_poly)

print("x =", x)
print("y =", y)
print("x + y =", x + y)
print("x * y =", x * y)
print("x^2 =", x ** 2)
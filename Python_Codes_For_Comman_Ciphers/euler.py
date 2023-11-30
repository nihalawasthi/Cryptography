#13 Euler Toitent Function
def euler(x):
    output = x
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0: 
            while x % i == 0:
                x //= i
            output -= output // i
        if x == 1:
            break
        
    if x > 1:
        output -= output // x

    print(output)

x = int(input('enter x'))
euler(x)

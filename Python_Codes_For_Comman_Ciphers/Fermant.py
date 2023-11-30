#14. Fermat's Little theorem
def fermat(x, y) :
    LHS = (y**(x-1))%x
    print("LHS = [",y,"^",x-1,"]%", x)
    if LHS==1:
        print("true")
    else :
        print("false")
p = int(input("enter p"))
a = int(input("enter a"))
 

for i in range(2, p):
        if (p % i) != 0 and a>0:
            fermat(p, a)
            break
        else:
            print("please check if p is a prime and a is positive")
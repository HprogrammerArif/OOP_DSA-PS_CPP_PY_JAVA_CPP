#WAF TO FIND FACTORIAL

def fact(n):
    f=1
    for i in range(1, n+1):
        f=f*i
    return f


n = int(input("Enter a number: "))
print("Factorial of", n, "is", fact(n))
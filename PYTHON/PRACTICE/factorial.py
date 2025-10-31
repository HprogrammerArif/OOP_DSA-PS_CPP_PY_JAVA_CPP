#WAF TO FIND FACTORIAL

def fact(n):
    f=1
    for i in range(1, n+1):
        print(i)
        f=f*i
    return f
 

# n = int(input("Enter a number: "))
# print("Factorial of", n, "is", fact(n))

def recursive_factorial(n):
    print(n)
    if(n==0 or n==1):
        return 1
    else:
        return n*recursive_factorial(n-1)
    
    

    
n = int(input("Enter a number: "))
print("Factorial of", n, "is", recursive_factorial(n))
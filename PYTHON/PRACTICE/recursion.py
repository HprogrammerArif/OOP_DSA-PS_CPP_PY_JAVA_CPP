#WAP TO CALCULATE THE SUM OF FIRST N NATURAL NUMBERS

def sum(n):
    if(n==0):
        return 0
    return n+sum(n-1)
    
    
n = int(input("Enter a number: "))
print("Sum of first", n, "natural numbers is", sum(n))


# PRINT LIST

def print_list(list, idx):
    print(list[idx])
    if(idx==len(list)):
        return
    print_list(list, idx+1)
    return

fruits = ["apple", "banana", "cherry"]
print_list(fruits, 0)
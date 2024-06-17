#find factorial of a number

def fact(n):
    if(n==1):
        return 1
    return n*fact(n-1)

n=int(input("Enter the number: "))
print("Factorial of",n,": ",fact(n))

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
try:
    n=int(input("enter a no"))
    if(n<0):
        print("factorial is not defined")
    else:
        print("Factorial of",n,"is",fact(n))
except ValueError:
    print("invalid input.Enter a positive integer")
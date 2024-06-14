a=int(input("enter number"))
b=int(input("enter number"))
choice=input("enter an operator +,-,*,/")
if choice=='+':
    print("sum of two numbers",a,"&",b,"is",a+b)
elif choice=='-':
    print("difference of two numbers",a,"&",b,"is",a-b)
elif choice=='*':
    print("product of two numbers",a,"&",b,"is",a*b)
elif choice=='/':
    print("quotient of two numbers",a,"&",b,"is",a/b)
else:
    print("enter a valid choice")
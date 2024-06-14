L=[]
n=int(input("enter how many numbers you want to enter"))
sum=0
for i in range(1,n+1):
    x=int(input("enter number"))
    L.append(x)
    sum+=x
print("Sum of the given numbers is",sum)

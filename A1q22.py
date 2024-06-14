import math
L=[]
n=int(input("How many members you want in list"))
i=1
while(i<=n):
    x=input("enter a number")
    L.append(x)
    i+=1
print("Maximum element in",L,"is",max(L))
print("Minimum element in",L,"is",min(L))

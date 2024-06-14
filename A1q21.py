L=[]
n=int(input("how many members you want in the list"))
for i in range(n):
    x=input("enter the member")
    L.append(x)
m=input("enter the member whose occurrence has to be checked")
count=0
for i in range(1,n):
    if(L[i]==m):
        count=count+1
print(m,"has occured",count,"times in given list")
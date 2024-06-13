n=int(input("enter a no"))
temp=n
sum=0
while(n!=0):
    dig=n%10
    sum+=dig
    n=n//10
print("Sum of digits of",temp,'is',sum)
str1=input("enter a string")
str2=input("enter a string")
str1.lower()
str2.lower()
flag=True
if sorted(str1)!=sorted(str2):
    flag=False
if flag:
    print("strings are anagram of each other")
else:
    print("strings are not anagram of each other")


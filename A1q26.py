str=input("enter string")
substr=input("enter substring to be checked")
choice=int(input("enter 1->check prefix ; 2->check suffix"))
if(choice==1):
    if str.startswith(substr):
        print(str,"starts with given prefix",substr)
    else:
        print(str,"doesn't start with given prefix",substr)
elif(choice==2):
    if str.endswith(substr):
        print(str,"ends with given suffix",substr)
    else:
        print(str,"doesn't end with given suffix",substr)
else:
    print("enter a valid choice")
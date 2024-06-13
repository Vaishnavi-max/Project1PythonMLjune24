lines=[]
while True:
    line=input("enter lines of text. Press Enter for an empty line to finish ")
    if line=="":
        break
    lines.append(line)
print("\n You entered:")
for line in lines:
    print(line)

    

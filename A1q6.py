file1=open('demo.txt','r')
file_lines=file1.readlines()
print("file content is:")
for line in file_lines:
    print(line.strip())
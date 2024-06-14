def copy_file(source_file, destination_file):
    with open(source_file, 'r') as src:
        content = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(content)
source_file = "C:/Users/vaish/OneDrive/Desktop/igdtuw ai ml internship/A1q5.txt"
destination_file = "C:/Users/vaish/OneDrive/Desktop/igdtuw ai ml internship/destination_file_q25.txt.txt"
copy_file(source_file, destination_file)

print("Contents of",source_file, "have been successfully copied to",destination_file)
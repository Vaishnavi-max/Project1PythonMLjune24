import csv
file_path="C:/Users/vaish/OneDrive/Desktop/igdtuw ai ml internship/q15data.csv.txt"
with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
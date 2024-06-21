import csv
with open("C:/Users/vaish/OneDrive/Desktop/igdtuw ai ml internship/secondfile.csv", mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

import csv

#read file
file_name = "file.csv"
try:
    csvfile = open(file_name, 'rt')
except:
    print("File not found")
csv_reader = csv.reader(csvfile, delimiter=";")

#structure data
for row in csv_reader:
    data = [word for word in [row for row in csv_reader]]

print('Number of lines: ', len(data))

#print of first 10 lines
for i in range(0,10):
    print(data[i])
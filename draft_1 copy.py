import csv

readPath = './docss/testCSV.csv'


result = None
with open(readPath, 'r') as file:
    result = list(csv.reader(file))
    file.close()

print(type(result))
print(result)







import csv


asdsd = "C:\\Users\\based on F1D\\Data 8199 2391 2_23_2015 14_55_35_10sec_comma.csv"
newfile = "C:\\Users\\based on F1D\\Data 8199 2391 2_23_2015 14_55_35_10sec_comma_trise.csv"

newContent = []
lowestH = 0
restSec = 0
with open(asdsd, 'r') as f: #, encoding='utf-8'
    reader = list(csv.reader(f))
    
    for i in range(0, len(reader)):
        row = reader[i]
        if i != 0:
            aim = row[0].split(":")
            # print(aim)
            if i == 1: 
                lowestH = int(aim[0])
                restSec = int(aim[1]) * 60 + int(aim[2]) - 1

            hours = int(aim[0]) * 60 * 60 * 1000
            minus = int(aim[1]) * 60 * 1000
            secos = int(aim[2]) * 1000
            mmsecos = int(aim[3])
            finalNum = (hours + minus + secos + mmsecos - (lowestH * 60 * 60 * 1000)) / 1000 - restSec
            newRow = [str(finalNum)] + row[1:]
            newContent.append(newRow)
        else:
            newContent.append(row)

newFile = open(newfile, "w", newline='')
newWriter = csv.writer(newFile)
newWriter.writerows(newContent)

    
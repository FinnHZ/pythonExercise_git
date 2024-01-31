import csv
import copy
import os


# define a covert float to int function------------------------------------------
def cFtoI(num):
    newNum = int(float(num) + 0.5)
    return newNum


# read information--------------------------------------------------------------------------------
pathRa = "./docss/rateeeeeeeeee_3Ti-40Amb-5SD_Model.csv"
rafile = open(pathRa, "r")
csvData = list(csv.reader(rafile))
rafile.close()


# generate title row and scale column--------------------------------------------------------------------------------
titleColumn = []
scaleColumn = []
titleColumn = copy.deepcopy(csvData[0])
temScale = []
for inde in range(1, len(csvData)):
    temScale.append(csvData[inde][1])

# scaleColumn = copy.deepcopy(sorted(set(list(map(lambda x: cFtoI(x), temScale)))))
scaleColumn = [11,14.8,19,28.5,42,57,69,81,100,131,162,195,233,285,388,437,560]

# tidy up data--------------------------------------------------------------------------------------------------
tiedDict = {}
for i in range(1, len(csvData[0])):    #column
    colList_tem = []
    for j in range(1, len(csvData)):   #row
        unitList = [cFtoI(csvData[j][i]), csvData[j][0]]
        colList_tem.append(unitList)
    tiedDict[csvData[0][i]] = colList_tem

# filter and export--------------------------------------------------------------------------------------------------
finalList = []
# finalList.append(titleColumn)
t = 0
while t < len(scaleColumn):
    finalList.append([scaleColumn[t]])
    t += 1



for key in tiedDict:
    objList = copy.deepcopy(tiedDict[key])
    objList.sort(key = lambda unit: unit[0], reverse = True)
    # print(key, "-----------------------------------------------")
    # print(tiedDict[key])
    # print(objList)
    for s in range(0, len(scaleColumn)):
        aimCell = ""
        for item in objList:
            if item[0] >= scaleColumn[s]:
                aimCell = item[1] + "_" + str(item[0])  +"A"  # + "\n"
        finalList[s].append(aimCell)

finalList.insert(0, titleColumn)
pathEx = "./docss/ratedTable.csv"
try:
    os.remove(pathEx)
except:
    pass
fileSave_para = open(pathEx, 'w', newline='')
fileSave_para_writer = csv.writer(fileSave_para)
fileSave_para_writer.writerows(finalList)
fileSave_para.close()

print("Finished!!")

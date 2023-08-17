import random
import itertools
import csv



bigList = []                #---------------------------------------1
for i in range(1, 41):
    bigList.append(i)



officialRandom_ori = []         #---------------------------------------2   
officialDataFile = open("./docss/officialRandom.csv", "r")                  
officialData = list(csv.reader(officialDataFile))
for ele in officialData:
    officialRandom_ori += ele
officialDataFile.close()

officialRandom = list(map(lambda x: int(x), officialRandom_ori))


officialLike = list(set(officialRandom))       #---------------------------------------3

for it in officialLike:
    probability = officialRandom.count(it)/len(officialRandom)*100
    # print(it, ": ", officialRandom.count(it), "--", "%.2f"%probability, "%", ", ", len(officialLike))
# print(sorted(officialLike), ": ", len(officialLike))



onOfficialList = []           #---------------------------------------4*
for item in bigList:
    if item not in officialLike:
        onOfficialList.append(item)

# print(officialLike)
# print(onOfficialList)

#on official
onOfficialAll = list(itertools.combinations(onOfficialList, 6))
onOfficialWin = sorted(random.sample(onOfficialList, 6))
print(onOfficialWin)

onOfficialAll_reversed = list(itertools.combinations(officialLike, 6))
onOfficialWin_reversed = sorted(random.sample(officialLike, 6))
print(onOfficialWin_reversed)



import random
import csv


# a = 0.64

# print(int(round(a,0)))


#--------------------------------------------------------------------------------------------------------


# pools = []         ###########################
# for i in range(1, 41):
#     ra = random.randint(1,41)
#     for j in range(0, ra):
#         pools.append(i)

pools = []         #---------------------------------------2   
officialDataFile = open("./docss/officialRandom.csv", "r")                  
officialData = list(csv.reader(officialDataFile))
for ele in officialData:
    pools += ele
officialDataFile.close()


def removeMultipleElesFromList(li, ele):
    num = li.count(ele)
    i = 0
    while i < num:
        li.remove(ele)
        i += 1

selectedList = []   #######################################

choiceTimes = 0
while choiceTimes < 6:
    choicedItem = random.choice(pools)
    selectedList.append(choicedItem)
    removeMultipleElesFromList(pools, choicedItem)
    choiceTimes += 1

print(sorted(selectedList))



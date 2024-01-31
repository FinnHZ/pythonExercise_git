
import random
import itertools
import time
import copy


bigList = []
maxLimit = 4
percentOffset = 0.05

#          [    6      5+1      5       4+1    4     3+1  3 ]
possible = [0.000001, 0.00001, 0.0001, 0.001, 0.01, 0.1, 0.5]
divisionDict = {"d1":0, "d3":0, "d5":0, "d7":0}

def connectNumStr(listObj):
    tem_str = str(listObj[0])
    for i in range(1, len(listObj)):
       it = listObj[i]
       tem_str += "-{}".format(str(it))
    return tem_str



# generate pool function---------------------------------------------------
def standardPool(limit):
    temSPool = []  # temporary real time number pool [[n1,n2,n3,n4, n5, n6], [n11,n12,n13,n14, n15, n16]...].
    
    i = 0
    while i < limit:
        tem_s =  sorted(random.sample(range(1,41), 6))  #generate one random standard line.
        temSPool.append(tem_s)  #put the new temporary standard line into temporary real time number pool.
        i += 1
        
    return temSPool

    # temBPool = []
    # tem_b =  sorted(random.sample(range(1,11), 1))  #generate random bouns
    
def overlapPercent(existingList, drawList):
    l1 = copy.deepcopy(existingList)
    l2 = copy.deepcopy(drawList)
    r1 = l2 + l1
    r2 = set(r1)
    r = (len(r1) -len(r2)) / len(l1)
    return r



# final time control---------------------------------------------------
alreadyPoolList= standardPool(maxLimit)

# passFlag =True
# while passFlag:
#     drawObj = sorted(random.sample(range(1,41), 6))
#     for item in alreadyPoolList:
#         overlapRate = overlapPercent(item, drawObj)
#         if overlapRate >= 3/6 and overlapRate < 4/6:

#         elif overlapRate >= 4/6 and overlapRate < 5/6:

#         elif overlapRate >= 5/6 and overlapRate < 6/6:

#         elif 




# real time control-------------------

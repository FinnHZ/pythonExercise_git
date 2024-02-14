import random
import copy

randGenerate = random.Random()

def randomList(rangeList, generateLength):
    chooseList = []

    restNumLength = len(rangeList)

    if restNumLength >= generateLength:
        j = 0 
        while j < generateLength:
            intIndexRandom = randGenerate.randint(a=0, b=restNumLength-1)
            intObj = rangeList[intIndexRandom]
            chooseList.append(intObj)
            rangeList.remove(intObj)
            j += 1
            restNumLength -= 1

        
    else:
        chooseList = copy.deepcopy(rangeList)
    
    return chooseList



#Step1-------------------------------------------------------------------------------------------
# Tidy up already existed integer list------------------------------------------------------------
# alreadyList_0 = [1,2,5,9,11,15,18,21,23,36,4,5,10,17,29,34,2,5,17,18,23,34,3 , 25, 16, 28, 13, 37,31, 26, 40, 32, 38, 6,8, 12, 33, 35, 27, 39,
#                  24, 7, 22, 20, 19, 14]
# alreadyList_1 = list(set(alreadyList_0))

# # generate a list contains integer from 1 to 40------------------------------------------------------------
# tList = []
# for i in range(1,41):  
#     tList.append(i)

# # remove the item we don't want from the 'tList'-----------------------------------------------------------
# for item in alreadyList_1:  
#     tList.remove(item)



# #Step2-------------------------------------------------------------------------------------------
# restList = copy.deepcopy(tList)  #step1 use
# finalList = randomList(restList, 6)

# print(finalList)

l1 = [1,4,11,15,10,18,21,26,29]
l2 = [3, 25, 16, 28, 13, 37,31, 40, 32, 38, 6,8, 12, 33, 35, 27, 39, 24, 7, 22, 20, 19, 14]


c1 = randomList(l1, 2)
c2 = randomList(l2, 4)

print(c1,c2)

finalList = c2 + c1
print(finalList)





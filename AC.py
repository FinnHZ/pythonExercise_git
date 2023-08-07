import random
import itertools


#Generate pool--------------------------------------------------------
# listPool = []

# for i in range(1, 41):
#     listPool.append(i)

#Generate all arr-----------------------------------------------------
# ginPool = []

# temList = [1,2,3,4]

# ginPool = list(itertools.combinations(temList, 3))

# print(ginPool)

# -----------------------------------------------------

listfilter_1 = [3,4,5,6,7]
listfilter_2 = [18,19,20,21,22,23,24]
listfilter_3 = [35,36,37,38,39]

listfilter_4 = listfilter_1 + listfilter_2 + listfilter_3
totalPool = list(itertools.combinations(listfilter_4, 3))

print(len(totalPool))













#simulate to generate draw--------------------------------------------
randomArr = sorted(random.sample(range(1, 41), 6))

# print(randomArr)
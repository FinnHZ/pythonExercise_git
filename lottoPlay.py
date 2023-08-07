import random
import itertools


#Generate pool--------------------------------------------------------
listPool = []


for i in range(1, 41):
    listPool.append(i)



#Generate all arr-----------------------------------------------------
ginPool = []

temList = [1,2,3,4]

ginPool = list(itertools.combinations(temList, 3))

print(ginPool)














#simulate to generate draw--------------------------------------------
randomArr = sorted(random.sample(range(1, 41), 6))

# print(randomArr)
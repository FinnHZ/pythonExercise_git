
import random
import itertools
import time
from functools import reduce

# -----------------------------------------------------------
# a="1;2;3;4;5"


# newlist = list(a.split(";"))

# print(newlist)


# secondlist = list(map(lambda x: int(x), newlist))

# print(secondlist)
# -----------------------------------------------------------
# l1 = [1,2,3,4,5,6]
# l2 = [1,0,2,7,8,9]
# l3 = [1,2]
# l4 = [3,4]
# l5 = [1, 2, 3, 4]

# r1 = set(l1) & set(l2)
# print(r1, type(r1), len(r1))


# r2 = [i for i, j in zip(l1, l2) if i ==j]

# print(r2, type(r2), len(r2))


# print(list(itertools.product(l3, l4)))


# print(list(itertools.combinations(l5, 2)))

# -----------------------------------------------------------
criteria = 4

def compareListFunc(d1, d2):
    l1 = d1["lo"]
    l2 = d2["lo"]
    r = len(set(l1) & set(l2))
    
    if r >= criteria:
        return [d1["date"], d2["date"], r]
    else:
        return []



bigDictComb= [
         {"date":"01.01.2023", "lo":[1,2,3,4,5,6]}, 
          {"date":"01.02.2023", "lo":[1,0,2,7,8,9]}, 
          {"date":"01.03.2023", "lo":[1,0,2,4,8,3]}]


bigDictListComb = list(itertools.combinations(bigDictComb, 2))

# print(bigDictListComb)
for item in bigDictListComb:
    test = reduce(lambda x, y: compareListFunc(x, y), item)
    print(test)











#-----------------------------------------------------------


# listfilter_1 = [3,4,5,6,7]
# listfilter_2 = [18,19,20,21,22,23,24]
# listfilter_3 = [35,36,37,38,39]

# listfilter_4 = listfilter_1 + listfilter_2 + listfilter_3



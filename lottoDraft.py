
import random
import itertools
import time
from functools import reduce
from datetime import datetime as dt
#-----------------------------------------------------------
# a="1;2;3;4;5"


# newlist = list(a.split(";"))

# print(newlist)


# secondlist = list(map(lambda x: int(x), newlist))

# print(secondlist)
#-----------------------------------------------------------
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

#-----------------------------------------------------------
criteria = 4

def compareListFunc(d1, d2):
    l1 = d1["lo"]
    l2 = d2["lo"]
    r = len(set(l1) & set(l2))
    
    date1 = dt.strptime(d1["date"], "%d/%m/%Y")
    date2 = dt.strptime(d2["date"], "%d/%m/%Y")
    intervalDays = str(date2-date1).split(" days")[0]

    # print(intervalDays)
    return [d1["date"], d2["date"], r, intervalDays]




bigDictComb= [
         {"date":"01/04/2023", "lo":[1,2,3,4,5,6]}, 
          {"date":"01/03/2023", "lo":[1,0,2,7,8,9]}, 
          {"date":"01/05/2023", "lo":[1,0,2,4,8,3]}]


# sort list according to one specific key of the dictionary os the list---------------------------
bigDictComb2 = {}
bigDictComb2 = sorted(bigDictComb, key=lambda item: item["date"])

print(bigDictComb2)

#  compare two items' date one by one-------------------------------------------------------------
bigDictListComb = list(itertools.combinations(bigDictComb2, 2))

# print(bigDictListComb)
for item in bigDictListComb:
    test = reduce(lambda x, y: compareListFunc(x, y), item)
    print(test)


# organize 'lo' data distribution------------------------------------------------------------------
pools ={}

for i in range(1, 41):
    pools[str(i)] = []

for key in pools:
    for item in bigDictComb2:
        if int(key) in item["lo"]:
            pools[key].append(item["date"])

print(pools)



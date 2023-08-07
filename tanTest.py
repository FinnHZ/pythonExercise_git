import math
from datetime import datetime as dt

# def testT(nums):
#     aaaaa = sorted(nums, reverse=True)
#     print(aaaaa)
#     bbbbb = ' '.join([str(i) for i in aaaaa])
#     # ccccc = int(forbbbbb)
#     return bbbbb

# x = [1, 2, 4, 6, 8, 8, 10, 90]

# r = testT(x)
# print(r, type(r))
#####################################################################################
# test = {"1x":"a",
#  "2x":"b"}

# for i in test:
#     print(i)

######################################################################################
# t = list(set([[1,2],2,2,[1,2],44,4,4]))
# print(t)
#########################################################################################

# print(math.pow(1/40,6))

################################################
d = "2023-03-07"
dd = dt.strptime(d, "%Y-%m-%d")
print(dd, type(dd))

nowd = dt.now()
print(nowd, type(nowd))
from functools import reduce

# powerFilePathDict = {"10s":"", "20s":"", "30s":"", "60s":""}
# powerFilePathDict = ["", "", "", ""]

# # def combine(k1, k2):
# #     newthing = powerFilePathDict[k1] + powerFilePathDict[k2]
# #     print(type(newthing))
# #     return newthing

# def combine(k1, k2):
#     newthing = k1 + k2
#     print(type(newthing))
#     return newthing


# readCheck = reduce(combine, powerFilePathDict) 
# print(readCheck)



ted = [1]
res = reduce(lambda x, y: x*10 + y*5, ted)
print(res, type(res))
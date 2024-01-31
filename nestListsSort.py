

originaList = [
    [1, 9],
    [2, 8],
    [3, 7],
    [4, 6]
]


originaList.sort(key=lambda unit: unit[0]) #, reverse=True

print(originaList)



a = {'a':[10,3], 'c':[3,4], 'b':[0,2]}
b = sorted(a.items(), key=lambda x: x[0][0])  
c = sorted(a.items(), key=lambda x: x[1][0])
# d = sorted(a.items(), key=lambda x: x[0][1])
e = sorted(a.items(), key=lambda x: x[1][1])


"""!!!!!!!!!
key:[v1, v2]  --->
index of key  ---> 0
index of [v1, v2] --->  1 

"""





print(b)
print(c)
# print(d)
print(e)
import copy


a = 10
b = a
c = a / 1
d = a - 5
e = b - 4
print(a,';', b,';', c,';', d,';', e,';', a==b, a==c)
print(id(a),';', id(b),';', id(c),';', id(a)==id(b), id(a)==id(c))


print("--------------------------------------------------------------Normal")
listA = [1, 2, ["a", "b"], 4, 5]
listB = [7, 8, ["t", "u"], 9, 10]
print(id(listA),';', id(listB),';', id(listA)==id(listB))
print(id(listA[2]),';', id(listB[2]),';', id(listA[2])==id(listB[2]))


print("--------------------------------------------------------------assignment")
listC = [1, 2, ["a", "b"], 4, 5]
listD = listC
print(id(listC),';', id(listD),';', id(listC)==id(listD))
print(id(listC[2]),';', id(listD[2]),';', id(listC[2])==id(listD[2]))


print("--------------------------------------------------------------copy.copy")
listE = [1, 2, ["a", "b"], 4, 5]
listF = copy.copy(listE)
print(id(listE),';', id(listF),';', id(listE)==id(listF))
print(id(listE[2]),';', id(listF[2]),';', id(listE[2])==id(listF[2]))


print("--------------------------------------------------------------copy.deepcopy")
listG = [1, 2, ["a", "b"], 4, 5]
listH = copy.deepcopy(listG)
print(id(listG),';', id(listH),';', id(listG)==id(listH))
print(id(listG[2]),';', id(listH[2]),';', id(listG[2])==id(listH[2]))


print("--------------------------------------------------------------draft problem")
listI = [{"a": 1}, {"b": 1}]
listJ = [copy.deepcopy(listI[0])]
listJ[0]["a"] = 3 

print(listI)
print(listJ)
print(id(listI))
print(id(listJ))

listK = [{"a": 1}, {"b": 1}]
listL = [listK[0]]
listL[0]["a"] = 3 


print(listK)
print(listL)
print(id(listK))
print(id(listL))
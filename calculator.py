import math


# power calculator
# while True:
#     baseNumber = input("Enter the base number: ")
#     power = input("Enter the power: ")


#     result = math.pow(float(baseNumber), int(power))

#     print("result: " + str(result))


#base of 8 or 16 ----> 2
while True:
    eightBase = input("Enter the 8 / 16 base number: ")

    f_Number = eightBase[0]
    s_Number = eightBase[1]
    lengthNumber = len(eightBase)
    if f_Number == "0":
        if s_Number == "x":
            try:
                obj16 = 0
                base16List = []
                for i in range(2, lengthNumber):
                    base16List.append(eightBase[i])
                
                for j in range(0, len(base16List)):
                    l16 = len(base16List) -1
                    item = base16List[j]
                    number16 = 0
                    if item == "A":
                        number16 = 10
                    elif item == "B":
                        number16 = 11
                    elif item == "C":
                        number16 = 12
                    elif item == "D":
                        number16 = 13
                    elif item == "E":
                        number16 = 14
                    elif item == "F":
                        number16 = 15
                    else:
                        number16 = int(item)
                    
                    tem16 = number16 * math.pow(16, l16-j)
                    obj16 = obj16 + tem16
                    
                print(obj16)
            except:
                print("This is not a 16 base of number")
        else:
            try:
                obj8 = 0
                base8List = []
                for i in range(1, lengthNumber):
                    base8List.append(eightBase[i])
                
                for j in range(0, len(base8List)):
                    l8 = len(base8List) -1
                    item = base8List[j]
                    number8 = int(item)
                    
                    tem8 = number8 * math.pow(8, l8-j)
                    obj8 = obj8 + tem8
                print(obj8)
            except:
                print("This is not a 8 base of number")
    else:
        print("This is not a 8 or 16 base of number")






# 2 ---->  base of 16
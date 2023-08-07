

string_test = "1:a, 2:b, 3:c"

test_1List = list(string_test.replace(" ", "").split(","))





def mapTest(sList):
    newList = sList.split(":")
    return newList


result = list(map(mapTest, test_1List))

print(result)
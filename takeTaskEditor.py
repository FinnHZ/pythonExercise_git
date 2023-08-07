from functools import reduce


parentPath = "C:\\Users"


fileNameList = [
"Prototype source 2 Phase - updated",
"Prototype source 2 Phase GERMAN - updated",
"Prototype source S2E - Updated added serial setting",
"Prototype source S2E GERMAN - updated",
"EMX4e Dielec",
"EMX4i Dielec - Copy",
"EMX4i Dielec",
"MCD600 Dielec"
]


def getNecessaryEditor(path):

    f =  open(path, "r")

    content_f = f.readlines()

    newC = []
    for item in content_f:
        newC.append(item.strip('\n').strip())
    
    f.close()

    classifyList = []
    temList = []
    for item in newC:
        if "<TaskObject" in item:
            temList = []
        temList.append(item)
        if "</TaskObject>" in item:
            classifyList.append(temList)

    editorMethodMatchlist = []
    for item in classifyList:
        temMatchList = []
        for x in item:
            if "<MethodId>" in x:
                temMatchList.append(x)
            elif "<Editor>" in x:
                temMatchList.append(x)
        editorMethodMatchlist.append(temMatchList)

    emLIST = []
    for item in editorMethodMatchlist:
        temEMlist = []
        temEMlist.append(item[0].replace("<MethodId>","").replace("</MethodId>",""))
        temEMlist.append(item[1].replace("<Editor>","").replace("</Editor>",""))
        emLIST.append(temEMlist)

    necessaryMethod = ["Test Measure Meter",
    "TestControlSoftwareVersion",
    "TestModelSoftwareVersion",
    "Test Resistance Agilent DMM",
    "Test AC Voltage Agilent DMM",
    "Test Power Meter Current"]

    necessaryEditor = []
    for item in emLIST:
        if item[0] in necessaryMethod:
            necessaryEditor.append(item[1])

    finalNessaryEditor = list(set(necessaryEditor))
    
    return finalNessaryEditor


separateNecessaryEditors = []
for file in fileNameList:
    tem_NecessaryEdits = getNecessaryEditor(parentPath+file+".xml")
    separateNecessaryEditors.append(tem_NecessaryEdits)

combineNecessaryEditors = reduce(lambda x,y: x+y, separateNecessaryEditors)
finalCombined = list(set(combineNecessaryEditors))
print(finalCombined)



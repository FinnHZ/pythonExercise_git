parentPath = "C:\\Users\\f.he\\OneDrive - AuCom Group\\Desktop\\sssss.txt"



def getNecessaryEditor(path):

    f =  open(path, "r")

    content_f = f.readlines()

    newC = []
    for item in content_f:
        newC.append(item.strip('\n').strip())
    
    f.close()


    needItemList = []
    for item in newC:
        if ("StringVar()" in item) or ("IntVar()" in item):
            needItemList.append(item)

    print(needItemList)



getNecessaryEditor(parentPath)
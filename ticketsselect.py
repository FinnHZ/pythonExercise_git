import copy
from itertools import combinations

#Step1: prepare a pool
pool = []

for i in range(0, 40):
    pool.append(i+1)

def removeRepeated(listObj):
    newList = copy.deepcopy(listObj)
    for item in newList:
        removeFlag = True
        
        while removeFlag:
            numObjs = newList.count(item)
            if numObjs > 0:
                newList.remove(item)
            else:
                removeFlag = False
    
    return newList

#Step2: from L
tickets_l = [
    [1,2,3,4,5,6],
    [1,2,3,4,6,7],
    [1,2,3,4,7,8]
    # [],
    # [],
    # [],
    # [],
    # [],
    # [],
    # [],
    ]

luckyLevel = 4  # 4 is the most small award. This number:  4 <= luckyLevel <= 6
luckyTiNum = 1  # This number:  1 <= luckyLevel <= len(tickets_l)  or -- >   int(len(tickets_l)*percent)   < --percent<1


#Step3: remove non-autofill number
noAutoTicketEle = copy.deepcopy(pool)

for ti in tickets_l:           #!!!!get the elements which L does not choose.
    for el in ti:
        try:
            noAutoTicketEle.remove(el)
        except:
            pass
print("Non-Chosen number:", noAutoTicketEle)    # -------------Finn: get the elements which L does not choose.

#Step4: lucky level

aimTicket = copy.deepcopy(tickets_l)

ticketDictCom = {}
ticketListCom = []

for i in range(0, len(aimTicket)):    #!!!!!!!generate all combinations based on different 'luckyLevel'
    tis = aimTicket[i]
    temList = []
    for t in combinations(tis, luckyLevel):
        aimCom = sorted(list(t))
        temList.append(aimCom)
        ticketListCom.append(aimCom)
    ticketDictCom[str(i)] = temList

filterOptions_1 = []
for ai in ticketListCom:      # find the possibility, which may be from L's hope
    countAI = ticketListCom.count(ai)
    if countAI == luckyTiNum:
        filterOptions_1.append(ai)

if len(filterOptions_1) == 0:
    print("There is not any tickt can make you win a level {} award, if you just want win {} tickt.".format(str(luckyLevel), str(luckyTiNum)))
else:
    filterOptions_2 = filterOptions_1 #removeRepeated(filterOptions_1)
    print("Aim combinations:", filterOptions_2)   # -------------Finn: get the aim combinations under the condition
    for k in ticketDictCom:
        for item in filterOptions_2:
            if item in ticketDictCom[k]:
                print("Index of aim ticket:", k)    # -------------Finn: get the index of aim ticket under the condition













targetList = [
    {"totalPool":3186997, "6B":1, "5B":373, "4B":15116, "3B":218608},
    {"totalPool":2629909, "6B":0, "5B":260, "4B":11281, "3B":159528},
    {"totalPool":3008135, "6B":2, "5B":409, "4B":15443, "3B":206431},
    {"totalPool":2916753, "6B":2, "5B":341, "4B":14073, "3B":199070},
    {"totalPool":2600135, "6B":1, "5B":261, "4B":12128, "3B":168157},
    {"totalPool":3084261, "6B":0, "5B":374, "4B":15105, "3B":204994},
    {"totalPool":2534188, "6B":0, "5B":297, "4B":12270, "3B":165619},
    {"totalPool":3369284, "6B":2, "5B":433, "4B":17564, "3B":248239},
    {"totalPool":2743941, "6B":4, "5B":343, "4B":14362, "3B":190522}
]

aimList = []
for item in targetList:
    temDict = {}
    totalTicket = int(item["totalPool"] / 1.5)
    temDict["total"] = totalTicket
    temDict["6Bn"] = "%2f"%((item["6B"] / totalTicket) * 100) + "%"
    temDict["5Bn"] = "%2f"%((item["5B"] / totalTicket) * 100) + "%"
    temDict["4Bn"] = "%2f"%((item["4B"] / totalTicket) * 100) + "%"
    temDict["3Bn"] = "%2f"%((item["3B"] / totalTicket) * 100) + "%"
    aimList.append(temDict)

for it in aimList:
    print(it)

import docx
import copy


historyYear = {'2011':[], '2012':[], '2013':[], '2014':[], '2015':[], '2016':[], '2017':[], '2018':[], '2019':[], '2020':[], '2021':[], '2022':[], '2023':[]}
lottoHistoryPath = ''


def clearLottoHistory(readPath):
    lottoList = []

    hiList = []
    with open(readPath, 'r') as file:
        hiList = file.readlines()
        file.close()

    for i in range(0, len(hiList)):
        one_tem ={"date": "", "weekDay": "", "lotto": [], "bonus": 0, "day": "", "month": "", "year": ""}
        item = hiList[i]
        if '<div class="date">' in item:
            dw = hiList[i+1].replace("<span>", "").replace("\t\t\t\t\t\t", "").replace("\t\t\t\t\t\n", "")
            dwlist = dw.split("</span>")
            one_tem["date"] = dwlist[1]
            dateSeparate = dwlist[1].split(" ")
            one_tem["day"] = dateSeparate[1]
            one_tem["month"] = dateSeparate[0]
            one_tem["year"] = dateSeparate[2]


            one_tem["weekDay"] = dwlist[0]

            if  "Draw Number:" not in hiList[i+4]:
                for t in range(0,7):
                    if t < 6:
                        lb = hiList[i+14+t].replace('<li class="ball ball"><span>', '').replace('</span><div></div></li>', '').replace('\t\t\t\t\t\t\t\t', '').replace('\n', '')
                        one_tem["lotto"].append(int(lb))
                    elif t == 6:
                        lbo = hiList[i+14+t].replace('<li class="ball bonus-ball"><span>', '').replace('</span><div>Bonus </div></li>', '').replace('\t\t\t\t\t\t\t\t', '').replace('\n', '')
                        one_tem["bonus"] = int(lbo)
            else:
                for t in range(0,7):
                    if t < 6:
                        lb = hiList[i+11+t].replace('<li class="ball ball"><span>', '').replace('</span><div></div></li>', '').replace('\t\t\t\t\t\t\t\t', '').replace('\n', '')
                        one_tem["lotto"].append(int(lb))
                    elif t == 6:
                        lbo = hiList[i+11+t].replace('<li class="ball bonus-ball"><span>', '').replace('</span><div>Bonus </div></li>', '').replace('\t\t\t\t\t\t\t\t', '').replace('\n', '')
                        one_tem["bonus"] = int(lbo)


            lottoList.append(one_tem)
    
    return lottoList
        

for key in historyYear:
    # print(key)
    lottoHistoryPath = './docss/' + key + 'Lotto.txt'
    result = clearLottoHistory(lottoHistoryPath)
    historyYear[key] = result

# print(historyYear['2013'])

allLotto = []

for oneYearLotto_key in historyYear:
    allLotto += historyYear[oneYearLotto_key]


def organizeData():
    dayDict_total = {"1st":{"times":0,"nums":[]}, "2nd":{"times":0,"nums":[]}, "3rd":{"times":0,"nums":[]}, "4th":{"times":0,"nums":[]}, "5th":{"times":0,"nums":[]}, "6th":{"times":0,"nums":[]}, "7th":{"times":0,"nums":[]}, "8th":{"times":0,"nums":[]}, "9th":{"times":0,"nums":[]}, "10th":{"times":0,"nums":[]}, "11th":{"times":0,"nums":[]}, "12th":{"times":0,"nums":[]}, "13th":{"times":0,"nums":[]}, "14th":{"times":0,"nums":[]}, "15th":{"times":0,"nums":[]}, "16th":{"times":0,"nums":[]}, 
                    "17th":{"times":0,"nums":[]}, "18th":{"times":0,"nums":[]}, "19th":{"times":0,"nums":[]}, "20th":{"times":0,"nums":[]}, "21st":{"times":0,"nums":[]}, "22nd":{"times":0,"nums":[]}, "23rd":{"times":0,"nums":[]}, "24th":{"times":0,"nums":[]}, "25th":{"times":0,"nums":[]}, "26th":{"times":0,"nums":[]}, "27th":{"times":0,"nums":[]}, "28th":{"times":0,"nums":[]}, "29th":{"times":0,"nums":[]}, "30th":{"times":0,"nums":[]}, "31st":{"times":0,"nums":[]}}

    dayDict_lotto = {"1st":{"times":0,"nums":[]}, "2nd":{"times":0,"nums":[]}, "3rd":{"times":0,"nums":[]}, "4th":{"times":0,"nums":[]}, "5th":{"times":0,"nums":[]}, "6th":{"times":0,"nums":[]}, "7th":{"times":0,"nums":[]}, "8th":{"times":0,"nums":[]}, "9th":{"times":0,"nums":[]}, "10th":{"times":0,"nums":[]}, "11th":{"times":0,"nums":[]}, "12th":{"times":0,"nums":[]}, "13th":{"times":0,"nums":[]}, "14th":{"times":0,"nums":[]}, "15th":{"times":0,"nums":[]}, "16th":{"times":0,"nums":[]}, 
            "17th":{"times":0,"nums":[]}, "18th":{"times":0,"nums":[]}, "19th":{"times":0,"nums":[]}, "20th":{"times":0,"nums":[]}, "21st":{"times":0,"nums":[]}, "22nd":{"times":0,"nums":[]}, "23rd":{"times":0,"nums":[]}, "24th":{"times":0,"nums":[]}, "25th":{"times":0,"nums":[]}, "26th":{"times":0,"nums":[]}, "27th":{"times":0,"nums":[]}, "28th":{"times":0,"nums":[]}, "29th":{"times":0,"nums":[]}, "30th":{"times":0,"nums":[]}, "31st":{"times":0,"nums":[]}}
    
    dayDict_bonus = {"1st":{"times":0,"nums":[]}, "2nd":{"times":0,"nums":[]}, "3rd":{"times":0,"nums":[]}, "4th":{"times":0,"nums":[]}, "5th":{"times":0,"nums":[]}, "6th":{"times":0,"nums":[]}, "7th":{"times":0,"nums":[]}, "8th":{"times":0,"nums":[]}, "9th":{"times":0,"nums":[]}, "10th":{"times":0,"nums":[]}, "11th":{"times":0,"nums":[]}, "12th":{"times":0,"nums":[]}, "13th":{"times":0,"nums":[]}, "14th":{"times":0,"nums":[]}, "15th":{"times":0,"nums":[]}, "16th":{"times":0,"nums":[]}, 
            "17th":{"times":0,"nums":[]}, "18th":{"times":0,"nums":[]}, "19th":{"times":0,"nums":[]}, "20th":{"times":0,"nums":[]}, "21st":{"times":0,"nums":[]}, "22nd":{"times":0,"nums":[]}, "23rd":{"times":0,"nums":[]}, "24th":{"times":0,"nums":[]}, "25th":{"times":0,"nums":[]}, "26th":{"times":0,"nums":[]}, "27th":{"times":0,"nums":[]}, "28th":{"times":0,"nums":[]}, "29th":{"times":0,"nums":[]}, "30th":{"times":0,"nums":[]}, "31st":{"times":0,"nums":[]}}
    
    #just combined total lotto nums
    for item in allLotto:
        totalNums_tem = copy.deepcopy(item["lotto"])
        totalNums_tem.append(item["bonus"])
        # print(totalNums_tem)
        # print(item["day"])
        dayDict_total[item["day"]]["nums"] += totalNums_tem
        dayDict_total[item["day"]]["times"] += 1

    # #just lotto nums
    # for item in allLotto:
    #     dayDict_lotto[item["day"]]["nums"] += item["lotto"]
    #     dayDict_lotto[item["day"]]["times"] += 1
    
    # #just bonus nums
    # for item in allLotto:
    #     dayDict_bonus[item["day"]]["nums"].append(item["bonus"])
    #     dayDict_bonus[item["day"]]["times"] += 1


    # dateresult = {"totalDraw":dayDict_total, 
    #             "lottoDraw":dayDict_lotto,
    #             "bonusDraw":dayDict_bonus}

    dateLottoResult = []

    basicDateDict = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th", "14th", "15th", "16th", 
                    "17th", "18th", "19th", "20th", "21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st"]
    lottoBalls_total = []
    for n in range(1, 41):
        lottoBalls_total.append(n) 




    for i in range(0, len(lottoBalls_total)):
        for j in range(0, len(basicDateDict)):
            unitList = []  # it should include 3 number:[lottoNum, dateday, numOfTheLottoNum]
            
            unitList.append(i)
            unitList.append(j)
            unitList.append(dayDict_total[basicDateDict[j]]["nums"].count(lottoBalls_total[i]))

            dateLottoResult.append(unitList)



    return dateLottoResult


rrrrrr = organizeData()
print(rrrrrr)

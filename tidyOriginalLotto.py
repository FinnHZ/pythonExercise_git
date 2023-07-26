import os
import csv

yearList = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]




def tidyLottoHistory_v1(readPath):
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

            

            for key in one_tem:
                temList = []
                temList.append(key)
                temList.append(one_tem[key])
                lottoList.append(temList)
    
    return lottoList




def writeTidyLottoFile(yearKey):
    originalLottoPath = './static/doc/Original/' + str(yearKey) + 'LottoOri.txt'
    tidyLottoPath = './static/doc/lotto/' + str(yearKey) + 'LottoTidy.txt'
    try:
        os.remove(tidyLottoPath)
    except:
        pass


    tidyLottoResult = tidyLottoHistory_v1(originalLottoPath)


    with open(tidyLottoPath, 'w', newline='') as csvFile:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerows(tidyLottoResult)
        csvFile.close()


for y in yearList:
    writeTidyLottoFile(y)



import winreg
import xlsxwriter
import itertools
import copy
from datetime import datetime as dt
from datetime import date

#Function----------------------------------------------------------------------------------------------------------
class DistributionGenerate:
    def __init__(self) -> None:
        pass

    def sortBasedOnDate(self, lo_all_tem):
        lo_all = []
        for ori in lo_all_tem:
            temORI = {}
            temORI = copy.deepcopy(ori)
            temDate = dt.strptime(ori["date"], "%d/%m/%Y")   # for excel write use=========
            temORI["date"] = temDate
            lo_all.append(temORI)

        # sort list according to one specific key of the dictionary os the list---------------------------
        bigDictComb_tem = sorted(lo_all, key = lambda item: item["date"], reverse = True)

        bigDictComb = []
        for bi in bigDictComb_tem:
            temBI = copy.deepcopy(bi)
            temDate = date.strftime(bi["date"], "%d/%m/%Y")   # for excel write use=========
            temBI["date"] = temDate
            bigDictComb.append(temBI)
        
        return bigDictComb
    
    
    def tidyForExcel(self, bigDictComb):
        #tidy data up and organize them to the specific format
        tidyForExcel = []
        firstUnit = []
        firstUnit.append("Date")
        firstUnit.append("WeekDay")
        for i in range(1, 41):
            firstUnit.append(i)

        tidyForExcel.append(firstUnit)

        for item in bigDictComb:
            unit = []
            unit.append(item["date"])
            unit.append(item["wD"])
            for j in range(1, 41):
                if j in item["lo"] or j == item["bo"]:
                    unit.append("$")
                else:
                    unit.append('')
            tidyForExcel.append(unit)

        return tidyForExcel

    
    def accumulationOrganize(self, sourceTidiedList, startRow, accumulateNum):   # real data row number the first is 1
        #Accumulation organize
        accumulateDistribution = []

        tidyForExcelAccu = copy.deepcopy(sourceTidiedList)
        tidyForExcelAccu.pop(0)

        unit0 = []      #for separate two parts
        for i in range(0, 42):
            unit0.append("")
        accumulateDistribution.append(unit0)
        accumulateDistribution.append(tidyForExcelAccu[startRow-1])

        if startRow+accumulateNum <= len(tidyForExcelAccu)-1 and startRow >=0:
            # try to get all kinds of row combines number groups
            groupQuenue = []
            for m in range(0, len(tidyForExcelAccu)):
                groupQuenue.append(m)
            
            differentRangeCom = list(itertools.combinations(groupQuenue, 2))
            for gItem in differentRangeCom: 
                if gItem[0]+1 == startRow and gItem[1]-gItem[0]+1 <= accumulateNum:
                    self.accumulateTidy(accumulateDistribution, tidyForExcelAccu, gItem[0], gItem[1])
            return accumulateDistribution
        else:
            raise Exception


    def accumulateTidy(self, newAccumulateList, objList, accuStart, accuEnd):
        unit1 = []
        for i in range(0, 42):
            unit1.append("")
        
        unit1[0] = objList[accuStart][0] + " to " + objList[accuEnd][0]
        unit1[1] = "weekDay"

        t = accuStart
        while t <= accuEnd:
            for n in range(2, len(objList[t])):
                if unit1[n] == "" and objList[t][n] == "$":
                    unit1[n] = "$"
            t += 1
        newAccumulateList.append(unit1)


    def exportDistribution(self, exportData):
        """#we use desktop path as export path now, but if this class is used for website, this function should be modified to make 
        organize all export necessary data into json format and then it can be used to send back to front-end.
        """
        try:
            # get path of desktop 
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
            deskPath = winreg.QueryValueEx(key, "Desktop")[0]    
            #create excel file and write data into excel
            excelCreate = xlsxwriter.Workbook(deskPath+ "\L Distribution plus.xlsx")   #"{exportPath}
            workSheet = excelCreate.add_worksheet("Distribution")
            for j in range(0, len(exportData)):
                workSheet.write_row(j, 0, exportData[j])
                j += 1
            excelCreate.close()
            return "Finished!"
        except:
            return "Error!"


#Data----------------------------------------------------------------------------------------------------------
originalAll= [
         {"date":"16/08/2023", "wD":"Wednesday", "lo":[7,17,19,29,36,38], "bo":20}, 
         {"date":"12/08/2023", "wD":"Saturday", "lo":[15,19,20,23,31,33], "bo":8}, 
         {"date":"9/08/2023", "wD":"Wednesday", "lo":[4,13,14,34,35,40], "bo":15}, 
         {"date":"5/08/2023", "wD":"Saturday", "lo":[18,23,24,26,28,32], "bo":16}, 
         {"date":"2/08/2023", "wD":"Wednesday", "lo":[6,23,25,27,28,32,], "bo":17}, 
         {"date":"29/07/2023", "wD":"Saturday", "lo":[4,10,13,18,21,34], "bo":40}, 
         {"date":"26/07/2023", "wD":"Wednesday", "lo":[17,19,23,25,27,37], "bo":13}, 
         {"date":"22/07/2023", "wD":"Saturday", "lo":[3,4,12,22,24,25], "bo":10}, 
         {"date":"19/07/2023", "wD":"Wednesday", "lo":[6,20,23,28,35,38], "bo":2}, 
         {"date":"15/07/2023", "wD":"Saturday", "lo":[7,11,15,21,24,34], "bo":6}, 
         {"date":"12/07/2023", "wD":"Wednesday", "lo":[8,22,29,34,36,37], "bo":11}, 
         {"date":"8/07/2023", "wD":"Saturday", "lo":[6,8,10,18,25,32], "bo":2}, 
         {"date":"5/07/2023", "wD":"Wednesday", "lo":[4,7,26,29,36,38], "bo":23}, 
         {"date":"1/07/2023", "wD":"Saturday", "lo":[9,23,24,25,30,34], "bo":10}
          ]





#Action----------------------------------------------------------------------------------------------------------
disGenerator = DistributionGenerate()

firstSortedData = disGenerator.sortBasedOnDate(originalAll)
secondTidiedData = disGenerator.tidyForExcel(firstSortedData)
thirdAccumulatedData = disGenerator.accumulationOrganize(secondTidiedData, 1, 5)
fourthExportData = secondTidiedData + thirdAccumulatedData
fifthExportAction = disGenerator.exportDistribution(fourthExportData)

print(fifthExportAction)

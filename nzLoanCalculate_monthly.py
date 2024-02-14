import copy
import csv
import winreg

#*****************************Defination********************************************************
class LoanCaucuale:
    def __init__(self) -> None:
        pass
    
    
    def averageBaseReturn(self, downPay, downPayPercent_initial, loanPart_initial, loanMonths, fixedInterest_monthly, yearlyInterest_monthly):
        """Average return base****************************"""
        
        final_results = []
        exportFile = "AverageBase_llllCalculate_monthly.csv"
        final_results.append(["Same monthly base", "{}".format(str(downPay)), "{}".format(str(loanPart_initial)), "{}".format(str(downPayPercent_initial))])
        final_results.append(["Month", "MonthlyReturn", "MonthlyBase", "MonthlyInterest", "InterestReturn", "LoanRest"])
        monthlyBase = loanPart_initial / loanMonths
        interestReturn = 0
        monthlyReturn = 0

        loanPart_rest = loanPart_initial

        returnMonths = 1
        interest_current = 0
        while loanPart_rest > 0:
            temList = []
            if returnMonths <= 36:
                interest_current = fixedInterest_monthly
            else:
                interest_current = yearlyInterest_monthly

            monthlyInterest = loanPart_rest * interest_current
            monthlyReturn = monthlyBase + monthlyInterest
            interestReturn = interestReturn + monthlyInterest

            loanPart_rest = loanPart_rest - monthlyBase

            # print("Month: {}".format(str(returnMonths)))
            # print("MonthlyReturn: {}".format(str(monthlyReturn)))
            # print("MonthlyBase: {}".format(str(monthlyBase)))
            # print("MonthlyInterest: {}".format(str(monthlyInterest)))
            # print("InterestReturn: {}".format(str(interestReturn)))
            # print("LoanRest: {}".format(str(loanPart_rest)))
            # print("*************************************************************\n")
            temList.append(returnMonths)
            temList.append(monthlyReturn)
            temList.append(monthlyBase)
            temList.append(monthlyInterest)
            temList.append(interestReturn)
            temList.append(loanPart_rest)


            final_results.append(temList)

            returnMonths += 1

        self.exportResult(exportFile, final_results)
        print("Same monthly base export successfully!")


    def sameMonthTotalReturn(self, downPay, downPayPercent_initial, loanPart_initial, loanMonths, fixedInterest_monthly, yearlyInterest_monthly):
        """Same monthly return total --> 
        monthlyBase = (loanPart_initial * interest_current * (1 + interest_current) ** loanMonths) / ((1 + interest_current) ** loanMonths - 1)"""

        final_results = []
        exportFile = "AverageTotal_llllCalculate_monthly.csv"
        final_results.append(["Same monthly total", "{}".format(str(downPay)), "{}".format(str(loanPart_initial)), "{}".format(str(downPayPercent_initial))])
        final_results.append(["Month", "MonthlyReturn", "MonthlyBase", "MonthlyInterest", "InterestReturn", "LoanRest"])
        
        interestReturn = 0

        loanPart_rest = loanPart_initial

        returnMonths = 1
        interest_current = 0
        while loanPart_rest > 0:
            temList_sameTotal = []
            if returnMonths <= 36:
                interest_current = fixedInterest_monthly
            else:
                interest_current = yearlyInterest_monthly
            # interest_current = fixedInterest_monthly

            monthlyReturn = (loanPart_initial * interest_current * (1 + interest_current) ** loanMonths) / ((1 + interest_current) ** loanMonths - 1)
            monthlyInterest = loanPart_rest * interest_current
            monthlyBase = monthlyReturn - monthlyInterest

            if loanPart_rest < monthlyBase:
                monthlyBase = loanPart_rest
                monthlyReturn = monthlyInterest + monthlyBase
                
            interestReturn = interestReturn + monthlyInterest
            loanPart_rest = loanPart_rest - monthlyBase

            temList_sameTotal.append(returnMonths)
            temList_sameTotal.append(monthlyReturn)
            temList_sameTotal.append(monthlyBase)
            temList_sameTotal.append(monthlyInterest)
            temList_sameTotal.append(interestReturn)
            temList_sameTotal.append(loanPart_rest)


            final_results.append(temList_sameTotal)

            returnMonths += 1
        
        self.exportResult(exportFile, final_results)
        print("Same monthly total export successfully!")


    def exportResult(self, filename, results):
        # get desktop path
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
        deskTopPath = winreg.QueryValueEx(key, "Desktop")[0]

        #getfullPath
        fullPath = deskTopPath + "\\" + filename
        print(fullPath)
        newFile = open(fullPath, "w", newline='')
        newWriter = csv.writer(newFile)
        newWriter.writerows(results)



#******************************Parameters********************************************************
totalPrice_initial_p = 850000     # adjust
# downPayPercent_initial_p = 0.2   # adjust
# downPay_initial_p = totalPrice_initial_p *  downPayPercent_initial_p

downPay_initial_p = 140000
downPayPercent_initial_p = downPay_initial_p / totalPrice_initial_p

loanPercent_initial_p = 1 - downPayPercent_initial_p
loanPart_initial_p = totalPrice_initial_p - downPay_initial_p
loanYears_p = 30
loanMonths_p = loanYears_p * 12
fixedInterest_p = 0.068
fixedInterest_monthly_p = fixedInterest_p / 12
yearlyInterest_p = 0.0875
yearlyInterest_monthly_p = yearlyInterest_p / 12

#*********************************EXecute*******************************************************
# if downPayPercent_initial_p == 0.2 and loanPart_initial_p > 880000:
#     print("DownPay is not enough! \nDownPay: {}\nLoan: {}\n --- {}".format(str(downPay_initial_p), str(loanPart_initial_p), str(downPayPercent_initial_p*100)+"%"))
# elif downPayPercent_initial_p == 0.15 and loanPart_initial_p > 700000:
#     print("DownPay is not enough! \nDownPay: {}\nLoan: {}\n --- {}".format(str(downPay_initial_p), str(loanPart_initial_p), str(downPayPercent_initial_p*100)+"%"))
# elif downPayPercent_initial_p == 0.1 and loanPart_initial_p > 650000:
#     print("DownPay is not enough! \nDownPay: {}\nLoan: {}\n --- {}".format(str(downPay_initial_p), str(loanPart_initial_p), str(downPayPercent_initial_p*100)+"%"))
# else:
#     clacualtors = LoanCaucuale()  

#     clacualtors.averageBaseReturn(downPay_initial_p, downPayPercent_initial_p, loanPart_initial_p, loanMonths_p, fixedInterest_monthly_p, yearlyInterest_monthly_p)
#     clacualtors.sameMonthTotalReturn(downPay_initial_p, downPayPercent_initial_p,loanPart_initial_p, loanMonths_p, fixedInterest_monthly_p, yearlyInterest_monthly_p)

clacualtors = LoanCaucuale()  
clacualtors.averageBaseReturn(downPay_initial_p, downPayPercent_initial_p, loanPart_initial_p, loanMonths_p, fixedInterest_monthly_p, yearlyInterest_monthly_p)
clacualtors.sameMonthTotalReturn(downPay_initial_p, downPayPercent_initial_p,loanPart_initial_p, loanMonths_p, fixedInterest_monthly_p, yearlyInterest_monthly_p)






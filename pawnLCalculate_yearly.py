import copy
import csv
import winreg

loan = 600000
limateYears = 10
interest_month = 0.0035
interest_year = interest_month * 12
rB_percent = 0.05
rT_month_beforeFinal = 10000


rB_total = 0 
rI_total = 0
years = 0
rT_year = 0
rT_year_beforeFinal = rT_month_beforeFinal * 12  # set by ourselves(yearly RMB)
finalReturn = 0
restLoan = copy.deepcopy(loan)

exportFile = "pawnCalculate_yearly.csv"
c_results = []
c_results.append(["Return years", "Current Year Total", "Current Year Interest", "RestLoan", "Total return", "Total Interest"])


maxReturn_b_and_i = loan * rB_percent + loan * interest_year  #4600
print("maxReturn_b_and_i: {}".format(str(maxReturn_b_and_i)))
print("Max Interest: {}\n".format(str(loan * interest_year)))

if rT_year_beforeFinal >= maxReturn_b_and_i:
    while rB_total < loan:
        temList = []
        rI_year = restLoan * interest_year
        rI_total = rI_total + rI_year
        if years >= limateYears-1:
            if finalReturn == 0:
                finalReturn = copy.deepcopy(restLoan)
            rB_year = finalReturn
        elif restLoan <= rT_year_beforeFinal:
            rB_year = copy.deepcopy(restLoan)
        else:
            rB_year = rT_year_beforeFinal - rI_year
        rB_total = rB_total + rB_year
        restLoan = restLoan - rB_year
        rT_year = rB_year + rI_year

        years += 1
        temList = [str(years), str(rT_year), str(rI_year),str(restLoan), str(rB_total), str(rI_total)]
        print("Return years: {}\nCurrent Year Total: {}\nCurrent Year Interest: {}\nRestLoan: {}\nTotal return: {}\nTotal Interest: {}\n".format(str(years), str(rT_year), str(rI_year),str(restLoan), str(rB_total), str(rI_total)))
        c_results.append(temList)
else:
    print("Monthly payment is too low to finish the return under limated years!")


def exportResult(filename, results):
    # get desktop path
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    deskTopPath = winreg.QueryValueEx(key, "Desktop")[0]

    #getfullPath
    fullPath = deskTopPath + "\\" + filename
    print(fullPath)
    newFile = open(fullPath, "w", newline='')
    newWriter = csv.writer(newFile)
    newWriter.writerows(results)



exportResult(exportFile, c_results)



    
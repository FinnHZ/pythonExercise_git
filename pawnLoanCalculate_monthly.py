import copy
import csv
import winreg

loan = 600000
limateYears = 10
interest_month = 0.0035
rB_percent = 0.05      #base return monthly
rT_month_beforeFinal = 10000  # set by ourselves(monthly RMB)



rB_total = 0 
rI_total = 0
months = 0
rT_month = 0
finalReturn = 0
restLoan = copy.deepcopy(loan)

exportFile = "pawnCalculate_monthly.csv"
c_results = []
c_results.append(["Return months", "Return years", "Current Month Total", "Current Month Interest", "RestLoad", "Total return", "Total Interest"])


maxReturn_b_and_i = loan * rB_percent / 12 + loan * interest_month  #4600
print("maxReturn_b_and_i: {}".format(str(maxReturn_b_and_i)))
print("Max Interest: {}\n".format(str(loan * interest_month)))

if rT_month_beforeFinal >= maxReturn_b_and_i:
    while rB_total < loan:
        temList = []
        rI_month = restLoan * interest_month
        rI_total = rI_total + rI_month
        if months >= (limateYears-1) * 12:
            if finalReturn == 0:
                finalReturn = copy.deepcopy(restLoan)
            rB_month = finalReturn / 12
        elif restLoan <= rT_month_beforeFinal:
            rB_month = copy.deepcopy(restLoan)
        else:
            rB_month = rT_month_beforeFinal - rI_month
        rB_total = rB_total + rB_month
        restLoan = restLoan - rB_month
        rT_month = rB_month + rI_month

        months += 1
        temList = [str(months), str(months/12), str(rT_month), str(rI_month),str(restLoan), str(rB_total), str(rI_total)]
        print("Return months: {}\nReturn years: {}\nCurrent Month Total: {}\nCurrent Month Interest: {}\nRestLoad: {}\nTotal return: {}\nTotal Interest: {}\n".format(str(months), str(months/12), str(rT_month), str(rI_month),str(restLoan), str(rB_total), str(rI_total)))
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



    
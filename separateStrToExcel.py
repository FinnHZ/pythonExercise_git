import xlsxwriter
import winreg


#Input Area>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
aimString = 'Tamb, start_duration, dutyState, onTime, startPerHour, scaleFactor, vTO, formFactor, rT,\
rjc180sinAC_original, rjc1_original, cjc1_original, rjc2_original, cjc2_original,\
rjc3_original, cjc3_original, rjc4_original, cjc4_original, rjc5_original, cjc5_original,\
avgPower, rcs_init, ccs_init, rsa_init, csa_init, runTimes'

splitFlag =","

endwaysFlag = 1  # 0 --> bent array ;   1 --> endways


#Function>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
exportDictory = winreg.QueryValueEx(key, "Desktop")[0]


spreadSheetCreate = xlsxwriter.Workbook(exportDictory+ "\separate.xlsx")   #"{exportPath}
workSheet = spreadSheetCreate.add_worksheet("separate")

wirteData = aimString.split(splitFlag)

try:
    if endwaysFlag == 0:
        workSheet.write_row(0, 0, wirteData)
    elif endwaysFlag == 1:
        wirteData = list(map(lambda x: [x], wirteData))  # transform to endways
        for j in range(0, len(wirteData)):
            workSheet.write_row(j, 0, wirteData[j])
            j += 1
    print("Successfully! Please check your desktop of computer!")
    spreadSheetCreate.close()
except KeyError:
    print(KeyError)
    spreadSheetCreate.close()





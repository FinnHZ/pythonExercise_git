import os
import csv
import time


paraDOCpath = "./modbusCommunicate/static/document/paraDOCpath.csv"
measureDOCpath = "./modbusCommunicate/static/document/measureDOCpath.csv"
referDOCpath = "./modbusCommunicate/static/document/referDOCpath.csv"


# Input settings-----------------------------------------------------------
userInterface = [
    ["StarterState","604", "0", "4", "0", "Para",   #[name, register, bitStart, bitEnd, isSingle, monitorType, details]
     [
        ["0", "Reserved"],
        ["1", "Ready"],
        ["2", "Starting"],
        ["3", "Running"],
        ["4", "Stopping"],
        ["5", "Not Ready"],
        ["6", "Tripped"],
        ["7", "Programming mode"],  
        ["8", "Jog forward"],
        ["9", "Jog reverse"]
        ]],
    ["TripCode","619", "0", "7", "0", "Para", 
     [
        ["1", "Excess start time"],
        ["2", "Motor overload"],
        ["3", "Motor thermistor"],
        ["4", "Current imbalance"],
        ["5", "Frequency"], 
        ["6", "Phase sequence"], 
        ["7", "Overcurrent"],       
        ["8", "Power loss"], 
        ["9", "Undercurrent"], 
        ["10", "Heatsink overtemperature"],   
        ["11", "Motor connection"],
        ["12", "Input A trip"],
        ["13", "FLC too high"],
        ["14", "Unsupported option"], 
        ["15", "Communications card fault"],
        ["16", "Network communications"],
        ["18", "Overvoltage"],
        ["19", "Undervoltage"],
        ["20", "Ground fault"],
        ["23", "Parameter out of Range"],
        ["24", "Input B trip"],
        ["26", "L1 phase loss"],
        ["27", "L2 phase loss"],
        ["28", "L3 phase loss"],
        ["29", "L1-T1 shorted"],
        ["30", "L2-T2 shorted"],
        ["31", "L3-T3 shorted"],
        ["33", "Time-overcurrent (Bypass overload)"],
        ["34", "SCR overtemperature"],
        ["35", "Battery/clock"],
        ["36", "Thermistor circuit"],      
        ["47", "Over power"],
        ["48", "Under power"],
        ["56", "Keypad disconnected"], 
        ["57", "Zero speed detect"], 
        ["58", "SCR ITSM"], 
        ["59", "Instantaneous overcurrent"],
        ["60", "Rating capacity"],
        ["70", "Current Read Err L1"],
        ["71", "Current Read Err L2"],
        ["72", "Current Read Err L3"],
        ["74", "Motor connection T1"],
        ["75", "Motor connection T2"],
        ["76", "Motor connection T3"],
        ["77", "Firing fail P1"],
        ["78", "Firing fail P2"],
        ["79", "Firing fail P3"],
        ["80", "VZC Fail P1"],
        ["81", "VZC Fail P2"],
        ["82", "VZC Fail P3"],
        ["83", "Low Control Volts"],
        ["84", "Internal fault 84"],   
        ["85", "Internal fault 85"],
        ["86", "Internal fault 86"], 
        ["87", "Internal fault 87"],
        ["88", "Internal fault 88"],
        ["89", "Internal fault 89"],
        ["90", "Internal fault 90"],
        ["91", "Internal fault 91"],
        ["92", "Internal fault 92"],
        ["93", "Internal fault 93"],
        ["94", "Internal fault 94"],
        ["95", "Internal fault 95"],
        ["96", "Internal fault 96"],
        ["255","No trip"]
    ]],
    ["Initialisation","604", "", "6", "1", "Para", 
     [
        ["0","Unintiallised"],
        ["1","Intiallised"]
     ]],
    ["CommandSource","604", "", "7", "1", "Para", 
     [
        ["0","Remote Keypad, Digital Inputs, Clock"],
        ["1","Network"]
     ]],
    ["ParametersChange","604", "", "8", "1", "Para", 
     [
        ["0","Parameter(s) have changed since last parameter read"],
        ["1","No parameter(s) have changed"]
     ]],
    ["PhaseSequence","604", "", "9", "1", "Para", 
     [
        ["0","Negative phase sequence"],
        ["1","Postive phase sequence"]
     ]],
    ["Versions_Product","600", "9", "15", "0", "Para", 
     [
        ["1", "MCD3000"],
        ["2", "IMS2"],
        ["3", "TMS7"],
        ["4", "Jake"],
        ["5", "MVS"],
        ["6", "EMX3"],
        ["7", "MCD500"],
        ["8", "Digistart"],
        ["9", "Jane"],
        ["10", "Aston"],
        ["11", "MVS Multi"],
        ["12", "EMX4e"],
        ["13", "EMX4i"] 
     ]],
    ["Versions_Model","601", "8", "15", "0", "Para", 
     [
        ["1", "F1-A"],
        ["2", "F1-B"],
        ["3", "F1-C"],
        ["4", "F1-D-ph"],
        ["5", "F1-D"],
        ["6", "F1-E-ph"],
        ["7", "F1-E"],
        ["8", "F1-F"],
        ["9", "F2-A-ph1"],
        ["10", "F2-A-ph2"],
        ["11", "F2-A"],
        ["12", "F2-B"],
        ["13", "F3-A-ph"],
        ["14", "F3-A"],
        ["15", "F3-B"],
        ["16", "F4-A-ph"],
        ["17", "F4-A"]
     ]],
    ["PowerScale","608", "12", "13", "0", "Para", 
     [
        ["0", "Multiply power by 10 to ger W"],
        ["1", "Multiply power by 100 to ger W"],
        ["2", "Power(kw)"],
        ["3", "Multiply power by 10 to ger kW"]    
     ]],
    ["DigitalInput_StartStop","618", "", "0", "1", "Para", 
     [
        ["0", "Open"],
        ["1", "Closed(shorted)"]
     ]],
    ["DigitalInput_Reserved","618", "", "1", "1", "Para", 
     [
        ["0", "Open"],
        ["1", "Closed(shorted)"]
     ]],
    ["DigitalInput_Reset","618", "", "2", "1", "Para", 
     [
        ["0", "Open"],
        ["1", "Closed(shorted)"]
     ]],
    ["DigitalInput_InputA","618", "", "3", "1", "Para", 
     [
        ["0", "Open"],
        ["1", "Closed(shorted)"]
     ]],
    ["DigitalInput_InputB","618", "", "4", "1", "Para", 
     [
        ["0", "Open"],
        ["1", "Closed(shorted)"]
     ]],
    ["Average3phRmsCurrent","605", "0", "13", "0", "Val", []],
    ["Average3phRmsVoltage","610", "0", "13", "0", "Val", []],
    ["CurrentMotorFLC","606", "0", "9", "0", "Val", []],
    ["MotorThermalModel","607", "0", "7", "0", "Val", []],
    ["PowerFactor","609", "0", "7", "0", "Val", []],
    ["Current_P1","611", "0", "13", "0", "Val", []],
    ["Current_P2","612", "0", "13", "0", "Val", []],
    ["Current_P3","613", "0", "13", "0", "Val", []],
    ["Voltage_P1","614", "0", "13", "0", "Val", []],
    ["Voltage_P2","615", "0", "13", "0", "Val", []],
    ["Voltage_P3","616", "0", "13", "0", "Val", []],
    ["Versions_Binary","600", "0", "5", "0", "Val", []],
    ["Versions_ParamList_major","617", "8", "15", "0", "Val", []],
    ["Versions_ParamList_minor","617", "0", "7", "0", "Val", []]
]


# Process input-----------------------------------------------------------
productParaItems = {}
productMeasureItems = {}
processedSettingsRefer = {}

for i in range(0, len(userInterface)):
    p_tem = []
    if userInterface[i][5] == "Para":
        if userInterface[i][4] == "0":
            p_tem = [userInterface[i][1], str(15-int(userInterface[i][3])), str(16-int(userInterface[i][2]))]
        if userInterface[i][4] == "1":
            p_tem = [userInterface[i][1], str(15-int(userInterface[i][3])), str(15-int(userInterface[i][3])+1)]
        
        productParaItems[userInterface[i][0]] = p_tem
        processedSettingsRefer[userInterface[i][0]] = userInterface[i][6]
    
    elif userInterface[i][5] == "Val":
        if userInterface[i][4] == "0":
            p_tem = [userInterface[i][1], str(15-int(userInterface[i][3])), str(16-int(userInterface[i][2]))]
        if userInterface[i][4] == "1":
            p_tem = [userInterface[i][1], str(15-int(userInterface[i][3])), str(15-int(userInterface[i][3])+1)]
        
        productMeasureItems[userInterface[i][0]] = p_tem




# result save and read-----------------------------------------------------------
print("Save para settings") #----------------------------------------------------

newParaItemsList = []
for key1 in productParaItems:
   tem_para = []
   tem_para.append(key1)
   for item1 in productParaItems[key1]:
       tem_para.append(item1)
   newParaItemsList.append(tem_para)

os.remove(paraDOCpath)
fileSave_para = open(paraDOCpath, 'w', newline='')
fileSave_para_writer = csv.writer(fileSave_para)
fileSave_para_writer.writerows(newParaItemsList)
fileSave_para.close()

time.sleep(1)


print("Read para settings") #----------------------------------------------------

file_para = open(paraDOCpath, "r")
fileContentList_para = list(csv.reader(file_para))

settingParaDict = {}
for item_p in fileContentList_para:
      isSingleFlag_p = int(item_p[3]) - int(item_p[2])
      if isSingleFlag_p == 1:
         settingParaDict[item_p[0]] = [item_p[1], "", str(15-int(item_p[2]))]
      else:
         settingParaDict[item_p[0]] = [item_p[1], str(16-int(item_p[3])), str(15-int(item_p[2]))]
      # if item_p[0] != "":
      #    settingParaDict[item_p[0]] = [item_p[1], item_p[2], item_p[3]]

file_para.close()



print(settingParaDict)

print("ParaItems finished------------------------------------------------------------------------------------------------")





print("Save measure settings") #----------------------------------------------------

newMeasureItemsList = []
for key2 in productMeasureItems:
   tem_measure = []
   tem_measure.append(key2)
   for item2 in productMeasureItems[key2]:
       tem_measure.append(item2)
   newMeasureItemsList.append(tem_measure)

os.remove(measureDOCpath)
fileSave_measure = open(measureDOCpath, 'w', newline='')
fileSave_measure_writer = csv.writer(fileSave_measure)
fileSave_measure_writer.writerows(newMeasureItemsList)
fileSave_measure.close()

time.sleep(1)


print("Read measure settings") #----------------------------------------------------

file_measure = open(measureDOCpath, "r")
fileContentList_measure = list(csv.reader(file_measure))

settingMeasureDict = {}
for item_m in fileContentList_measure:
      isSingleFlag_m = int(item_m[3]) - int(item_m[2])
      if isSingleFlag_m == 1:
         settingMeasureDict[item_m[0]] = [item_m[1], "", str(15-int(item_m[2]))]
      else:
         settingMeasureDict[item_m[0]] = [item_m[1], str(16-int(item_m[3])), str(15-int(item_m[2]))]

file_measure.close()



print(settingMeasureDict)

print("MeasureItems finised------------------------------------------------------------------------------------------------")




print("Save settingsRefer settings") #----------------------------------------------------

newReferItemsList = []
for key3 in processedSettingsRefer:
   newReferItemsList.append([key3])
   for key3_item in processedSettingsRefer[key3]:
      newReferItemsList.append(key3_item)


os.remove(referDOCpath)
fileSave_refer = open(referDOCpath, 'w', newline='')
fileSave_refer_writer = csv.writer(fileSave_refer)
fileSave_refer_writer.writerows(newReferItemsList)
fileSave_refer.close()

time.sleep(1)


print("Read settingsRefer settings") #----------------------------------------------------

file_refer = open(referDOCpath, "r")
fileContentList_refer = list(csv.reader(file_refer))

settingReferDict = {}
currentKEY = ""

for item_r in fileContentList_refer:
   if len(item_r) == 1:
      currentKEY = item_r[0]
      settingReferDict[currentKEY] = {}
   elif len(item_r) == 2:
      settingReferDict[currentKEY][item_r[0]] = item_r[1]


file_refer.close()


print(settingReferDict)

print("SettingsRefer finished------------------------------------------------------------------------------------------------")







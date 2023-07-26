
# from pyModbusTCP.client import ModbusClient
# c = ModbusClient(host="localhost", port=502, debug=True)

from pymodbus.client import ModbusTcpClient
import time
import struct
from modbusRtuRefer import modbusRtuRefer



client = ModbusTcpClient(host="10.123.162.10", port=502, debug=False)

print("1111111111111", client.connect())
while True:
    testStateClient = client.read_holding_registers(address = 0, count = 100, slave = 1)  
    print("222222222222222222", testStateClient)
    encodeObj = testStateClient.encode()
    encodeObj_str = str(encodeObj)
    print("3333333333333333333333", encodeObj_str)
    time.sleep(0.5)

            


# reigster40600Start = {
#     "600": None, "601": None, "602": None, "603": None, "604": None, "605": None, "606": None, "607": None, 
#     "608": None, "609": None, "610": None, "611": None, "612": None, "613": None, "614": None, "615": None, 
#     "616": None, "617": None, "618": None, "619": None, "620": None, "621": None, "622": None, "623": None, 
#     "624": None, "625": None, "626": None, "627": None, "628": None, "629": None, "630": None, "631": None
#     }

# productParaItems = {
#     "StarterState":None,
#     "TripCode":None,
#     "Initialisation":None,
#     "CommandSource":None,
#     "ParametersChange":None,
#     "PhaseSequence":None,
#     "Versions_Product":None,
#     "Versions_Model":None,
#     "PowerScale": None,
#     "DigitalInput_StartStop": None,
#     "DigitalInput_Reserved": None,
#     "DigitalInput_Reset": None,
#     "DigitalInput_InputA": None,
#     "DigitalInput_InputB": None
# }


# productMeasureItems = {
#     "Average3phRmsCurrent":None,
#     "Average3phRmsVoltage":None,
#     "CurrentMotorFLC":None,
#     "MotorThermalModel":None,
#     "PowerFactor":None,
#     "Current_P1":None,
#     "Current_P2":None,
#     "Current_P3":None,
#     "Voltage_P1":None,
#     "Voltage_P2":None,
#     "Voltage_P3":None,
#     "Versions_Binary":None,
#     "Versions_ParamList_major":None,
#     "Versions_ParamList_minor":None
# }



# #The dictionaries belwo will be imported from user interface file.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# productParaItems_diagram = {'StarterState': ['604', '11', '16'], 'TripCode': ['619', '8', '16'], 'Initialisation': ['604', '9', '10'], 'CommandSource': ['604', '8', '9'], 'ParametersChange': ['604', '7', '8'], 'PhaseSequence': ['604', '6', '7'], 'Versions_Product': ['600', '0', '7'], 'Versions_Model': ['601', '0', '8'], 'PowerScale': ['608', '2', '4'], 'DigitalInput_StartStop': ['618', '15', '16'], 'DigitalInput_Reserved': ['618', '14', '15'], 'DigitalInput_Reset': ['618', '13', '14'], 'DigitalInput_InputA': ['618', '12', '13'], 'DigitalInput_InputB': ['618', '11', '12']}
# productMeasureItems_diagram = {'Average3phRmsCurrent': ['605', '2', '16'], 'Average3phRmsVoltage': ['610', '2', '16'], 'CurrentMotorFLC': ['606', '6', '16'], 'MotorThermalModel': ['607', '8', '16'], 'PowerFactor': ['609', '8', '16'], 'Current_P1': ['611', '2', '16'], 'Current_P2': ['612', '2', '16'], 'Current_P3': ['613', '2', '16'], 'Voltage_P1': ['614', '2', '16'], 'Voltage_P2': ['615', '2', '16'], 'Voltage_P3': ['616', '2', '16'], 'Versions_Binary': ['600', '10', '16'], 'Versions_ParamList_major': ['617', '0', '8'], 'Versions_ParamList_minor': ['617', '8', '16']}
# #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<








# #**************************************************************************************************************
# # GET STATE: read_holding_registers(address=1, count=3, slave=1)"""
# commandNum_str = None
# stateNum_str = None

# encodeObj_str_initial = None
# is_First = True


# countNUm = 32


# while True:
#     try:
#         # client.write_register(address=)

#         testStateClient = client.read_input_registers(address=599, count=countNUm, slave=1)
#         encodeObj = testStateClient.encode()
#         #1) The result(encodeObj) will be shown as binary(hex) style.
#         #2) Every 1 hex location is 1 byte, we also can look it as 16 bits.
#         #3) Every 1 register have only 2 bytes.
#         #4) In terms of the knowledge above and instruction of the product, we can make a example like below:

#         """ 
#         As the regulation of modbus-RTU, different register range should be read by different command, so we use 
#         'read_holding_registers' based on the instruction of the product.
#         00001 - 09999	Coil	1 bit	Read-write
#         10001 - 19999	Discrete input	1 bit	Read-only
#         30001 - 39999	Input register	16 bits	Read-only
#         40001 - 49999	Holding register	16 bits	Read-write

#         Example:
#         1. As instrcution, if we want to get the starter state, we should get the value of 40604.
#         2. We just need to use 604 as the start address because we have already use 'read_holding_registers' to limit the read range into '40001 - 49999'.
#         3. We only need 1 register, so we only need 2 bytes  --> 2 hex value, so the count of register shoud be 1
#         4. We only have 1 device, so the value of 'slave' should be 1
        
#         so we can use the formula: testStateClient = client.read_holding_registers(address=604, count=1, slave=1)
#         however, the design of the instruction may made some mistake, so all the address of real use should be less 1 than the address of instruction
#         so, the final formula should be: 
#         --------->>   testStateClient = client.read_holding_registers(address=603, count=1, slave=1)
        
#         then, we will get a binary result : b'\x02\xff\x01'  
#         1) 1st byte: We should ingnore the first byte, because the first byte is a number indicate you got how many byte here.
#         2) 2nd byte: This is from 8th to 15th bit location(actually, I didn't find the use at the moment.)
#                       a) the 8th can indicate the parameter change 
#                       b) the 9th can indicate the phase state(Negative/Postive)
#                       c) others reserved(not use at the moment)             
#         3) 3rd byte: It indicate the state of the starter. The detail about that from instruction like below:
#             0 = Reserverd
#             1 = Ready
#             2 = Starting
#             3 = Running
#             4 = Stopping
#             5 = Not ready
#             6 = Tripped
#             7 = Programming
#             8 = Jog forward
#             9 = Jog revers

#         """
        

#         encodeObj_str = str(encodeObj)
#         testUNPACK_list = []

#         if encodeObj_str_initial != encodeObj_str:
#             # print(encodeObj_str,":", len(encodeObj))
#             # print(encodeObj)
        
#             formatData = ">" + ((countNUm*2+1) * "B")
            
#             testUNPACK= struct.unpack(formatData, encodeObj[0:(countNUm*2+1)])
#             testUNPACK_list = list(testUNPACK)
#             # print(testUNPACK_list)       #----------------------1

#             testUNPACK_list.pop(0)
#             # print(testUNPACK_list)       #----------------------2

#             oneRegister = []
#             i_UNPACK = 0
#             i_register = 599
#             while i_UNPACK < len(testUNPACK_list):
#                 distribute_flag = i_UNPACK % 2
#                 if distribute_flag == 0:
#                     oneRegister = []
                
#                 # print(type(testUNPACK_list[i_UNPACK]))
#                 oneRegister.append(testUNPACK_list[i_UNPACK])

#                 if distribute_flag == 1:
#                     a = oneRegister[0]
#                     b = oneRegister[1]
#                     a1 = "{0:b}".format(a).zfill(8)
#                     b1 = "{0:b}".format(b).zfill(8)
#                     c = a1+b1

#                     reigster40600Start[str(i_register+1)] = c
#                     i_register += 1
#                 i_UNPACK += 1

                
#             print(reigster40600Start)


#             for k1 in productParaItems_diagram:   #for TCP, ParametersChange is reserved
#                 productParaItems[k1] = str(int(reigster40600Start[productParaItems_diagram[k1][0]][int(productParaItems_diagram[k1][1]):int(productParaItems_diagram[k1][2])], 2))

#             for k2 in productMeasureItems_diagram:
#                 productMeasureItems[k2] = str(int(reigster40600Start[productMeasureItems_diagram[k2][0]][int(productMeasureItems_diagram[k2][1]):int(productMeasureItems_diagram[k2][2])], 2))
     



#             # productParaItems["StarterState"] = str(int(reigster40600Start["604"][11:16], 2)) #In binary [0:4], but in string is in the opposite direction
#             # productParaItems["TripCode"] = str(int(reigster40600Start["619"][8:16], 2)) #In binary [0:7], but in string is in the opposite direction
#             # productParaItems["Initialisation"] = str(int(reigster40600Start["604"][9], 2)) #In binary [6], but in string is in the opposite direction          
#             # productParaItems["CommandSource"] = str(int(reigster40600Start["604"][8], 2)) #In binary [7], but in string is in the opposite direction
#             # productParaItems["ParametersChange"] = str(int(reigster40600Start["604"][7], 2)) #In binary [8], but in string is in the opposite direction
#             # productParaItems["PhaseSequence"] = str(int(reigster40600Start["604"][6], 2)) #In binary [9], but in string is in the opposite direction
#             # productParaItems["Versions_Product"] = str(int(reigster40600Start["600"][0:7], 2)) #In binary [9:15], but in string is in the opposite direction
#             # productParaItems["Versions_Model"] = str(int(reigster40600Start["601"][0:8], 2)) #In binary [8:15], but in string is in the opposite direction
#             # productParaItems["PowerScale"] = str(int(reigster40600Start["608"][2:4], 2)) #In binary [12:13], but in string is in the opposite direction
#             # productParaItems["DigitalInput_StartStop"] = str(int(reigster40600Start["618"][15], 2)) #In binary [0], but in string is in the opposite direction
#             # productParaItems["DigitalInput_Reserved"] = str(int(reigster40600Start["618"][14], 2)) #In binary [1], but in string is in the opposite direction
#             # productParaItems["DigitalInput_Reset"] = str(int(reigster40600Start["618"][13], 2)) #In binary [2], but in string is in the opposite direction
#             # productParaItems["DigitalInput_InputA"] = str(int(reigster40600Start["618"][12], 2)) #In binary [3], but in string is in the opposite direction
#             # productParaItems["DigitalInput_InputB"] = str(int(reigster40600Start["618"][11], 2)) #In binary [4], but in string is in the opposite direction



#             # productMeasureItems["Average3phRmsCurrent"] = str(int(reigster40600Start["605"][2:16], 2)) #In binary [0:13], but in string is in the opposite direction
#             # productMeasureItems["Average3phRmsVoltage"] = str(int(reigster40600Start["610"][2:16], 2)) #In binary [0:13], but in string is in the opposite direction
#             # productMeasureItems["CurrentMotorFLC"] = str(int(reigster40600Start["606"][6:16], 2)) #In binary [0:9], but in string is in the opposite direction
#             # productMeasureItems["MotorThermalModel"] = str(int(reigster40600Start["607"][8:16], 2)) #In binary [0:7], but in string is in the opposite direction
#             # productMeasureItems["PowerFactor"] = str(int(reigster40600Start["609"][8:16], 2)) #In binary [0:7], but in string is in the opposite direction
#             # productMeasureItems["Current_P1"] = str(int(reigster40600Start["611"][2:16], 2)) #In binary [0:13], but in string is in the opposite direction
#             # productMeasureItems["Current_P2"] = str(int(reigster40600Start["612"][2:16], 2)) #In binary [0:13], but in string is in the opposite direction
#             # productMeasureItems["Current_P3"] = str(int(reigster40600Start["613"][2:16], 2)) #In binary [0:13], but in string is in the opposite direction
#             # productMeasureItems["Voltage_P1"] = str(int(reigster40600Start["614"][2:16], 2)) #In binary [0:13], but in string is in the opposite direction
#             # productMeasureItems["Voltage_P2"] = str(int(reigster40600Start["615"][2:16], 2)) #In binary [0:13], but in string is in the opposite direction
#             # productMeasureItems["Voltage_P3"] = str(int(reigster40600Start["616"][2:16], 2)) #In binary [0:13], but in string is in the opposite direction
#             # productMeasureItems["Versions_Binary"] = str(int(reigster40600Start["600"][10:16], 2)) #In binary [0:5], but in string is in the opposite direction
#             # productMeasureItems["Versions_ParamList"] = str(int(reigster40600Start["617"][0:8], 2)) + "." + str(int(reigster40600Start["617"][8:16], 2)) #In binary [8:15]&[0:7], but in string is in the opposite direction. ??[9:16] should be the minor revision,


#             # print(modbusRefer["StarterState"])
# #draftttttttttttttttttttt>>>>>>>>>>>>>

#             print("*********************************************************************************")
#             for it_p in productParaItems:
#                 print(it_p, ": ", productParaItems[it_p], ", ", modbusRtuRefer[it_p].get(productParaItems[it_p]))  #!!!Important: If you want to get a default value(None) when you try to read a non-existent key, you should use : dictionary.get(key) instead of dictionary[key]
#                 # modbusRtuRefer will be imported from user interface file.
#             for it_m in productMeasureItems:
#                 print(it_m, ": ", productMeasureItems[it_m])
# #draftttttttttttttttttttt<<<<<<<<<<<

#         encodeObj_str_initial = encodeObj_str
#         time.sleep(2)
#     except AttributeError:
#         print("Please check the connection.")
#         if is_First == True:
#             is_First = False
#         else:
#             break


#             # try:
#             #     commandNum_int = int(str(encodeObj[6:7])[-2])
#             #     if (commandNum_int <= 6) and (commandNum_int >= 0):
#             #         commandNum_str = str(encodeObj[6:7])[-2]
#             #     else:
#             #         raise
#             #     print("Command Source: " + commandNum_str + "--" + commandSourceDict[commandNum_str])
#             # except:
#             #     print("There is some error with Command source")

#             # try:
#             #     stateNum_int = int(str(encodeObj[8:9])[-2])
#             #     if (stateNum_int <= 9) and (stateNum_int >= 0):
#             #         stateNum_str = str(encodeObj[8:9])[-2]
#             #     else:
#             #         raise
#             #     print("Starter State: " + stateNum_str + "--" + stateDict[stateNum_str])
#             # except:
#             #     print("There is some error with state of stater")
        
        

# #**************************************************************************************************************






# #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# #!!!!!important--2!!!!!!start and reset  (stop?)
# #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# # def mornitorState():
# #    # while True:
# #     #    print("state:" + str(client.state))
# #     #    # print("recv:" + str(client.recv(1024)))
# #     #    # testStateClient = client.read_coils(address=8, count=10, slave=1)  #address(8~243)
# #      #   # print(testStateClient)
# #      #   time.sleep(0.5)



# # monitorThread = threading.Thread(target=mornitorState) #, args=()
# # monitorThread.start()
# # timer_i = 0

# # while timer_i <5:
# #     time.sleep(1)
# #     timer_i += 1
# #     print(timer_i)


# # print("start command")
# # _result_1 = client.write_register(address=1, value=1, slave=1)
# # # _result_1 = client.write_register(address=1, value=43265, slave=1)
# # print("******************")
# # print(_result_1)


# # timer_j = 0

# # while timer_j <5:
# #     time.sleep(1)
# #     timer_j += 1
# #     print(timer_j)

# # print("reset command")
# # # _result_2 = client.send(b'\x01\x03\x00\xfc')

# # _result_2 = client.write_register(address=1, value=3, slave=1)
# # print("##################")
# # print(_result_2)
# # time.sleep(10)
# #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



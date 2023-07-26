from pymodbus.client import ModbusSerialClient
import time
import threading
import struct
import binascii
from modbusRtuRefer import modbusRtuRefer


client = ModbusSerialClient(method = "rtu", port = "COM8", stopbits = 2, bytesize = 8, parity = 'N', baudrate = 9600)
print("Connect------------------------------------------")
print(client.connect())



#**************************************************************************************************************
commandNum_str = None
stateNum_str = None
encodeObj_str_initial = None
is_First = True
countNUm = 1 #32
addressVal = 599
while True:
    try:
        # client.write_register(address=)
        testStateClient = client.read_input_registers(address=addressVal, count=countNUm, slave=1)  #address=599
        # testStateClient = client.read_holding_registers(address=599, count=countNUm, slave=1)  #address=599
        print(testStateClient)

        encodeObj = testStateClient.encode()
        print(encodeObj)

        str_tem = str(encodeObj).replace("b'@", "").split("\\")
        print(str_tem)

        time.sleep(2)
    except Exception as e:
        print("Please check the connection: ", e)
        if is_First == True:
            is_First = False
        else:
            break
#**************************************************************************************************************








#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#!!!!!important--2!!!!!!start and reset  (stop?)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def mornitorState():
#    while True:
#        print("state:" + str(client.state))
#        print("recv:" + str(client.recv(1024)))
#        testStateClient = client.read_coils(address=8, count=10, slave=1)  #address(8~243)
#        print(testStateClient)
#        time.sleep(0.5)



# monitorThread = threading.Thread(target=mornitorState) #, args=()
# monitorThread.start()

# time.sleep(5)
# print("start command")
# _result_1 = client.write_register(address=1, value=1, slave=1)
# print("******************")
# print(_result_1)




# time.sleep(5)
# print("reset command")
# _result_2 = client.write_register(address=4, value=1, slave=1)
# # print("##################")
# print(_result_2)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

















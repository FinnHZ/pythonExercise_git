from pymodbus.client import ModbusSerialClient
from pymodbus.client import ModbusTcpClient
import time
import threading
import struct
import binascii

client = ModbusSerialClient(method = "rtu", port = "COM3", stopbits = 1, bytesize = 8, parity = 'N', baudrate = 19200)
# client = ModbusTcpClient(host="192.168.0.2", port=502, debug=False)
print("1--", "Connect------------------------------------------")
print("2--", client.connect())
print("3--", client.connected)

print("4--", "Write------------------------------------------")
changeState = client.write_registers(address=0, slave=1, values=[2])
# changeState = client.write_register(address=0, value=9, slave=1)
print("5--", changeState)

#READ---------------------------------------------------------------------------------------------------------------
print("6--", "Read------------------------------------------")

countNUm = 1
testStateClient = client.read_holding_registers(address=2000, count=countNUm, slave=1) 
# testStateClient = client.read_input_registers(address=2000, count=countNUm, slave=1)


# loopFlag = 0
# while loopFlag < 9999:
#     try:
#         countNUm = 1
#         testStateClient = client.read_holding_registers(address=loopFlag, count=countNUm, slave=1) 
#         # testStateClient = client.read_input_registers(address=2000, count=countNUm, slave=1)
#         print("{}--".format(loopFlag), testStateClient)
#         loopFlag +=1
#     except:
#         loopFlag +=1

print("7--", testStateClient)
encodeObj = testStateClient.encode()
print("8--", encodeObj)



formatData = ">" + ((countNUm*2+1) * "B")

testUNPACK= struct.unpack(formatData, encodeObj[0:(countNUm*2+1)])
testUNPACK_list = list(testUNPACK)
print("9--", testUNPACK_list)       #----------------------1

testUNPACK_list.pop(0)
print("10--", testUNPACK_list)       #----------------------2





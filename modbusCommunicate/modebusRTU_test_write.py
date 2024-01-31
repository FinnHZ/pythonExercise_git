from pymodbus.client import ModbusSerialClient
import time
import threading
import struct
import binascii
from modbusRtuRefer import modbusRtuRefer
from typing import Any, List, Tuple, Union
from pymodbus.client import ModbusTcpClient

client = ModbusSerialClient(method = "rtu", port = "COM8", stopbits = 2, bytesize = 8, parity = 'N', baudrate = 9600)
# client = ModbusTcpClient(host="192.168.0.2", port=502, debug=False)


print("Connect------------------------------------------")
print(client.connect())




_result_2 = client.write_registers(address=1003, values=[0,1], slave=1)
print(_result_2)
encodeObj = _result_2.encode()
print(encodeObj)


#------------------------------------------------------------------------------------------------------------
#profibus try--------------
# print("##################")
# _result_2 = client.write_register(address=2, slave=1, value=0)   
# _result_2 = client.readwrite_registers(
#         read_address = 1,
#         read_count = 1,
#         write_address = 1,
#         values = Union[[1]],
#         slave = 1,
# )
# encodeObj = _result_2.encode()
# print(_result_2)
# print(encodeObj)

#------------------------------------------------------------------------------------------------------------

# print("##################")
# testStateClient = client.read_input_registers(address=0, count=5, slave=1)  #profibus getway: a0v1-a0v8   / (a0v5-a0v15)  /a0v17-a0v24  / a0v33-a0v40  / a0v49-a0v56.....
# encodeObj1 = testStateClient.encode()
# print(encodeObj1)


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

















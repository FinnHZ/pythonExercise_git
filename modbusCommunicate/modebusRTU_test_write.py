from pymodbus.client import ModbusSerialClient
import time
import threading
import struct
import binascii
from modbusRtuRefer import modbusRtuRefer
from typing import Any, List, Tuple, Union


client = ModbusSerialClient(method = "rtu", port = "COM8", stopbits = 2, bytesize = 8, parity = 'N', baudrate = 9600)
print("Connect------------------------------------------")
print(client.connect())




_result_2 = client.write_registers(address=1, values=[1,0], slave=1)
encodeObj = _result_2.encode()
print(_result_2)
print("##################")
print(encodeObj)


# _result_2 = client.write_register(address=1, value=3, slave=1)
# encodeObj = _result_2.encode()
# print(_result_2)
# print("##################")
# print(encodeObj)




#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

















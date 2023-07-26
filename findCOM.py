import serial
import time
import serial.tools.list_ports
from pymodbus.client import ModbusSerialClient


# Replace 'COM3' with the appropriate port name for your system
serial_port = 'COM9'
baud_rate = 9600

# Establish a connection to the serial port
ser = serial.Serial(serial_port, baud_rate, timeout=5)

# port_list = list(serial.tools.list_ports.comports())
# print(port_list)

abc = ser.write(b'\x01\x01\x01\xfd')
print(abc)


strtest = ""
for i in range(abc):
    strtest += ser.read().decode("utf-8")

print(strtest)






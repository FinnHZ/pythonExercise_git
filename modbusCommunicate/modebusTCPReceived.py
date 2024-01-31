from pymodbus.client import AsyncModbusTcpClient
import time
import struct
from modbusRtuRefer import modbusRtuRefer



client = AsyncModbusTcpClient(host="192.168.0.2", debug=False)
client.connect()

while True:
    result = client.re
    print(result)
    time.sleep(0.2)
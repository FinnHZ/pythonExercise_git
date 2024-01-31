from pymodbus.client import ModbusSerialClient
import time
import threading
import struct
import binascii
from modbusRtuRefer import modbusRtuRefer


client = ModbusSerialClient(method = "rtu", port = "COM8", stopbits = 2, bytesize = 8, parity = 'N', baudrate = 9600)
print("Connect------------------------------------------")
print(client.connect())

reigster40600Start = {}


#**************************************************************************************************************
commandNum_str = None
stateNum_str = None

encodeObj_str_initial = None
is_First = True


countNUm = 32 #32
i_address = 599
iUnpackMax = 1

while True:
    # try:
        # client.write_register(address=)
        testStateClient = client.read_input_registers(address=i_address, count=countNUm, slave=1)  #address=599
        # print(testStateClient)
        encodeObj = testStateClient.encode()
        # print(encodeObj)
        encodeObj_str = str(encodeObj)
        testUNPACK_list = []

        if encodeObj_str_initial != encodeObj_str:
            # print(encodeObj_str,":", len(encodeObj))
            print(encodeObj)
        
            formatData = ">" + ((countNUm*2+1) * "B")
            
            testUNPACK= struct.unpack(formatData, encodeObj[0:(countNUm*2+1)])
            testUNPACK_list = list(testUNPACK)
            print(testUNPACK_list)       #----------------------1

            testUNPACK_list.pop(0)
            print(testUNPACK_list)       #----------------------2

            oneRegister = []
            i_UNPACK = 0
            i_register = i_address
            


            while i_UNPACK < len(testUNPACK_list):
                distribute_flag = i_UNPACK % iUnpackMax  #2 --> one register, 4 ---> two register!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                if distribute_flag == 0:
                    oneRegister = []
                # print(testUNPACK_list[i_UNPACK])

                # print(type(testUNPACK_list[i_UNPACK]))
                oneRegister.append(testUNPACK_list[i_UNPACK])

                # print(oneRegister)

                if distribute_flag == iUnpackMax-1:

                    c = ''
                    for i in range(0, len(oneRegister)):
                        temByte = "{0:b}".format(oneRegister[i]).zfill(8)
                        c += temByte
                    reigster40600Start[str(i_register+1)] = c
                    i_register += 1
                i_UNPACK += 1

                
            print(reigster40600Start)

        encodeObj_str_initial = encodeObj_str
        time.sleep(2)
    # except AttributeError:
    #     print("Please check the connection.")
    #     if is_First == True:
    #         is_First = False
    #     else:
    #         break
#**************************************************************************************************************










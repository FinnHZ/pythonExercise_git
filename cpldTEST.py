import ctypes as ct
from ctypes import *


addr = "C:\\Phyton\\ChipProgUSB\\6_29_01\\ACI64.dll"


cpldDll = ct.windll.LoadLibrary(addr)



char = c_char
byte = c_byte                           #int
ubyte = c_ubyte

sss = ubyte(14)
ccc1 = char(64)
ccc2 = char(64)


cpldDll.ACI_Launch()
abc = cpldDll.ACI_GetConnection()

print(abc)

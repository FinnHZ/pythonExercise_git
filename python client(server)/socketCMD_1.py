#client.py
import socket

s = socket.socket()

host = "192.168.0.2" #socket.gethostname()  #this address is from the setting of soft starter, should be different from the computer(controller)'s IP, but should be in the same damain.
port = 4000  #this port is fixed based on the setting of soft starter
s.connect((host, port))


asciiCommand = b'\x01\x01\x01\xfd'   #!!!!!it works this is the ASCII form in python (\01  --> \x01) 

print("ASCCmd", asciiCommand)

sds = s.send(asciiCommand)
asciiVar = s.recv(1024)

print("receive:" ,asciiVar)
print("rec:" , sds)
# print("receiveASCII:" ,asciiVar.decode("ascii"))
# print("receiveUTF8:" ,asciiVar.decode(encoding="utf-8"))
# print("receiveInt:" ,int.from_bytes(asciiVar, "big"))

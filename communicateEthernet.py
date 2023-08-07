# import socket

# TCP_IP = '192.168.0.2'
# TCP_PORT = 4000

# # TCP_IP = '127.0.0.1'
# # TCP_PORT = 50212

# BUFFER_SIZE = 10  # Normally 1024, but we want fast response
# print("111111111111")
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print("22222222222")
# s.bind((TCP_IP, TCP_PORT))
# print("333333333333")

# s.listen(4)
# print("4444444444444")
# conn, addr = s.accept()
# print("55555555555555")

# print ('Connection address:', addr)
# print("6666666666666666")

# while 1:
#      print("7777777777")
#      data = conn.recv(BUFFER_SIZE)

#      if not data: 
#           break
#      print ("received data:", data)
#      print("88888888888")
#      conn.send(data)  # echo
#      print(data)
# conn.close()

# #*****************************************************************************************




#----- A simple TCP client program in Python using send() function -----

import socket

 

# Create a client socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 

# Connect to the server

clientSocket.connect(("192.168.0.2",4000))

 

# Send data to server

data = b"\01\01\01\fd"

clientSocket.send(data.encode())

 

# Receive data from server

dataFromServer = clientSocket.recv(1024)

 

# Print to the console

print(dataFromServer.decode())
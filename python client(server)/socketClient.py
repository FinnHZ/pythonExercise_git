#client.py
import socket

s = socket.socket()

host = "192.168.0.2" #socket.gethostname()  #this address should match with the address of server
port = 4000 #1234   #this port should match with the port of server

# host = "127.0.0.1" #socket.gethostname()  #this address should match with the address of server
# port = 1234 #1234   #this port should match with the port of server


s.connect((host, port))
print("receive:" ,s.recv(1024))
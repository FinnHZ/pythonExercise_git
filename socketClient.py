import socket

s = socket.socket()


host = "192.168.0.2"  #169.254.211.117
port = 4000

s.connect((host, port))
# s.send(b'\01\01\01\fd')

print("receive:", s.recv(1024))

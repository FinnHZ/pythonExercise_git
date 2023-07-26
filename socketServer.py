import socket

s = socket.socket()


host = "192.168.0.3" # "127.0.0.1" #
port = 4000

s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()
    c.send(b'\01\01\01\fd')
    print('Got connection from', addr)
    c.close()
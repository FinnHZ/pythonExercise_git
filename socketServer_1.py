# server.py
import socket

s = socket.socket()
host = "192.168.0.2" #socket.gethostname()  #only can be local address.
port = 4000 #1234

# host = "127.0.0.1"  #only can be local address.
# port = 1234
s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()
    # c.send(b'Thank you for your connecting')
    c.send(b'\\01\\01\\01\\fd')
    print('Got connection from', addr)

    c.close()
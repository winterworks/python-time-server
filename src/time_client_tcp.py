# example source: https://wiki.python.org/moin/TcpCommunication

import socket
from struct import unpack

TCP_IP = '127.0.0.1'
TCP_PORT = 37
BUFFER_SIZE = 1024
MESSAGE = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", unpack("!L", data))

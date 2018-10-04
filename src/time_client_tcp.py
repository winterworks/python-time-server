# example source: https://wiki.python.org/moin/TcpCommunication

import socket
from struct import unpack
from print_time import print_time


TCP_IP = '127.0.0.1'
TCP_PORT = 37
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
data = s.recv(BUFFER_SIZE)
s.close()

time = unpack("!L", data)
time = time[0]
print"received data: " +  str(time)

print_time(time)



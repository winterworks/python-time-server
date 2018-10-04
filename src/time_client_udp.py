# example source: https://wiki.python.org/moin/TcpCommunication

import socket
from struct import unpack

UDP_IP = '127.0.0.1'
UDP_PORT = 37
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(bytes(), (UDP_IP, UDP_PORT))

data = s.recvfrom(BUFFER_SIZE)

print("received data:", unpack("!L", data[0]))


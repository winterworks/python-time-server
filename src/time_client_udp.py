# example source: https://wiki.python.org/moin/TcpCommunication

import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(MESSAGE, (UDP_IP, UDP_PORT))

data = s.recvfrom(BUFFER_SIZE)

print("received data:", data)
# example source: https://wiki.python.org/moin/TcpCommunication

import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 5005
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((UDP_IP, UDP_PORT))

while 1:
    data, addr = s.recvfrom(BUFFER_SIZE)
    print('Connection address:', addr)
    print("received data:", data)
    s.sendto(data, addr)
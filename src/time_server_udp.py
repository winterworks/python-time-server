# example source: https://wiki.python.org/moin/TcpCommunication

from our_time import get_time_in_bin
import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 37
BUFFER_SIZE = 1024

print("Listening for UDP on IP: " + UDP_IP + " and port: " + str(UDP_PORT))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((UDP_IP, UDP_PORT))

while 1:
    data, addr = s.recvfrom(BUFFER_SIZE)

    if data != bytes(): break
    print('Connection address: ' + addr[0] + " and port: " + str(addr[1]))
    print("received data:", data)
    s.sendto(get_time_in_bin(), addr)
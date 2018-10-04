# example source: https://wiki.python.org/moin/TcpCommunication

from our_time import get_time_in_bin
import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 37
BUFFER_SIZE = 1024


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    print('Connection address:', addr)

    conn.send(get_time_in_bin())
    conn.close()

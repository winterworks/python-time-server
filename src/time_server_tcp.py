#!/usr/bin/python
# example source: https://wiki.python.org/moin/TcpCommunication

from our_time import get_time_in_bin
import socket
from common import getargs
import sys


def main(argv):
    tcp_ip, tcp_port = getargs(argv)

    print("Listening TCP on IP: " + tcp_ip + " and port: " + str(tcp_port))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((tcp_ip, tcp_port))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        print('Connection address: ' + addr[0] + " and port: " + str(addr[1]))

        conn.send(get_time_in_bin())
        conn.close()


if __name__ == '__main__':
    main(sys.argv)

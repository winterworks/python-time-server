# example source: https://wiki.python.org/moin/TcpCommunication

import socket
from struct import unpack
from print_time import print_time
from common import getargs
import sys


def main(argv):
    tcp_ip, tcp_port = getargs(argv)
    buffer_size = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((tcp_ip, tcp_port))
    data = s.recv(buffer_size)
    s.close()

    time = unpack("!L", data)
    time = time[0]
    print("received data: " + str(time))

    print_time(time)


if __name__ == '__main__':
    main(sys.argv)

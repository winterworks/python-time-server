# example source: https://wiki.python.org/moin/TcpCommunication

import socket
from struct import unpack
from print_time import print_time
from common import getargs
import sys


def main(argv):
    udp_ip, udp_port = getargs(argv)
    buffer_size = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(bytes(), (udp_ip, udp_port))

    data = s.recvfrom(buffer_size)

    time = unpack("!L", data[0])
    time = time[0]
    print("received data: " + str(time))

    print_time(time)


if __name__ == '__main__':
    main(sys.argv)

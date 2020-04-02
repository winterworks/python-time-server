# example source: https://wiki.python.org/moin/TcpCommunication

from our_time import get_time_in_bin
import socket
from common import getargs
import sys


def main(argv):
    udp_ip, udp_port = getargs(argv)
    buffer_size = 1024

    print("Listening for UDP on IP: " + udp_ip + " and port: " + str(udp_port))

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((udp_ip, udp_port))

    while 1:
        data, addr = s.recvfrom(buffer_size)

        if data != bytes(): break
        print('Connection address: ' + addr[0] + " and port: " + str(addr[1]))
        print("received data:", data)
        s.sendto(get_time_in_bin(), addr)


if __name__ == '__main__':
    main(sys.argv)

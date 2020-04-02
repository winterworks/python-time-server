import getopt
import sys
from os.path import basename


# Print description
def usage(filename):
    print('Usage:')
    print('  ' + basename(filename) + ' [-a <ip>] [-p <port>]')
    print('  ' + basename(filename) + ' -h | --help')
    print()
    print('Options:')
    print('  -h, --help                Show this screen')
    print('  -a <ip>, --address <ip>   Ip address to use [default: 127.0.0.1')
    print('  -p <port>, --port <port>  Port number to use [default: 37]')


# Retrieves the argument from launch and returns them
# Parameter: argv; the argument list from launch
# Return:
def getargs(argv):
    ip = '127.0.0.1'
    port = 37

    try:
        opts, args = getopt.getopt(argv[1:], "ha:p:", ["help", "address=", "port="])
    except getopt.GetoptError:
        usage(argv[0])
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            usage(argv[0])
            sys.exit()
        elif opt in ("-a", "--address"):
            ip = arg
        elif opt in ("-o", "--port"):
            port = arg

    return ip, port

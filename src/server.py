
from time_server_tcp import run_tcp_server
from time_server_udp import run_udp_server
import threading

t_tcp = threading.Thread(target=run_tcp_server)
t_tcp.daemon = True
t_udp = threading.Thread(target=run_udp_server)
t_udp.daemon = True

t_tcp.start()
t_udp.start()

while 1:
    continue

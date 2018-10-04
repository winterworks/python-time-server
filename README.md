# python-time-server
A python implementation of the Time Protocol ([https://tools.ietf.org/html/rfc868](https://tools.ietf.org/html/rfc868)).

## How to run the TCP server and client
### Run a time server
1. Open a terminal in /src
2. run: $ python time_server_tcp.py

The server will show _Listening for TCP on IP, PORT_ when it's running. It will show all the incoming requests. It can be accessed on localhost on port 37.
  
### Run a time client
1. Open another terminal in /src
2. run: $ python time_client_tcp.py

The client will make a request to localhost on port 37 by default.
  
## How to run the UDP server and client
Running the upd works the same, only now use time_server_udp.py and time_client_udp.py instead.

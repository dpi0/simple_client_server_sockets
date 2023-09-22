from socket import gethostbyname, gethostname, socket, AF_INET, SOCK_STREAM

import threading


SERVER_IP = gethostbyname(gethostname())
PORT_USED = 6969

ADDRESS = (SERVER_IP, PORT_USED)

server = socket(AF_INET, SOCK_STREAM)
# IPV4 and TCP based server


with server:
    server.bind(ADDRESS)

    server.listen()
    # enables a server to accept connections. It makes the server a “listening” socket
    # NOTE: can take a param int "backlog"
    # specifies the number of unaccepted connections that the system will allow before
    # refusing new connections

    print(f"Listening at {SERVER_IP}:{PORT_USED}")

    connection, address_info = server.accept()
    # blocks execution and waits for an incoming connection
    # client connects, it returns a new socket object
    # with connection and the address of the client
    # SIDENOTE: (host, port, flowinfo, scopeid) for IPv6

    with connection:
        print(f"Connected to {address_info}")

        while True:
            # loop over blocking calls to conn.recv()
            data = connection.recv(1024)
            # reads whatever data the client sends and echoes back using conn.sendall()

            if not data:
                break

            connection.sendall(data)

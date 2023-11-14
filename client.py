from socket import socket, AF_INET, SOCK_STREAM


SERVER_IP = "192.168.1.4"
PORT_SERVER = 6969

ADDRESS = (SERVER_IP, PORT_SERVER)

server = socket(AF_INET, SOCK_STREAM)

msg: str = "Hello!"

with server:
    server.connect(ADDRESS)
    server.sendall(b"Hello in binary!")

    data = server.recv(1024)

print(f"Recevied {data!r}")

import socket

# IP address and port number
ip_address = "0.0.0.0"
port = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((ip_address, port))

while True:
    command_input = input()
    server_socket.send(command_input)
    data = server_socket.recv(1024)
    print(data)
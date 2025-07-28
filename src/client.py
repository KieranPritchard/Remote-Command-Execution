import socket

# IP address and port number
ip_address = "0.0.0.0"
port = 5001

# server object and connection to server program
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((ip_address, port))

# Loops the command input and output of data from the server
while True:
    command_input = input("Please input a command: ")
    try:
        server_socket.send(command_input.encode())
        data = server_socket.recv(1024)
        print(data.decode())
    except Exception as e:
        print(f"Error encountered: {e}")
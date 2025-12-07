import socket

# IP address
ip_address = "127.0.0.1"
# port number
port = 5001

# server object and connection to server program
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connects to the server
server_socket.connect((ip_address, port))

# Loops the command input and output of data from the server
while True:
    # Allows the user to input a command
    command_input = input("Please input a command: ")
    # Trys to send it to the server program
    try:
        # Sends the encoded command to the server
        server_socket.send(command_input.encode())
        # Recevies the data
        data = server_socket.recv(1024)
        # Outputs the data
        print(data.decode())
    # catches and outputs the error
    except Exception as e:
        print(f"Error encountered: {e}")
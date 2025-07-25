import socket

def start_server():
    # IP address and port number
    ip_address = "0.0.0.0"
    port = 5000

    # Socket object creation
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip_address,port))
    server_socket.listen()
    print(f"Server started, listening on {ip_address}:{port}")

    # Handles input from client
    while True:
        # Accepts connection from the client
        client, address = server_socket.accept()
        print(f"Connected to client at: {address}")

        while True:
            try:
                receive_command = client.recv(1024)

                if not receive_command:
                    print(f"Client at {address} disconnected")
                    break

                command = receive_command.decode()
                print(f"Command received from client: {command}")

            except socket.error as e:
                print(f"Error encountered {e}")
        client.close()
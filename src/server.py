import socket
import subprocess

def start_server():
    # IP address and port number
    ip_address = "127.0.0.1"
    port = 5001

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
                # Receives a command from the client app
                receive_command = client.recv(1024)

                # Displays disconnect message
                if not receive_command:
                    print(f"Client at {address} disconnected")
                    break

                # Receives and decodes the command to sends the result back to the user
                command = receive_command.decode()
                print(f"Command received from client: {command}")
                stored_result = execute_command(command)
                print(f"Command executed from client: {command}")
                client.send(stored_result.encode())

            except socket.error as e:
                # Prints error message
                print(f"Error encountered {e}")
        client.close()

def execute_command(command):
    # Executes the command and stores the output to send back to client
    result = subprocess.run([command], capture_output=True, text=True)

    stored_result =  result.stdout if result.stdout else result.stderr

    return stored_result

if __name__ == "__main__":
    start_server()
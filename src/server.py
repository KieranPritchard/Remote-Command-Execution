import socket
import subprocess

def start_server():
    # IP address
    ip_address = "127.0.0.1"
    # port number
    port = 5001

    # Socket object creation
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Binds the object to the ip address and port
    server_socket.bind((ip_address,port))
    # starts listening for commands
    server_socket.listen()
    # Outputs that the server has started and what ip address and port it is running on
    print(f"Server started, listening on {ip_address}:{port}")

    # Runs the loop while true
    while True:
        # Accepts connection from the client
        client, address = server_socket.accept()
        # Outputs the address of the client
        print(f"Connected to client at: {address}")
        
        # Runs the loop while true
        while True:
            # Trys to receive a command
            try:
                # Receives a command from the client app
                receive_command = client.recv(1024)

                # Displays disconnect message if disconnected
                if not receive_command:
                    print(f"Client at {address} disconnected")
                    # Breaks the loop
                    break

                # Receives and decodes the command to sends the result back to the user
                command = receive_command.decode()
                # Outputs the command sent in
                print(f"Command received from client: {command}")
                # Stores the result of it
                stored_result = execute_command(command)
                # Outputs what was executed
                print(f"Command executed from client: {command}")
                # sends the data back to the client
                client.send(stored_result.encode())
            # Catches and outputs
            except socket.error as e:
                # Prints error message
                print(f"Error encountered {e}")
        client.close()

def execute_command(command):
    # Executes the command and stores the output to send back to client
    result = subprocess.run([command], capture_output=True, text=True)
    
    # Stores the result from the standard output
    stored_result =  result.stdout if result.stdout else result.stderr

    # Retuns the stored result
    return stored_result

# Starts the program
if __name__ == "__main__":
    start_server()
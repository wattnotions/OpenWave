import socket

# Use the local machine's IP and choose a port
HOST = '192.168.0.24'  # Replace with your Windows machine's local IP
PORT = 8000  # You can choose another port if this one is in use

# Create a socket (SOCK_STREAM means a TCP socket)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections (the argument is the maximum number of queued connections)
server_socket.listen(1)

print(f'Server listening on {HOST}:{PORT}...')

while True:
    # Accept a connection
    client_socket, addr = server_socket.accept()
    print(f'Connected by {addr}')

    # Receive and print data sent by the client
    while True:
        data = client_socket.recv(1024)  # Buffer size is 1024 bytes
        if not data:
            break
        print('Received', repr(data))

    # Close the connection
    client_socket.close()

# Ideally, we should never reach this point in a server script
server_socket.close()

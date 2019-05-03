import socket
import sys

#Controlers
finished = False

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while not finished:
    # Wait for a connection
    connection, client_address = sock.accept()

    try:

        while True:
            data = connection.recv(4096)
            if data: 
                connection.sendall('Recibido ' + data)
                if data=='E': finished = True
            else:
                break
    finally:
        # Clean up the connection
        connection.close()
print("Hasta luego")
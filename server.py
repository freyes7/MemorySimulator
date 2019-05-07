import socket
import sys
from MessageProcessor import MessageProcessor
from tabulate import tabulate

#Controler
state = 0

#Global variables
realMemorySize = 0
swapMemorySize = 0
pageSize = 0
politic = 'FIFO'
memory = 0


def processMessage(data):
    global state
    if state == 0:
        realMemorySize,change,message =MessageProcessor.setRealMemorySize(data)
        state = state + change
        return message
    elif state == 1:
        realMemorySize,change,message =MessageProcessor.setSwapMemorySize(data)
        state = state + change
        return message
    elif state == 2:
        pageSize,change,message =MessageProcessor.setPageSize(data)
        state = state + change
        return message
    elif state == 3:
        politic,change,message =MessageProcessor.setPolitic(data)
        state = state + change
        return message
    elif state == 4:
        change,message =MessageProcessor.instruction(data)
        state = state + change
        return message
    return '\nError'

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while state<5:
    # Wait for a connection
    connection, client_address = sock.accept()

    try:

        while True:
            data = connection.recv(4096)
            if data: 
                connection.sendall('Recibido ' + data + processMessage(data))
                if data=='E': finished = True
            else:
                break
    finally:
        # Clean up the connection
        connection.close()
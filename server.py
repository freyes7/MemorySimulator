import socket
import sys
import time
from MessageProcessor import MessageProcessor
from Memory import Memory
from Output import Output
import copy

#Controler
state = 0

#Global variables
realMemorySize = 0
swapMemorySize = 0
pageSize = 0
politic = 'FIFO'
memory = 0
initialTime = 0


def processMessage(data):
    global state
    global realMemorySize
    global swapMemorySize
    global pageSize
    global politic
    global memory
    global initialTime

    if state == 0:
        realMemorySize,change,message =MessageProcessor.setRealMemorySize(data)
        state = state + change
        return message
    elif state == 1:
        swapMemorySize,change,message =MessageProcessor.setSwapMemorySize(data)
        state = state + change
        return message
    elif state == 2:
        pageSize,change,message =MessageProcessor.setPageSize(realMemorySize, data)
        state = state + change
        return message
    elif state == 3:
        politic,change,message =MessageProcessor.setPolitic(data)
        state = state + change
        if state == 4:
            memory = Memory(realMemorySize,swapMemorySize,pageSize,politic)
            initialTime = time.time()
            Output.resetTableRows()
            Output.lastRealList = copy.copy(memory.realMemory)
            Output.lastSwapList = copy.copy(memory.swapMemory)
            Output.addCommandRow("0", "", "", memory.realMemory, memory.swapMemory, memory.freedProcesses)
        return message
    elif state == 4:
        change,values,message =MessageProcessor.instruction(data)
        if message == 'A':
            message, realMemory = memory.accessAddress(values[0],values[1],values[2])
            Output.addCommandRow(time.time()-initialTime, data, realMemory, memory.realMemory, memory.swapMemory, memory.freedProcesses)
            Output.displayCommandsTableLast()
        elif message == 'P':
            message = memory.loadProcess(values[1],values[0])
            Output.addCommandRow(time.time()-initialTime, data, "", memory.realMemory, memory.swapMemory, memory.freedProcesses)
            Output.displayCommandsTableLast()
        elif message == 'L':
            message = memory.freeProcess(values[0])
            Output.addCommandRow(time.time()-initialTime, data, "", memory.realMemory, memory.swapMemory, memory.freedProcesses)
            Output.displayCommandsTableLast()
        elif message == 'C':
            message = memory.saveComment(data)
        elif message == 'F':
            Output.displayCommandsTable()
            Output.displayFaultsTable()
            Output.resetTableRows()
            message = memory.endSimulation()
            state = 1

        #memory.pri()
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
    finished = False

    try:

        while not finished:
            data = connection.recv(4096)
            if data: 
                if data=='E': 
                    finished = True
                    connection.sendall('Recibido ' + data)
                    state = 5
                    # Clean up the connection
                    connection.close()
                else:
                    connection.sendall('Recibido ' + data + processMessage(data))
            else:
                break
    finally:
        # Clean up the connection
        connection.close()
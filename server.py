import socket # para poder crear el servidor
import sys # para poder crear el servidor
import time # para poder imprimir los tiempos de las operaciones
from MessageProcessor import MessageProcessor # para procesar los mensages que se reciben
from Memory import Memory # para importar el manejo de la memoria
from Output import Output #para imprimir las tablas
import copy

#Controler
state = 0

#Global variables
realMemorySize = 0
swapMemorySize = 0
pageSize = 0 
politic = 'FIFO' #se inicia con la politica FIFO y puede camiar a LIFO
memory = 0
initialTime = 0


def processMessage(data):
    # se crean las variables globales que vamos necesitar para cada operacón
    global state
    global realMemorySize
    global swapMemorySize
    global pageSize
    global politic
    global memory
    global initialTime

    if state == 0:
        initialTime = time.time() #se obtiene el tiempo en que se inician las operaciones
        realMemorySize,change,message =MessageProcessor.setRealMemorySize(data)
        state = state + change
        return message # se regresa la comprobación de lo que se recibió
    elif state == 1:
        swapMemorySize,change,message =MessageProcessor.setSwapMemorySize(data)
        state = state + change
        return message # se regresa la comprobación de lo que se recibió
    elif state == 2:
        pageSize,change,message =MessageProcessor.setPageSize(realMemorySize, data)
        state = state + change
        return message # se regresa la comprobación de lo que se recibió
    elif state == 3:
        politic,change,message =MessageProcessor.setPolitic(data)
        state = state + change
        if state == 4:
            memory = Memory(realMemorySize,swapMemorySize,pageSize,politic)
            Output.resetTableRows()
            actualTime = time.time()-initialTime
            Output.lastRealList = copy.copy(memory.realMemory)
            Output.lastSwapList = copy.copy(memory.swapMemory)
            Output.addCommandRow(actualTime, "", "", memory.realMemory, memory.swapMemory, memory.freedProcesses)
        return message # se regresa la comprobación de lo que se recibió
    elif state == 4:
        change,values,message =MessageProcessor.instruction(data)
        actualTime = time.time()-initialTime
        #se crea la condición para cada posible comando
        if message == 'A': #Es el comando que permite 
            message, realMemory = memory.accessAddress(values[0],values[1],values[2])
            Output.addCommandRow(actualTime, data, realMemory, memory.realMemory, memory.swapMemory, memory.freedProcesses)
            Output.displayCommandsTableLast()
        elif message == 'P': #Es el comando que permite cargar un nuevo proceso
            message = memory.loadProcess(values[1],values[0])
            #esto agrega los valos nuevos a la tabla para desplegarlos
            Output.addCommandRow(actualTime, data, "", memory.realMemory, memory.swapMemory, memory.freedProcesses)
            Output.displayCommandsTableLast()#se llama al despliegue de la tabla
        elif message == 'L': #Es el comando que permite liberar las paginas
            message = memory.freeProcess(values[0])
            Output.addCommandRow(actualTime, data, "", memory.realMemory, memory.swapMemory, memory.freedProcesses)
            Output.displayCommandsTableLast()
        elif message == 'C': #Es el comando para cuando se usan comentarios
            message = memory.saveComment(data)
        elif message == 'F': #Es el comando que termina un conjuntode especificaciones
            message = memory.endSimulation()
            Output.displayCommandsTable()
            Output.displayFaultsTable()
            Output.resetTableRows()
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
                connection.close()
                break
    finally:
        # Clean up the connection
        connection.close()
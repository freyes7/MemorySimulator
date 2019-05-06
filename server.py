import socket
import sys
from tabulate import tabulate

#Controlers
finished = False
state = 0

#Global variables
realMemorySize = 0
swapMemorySize = 0
pageSize = 0
politica = 'FIFO'

#Functions
def setRealMemorySize(data):
    command = data.split()
    if len(command)<2 : 
        return '\nInsuficientes parametros'
    if command[0] != 'RealMemory': 
        return '\nEl comando no es el esperado, intenta de nuevo.'
    try:
        realMemorySize = int(command[1])
    except ValueError:
        return '\nIngresa un entero para el tamanio de la memoria'
    global state
    state = state + 1
    return '\nEl tamanio de la memoria se cambio con exito'

def setSwapMemorySize(data):
    command = data.split()
    if len(command)<2 : 
        return '\nInsuficientes parametros'
    if command[0] != 'SwapMemory': 
        return '\nEl comando no es el esperado, intenta de nuevo.'
    try:
        swapMemorySize = int(command[1])
    except ValueError:
        return '\nIngresa un entero para el tamanio de la memoria'
    global state
    state = state + 1
    return '\nEl tamanio de la memoria se cambio con exito'

def setPageSize(data):
    command = data.split()
    if len(command)<2 : 
        return '\nInsuficientes parametros'
    if command[0] != 'PageSize': 
        return '\nEl comando no es el esperado, intenta de nuevo.'
    try:
        pageSize = int(command[1])
    except ValueError:
        return '\nIngresa un entero para el tamanio de las paginas'
    global state
    state = state + 1
    return '\nEl tamanio de las paginas se cambio con exito'

def setPolitica(data):
    command = data.split()
    if len(command)>=1 and command[0] == 'E': 
        finished = True
        return '\nHasta Luego'
    if len(command)<2 : 
        return '\nInsuficientes parametros'
    if command[0] != 'PoliticaMemory': 
        return '\nEl comando no es el esperado, intenta de nuevo.'
    if command[1] != 'FIFO' and command[1] != 'LIFO':
        return '\nDicha Politica no es manejada por el programa'
    global state
    state = state + 1
    politica = command[1]
    return '\nLa politica de remplazo se cambio con exito'

def instruction(data):
    command = data.split()
    if len(command)>=1 and command[0]=='F':
        global state
        state = state - 1
        return '\nElige la nueva politica de remplazo o ingresa E para terminar'
    return '\nError'

def process(data):
    global state
    if state == 0:
        return setRealMemorySize(data)
    elif state == 1:
        return setSwapMemorySize(data)
    elif state == 2:
        return setPageSize(data)
    elif state == 3:
        return setPolitica(data)
    elif state == 4:
        return instruction(data)
    return '\nError'

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
                connection.sendall('Recibido ' + data + process(data))
                if data=='E': finished = True
            else:
                break
    finally:
        print tabulate([['Alice', 24], ['Bob', 19]], headers=['Name', 'Age'])
        # Clean up the connection
        connection.close()
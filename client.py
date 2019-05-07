import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    
    # Send data
    message = " "
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "RealMemory noSoyUnEntero"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "RealMemory 34"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "SwapMemory 34"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "PageSize 34"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "PoliticaMemory SSTF"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "PoliticaMemory LIFO"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "A hola 1 35"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "F"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "PoliticaMemory FIFO"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "F"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = 'E'
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data
finally:
    sock.close()
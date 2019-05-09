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

    message = "RealMemory 1"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "SwapMemory 1"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "PageSize 512"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "PoliticaMemory LIFO"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "P 1024 1"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "P 3000 3"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "P 2048 2"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "L 1"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "L 2"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "P 512 3"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "P 512 4"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "P 2048 5"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "L 3"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "L 5"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "L 4"
    sock.sendall(message)

    data = sock.recv(4096)
    print >>sys.stderr, '%s' % data

    message = "L 5"
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
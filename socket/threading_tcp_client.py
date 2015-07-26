# http://danieldandrada.blogspot.com/2007/09/python-socketserverthreadingtcpserver.html

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 5000))
print sock.recv(1024)

sock.send('bye')
print sock.recv(1024)

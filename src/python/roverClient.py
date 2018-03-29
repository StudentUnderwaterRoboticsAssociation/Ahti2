import socket
import time


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address = ('192.168.1.100', 4242)
sock.connect(server_address)
sock.sendall("3")
sock.close()


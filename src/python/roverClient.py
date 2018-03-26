import socket
import time


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address = ('10.78.18.2', 4242)
sock.connect(server_address)


try:
	sock.sendall("nin ax")
except:
	pass




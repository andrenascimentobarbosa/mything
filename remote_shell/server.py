import socket

host = '127.0.0.1'
port = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)
print('listening on ', port)

client, addr = server.accept()
print('connection established with ', addr)

while True:
    comm = input('shell# ').strip().lower()
    if comm == 'close':
        break
    elif comm == '':
        pass
    else:
        server.send(comm.encode())
        output = server.recv(1024).decode()
        print(output)

server.close()

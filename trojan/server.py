import socket
import os


class Server:
    def __init__(self):
        self.server = None
        self.addr = None
        self.client = None
        self.quit_list = ['exit', 'close', 'quit']
        self.host = '127.0.0.1'
        self.port = 8080


    def connect(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(1)
        print('[-] Wating for connection...')
        print(f'listening on port {self.port}')
        self.client, self.addr = self.server.accept()
        print(f'[+] Connected to {self.addr}')
        

    def shell(self):
        self.connect()
        while True:
            try:
                command = input(f'{self.addr[0]}> ').lower().strip()
                if command in self.quit_list:
                    self.client.send(command.encode('utf-8'))
                    break
                elif command == 'clear':
                    os.system(command)
                else:
                    self.client.send(command.encode('utf-8'))
                    output = self.client.recv(1024).decode('utf-8')
                    if not output:
                        continue
                    else:
                        print(output)
            except OSError as e:
                print(f'Error: {e}')
            except KeyboardInterrupt:
                print(f'\nTry one of these commands: {quit_list}')
            except Exception as e:
                print(f'Error: {e}')
        self.server.close()


    def main(self):
        self.shell()


if __name__ == "__main__":
    server = Server()
    server.main()



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
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.host, self.port))
            self.server.listen(1)
            print('\033[1m[-]\033[m Wating for connection...')
            print(f'listening on port {self.port}\n')
            self.client, self.addr = self.server.accept()
            print(f'\033[1;32m[+]\033[m Connected to {self.addr}\n')
        except OSError:
            print('Host or Port already in use.')


    def shell(self):
        self.connect()
        while True:
            try:
                command = input(f'{self.addr[0]}:{self.addr[1]}~:>_ ').lower().strip()
                if command in self.quit_list:
                    self.client.send(command.encode('utf-8'))
                    break
                elif command == 'clear':
                    os.system(command)
                elif command[:3] == 'cd ':
                    self.client.send(command.encode('utf-8'))
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



# client.py

import socket

class Client:
    def __init__(self, host, port):
        self.server = (host, port)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.server)

    def send(self, data):
        self.client.send(data.encode())

    def receive(self):
        return self.client.recv(2048).decode()

    def close(self):
        self.client.close()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 5555
    client = Client(host, port)
    # Logique de communication avec le serveur

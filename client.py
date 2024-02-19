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

    def start(self):
        try:
            while True:
                # Receive the message from the server (game state, etc.)
                server_response = self.receive()  # Vous devriez recevoir le message de bienvenue ici.
                print(server_response)

                # Check if the game is over
                if "Félicitations" in server_response or "Dommage" in server_response:
                    break

                # Ask the player to guess a letter
                guess = input("Devinez une lettre: ").strip().lower()
                if guess and len(guess) == 1:
                    self.send(guess)
                else:
                    print("Veuillez entrer une seule lettre.")
        finally:
            print("Fermeture de la connexion.")
            self.close()

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

def main():
    host = "127.0.0.1"
    port = 5555
    client = Client(host, port)

    try:
        while True:
            # Recevoir le message du serveur etat du jeu
            server_response = client.receive()
            print(server_response)

            # Vérifier si le jeu est terminé
            if "Félicitations" in server_response or "Dommage" in server_response:
                break

            # Demander au joueur de deviner une lettre
            guess = input("Devinez une lettre: ").strip().lower()
            if guess and len(guess) == 1:
                client.send(guess)
            else:
                print("Veuillez entrer une seule lettre.")
    finally:
        print("Fermeture de la connexion.")
        client.close()

if __name__ == "__main__":
    main()

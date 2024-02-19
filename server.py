# server.py

import socket
import threading
from game_logic import Game

class HangmanServer:
    def __init__(self, host, port, word, max_attempts):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen()
        self.clients = []
        self.game = Game(word, max_attempts)

    def broadcast(self, message):
        for client in self.clients:
            client.send(message.encode())

    def handle_client(self, client):
        client.send("Connexion au serveur de pendu réussie! Veuillez deviner une lettre:".encode())
        while True:
            try:
                guess = client.recv(1024).decode()
                if guess:
                    if self.game.guess(guess):
                        message = "Bonne lettre!"
                    else:
                        message = "Mauvaise lettre."

                    if self.game.is_game_over():
                        if all(letter in self.game.guessed_letters for letter in self.game.word):
                            message = "Félicitations! Le mot était: " + self.game.word
                        else:
                            message = "Dommage! Le mot était: " + self.game.word

                        self.broadcast(message)
                        break
                    else:
                        message += "\n" + self.game.display_word()
                        self.broadcast(message)
            except:
                break

        client.close()
        self.clients.remove(client)

    def start(self):
        print(f"Serveur en attente sur {self.host}:{self.port}...")
        while True:
            client, address = self.server.accept()
            print(f"Nouvelle connexion de {address}.")
            self.clients.append(client)
            client_handler = threading.Thread(target=self.handle_client, args=(client,))
            client_handler.start()

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 5555
    WORD_TO_GUESS = "pendu"
    MAX_ATTEMPTS = 6

    hangman_server = HangmanServer(HOST, PORT, WORD_TO_GUESS, MAX_ATTEMPTS)
    hangman_server.start()

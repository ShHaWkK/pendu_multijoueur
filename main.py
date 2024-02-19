# main.py

import server
import client
import game_logic

def main():
    # Initialisation du serveur et des clients
    server.start_server()
    client1 = client.Client()
    client2 = client.Client()

    # Lancement du jeu
    game = game_logic.Game()
    game.start()

if __name__ == "__main__":
    main()

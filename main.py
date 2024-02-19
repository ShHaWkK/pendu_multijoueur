# main.py

import threading
import server
import client
import game_logic

def start_game_server():
    # Initialize and start the game server
    hangman_server = server.HangmanServer("127.0.0.1", 5555, "pendu", 6)
    server_thread = threading.Thread(target=hangman_server.start)
    server_thread.start()

def start_game_client():
    hangman_client = client.Client("127.0.0.1", 5555)
    client_thread = threading.Thread(target=hangman_client.start)  # Assuming you have a 'start' method
    client_thread.start()
    return client_thread

def main():
    # Start the server
    start_game_server()

    # Start two clients for demonstration
    clients = [start_game_client() for _ in range(2)]

    # Wait for both clients to finish
    for c in clients:
        c.join()

if __name__ == "__main__":
    main()

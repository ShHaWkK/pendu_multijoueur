# server.py

import socket
import threading

def handle_client(client, address):
    print(f"Nouvelle connexion de {address}.")
    # Logique de gestion du client

def start_server():
    host = "127.0.0.1"
    port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen()

    print(f"Serveur en attente sur {host}:{port}...")

    while True:
        client, address = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client, address))
        client_handler.start()

if __name__ == "__main__":
    start_server()

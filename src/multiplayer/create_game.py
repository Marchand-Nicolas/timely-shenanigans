# Nico
import socket

from src.utils.constants import server_address, server_port
from src.multiplayer.create_packet import create_packet


# Envoyer une requête TCP au serveur pour créer une partie.
def create_game(username):
    # Création d'une socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connexion au serveur
    sock.connect((server_address, server_port))
    # Envoi de la requête
    request = create_packet("create_game", {"username": username})
    sock.sendall(request.encode())
    # Réception de la réponse
    response = sock.recv(1024).decode()
    # Fermeture de la connexion
    sock.close()
    return response

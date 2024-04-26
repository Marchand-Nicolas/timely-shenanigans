from src.multiplayer.create_packet import create_packet
import socket
from src.utils.constants import server_address, server_port
import json

# Nico


def call_server(route, data):
    # Création d'une socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connexion au serveur
    sock.connect((server_address, server_port))
    # Envoi de la requête
    request = create_packet(route, data)
    sock.sendall(request.encode())
    # Réception de la réponse
    response = sock.recv(1024).decode()
    # Fermeture de la connexion
    sock.close()
    parsed_response = json.loads(response)
    if parsed_response["status"] == "error":
        print(parsed_response["message"])
        exit(1)
    return parsed_response

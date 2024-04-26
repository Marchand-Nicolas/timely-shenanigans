# Nico

import socket
import json
from server.routes.create_game import handle_create_game
from server.routes.join_game import handle_join_game
from server.routes.get_game_state import handle_get_game_state

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("", 3011))
server.listen(5)

print("Server is listening on port 3011")

routes = {
    "create_game": handle_create_game,
    "join_game": handle_join_game,
    "get_game_state": handle_get_game_state,
}

# On stocke les parties en cours
games = []

while True:
    client, addr = server.accept()
    print(f"Connection from {addr}")
    data = client.recv(1024)
    parsed = json.loads(data)
    route = parsed["route"]
    body = parsed["body"]
    # Ouvrir dynamiquement le fichier correspondant à la route
    # et exécuter la fonction correspondante en lui passant le body
    response = routes[route](body, games)
    client.sendall(response.encode())
    client.close()
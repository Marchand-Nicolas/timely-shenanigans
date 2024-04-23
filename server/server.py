# Nico

import socket
import json
from server.routes.create_game import handle_create_game

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("", 3011))
server.listen(5)

print("Server is listening on port 3011")

routes = {"create_game": handle_create_game}

state = {"games": []}

while True:
    client, addr = server.accept()
    print(f"Connection from {addr}")
    data = client.recv(1024)
    parsed = json.loads(data)
    route = parsed["route"]
    body = parsed["body"]
    # Ouvrir dynamiquement le fichier correspondant à la route
    # et exécuter la fonction correspondante en lui passant le body
    response = routes[route](body, state)
    client.sendall(response.encode())
    client.close()

# Nico

import socket
import json
from server.routes.create_game import handle_create_game
from server.routes.join_game import handle_join_game
from server.routes.get_game import handle_get_game
from server.routes.kill_player import handle_kill_player
from server.routes.restart_game import handle_restart_game
from server.utils.constants import end_time_duration_seconds
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Eviter l'erreur "Address already in use"
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("", 3011))
server.listen(5)

print("Server is listening on port 3011")

routes = {
    "create_game": handle_create_game,
    "join_game": handle_join_game,
    "get_game": handle_get_game,
    "kill_player": handle_kill_player,
    "restart_game": handle_restart_game,
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
    for game in games:
        players = game.get_players()
        for player in players:
            if player.is_disconnected():
                game.remove_player(player.id)
        # On termine les parties dont le délai est dépassé
        game.restart_if_ended()
        # On relance les parties terminées depuis end_time_duration_seconds
        if (
            game.state == "finished"
            and time.time() - game.end_time > end_time_duration_seconds
        ):
            game.start_game()

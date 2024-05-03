# Nico

from src.multiplayer.call_server import call_server
import time


def server_loop(code, players, player_id, get_exit_app, player_coordinates, game_state):
    """
    Récupère les données de la partie, notamment la liste des joueurs avec leurs coordonnées
    actualisées.
    Modifie la variable players passée en paramètre.
    """
    print("Server loop started")
    while True:
        response = call_server(
            "get_game_state",
            {
                "code": code,
                "player_id": player_id,
                "x": player_coordinates.x,
                "y": player_coordinates.y,
            },
        )
        players.clear()
        for player in response["players"]:
            players.append(player)
        game_state["state"] = response["state"]
        game_state["start_time"] = response["start_time"]
        time.sleep(0.1)
        if get_exit_app():
            break

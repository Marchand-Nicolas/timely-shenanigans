# Nico
import json
import time


def handle_get_game_state(body, games):
    # On cherche la partie correspondant au code
    game = None
    for g in games:
        if g.code == body["code"]:
            game = g
            break
    if game is None:
        return json.dumps({"status": "error", "message": "Game not found to get state"})

    player_id = body["player_id"]

    players = game.get_players()

    # On renvoie la liste des joueurs, sans le joueur qui a fait la requête
    # Mais on modifie le joueur qui a fait la requête pour lui donner sa position
    x = body["x"]
    y = body["y"]
    player_list = []
    for player in players:
        if player.id != player_id:
            player_list.append(player)
        else:
            player.update(x, y)

    return json.dumps(
        {
            "status": "ok",
            "players": [p.to_json() for p in player_list],
            "state": game.state,
        }
    )

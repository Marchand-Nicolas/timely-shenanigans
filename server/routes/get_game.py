# Nico
import json


def handle_get_game(body, games):
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

    # On renvoie la liste des joueurs
    # Mais on modifie le joueur qui a fait la requête pour lui donner sa position
    x = body["x"]
    y = body["y"]
    for player in players:
        if player.id == player_id:
            player.update(x, y)

    return json.dumps(
        {
            "status": "ok",
            "players": [p.to_json() for p in players],
            "state": game.state,
            "start_time": game.start_time,
        }
    )

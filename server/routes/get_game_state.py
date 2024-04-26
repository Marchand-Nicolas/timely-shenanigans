# Nico
import json


def handle_get_game_state(body, games):
    # On cherche la partie correspondant au code
    game = None
    for g in games:
        if g.code == body["code"]:
            game = g
            break
    if game is None:
        return json.dumps({"status": "error", "message": "Game not found"})

    player_id = body["player_id"]

    players = game.get_players()

    # On renvoie la liste des joueurs, sans le joueur qui a fait la requête
    player_list = []
    for player in players:
        if player.id != player_id:
            player_list.append(player)

    return json.dumps({"status": "ok", "players": player_list, "state": game.state})
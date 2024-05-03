# Nico
import json
from server.classes.player import Player


def handle_kill_player(body, games):
    # On cherche la partie correspondant au code
    game = None
    for g in games:
        if g.code == body["code"]:
            game = g
            break
    if game is None:
        return json.dumps({"status": "error", "message": "Game not found"})

    player_id = body["player_id"]

    game.kill_player(player_id)

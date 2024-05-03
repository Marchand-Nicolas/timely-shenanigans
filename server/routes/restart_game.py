# Nico
import json
from server.classes.player import Player


def handle_restart_game(body, games):
    # On cherche la partie correspondant au code
    game = None
    for g in games:
        if g.code == body["code"]:
            game = g
            break
    if game is None:
        return json.dumps({"status": "error", "message": "Game not found"})

    # On réinitialise la partie
    game.start_game()

    return json.dumps(
        {
            "status": "ok",
        }
    )

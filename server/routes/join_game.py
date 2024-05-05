# Nico
import json
from server.classes.player import Player


def handle_join_game(body, games):
    # On cherche la partie correspondant au code
    game = None
    for g in games:
        if g.code == body["code"]:
            game = g
            break
    if game is None:
        return json.dumps({"status": "error", "message": "Game not found"})

    player_count = game.get_player_count()
    # On crée le joueur
    player = Player(body["username"], player_count)
    game.players.append(player)
    if player_count == 1:
        game.state = "running"
    game.start_game()
    return json.dumps(
        {
            "status": "ok",
            "game_id": game.id,
            "seed": game.seed,
            "player_id": player.id,
            "code": game.code,
        }
    )

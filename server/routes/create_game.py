# Nico
import json
from server.classes.player import Player
from server.classes.game import Game
import random


def handle_create_game(body, games):
    # On crée le joueur initial
    main_player = Player(body["username"], 0)
    game_id = len(games)
    # On génère le code à 6 chiffres pour rejoindre la partie
    code = "".join([str(random.randint(0, 9)) for _ in range(6)])
    # On génère une seed à 10 chiffres
    seed = int("".join([str(random.randint(0, 9)) for _ in range(10)]))
    game = Game(game_id, [main_player], "waiting", code, seed)
    games.append(game)
    return json.dumps({"status": "ok", "game_id": game_id, "code": code, "seed": seed})

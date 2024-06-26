from src.utils.start_game import start_game
from src.multiplayer.create_game import create_game as create


# Nico


def create_game(username, screen):
    res = create(username)
    if res:
        seed = res["seed"]
        code = res["code"]
        print(f"Game created with seed {seed} and code {code}")
        start_game(seed, screen, code, 0)

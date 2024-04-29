from src.multiplayer.join_game import join_game
from src.utils.start_game import start_game


# Nico


def create_game(username):
    res = create_game(username)
    if res:
        seed = res["seed"]
        code = res["code"]
        print(f"Game created with seed {seed} and code {code}")
        start_game(seed, code, 0)

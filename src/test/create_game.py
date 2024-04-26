from src.multiplayer.create_game import create_game
from src.utils.start_game import start_game


# Nico

res = create_game("Penguin")

if res:
    seed = res["seed"]
    code = res["code"]
    print(f"Game created with seed {seed} and code {code}")
    start_game(seed, code, 0)

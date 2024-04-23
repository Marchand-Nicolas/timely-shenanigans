from src.multiplayer.join_game import join_game
from src.utils.start_game import start_game


# Nico

code = input("Enter the game code: ")

res = join_game("Pomme", code)

if res:
    seed = res["seed"]
    code = res["code"]
    print(f"Game joined with seed {seed} and code {code}")
    start_game(seed)

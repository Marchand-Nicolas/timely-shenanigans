from src.multiplayer.join_game import join_game as join
from src.utils.start_game import start_game


# Nico


def join_game(username, screen, code):
    res = join(username, code)
    if res:
        seed = res["seed"]
        code = res["code"]
        player_id = res["player_id"]
        print(f"Game joined with seed {seed} and code {code} and player_id {player_id}")
        start_game(seed, screen, code, player_id)

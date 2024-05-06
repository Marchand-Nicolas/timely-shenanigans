# Nico
from src.utils.constants import game_duration_seconds


def get_game_duration(player_amount):
    return 30 + 20 + game_duration_seconds * player_amount

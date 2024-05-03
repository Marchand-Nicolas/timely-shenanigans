# Nico
from server.utils.constants import game_duration_seconds


def get_game_duration(player_amount):
    return game_duration_seconds * player_amount

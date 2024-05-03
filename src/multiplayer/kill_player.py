# Nico

from src.multiplayer.call_server import call_server


def kill_player(player_id, code):
    return call_server("kill_player", {"player_id": player_id, "code": code})

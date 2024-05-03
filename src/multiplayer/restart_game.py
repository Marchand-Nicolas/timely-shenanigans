# Nico

from src.multiplayer.call_server import call_server


def restart_game(code):
    return call_server("restart_game", {"code": code})

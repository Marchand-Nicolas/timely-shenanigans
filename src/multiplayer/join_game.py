# Nico

from src.multiplayer.call_server import call_server


def join_game(username, code):
    return call_server("join_game", {"username": username, "code": code})

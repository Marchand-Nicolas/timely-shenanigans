# Nico
from src.multiplayer.call_server import call_server


# Envoyer une requête TCP au serveur pour créer une partie.
def create_game(username):
    return call_server("create_game", {"username": username})

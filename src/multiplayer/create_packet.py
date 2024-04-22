# Nico

import json


def create_packet(route, body):
    """
    Créer le contenu d'un packet (string), qui est traitable facilement
    côté serveur.
    IN: route (str), body (dict),
    OUT: packet (str)
    """
    return json.dumps({"route": route, "body": body})

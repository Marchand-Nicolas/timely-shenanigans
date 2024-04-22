# crée par Elliot
from math import sqrt
from src.map.asset import Asset


def generate_map(seed: int, width: int, height: int, player_amount=2):
    """
    Génère de manière procédurale une carte à partir d'une graine.
    On n'utilise pas des nombres aléatoires, car l'objectif est de transmettre la graine
    aux autres joueurs.
    Out: Liste d'assets
    """
    assets = []
    for x in range(0, width, 10):
        for y in range(0, height, 10):
            if ((seed) + (x*y)) % 14 == 0 and x % 6 == 0 and y % 4 == 0:
                # condition dépendant de la graine pour générer un arbre ou non
                assets.append(Asset((x, y), "src/assets/grass.png", None, 50))
            elif (seed - (x*y)) % 24 == 0:  # pareil pour l'herbe
                assets.append(Asset((x, y), "src/assets/vaisseau.png", None, 50))
    # Génération des bases des joueurs en fonction de la taille de la map
    assets.append(Asset((width // 10, height // 2), "src/assets/base.jpg", None, 50))
    assets.append(
        Asset((width - (width // 10), height // 2), "src/assets/base.jpg", None, 50)
    )
    # print([str(asset) for asset in assets])
    return assets
from math import sqrt
import asset


def generate_map(seed: int, width: int, height: int, player_amount=2):
    """
    Génère de manière procédurale une carte à partir d'une graine.
    On n'utilise pas des nombres aléatoires, car l'objectif est de transmettre la graine
    aux autres joueurs.
    Out: Liste d'assets
    """
    assets = []
    for x in range(width, 5):
        for y in range(height, 5):
            if sqrt(seed) % x == 0:
                # condition dépendant de la graine pour générer un arbre ou non
                assets.append(asset.Asset((x, y), "alien.png", None))
            elif (seed(2) * 1000) % y == 0:  # pareil pour l'herbe
                assets.append(asset.Asset((x, y), "vaisseau.png", None))
    # Génération des bases des joueurs en fonction de la taille de la map
    assets.append(asset.Asset((width // 10, height // 2), "base_rouge.png", None))
    assets.append(
        asset.Asset((width - (width // 10), height // 2), "base_rouge.png", None)
    )
    return assets

# crée par Elliot
from math import cos, sin
from src.map.asset import Asset

table = [
    { "src/assets/grass.png" : 15, "src/assets/fleur.jpg" : -9 , "src/assets/arbre.png" : -9},
    { "src/assets/grass.png" : -9, "src/assets/arbre.png" : 15, "src/assets/fleur.jpg" : 0},
    { "src/assets/arbre.png" : -9, "src/assets/fleur.jpg" : 15, "src/assets/grass.png" : 0}   
]

def generate_map(seed: int, width: int, height: int, player_amount=2):
    """
    Génère de manière procédurale une carte à partir d'une graine.
    On n'utilise pas des nombres aléatoires, car l'objectif est de transmettre la graine
    aux autres joueurs.
    Out: Liste d'assets
    """
    assets = [Asset((width // 10, height // 2), "src/assets/base.jpg", None, 50), Asset((width - (width // 10), height // 2), "src/assets/base.jpg", None, 50), Asset((0, 0), "src/assets/fleur.jpg", None, 50) ]
    for y in range(10, width, 10):
        for x in range(10, height, 10):
            valeur = abs(sin(seed * x * y)) * 100    # on génère un nombre entre 0 et 100 dépendant de la seed et des coordonnées
            if valeur >= 10:
                continue
            valeur = abs(cos(seed * x * y / 100)) * 100
            modificateur = table[2][assets[-1].get_image()]
            if valeur + modificateur >= 90:
                assets.append(Asset((x, y), "src/assets/grass.png", None, 50))
                continue
            modificateur = table[1][assets[-1].get_image()]
            if valeur + modificateur >= 90:
                assets.append(Asset((x, y), "src/assets/fleur.jpg", None, 70))
                continue
            modificateur = table[0][assets[-1].get_image()]
            if valeur + modificateur >= 90:
                assets.append(Asset((x, y), "src/assets/arbre.png", None, 80))
    # Génération des bases des joueurs en fonction de la taille de la map
    # print([str(asset) for asset in assets])
    return assets

generate_map
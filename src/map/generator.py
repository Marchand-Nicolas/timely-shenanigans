# crée par Elliot
from math import cos, sin
from src.map.asset import Asset
from src.map.coordinates import Coordinates

table = [
    {
        "src/assets/grass.png": 15,
        "src/assets/fleur.png": -9,
        "src/assets/arbre.png": -9,
    },
    {"src/assets/grass.png": -9, "src/assets/arbre.png": 8, "src/assets/fleur.png": -5},
    {"src/assets/arbre.png": -9, "src/assets/fleur.png": 15, "src/assets/grass.png": 0},
]

image_paths = [
    "src/assets/arbre.png",
    "src/assets/fleur.png",
    "src/assets/grass.png",
]


def generate_map(seed: int, width: int, height: int, loaded_images: dict):
    """
    Génère de manière procédurale une carte à partir d'une graine.
    On n'utilise pas des nombres aléatoires, car l'objectif est de transmettre la graine
    aux autres joueurs.
    Out: Liste d'assets
    """
    assets = [              # On crée un asset fixe pour lancer la génération des suivants
        Asset(
            Coordinates(0, 0),
            "src/assets/fleur.png",
            None,
            loaded_images["src/assets/fleur.png"],
        )
    ]
    for y in range(10, width, 10):
        for x in range(10, height, 10):
            valeur = (
                abs(sin(seed * x * y)) * 100
            )  # on génère un nombre entre 0 et 100 dépendant de la seed et des coordonnées
            if valeur >= 10:
                continue
            valeur = abs(cos(seed * x * y / 100)) * 100
            for i in range(3):
                modificateur = table[i][assets[-1].get_image_path()]
                image_path = image_paths[i]
                image = loaded_images[image_path]
                if valeur + modificateur >= 90:
                    image_path = image_paths[i]
                    asset = Asset(Coordinates(x, y), image_path, None, image)
                    assets.append(asset)
                    break
    # Génération des bases des joueurs en fonction de la taille de la map
    # print([str(asset) for asset in assets])
    # Order assets by y + height
    assets.sort(
        key=lambda asset: asset.get_position().get_y() + asset.get_height(),
    )  # Nico
    return assets


generate_map

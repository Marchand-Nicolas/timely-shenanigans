# crée par Elliot
from math import cos, sin, sqrt
from src.map.asset import Asset
from src.map.coordinates import Coordinates

table_gener = [
    {
        "nom": "src/assets/grass.png",
        "proba": 90,
        "src/assets/arbre.png": 5,
        "src/assets/fleur.png": -5,
        "src/assets/grass.png": 0,
        "src/assets/cottage.png": 0
    },
    {
        "nom": "src/assets/arbre.png",
        "proba": 98,
        "src/assets/grass.png": 3,
        "src/assets/fleur.png": -5,
        "src/assets/arbre.png": 3,
        "src/assets/cottage.png": -3
    },
    {
        "nom": "src/assets/fleur.png",
        "proba": 97,
        "src/assets/grass.png": 2,
        "src/assets/arbre.png": -5,
        "src/assets/fleur.png": -5,
        "src/assets/cottage.png": 0
    },
    {
       "nom": "src/assets/cottage.png",
       "proba": 99,
       "src/assets/grass.png": 0,
        "src/assets/arbre.png": -2,
        "src/assets/fleur.png": 0,
        "src/assets/cottage.png": -2  
    }
]

image_paths = ["src/assets/grass.png", "src/assets/arbre.png", "src/assets/fleur.png"]


def generate_map(seed: int, width: int, height: int, loaded_images: dict):
    """
    Génère de manière procédurale une carte à partir d'une graine.
    On n'utilise pas des nombres aléatoires, car l'objectif est de transmettre la graine
    aux autres joueurs.
    Out: Liste d'assets
    """
    assets = [  # On crée un asset fixe pour lancer la génération des suivants
        Asset(
            Coordinates(0, 0),
            "src/assets/fleur.png",
            None,
            loaded_images["src/assets/fleur.png"],
        )
    ]
    for y in range(10, width, 10):
        for x in range(10, height, 10):
            if abs(sin(seed * x * y)) * 100 > 8:
                continue
            for i in range(len(table_gener)):
                valeur = (
                    abs(cos(seed + (sin(x) + sqrt(y)) * 7 * (i + 1))) * 100
                )  # on génère un nombre entre 0 et 100 dépendant de la seed et des coordonnées
                modificateur = table_gener[i][assets[-1].get_image_path()]
                image_path = image_paths[i]
                image = loaded_images[image_path]
                if valeur + modificateur >= table_gener[i]["proba"]:
                    image_path = image_paths[i]
                    asset = Asset(Coordinates(x, y), image_path, None, image)
                    assets.append(asset)
                    break
    # print([str(asset) for asset in assets])
    # Order assets by y + height
    assets.sort(
        key=lambda asset: asset.get_position().get_y() + asset.get_height(),
    )  # Nico
    return assets


generate_map

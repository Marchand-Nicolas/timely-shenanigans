from world import *
from coordinates import *


def render(world: World, coordinates: Coordinates, fenetre):
    """
    Affiche le monde sur la fenêtre.
    -> On déplace le monde sur la fenêtre en fonction des coordonnées.
    """
    # Remplir l'arrière plan en vert
    fenetre.fill((0, 255, 0))
    # Récupérer

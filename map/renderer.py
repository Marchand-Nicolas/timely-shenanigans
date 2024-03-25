# Nico
from world import *
from coordinates import *
from generator import *
from ..utils.get_visible_assets import get_visible_assets


def render(world: World, coordinates: Coordinates, fenetre):
    """
    Affiche le monde sur la fenêtre.
    -> On déplace le monde sur la fenêtre en fonction des coordonnées.
    """
    # Remplir l'arrière plan en vert
    fenetre.fill((0, 255, 0))

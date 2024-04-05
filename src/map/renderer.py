# Nico
from src.map.world import *
from src.map.coordinates import *
from src.map.generator import *
from src.utils.get_visible_assets import *
from src.utils.create_screen import *


def render(world: World, coordinates: Coordinates, fenetre):
    """
    Affiche le monde sur la fenêtre.
    -> On déplace le monde sur la fenêtre en fonction des coordonnées.
    """
    # Remplir l'arrière plan en vert
    fenetre = create_screen()

    fenetre.fill((0, 255, 0))

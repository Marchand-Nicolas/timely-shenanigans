# Nico
from src.map.world import *
from src.map.coordinates import *
from src.map.generator import *
from src.utils.get_visible_assets import *
from src.utils.create_screen import *
from src.utils.screen import *


def render(world: World, coordinates: Coordinates, screen: Screen):
    """
    Affiche le monde sur la fenêtre.
    -> On déplace le monde sur la fenêtre en fonction des coordonnées.
    """
    pygame_screen = screen.get_pygame_screen()
    # Remplir l'arrière plan en vert
    pygame_screen.fill((63, 140, 75))

    # On récupère les assets visibles
    visible_assets = get_visible_assets(coordinates, world.get_assets(), screen)

    # On parcourt les assets visibles
    for asset in visible_assets:
        # On récupère la position de l'asset
        x, y = asset.get_position()

        # On récupère le chemin de l'image de l'asset
        image_path = asset.get_image()

        # On charge l'image
        image = pygame.image.load(image_path)

        # On affiche l'image sur la fenêtre
        pygame_screen.blit(image, (x - coordinates.get_x(), y - coordinates.get_y()))

    # Actualiser l'affichage
    pygame.display.flip()

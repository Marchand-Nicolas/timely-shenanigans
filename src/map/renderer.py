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

        # Dimensions de l'image
        image_width, image_height = image.get_rect().size

        # On récupère les dimensions de l'écran
        screen_width, screen_height = screen.get_dimensions()
        image = pygame.transform.scale(image, (asset.get_width(), (asset.get_width() * int(image.get_height())) / image.get_width()))


        x_on_screen = x - coordinates.get_x() + screen_width // 2 - image_width // 2
        y_on_screen = y - coordinates.get_y() + screen_height // 2 - image_height // 2

        # On affiche l'image sur la fenêtre
        pygame_screen.blit(image, (x_on_screen, y_on_screen))

    # Actualiser l'affichage
    pygame.display.flip()

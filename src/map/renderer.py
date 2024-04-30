# Nico
from src.map.world import *
from src.map.coordinates import *
from src.map.generator import *
from src.utils.get_visible_assets import *
from src.utils.create_screen import *
from src.utils.screen import *


def render(
    world: World,
    coordinates: Coordinates,
    screen: Screen,
    players: list,
    loaded_images: dict,
    code: str = None,
):
    """
    Affiche le monde sur la fenêtre.
    -> On déplace le monde sur la fenêtre en fonction des coordonnées.
    """
    arial24 = pygame.font.SysFont("arial", 24)
    arial12 = pygame.font.SysFont("arial", 12)
    pygame_screen = screen.get_pygame_screen()
    # Remplir l'arrière plan en vert
    pygame_screen.fill((63, 140, 75))

    # On récupère les assets visibles
    visible_assets = get_visible_assets(coordinates, world.get_assets(), screen)
    joueur_affiches = [False for _ in players]
    # On parcourt les assets visibles
    asset_amount = len(visible_assets)

    for asset_index in range(asset_amount):
        asset = visible_assets[asset_index]
        # On récupère la position de l'asset
        x, y = asset.get_position()

        # On récupère l'image de l'asset
        image_object = asset.get_image()

        # Dimensions de l'image
        image_width, image_height = image_object.get_width(), image_object.get_height()

        image = image_object.get_loaded_image()

        # On récupère les dimensions de l'écran
        screen_width, screen_height = screen.get_dimensions()

        x_on_screen = x - coordinates.get_x() + screen_width // 2 - image_width // 2
        y_on_screen = y - coordinates.get_y() + screen_height // 2

        # Placement des joueurs
        for i in range(len(players)):
            joueur_affiche = joueur_affiches[i]
            player = players[i]
            if not joueur_affiche:
                joueur_width = 70
                joueur_height = 70
                x_player_on_screen = (
                    player["x"]
                    - coordinates.get_x()
                    + screen_width // 2
                    - joueur_width // 2
                )
                y_player_on_screen = (
                    player["y"]
                    - coordinates.get_y()
                    + screen_height // 2
                    - joueur_height
                )
                if (
                    y_on_screen + image_height >= y_player_on_screen + joueur_height
                    or asset_index == asset_amount - 1
                ):
                    joueur = loaded_images["src/assets/player.png"].get_loaded_image()
                    username = arial24.render(
                        player["name"], True, pygame.Color(255, 255, 255)
                    )
                    pygame_screen.blit(
                        username,
                        (
                            x_player_on_screen + joueur_width // 2 - 50,
                            y_player_on_screen - 50,
                        ),
                    )
                    joueur = pygame.transform.scale(
                        joueur, (joueur_width, joueur_height)
                    )

                    if player["rotation"] == "left":
                        joueur = pygame.transform.flip(joueur, True, False)

                    pygame_screen.blit(joueur, (x_player_on_screen, y_player_on_screen))
                    joueur_affiches[i] = True

        # On affiche l'image sur la fenêtre
        pygame_screen.blit(image, (x_on_screen, y_on_screen))

        # On affiche le code s'il est présent
        if code:
            code_render = arial24.render(code, True, pygame.Color(255, 255, 255))
            pygame_screen.blit(code_render, (10, 10))

        # On affiche les coordonnées du joueur x / y (arrondies)
        coordinates_render = arial12.render(
            f"{round(coordinates.get_x())} / {round(coordinates.get_y())}",
            True,
            pygame.Color(255, 255, 255),
        )
        pygame_screen.blit(coordinates_render, (10, 40))

    # Actualiser l'affichage
    pygame.display.flip()

# Crée par Elliot & Nico
from ..map.coordinates import Coordinates
from .screen import Screen


def get_visible_assets(coordinates: Coordinates, assets: list, screen: Screen):
    visible_assets = []

    # Marge pour les assets, car cette fonction n'est pas appelée à chaque frame
    margin_multiplier = 1.2

    screen_width = screen.get_width() * margin_multiplier
    screen_height = screen.get_height() * margin_multiplier

    # Précalcul
    screen_x = coordinates.get_x()
    screen_y = coordinates.get_y()
    half_screen_width = screen_width // 2
    half_screen_height = screen_height // 2

    screen_left = screen_x - half_screen_width
    screen_right = screen_x + half_screen_width
    screen_top = screen_y - half_screen_height
    screen_bottom = screen_y + half_screen_height

    for asset in assets:
        x, y = asset.get_position()
        half_image_width = asset.get_width() // 2
        full_image_height = asset.get_height()

        left_edge = x - half_image_width
        right_edge = x + half_image_width
        top_edge = y - full_image_height
        bottom_edge = y + full_image_height
        if (
            right_edge > screen_left
            and left_edge < screen_right
            and bottom_edge > screen_top
            and top_edge < screen_bottom
        ):
            visible_assets.append(asset)

        # Les assets sont ordonnés par ordre croissant de y + height donc on peut arrêter la boucle dès qu'on dépasse le bas de l'écran
        if top_edge > screen_bottom:
            break
    return visible_assets

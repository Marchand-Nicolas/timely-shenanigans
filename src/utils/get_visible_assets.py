# Crée par Elliot & Nico
from ..map.coordinates import Coordinates
from .screen import Screen


def get_visible_assets(coordinates: Coordinates, assets: list, screen: Screen):
    visible_assets = []

    # Précalcul des coordonnées de l'écran
    screen_left = coordinates.get_x() - (screen.get_width() // 2)
    screen_right = coordinates.get_x() + (screen.get_width() // 2)
    screen_top = coordinates.get_y() - (screen.get_height() // 2)
    screen_bottom = coordinates.get_y() + (screen.get_height() // 2)

    for asset in assets:
        (x, y) = asset.get_position()
        image_width = asset.get_width()
        image_height = asset.get_height()

        left_edge = x - image_width // 2
        right_edge = x + image_width // 2
        top_edge = y - image_height
        bottom_edge = y + image_height

        if (
            screen_left < right_edge
            and left_edge < screen_right
            and screen_top < bottom_edge
            and top_edge < screen_bottom
        ):
            visible_assets.append(asset)

        if top_edge > screen_bottom:
            break
    return visible_assets

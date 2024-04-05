# Crée par Elliot
from ..map.coordinates import Coordinates
from .screen import Screen


def get_visible_assets(coordinates: Coordinates, assets: list, screen: Screen):
    visible_assets = []
    for asset in assets:
        (x, y) = asset.get_position()
        if coordinates.get_x() - (screen.get_width() // 2) < x < coordinates.get_x() + (
            screen.get_width() // 2
        ) and coordinates.get_y() - (
            screen.get_height() // 2
        ) < y < coordinates.get_y() + (
            screen.get_height() // 2
        ):
            visible_assets.append(asset)
    return visible_assets

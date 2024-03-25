# Crée par Elliot
from coordinates import *


class Asset:
    def __init__(self, coordinates: Coordinates, image: str, hitbox):
        self.coordinates = coordinates
        self.image = image
        self.hitbox = hitbox

    def get_coordinates(self):
        return self.coordinates

    def get_image(self):
        return self.image

    def get_hitbox(self):
        return self.hitbox

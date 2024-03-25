from coordinates import *


class Asset:
    def __init__(self, coordinates: Coordinates, image: str, hitbox):
        self.coordinates = coordinates
        self.image = image
        self.hitbox = hitbox

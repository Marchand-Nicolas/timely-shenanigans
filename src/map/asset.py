# Crée par Elliot
from src.map.coordinates import *


class Asset:
    def __init__(self, coordinates: Coordinates, image: str, hitbox, length: int):
        self.coordinates = coordinates
        self.image = image
        self.hitbox = hitbox

    def get_position(self):
        return self.coordinates

    def get_image(self):
        return self.image

    def get_hitbox(self):
        return self.hitbox
    
    def get_length(self):
        return self.get_length

    # Nico
    # Str method to print the asset
    def __str__(self):
        return f"Asset at {self.coordinates} with image {self.image} and hitbox {self.hitbox}"

# Crée par Elliot
from src.map.coordinates import *
from src.utils.load_images import Image


class Asset:
    def __init__(self, coordinates: Coordinates, image_path: str, hitbox, image: Image):
        self.coordinates = coordinates
        self.image_path = image_path
        self.image = image
        self.hitbox = hitbox
        self.width = image.get_width()
        self.height = image.get_height()

    def get_position(self):
        return self.coordinates

    def get_image_path(self):
        return self.image_path

    def get_image(self):
        return self.image

    def get_hitbox(self):
        return self.hitbox

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    # Nico
    # Str method to print the asset
    def __str__(self):
        return f"Asset at {self.coordinates} with image {self.image} and hitbox {self.hitbox}"

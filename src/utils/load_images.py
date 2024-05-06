import pygame
from src.utils.screen import Screen

# Nico


class Image(object):
    def __init__(self, path, width, height=None):
        self.path = path
        image = pygame.image.load(path)
        self.width = width
        self.image = pygame.transform.scale(
            image,
            (
                width,
                (
                    height
                    if height
                    else (width * int(image.get_height())) / image.get_width()
                ),
            ),
        )
        self.height = self.image.get_height()

    def get_image_path(self):
        return self.path

    def get_loaded_image(self):
        return self.image

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def set_dimensions(self, width, height):
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(
            self.image,
            (
                width,
                height,
            ),
        )

    def __str__(self):
        return f"Image at {self.path} with width {self.width} and height {self.height}"


def load_images(screen: Screen):
    return {
        "src/assets/grass.png": Image("src/assets/grass.png", 50),
        "src/assets/fleur.png": Image("src/assets/fleur.png", 24),
        "src/assets/arbre.png": Image("src/assets/arbre.png", 80),
        "src/assets/player.png": Image("src/assets/player.png", 70),
        "src/assets/hunter.png": Image("src/assets/hunter.png", 95),
        "src/assets/ghost.png": Image("src/assets/ghost.png", 40),
        "src/assets/vision.png": Image(
            "src/assets/vision.png", screen.get_width(), screen.get_height()
        ),
        "src/assets/cottage.png": Image("src/assets/cottage.png", 90),
        "src/assets/rock.png": Image("src/assets/rock.png", 70),
    }

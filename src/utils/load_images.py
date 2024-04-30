import pygame

# Nico


class Image(object):
    def __init__(self, path, width):
        self.path = path
        image = pygame.image.load(path)
        self.width = width
        self.image = pygame.transform.scale(
            image,
            (
                width,
                (width * int(image.get_height())) / image.get_width(),
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

    def __str__(self):
        return f"Image at {self.path} with width {self.width} and height {self.height}"


def load_images():
    return {
        "src/assets/grass.png": Image("src/assets/grass.png", 50),
        "src/assets/fleur.png": Image("src/assets/fleur.png", 24),
        "src/assets/arbre.png": Image("src/assets/arbre.png", 80),
        "src/assets/player.png": Image("src/assets/player.png", 70),
    }

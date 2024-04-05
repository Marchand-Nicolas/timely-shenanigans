# Nico
class Screen:
    def __init__(self, width, height, pygame_screen):
        self.width = width
        self.height = height
        self.pygame_screen = pygame_screen

    def get_width(self):  # Elliot
        return self.width

    def get_height(self):  # Elliot
        return self.height

    def get_pygame_screen(self):
        return self.pygame_screen

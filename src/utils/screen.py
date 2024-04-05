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

    def get_dimensions(self):  # Nico
        return self.width, self.height

    def get_pygame_screen(self):  # Nico
        return self.pygame_screen

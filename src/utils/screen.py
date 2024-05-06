# Nico, Elliot
class Screen:
    def __init__(self, width, height, pygame_screen):
        self.width = width
        self.height = height
        self.pygame_screen = pygame_screen

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_dimensions(self):
        return self.width, self.height

    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

    def get_pygame_screen(self):
        return self.pygame_screen

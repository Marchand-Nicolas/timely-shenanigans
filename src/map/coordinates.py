# Nico


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    # Unpack coordinates
    def __iter__(self):
        return iter((self.x, self.y))

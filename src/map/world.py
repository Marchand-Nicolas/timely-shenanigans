# Nico
class World(object):
    def __init__(self, width, height, assets, spawn_points):
        self.width = width
        self.height = height
        self.assets = assets
        self.spawn_points = spawn_points

    def get_assets(self):
        return self.assets

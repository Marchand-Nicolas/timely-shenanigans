# Nico
class World(object):
    def __init__(self, width, height, assets, spawn_points):
        self.width = width
        self.height = height
        self.assets = assets
        self.spawn_points = spawn_points

    def get_assets(self):
        return self.assets

    # Str method to print the world
    def __str__(self):
        assets = ""
        for asset in self.assets:
            assets += f"\n{asset}"
        return f"World of size {self.width}x{self.height} with {len(self.assets)} assets and {len(self.spawn_points)} spawn points.{assets}"

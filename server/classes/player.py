import time


class Player:
    def __init__(self, username, user_id):
        self.name = username
        self.id = user_id
        self.x = 0
        self.y = 0
        self.last_update = time.time()

    def update(self, x, y):
        self.x = x
        self.y = y
        self.last_update = time.time()

    def is_disconnected(self):
        return time.time() - self.last_update > 5

    def __str__(self):
        return f"Player {self.name} ({self.id})"

    # JSON serialization
    def to_json(self):
        return {"name": self.name, "id": self.id, "x": self.x, "y": self.y}

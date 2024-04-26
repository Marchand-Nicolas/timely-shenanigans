class Player:
    def __init__(self, username, user_id):
        self.name = username
        self.id = user_id
        self.x = 0
        self.y = 0

    def update(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Player {self.name} ({self.id})"

    # JSON serialization
    def to_json(self):
        return {"name": self.name, "id": self.id, "x": self.x, "y": self.y}

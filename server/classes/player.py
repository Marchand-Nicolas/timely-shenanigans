class Player:
    def __init__(self, username, user_id):
        self.name = username
        self.id = user_id

    def __str__(self):
        return f"Player {self.name} ({self.id})"

# Nico


class User:
    def __init__(self, username, id):
        self.username = username
        self.id = id

    def __str__(self):
        return f"username: {self.username}, id: {self.id}"

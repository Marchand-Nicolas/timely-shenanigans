class Game:
    def __init__(self, id: int, players: list, state: str, code: str, seed: str):
        self.id = id
        self.players = players
        self.state = state
        self.code = code
        self.seed = seed

    def get_player_count(self):
        return len(self.players)

    def get_players(self):
        return self.players

    def remove_player(self, player_id):
        self.players = [player for player in self.players if player.id != player_id]

    def __str__(self):
        return f"Game {self.id} with {len(self.players)} players and code {self.code}"

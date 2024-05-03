import random
import time


class Game:
    def __init__(self, id: int, players: list, state: str, code: str, seed: str):
        self.id = id
        self.players = players
        self.state = state
        self.code = code
        self.seed = seed
        self.state = "waiting"
        self.start_time = time.time()

    def get_player_count(self):
        return len(self.players)

    def get_players(self):
        return self.players

    def remove_player(self, player_id):
        self.players = [player for player in self.players if player.id != player_id]

    def start_game(self):
        self.state = "running"
        self.choose_new_hunter()
        self.start_time = time.time()

    def choose_new_hunter(self):
        hunter = random.choice(self.players)
        hunter.setHunter()
        for player in self.players:
            if player.id != hunter.id:
                player.setMate()

    def get_mates(self):
        return [player for player in self.players if player.state == "mate"]

    def kill_player(self, player_id):
        for player in self.players:
            if player.id == player_id:
                player.kill()
                break
        mates = self.get_mates()
        if len(mates) == 0:
            self.state = "finished"

    def __str__(self):
        return f"Game {self.id} with {len(self.players)} players and code {self.code}"

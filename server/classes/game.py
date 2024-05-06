import random
import time
from server.utils.get_game_duration import get_game_duration


class Game:
    def __init__(self, id: int, players: list, state: str, code: str, seed: str):
        self.id = id
        self.players = players
        self.state = state
        self.code = code
        self.seed = seed
        self.state = "waiting"
        self.start_time = time.time()
        self.end_time = None

    def get_player_count(self):
        return len(self.players)

    def get_players(self):
        return self.players

    def remove_player(self, player_id):
        self.players = [player for player in self.players if player.id != player_id]

    def start_game(self):
        # Check there is at least 2 players
        if len(self.players) < 2:
            return
        self.state = "running"
        self.choose_new_hunter()
        self.start_time = time.time()

    def restart_if_ended(self):
        if (
            self.start_time + get_game_duration(self.get_player_count()) < time.time()
            and self.state == "running"
        ):
            self.end_game()

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
            self.end_game()

    def end_game(self):
        self.state = "finished"
        self.end_time = time.time()

    def __str__(self):
        return f"Game {self.id} with {len(self.players)} players and code {self.code}"

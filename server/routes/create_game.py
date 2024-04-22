import json


def handle_create_game(body, state):
    print(body)

    return json.dumps({"status": "ok", "game_id": 1})

import pygame
from src.map.generator import generate_map
from src.map.renderer import render
from src.utils.game_loop import game_loop
from src.map.world import World
from src.map.coordinates import Coordinates
from src.utils.game_context import GameContext
from src.utils.game_loop import game_loop
from src.multiplayer.server_loop import server_loop
from src.utils.constants import world_width, world_height, speed
from src.utils.load_images import load_images
from src.utils.get_visible_assets import get_visible_assets
from src.multiplayer.kill_player import kill_player
from src.multiplayer.restart_game import restart_game
import threading
import time

# Nico, Elliot

game_state = {
    "state": "waiting",
    "start_time": time.time(),
}

players_server = []


def start_game(seed, screen, code=None, player_id=0):

    loaded_images = load_images()

    generated_assets = generate_map(seed, world_width, world_height, loaded_images)

    world = World(world_width, world_height, generated_assets, [(100, 100)])

    player_coordinates = Coordinates(world_width // 2, world_height // 2)

    right, left, up, down = (False, False, False, False)

    last_time = 0

    stop_threads = False

    get_exit_app = lambda: stop_threads

    # On créé un thread pour le serveur, car les appels réseau bloqueraient le jeu
    # autrement.
    if code:
        threading.Thread(
            target=lambda: server_loop(
                code,
                players_server,
                player_id,
                get_exit_app,
                player_coordinates,
                game_state,
            )
        ).start()

    players_client = []

    # On stocke les joueurs, avec leurs positions actuelles.
    def sync_players(distance):
        # On vérifie que tous les joueurs sont bien dans la liste.
        for player in players_server:
            if player["id"] not in [p["id"] for p in players_client]:
                print("Loading player", player["id"])
                player["rotation"] = "right"
                players_client.append(player)
        # On supprime les joueurs qui ne sont plus dans la partie.
        for player in players_client:
            if player["id"] not in [p["id"] for p in players_server]:
                print("Unloading player", player["id"])
                players_client.remove(player)
        # On met à jour les positions des joueurs en fonction de la vitesse.
        for client_player in players_client:
            server_player = None
            for p in players_server:
                if p["id"] == client_player["id"]:
                    server_player = p
            if not server_player:
                print("Player not found in server list, but present in client list.")
                continue
            x_distance = abs(client_player["x"] - server_player["x"])
            y_distance = abs(client_player["y"] - server_player["y"])
            x_movement = min(distance, x_distance)
            y_movement = min(distance, y_distance)
            distance = (x_distance**2 + y_distance**2) ** 0.5
            # Si la distance est plus grande que la distance parcourue en une seconde,
            # on accélère le mouvement en fonction de la distance.
            if distance > speed:
                multiplier = distance / speed
                if multiplier < 2:
                    x_movement *= 1.5
                    y_movement *= 1.5
                else:
                    # On téléporte le joueur si la distance est trop grande.
                    client_player["x"] = server_player["x"]
                    client_player["y"] = server_player["y"]
            if client_player["x"] != server_player["x"]:
                client_player["rotation"] = (
                    "right" if client_player["x"] < server_player["x"] else "left"
                )
            client_player["x"] += (
                x_movement if client_player["x"] < server_player["x"] else -x_movement
            )
            client_player["y"] += (
                y_movement if client_player["y"] < server_player["y"] else -y_movement
            )

    player_rotation = "right"

    visible_assets = []
    time_since_last_asset_refresh = 0

    def refresh():
        nonlocal last_time
        nonlocal player_rotation
        nonlocal time_since_last_asset_refresh
        nonlocal visible_assets
        current_time = time.time()
        delta = current_time - last_time
        distance = speed * delta

        player_coordinates.x += (
            distance if right and player_coordinates.x <= world_height else 0
        )
        if right:
            player_rotation = "right"
        elif left:
            player_rotation = "left"
        player_coordinates.x -= distance if left and player_coordinates.x >= 0 else 0
        player_coordinates.y -= distance if up and player_coordinates.y >= 0 else 0
        player_coordinates.y += (
            distance if down and player_coordinates.y <= world_height else 0
        )

        sync_players(distance)
        players_copy = players_client.copy()
        players_copy.append(
            {
                "name": "",
                "id": player_id,
                "x": player_coordinates.get_x(),
                "y": player_coordinates.get_y(),
                "rotation": player_rotation,
            }
        )

        # On récupère les assets visibles
        if time_since_last_asset_refresh > 0.3:
            visible_assets = get_visible_assets(
                player_coordinates, world.get_assets(), screen
            )
            time_since_last_asset_refresh = 0

        render(
            visible_assets,
            player_coordinates,
            screen,
            players_copy,
            loaded_images,
            code,
        )
        last_time = current_time
        time_since_last_asset_refresh += delta

    ctrl_pressed = False

    def process_event(event):
        nonlocal right, left, up, down, ctrl_pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True
            if event.key == pygame.K_SPACE:
                for player in players_server:
                    id = player["id"]
                    if player["state"] == "mate":
                        if (
                            abs(player_coordinates[0] - player["x"]) <= 10
                            and abs(player_coordinates[1] - player["y"]) <= 10
                        ):
                            kill_player(id, code)
            if event.key == pygame.K_LCTRL:
                ctrl_pressed = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False
            if event.key == pygame.K_LCTRL:
                ctrl_pressed = False
            # Le host peut appuyer
            if player_id == 0 and event.key == pygame.K_r and ctrl_pressed:
                restart_game(code)

    def on_exit():
        nonlocal stop_threads
        stop_threads = True

    context = GameContext(refresh, process_event, on_exit)

    game_loop(screen=screen, context=context)

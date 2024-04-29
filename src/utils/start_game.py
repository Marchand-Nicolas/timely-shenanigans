import pygame
from src.utils.create_screen import create_screen
from src.map.generator import generate_map
from src.map.renderer import render
from src.utils.game_loop import game_loop
from src.map.world import World
from src.map.coordinates import Coordinates
from src.utils.game_context import GameContext
from src.utils.game_loop import game_loop
from src.multiplayer.server_loop import server_loop
import threading
import time

# Nico, Elliot

players_server = []


def start_game(seed, code=None, player_id=0):
    screen = create_screen()

    map_x = 2000
    map_y = 2000
    generated_assets = generate_map(seed, map_x, map_y)

    world = World(500, 500, generated_assets, [(100, 100)])

    player_coordinates = Coordinates(200, 200)

    right, left, up, down = (False, False, False, False)

    last_time = 0

    stop_threads = False

    get_exit_app = lambda: stop_threads



    # On créé un thread pour le serveur, car les appels réseau bloqueraient le jeu
    # autrement.
    if code:
        threading.Thread(
            target=lambda: server_loop(
                code, players_server, player_id, get_exit_app, player_coordinates
            )
        ).start()

    players_client = []

    # On stocke les joueurs, avec leurs positions actuelles.
    def sync_players(speed):
        # On vérifie que tous les joueurs sont bien dans la liste.
        for player in players_server:
            if player["id"] not in [p["id"] for p in players_client]:
                print("Loading player", player["id"])
                player["rotation"] = "right"
                players_client.append(player)
        # On met à jour les positions des joueurs en fonction de la vitesse.
        for client_player in players_client:
            server_player = None
            for p in players_server:
                if p["id"] == client_player["id"]:
                    server_player = p
            if not server_player:
                print("Player not found in server list, but present in client list.")
                continue
            x_distance = min(speed, abs(client_player["x"] - server_player["x"]))
            y_distance = min(speed, abs(client_player["y"] - server_player["y"]))
            client_player["rotation"] = "right" if client_player["x"] < server_player["x"] else "left"
            client_player["x"] += (
                x_distance if client_player["x"] < server_player["x"] else -x_distance
            )
            client_player["y"] += (
                y_distance if client_player["y"] < server_player["y"] else -y_distance
            )

    def refresh():
        nonlocal last_time
        current_time = time.time()
        delta = current_time - last_time
        speed = 200 * delta
        global player_rotation

        player_coordinates.x += speed if right and player_coordinates.x <= map_x else 0
        player_rotation = "right" if right and player_coordinates.x <= map_x else 0
        player_coordinates.x -= speed if left and player_coordinates.x >= 0 else 0
        player_rotation = "left" if left and player_coordinates.x >= 0 else 0
        player_coordinates.y -= speed if up and player_coordinates.y >= 0 else 0
        player_coordinates.y += speed if down and player_coordinates.y <= map_y else 0

        sync_players(speed)
        players_copy = players_client.copy()
        players_copy.append(
            {
                "name": "",
                "id": player_id,
                "x": player_coordinates.get_x(),
                "y": player_coordinates.get_y(),
                "rotation": player_rotation
            }
        )

        render(world, player_coordinates, screen, players_copy)
        last_time = current_time

    def process_event(event):
        nonlocal right, left, up, down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False

        # Mettre à jour les dimensions de l'écran si la fenêtre est redimensionnée
        if event.type == pygame.VIDEORESIZE:
            screen.set_dimensions(event.w, event.h)

    def on_exit():
        nonlocal stop_threads
        stop_threads = True

    context = GameContext(refresh, process_event, on_exit)

    game_loop(context)

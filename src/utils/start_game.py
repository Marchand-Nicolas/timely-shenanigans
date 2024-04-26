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


def start_game(seed, code=None, player_id=0):
    screen = create_screen()

    generated_assets = generate_map(seed, 2000, 2000, 2)

    world = World(500, 500, generated_assets, [(100, 100)])

    player_coordinates = Coordinates(200, 200)

    right, left, up, down = (False, False, False, False)

    last_time = 0

    players = []

    stop_threads = False

    get_exit_app = lambda: stop_threads

    # On créé un thread pour le serveur, car les appels réseau bloqueraient le jeu
    # autrement.
    if code:
        threading.Thread(
            target=lambda: server_loop(
                code, players, player_id, get_exit_app, player_coordinates
            )
        ).start()

    def refresh():
        nonlocal last_time
        current_time = time.time()
        delta = current_time - last_time
        speed = 200 * delta
        player_coordinates.x += speed if right else 0
        player_coordinates.x -= speed if left else 0
        player_coordinates.y -= speed if up else 0
        player_coordinates.y += speed if down else 0
        players_copy = players.copy()
        players_copy.append(
            {
                "name": "",
                "id": player_id,
                "x": player_coordinates.get_x(),
                "y": player_coordinates.get_y(),
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

    def on_exit():
        nonlocal stop_threads
        stop_threads = True

    context = GameContext(refresh, process_event, on_exit)

    game_loop(context)

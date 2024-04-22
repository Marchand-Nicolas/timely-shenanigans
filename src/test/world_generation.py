import pygame
from src.utils.create_screen import create_screen
from src.map.generator import generate_map
from src.map.renderer import render
from src.utils.game_loop import game_loop
from src.map.world import World
from src.map.coordinates import Coordinates
from src.utils.game_context import GameContext

screen = create_screen()
generated_assets = generate_map(1234567890, 2000, 2000, 2)

world = World(500, 500, generated_assets, [(100, 100)])

player_coordinates = Coordinates(200, 200)

right, left, up, down = (False, False, False, False)


def refresh():
    speed = 20
    global left, right, up, down
    player_coordinates.x += speed if right else 0
    player_coordinates.x -= speed if left else 0
    player_coordinates.y -= speed if up else 0
    player_coordinates.y += speed if down else 0
    render(world, player_coordinates, screen)


def process_event(event):
    global left, right, up, down
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

context = GameContext(refresh, process_event)

game_loop(context)

from src.utils.create_screen import create_screen
from src.map.generator import generate_map
from src.map.renderer import render
from src.utils.game_loop import game_loop
from src.map.world import World
from src.map.coordinates import Coordinates
from src.utils.game_context import GameContext

screen = create_screen()
generated_assets = generate_map(1234567890, 2000, 2000, 2)

world = World(2000, 2000, generated_assets, [(1000, 1000)])

player_coordinates = Coordinates(200, 1000)


def refresh():
    render(world, player_coordinates, screen)


def process_event(event):
    print(event)


context = GameContext(refresh, process_event)

game_loop(context)

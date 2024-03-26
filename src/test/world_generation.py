from src.utils.create_screen import create_screen
from src.map.generator import generate_map
from src.map.renderer import render

screen = create_screen()
generated_assets = generate_map(123456789, 2000, 2000, 2)

render(screen, generated_assets, (0, 0))

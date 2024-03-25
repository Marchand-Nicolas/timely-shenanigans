from ..utils.create_screen import create_screen
from ..map.generator import generate_map
from ..map.renderer import render

screen = create_screen()
generated_assets = generate_map(123456789, 2000, 2000, 2)

render(screen, generated_assets, (0, 0))


(x, y) = asset.get_coordinates()

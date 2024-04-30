from src.utils.join_game import join_game
from src.utils.create_screen import create_screen


# Nico

code = input("Enter the game code: ")

screen = create_screen()

join_game("Pomme", screen, code)

# Nicolas

import pygame
from src.utils.screen import Screen


def create_screen(width=1000, height=500):
    pygame.init()  # initialisation du module "pygame"

    pygame_screen = pygame.display.set_mode(
        (width, height),  # pygame.FULLSCREEN
        # On autorise le redimensionnement de la fenêtre
        pygame.RESIZABLE,
    )  # Création d'une fenêtre graphique de taille 600x600 pixels

    screen = Screen(width, height, pygame_screen)
    return screen

import pygame


def create_screen():
    pygame.init()  # initialisation du module "pygame"

    screen = pygame.display.set_mode(
        (0, 0), pygame.FULLSCREEN
    )  # Création d'une fenêtre graphique de taille 600x600 pixels
    return screen

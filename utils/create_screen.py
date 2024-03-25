import pygame


def create_screen():
    pygame.init()  # initialisation du module "pygame"

    screen = pygame.display.set_mode(
        (800, 500)
    )  # Création d'une fenêtre graphique de taille 600x600 pixels
    return screen

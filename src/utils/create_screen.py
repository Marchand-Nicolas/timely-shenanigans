import pygame


def create_screen():
    pygame.init()  # initialisation du module "pygame"

    screen = pygame.display.set_mode(
        (1000, 500)  # pygame.FULLSCREEN
    )  # Création d'une fenêtre graphique de taille 600x600 pixels


create_screen()

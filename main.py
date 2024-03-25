# -*- coding: utf-8 -*-

import pygame
from menus.first_menu import show_first_menu
from utils.createe_scrr

pygame.init()  # initialisation du module "pygame"

screen = pygame.display.set_mode(
    (0, 0), pygame.FULLSCREEN
)  # Création d'une fenêtre graphique de taille 600x600 pixels
pygame.display.set_caption("Space Invader")  # Définit le titre de la fenêtre

show_first_menu(screen)

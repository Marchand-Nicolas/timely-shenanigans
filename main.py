# -*- coding: utf-8 -*-

import pygame
from utils.create_screen import create_screen
from menus.first_menu import show_first_menu

"sdfdsq"

screen = create_screen()  # Création d'une fenêtre graphique
pygame.display.set_caption("Space Invader")  # Définit le titre de la fenêtre

show_first_menu(screen)

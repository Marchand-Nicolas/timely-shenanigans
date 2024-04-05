# -*- coding: utf-8 -*-

import pygame
from src.utils.create_screen import create_screen
from src.menus.first_menu import show_first_menu
from src.utils.game_loop import game_loop

screen = create_screen()  # Création d'une fenêtre graphique
pygame.display.set_caption("Space Invader")  # Définit le titre de la fenêtre

show_first_menu(screen)
game_loop()

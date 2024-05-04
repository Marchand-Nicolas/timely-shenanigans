# -*- coding: utf-8 -*-

""" 
Pour lancer le jeu, entrez:
python -m src.main
dans la console

pour tester la génération et les déplacements sans multi:
python -m src.test.world_generation

Si le serveur n'est pas allumé, vous pouvez aller dans src/utiils/constants.py et mettre l'ip à localhost:port pour vous connecter au serveur local
et pour le lancer : python -m server.server
"""

import pygame
from src.utils.create_screen import create_screen
from src.menus.first_menu import show_first_menu

screen = create_screen()  # Création d'une fenêtre graphique
pygame.display.set_caption("Space Invader")  # Définit le titre de la fenêtre

show_first_menu(screen)

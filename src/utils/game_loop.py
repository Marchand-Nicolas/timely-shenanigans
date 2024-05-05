# Nico

import pygame
from src.utils.game_context import GameContext


def game_loop(screen, context=None):
    if context is None:
        context = GameContext()
    run = True
    while run:
        for event in pygame.event.get():
            if context.get_on_event():
                # On appelle la fonction on_event à chaque événement
                context.get_on_event()(event)
            if event.type == pygame.QUIT:
                if context.get_on_exit():
                    # On appelle la fonction on_exit si l'événement est de type QUIT
                    context.get_on_exit()()
                    exit()
                run = False
            # Mettre à jour les dimensions de l'écran si la fenêtre est redimensionnée
            if event.type == pygame.VIDEORESIZE:
                screen.set_dimensions(event.w, event.h)

        if context.get_tick_event():
            # On appelle la fonction tick_event à chaque tour de boucle
            context.tick_event()

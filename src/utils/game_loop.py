# Nico

import pygame
from src.utils.game_context import GameContext


def game_loop(context=None):
    if context is None:
        context = GameContext()
    run = True
    while run:
        for event in pygame.event.get():
            if context.get_on_event():
                # On appelle la fonction on_event à chaque événement
                context.get_on_event()(event)
            if event.type == pygame.QUIT:
                run = False

        if context.get_tick_event():
            # On appelle la fonction tick_event à chaque tour de boucle
            context.tick_event()

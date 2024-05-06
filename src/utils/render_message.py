# Nico

import pygame
from src.utils.screen import Screen


def render_message(message, submessage, screen: Screen, important=False):
    """
    Affiche un message au centre de l'écran
    avec un sous-message en dessous de celui-ci
    """
    arial32 = pygame.font.SysFont("arial", 32)
    arial24 = pygame.font.SysFont("arial", 24)
    screen_width, screen_height = screen.get_dimensions()
    pygame_screen = screen.get_pygame_screen()
    message_render = arial32.render(message, True, pygame.Color(255, 255, 255))
    message_rect = message_render.get_rect(
        center=(screen_width // 2, screen_height // 2)
    )
    pygame_screen.blit(message_render, message_rect)
    submessage_render = arial24.render(submessage, True, pygame.Color(255, 255, 255))
    submessage_rect = submessage_render.get_rect(
        center=(screen_width // 2, screen_height // 2 + 30)
    )
    pygame_screen.blit(submessage_render, submessage_rect)

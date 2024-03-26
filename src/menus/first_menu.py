# quentin
import pygame


def show_first_menu(screen):
    rect = pygame.Rect(screen.get_width(), screen.get_height(), 50, 100)
    play_button = pygame.draw.rect(screen, (255, 45, 0), rect)

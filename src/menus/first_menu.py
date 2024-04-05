# quentin
import pygame


def show_first_menu(screen):
    rect = pygame.Rect(screen.get_width(), 100, 50, 100)
    run = True
    while run:
        
        pygame.draw.rect(screen, (255, 255, 255), rect)
        pygame.display.flip()
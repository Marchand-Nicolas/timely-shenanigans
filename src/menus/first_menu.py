# quentin
import pygame


def show_first_menu(screen):
    rect = pygame.Rect(100, 100, 50, 100)
    run = True
    while run:    
        pygame.draw.rect(screen, (255, 0, 0), rect)        
        pygame.display.flip()
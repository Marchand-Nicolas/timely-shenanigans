# quentin
import pygame


def show_first_menu(screen):
    run = True
    while run:    
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(100, 100, 50, 100))        
        pygame.display.flip()

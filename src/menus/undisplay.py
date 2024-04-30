# quentin
import pygame

pygame.init()

def undisplay(screen):
    """
    fonction qui vas recouvrire l'ecrant d'un rectagle noire pour effacer les rectagles dessiner sur l'ecrant
    """
    rect_undisplay = pygame.Rect(0, 0, screen.get_width(), screen.get_height())
    pygame.draw.rect(screen.get_pygame_screen(), (0,0,0), rect_undisplay)
    pygame.display.flip()
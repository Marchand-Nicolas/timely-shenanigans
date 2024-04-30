#quentin
import pygame

pygame.init()
arial24 = pygame.font.SysFont("arial", 24)

def enter_text(text_rect, screen, coordinates):
    """
    fonction qui vas gerer l'entrer d-un texte et sont affichage
    in: text_rect qui est le rectangle dnas le quel ecrire pour pouvoir le rafrechire, screen est l'ecrent sur lequel ecrire et coordinates sont les coordonner ou ecrire le text
    Out: renvoi le text ecrit
    """
    pygame.draw.rect(screen.get_pygame_screen(), (255, 255, 255), text_rect)
    pygame.display.flip()
    text = ""
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == 13:  # cas pour la touche entrer
                    return (text, True)
                elif event.key == 8 and text != "":  # cas pour le backspac
                    text = text[:-1]
                elif (
                    event.key == 8 and text == ""
                ):  # cas pour le backspac quand il n'y a pas de psedo
                    pass
                elif(
                    (event.key > 122 or event.key < 97) and (event.key < 48 or event.key > 57)
                ):
                    pass
                elif event.key == 32:  # cas pour les espaces
                    text += " "
                else:
                    text += pygame.key.name(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if not text_rect.collidepoint(
                    x, y
                ):  # si le joueur clique hors du rectengle d'entrer de texte
                    return (text, False)
        pygame.draw.rect(screen.get_pygame_screen(), (255, 255, 255), text_rect)
        text_name = arial24.render(text, True, pygame.Color(0, 0, 0))
        screen.get_pygame_screen().blit(text_name, coordinates)
        pygame.display.flip()

# quentin
import pygame
from tkinter import messagebox
from src.utils.create_game import create_game
from src.utils.join_game import join_game

pygame.init()

background_color = (0, 0, 0)
arial24 = pygame.font.SysFont("arial", 24)


def undisplay(screen):
    """
    fonction qui vas recouvrire l'ecrant d'un rectagle noire pour effacer les rectagles dessiner sur l'ecrant
    """
    rect_undisplay = pygame.Rect(0, 0, screen.get_width(), screen.get_height())
    pygame.draw.rect(screen.get_pygame_screen(), background_color, rect_undisplay)
    pygame.display.flip()


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


def menu_choose_game(screen, name):
    code = ""
    rect_creat_world = pygame.Rect(
        screen.get_width() // 2 - 150, screen.get_height() // 3 - 50, 300, 50
    )
    rect_join_world = pygame.Rect(
        screen.get_width() // 2 - 150, screen.get_height() // 3 + 50, 300, 50
    )
    rect_enter_code_to_join = pygame.Rect(
        screen.get_width() // 2 - 150, screen.get_height() // 3 + 125, 300, 50
    )
    rect_code = pygame.Rect(
        screen.get_width() // 2 - 150, screen.get_height() // 3 + 175, 300, 50
    )
    text_creat_world = arial24.render("create a new game", True, pygame.Color(0, 0, 0))
    text_join_world = arial24.render("join a game", True, pygame.Color(0, 0, 0))
    text_enter_code = arial24.render("enter a code:", True, pygame.Color(0, 0, 0))
    botton_join_clic = False
    running = True
    while running:
        code_text = arial24.render(code, True, pygame.Color(0, 0, 0))
        # dessine les bouton pour rejoidre ou cree un monde
        pygame.draw.rect(screen.get_pygame_screen(), (255, 255, 255), rect_creat_world)
        pygame.draw.rect(screen.get_pygame_screen(), (255, 255, 255), rect_join_world)
        screen.get_pygame_screen().blit(
            text_creat_world,
            (screen.get_width() // 2 - 150, screen.get_height() // 3 - 50),
        )
        screen.get_pygame_screen().blit(
            text_join_world,
            (screen.get_width() // 2 - 150, screen.get_height() // 3 + 50),
        )
        screen.get_pygame_screen().blit(
            text_enter_code,
            (screen.get_width() // 2 - 150, screen.get_height() // 3 + 125),
        )
        if botton_join_clic == True:
            pygame.draw.rect(
                screen.get_pygame_screen(), (255, 255, 255), rect_enter_code_to_join
            )
            pygame.draw.rect(screen.get_pygame_screen(), (255, 255, 255), rect_code)
            screen.get_pygame_screen().blit(
                text_enter_code,
                (screen.get_width() // 2 - 150, screen.get_height() // 3 + 125),
            )
            screen.get_pygame_screen().blit(
                code_text,
                (screen.get_width() // 2 - 150, screen.get_height() // 3 + 175),
            )
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if rect_creat_world.collidepoint(x, y):
                    return create_game(name, screen)
                if rect_join_world.collidepoint(x, y):
                    if code != "":
                        return join_game(name, screen, code)
                    botton_join_clic = True
                elif (
                    rect_enter_code_to_join.collidepoint(x, y)
                    or rect_code.collidepoint(x, y)
                    or rect_join_world.collidepoint(x, y)
                ) and botton_join_clic == True:
                    code = enter_text(
                        rect_code,
                        screen,
                        (screen.get_width() // 2 - 150, screen.get_height() // 3 + 175),
                    )


def show_first_menu(screen):
    name = ""
    title_game = arial24.render("game's title", True, pygame.Color(255, 255, 255))
    play_buton = pygame.Rect(
        screen.get_width() // 2 - 50, screen.get_height() // 2 - 50, 100, 100
    )
    text_enter_name_rect = pygame.Rect(
        screen.get_width() // 2 - 150, screen.get_height() // 2 + 100, 300, 50
    )
    enter_name_rect = pygame.Rect(
        screen.get_width() // 2 - 150, screen.get_height() // 2 + 150, 300, 50
    )
    text_enter_name = arial24.render("enter your name", True, pygame.Color(0, 0, 0))
    running = True
    while running:
        # dessine les objets du menu principale
        psedo_text = arial24.render(name, True, pygame.Color(0, 0, 0))
        pygame.draw.rect(screen.get_pygame_screen(), (255, 0, 0), play_buton)
        pygame.draw.rect(
            screen.get_pygame_screen(), (255, 255, 255), text_enter_name_rect
        )
        pygame.draw.rect(screen.get_pygame_screen(), (255, 255, 255), enter_name_rect)
        screen.get_pygame_screen().blit(
            title_game, (screen.get_width() // 2 - 50, screen.get_height() // 2 - 100)
        )
        screen.get_pygame_screen().blit(
            text_enter_name,
            (screen.get_width() // 2 - 150, screen.get_height() // 2 + 100),
        )
        screen.get_pygame_screen().blit(
            psedo_text, (screen.get_width() // 2 - 150, screen.get_height() // 2 + 150)
        )
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if enter_name_rect.collidepoint(
                    x, y
                ) or text_enter_name_rect.collidepoint(
                    x, y
                ):  # detecte si la sourie est cliquer dans le rect d'entrer de nom
                    text = enter_text(
                        enter_name_rect,
                        screen,
                        (screen.get_width() // 2 - 150, screen.get_height() // 2 + 150),
                    )
                    name = text[0]
                    if text[1] == True:
                        undisplay(screen)
                        return menu_choose_game(screen, name)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if play_buton.collidepoint(
                    x, y
                ):  # detecte si la sourie est cliquer dans le rect de debut de jeu
                    if name == "enter your name" or name == "":
                        messagebox.showinfo(
                            "user name",
                            "il faut entrer un nom d'utilisateur pour pouvoir jouer",
                        )
                    else:
                        undisplay(screen)
                        menu_choose_game(screen, name)
                        running = False

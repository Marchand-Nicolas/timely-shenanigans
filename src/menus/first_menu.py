# quentin
import pygame
from tkinter import messagebox
from src.menus.menu_choose_game import menu_choose_game
from src.menus.undisplay import undisplay
from src.menus.enter_text import enter_text


arial24 = pygame.font.SysFont("arial", 24)

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

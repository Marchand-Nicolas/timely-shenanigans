import pygame
from tkinter import messagebox
from src.menus.enter_text import enter_text
from src.utils.create_game import create_game
from src.utils.join_game import join_game

pygame.init()
arial24 = pygame.font.SysFont("arial", 24)


def menu_choose_game(screen, name):
    code = ""
    rect_creat_world = pygame.Rect(
        screen.get_width() // 2 - 150, screen.get_height() // 3 - 50, 300, 50
    )
    rect_join_world = pygame.Rect(
        screen.get_width() // 3 + 350, screen.get_height() // 3 + 75, 50, 50
    )
    rect_enter_code_to_join = pygame.Rect(
        screen.get_width() // 2 - 150, screen.get_height() // 3 + 50, 300, 50
    )
    rect_code = pygame.Rect(
        screen.get_width() // 2 - 150, screen.get_height() // 3 + 100, 300, 50
    )
    text_creat_world = arial24.render("create a new game", True, pygame.Color(0, 0, 0))
    text_join_world = arial24.render("join", True, pygame.Color(0, 0, 0))
    text_enter_code = arial24.render("enter a code:", True, pygame.Color(0, 0, 0))
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
            (screen.get_width() // 3 + 350, screen.get_height() // 3 + 75),
        )
        screen.get_pygame_screen().blit(
            text_enter_code,
            (screen.get_width() // 2 - 150, screen.get_height() // 3 + 125),
        )
        pygame.draw.rect(
            screen.get_pygame_screen(), (255, 255, 255), rect_enter_code_to_join
        )
        pygame.draw.rect(screen.get_pygame_screen(), (255, 255, 255), rect_code)
        screen.get_pygame_screen().blit(
            text_enter_code,
            (screen.get_width() // 2 - 150, screen.get_height() // 3 + 50, 300, 50),
        )
        screen.get_pygame_screen().blit(
            code_text,
            (screen.get_width() // 2 - 150, screen.get_height() // 3 + 100),
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
                    else:
                        messagebox.showinfo('code', 'il faut un code')
                elif (
                    rect_enter_code_to_join.collidepoint(x, y)
                    or rect_code.collidepoint(x, y)
                    or rect_join_world.collidepoint(x, y)
                ):
                    text = enter_text(
                        rect_code,
                        screen,
                        (screen.get_width() // 2 - 150, screen.get_height() // 3 + 100),
                    )
                    code = text[0]
                    if text[1] == True:
                        return join_game(name,code)
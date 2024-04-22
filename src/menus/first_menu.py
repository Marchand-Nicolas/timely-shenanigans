# quentin
import pygame

arial24 = pygame.font.SysFont("arial", 24)


def show_first_menu(screen):
    title_game = arial24.render("titre du jeu", True, pygame.Color(255, 255, 255))
    play_buton = pygame.Rect(
        screen.get_width() // 2 - 50, screen.get_height() // 2 - 50, 100, 100
    )
    running = True
    list = [play_buton]
    while running:
        # screen.blit(title_game, (screen.get_width()//2 - 50, screen.get_height()//2 - 100))
        # pygame.draw.rect(screen, (255, 0, 0), play_buton)
        # pygame.display.flip()
        display(list, screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if play_buton.collidepoint(x, y):
                    list = []
                    display(list, screen)
                    print("p")


def display(list, screen):
    if list == []:
        pygame.display.update()
    else:
        for elt in list:
            pygame.draw.rect(screen, (255, 0, 0), elt)
            pygame.display.flip()

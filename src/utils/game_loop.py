import pygame


def game_loop():
    run = True
    while run:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                run = False

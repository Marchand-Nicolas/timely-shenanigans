# quentin
import pygame
from tkinter import messagebox

background_color = (0,0,0)
arial24 = pygame.font.SysFont("arial",24)

def undisplay(screen):
    """
        fonction qui vas recouvrire l'ecrant d'un rectagle noire pour effacer les rectagles pres dessiner
    """
    rect_undisplay =  pygame.Rect(0, 0, screen.get_width(), screen.get_height())
    pygame.draw.rect(screen.get_pygame_screen(), background_color, rect_undisplay) 
    pygame.display.flip()
    
def menu_choose_game(screen):
    rect_creat_world = pygame.Rect(screen.get_width()//2 - 150, screen.get_height()//3 - 50, 300, 50)
    rect_join_world = pygame.Rect(screen.get_width()//2 - 150, screen.get_height()//3 + 50, 300, 50)
    running = True
    while running:
        pygame.draw.rect(screen.get_pygame_screen(), (255, 255, 255), rect_creat_world)
        pygame.draw.rect(screen.get_pygame_screen(), (255, 255, 255), rect_join_world)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        

def enter_name(enter_name_rect, screen):
    pygame.draw.rect(screen.get_pygame_screen(), (255, 255, 255), enter_name_rect)
    pygame.display.flip()  
    name = ''
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == 13: # cas pour la touche entrer 
                    return name
                elif event.key == 8 and name != '': # cas pour le backspac
                    name = name[:-1]
                else:
                    name += pygame.key.name(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos() 
                if not enter_name_rect.collidepoint(x, y):
                    return name
        text_name = arial24.render(name,True,pygame.Color(255,0,0))
        screen.get_pygame_screen().blit(text_name, (screen.get_width()//2 - 150, screen.get_height()//2 + 100))
        pygame.display.flip()  
                  
                   
def show_first_menu(screen):
    name = 'entrer votre psedo'
    title_game = arial24.render("titre du jeu",True,pygame.Color(255,255,255))
    play_buton = pygame.Rect(screen.get_width()//2 - 50, screen.get_height()//2 - 50, 100, 100)
    enter_name_rect = pygame.Rect(screen.get_width()//2 - 150, screen.get_height()//2 + 100 , 300, 100)
    running = True
    while running:
        psedo_text = arial24.render(name,True,pygame.Color(255,0,0))
        pygame.draw.rect(screen.get_pygame_screen(), (255, 0, 0), play_buton)        
        pygame.draw.rect(screen.get_pygame_screen(), (255, 255, 255), enter_name_rect)  
        screen.get_pygame_screen().blit(title_game, (screen.get_width()//2 - 50, screen.get_height()//2 - 100))
        screen.get_pygame_screen().blit(psedo_text, (screen.get_width()//2 - 150, screen.get_height()//2 + 100))      
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos() 
                if enter_name_rect.collidepoint(x, y):
                    name = enter_name(enter_name_rect, screen)
                    print(name)
                    if name == '':
                        name = 'entrer votre psedo'
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos() 
                if play_buton.collidepoint(x, y):
                    if name == 'entrer votre psedo':
                        messagebox.showinfo("nom utilisateur", "il faut entrer un nom d'utilisateur pour pouvoir jouer")
                    else:
                        undisplay(screen)
                        menu_choose_game(screen)
                        running = False
            
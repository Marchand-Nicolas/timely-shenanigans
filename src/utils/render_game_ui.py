# Nico, Elliot

import pygame
import time
from src.utils.get_game_duration import get_game_duration
from src.utils.render_message import render_message
from src.utils.screen import Screen


def render_game_ui(code, game, players, current_player, screen: Screen):
    arial48 = pygame.font.SysFont("arial", 48)
    arial24 = pygame.font.SysFont("arial", 24)
    screen_width, screen_height = screen.get_dimensions()
    pygame_screen = screen.get_pygame_screen()
    if code:
        code_render = arial24.render(code, True, pygame.Color(255, 255, 255))
        pygame_screen.blit(code_render, (10, 10))
        if game["state"] == "waiting":
            render_message(
                "Waiting for more players ...",
                "Share the code with your friends!",
                screen,
            )
        elif game["state"] == "running":
            countdown = 30 - time.time() + game["start_time"]
            if countdown >= 0:
                count_render = arial48.render(
                    str(round(countdown)), True, pygame.Color(255, 0, 0)
                )
                count_rect = count_render.get_rect(
                    center=(screen_width // 2, screen_height // 2)
                )
                pygame_screen.blit(count_render, count_rect)
            elif countdown >= -3:
                start_render = arial48.render("START", True, pygame.Color(255, 0, 0))
                start_rect = start_render.get_rect(
                    center=(screen_width // 2, screen_height // 2)
                )
                pygame_screen.blit(start_render, start_rect)
            else:
                remaining_players = 0
                for player in players:
                    if player["state"] == "mate":
                        remaining_players += 1
                remaining_render = arial24.render(
                    "Players remaining: " + str(remaining_players),
                    True,
                    pygame.Color(255, 255, 255),
                )
                pygame_screen.blit(remaining_render, (screen_width - 230, 10))
                time_remaining = round(
                    get_game_duration(len(players)) + game["start_time"] - time.time()
                )
                time_remaining_render = arial48.render(
                    str(time_remaining), True, pygame.Color(255, 0, 0)
                )
                pygame_screen.blit(time_remaining_render, (10, screen_height - 50))
        elif game["state"] == "finished":
            # Si le joueur est mate, on affiche un message
            if current_player["state"] == "mate":
                render_message(
                    "You survived! Well done " + current_player["name"],
                    "The mates won against the hunter",
                    screen,
                )
            # On regarde s'il reste des mates
            remaining_players = 0
            for player in players:
                if player["state"] == "mate":
                    remaining_players += 1
            if current_player["state"] == "dead":
                if remaining_players == 0:
                    render_message(
                        "You lost!",
                        "The hunter killed all the mates",
                        screen,
                    )
                else:
                    render_message(
                        "The hunter killed you...",
                        "But you won thanks to your mates!",
                        screen,
                    )
            elif current_player["state"] == "hunter":
                if remaining_players == 0:
                    render_message(
                        "You won! Well done " + current_player["name"],
                        "You killed all the mates",
                        screen,
                    )
                else:
                    render_message(
                        "You lost!",
                        "The mates won against you",
                        screen,
                    )

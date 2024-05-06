import pygame
import time
from src.utils.get_game_duration import get_game_duration


def render_game_ui(
    code,
    game_state,
    players,
    current_player,
    screen_width,
    screen_height,
    pygame_screen,
):
    arial48 = pygame.font.SysFont("arial", 48)
    arial24 = pygame.font.SysFont("arial", 24)
    arial12 = pygame.font.SysFont("arial", 12)
    if code:
        code_render = arial24.render(code, True, pygame.Color(255, 255, 255))
        pygame_screen.blit(code_render, (10, 10))
        if game_state["state"] == "waiting":
            wait_render = arial24.render(
                "Waiting for more players ...", True, pygame.Color(255, 0, 0)
            )
            pygame_screen.blit(wait_render, (10, screen_height - 30))
        elif game_state["state"] == "running":
            countdown = 30 - time.time() + game_state["start_time"]
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
                    get_game_duration(len(players))
                    + game_state["start_time"]
                    - time.time()
                )
                time_remaining_render = arial48.render(
                    str(time_remaining), True, pygame.Color(255, 0, 0)
                )
                pygame_screen.blit(time_remaining_render, (10, screen_height - 50))
        elif game_state["state"] == "finished":
            end_render = arial48.render("END", True, pygame.Color(255, 0, 0))
            end_rect = end_render.get_rect(
                center=(screen_width // 2, screen_height // 2)
            )
            pygame_screen.blit(end_render, end_rect)
            # Si le joueur est mate, on affiche un message
            if current_player["state"] == "mate":
                end_message = arial24.render(
                    "You survived! Well done " + current_player["name"],
                    True,
                    pygame.Color(255, 255, 255),
                )
                pygame_screen.blit(end_message, (10, 10))
                end_submessage = arial12.render(
                    "The mates won against the hunter",
                    True,
                    pygame.Color(255, 255, 255),
                )
                pygame_screen.blit(end_submessage, (10, 40))
            # On regarde s'il reste des mates
            remaining_players = 0
            for player in players:
                if player["state"] == "mate":
                    remaining_players += 1
            if current_player["state"] == "dead":
                if remaining_players == 0:
                    end_message = arial24.render(
                        "You lost!", True, pygame.Color(255, 255, 255)
                    )
                    pygame_screen.blit(end_message, (10, 10))
                    end_submessage = arial12.render(
                        "The hunter killed all the mates",
                        True,
                        pygame.Color(255, 255, 255),
                    )
                    pygame_screen.blit(end_submessage, (10, 40))
                else:
                    end_message = arial24.render(
                        "The hunter killed you...", True, pygame.Color(255, 255, 255)
                    )
                    pygame_screen.blit(end_message, (10, 10))
                    end_submessage = arial12.render(
                        "But you won thanks to your mates!",
                        True,
                        pygame.Color(255, 255, 255),
                    )
                    pygame_screen.blit(end_submessage, (10, 40))
            elif current_player["state"] == "hunter":
                if remaining_players == 0:
                    end_message = arial24.render(
                        "You won! Well done " + current_player["name"],
                        True,
                        pygame.Color(255, 255, 255),
                    )
                    pygame_screen.blit(end_message, (10, 10))
                    end_submessage = arial12.render(
                        "You killed all the mates", True, pygame.Color(255, 255, 255)
                    )
                    pygame_screen.blit(end_submessage, (10, 40))
                else:
                    end_message = arial24.render(
                        "You lost!", True, pygame.Color(255, 255, 255)
                    )
                    pygame_screen.blit(end_message, (10, 10))
                    end_submessage = arial12.render(
                        "The mates won against you", True, pygame.Color(255, 255, 255)
                    )

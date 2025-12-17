import pygame
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import programme.screen.Menu_screen as menu_screen
import programme.screen.Game_screen as game_screen
import programme.screen.Option_screen as option_screen
import programme.screen.Create_Game_screen as create_game_screen

from programme.utils.Constant import Screen
from programme.utils.LanguageManage import LanguageManager

# Déclarer les variables globales
screen_page = None
client = None
server = None

def set_client(cl):
    global client
    client = cl

def get_client():
    return client

def set_server(sv):
    global server
    server = sv

def get_server():
    return server

def change_page(page):
    global screen_page
    screen_page = page

def get_page():
    return screen_page

if __name__ == '__main__':
    # Initialisation de Pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("En Entreprise !")

    language = LanguageManager()

    running = True
    fullscreen = False
    screen_page = Screen.MENU.value
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if screen_page == Screen.MENU.value:
            menu_screen.menu_screen(screen, language, change_page, get_page, clock)
        elif screen_page == Screen.GAME.value:
            game_screen.Game_screen(screen, language, change_page, get_page, clock)
        elif screen_page == Screen.OPTION.value:
            option_screen.option_screen(screen, language, change_page, get_page, clock)
        elif screen_page == Screen.LOBBY.value:
            create_game_screen.Create_Game_screen(screen, language, change_page, get_page, clock)

    pygame.quit()

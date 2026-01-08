import pygame
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import screen.Menu_screen as menu_screen
import screen.Game_screen as game_screen
import screen.Option_screen as option_screen
import screen.Create_Game_screen as create_game_screen

from utils.Constant import Screen
from utils.LanguageManage import LanguageManager

# Déclarer les variables globales
screen_page = None
client = None

def set_client(cl):
    global client
    client = cl

def get_client():
    return client

def change_page(page):
    global screen_page
    print(f"change_page : {page}")
    screen_page = page

def get_page():
    return screen_page

if __name__ == '__main__':
    # Initialisation de Pygame
    pygame.init()
    screen = pygame.display.set_mode((1920 , 1080))
    pygame.display.set_caption("En Entreprise !")
    #pygame.display.toggle_fullscreen()

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
            game_screen.Game_screen(screen, language, get_client, change_page, get_page, clock)
        elif screen_page == Screen.OPTION.value:
            option_screen.option_screen(screen, language, change_page, get_page, clock)
        elif screen_page == Screen.LOBBY.value:
            create_game_screen.Create_Game_screen(screen, language, set_client, get_client, change_page, get_page, clock)

    pygame.quit()

import pygame
<<<<<<< HEAD
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
    print(f"change_page : {page}")
    screen_page = page
=======
import screen.Menu_screen as menu_screen
import screen.Game_screen as game_screen

def evnt_fullscreen():
    global fullscreen, screen
    fullscreen = not fullscreen
    if fullscreen:
        screen = pygame.display.set_mode((800,600), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((800,600))

def change_page(page):
    global screen_page
    screen_page = page
    print("Change page")
>>>>>>> 9212f0b01ed2a1573c52b80ae04bc537e3cd42a3

def get_page():
    return screen_page

if __name__ == '__main__':
    # Initialisation de Pygame
    pygame.init()
<<<<<<< HEAD
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
=======
    screen = pygame.display.set_mode((1920 , 1080))
    pygame.display.set_caption("En Entreprise !")

    running = True
    fullscreen = False
    screen_page = 0
    clock = pygame.time.Clock()

    while running:
        if screen_page == 0:
            menu_screen.menu_screen(screen, change_page, get_page, clock)
        if screen_page == 1:
            game_screen.Game_screen(screen, change_page, get_page, clock)
        if screen_page == 2:
            print("Option")
            change_page(0)

    pygame.quit()
>>>>>>> 9212f0b01ed2a1573c52b80ae04bc537e3cd42a3

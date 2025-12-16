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

def change_page(page):
    global screen_page
    screen_page = page
    print("Change page")

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
        if screen_page == Screen.MENU.value:
            menu_screen.menu_screen(screen, language, change_page, get_page, clock)
        if screen_page == Screen.GAME.value:
            game_screen.Game_screen(screen, language, change_page, get_page, clock)
        if screen_page == Screen.OPTION.value:
            print("Option")
            change_page(Screen.MENU.value)
        if screen_page == Screen.LOBBY.value:
            create_game_screen.Create_Game_screen(screen, language, change_page, get_page, clock)

    pygame.quit()
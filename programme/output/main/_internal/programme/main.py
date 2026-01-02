import pygame
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import programme.screen.Menu_screen as menu_screen
import programme.screen.Game_screen as game_screen

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
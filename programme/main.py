import pygame
import pygame_gui
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import screen.Menu_screen as menu_screen
import screen.Game_screen as game_screen
import screen.Option_screen as option_screen
import screen.Create_Game_screen as create_game_screen

from utils.Constant import Screen
from utils.LanguageManage import LanguageManager

from utils.Read_Data import read_json

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

def resource_path(relative_path):
    """ Retourne le chemin absolu vers la ressource """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        # __file__ = main.py qui est dans programme/
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    return os.path.normpath(os.path.join(base_path, relative_path))
if __name__ == '__main__':
    # Initialisation de Pygame
    pygame.init()

    data_ = read_json(resource_path("config.json"))

    data_ = read_json(path)
    print(data_["resolution"])
    resolution_str = str(data_["resolution"]).strip("()'\"")
    largeur, hauteur = map(int, resolution_str.split('x'))
    screen = pygame.display.set_mode((largeur, hauteur))
    if data_.get("fullcreen",False):
        screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN| pygame.SCALED)

    manager = pygame_gui.UIManager(screen.get_size())

    pygame.display.set_caption("En Entreprise !")

    pygame.mixer.music.set_volume(0.5)

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
            option_screen.option_screen(screen,manager, language, change_page, get_page, clock)
        elif screen_page == Screen.LOBBY.value:
            create_game_screen.Create_Game_screen(screen, language, set_client, get_client, change_page, get_page, clock)

    pygame.quit()

import pygame
from programme.utils.Object import *

def background_screen(screen):
    pygame.init()

def game_screen_init(screen):
    global Barre_Outil
    Barre_Outil = pygame.Rect(0,screen.get_height() -80, screen.get_width(), 80)


def Game_screen(screen):

    pygame.display.set_caption("Game")
import pygame
from programme.utils.Object import *

def button_center(event):
    Start_bouton.animation_check_color(pygame.mouse.get_pos())
    Start_bouton.event(event, pygame.mouse.get_pos(), lambda: print("Start"))
    Option_bouton.animation_check_color(pygame.mouse.get_pos())
    Option_bouton.event(event, pygame.mouse.get_pos(), lambda: print("Option"))
    Quit_bouton.animation_check_color(pygame.mouse.get_pos())
    Quit_bouton.event(event, pygame.mouse.get_pos(), pygame.QUIT)

def menu_init(screen):
    global fullscreen_bouton, Start_bouton, Option_bouton, Quit_bouton
    fullscreen_bouton = Button((15, 20), pygame.image.load("src/img/Bouton_1.png"), 2, text="Fullscreen",
                               color_input='Black', color_input1='Red')
    Start_bouton = Button(((screen.get_width() / 2) - 20, (screen.get_height() / 2) - 80),
                          pygame.image.load("src/img/Bouton_1.png"), 3, text="Start", color_input='Black',
                          color_input1='Red')
    Option_bouton = Button(((screen.get_width() / 2) - 20, (screen.get_height() / 2)),
                           pygame.image.load("src/img/Bouton_1.png"), 3, text="Option", color_input='Black',
                           color_input1='Red')
    Quit_bouton = Button(((screen.get_width() / 2) - 20, (screen.get_height() / 2) + 80),
                         pygame.image.load("src/img/Bouton_1.png"), 3, text="Quit", color_input='Black',
                         color_input1='Red')

def menu_update(screen):
    Start_bouton.update(screen)
    Option_bouton.update(screen)
    Quit_bouton.update(screen)

def menu_screen(screen):
    screen.fill((146,147,147))
    for event in pygame.event.get():
        button_center(event)

    menu_update(screen)

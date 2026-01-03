import pygame
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.Object import *
import screen.popup.menu.Quit_Popup as Popup
from utils.Constant import Screen

def button_center(event, page):
    Start_bouton.animation_check_color(pygame.mouse.get_pos())
    Start_bouton.event(event, pygame.mouse.get_pos(), lambda: page(Screen.LOBBY.value))
    Option_bouton.animation_check_color(pygame.mouse.get_pos())
    Option_bouton.event(event, pygame.mouse.get_pos(), lambda: page(Screen.OPTION.value))
    Quit_bouton.animation_check_color(pygame.mouse.get_pos())
    Quit_bouton.event(event, pygame.mouse.get_pos(), popup_quit.change_active)

def menu_init(screen):
    global Start_bouton, Option_bouton, Quit_bouton
    img_boutton = pygame.image.load("src/img/util/btn_standard.png")
    Start_bouton = Button(screen,((screen.get_width() / 2) - 20, (screen.get_height() / 2) - 80),
                          img_boutton, 3,language=lg, text="menu::btn:start",
                          color_input='Black',color_input1='Red')
    Option_bouton = Button(screen,((screen.get_width() / 2) - 20, (screen.get_height() / 2)),
                           img_boutton, 3,language=lg, text="menu::btn:option",
                           color_input='Black',color_input1='Red')
    Quit_bouton = Button(screen,((screen.get_width() / 2) - 20, (screen.get_height() / 2) + 80),
                         img_boutton, 3,language=lg, text="menu::btn:exit",
                         color_input='Black',color_input1='Red')

def menu_update():
    Start_bouton.update()
    Option_bouton.update()
    Quit_bouton.update()

def evnt_fullscreen():
    global fullscreen, screen
    fullscreen = not fullscreen
    if fullscreen:
        screen = pygame.display.set_mode((800,600), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((800,600))


def menu_screen(screen,lang, pageset, pageget, clock):
    global popup_quit, lg
    menu_active=True
    lg = lang

    menu_init(screen)
    popup_quit = Popup.Quit_Popup(screen, lang, (int(screen.get_width()/2)-100, int(screen.get_height()/2)-100))

    while(menu_active):
        screen.fill((146,147,147))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if not popup_quit.get_active():
                button_center(event, pageset)
            else:
                popup_quit.event_handler(event,
                                         lambda: popup_quit.change_active(),
                                         lambda: pygame.quit())
                popup_quit.animation_check_color()
        menu_update()
        popup_quit.update()

        menu_active= pageget()==Screen.MENU.value

        clock.tick(60)
        pygame.display.flip()

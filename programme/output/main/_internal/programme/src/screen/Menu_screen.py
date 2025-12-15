from urllib.parse import scheme_chars

import pygame
from programme.Object import *
import programme.screen.popup.menu.Quit_Popup as Popup

def button_center(event, page):
    Start_bouton.animation_check_color(pygame.mouse.get_pos())
    Start_bouton.event(event, pygame.mouse.get_pos(), lambda: page(1))
    Option_bouton.animation_check_color(pygame.mouse.get_pos())
    Option_bouton.event(event, pygame.mouse.get_pos(), lambda: page(2))
    Quit_bouton.animation_check_color(pygame.mouse.get_pos())
    Quit_bouton.event(event, pygame.mouse.get_pos(), popup_quit.change_active)

def menu_init(screen):
    global fullscreen_bouton, Start_bouton, Option_bouton, Quit_bouton
    img_boutton = pygame.image.load("../programme/src/img/util/btn_standard.png")
    fullscreen_bouton = Button(screen, (15, 20), img_boutton, 1, text="Fullscreen",
                               color_input='Black', color_input1='Red')
    Start_bouton = Button(screen,((screen.get_width() / 2) - 20, (screen.get_height() / 2) - 80),
                          img_boutton, 3, text="Start", color_input='Black',
                          color_input1='Red')
    Option_bouton = Button(screen,((screen.get_width() / 2) - 20, (screen.get_height() / 2)),
                           img_boutton, 3, text="Option", color_input='Black',
                           color_input1='Red')
    Quit_bouton = Button(screen,((screen.get_width() / 2) - 20, (screen.get_height() / 2) + 80),
                         img_boutton, 3, text="Quit", color_input='Black',
                         color_input1='Red')

def menu_update():
    fullscreen_bouton.update()
    Start_bouton.update()
    Option_bouton.update()
    Quit_bouton.update()

def is_menu_kill(data):
    if data == 0:
        return True
    else:
        return False

def menu_screen(screen, pageset, pageget, clock):
    global popup_quit
    menu_active=True
    menu_init(screen)

    popup_quit = Popup.Quit_Popup(screen, (int(screen.get_width()/2)-100, int(screen.get_height()/2)-100))

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

        menu_active=is_menu_kill(pageget())

        clock.tick(60)
        pygame.display.flip()

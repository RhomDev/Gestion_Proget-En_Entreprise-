import pygame
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from programme.utils.Object import *


def create_game_screen_init(screen):
    global edit_surname, edit_ip, edit_port, edit_nb_player, btn_valide, btn_cancel, panel_background

    img_btn_std = pygame.image.load("src/img/util/btn_standard.png")

    btn_valide = Button(screen, (screen.get_width()/2,screen.get_height()/2), img_btn_std, 1, "Valide")
    btn_cancel = Button(screen, ((screen.get_width() / 2)+100, screen.get_height() / 2), img_btn_std, 1, "Cancel")


def create_game_update():
    edit_surname.update()
    edit_ip.update()
    edit_port.update()
    edit_nb_player.update()
    btn_valide.update()
    btn_cancel.update()
    panel_background.update()

def event_create_game(event, page):
    btn_valide.animation_check_color(pygame.mouse.get_pos())
    btn_valide.event(event, pygame.mouse.get_pos(), lambda : page(1))
    btn_cancel.animation_check_color(pygame.mouse.get_pos())
    btn_cancel.event(event, pygame.mouse.get_pos(), lambda: page(0))


def Create_Game_screen(screen, pageset, pageget, clock):
    game_active = True
    create_game_screen_init(screen)
    while (game_active):
        screen.fill((146, 147, 147))
        create_game_update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            event_create_game(event, pageset)

        game_active = pageget() == 2

        clock.tick(60)
        pygame.display.flip()

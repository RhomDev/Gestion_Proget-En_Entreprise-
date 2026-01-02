import pygame
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from programme.utils.Object import *


def create_game_screen_init(screen):
    global edit_surname, edit_ip, edit_port, edit_nb_player, btn_valide, btn_cancel, panel_background

        img_btn_std = pygame.image.load("src/img/util/btn_standard.png")

        btn_valide = Button(screen, (screen.get_width()/2,screen.get_heigth()/2), )


def create_game_update():
    edit_surname.update()
    edit_ip.update()
    edit_port.update()
    edit_nb_player.update()
    btn_valide.update()
    btn_cancel.update()
    panel_background.update()

def event_create_game(event):



def Create_Game_screen(screen, pageset, pageget, clock):
    game_active = True
    create_game_screen_init(screen)
    while (game_active):
        screen.fill((146, 147, 147))
        create_game_update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            event_create_game(event)

        game_active = pageget() == 2

        clock.tick(60)
        pygame.display.flip()

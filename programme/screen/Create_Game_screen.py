import pygame
import sys,os

from programme.main import change_page, set_client, set_server, get_page

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from programme.utils.Object import *
from programme.utils.Constant import Screen
from programme.Serveur import Client, Serveur

import re

def is_valid_ip(ip_string):
    # Expression régulière pour valider une adresse IPv4
    ip_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return bool(re.match(ip_pattern, ip_string)) or ip_string == "localhost"

def is_valid_port(port_string):
    try:
        port = int(port_string)
        return 0 <= port <= 65535
    except ValueError:
        return False

def create_game_screen_init(screen):
    global edit_surname, edit_ip, edit_port, edit_nb_player, btn_valide, btn_cancel, btn_server, panel_background

    img_btn_std = pygame.image.load("../programme/src/img/util/btn_standard.png")
    img_panel = pygame.image.load("../programme/src/img/game_img/background_btn_option.jpg")

    panel_background = Rectangle(screen,((screen.get_width() / 2)-200, (screen.get_height() / 2)-250), (400,500), 1, img=img_panel)

    edit_surname = InputBox(screen, lg, ((screen.get_width() / 2)-100, (screen.get_height() / 2)-200),(250,30),text_hint="loggy::edit:surname")
    edit_ip =InputBox(screen, lg, ((screen.get_width() / 2)-100, (screen.get_height() / 2)-150),(250,30),text_hint="loggy::edit:ip")
    edit_port =InputBox(screen, lg, ((screen.get_width() / 2)-100, (screen.get_height() / 2)-100),(100,30),text_hint="loggy::edit:port")
    edit_nb_player =InputBox(screen, lg, ((screen.get_width() / 2), (screen.get_height() / 2)-100),(100,30),text_hint="loggy::edit:nb_player")

    btn_valide = Button(screen, ((screen.get_width()/2)-100,screen.get_height()/2), img_btn_std, 2, lg,"loggy::btn:valid",16)
    btn_server = Button(screen, ((screen.get_width() / 2) - 100, (screen.get_height() / 2)+50), img_btn_std, 2, lg,
                        "loggy::btn:server", 16)
    btn_cancel = Button(screen, ((screen.get_width() / 2), (screen.get_height() / 2)), img_btn_std, 2,lg, "loggy::btn:cancel",16)


def create_game_update():
    panel_background.update()
    edit_surname.update()
    edit_ip.update()
    edit_port.update()
    edit_nb_player.update()
    btn_valide.update()
    btn_cancel.update()
    btn_server.update()

def create_server(page):
    if is_valid_port(edit_port.get_text()):
        serveur = Serveur(port=int(edit_port.get_text()))
        serveur.start()
        set_server(serveur)
        page(Screen.GAME.value)

def joint_server(page):
    ip = edit_ip.get_text()
    port_text = edit_port.get_text()

    if is_valid_ip(ip) and is_valid_port(port_text):
        try:
            port = int(port_text)
            set_client(Client(host=ip, port=port))
            page(Screen.GAME.value)
        except Exception as e:
            print(f"Erreur lors de la connexion au serveur : {e}")
    else:
        print("Adresse IP ou port invalide.")

def event_create_game(event,page):
    edit_surname.handle_event(event)
    edit_ip.handle_event(event)
    edit_port.handle_event(event)
    edit_nb_player.handle_event(event)

    btn_valide.animation_check_color(pygame.mouse.get_pos())
    btn_valide.event(event, pygame.mouse.get_pos(), lambda: joint_server(page))
    btn_cancel.animation_check_color(pygame.mouse.get_pos())
    btn_cancel.event(event, pygame.mouse.get_pos(), lambda: change_page(Screen.MENU))
    btn_server.animation_check_color(pygame.mouse.get_pos())
    btn_server.event(event, pygame.mouse.get_pos(), lambda: create_server(page))


def Create_Game_screen(screen,lang,page,get, clock):
    global lg
    lg = lang
    game_active = True
    create_game_screen_init(screen)
    while (game_active):
        screen.fill((146, 147, 147))
        create_game_update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            event_create_game(event,page)

        game_active = get() == Screen.LOBBY.value

        clock.tick(60)
        pygame.display.flip()

import pygame
import pygame_gui.elements as gui
import sys,os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import time

from utils.Object import *
from utils.Constant import Screen
from network.Serveur import Serveur
from network.Client import Client

from screen.popup.game.Wait_connect import Wait_Popup

from utils.Read_Data import read_json, resource_path

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

def create_game_screen_init(screen,manage):
    global edit_surname, edit_ip, edit_port, btn_valide, btn_cancel, btn_server, panel_background, \
    txt_err_msg, text_surname,text_ip,text_port

    img_btn_std = pygame.image.load(resource_path("src/img/lobby/btn_.png"))
    img_btn_std = pygame.transform.scale(img_btn_std, (400, 80))

    img_panel = pygame.image.load(resource_path("src/img/lobby/fond_lobby.png"))

    panel_background = RectangleView(screen,(200, 150), (1600, 800), 1, img=img_panel)

    text_surname = TextView(screen, (350, 250), 4,
                            "loggy::edit:surname", "White", lg)
    edit_surname = gui.UITextEntryLine(
        relative_rect=pygame.Rect((290, 270),(400,50)),
        manager=manage)

    text_ip= TextView(screen, ((screen.get_width() / 2), 250), 4,
                            "loggy::edit:ip", "White", lg)
    edit_ip = gui.UITextEntryLine(
        relative_rect=pygame.Rect(((screen.get_width() / 2)-100, 270),(400,50)),
        manager=manage)

    text_port = TextView(screen, ((screen.get_width() / 2)-50, 400), 4,
                       "loggy::edit:port", "White", lg)
    edit_port =gui.UITextEntryLine(
        relative_rect=pygame.Rect(((screen.get_width() / 2)-100, 420),(200,50)),
        manager=manage)

    txt_err_msg = TextView(screen,((screen.get_width() / 2), (screen.get_height() / 2)-50),3,"", "Red")

    btn_valide = Button(screen, ((screen.get_width()/2)+350,270), img_btn_std, 1, lg,"loggy::btn:join",
                        "White", color_input1='Red', police_taille=8)

    btn_server = Button(screen, ((screen.get_width()/2)+350,400), img_btn_std, 1, lg,
                        "loggy::btn:server", "White", color_input1='Red', police_taille=8)
    btn_cancel = Button(screen, (350, screen.get_height()-300), img_btn_std, 1, lg, "loggy::btn:cancel",
                        "White", color_input1='Red', police_taille=7)


def create_game_update():
    panel_background.update()

    text_surname.update()
    text_ip.update()
    text_port.update()

    txt_err_msg.update()

    btn_valide.update()
    btn_cancel.update()
    btn_server.update()

def create_server(set_client):
    global serveur

    try:
            port = int(edit_port.get_text())
            # Créer le serveur
            serveur = Serveur(port=port, nb_wait=int(data_config.get("nb_player",1)))
            set_client(serveur)
            serveur.start()
            time.sleep(1)
            joint_server(set_client)

    except ValueError as e:
        if data_config.get("dev_mod",False) == True:
            print("coucou")
            serveur = Serveur()
            set_client(serveur)
            serveur.start()
            time.sleep(1)
            joint_server(set_client)
        else:
            txt_err_msg.change_text(lg.get_text("lobby:error::port_input"))

    except OSError as e:
        # Erreur de création de socket (port occupé ou invalide)
        txt_err_msg.change_text(lg.get_text("lobby:error::port_fail"))
        print(f"Erreur serveur : {e}")
    except Exception as e:
        text_error = lg.get_text("lobby:error::server_fail")
        txt_err_msg.change_text(f"{text_error} : {e}")
        print(f"Erreur serveur : {e}")

def joint_server(set_client):
    ip = edit_ip.get_text()
    port_text = edit_port.get_text()
    try:
        port = int(port_text)
        client = Client(host=ip, port=port)

        set_client(client)
        time.sleep(1)
        popup_wait.set_client(client)
        popup_wait.change_active()

    except ValueError as e:
        if data_config.get("dev_mod",False) == True:
            client = Client()

            set_client(client)
            time.sleep(1)
            popup_wait.set_client(client)
            popup_wait.change_active()
        else:
            txt_err_msg.change_text(lg.get_text("lobby:error::port_input"))
    except ConnectionRefusedError:
        txt_err_msg.change_text(lg.get_text("lobby:error::client_connect"))
    except TimeoutError:
        txt_err_msg.change_text("lobby:error::client_timeout")
        print("Connexion au serveur timeout")
    except OSError as e:
        text_error = lg.get_text("lobby:error::client_error")
        txt_err_msg.change_text(f"{text_error}: {e}")
        print(f"Erreur réseau : {e}")
    except Exception as e:
        txt_err_msg.change_text(f"Erreur : {e}")
        print(f"Erreur : {e}")

def event_create_game(event,page,set_cl):
    btn_valide.animation_check_color(pygame.mouse.get_pos())
    btn_valide.event(event, pygame.mouse.get_pos(), lambda: joint_server(page,set_cl))
    btn_cancel.animation_check_color(pygame.mouse.get_pos())
    btn_cancel.event(event, pygame.mouse.get_pos(), lambda: page(Screen.MENU.value))
    btn_server.animation_check_color(pygame.mouse.get_pos())
    btn_server.event(event, pygame.mouse.get_pos(), lambda: create_server(set_cl))

def cancel_wait(client, set_client):
    global serveur
    if serveur is not None:
        serveur.stop()
        serveur = None
    else:
        client().stop()
        set_client(None)

    popup_wait.change_active()

def verif_wait(page, cl):
    if cl() is None:
        return
    data = cl().get_state()
    if data is None:
        return  # on attend encore que le serveur réponde
    wait = data["wait_nb_player"]
    new_ = data["nb_player"]
    if wait==new_:
        page(Screen.GAME.value)



def Create_Game_screen(screen,manage,lang, set_cl, get_cl,page,get, clock):
    global lg, popup_wait, serveur, data_config
    serveur=None
    data_config = read_json(resource_path("config.json"))
    lg = lang
    game_active = True
    create_game_screen_init(screen,manage)

    popup_wait = Wait_Popup(screen,lang,(int(screen.get_width()/2)-250, int(screen.get_height()/2)-100))

    while (game_active):
        screen.fill((146, 147, 147))
        time_delta = clock.tick(60) / 1000.0
        create_game_update()

        for event in pygame.event.get():
            manage.process_events(event)
            if event.type == pygame.QUIT:
                pygame.quit()
            if not popup_wait.get_active():
                event_create_game(event,page,set_cl)
            else:
                popup_wait.event_handler(event,
                                         lambda : cancel_wait(get_cl,set_cl))
                popup_wait.animation_check_color()

        if popup_wait.get_active():
            verif_wait(page, get_cl)

        game_active = get() == Screen.LOBBY.value

        popup_wait.update()

        manage.update(time_delta)
        manage.draw_ui(screen)

        clock.tick(60)
        pygame.display.flip()
    manage.get_root_container().clear()
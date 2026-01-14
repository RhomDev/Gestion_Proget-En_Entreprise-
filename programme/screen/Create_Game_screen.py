import pygame
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

def create_game_screen_init(screen):
    global edit_surname, edit_ip, edit_port, edit_nb_player, btn_valide, btn_cancel, btn_server, panel_background, \
    txt_err_msg

    img_btn_std = pygame.image.load(resource_path("src/img/util/btn_standard.png"))
    img_panel = pygame.image.load(resource_path("src/img/game_img/background_btn_option.jpg"))

    panel_background = RectangleView(screen,((screen.get_width() / 2)-200, (screen.get_height() / 2)-250), (400,500), 1, img=img_panel)

    edit_surname = InputBox(screen, lg, ((screen.get_width() / 2)-100, (screen.get_height() / 2)-200),(250,30),text_hint="loggy::edit:surname")
    edit_ip =InputBox(screen, lg, ((screen.get_width() / 2)-100, (screen.get_height() / 2)-150),(250,30),text_hint="loggy::edit:ip")
    edit_port =InputBox(screen, lg, ((screen.get_width() / 2)-100, (screen.get_height() / 2)-100),(100,30),text_hint="loggy::edit:port")
    edit_nb_player =InputBox(screen, lg, ((screen.get_width() / 2), (screen.get_height() / 2)-100),(100,30),text_hint="loggy::edit:nb_player")

    txt_err_msg = TextView(screen,((screen.get_width() / 2), (screen.get_height() / 2)-50),3,"", "Red", lg)

    btn_valide = Button(screen, ((screen.get_width()/2)-100,screen.get_height()/2), img_btn_std, 2, lg,"loggy::btn:valid", 16,
                        color_input1='Red')
    btn_server = Button(screen, ((screen.get_width() / 2) - 100, (screen.get_height() / 2)+50), img_btn_std, 2, lg,
                        "loggy::btn:server", 16, color_input1='Red')
    btn_cancel = Button(screen, ((screen.get_width() / 2), (screen.get_height() / 2)), img_btn_std, 2, lg, "loggy::btn:cancel", 16,
                        color_input1='Red')


def create_game_update():
    panel_background.update()
    edit_surname.update()
    edit_ip.update()
    edit_port.update()
    edit_nb_player.update()

    txt_err_msg.update()

    btn_valide.update()
    btn_cancel.update()
    btn_server.update()

def create_server(set_client):
    global serveur
    if 1:
        if 1:
            try:



                    port = edit_port.get_text()
                    nb_wait = edit_nb_player.get_text()
                    # Créer le serveur
                    if port == '' and nb_wait == '' :
                        port=55555
                        nb = 1
                    else:
                        port = int(port)
                        nb = int(nb_wait)

                
                    serveur = Serveur(port= port  , nb_wait= nb)

                    serveur.start()

                    time.sleep(1)

                    client = Client(port=port)
                    client.start()
                    set_client(client)

                    time.sleep(1)

                    popup_wait.set_client(client)

                    popup_wait.change_active()


            except OSError as e:
                # Erreur de création de socket (port occupé ou invalide)
                txt_err_msg.change_text(f"Erreur serveur")
                print(f"Erreur serveur : {e}")
            except Exception as e:
                txt_err_msg.change_text(f"Erreur serveur")
                print(f"Erreur serveur : {e}")
        else:
            txt_err_msg.change_text("Port invalide")
    else:
        txt_err_msg.change_text("Nombre de joueur incorrect")

def joint_server(page,set_client):
    ip = edit_ip.get_text()
    port_text = edit_port.get_text()

    if not is_valid_ip(ip):
        txt_err_msg.change_text("Adresse IP invalide")
    if not is_valid_port(port_text):
        txt_err_msg.change_text("Port invalide")
        return

    try:
        port = int(port_text)
        client = Client(host=ip, port=port)

        set_client(client)

        popup_wait.set_client(client)

        popup_wait.change_active()

    except ConnectionRefusedError:
        txt_err_msg.change_text("Connexion refusée : serveur inaccessible")
        print("Connexion refusée : serveur inaccessible")
    except TimeoutError:
        txt_err_msg.change_text("Connexion au serveur timeout")
        print("Connexion au serveur timeout")
    except OSError as e:
        txt_err_msg.change_text(f"Erreur réseau : {e}")
        print(f"Erreur réseau : {e}")
    except Exception as e:
        txt_err_msg.change_text(f"Erreur : {e}")
        print(f"Erreur : {e}")

def event_create_game(event,page,set_cl):
    edit_surname.handle_event(event)
    edit_ip.handle_event(event)
    edit_port.handle_event(event)
    edit_nb_player.handle_event(event)

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



def Create_Game_screen(screen,lang, set_cl, get_cl,page,get, clock):
    global lg, popup_wait, serveur
    serveur=None
    lg = lang
    game_active = True
    create_game_screen_init(screen)

    popup_wait = Wait_Popup(screen,lang,(int(screen.get_width()/2)-250, int(screen.get_height()/2)-100))

    while (game_active):
        screen.fill((146, 147, 147))
        create_game_update()

        for event in pygame.event.get():
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

        clock.tick(60)
        pygame.display.flip()

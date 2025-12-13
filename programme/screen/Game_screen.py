import pygame
from programme.utils.Object import *

def game_screen_init(screen):
    global panel_outil,tache_bouton,deplacement_bouton,mission_bouton,hint_panel, var_open_panel
    var_open_panel=True
    img_background_outil = pygame.image.load("src/img/game_img/background_btn_option.jpg")
    img_bouton_standard = pygame.image.load("src/img/util/btn_standard.png")
    img_hint_panel = pygame.image.load("src/img/game_img/hint_panel.png")

    img_hint_panel = pygame.transform.scale(img_hint_panel, (64,64))
    img_hint_panel = pygame.transform.rotate(img_hint_panel, 90)

    align_left = 70

    panel_outil = Rectangle(screen, (0, screen.get_height()-140),dim=(screen.get_width(), 140), img=img_background_outil, scale=1)

    tache_bouton = Button(screen, (align_left, screen.get_height()-110), img_bouton_standard, 4, text="Tache",
                          color_input='Black', color_input1='White')
    deplacement_bouton = Button(screen, (align_left + 230, screen.get_height()-110), img_bouton_standard, 4, text="Deplacement",
                                color_input='Black', color_input1='White')
    mission_bouton = Button(screen, (align_left + 230*2, screen.get_height() - 110), img_bouton_standard, 4, text="Mission",
                                color_input='Black', color_input1='White')

    hint_panel = Button(screen, (screen.get_width()-80,screen.get_height()-170), img_hint_panel,1)

def game_update():
    panel_outil.update()
    hint_panel.update()
    if var_open_panel:
        tache_bouton.update()
        deplacement_bouton.update()
        mission_bouton.update()

def close_panel():
    global var_open_panel
    var_open_panel = False
    screen = panel_outil.get_screen()

    # Tourner l'image du bouton
    img_button_hint_panel = pygame.transform.rotate(hint_panel.get_image(), 180)
    hint_panel.change_image(img_button_hint_panel)
    # Déplacer le bouton (exemple : vers le bas)
    hint_panel.change_position((hint_panel.get_position()[0], screen.get_height() - 80))

    # Changer la taille et la position du panel
    panel_outil.change_dim((panel_outil.get_rect().width, 50))
    panel_outil.change_position((0, screen.get_height() - 50))

def open_panel():
    global var_open_panel
    var_open_panel = True
    screen = panel_outil.get_screen()

    # Tourner l'image du bouton
    img_button_hint_panel = pygame.transform.rotate(hint_panel.get_image(), 180)
    hint_panel.change_image(img_button_hint_panel)
    # Déplacer le bouton (exemple : vers le haut)
    hint_panel.change_position((hint_panel.get_position()[0], screen.get_height()-170))

    # Changer la taille et la position du panel
    panel_outil.change_dim((panel_outil.get_rect().width, 140))
    panel_outil.change_position((0, screen.get_height() - 140))

def event_outil_panel(event):

    if var_open_panel:
        hint_panel.event(event, pygame.mouse.get_pos(), close_panel)
        tache_bouton.animation_check_color(pygame.mouse.get_pos())
        tache_bouton.event(event, pygame.mouse.get_pos(), lambda: print("tache"))
        deplacement_bouton.animation_check_color(pygame.mouse.get_pos())
        deplacement_bouton.event(event, pygame.mouse.get_pos(), lambda: print("deplacement"))
        mission_bouton.animation_check_color(pygame.mouse.get_pos())
        mission_bouton.event(event, pygame.mouse.get_pos(), lambda: print("mission"))
    else:
        hint_panel.event(event, pygame.mouse.get_pos(), open_panel)

def is_menu_kill(data):
    if data == 1:
        return True
    else:
        return False

def Game_screen(screen, pageset, pageget,clock):
    game_active=True
    game_screen_init(screen)
    while(game_active):
        screen.fill((35, 206, 235))
        game_update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            event_outil_panel(event)

        game_active=is_menu_kill(pageget())

        clock.tick(60)
        pygame.display.flip()
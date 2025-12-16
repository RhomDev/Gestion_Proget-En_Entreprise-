import pygame

from programme.Object import *
from programme.utils.map import *
from programme.utils.ouvrier import *


def game_screen_init(screen):
    global \
        panel_outil,tache_bouton,deplacement_bouton,mission_bouton,hint_panel,var_open_panel,bob, mapes, \
        ObjA,ObjB,ObjD,ObjC,ObjE, \
        panel_deplacement,menu_Deroulent,Up,Down
    panel_deplacement = True
    var_open_panel = True
    img_background_outil = pygame.image.load( "programme/src/img/game_img/background_btn_option.jpg")
    img_bouton_standard = pygame.image.load("programme/src/img/util/btn_standard.png")
    img_hint_panel = pygame.image.load("programme/src/img/game_img/hint_panel.png")

    img_hint_panel = pygame.transform.scale(img_hint_panel, (64, 64))
    img_hint_panel = pygame.transform.rotate(img_hint_panel, 90)

    align_left = 70
    sHeight = screen.get_height()
    sWidth = screen.get_width()
    panel_outil = Rectangle(
        screen,
        (0, sHeight - 140),
        dim=(sWidth, 140),
        img=img_background_outil,
        scale=1,
    )

    tache_bouton = Button(
        screen,
        (align_left, sHeight - 110),
        img_bouton_standard,
        4,
        text="Tache",
    )
    deplacement_bouton = Button(
        screen,
        (align_left + 230 * 2, sHeight - 110),
        img_bouton_standard,
        4,
        text="Deplacement",
    )
    mission_bouton = Button(
        screen,
        (align_left + 230, sHeight - 110),
        img_bouton_standard,
        4,
        text="Mission",
    )
    ObjA = Button(
        screen,
        (0,0),
        img_bouton_standard,
        4,
        text="Objectif A",
    )
    ObjB = Button(
        screen,
        (0,0),
        img_bouton_standard,
        4,
        text="Objectif B",
    )
    ObjD = Button(
        screen,
        (0,0),
        img_bouton_standard,
        4,
        text="Objectif D",
    )
    ObjC = Button(
        screen,
        (0,0),
        img_bouton_standard,
        4,
        text="Objectif C",
    )
    ObjE = Button(
        screen,
        (0,0),
        img_bouton_standard,
        4,
        text="Objectif E",
    )
    Up = Button(
        screen,
        (0,0),
        img_bouton_standard,
        2,
        text="↑",
        police_taille=2,
    )
    Down = Button(
        screen,
        (0,0),
        img_bouton_standard,
        2,
        text="↓",
        police_taille=2,
    )
    hint_panel = Button(screen, (sWidth - 80, sHeight - 170), img_hint_panel, 1)

    mapes = Map(screen, 1)
    bob = Ouvrier(screen, mapes)

    menu_Deroulent = Menu_Deroulent(
        [ObjA, ObjB, ObjC, ObjD, ObjE],#bouton qu'on ici
        (550, 480),(150,300),#position du coin bas gauche !! et taille du menu
        Up,#bouton up
        Down,#bouton down
        nombre_bouton_affiche=4# nmobre de boutons à afficher dans le menu
    )


def game_update():
    mapes.update()
    panel_outil.update()
    hint_panel.update()
    bob.update()

    if var_open_panel:
        tache_bouton.update()
        deplacement_bouton.update()
        mission_bouton.update()
        if panel_deplacement:
            menu_Deroulent.update()


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
    hint_panel.change_position((hint_panel.get_position()[0], screen.get_height() - 170))

    # Changer la taille et la position du panel
    panel_outil.change_dim((panel_outil.get_rect().width, 140))
    panel_outil.change_position((0, screen.get_height() - 140))


def toggle_deplacement():  # menu déroulant déplacement
    global panel_deplacement
    panel_deplacement = not panel_deplacement


def event_outil_panel(event):
    if var_open_panel:
        hint_panel.event(event, pygame.mouse.get_pos(), close_panel)
        tache_bouton.animation_check_color(pygame.mouse.get_pos())
        tache_bouton.event(event, pygame.mouse.get_pos(), lambda: print("tache"))
        if panel_deplacement:
            Up.animation_check_color(pygame.mouse.get_pos())
            Up.event(event, pygame.mouse.get_pos(), lambda: menu_Deroulent.deroule(-1))
            Down.animation_check_color(pygame.mouse.get_pos())
            Down.event(event, pygame.mouse.get_pos(), lambda: menu_Deroulent.deroule(1))
            ObjA.animation_check_color(pygame.mouse.get_pos())
            ObjA.event(event, pygame.mouse.get_pos(), lambda: bob.Set_Objectif("A"))
            ObjB.animation_check_color(pygame.mouse.get_pos())
            ObjB.event(event, pygame.mouse.get_pos(), lambda: bob.Set_Objectif("B"))
            ObjD.animation_check_color(pygame.mouse.get_pos())
            ObjD.event(event, pygame.mouse.get_pos(), lambda: bob.Set_Objectif("D"))
            ObjC.animation_check_color(pygame.mouse.get_pos())
            ObjC.event(event, pygame.mouse.get_pos(), lambda: bob.Set_Objectif("C"))
            ObjE.animation_check_color(pygame.mouse.get_pos())
            ObjE.event(event, pygame.mouse.get_pos(), lambda: bob.Set_Objectif("E"))
        deplacement_bouton.animation_check_color(pygame.mouse.get_pos())
        deplacement_bouton.event(
            event, pygame.mouse.get_pos(), lambda: toggle_deplacement()
        )
        mission_bouton.animation_check_color(pygame.mouse.get_pos())
        mission_bouton.event(event, pygame.mouse.get_pos(), lambda: print("mission"))
    else:
        hint_panel.event(event, pygame.mouse.get_pos(), open_panel)


def Game_screen(screen, pageset, pageget, clock):
    game_active = True
    game_screen_init(screen)
    while game_active:
        screen.fill((35, 206, 235))
        game_update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            event_outil_panel(event)

        game_active = pageget() == 1

        clock.tick(60)
        pygame.display.flip()

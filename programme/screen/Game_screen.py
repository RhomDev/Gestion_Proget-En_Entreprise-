
import pygame

from programme.Object import *
from programme.utils.map import *
from programme.utils.ouvrier import *
from programme.utils.Read_Data import read_json





def game_screen_init(screen):
    global \
        panel_outil,tache_bouton,deplacement_bouton,mission_bouton,hint_panel,var_open_panel,bob, mapes, \
        GoEntre,GoElectric ,GoTravail,GoMange,\
        panel_deplacement,menu_Deroulent,Up,Down,Energie,description_bouton,Stress,Menu_Liste_Attente,Menu_Mission,\
        Up_mission,Down_mission
    panel_deplacement = True
    var_open_panel = True
    img_background_outil = pygame.image.load( "programme/src/img/game_img/background_btn_option.jpg")
    img_bouton_standard = pygame.image.load("programme/src/img/util/btn_standard.png")
    img_hint_panel = pygame.image.load("programme/src/img/game_img/hint_panel.png")
    img_bar = pygame.image.load("programme/src/img/game_img/bar_life.png")

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

    desciprtion_data = read_json("programme/src/json/Description.json")
    print(desciprtion_data["GoEntrée"][1])

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
    GoEntre = Button(
        screen,
        (0,0),
        img_bouton_standard,
        4,
        text="Entrée",
        function=lambda: description_bouton_update(desciprtion_data["GoEntrée"],pos=(1563,32),dim=(300,230),police_taille=24),

    )
    GoElectric = Button(
        screen,
        (0,0),
        img_bouton_standard,
        4,
        text="Electricité",
        function=lambda: description_bouton_update(desciprtion_data["GoElectric"],pos=(1563,32),dim=(300,230),police_taille=24),

    )

    GoTravail = Button(
        screen,
        (0,0),
        img_bouton_standard,
        4,
        text="Travail",
        function=lambda: description_bouton_update(desciprtion_data["GoTravail"],pos=(1563,32),dim=(300,230),police_taille=24),

    )
    GoMange = Button(
        screen,
        (0,0),
        img_bouton_standard,
        4,
        text="Mange",
        function=lambda: description_bouton_update(desciprtion_data["GoMange"],pos=(1563,32),dim=(300,230),police_taille=24),

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
    Energie = barre_de_vie(screen, (63,15), (300,30), scale=1)
    Energie.set_value(0.25)
    Stress = barre_de_vie(screen, (63,75), (300,30), scale=1,color2=(127,0,255))
    Stress.set_value(0.60)

    description_bouton = Button(screen, (125,125),img_bouton_standard,3,text="")

    hint_panel = Button(screen, (sWidth - 80, sHeight - 170), img_hint_panel, 1)

    mapes = Map(screen, 1)
    bob = Ouvrier(screen, mapes)

    menu_Deroulent = Menu_Deroulent(
        [GoEntre, GoElectric, GoTravail, GoMange],#bouton qu'on ici
        (1650, 900),(200,400),#position du coin bas gauche !! et taille du menu
        up=Up,#bouton up
        down=Down,#bouton down
        nombre_bouton_affiche=3,# nmobre de boutons à afficher dans le menu
        police_taille=30
    )


    
    Liste_mission = Button(screen,(0,0),img_bouton_standard,1,text="Liste D'attente", police_taille=3)
    mission1 = Button(screen, (125,125),img_bouton_standard,1,text="mission1")
    mission2 = Button(screen, (125,125),img_bouton_standard,1,text="mission2")
    mission3 = Button(screen, (125,125),img_bouton_standard,1,text="mission3")
    Liste_Attente=[mission1,mission2,mission3]
    Menu_Liste_Attente= Menu_Deroulent(
        Liste_Attente,
        (63,560),(180,250),
        up=Liste_mission,
        nombre_bouton_affiche=3,
        police_taille=24
    )



    Répondre_aux_mails = Button(screen, (125,125),img_bouton_standard,1,text="Répondre aux mails") 
    Réunion_improvisée = Button(screen, (125,125),img_bouton_standard,1,text="Réunion improvisée")
    Rapport_express = Button(screen, (125,125),img_bouton_standard,1,text="Rapport express")

    Analyse_marché = Button(screen, (125,125),img_bouton_standard,1,text="Analyse marché")
    Plan_stratégique = Button(screen, (125,125),img_bouton_standard,1,text="Plan stratégique")
    Présentation_finale = Button(screen, (125,125),img_bouton_standard,1,text="Présentation finale")

    Brainstorming = Button(screen,(0,0),img_bouton_standard,1,text="Brainstorming")
    Design_prototype = Button(screen, (125,125),img_bouton_standard,1,text="Design prototype")
    Pitch_client = Button(screen, (125,125),img_bouton_standard,1,text="Pitch client")
    Up_mission = Button(screen,(0,0),img_bouton_standard,2,text="↑",police_taille=2,)
    Down_mission = Button(screen,(0,0),img_bouton_standard,2,text="↓",police_taille=2,)

    Liste_missions=[Répondre_aux_mails,Réunion_improvisée,Rapport_express,
                    Analyse_marché,Plan_stratégique,Présentation_finale,
                    Brainstorming,Design_prototype,Pitch_client]
    
    Menu_Mission=Menu_Deroulent(
        Liste_missions,
        (319, 929),(300,300),
        up=Up_mission,
        down=Down_mission,
        nombre_bouton_affiche=3,
        police_taille=30
    )


def game_update():
    mapes.update()
    panel_outil.update()
    hint_panel.update()
    bob.update()
    Energie.update()
    Stress.update()
    Menu_Liste_Attente.update()
    if var_open_panel:
        tache_bouton.update()
        deplacement_bouton.update()
        mission_bouton.update()
        if panel_deplacement:
            menu_Deroulent.update()
            Menu_Mission.update()


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

def description_bouton_update(texte,pos=(125,125),dim=(200,50),police_taille=3):
    description_bouton.change_text(texte)
    description_bouton.change_position(pos)
    description_bouton.change_dim(dim, police_taille)
    description_bouton.update()

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
            Up_mission.animation_check_color(pygame.mouse.get_pos())
            Up_mission.event(event, pygame.mouse.get_pos(), lambda: Menu_Mission.deroule(-1))
            Down_mission.animation_check_color(pygame.mouse.get_pos())
            Down_mission.event(event, pygame.mouse.get_pos(), lambda: Menu_Mission.deroule(1))
            GoEntre.animation_check_color(pygame.mouse.get_pos())
            GoEntre.event(event, pygame.mouse.get_pos(), lambda: bob.Set_Objectif("Entrée"))
            GoElectric.animation_check_color(pygame.mouse.get_pos())
            GoElectric.event(event, pygame.mouse.get_pos(), lambda: bob.Set_Objectif("Electricité"))
            GoTravail.animation_check_color(pygame.mouse.get_pos())
            GoTravail.event(event, pygame.mouse.get_pos(), lambda: bob.Set_Objectif("Travail"))
            GoMange.animation_check_color(pygame.mouse.get_pos())
            GoMange.event(event, pygame.mouse.get_pos(), lambda: bob.Set_Objectif("Mange"))
        deplacement_bouton.animation_check_color(pygame.mouse.get_pos())
        deplacement_bouton.event(event, pygame.mouse.get_pos(), lambda: toggle_deplacement())

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

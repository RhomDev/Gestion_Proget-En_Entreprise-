
import pygame

from programme.Object import *
from programme.utils.map import *
from programme.utils.ouvrier import *
from programme.utils.Read_Data import read_json





def game_screen_init(screen):
    global \
        panel_outil,tache_bouton,deplacement_bouton,mission_bouton,hint_panel,var_open_panel,bob, mapes, \
        GoEntre,GoElectric ,GoTravail,GoMange,\
        panel_deplacement,menu_Deroulent,Up,Down,Energie,description_bouton,Stress,Menu_Liste_Attente,Menu_taches,\
        Up_taches,Down_taches,panel_taches,mission1,mission2,mission3,GoEntrepot,GoMachine,liste_longeurs,Liste_Entrée,Liste_Electricité,Liste_Travail,Liste_taches
    panel_deplacement = False
    panel_taches = False
    bob_pièce = "Entrée"
    liste_longeurs = {"Entrée":"0","Electricité":"0","Travail":"0","Mange":"0","Machine":"0","Entrepôt":"0"}
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
        function=lambda: description_bouton_update(liste_longeurs["Entrée"],pos=(1450,510),dim=(200,100),police_taille=36),

    )
    GoElectric = Button(
        screen,
        (0,0),
        img_bouton_standard,
        4,
        text="Electricité",
        function=lambda: description_bouton_update(liste_longeurs["Electricité"],pos=(1450,510),dim=(200,100),police_taille=36),

    )

    GoTravail = Button(
        screen,
        (0,0),
        img_bouton_standard,
        4,
        text="Travail",
        function=lambda: description_bouton_update(liste_longeurs["Travail"],pos=(1450,510),dim=(200,100),police_taille=36),

    )
    GoMange = Button(
        screen,
        (0,0),
        img_bouton_standard,
        4,
        text="Mange",
        function=lambda: description_bouton_update(liste_longeurs["Mange"],pos=(1450,510),dim=(200,100),police_taille=36),

    )
    GoMachine = Button(
        screen,
        (0,0),
        img_bouton_standard,
        4,
        text="Machine",
        function=lambda: description_bouton_update(liste_longeurs["Machine"],pos=(1450,510),dim=(200,100),police_taille=36),
    )
    GoEntrepot = Button(
        screen,
        (0,0),
        img_bouton_standard,
        4,
        text="Entrepôt",
        function=lambda: description_bouton_update(liste_longeurs["Entrepôt"],pos=(1450,510),dim=(200,100),police_taille=36),
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
        [GoEntre, GoElectric, GoTravail, GoMange,GoMachine,GoEntrepot],#bouton qu'on ici
        (1650, 900),(200,400),#position du coin bas gauche !! et taille du menu
        up=Up,#bouton up
        down=Down,#bouton down
        nombre_bouton_affiche=3,# nmobre de boutons à afficher dans le menu
        police_taille=30
    )


    
    Liste_mission = Button(screen,(0,0),img_bouton_standard,1,text="Liste D'attente", police_taille=3)
    mission1 = Button(screen, (125,125),img_bouton_standard,1,text="mission1",function=lambda:Affiche_tache_m1.update())
    mission2 = Button(screen, (125,125),img_bouton_standard,1,text="mission2",function=lambda:Affiche_tache_m2.update())
    mission3 = Button(screen, (125,125),img_bouton_standard,1,text="mission3",function=lambda:Affiche_tache_m3.update())
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
    Up_taches = Button(screen,(0,0),img_bouton_standard,2,text="↑",police_taille=2,)
    Down_taches = Button(screen,(0,0),img_bouton_standard,2,text="↓",police_taille=2,)

    Liste_Entrée=[Répondre_aux_mails,Réunion_improvisée,Rapport_express]
    Liste_Electricité=[Analyse_marché,Plan_stratégique,Présentation_finale]
    Liste_Travail=[Brainstorming,Design_prototype,Pitch_client]


    Liste_taches=Liste_Entrée

    Menu_taches=Menu_Deroulent(
        Liste_taches,
        (63, 929),(300,260),
        up=Up_taches,
        down=Down_taches,
        nombre_bouton_affiche=3,
        police_taille=24
    )

    Tache1m1 = Button(screen, (0,0),img_bouton_standard,3,text="Tache1 m1")
    Tache2m1 = Button(screen, (0,0),img_bouton_standard,3,text="Tache2 m1")
    Tache3m1 = Button(screen, (0,0),img_bouton_standard,3,text="Tache3 m1")
    Liste_Tache_m1=[Tache1m1,Tache2m1,Tache3m1]
    Affiche_tache_m1= Menu_Deroulent(Liste_Tache_m1,(243,560),(180,250),nombre_bouton_affiche=3,police_taille=24)

    Tache1m2 = Button(screen, (0,0),img_bouton_standard,3,text="Tache1 m2")
    Tache2m2 = Button(screen, (0,0),img_bouton_standard,3,text="Tache2 m2")
    Tache3m2 = Button(screen, (0,0),img_bouton_standard,3,text="Tache3 m2")
    Liste_Tache_m2=[Tache1m2,Tache2m2,Tache3m2]
    Affiche_tache_m2= Menu_Deroulent(Liste_Tache_m2,(243,560),(180,250),nombre_bouton_affiche=3,police_taille=24)

    Tache1m3 = Button(screen, (0,0),img_bouton_standard,3,text="Tache1 m3")
    Tache2m3 = Button(screen, (0,0),img_bouton_standard,3,text="Tache2 m3")
    Tache3m3 = Button(screen, (0,0),img_bouton_standard,3,text="Tache3 m3")     
    Liste_Tache_m3=[Tache1m3,Tache2m3,Tache3m3]
    Affiche_tache_m3= Menu_Deroulent(Liste_Tache_m3,(243,560),(180,250),nombre_bouton_affiche=3,police_taille=24)

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
        if panel_taches:
            Menu_taches.update()


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
def toggle_taches():  # menu déroulant taches
    global panel_taches
    panel_taches = not panel_taches

def description_bouton_update(texte,pos=(125,125),dim=(200,50),police_taille=3, liste=None):
    if liste is None:
        description_bouton.change_text(texte)
        description_bouton.change_position(pos)
        description_bouton.change_dim(dim, police_taille)
        description_bouton.update()

def Update_Objectif(objectif,liste_longeurs):
    global bob_pièce,Liste_taches
    bob.Set_Objectif(objectif,liste_longeurs)
    bob_pièce=objectif
    if bob_pièce=="Entrée":
        Liste_taches=Liste_Entrée
    elif bob_pièce=="Electricité":
        Liste_taches=Liste_Electricité
    elif bob_pièce=="Travail":
        Liste_taches=Liste_Travail
    Menu_taches.change_liste(Liste_taches)


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
            GoEntre.animation_check_color(pygame.mouse.get_pos())
            GoEntre.event(event, pygame.mouse.get_pos(), lambda: Update_Objectif("Entrée", liste_longeurs))
            GoElectric.animation_check_color(pygame.mouse.get_pos())
            GoElectric.event(event, pygame.mouse.get_pos(), lambda: Update_Objectif("Electricité", liste_longeurs))
            GoTravail.animation_check_color(pygame.mouse.get_pos())
            GoTravail.event(event, pygame.mouse.get_pos(), lambda: Update_Objectif("Travail", liste_longeurs))
            GoMange.animation_check_color(pygame.mouse.get_pos())
            GoMange.event(event, pygame.mouse.get_pos(), lambda: Update_Objectif("Mange", liste_longeurs))
            GoMachine.animation_check_color(pygame.mouse.get_pos())
            GoMachine.event(event, pygame.mouse.get_pos(), lambda: Update_Objectif("Machine", liste_longeurs))
            GoEntrepot.animation_check_color(pygame.mouse.get_pos())
            GoEntrepot.event(event, pygame.mouse.get_pos(), lambda: Update_Objectif("Entrepôt", liste_longeurs))
        deplacement_bouton.animation_check_color(pygame.mouse.get_pos())
        deplacement_bouton.event(event, pygame.mouse.get_pos(), lambda: toggle_deplacement())

        if panel_taches:
            Up_taches.animation_check_color(pygame.mouse.get_pos())
            Up_taches.event(event, pygame.mouse.get_pos(), lambda: Menu_taches.deroule(-1))
            Down_taches.animation_check_color(pygame.mouse.get_pos())
            Down_taches.event(event, pygame.mouse.get_pos(), lambda: Menu_taches.deroule(1))
        tache_bouton.animation_check_color(pygame.mouse.get_pos())
        tache_bouton.event(event, pygame.mouse.get_pos(), lambda: toggle_taches())

        mission1.animation_check_color(pygame.mouse.get_pos())
        mission2.animation_check_color(pygame.mouse.get_pos())
        mission3.animation_check_color(pygame.mouse.get_pos())
        mission1.event(event, pygame.mouse.get_pos(), lambda: print("mission1"))
        mission2.event(event, pygame.mouse.get_pos(), lambda: print("mission2"))
        mission3.event(event, pygame.mouse.get_pos(), lambda: print("mission3"))
        
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

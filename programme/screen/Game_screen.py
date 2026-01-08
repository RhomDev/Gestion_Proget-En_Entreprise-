import pygame

from utils.Object import *
from utils.Map import *
from player.Ouvrier import *
from utils.Read_Data import read_json, write_json

from utils.Constant import Screen, Tache


def game_screen_init(screen):
    global \
        panel_outil,tache_bouton,deplacement_bouton,mission_bouton,hint_panel,var_open_panel,bob, mapes,bob_pièce, \
        liste_deplacement,\
        panel_deplacement,menu_Deroulent,Up,Down,Energie,description_bouton,Stress,Menu_Liste_Attente,Menu_taches,\
        Up_taches,Down_taches,panel_taches,mission1,mission2,mission3,liste_longeurs,Tache_par_pièce,\
        background_meca_tour,txt_N_tour, txt_heure, btn_fin_tour, img_statue,credits_restants,credit





    panel_deplacement = False
    panel_taches = False
    bob_pièce = "Entrée"
    liste_longeurs = {"Entrée":"0","Electricité":"0","Travail":"0","Mange":"0","Machine":"0","Entrepôt":"0","Dehors":"0"}
    var_open_panel = False

    img_background_outil = pygame.image.load( "src/img/game_img/background_btn_option.jpg")
    img_bouton_standard = pygame.image.load("src/img/util/btn_standard.png")
    img_hint_panel = pygame.image.load("src/img/game_img/hint_panel.png")
    img_btn_fin_tour = pygame.image.load("src/img/game_img/btn_tour.png")
    img_btn_fin_tour = pygame.transform.scale(img_btn_fin_tour, (450, 70))
    img_bar = pygame.image.load("src/img/game_img/bar_life.png")

    img_hint_panel = pygame.transform.scale(img_hint_panel, (64, 64))
    img_hint_panel = pygame.transform.rotate(img_hint_panel, 90)

    align_left = 70
    sHeight = screen.get_height()
    sWidth = screen.get_width()
    panel_outil = RectangleView(
        screen,
        (0, sHeight - 140),
        dim=(sWidth, 140),
        img=img_background_outil,
        scale=1,
    )
    credits_restants = 100

    credit = Button(
        screen,(1400, 24),img_bouton_standard,4,
        text=f"Crédits: {credits_restants}",)
    
# Bouton option
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


    # Bouton Déplacement

    liste_deplacement=[]
    for key in liste_longeurs:
            btn = Button(
                    screen,
                    (0,0),
                    img_bouton_standard,
                    4,
                    text=key,
                    function=lambda: description_bouton_update(liste_longeurs[key],pos=(1450,510),dim=(200,100),police_taille=36),
                )
            liste_deplacement.append(btn)


    Up = Button(screen,(0,0),img_bouton_standard,2,text="↑",police_taille=2,)
    Down = Button(screen,(0,0),img_bouton_standard,2,text="↓",police_taille=2,)

    menu_Deroulent = Menu_Deroulent(
        liste_deplacement,#bouton qu'on ici
        (1650, 900),(200,400),#position du coin bas gauche !! et taille du menu
        up=Up,#bouton up
        down=Down,#bouton down
        nombre_bouton_affiche=3,# nmobre de boutons à afficher dans le menu
        police_taille=30
    )

    



# Barre
    Energie = barre_de_vie(screen, (63,15), (300,30), scale=1)
    Energie.set_value(0.25)
    Stress = barre_de_vie(screen, (63,75), (300,30), scale=1,color2=(127,0,255))
    Stress.set_value(0.60)

    description_bouton = Button(screen, (125,125),img_bouton_standard,3,text="")

    hint_panel = Button(screen, (sWidth - 80, sHeight - 170), img_hint_panel, 1)

    mapes = Map(screen, 1)
    bob = Ouvrier(screen, mapes)




    
    Liste_mission = Button(screen,(0,0),img_bouton_standard,1,text="Liste D'attente", police_taille=3)
    mission1 = Button(screen, (125,125),img_bouton_standard,1,text="mission1",function=lambda:Affiche_tache_m1.update())
    mission2 = Button(screen, (125,125),img_bouton_standard,1,text="mission2",function=lambda:Affiche_tache_m2.update())
    mission3 = Button(screen, (125,125),img_bouton_standard,1,text="mission3",function=lambda:Affiche_tache_m3.update())
    Liste_Attente=[mission1,mission2,mission3]

    Menu_Liste_Attente= Menu_Deroulent(
        Liste_Attente,
        (63,475),(180,360),
        up=Liste_mission,
        nombre_bouton_affiche=3,
        police_taille=24
    )


# Bouton Tache

    Up_taches = Button(screen,(0,0),img_bouton_standard,2,text="↑",police_taille=2,)
    Down_taches = Button(screen,(0,0),img_bouton_standard,2,text="↓",police_taille=2,)
    
    def init_tache(pièce):
            data_tache = read_json("src/data/tache/info.json")[pièce]
            Liste_tache = []
            for key in data_tache:
                crédit = str(data_tache[key][1]) + " crédits"
                btn = Button(screen,(0,0),img_bouton_standard,1,text=data_tache[key][0], language=lg , police_taille=2,
                                function=lambda credit = crédit: description_bouton_update(credit,pos=(283,700),dim=(200,100),police_taille=36),argument=data_tache[key][1])
                Liste_tache.append(btn)
            return Liste_tache
    

    Tache_par_pièce={
        "Entrée":[],
        "Electricité":init_tache("electricite"),
        "Travail":init_tache("travail"),
        "Machine":init_tache("machine"),
        "Entrepôt":init_tache("reception"),
        "Mange":init_tache("reunion"),
        "Dehors":init_tache("dehors"),
    }



    Menu_taches=Menu_Deroulent(
        Tache_par_pièce[bob_pièce],
        (71, 680),(200,180),
        up=Up_taches,
        down=Down_taches,
        nombre_bouton_affiche=3,
        police_taille=50
    )

    Tache1m1 = Button(screen, (0,0),img_bouton_standard,3,text="Tache1 m1")
    Tache2m1 = Button(screen, (0,0),img_bouton_standard,3,text="Tache2 m1")
    Tache3m1 = Button(screen, (0,0),img_bouton_standard,3,text="Tache3 m1")
    Liste_Tache_m1=[Tache1m1,Tache2m1,Tache3m1]
    Affiche_tache_m1= Menu_Deroulent(Liste_Tache_m1,(243,475),(180,360),nombre_bouton_affiche=3,police_taille=24)

    Tache1m2 = Button(screen, (0,0),img_bouton_standard,3,text="Tache1 m2")
    Tache2m2 = Button(screen, (0,0),img_bouton_standard,3,text="Tache2 m2")
    Tache3m2 = Button(screen, (0,0),img_bouton_standard,3,text="Tache3 m2")
    Liste_Tache_m2=[Tache1m2,Tache2m2,Tache3m2]
    Affiche_tache_m2= Menu_Deroulent(Liste_Tache_m2,(243,475),(180,360),nombre_bouton_affiche=3,police_taille=24)
    Tache1m3 = Button(screen, (0,0),img_bouton_standard,3,text="Tache1 m3")
    Tache2m3 = Button(screen, (0,0),img_bouton_standard,3,text="Tache2 m3")
    Tache3m3 = Button(screen, (0,0),img_bouton_standard,3,text="Tache3 m3")     
    Liste_Tache_m3=[Tache1m3,Tache2m3,Tache3m3]
    Affiche_tache_m3= Menu_Deroulent(Liste_Tache_m3,(243,475),(180,360),nombre_bouton_affiche=3,police_taille=24)

    # system tour

    background_meca_tour = ImageView(screen, (sWidth - 300,sHeight - 90),0.6,
                                     "src/img/game_img/background_meca_tour.png")
    img_statue = ImageView(screen, (sWidth - 300,sHeight - 130),0.8,"src/img/game_img/statue/statue_loading.png")
    txt_N_tour = TextView(screen, (sWidth - 420,sHeight - 90),1,"0 tour","Black",police=20)
    txt_heure = TextView(screen, (sWidth - 200,sHeight - 90), 1, "00:00", "Black",police=20)

    btn_fin_tour = Button(screen, (sWidth - 525,sHeight - 70),img_btn_fin_tour,1,text="Fin de tour (60/60)",police_taille=4)

def game_update():
    data = cl.get_state()

    mapes.update()
    panel_outil.update()
    credit.update()
    if data["statue"]==1:
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

        img_statue.update()
        background_meca_tour.update()
        txt = data["tour"]
        txt_N_tour.change_text(f"{txt} tours")
        txt_N_tour.update()
        txt_heure.update()
        btn_fin_tour.update()

def close_panel():
    print("close")
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
    print("open")
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
    print(texte)
    if liste is None:
        description_bouton.change_text(texte)
        description_bouton.change_position(pos)
        description_bouton.change_dim(dim, police_taille)
        description_bouton.update()

def Update_Objectif(objectif,liste_longeurs):
    global bob_pièce,Tache_par_pièce

    bob.Set_Objectif(objectif,liste_longeurs)
    bob_pièce=objectif
    Menu_taches.change_liste(Tache_par_pièce[bob_pièce])

def fin_tour(client):
    client().send_end_turn()

def update_credits(montant):
    global credits_restants
    credits_restants += montant
    credit.change_text(f"Crédits: {credits_restants}")
    credit.update()

def event_outil_panel(event, client):
    global var_open_panel, panel_deplacement, panel_taches,bob_pièce
    print(bob_pièce)
    def event_check(btn,function):
        btn.animation_check_color(pygame.mouse.get_pos())
        btn.event(event, pygame.mouse.get_pos(), function)

    if var_open_panel:
        hint_panel.event(event, pygame.mouse.get_pos(), close_panel)
        event_check(tache_bouton,lambda:print("tache"))    

        if panel_deplacement:
            event_check(Up,lambda: menu_Deroulent.deroule(-1))
            event_check(Down,lambda: menu_Deroulent.deroule(1))
            for btn in liste_deplacement:
                event_check( btn,lambda: cl.send_action(btn._input_text))
        event_check(deplacement_bouton, lambda: toggle_deplacement())
        

        if panel_taches:
            event_check(Up_taches,lambda: Menu_taches.deroule(-1))
            event_check(Down_taches,lambda: Menu_taches.deroule(1))
            for btn in Tache_par_pièce[bob_pièce]:
                event_check( btn,lambda credit_amount = btn.argument: update_credits(-credit_amount) )
        event_check(tache_bouton, lambda: toggle_taches())

        event_check(btn_fin_tour,fin_tour)
        
        mission1.animation_check_color(pygame.mouse.get_pos())
        mission2.animation_check_color(pygame.mouse.get_pos())
        mission3.animation_check_color(pygame.mouse.get_pos())
        mission1.event(event, pygame.mouse.get_pos(), lambda: print("mission1"))
        mission2.event(event, pygame.mouse.get_pos(), lambda: print("mission2"))
        mission3.event(event, pygame.mouse.get_pos(), lambda: print("mission3"))
        
    else:
        hint_panel.event(event, pygame.mouse.get_pos(), open_panel)

def loading_animation_serveur(client):
    global var_open_panel
    if client().get_state()["statue"] != 1 and var_open_panel:
        close_panel()
    if client().get_state()["action_realisee"] != "":
        act = client().get_state()["action_realisee"]
        Update_Objectif(act, liste_longeurs)
        client().send_animation_done()



def Game_screen(screen,language, client, pageset, pageget, clock):
    global lg, loading, cl
    lg = language
    cl = client()
    loading = True
    game_active = True
    game_screen_init(screen)
    while game_active:
        screen.fill((35, 206, 235))
        game_update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            event_outil_panel(event, client)

        game_active = pageget() == Screen.GAME.value

        loading_animation_serveur(client)

        clock.tick(60)
        pygame.display.flip()

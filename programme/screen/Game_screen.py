import random



from utils.Object import *
from utils.Map import *
from player.Ouvrier import *
from utils.Read_Data import read_json, write_json, resource_path
from popup.End_game.Game_Over import *
from utils.Constant import Screen, Tache


def game_screen_init(screen):
    global \
        panel_outil,tache_bouton,deplacement_bouton,mission_bouton,hint_panel,var_open_panel,bob, mapes,bob_piece, \
        liste_deplacement,\
        panel_deplacement,menu_Deroulent,Up,Down,description_bouton,Stress,Menu_Liste_Attente,Menu_taches,\
        Up_taches,Down_taches,panel_taches,list_mission_btn,Tache_par_pièce,\
        background_meca_tour,txt_N_tour, txt_heure, btn_fin_tour, img_statue,credits_restants,credit,i_btn,credit_effet,data_tache_effet,Burnout_bar,\
        credit_bonus,piece_ferme,btn_affiche_effet,event_tache_effet,bonus_next_task,ecran,tache_a_faire,btn_tache_a_faire,Event_sound

    panel_deplacement = False
    panel_taches = False
    Event_sound = pygame.mixer.Sound(resource_path("src/sound/event.mp3"))
    data_tache_effet = read_json(resource_path("src/data/tache_effet.json"))
    event_tache_effet = read_json(resource_path("src/data/event_effet.json"))
    var_open_panel = True
    piece_ferme = [[],[],[],[],[]]
    credit_bonus = [0,0,0,0,0]
    ecran = screen
    tache_a_faire = ""
    btn_tache_a_faire = Button(screen,(397, 33),pygame.image.load(resource_path("src/img/util/btn_standard.png")),4,taille=(400,200),text="",police_taille=1)

    bonus_next_task = 0
    img_background_outil = pygame.image.load(resource_path( "src/img/game_img/background_btn_option.jpg"))
    img_bouton_standard = pygame.image.load(resource_path("src/img/util/btn_standard.png"))
    img_hint_panel = pygame.image.load(resource_path("src/img/game_img/hint_panel.png"))
    img_bar = pygame.image.load(resource_path("src/img/game_img/bar.png"))
    img_btn_fin_tour = pygame.image.load(resource_path("src/img/game_img/btn_tour.png"))
    img_btn_fin_tour = pygame.transform.scale(img_btn_fin_tour, (450, 70))
    img_description = pygame.image.load(resource_path("src/img/util/btn_standard.png"))

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
    credits_restants = credit_init
    credit_effet = 0
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
    i_btn = {}
    liste_deplacement=[]
    for i,key in enumerate(liste_longeurs):

            btn = Button(
                    screen,
                    (0,0),
                    img_bouton_standard,
                    4,
                    text=key,
                    function=lambda clé=key: description_bouton_update(liste_longeurs[clé],pos=(1450,510),dim=(200,100),police_taille=36),
                )
            liste_deplacement.append(btn)
            i_btn[key]=i





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
    img_description = pygame.image.load(resource_path("src/img/game_img/btn_tour.png"))

    Burnout_bar = barre_de_vie(screen, (39,80), (160,120),image=img_bar, scale_img=2 , scale=1.8)
    Burnout_bar.set_value(0)

    description_bouton = Button(screen, (125,125),img_description,3,text="")

    hint_panel = Button(screen, (sWidth - 80, sHeight - 170), img_hint_panel, 1)

    mapes = Map(screen, 1)
    bob = Ouvrier(screen, mapes)

# Mission + Tache a faire
    Menu_Liste_Attente,list_mission_btn = print_mission(screen,missions)

# Bouton Tache

    Up_taches = Button(screen,(0,0),img_bouton_standard,2,text="↑",police_taille=2,)
    Down_taches = Button(screen,(0,0),img_bouton_standard,2,text="↓",police_taille=2,)

    def init_tache(piece):
            data_tache = read_json(resource_path("src/data/tache_effet.json"))[piece]
            Liste_tache = []
            for tache in data_tache:
                task = data_tache[tache] 
                credit_in = str(task["credit"]) + " crédits"
                text= credit_in +"\n"+ task.get("Description", "")
                print("DESCRIPTION TACHE:", text)
                btn = Button(screen,(0,0),img_bouton_standard,1,text=tache , police_taille=2,
                                function=lambda texts = text: description_bouton_update(texts,pos=(287, 588),dim=(300,320),police_taille=36),argument=[task["credit"],task,piece])
                Liste_tache.append(btn)
            return Liste_tache


    Tache_par_pièce={
        "Entrée":[],
        "Electricité":init_tache("Electricité"),
        "Info":init_tache("Info"),
        "Machine":init_tache("Machine"),
        "Entrepôt":init_tache("Entrepôt"),
        "Reception":init_tache("Reception"),
        "Dehors":init_tache("Dehors"),
    }
    Menu_taches=Menu_Deroulent(
        Tache_par_pièce[bob_piece],
        (71, 680),(200,180),
        up=Up_taches,
        down=Down_taches,
        nombre_bouton_affiche=3,
        police_taille=50
    )

    # system tour

    background_meca_tour = ImageView(screen, (sWidth - 300,sHeight - 90),0.6,
                                     resource_path("src/img/game_img/background_meca_tour.png"))
    img_statue = ImageView(screen, (sWidth - 300,sHeight - 130),0.8,resource_path("src/img/game_img/statue/statue_loading.png"))
    txt_N_tour = TextView(screen, (sWidth - 420,sHeight - 90),1,"0 tour","Black",police=20)
    txt_heure = TextView(screen, (sWidth - 200,sHeight - 90), 1, "00:00", "Black",police=20)

    btn_fin_tour = Button(screen, (sWidth - 525,sHeight - 70),img_btn_fin_tour,1,text=f"Fin de tour ({credits_restants}/{credit_init})",police_taille=4)

    btn_affiche_effet = Button(screen, (sWidth - 350,70),img_description,3,text=f"",police_taille=1,taille=(300,130))

def print_mission(screen, list):
    print_list_tache_a_faire = []
    for mission in list:
        list_tache_a_faire = []
        for i, task in enumerate(mission):
            list_tache_a_faire.append(
                TextView(screen, (0, 0), 1, task, "Green" if i == 0 else "Black", police=20)
            )
        print_list_tache_a_faire.append(None if len(list_tache_a_faire)==0 else
            Menu_Deroulent(list_tache_a_faire, (243, 475), (180, 360), nombre_bouton_affiche=len(list_tache_a_faire),
                           police_taille=24))
    list_mission_btn=[]

    for i, list in enumerate(print_list_tache_a_faire):
        print(list)
        list_mission_btn.append(TextView(screen, (125,125),1,f"mission {i}","Green" if list is None else "Black" ,function= list if list is None else lambda l = list :l.update(),police=20))
    return Menu_Deroulent(list_mission_btn,(63,475),(180,360),nombre_bouton_affiche=3,police_taille=24),list_mission_btn

#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def game_update():
    data = cl.get_state()
    #print(data)
    mapes.update()
    panel_outil.update()
    if data["statue"]==1:
        hint_panel.update()
    bob.update()
    Burnout_bar.update()
    Menu_Liste_Attente.update()
    btn_affiche_effet.update()
    if tache_a_faire != "":
        btn_tache_a_faire.change_text(f"Tâche à faire:\n{tache_a_faire}")
        btn_tache_a_faire.update()
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

def Update_Objectif(objectif):
    global bob_piece,Tache_par_pièce,tache_bouton
    if objectif == "Reception":
        tache_bouton.blocked = False
        toggle_taches()
        for btn in liste_deplacement:
            btn.blocked = False
            #print("Désactivation du bouton:", btn.get_text())

    bob.Set_Objectif(objectif,liste_longeurs)
    bob_piece=objectif
    Menu_taches.change_liste(Tache_par_pièce[bob_piece])

def fin_tour():
    global  credit_effet
    credit_effet = 0
    cl.send_end_turn()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def event_outil_panel(event, client):
    global var_open_panel, panel_deplacement, panel_taches,bob_piece

    def event_check(btn,function,functions=[]):
        btn.animation_check_color(pygame.mouse.get_pos())
        btn.event(event, pygame.mouse.get_pos(), function)
        for func in functions:
            btn.event_right(event, pygame.mouse.get_pos(), func)

    if var_open_panel:
        hint_panel.event(event, pygame.mouse.get_pos(), close_panel)
        event_check(tache_bouton,lambda:print("tache"))

        if panel_deplacement:
            event_check(Up,lambda: menu_Deroulent.deroule(-1))
            event_check(Down,lambda: menu_Deroulent.deroule(1))
            for btn in liste_deplacement:

                credit_depense = int(liste_longeurs[btn._input_text])+credit_effet
                if credit_depense < 0:
                    credit_depense = 0

                if credit_depense > credits_restants or btn.piece_ferme or btn.blocked:
                    btn.set_input_color1("Gray")
                else:
                    btn.set_input_color1("White")
                    btn.event(event, pygame.mouse.get_pos(), lambda : client().send_action(btn.get_text()))

                btn.animation_check_color(pygame.mouse.get_pos())
        event_check(deplacement_bouton, lambda: toggle_deplacement())


        if panel_taches:
            event_check(Up_taches,lambda: Menu_taches.deroule(-1))
            event_check(Down_taches,lambda: Menu_taches.deroule(1))
            for btn in Tache_par_pièce[bob_piece]:
                credit_depense = btn.argument[0]+credit_effet+bonus_next_task
                if credit_depense < 0:
                    credit_depense = 0
                if credit_depense > credits_restants or btn.blocked:
                    btn.set_input_color1("Gray")
                else:
                    btn.set_input_color1("White")

                    btn.event(event, pygame.mouse.get_pos(), lambda: client().send_task(btn.get_text()))

                btn.animation_check_color(pygame.mouse.get_pos())
        event_check(tache_bouton, lambda: toggle_taches())

        event_check(btn_fin_tour, fin_tour)

    for mission_btn in list_mission_btn:
        mission_btn.animation_check_color(pygame.mouse.get_pos())

    else:
        hint_panel.event(event, pygame.mouse.get_pos(), open_panel)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def loading_animation_serveur(screen, client):
    global var_open_panel,credits_restants,credit_effet,Burnout_bar,data_tache_effet,missions,Menu_Liste_Attente,list_mission_btn, next_turn,tour_act,btn_affiche_effet,\
            bonus_next_task,tache_a_faire
    burnout=0
    if client().get_state()["tour"] != tour_act:
        init_next_tour()
        tour_act=client().get_state()["tour"]
    if client().get_state()["statue"] != 1 and var_open_panel:
        close_panel()
    if client().get_state()["action_realisee"] != "":
        act = client().get_state()["action_realisee"]
        if client().get_state()["statue"]  == 1:

            credit_depense = int(liste_longeurs[act]) + 0 if int(liste_longeurs[act]) else credit_effet
            print("credit depense",credit_depense)
            if credit_depense < 0:
                credit_depense = 0

            credits_restants -=  credit_depense
            if credits_restants <0:
                credits_restants = 0

        Update_Objectif(act)
        client().get_state()["action_realisee"] = ""
        client().send_animation_done()


    if client().get_state()["tache_realisee"]:
        tache = client().get_state()["tache_realisee"]
        if tache_a_faire == tache:
            tache_a_faire = ""
        fait = client().get_state()["mission_faite"]
        for mission in missions:
            if len(mission) > 0:
                if mission[0]==tache:
                    fait.append(tache)
                    mission.remove(tache)
        Menu_Liste_Attente,list_mission_btn = print_mission(screen, missions)

        if client().get_state()["statue"] == 1:
            text_ = btn_fin_tour.get_text()
            credits_ = int(text_.split("(")[1].split("/")[0])
            credit_depense = 0
            if bob_piece != "Entrée" and tache[0:5] != "Event":
                credit_depense = data_tache_effet[bob_piece][tache]["credit"] + credit_effet + bonus_next_task

            if credit_depense < 0:
                credit_depense = 0

            credits_restants = credits_ - credit_depense
            if credits_restants <0:
                credits_restants = 0
        bonus_next_task = 0
        executer_effets_tache(bob_piece, tache)
        btn_affiche_effet.change_text(tache)

        client().get_state()["tache_realisee"] = ""
        

        client().send_animation_done([missions,fait])

    btn_fin_tour.change_text(f"Fin de tour ({credits_restants}/{credit_init})")
#-----------------------------------------------------------------------------------------------------------------------------------------------------------
def init_game():
    bob.Set_Objectif("Entrée",liste_longeurs)
    Menu_taches.change_liste(Tache_par_pièce["Entrée"])

def tirage_taches():
    data_tache = read_json("src/data/tache_effet.json")
    result =[]
    for i in range(3):
        lieu = random.choice(list(data_tache.keys()))

        code_tache = random.choice(list(data_tache[lieu].keys()))
        result.append(code_tache)
    return result

def Game_screen(screen,language, client, pageset, pageget, clock):
    global lg, loading, cl, credit_init, liste_longeurs,bob_piece, missions, tour_act , Burnout_bar
    lg = language
    bob_piece = "Entrée"
    tour_fin = read_json(resource_path("config.json")).get("nb_tour",40)

    liste_longeurs = {"Entrée": "0", "Electricité": "0", "Info": "0", "Reception": "0", "Machine": "0", "Entrepôt": "0",
                      "Dehors": "0"}

    missions = []
    for i in range(3):
        missions.append(tirage_taches())

    pygame.mixer.music.load(resource_path("src/sound/music_fond_low_burnout.wav"))
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

    tour_act = 0
    credit_init = 100
    cl = client()
    loading = True
    game_active = True

    client().send_loading_mission(missions,[])

    game_screen_init(screen)
    init_game()
    while game_active:
        screen.fill((35, 206, 235))
        game_update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            event_outil_panel(event, client)

        game_active = pageget() == Screen.GAME.value
        #print("GAME ACTIVE :", game_active)
        Is_Game_Over(Burnout_bar,pageset, tour_fin, client)
        loading_animation_serveur(screen,client)

        clock.tick(60)
        pygame.display.flip()

#Regarde si game over

def Is_Game_Over(burnout,pageset, tour, client):
    if burnout.value > 1 or client().get_state().get("tour",0)>=tour:
        pygame.mixer.music.stop()
        burnout.value = 0
        pageset(5)


# TOUT LES FONCTION D EFFET UTILE DU JEU , J'ai préféré les mettre la que de creer un fichier car il y a des probleme avec les variable global, comme tu disai ----------------------------------------------------------

def credit_effets(credit,tour):
    global credit_bonus
    for i in range(tour):
        if len(credit_bonus) > i+1:
            credit_bonus[i] += credit
        else:
            credit_bonus.append(credit)

def ferme_piece(piece,tour):
        global piece_ferme

        for n in range(tour):
            if len(piece_ferme) > n+1:
                for p in piece:
                    if p not in piece_ferme[n]:
                        piece_ferme[n].append(p)
            else:
                piece_ferme.append(piece)

def effet_credit(credit):
    global credit_effet
    credit_effet = credit


def init_next_tour():#les effets qui ce update en fonction des tours
    global credits_restants,liste_deplacement,i_btn, piece_ferme, credit_bonus,event_tache_effet,tache_a_faire

    if tache_a_faire != "":
        tache_a_faire = ""
        credit_effets(-20, 1)

    credits_restants=credit_init
    debloque_toutes_pieces()

    if len(credit_bonus)>0:
        bonus = credit_bonus[0]
        credits_restants+=bonus
        credit_bonus.remove(bonus)

    if len(piece_ferme)>0:
        for i in range(len(piece_ferme[0])):
            for btn_piece in liste_deplacement:
                if btn_piece._input_text in piece_ferme[0][i]:
                    print("Piece en question : ", piece_ferme[i])
                    btn_piece.piece_ferme = True
        piece_ferme.remove(piece_ferme[0])

    print("CREDIT BONUS:",credit_bonus)

    a=[0,0,1] #une chance sur 3 d'avoir un evenement
    if random.choice(a):
        event =random.choice(list(event_tache_effet.keys()))
        cl.send_task(event)




def executer_effets_tache(piece, nom_tache):
    global data_tache_effet,bob,event_tache_effet,Burnout_bar,liste_deplacement,Even
    data_tache = data_tache_effet
    burnout = 0




    if nom_tache[0:5] == "Event":

        Event_sound.play()
        Event_sound.set_volume(0.35)
        event = event_tache_effet[nom_tache]
        effets = event.get('effets', [])
        burnout = event.get('burnout', 0)
        #print("BOURNOUT EVENT :", burnout)


    else:

        piece = data_tache.get(piece, {})
        tache = piece.get(nom_tache, {})
        effets = tache.get('effets', [])
        burnout = tache.get('burnout', 0)
        bob.anim()
        #print("BOURNOUT TACHE:", burnout)





    burnout = Burnout_bar.value +burnout/100
    if burnout < 0:
        burnout = 0
    Burnout_bar.set_value(burnout)

    
    for effet in effets:
        fonction = effet.get('fonction')
        print("FONCTION EFFET:", fonction)

        if fonction == 'ferme_piece':
            pieces = effet.get('piece', [])
            duree = effet.get('duree', 1)
            ferme_piece(pieces, duree)

        elif fonction == 'effet_credit':
            # Modif credit pour ce tour
            argument = effet.get('argument', 0)
            effet_credit(argument)

        elif fonction == 'credit_effets':
            #Modif credit pour les prochain tour
            argument = effet.get('argument', 0)
            duree = effet.get('duree', 1)
            #print("ARGUMENT CREDIT EFFET:", argument, duree)
            credit_effets(argument, duree)

        elif fonction == 'debloque_piece':
            # Débloquer toutes les pièces
            debloque_toutes_pieces()

        elif fonction == "fin_tour":
            fin_tour()

        elif fonction == "Go_Reception":
            #print("EXECUTION Go_Reception")
            Go_Reception()

        elif fonction == "bloque_piece":
            piece = random.choice(liste_deplacement)
            piece.piece_ferme = True
        
        elif fonction == "bonus_next_task":
            global bonus_next_task
            argument = effet.get('argument', 0)
            bonus_next_task += argument
        
        elif fonction == "Ajout_Tache":
            ajout_tache()
        
        elif fonction == "Ajout_Tache_Prioritaire":
            global tache_a_faire
            tache_a_faire = tirage_taches()[0]


def ajout_tache():
    global ecran,Menu_Liste_Attente,list_mission_btn,missions
    fait = cl.get_state()["mission_faite"] #marche pas trop
    for mission in missions:

        if len(mission) < 3:
            tache = tirage_taches()[0]
            mission.append(tache)
    Menu_Liste_Attente,list_mission_btn = print_mission(ecran, missions)
    cl.send_animation_done([missions,fait])

def Go_Reception():
    global tache_bouton,panel_taches
    tache_bouton.blocked = True
    if panel_taches:
        toggle_taches()

    for btn in liste_deplacement:
        if btn.get_text() != "Reception":
            btn.blocked = True
            #print("Désactivation du bouton:", btn.get_text())



def debloque_toutes_pieces():
    """Débloque toutes les pièces fermées"""
    for btn_piece in liste_deplacement:
        btn_piece.piece_ferme = False

    #print("Toutes les pièces ont été débloquées")

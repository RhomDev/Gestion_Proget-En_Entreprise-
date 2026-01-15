from math import sqrt,floor
import pygame

from utils.Read_Data import resource_path


class Ouvrier:
    def __init__(s, fenetre,  map):
        s.state = 0
        s.etat = ["Fixe", "Cour", "Anim"]
        s.image = pygame.image.load("src/img/perso/homme.png")
        s.width_image, s.heigth_image = s.image.get_size()[0] // 3, s.image.get_size()[1] // 3
        s.img_anim = pygame.image.load("src/img/perso/bob_anim.png")
        s.width_anim, s.heigth_anim = s.img_anim.get_size()[0] // 3, s.img_anim.get_size()[1]
        s.image_flip = pygame.transform.flip(s.image, True, False)
        s.flip = 0
        s.fenetre = fenetre
        s.width = fenetre.get_size()[0]
        s.heigth = fenetre.get_size()[1]
        s.centre = (s.width / 2, s.heigth / 2)
        s.walk_sound = pygame.mixer.Sound(resource_path("src/sound/walk.wav"))

        s.i = 0
        s.k = 0
        s.frame = 0
        s.scale = 0.6
        s.map = map

        s.nodes = map.nodes
        s.objectif = "EntréeBis"
        s.dest = map.nodes.noeuds[s.objectif].data
        s.node = map.nodes.EntreeBis
        s.pose = s.node.data
        s.obj = s.pose

    def get_Longueur(s, objectif):
        return s.nodes.liste_longueur_chemin(s.nodes.noeuds[objectif])

    def Set_Objectif(s, objectif,liste_longeurs):
        print(objectif)
        s.walk_sound.play(-1)
        liste_longeurs_int = s.nodes.liste_longueur_chemin(s.nodes.noeuds[objectif])
        for key in liste_longeurs_int:
            liste_longeurs[key] = str(int(liste_longeurs_int[key]/5)*5)
        print(liste_longeurs)
        bool = s.nodes.Chemin(objectif, s.node.name)
        if bool:
            s.obj = s.node.pointe.data
            s.objectif = objectif
            s.dest = s.nodes.noeuds[objectif].data

    def Draw(s):
        k = s.k
        i = s.i
        state = s.state
        s.k = (k + 1) % (60 * 5 * 3)
        s.i = k // 4
        position = [s.pose[0] - 50, s.pose[1] - 100]

        images = [s.image, s.image_flip]

        if s.etat[state] == "Cour":
            img = images[s.flip].subsurface(((i % 3) * s.width_image, s.width_image, s.width_image, s.heigth_image))
            image_scale = pygame.transform.scale_by(img, s.scale)
            s.fenetre.blit(image_scale, position)
        elif s.etat[state] == "Fixe":
            img = images[0].subsurface((0, 0, s.width_image, s.heigth_image))
            image_scale = pygame.transform.scale_by(img, s.scale)
            s.fenetre.blit(image_scale, position)
        elif s.etat[state] == "Anim":
            img = s.img_anim.subsurface( ( (i % 2) * s.width_anim, 0, s.width_anim, s.heigth_anim ) )
            image_scale = pygame.transform.scale_by(img, 1.5)
            position = [s.pose[0]-45, s.pose[1]-180]
            s.fenetre.blit(image_scale, position)
            s.frame = s.frame + 1
            if s.frame > 60:
                s.frame = 0
                s.state = 0
 


    def Position(s):
            if pygame.mouse.get_pressed()[0]:
               print(pygame.mouse.get_pos())

            x = s.obj[0] - s.pose[0]
            y = s.obj[1] - s.pose[1]
            norm = sqrt(x**2 + y**2)
            if norm == 0:
                if s.state != 2:
                    s.state = 0
                return
            x = x / norm
            y = y / norm

            s.state = 1
            vitesse = 5

            s.pose[0] = s.pose[0] + x * vitesse
            s.pose[1] = s.pose[1] + y * vitesse

            if norm < vitesse + 1:
                if s.node.name == s.objectif or s.node is None:
                    s.pose[0] = s.obj[0]
                    s.pose[1] = s.obj[1]
                    if s.state != 2:
                        print("Arrivé à l'objectif :", s.objectif)
                        s.walk_sound.stop()
                        s.state = 0
                else:
                    if s.node.pointe is not None:
                        s.node = s.node.pointe
                    else:
                        s.node.pointe = s.dest
                    s.obj = s.node.data

            s.flip = 1 if x < 0 else 0

    def anim(s):
        s.state = 2
                



    def update(s):
        s.Draw()
        s.Position()

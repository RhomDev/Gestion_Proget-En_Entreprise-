from math import sqrt


import pygame



class Ouvrier:
    def __init__(s, fenetre, position, map):
        s.state = 0
        s.etat = ["Fixe", "Cour"]
        s.image = pygame.image.load("programme/src/img/perso/homme.bmp")
        s.image_flip = pygame.transform.flip(s.image, True, False)
        s.flip = 0
        s.fenetre = fenetre
        s.width = fenetre.get_size()[0]
        s.heigth = fenetre.get_size()[1]
        s.centre = (s.width / 2, s.heigth / 2)

        s.i = 0
        s.k = 0

        s.scale = 0.6
        s.map = map

        s.nodes = map.nodes
        s.objectif = "AB"
        s.dest = map.nodes.noeuds[s.objectif].data
        s.node = map.nodes.ab
        print(s.node.data)
        s.pose = s.node.data
        s.obj = s.pose


    def Set_Objectif(s, objectif):
        bool = s.nodes.Chemin(objectif, s.node.name)
        if bool:
            s.obj = s.node.pointe.data
            s.objectif = objectif
            s.dest = s.nodes.noeuds[objectif].data
           # print("Objectif :", s.node.data, s.pose)
           # print("A star Bouton")
            k = s.node
            while k is not None:
                #print(k.name)
                k = k.pointe

    def Draw(s):
        k = s.k
        i = s.i
        state = s.state
        s.k = (k + 1) % (60 * 5 * 3)
        s.i = k // 4
        position = [s.pose[0] - 50, s.pose[1] - 100]

        images = [s.image, s.image_flip]

        if s.etat[state] == "Cour":
            img = images[s.flip].subsurface(((i % 8) * 128, 0, 120, 160))
            image_scale = pygame.transform.scale_by(img, s.scale)
            s.fenetre.blit(image_scale, position)
        elif s.etat[state] == "Fixe":
            img = images[0].subsurface((128 * 3, 163 * 2, 128, 160))
            image_scale = pygame.transform.scale_by(img, s.scale)
            s.fenetre.blit(image_scale, position)

    def Position(s):

        if (
            s.pose[0] != s.obj[0]
            or s.pose[1] != s.obj[1]
        ):
            x = s.obj[0] - s.pose[0]
            y = s.obj[1] - s.pose[1]
            norm = sqrt(x**2 + y**2)
            if norm !=0:
                x = x / norm
                y = y / norm
            else :
                x,y= 0,0
            s.state = 1
            vitesse = 5

            s.pose[0] = s.pose[0] + x * vitesse
            s.pose[1] = s.pose[1] + y * vitesse

            if norm < vitesse + 1:
                print("Noeud Position", s.node.name, "objectif =", s.objectif, s.dest)
                if s.node.name == s.objectif or s.node is None:
                    s.pose[0] = s.obj[0]
                    s.pose[1] = s.obj[1]
                    s.state = 0
                else:
                    if s.node.pointe is not None:
                       # print("here")
                        s.node = s.node.pointe
                        s.obj = s.node.data
                    else:
                       # print("here 2")
                        s.node.pointe = s.dest
                        s.obj = s.node.data

            if x < 0:
                s.flip = 1
            else:
                s.flip = 0

    def update(s):
        s.Draw()
        s.Position()

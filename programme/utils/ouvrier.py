from math import sqrt

import pygame


class Ouvrier:
    def __init__(s, fenetre, objectif, map):
        s.state = 0
        s.etat = ["Fixe", "Cour"]
        s.image = pygame.image.load("programme/src/img/perso/homme.bmp")
        s.image_flip = pygame.transform.flip(s.image, True, False)
        s.flip = 0
        s.fenetre = fenetre
        s.width = fenetre.get_size()[0]
        s.heigth = fenetre.get_size()[1]
        s.centre = (s.width / 2, s.heigth / 2)
        s.pose = [s.centre[0], s.centre[1]]
        s.i = 0
        s.k = 0
        s.obj = s.pose
        s.objectif = objectif
        s.scale = 0.6
        s.node = map.nodes.a
        s.dest = map.nodes.noeuds[objectif]

    def Set_Objectif(s, objectif):
        s.objectif = objectif
        s.dest = map.nodes.noeuds[objectif]

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
        s.obj = s.node.data

        if s.pose[0] != s.obj[0] and s.pose[1] != s.obj[1]:
            x = s.obj[0] - s.pose[0]
            y = s.obj[1] - s.pose[1]
            norm = sqrt(x**2 + y**2)
            x = x / norm
            y = y / norm
            s.state = 1
            vitesse = 10

            s.pose[0] = s.pose[0] + x * vitesse
            s.pose[1] = s.pose[1] + y * vitesse

            if norm < vitesse + 1:
                if s.node.name == s.objectif:
                    s.pose[0] = s.obj[0]
                    s.pose[1] = s.obj[1]
                    s.state = 0
                else:
                    s.node = s.node.nexte(s.dest)

            if x < 0:
                s.flip = 1
            else:
                s.flip = 0

    def update(s):
        s.Draw()
        s.Position()

from math import sqrt
from utils.Read_Data import resource_path

import pygame


def dist(n1, n2):
    x, y = n1.data[0], n1.data[1]
    x1, y1 = n2.data[0], n2.data[1]
    return sqrt((x - x1) ** 2 + (y - y1) ** 2)




class Map:
    def __init__(s, screen, choix):
        s.screen = screen
        s.resolution = (s.screen.get_width(), s.screen.get_height())
        s.image = pygame.image.load(resource_path(f"src/img/map/map{choix}.png"))
        s.image = pygame.transform.scale(s.image, s.resolution)
        s.nodes = Nodes()

    def Draw(s):
        s.screen.blit(s.image, (0, 0))

    def Set_Map(s, choix):
        s.image = pygame.image.load(resource_path(f"src/img/map/map{choix}.png"))
        s.image = pygame.transform.scale(s.image, s.resolution)

    def update(s):
        s.Draw()


class Node:
    def __init__(s, data, name):
        s.name = name
        s.data = data
        s.lien = []
        s.pointe = None
        s.score = 1000000
        s.visited = False


class Nodes:
    def __init__(s):
        s.EntreeBis = Node([1294, 655], "EntréeBis")
        s.Entree    = Node([1293, 654], "Entrée")
        s.a         = Node([1390, 555], "A")
        s.electric  = Node([1563, 372], "Electricité")
        s.b         = Node([1042, 406], "B")
        s.mange     = Node([1134, 264], "Mange")
        s.ba        = Node([885,  328], "BA")          
        s.travail   = Node([752,  393], "Travail")
        s.c         = Node([986, 690], "C")
        s.ca1       = Node([998, 790], "CA1")
        s.ca2       = Node([896, 680], "CA2")
        s.cb2       = Node([718, 762], "CB2")
        s.machine   = Node([636, 712], "Machine")
        s.entrepot  = Node([887, 871], "Entrepôt")
        s.dehors    = Node([1462, 756], "Dehors")
        s.objectifs = {"Entrée":0,"Electricité":0,"Travail":0,"Mange":0,"Machine":0,"Entrepôt":0,"Dehors":0}
        s.noeuds = {
            "EntréeBis": s.EntreeBis, "Entrée": s.Entree,
            "A": s.a, "Electricité": s.electric, "B": s.b,
            "Mange": s.mange, "BA": s.ba, "Travail": s.travail,
            "C": s.c, "CA1": s.ca1, "CA2": s.ca2, "CB2": s.cb2,
            "Machine": s.machine, "Entrepôt": s.entrepot,"Dehors":s.dehors
        }


        def link(u, v):
            u.lien.append(v)
            v.lien.append(u)


        link(s.EntreeBis, s.Entree)

        link(s.Entree, s.a)
        link(s.Entree, s.b)
        link(s.Entree, s.c)
        link(s.Entree, s.ca1)
        link(s.Entree, s.dehors)

        link(s.a, s.b)
        link(s.a, s.c)
        link(s.a, s.electric)
        link(s.a, s.ca2)

        link(s.b, s.c)
        link(s.b, s.mange)
        link(s.b, s.ba)
        link(s.b, s.ca2)

        link(s.ba, s.travail)

        link(s.c, s.ca1)
        link(s.c, s.ca2)

        link(s.ca1, s.entrepot)

        link(s.ca2, s.cb2)

        link(s.cb2, s.machine)




    def Chemin(s, deb, fin):
        if deb == fin:
            return 0
        for nod in s.noeuds.values():
            nod.score = 100000
            nod.visited = False
            nod.pointe = None
        start = s.noeuds[deb]
        end = s.noeuds[fin]
        priorité = {0: start}
        start.score = 0
        while 1:
            a = next(iter(sorted(priorité)))

            noeud = priorité[a]  
            #print("Noeud : ", noeud.name)
            sup = priorité.pop(a)
            noeud.visited = True
            for i in noeud.lien:
                if i.name == fin:
                    end.pointe = noeud
                    return 1
                score = noeud.score + dist(noeud, i)
                if i.score > score and not i.visited:
                    i.score = score
                    i.pointe = noeud
                    priority = int(score + dist(i, end))
                    priorité[priority] = i

    def longueur_chemin(s, deb, fin):
        length = 0
        current = s.noeuds[fin.name]
        while current.name != deb.name:
            length += dist(current, current.pointe)
            current = current.pointe
        return length

    def liste_longueur_chemin(s, deb):
        for fin in s.objectifs:
            nod = s.noeuds[fin]
            bool = s.Chemin(deb.name, nod.name)
            if bool:
                s.objectifs[fin] = round(s.longueur_chemin(deb, nod)*30/1000)
            else:
                s.objectifs[fin] = 0
        return s.objectifs
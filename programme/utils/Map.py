from math import sqrt
from tkinter.constants import FALSE, TRUE

import pygame


def dist(n1, n2):
    x, y = n1.data[0], n1.data[1]
    x1, y1 = n2.data[0], n2.data[1]
    return sqrt((x - x1) ** 2 + (y - y1) ** 2)




class Map:
    def __init__(s, screen, choix):
        s.screen = screen
        s.resolution = (s.screen.get_width(), s.screen.get_height())
        s.image = pygame.image.load(f"src/img/map/map{choix}.png")
        s.image = pygame.transform.scale(s.image, s.resolution)
        s.nodes = Nodes()

    def Draw(s):
        s.screen.blit(s.image, (0, 0))

    def Set_Map(s, choix):
        s.image = pygame.image.load(f"src/img/map/map{choix}.png")
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
        s.visited = FALSE


class Nodes:
    def __init__(s):
        s.EntreeBis = Node([1294,655], "EntréeBis")
        s.Entree = Node([1293,654], "Entrée")
        s.a = Node([1390,555], "A")
        s.electric = Node([1563, 372], "Electricité")
        s.b = Node([1042, 406], "B")
        s.mange = Node([1134, 264], "Mange")
        s.ba = Node([885, 328], "BA")
        s.travail = Node([752, 393], "Travail")

        s.noeuds = {"EntréeBis": s.EntreeBis, "Entrée":s.Entree,
                    "A": s.a, "Electricité": s.electric,"B": s.b, "Mange": s.mange, "BA": s.ba, "Travail": s.travail}

        s.EntreeBis.lien.append(s.Entree)
        s.Entree.lien.append(s.EntreeBis)
        s.Entree.lien.append(s.a)
        s.a.lien.append(s.Entree)
        s.a.lien.append(s.electric)
        s.electric.lien.append(s.a)

        s.Entree.lien.append(s.b)
        s.b.lien.append(s.Entree)
        s.b.lien.append(s.mange)
        s.mange.lien.append(s.b)
        s.b.lien.append(s.ba)
        s.ba.lien.append(s.b)
        s.ba.lien.append(s.travail)
        s.travail.lien.append(s.ba)




    def Chemin(s, deb, fin):
        if deb == fin:
            return 0
        for nod in s.noeuds.values():
            nod.score = 100000
            nod.visited = FALSE
            nod.pointe = None
        start = s.noeuds[deb]
        end = s.noeuds[fin]
        priorité = {0: start}
        start.score = 0
        while 1:
            a = next(iter(sorted(priorité)))

            noeud = priorité[a]  # prend l'élément avec la plus petite priorité
            #print("Noeud : ", noeud.name)
            sup = priorité.pop(a)
            noeud.visited = TRUE
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

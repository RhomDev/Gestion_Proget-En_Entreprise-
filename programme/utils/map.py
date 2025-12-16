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
        s.image = pygame.image.load(f"programme/src/img/map/map{choix}.png")
        s.image = pygame.transform.scale(s.image, s.resolution)
        s.nodes = Nodes()

    def Draw(s):
        s.screen.blit(s.image, (0, 0))

    def Set_Map(s, choix):
        s.image = pygame.image.load(f"programme/src/img/map/map{choix}.png")
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
        s.ab = Node([167, 159], "AB")
        s.a = Node([162, 159], "A")
        s.b = Node([167, 292], "B")
        s.c = Node([354, 292], "C")
        s.e = Node([420, 292], "E")
        s.d = Node([357, 244], "D")
        s.noeuds = {"AB":s.ab,"A": s.a, "B": s.b, "C": s.c, "D": s.d, "E": s.e}

        s.ab.lien.append(s.a)
        s.a.lien.append(s.ab)
        s.a.lien.append(s.b)
        s.b.lien.append(s.a)
        s.b.lien.append(s.c)
        s.c.lien.append(s.b)
        s.c.lien.append(s.d)
        s.d.lien.append(s.c)

        s.e.lien.append(s.c)
        s.c.lien.append(s.e)

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
            print("Noeud : ", noeud.name)
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

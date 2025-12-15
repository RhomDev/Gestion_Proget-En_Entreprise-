from math import sqrt
from tkinter.constants import FALSE, TRUE

import pygame


def dist(x, y, x1, y1):
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
        s.next = []
        s.visited = FALSE

    def nexte(s, obj):
        min = 1000000
        k = -1
        s.visited = TRUE
        for i in range(len(s.next)):
            nod = s.next[i]
            print(s.name, nod.name, nod.visited)
            if not nod.visited:
                x, y = nod.data[0], nod.data[1]
                distance = dist(x, y, obj[0], obj[1])

                if obj[0] == x and obj[1] == y:
                    return s.next[i]
                if distance < min:
                    k = i
        print("return :", s.name, s.next[k].name)
        return s.next[k]


class Nodes:
    def __init__(s):
        s.a = Node([167, 159], "A")
        s.b = Node([167, 292], "B")
        s.c = Node([354, 292], "C")
        s.d = Node([357, 244], "D")
        s.noeuds = {"A": s.a, "B": s.b, "C": s.c, "D": s.d}

        s.a.next.append(s.b)
        s.b.next.append(s.a)
        s.b.next.append(s.c)
        s.c.next.append(s.b)
        s.c.next.append(s.d)
        s.d.next.append(s.c)

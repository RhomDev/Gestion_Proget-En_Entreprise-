from math import sqrt

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

    def nexte(s, obj):
        min = 1000000
        k = None
        for i in range(len(s.next)):
            nod = s.next[i]
            x, y = nod.data[0], nod.data[1]
            distance = dist(x, y, obj[0], obj[1])
            print(distance, nod.name, nod.data, obj)
            if obj[0] == x and obj[1] == y:
                return s.next[i]
            if distance < min:
                k = i
        return s.next[k]


class Nodes:
    def __init__(s):
        s.noeuds = {"A": (167, 159), "B": (167, 292), "C": (354, 292), "D": (357, 244)}
        s.a = Node((167, 159), "A")
        s.b = Node((167, 292), "B")
        s.c = Node((354, 292), "C")
        s.d = Node((357, 244), "D")

        s.a.next.append(s.b)
        s.b.next.append(s.a)
        s.b.next.append(s.c)
        s.c.next.append(s.d)
        s.c.next.append(s.b)
        s.d.next.append(s.c)

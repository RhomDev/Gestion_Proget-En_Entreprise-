import pygame
from math import *


class Ouvrier:
    def __init__(self, nom, fenetre):
        self.nom = nom
        self.state = 0
        self.etat = ["Fixe", "Cour"]
        self.image = pygame.image.load("image/homme.bmp")
        self.fenetre = fenetre
        self.width = fenetre.get_size()[0]
        self.heigth = fenetre.get_size()[1]
        self.centre = (self.width / 2, self.heigth / 2)
        self.pose = [self.centre[0], self.centre[1]]
        self.i = 0
        self.k = 0

    def Draw(self):
        k = self.k
        i = self.i
        state = self.state
        self.k = (k + 1) % (60 * 5 * 3)
        self.i = k // 10
        position = [self.pose[0] - 50, self.pose[1] - 100]
        if self.etat[state] == "Cour":
            self.fenetre.blit(self.image, position, ((i % 8) * 128, 0, 120, 160))
        elif self.etat[state] == "Fixe":
            self.fenetre.blit(self.image, position, (128 * 3, 163 * 2, 128, 160))

    def Position(self, obj):
        if self.pose[0] != obj[0] and self.pose[1] != obj[1]:
            x = obj[0] - self.pose[0]
            y = obj[1] - self.pose[1]
            norm = sqrt(x**2 + y**2)
            x = x / norm
            y = y / norm
            self.state = 1
            vitesse = 10

            self.pose[0] = self.pose[0] + x * vitesse
            self.pose[1] = self.pose[1] + y * vitesse

            if norm < vitesse + 1:
                self.pose[0] = obj[0]
                self.pose[1] = obj[1]
                self.state = 0

    def update(self, obj):
        self.Draw()
        self.Position(obj)

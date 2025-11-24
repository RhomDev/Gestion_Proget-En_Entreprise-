import pygame
from math import *


class Ouvrier:
    def __init__(self, nom, fenetre):
        self.nom = nom
        self.state = 0

        self.image = pygame.image.load("image/pngegg.bmp")
        self.image_surf = pygame.Surface((670, 550))
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
        self.k = (k + 1) % (60 * 5 * 3)
        self.i = k // 20
        position = [self.pose[0] - 50, self.pose[1] - 100]
        self.fenetre.blit(
            self.image, position, ((i % 5) * 138, ((i // 5) % 3) * 200, 100, 200)
        )

    def update(self, obj):
        self.Draw()
        if self.pose[0] != obj[0] and self.pose[1] != obj[1]:
            x = obj[0] - self.pose[0]
            y = obj[1] - self.pose[1]
            norm = sqrt(x**2 + y**2)
            x = x / norm
            y = y / norm

            vitesse = 10

            self.pose[0] = self.pose[0] + x * vitesse
            self.pose[1] = self.pose[1] + y * vitesse

            if norm < vitesse + 1:
                self.pose[0] = obj[0]
                self.pose[1] = obj[1]

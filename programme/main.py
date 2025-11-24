import pygame
from Object import *

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("En Entreprise !")
main_font = pygame.font.SysFont('freesansbold.ttf',32)
get_info(screen, main_font)



text_test = TextView((0,0),(2,2), "bonjour", (0,0,0))

while True:

    text_test.update()

    pygame.display.update()


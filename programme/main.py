import pygame

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mon Jeu Pygame pour Android")

# Couleurs
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Position initiale du carré
x, y = WIDTH // 2, HEIGHT // 2
speed = 5

# Boucle principale
running = True
clock = pygame.time.Clock()

while running:
    print(pygame.key.get_pressed())
    for event in pygame.event.get():
        print(pygame.key.get_pressed())

pygame.quit()


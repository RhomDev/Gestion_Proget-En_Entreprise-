import pygame
from Object import Button, TextView

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("En Entreprise !")

# Police
main_font = pygame.font.SysFont('freesansbold.ttf', 32)

# Exemple d'utilisation de TextView
text_test = TextView(screen, main_font, (400, 300), 1, "Bonjour", (0, 0, 0))
text_test.set_inter_actif(True)  # Active l'interaction

# Boucle principale
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            # Met à jour la couleur du texte si la souris est dessus
            text_test.animation_check_color(event.pos)

    # Mise à jour de l'affichage
    screen.fill((255, 255, 255))  # Efface l'écran
    text_test.update()
    pygame.display.update()
    clock.tick(60)

pygame.quit()

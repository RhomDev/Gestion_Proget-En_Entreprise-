import pygame
from Object import Button, TextView

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("En Entreprise !")
# Exemple d'utilisation de TextView

#text_test.set_inter_actif(True)  # Active l'interaction
fullscreen_bouton = Button((15, 20), pygame.image.load("src/img/Bouton_1.png"), 2, text="Fullscreen", color_input='Black', color_input1='Red')
Start_bouton = Button(((screen.get_width()/2)-20, (screen.get_height()/2)-80), pygame.image.load("src/img/Bouton_1.png"), 3, text="Start", color_input='Black', color_input1='Red')
Option_bouton = Button(((screen.get_width()/2)-20, (screen.get_height()/2)), pygame.image.load("src/img/Bouton_1.png"), 3, text="Option", color_input='Black', color_input1='Red')
Quit_bouton = Button(((screen.get_width()/2)-20, (screen.get_height()/2)+80), pygame.image.load("src/img/Bouton_1.png"), 3, text="Quit", color_input='Black', color_input1='Red')

# Boucle principale
running = True
fullscreen = False
clock = pygame.time.Clock()

def update():
    screen.fill((255, 255, 255))
    fullscreen_bouton.update(screen)
    Start_bouton.update(screen)
    Option_bouton.update(screen)
    Quit_bouton.update(screen)
    pygame.display.update()

def evnt_fullscreen():
    global fullscreen, screen
    fullscreen = not fullscreen
    if fullscreen:
        screen = pygame.display.set_mode((800,600), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((800,600))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        fullscreen_bouton.animation_check_color(pygame.mouse.get_pos())
        fullscreen_bouton.event(event,pygame.mouse.get_pos(), pygame.display.toggle_fullscreen)

        Start_bouton.animation_check_color(pygame.mouse.get_pos())
        Start_bouton.event(event, pygame.mouse.get_pos(), pygame.display.toggle_fullscreen)
        Option_bouton.animation_check_color(pygame.mouse.get_pos())
        Option_bouton.event(event, pygame.mouse.get_pos(), pygame.display.toggle_fullscreen)
        Quit_bouton.animation_check_color(pygame.mouse.get_pos())
        Quit_bouton.event(event, pygame.mouse.get_pos(), pygame.QUIT)


    update()
    clock.tick(60)

pygame.quit()

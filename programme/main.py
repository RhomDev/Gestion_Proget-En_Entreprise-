import pygame
import programme.screen.Menu_screen as menu_screen
import programme.screen.Game_screen as game_screen

def evnt_fullscreen():
    global fullscreen, screen
    fullscreen = not fullscreen
    if fullscreen:
        screen = pygame.display.set_mode((800,600), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((800,600))

if __name__ == '__main__':
    # Initialisation de Pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("En Entreprise !")

    menu_screen.menu_init(screen)

    # Boucle principale
    running = True
    fullscreen = False
    screen_page = 0
    clock = pygame.time.Clock()

    while running:
        if screen_page == 0:
            menu_screen.menu_screen(screen)
        if screen_page == 1:
            game_screen.Game_screen(screen)
        clock.tick(60)
        pygame.display.flip()

    pygame.quit()



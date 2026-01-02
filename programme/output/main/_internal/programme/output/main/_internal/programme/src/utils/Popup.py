import pygame

class Popup:
    def __init__(self,screen):
        self.screen = screen
        self.active = False

        background_color = (70, 70, 70)
        background_alpha = 200

        self.rect_surface = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
        self.rect_surface.fill((*background_color, background_alpha))  # Remplir avec la couleur et l'alpha

    def update(self):
        self.screen.blit(self.rect_surface, (0,0))

    def get_active(self):
        return self.active
    def change_active(self):
        self.active = not self.active